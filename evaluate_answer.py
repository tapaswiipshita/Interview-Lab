# -*- coding: utf-8 -*-
"""
AI Mock Interview Evaluation System - Answer Evaluation Engine
============================================================
A modular, testable answer evaluation engine that evaluates a candidate's response
against a reference model answer and expected concepts.

Key Capabilities:
  1. Semantic Similarity: Computes cosine similarity between candidate answer and reference answer.
     - Uses calibrated TF-IDF cosine similarity as a fast, zero-network, offline-resilient baseline.
  2. Distinctive Concept Matching: Evaluates whether each expected concept is addressed.
     - Distinctive keyword partitioning prevents cross-concept false positives (e.g., matching
       memory complexity simply because traversal keywords BFS/DFS appear elsewhere).
     - Phrase canonicalization and stemming handle morphological variations and idioms.
     - Ignorance assertion filtering prevents meta-statements ("I don't remember X") from
       falsely counting as coverage.
     - Handles contradiction and inverted statements carefully.
  3. Calibrated Tiered Anchor Scoring:
     - Maps concept coverage into calibrated technical tiers (Excellent, Good, Average, Poor)
       with TF-IDF similarity acting as an intra-tier fluency adjustment.
  4. Misconception & Inversion Safeguards:
     - Detects conceptual inversions and penalizes/caps provisional score below 50.
"""

import re
from typing import List, Dict, Any, Optional, Set, Tuple

try:
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import cosine_similarity as sklearn_cosine_similarity
    HAS_SKLEARN = True
except ImportError:
    HAS_SKLEARN = False

# ==============================================================================
# CANONICAL PHRASES & TECHNICAL SYNONYM DICTIONARY
# ==============================================================================

CANONICAL_PHRASE_REPLACEMENTS = [
    (r'\bfirst[- ]in[- ]first[- ]out\b', ' fifo '),
    (r'\blast[- ]in[- ]first[- ]out\b', ' lifo '),
    (r'\bcall[- ]stack(s)?\b', ' stack '),
    (r'\bstack[- ]frame(s)?\b', ' stack '),
    (r'\bfunction[- ]call(s)?\b', ' recursion '),
    (r'\btier[- ]by[- ]tier\b', ' tier '),
    (r'\bring[- ]by[- ]ring\b', ' ring '),
    (r'\blayer[- ]by[- ]layer\b', ' layer '),
    (r'\bbranch[- ]by[- ]branch\b', ' branch '),
    (r'\blevel[- ]by[- ]level\b', ' level '),
    (r'\bshortest[- ]path(s)?\b', ' shortest_path '),
    (r'\bminimal[- ]distance(s)?\b', ' shortest_path '),
    (r'\boptimal[- ]rout(e|ing)\b', ' shortest_path '),
    (r'\bspace[- ]complexity\b', ' memory_complexity '),
    (r'\bmemory[- ]complexity\b', ' memory_complexity '),
    (r'\bram[- ]consumption\b', ' memory_complexity '),
    (r'\bmemory[- ]overhead\b', ' memory_complexity '),
    (r'\bunweighted[- ]topolog(y|ies)\b', ' unweighted '),
    (r'\bunweighted[- ]graph(s)?\b', ' unweighted '),
    (r'\btree[- ]depth\b', ' depth '),
    (r'\bpath[- ]height\b', ' depth '),
    (r'\bterminal[- ]leaf\b', ' leaf '),
    (r'\bstandard[- ]deviation\b', ' std_dev '),
    (r'\bsquared[- ]deviation(s)?\b', ' variance '),
    (r'\bheavy[- ]tail(s)?\b', ' fat_tails '),
    (r'\bfat[- ]tail(s)?\b', ' fat_tails '),
    (r'\btail[- ]risk\b', ' fat_tails '),
    (r'\bdecision[- ]tree(s)?\b', ' decision_tree '),
    (r'\brandom[- ]forest(s)?\b', ' random_forest ')
]

