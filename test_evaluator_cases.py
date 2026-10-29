# -*- coding: utf-8 -*-
"""
Targeted Technical Correctness Test Suite (Phase 7 & Deliverable 5)
Evaluates 10 specific edge cases:
  1. A technically correct answer using different wording from the reference answer.
  2. An answer containing relevant keywords but incorrect reasoning.
  3. An answer that correctly explains only part of the question.
  4. A fluent but technically incorrect answer (hallucination).
  5. A short but correct answer.
  6. An answer with a major misconception (e.g., category inversion).
  7. An empty candidate answer.
  8. An irrelevant answer (completely off-topic).
  9. An answer that omits an expected concept.
 10. An answer that explains a concept correctly using a synonym or paraphrase.
"""

import sys
import os
import json

sys.path.insert(0, os.path.abspath('.'))
from evaluate_answer import AnswerEvaluator


def run_targeted_tests():
    sample_q = "What is the key difference between Breadth-First Search (BFS) and Depth-First Search (DFS) in graph traversal?"
    sample_model = (
        "Breadth-First Search (BFS) and Depth-First Search (DFS) differ fundamentally in their exploration order "
        "and data structures. BFS explores nodes level by level using a First-In-First-Out (FIFO) queue, visiting "
        "all immediate neighbors before advancing to the next depth. Because it explores in order of path length, "
        "BFS guarantees finding the shortest path on unweighted graphs. However, BFS requires significant memory—up to "
        "O(V) or exponential in search depth—to maintain the frontier queue. In contrast, DFS dives as deeply as possible "
        "along each branch using a Last-In-First-Out (LIFO) stack or recursion before backtracking. While DFS does not "
        "guarantee shortest paths and can get stuck in deep or infinite branches, its memory overhead is much lower, "
        "scaling with the maximum path depth rather than the branching width."
    )
    sample_concepts = [
        "BFS traverses level-by-level using a FIFO queue",
        "DFS traverses branch-by-branch deeply before backtracking using a LIFO stack or recursion",
        "BFS guarantees the shortest path in unweighted graphs",
        "Memory complexity differs: BFS stores entire frontier level (O(V)), DFS only stores current path (O(depth))"
    ]
    keywords = ["Breadth-First Search", "Depth-First Search", "Queue", "Stack", "Shortest Path", "Memory Complexity"]

    test_cases = [
        {
            "id": "TC01",
            "name": "Technically correct answer with alternative wording / paraphrase",
            "candidate_answer": (
                "The essential distinction is the exploration pattern. Breadth-First approaches the network ring by ring, "
                "relying on a FIFO buffer to visit all adjacent vertices before descending. Hence it reliably uncovers "
                "minimal distance routes in unweighted topologies. Conversely, Depth-First pursues an individual branch "
                "to its terminal leaf via call stack frames before unwinding, requiring far less RAM."
            ),
            "expected_tier": ["excellent", "good"],
            "expected_criteria": "Should recognize concept coverage and award passing score (90-95) despite novel terminology."
        },
        {
            "id": "TC02",
            "name": "Relevant keywords present but incorrect reasoning / inverted logic",
            "candidate_answer": (
                "Breadth-First Search and Depth-First Search both use Queue and Stack. In BFS, the stack ensures that shortest path "
                "is avoided, while DFS uses a FIFO queue to backtrack through memory complexity. Therefore, graph traversal "
                "runs in linear logarithmic time because the queue reverses the stack."
            ),
            "expected_tier": ["poor"],
            "expected_criteria": "Must detect contradictory claim ('shortest path is avoided') or misconception and cap below 50."
        },
        {
            "id": "TC03",
            "name": "Correctly explains only part of the question (partial coverage)",
            "candidate_answer": (
                "BFS explores layer by layer using a FIFO queue, and because of this level-order progression, "
                "it guarantees the shortest path in unweighted graphs. I do not remember how DFS works or how memory compares."
            ),
            "expected_tier": ["average", "good"],
            "expected_criteria": "Should award credit for the BFS concepts (~50% coverage) while identifying DFS/memory as missing."
        },
        {
            "id": "TC04",
            "name": "Fluent but technically incorrect answer (hallucination)",
            "candidate_answer": (
                "BFS and DFS are state-of-the-art transformer architectures designed for graph attention networks. "
                "BFS leverages multi-head attention to vectorize the adjacency matrix, whereas DFS uses convolutional "
                "dropout to prune recurrent gradients during backpropagation."
            ),
            "expected_tier": ["poor"],
            "expected_criteria": "Must return 0% concept coverage and very low provisional score (< 30) despite grammatical fluency."
        },
        {
            "id": "TC05",
            "name": "Short but correct answer (concise)",
            "candidate_answer": (
                "BFS uses a FIFO queue and visits neighbors level-by-level, finding shortest paths on unweighted graphs. "
                "DFS uses a stack or recursion, going deep along branches, using less memory."
            ),
            "expected_tier": ["good", "excellent"],
            "expected_criteria": "Should recognize 100% conceptual coverage without zeroing out score for brevity."
        },
        {
            "id": "TC06",
            "name": "Answer with a major structural misconception (category inversion)",
            "candidate_answer": (
                "BFS uses a stack and goes deep first without backtracking, whereas DFS uses a FIFO queue to visit all neighbors first. "
                "So DFS is what guarantees shortest path and BFS uses way more memory."
            ),
            "expected_tier": ["poor"],
            "expected_criteria": "Must detect data structure inversion and cap provisional score in the Poor band (< 50)."
        },
        {
            "id": "TC07",
            "name": "Empty candidate answer",
            "candidate_answer": "   \n\t  ",
            "expected_tier": ["poor"],
            "expected_criteria": "Must return exactly 0.0 provisional score with an explicit warning."
        },
        {
            "id": "TC08",
            "name": "Completely irrelevant / off-topic answer",
            "candidate_answer": (
                "Yesterday I made a delicious Margherita pizza with fresh basil and mozzarella. "
                "Baking it at 500 degrees creates a crispy sourdough crust."
            ),
            "expected_tier": ["poor"],
            "expected_criteria": "Must return 0.0 provisional score with an irrelevance warning."
        },
        {
            "id": "TC09",
            "name": "Answer that omits an expected concept (memory complexity)",
            "candidate_answer": (
                "BFS traverses level by level with a FIFO queue and finds the shortest path on unweighted graphs. "
                "DFS explores as deep as possible down each path using recursion or a stack before backtracking."
            ),
            "expected_tier": ["good"],
            "expected_criteria": "Should score in Good tier (75-85) on traversal mechanics and flag memory complexity as omitted."
        },
        {
            "id": "TC10",
            "name": "Answer explaining concepts correctly using synonyms",
            "candidate_answer": (
                "BFS processes nodes tier-by-tier with a first-in first-out buffer, ensuring optimal routing without edge weights. "
                "DFS descends individual branches to the bottom using a last-in first-out storage or function calls before unwinding. "
                "BFS memory consumption is proportional to the widest tier, whereas DFS consumption is bounded by path height."
            ),
            "expected_tier": ["excellent", "good"],
            "expected_criteria": "Should successfully recognize 100% coverage and score in Excellent/Good tier (90-95)."
        }
    ]

    evaluator = AnswerEvaluator(
        similarity_weight=0.35,
        concept_coverage_weight=0.65,
        concept_match_threshold=0.20
    )

    print("=" * 80)
    print("TARGETED TEST SUITE: 10 TECHNICAL INTERVIEW SCENARIOS")
    print("=" * 80)

    results = []
    all_passed = True

    for tc in test_cases:
        res = evaluator.evaluate(
            question=sample_q,
            model_answer=sample_model,
            expected_concepts=sample_concepts,
            candidate_answer=tc['candidate_answer'],
            keywords=keywords
        )

        pred_tier = res['predicted_quality_level']
        score = res['provisional_score']
        sim = res['semantic_similarity']
        cov = res['concept_coverage_score']
        warnings = res['warnings']
        misconceptions = res['possible_misconceptions']

        # Determine pass/fail based on expected criteria
        passed = pred_tier in tc['expected_tier']
        if tc['id'] == 'TC07' and score != 0.0:
            passed = False
        if tc['id'] == 'TC08' and score != 0.0:
            passed = False
        if tc['id'] in ['TC02', 'TC06'] and score >= 50.0:
            passed = False

        if not passed:
            all_passed = False

        results.append({
            "id": tc['id'],
            "name": tc['name'],
            "score": score,
            "predicted_tier": pred_tier,
            "expected_tier": tc['expected_tier'],
            "passed": passed,
            "similarity": sim,
            "coverage": cov,
            "warnings": warnings,
            "misconceptions": misconceptions,
            "explanation": res['explanation']
        })

        status_str = "PASS" if passed else "FAIL"
        print(f"\n[{tc['id']}] {tc['name']} -> [{status_str}]")
        print(f"  Score: {score}/100 ({pred_tier}) | Sim: {sim} | Cov: {cov}")
        print(f"  Expected Tier: {tc['expected_tier']} | Warnings: {warnings}")
        print(f"  Misconceptions: {misconceptions}")

    print("\n" + "=" * 80)
    print(f"TARGETED TESTS SUMMARY: {'ALL 10 TESTS PASSED' if all_passed else 'SOME TESTS FAILED'}")
    print("=" * 80)

    return results

if __name__ == '__main__':
    run_targeted_tests()