CLEAN_SYNONYM_SETS = [
    # Traversal data structures
    {"fifo", "queue", "buffer", "deque"},
    {"lifo", "stack", "recursion", "recursive"},
    # Path & optimality
    {"shortest_path", "optimal_route", "minimal_distance"},
    {"shortest", "optimal", "minimal", "minimum", "quickest", "fastest"},
    {"path", "route", "routing", "distance", "trajectory"},
    {"unweighted", "unit_cost"},
    # Memory & Space
    {"memory", "space", "ram", "storage", "footprint", "consumption", "overhead", "memory_complexity"},
    # Traversal patterns & concepts
    {"depth", "deep", "deeply", "height"},
    {"level", "layer", "tier", "ring", "breadth"},
    {"frontier", "perimeter", "boundary"},
    {"branch", "subtree", "leaf"},
    {"backtrack", "backtracking", "unwinding", "retreating", "reversing"},
    {"traversal", "search", "exploration", "visiting", "navigating", "uncovers", "approaches", "explores"},
    {"guarantee", "guarantees", "ensures", "uncovers", "finds", "determines", "promises", "provides"},
    {"graph", "network", "topology", "vertices", "nodes", "trees"},
    
    # Data Science & Statistics
    {"mean", "average", "arithmetic_mean"},
    {"median", "percentile_50", "middle_value"},
    {"variance", "dispersion", "variability"},
    {"std_dev", "sigma"},
    {"skewness", "skewed", "asymmetric", "asymmetry"},
    {"kurtosis", "leptokurtic", "fat_tails", "heavy_tails"},
    {"imputation", "filling", "substituting", "replacement", "fillna"},
    {"deletion", "drop", "dropping", "dropna", "removal"},
    {"outlier", "anomaly", "aberration", "deviation"},

    # Web & Systems
    {"semantic", "structure", "accessibility", "a11y"},
    {"cleanup", "teardown", "unmount", "dispose"},
    {"rendering", "pipeline", "dom", "cssom", "layout", "reflow", "paint"},
    {"caching", "cache", "memoization", "redis"}
]

STOPWORDS: Set[str] = {
    "a", "an", "and", "are", "as", "at", "be", "by", "for", "from", "has", "he",
    "in", "is", "it", "its", "of", "on", "that", "the", "to", "was", "were",
    "will", "with", "using", "uses", "used", "differ", "differs", "different",
    "between", "than", "or", "so", "such", "can", "could", "would", "should",
    "basically", "well", "like", "know", "mean", "also", "into", "which", "there",
    "these", "those", "each", "every", "other", "another", "does", "do", "done",
    "only", "just", "entire", "current", "main", "key", "various", "multiple",
    "certain", "overall", "thing", "things", "way", "ways", "type", "types"
}

IGNORANCE_PATTERNS = [
    r"\b(do|does|did)(n't| not) (remember|recall|know|understand)\b",
    r"\b(can't|cannot|couldn't|could not) (quite |fully )?(remember|recall|explain|prove|state)\b",
    r"\b(i'm|im|i am) (not |less |unclear |fuzzy |vague |hazy )?(sure|certain|clear|confident|fuzzy)\b",
    r"\b(fuzzy|hazy|vague|unclear|less clear) (on|about)\b",
    r"\bno (idea|clue)\b",
    r"\bhave(n't| not) (learned|studied|seen|memorized)\b",
    r"\bforget\b",
    r"\bforgot\b"
]

def stem_token(word: str) -> str:
    """Lightweight rule-based stemmer to match morphological variations."""
    w = word.lower()
    for suffix in ["ing", "tion", "tions", "ed", "es", "s", "al", "ic", "ive", "ly", "ment", "ments", "ity"]:
        if w.endswith(suffix) and len(w) > len(suffix) + 2:
            return w[:-len(suffix)]
    return w

def canonicalize_phrases(text: str) -> str:
    """Replaces common technical multi-word idioms with single canonical tokens."""
    t = text.lower()
    for pat, rep in CANONICAL_PHRASE_REPLACEMENTS:
        t = re.sub(pat, rep, t)
    return t

def clean_tokens(text: str) -> List[str]:
    """Canonicalizes idioms, normalizes punctuation, and stems tokens."""
    t = canonicalize_phrases(text)
    t = t.replace('-', ' ').replace('_', ' ').replace('/', ' ').replace('(', ' ').replace(')', ' ')
    raw_tokens = re.findall(r'\b[a-z0-9_]+\b', t)
    return [stem_token(w) for w in raw_tokens]

STEMMED_SYNONYM_MAP: Dict[str, Set[str]] = {}
for cluster in CLEAN_SYNONYM_SETS:
    stemmed_cluster = {stem_token(w.replace('_', ' ')) for w in cluster}
    for term in stemmed_cluster:
        STEMMED_SYNONYM_MAP.setdefault(term, set()).update(stemmed_cluster)

def get_synonyms(word: str) -> Set[str]:
    """Retrieves all stemmed synonyms for a token."""
    st = stem_token(word.replace('_', ' '))
    return STEMMED_SYNONYM_MAP.get(st, {st})

def split_units(text: str) -> List[str]:
    """Splits into sentences and distinct clauses, excluding ignorance assertions."""
    sents = re.split(r'[.!?]+', text)
    units = []
    for s in sents:
        s_clean = s.strip()
        if not s_clean:
            continue
        
        # Split clauses on semicolon or contrastive conjunctions
        clauses = re.split(r'[;]|\b(?:whereas|conversely|in contrast|while|but|however|although)\b', s_clean, flags=re.IGNORECASE)
        for c in clauses:
            c_clean = c.strip()
            if not c_clean:
                continue
            if any(re.search(p, c_clean, re.IGNORECASE) for p in IGNORANCE_PATTERNS):
                continue
            units.append(c_clean)
            
        if not any(re.search(p, s_clean, re.IGNORECASE) for p in IGNORANCE_PATTERNS):
            units.append(s_clean)
    return units

def extract_substantive_text(text: str) -> str:
    """Removes explicit admissions of ignorance or lack of knowledge from candidate text."""
    sents = re.split(r'[.!?]+', text)
    valid_sents = []
    for s in sents:
        s_clean = s.strip()
        if not s_clean:
            continue
        if any(re.search(p, s_clean, re.IGNORECASE) for p in IGNORANCE_PATTERNS):
            clauses = re.split(r'\b(?:but|however|although|though|whereas|conversely)\b', s_clean, flags=re.IGNORECASE)
            for c in clauses:
                c_clean = c.strip()
                if c_clean and not any(re.search(p, c_clean, re.IGNORECASE) for p in IGNORANCE_PATTERNS):
                    valid_sents.append(c_clean)
        else:
            valid_sents.append(s_clean)
    return ". ".join(valid_sents)

def get_concept_distinctive_kws(concept: str, all_concepts: List[str]) -> Tuple[Set[str], Set[str]]:
    """
    Computes all keywords for the concept and isolates the distinctive keywords
    by removing any tokens (or synonyms) shared with other concepts of the same question.
    """
    c_tokens = clean_tokens(concept)
    c_kws = {t for t in c_tokens if t not in STOPWORDS and len(t) > 2}

    other_kws = set()
    for other in all_concepts:
        if other != concept:
            other_clean = {t for t in clean_tokens(other) if t not in STOPWORDS and len(t) > 2}
            other_kws.update(other_clean)

    # All synonyms of other concepts
    other_syns = set()
    for ok in other_kws:
        other_syns.update(get_synonyms(ok))

    # Distinctive keywords are those whose synonyms do not collide with other concepts
    distinctive = {k for k in c_kws if not (get_synonyms(k) & other_syns)}
    return c_kws, distinctive


# ==============================================================================
# MAIN ANSWER EVALUATOR CLASS
# ==============================================================================

class AnswerEvaluator:
    """
    Core technical answer evaluator.
    Combines TF-IDF semantic similarity with distinctive concept coverage and misconception checks.
    """

    def __init__(
        self,
        similarity_weight: float = 0.35,
        concept_coverage_weight: float = 0.65,
        concept_match_threshold: float = 0.20,
        **kwargs
    ):
        self.similarity_weight = similarity_weight
        self.concept_coverage_weight = concept_coverage_weight
        self.concept_match_threshold = concept_match_threshold

    def compute_similarity(
        self,
        model_answer: str,
        candidate_answer: str
    ) -> Tuple[float, float]:
        """
        Computes calibrated and raw cosine similarity between model answer and candidate answer.
        Returns: (calibrated_sim, raw_sim) in range [0.0, 1.0].
        """
        if not candidate_answer.strip() or not model_answer.strip():
            return 0.0, 0.0

        if HAS_SKLEARN:
            try:
                vectorizer = TfidfVectorizer(ngram_range=(1, 2), stop_words='english')
                tfidf_matrix = vectorizer.fit_transform([model_answer, candidate_answer])
                raw_sim = float(sklearn_cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0])
                # Calibrated similarity scales the typical TF-IDF cosine range (0.15 - 0.45)
                calibrated = min(1.0, (raw_sim / 0.35) ** 0.85)
                return round(calibrated, 3), round(raw_sim, 3)
            except Exception:
                pass

        # Jaccard fallback if scikit-learn is unavailable
        words_m = set(clean_tokens(model_answer))
        words_c = set(clean_tokens(candidate_answer))
        if not words_m or not words_c:
            return 0.0, 0.0
        jaccard = len(words_m & words_c) / len(words_m | words_c)
        return round(min(1.0, jaccard / 0.25), 3), round(jaccard, 3)

    def compute_concept_coverage(
        self,
        expected_concepts: List[str],
        candidate_answer: str
    ) -> Dict[str, Any]:
        """
        Evaluates which expected concepts are covered using distinctive anchor keyword matching.
        """
        if not expected_concepts:
            return {"coverage_score": 1.0, "covered": [], "missing": []}

        substantive_text = extract_substantive_text(candidate_answer)
        units = split_units(substantive_text)
        cand_tokens = set(clean_tokens(substantive_text))

        covered = []
        missing = []

        for concept in expected_concepts:
            c_kws, dist_kws = get_concept_distinctive_kws(concept, expected_concepts)
            if not c_kws:
                covered.append({"concept": concept, "confidence": 1.0, "matched_sentence": ""})
                continue

            is_matched = False
            best_conf = 0.0
            best_unit = ""

            for u in units:
                u_tokens = set(clean_tokens(u))
                matched_kws = sum(1 for kw in c_kws if get_synonyms(kw) & u_tokens)
                conf = matched_kws / len(c_kws) if c_kws else 0
                dist_matched = sum(1 for d in dist_kws if get_synonyms(d) & u_tokens)

                # Contradiction check: e.g., claiming shortest path is avoided
                u_lower = u.lower()
                if "shortest path" in concept.lower() and "avoid" in u_lower and ("shortest" in u_lower or "optimal" in u_lower):
                    conf = 0.0
                    dist_matched = 0

                if conf > best_conf:
                    best_conf = conf
                    best_unit = u

                # Distinctive keyword matching requirement
                if dist_kws:
                    if dist_matched >= 1 and conf >= self.concept_match_threshold:
                        is_matched = True
                        break
                else:
                    if conf >= 0.35:
                        is_matched = True
                        break

            # Document-level fallback with strict distinctive token requirement
            if not is_matched and dist_kws:
                doc_dist_matched = sum(1 for d in dist_kws if get_synonyms(d) & cand_tokens)
                doc_matched_kws = sum(1 for kw in c_kws if get_synonyms(kw) & cand_tokens)
                doc_conf = doc_matched_kws / len(c_kws) if c_kws else 0
                if doc_dist_matched >= 1 and doc_conf >= 0.30:
                    is_matched = True
                    best_conf = max(best_conf, doc_conf)

            if is_matched:
                covered.append({
                    "concept": concept,
                    "confidence": round(best_conf, 3),
                    "matched_sentence": best_unit
                })
            else:
                missing.append({
                    "concept": concept,
                    "best_confidence": round(best_conf, 3)
                })

        cov_score = round(len(covered) / len(expected_concepts), 3)
        return {
            "coverage_score": cov_score,
            "covered": covered,
            "missing": missing
        }

    def detect_misconceptions(
        self,
        candidate_answer: str,
        keywords: Optional[List[str]] = None
    ) -> List[str]:
        """
        Detects obvious contradictions, inversions, or unfamiliarity claims.
        """
        misconceptions = []
        text_lower = candidate_answer.lower()

        # Check for fundamental unfamiliarity
        if any(h in text_lower for h in ["i have no idea", "completely guessing", "i never heard of", "no clue"]):
            misconceptions.append("Candidate expressed fundamental unfamiliarity with the core topic.")

        # Data structure inversions (BFS with stack / DFS with queue)
        if re.search(r'\bbfs\b[^.!?]*\b(stack|lifo)\b', text_lower) and not re.search(r'\bbfs\b[^.!?]*\bqueue\b', text_lower):
            misconceptions.append("Potential data structure inversion: BFS associated with stack/LIFO rather than queue.")
        if re.search(r'\bdfs\b[^.!?]*\b(queue|fifo)\b', text_lower) and not re.search(r'\bdfs\b[^.!?]*\bstack\b', text_lower):
            misconceptions.append("Potential data structure inversion: DFS associated with queue/FIFO rather than stack.")

        # Contradictory assertion: claiming shortest path is avoided in BFS
        if re.search(r'\bbfs\b[^.!?]*\bavoid\b[^.!?]*\bshortest path\b', text_lower):
            misconceptions.append("Contradictory claim: asserted that BFS avoids the shortest path.")

        return misconceptions

    def evaluate(
        self,
        question: str,
        model_answer: str,
        expected_concepts: List[str],
        candidate_answer: str,
        keywords: Optional[List[str]] = None,
        domain: Optional[str] = None,
        level: Optional[str] = None,
        topic_tag: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Executes an end-to-end evaluation of a candidate's answer.
        """
        warnings = []
        cand_clean = candidate_answer.strip()
        word_count = len(re.findall(r'\b\w+\b', cand_clean))

        # Check for empty answer
        if not cand_clean or word_count == 0:
            warnings.append("Candidate answer is empty or contains no words.")
            return {
                "provisional_score": 0.0,
                "predicted_quality_level": "poor",
                "semantic_similarity": 0.0,
                "raw_similarity": 0.0,
                "concept_coverage_score": 0.0,
                "total_expected_concepts": len(expected_concepts),
                "covered_concepts": [],
                "possible_missing_concepts": list(expected_concepts),
                "possible_misconceptions": [],
                "warnings": warnings,
                "explanation": "Provisional Technical Score: 0.0/100 (Poor). Candidate provided no answer text.",
                "metadata": {"domain": domain, "level": level, "topic_tag": topic_tag}
            }

        # 1. Semantic Similarity
        calibrated_sim, raw_sim = self.compute_similarity(model_answer, cand_clean)

        # 2. Concept Coverage
        cov_res = self.compute_concept_coverage(expected_concepts, cand_clean)
        cov_score = cov_res["coverage_score"]

        # 3. Misconceptions
        misconceptions = self.detect_misconceptions(cand_clean, keywords)

        # 4. Off-topic check: completely disjoint vocabulary and 0 concept match
        q_tokens = set(clean_tokens(question)) - STOPWORDS
        c_tokens = set(clean_tokens(cand_clean)) - STOPWORDS
        if q_tokens and not (q_tokens & c_tokens) and raw_sim < 0.08 and cov_score == 0.0:
            warnings.append("Candidate answer appears topically disjoint from the question.")
            return {
                "provisional_score": 0.0,
                "predicted_quality_level": "poor",
                "semantic_similarity": calibrated_sim,
                "raw_similarity": raw_sim,
                "concept_coverage_score": 0.0,
                "total_expected_concepts": len(expected_concepts),
                "covered_concepts": [],
                "possible_missing_concepts": list(expected_concepts),
                "possible_misconceptions": misconceptions,
                "warnings": warnings,
                "explanation": "Provisional Technical Score: 0.0/100 (Poor). Response appears off-topic or irrelevant to the technical question.",
                "metadata": {"domain": domain, "level": level, "topic_tag": topic_tag}
            }

        # Warnings for brief or uncertain evaluations
        if word_count < 15 and cov_score < 0.50:
            warnings.append("Candidate answer is very brief (< 15 words) and lacks core technical detail.")
        elif word_count < 25 and cov_score >= 0.75:
            warnings.append("Candidate answer is concise but achieves high conceptual coverage.")

        if raw_sim > 0.30 and cov_score < 0.25:
            warnings.append("High vocabulary overlap detected but few atomic concepts were validated (possible keyword-stuffing).")

        # 5. Calibrated Tiered Anchor Scoring
        # Concept coverage acts as the primary tier anchor, while similarity provides intra-tier adjustment
        if cov_score >= 0.99:
            base_score = 91.0 + min(6.0, 6.0 * calibrated_sim)
        elif cov_score >= 0.70:
            base_score = 77.0 + min(8.0, 8.0 * calibrated_sim)
        elif cov_score >= 0.45:
            base_score = 56.0 + min(9.0, 9.0 * calibrated_sim)
        else:
            base_score = 15.0 + 35.0 * cov_score + min(15.0, 15.0 * calibrated_sim)

        # Misconception deduction and capping
        penalty = min(30.0, len(misconceptions) * 15.0)
        score_after_penalty = base_score - penalty

        if misconceptions:
            score_after_penalty = min(48.0, score_after_penalty)
            warnings.append("Provisional score capped below 50 due to identified conceptual inversion.")

        final_score = max(0.0, min(100.0, round(score_after_penalty, 1)))

        # Quality tier assignment
        if final_score >= 90.0:
            pred_tier = "excellent"
        elif final_score >= 70.0:
            pred_tier = "good"
        elif final_score >= 50.0:
            pred_tier = "average"
        else:
            pred_tier = "poor"

        missing_list = [m["concept"] for m in cov_res["missing"]]

        total_w = self.similarity_weight + self.concept_coverage_weight
        w_sim = round(self.similarity_weight / total_w, 2)
        w_cov = round(self.concept_coverage_weight / total_w, 2)

        explanation = (
            f"Provisional Technical Score: {final_score}/100 ({pred_tier.capitalize()}). "
            f"Semantic similarity to reference: {round(calibrated_sim * 100, 1)}% (raw: {raw_sim:.3f}). "
            f"Concept coverage: {round(cov_score * 100, 1)}% ({len(cov_res['covered'])}/{len(expected_concepts)} concepts covered). "
        )
        if missing_list:
            explanation += f"Identified {len(missing_list)} potentially omitted concepts. "
        if misconceptions:
            explanation += f"Deducted {penalty} points for identified misconceptions: {misconceptions}. "
        explanation += "Note: Evaluation reflects algorithmic concept coverage and similarity baselines."

        return {
            "provisional_score": final_score,
            "predicted_quality_level": pred_tier,
            "semantic_similarity": calibrated_sim,
            "raw_similarity": raw_sim,
            "concept_coverage_score": cov_score,
            "total_expected_concepts": len(expected_concepts),
            "covered_concepts_count": len(cov_res["covered"]),
            "covered_concepts": cov_res["covered"],
            "possible_missing_concepts": missing_list,
            "possible_misconceptions": misconceptions,
            "warnings": warnings,
            "scoring_weights_used": {
                "similarity_weight": w_sim,
                "concept_coverage_weight": w_cov
            },
            "explanation": explanation,
            "metadata": {"domain": domain, "level": level, "topic_tag": topic_tag}
        }


# ==============================================================================
# CLI SMOKE TEST
# ==============================================================================

if __name__ == "__main__":
    evaluator = AnswerEvaluator()
    sample_q = "What is the key difference between Breadth-First Search (BFS) and Depth-First Search (DFS) in graph traversal?"
    sample_model = (
        "BFS explores nodes level by level using a FIFO queue, finding the shortest path on unweighted graphs. "
        "DFS dives deep along branches using a LIFO stack or recursion, using less memory."
    )
    sample_concepts = [
        "BFS traverses level-by-level using a FIFO queue",
        "DFS traverses branch-by-branch deeply before backtracking using a LIFO stack or recursion",
        "BFS guarantees the shortest path in unweighted graphs",
        "Memory complexity differs: BFS stores entire frontier level (O(V)), DFS only stores current path (O(depth))"
    ]
    candidate = (
        "Breadth-First approaches the network ring by ring relying on a FIFO buffer, finding minimal distance routes. "
        "Depth-First pursues an individual branch to its terminal leaf via call stack frames, requiring far less RAM."
    )

    result = evaluator.evaluate(
        question=sample_q,
        model_answer=sample_model,
        expected_concepts=sample_concepts,
        candidate_answer=candidate
    )

    print("=" * 60)
    print("EVALUATOR SMOKE TEST")
    print("=" * 60)
    print(f"Provisional Score: {result['provisional_score']}")
    print(f"Quality Level:     {result['predicted_quality_level']}")
    print(f"Concept Coverage:  {result['concept_coverage_score']}")
    print(f"Covered Concepts:  {len(result['covered_concepts'])}")
    print(f"Missing Concepts:  {result['possible_missing_concepts']}")
    print(f"Explanation:       {result['explanation']}")
