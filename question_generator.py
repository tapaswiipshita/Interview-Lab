# -*- coding: utf-8 -*-
"""
Question Generation & Retrieval Module for AI Mock Interview Evaluation System
Retrieves curated technical questions from dataset/interview_dataset.json by domain & difficulty,
and optionally generates resume-specific questions via LLM API if configured.
"""

import os
import json
import random
import re
from typing import List, Dict, Any, Optional

DATASET_PATH = os.path.join(os.path.dirname(__file__), "dataset", "interview_dataset.json")

DOMAIN_NORMALIZATION = {
    "artificial intelligence": "AI",
    "ai": "AI",
    "machine learning": "ML",
    "ml": "ML",
    "web development": "Web Development",
    "web": "Web Development",
    "data science": "Data Science",
    "ds": "Data Science"
}

DIFFICULTY_NORMALIZATION = {
    "easy": "easy",
    "medium": "medium",
    "hard": "hard"
}

_DATASET_CACHE: Optional[List[Dict[str, Any]]] = None

def load_dataset() -> List[Dict[str, Any]]:
    """Loads and caches the 300 benchmark questions from dataset/interview_dataset.json."""
    global _DATASET_CACHE
    if _DATASET_CACHE is None:
        if not os.path.exists(DATASET_PATH):
            raise FileNotFoundError(f"Interview dataset not found at: {DATASET_PATH}")
        with open(DATASET_PATH, "r", encoding="utf-8") as f:
            _DATASET_CACHE = json.load(f)
    return _DATASET_CACHE

def normalize_domain(domain_str: str) -> str:
    """Normalizes domain strings to match dataset conventions ('AI', 'ML', 'Web Development', 'Data Science')."""
    d_clean = domain_str.strip().lower()
    return DOMAIN_NORMALIZATION.get(d_clean, domain_str)

def normalize_difficulty(difficulty_str: str) -> str:
    """Normalizes difficulty strings to ('easy', 'medium', 'hard')."""
    diff_clean = difficulty_str.strip().lower()
    return DIFFICULTY_NORMALIZATION.get(diff_clean, "medium")

def get_dataset_questions(
    domain: str,
    difficulty: str,
    count: int = 5,
    resume_skills: Optional[List[str]] = None
) -> List[Dict[str, Any]]:
    """
    Filters and retrieves curated questions matching domain and difficulty.
    If resume skills are supplied, prioritizes questions with relevant topic/keywords.
    """
    dataset = load_dataset()
    norm_dom = normalize_domain(domain)
    norm_diff = normalize_difficulty(difficulty)

    # Filter by domain and difficulty
    pool = [
        q for q in dataset
        if q.get("domain") == norm_dom and q.get("level") == norm_diff
    ]

    # Fallback to domain only if difficulty pool is too small
    if len(pool) < count:
        pool = [q for q in dataset if q.get("domain") == norm_dom]

    if not pool:
        # Fallback to entire dataset if domain has no matches
        pool = dataset

    # If resume skills exist, compute relevance score for each question
    scored_pool = []
    skill_tokens = set([s.lower() for s in (resume_skills or [])])

    for q in pool:
        q_tokens = set(re.findall(r'\b\w+\b', (q.get("question", "") + " " + q.get("topic_tag", "")).lower()))
        kws = set([k.lower() for k in q.get("keywords", [])])
        overlap = len(skill_tokens & (q_tokens | kws))
        scored_pool.append((overlap, q))

    # Sort primarily by resume skill overlap, with mild shuffle for variety
    scored_pool.sort(key=lambda x: (x[0], random.random()), reverse=True)
    selected_raw = [item[1] for item in scored_pool[:count]]

    # Ensure consistent schema
    formatted_questions = []
    for q in selected_raw:
        formatted_questions.append({
            "question_id": q.get("question_id", f"q_{random.randint(1000, 9999)}"),
            "question": q.get("question", ""),
            "domain": q.get("domain", norm_dom),
            "difficulty": q.get("level", norm_diff),
            "topic": q.get("topic_tag", "Core Concept"),
            "reference_answer": q.get("model_answer", ""),
            "expected_concepts": q.get("expected_concepts", []),
            "keywords": q.get("keywords", []),
            "source": "curated_benchmark",
            "is_personalized": False
        })

    return formatted_questions

def generate_personalized_question_llm(
    domain: str,
    difficulty: str,
    resume_profile: Dict[str, Any]
) -> Optional[Dict[str, Any]]:
    """
    Generates a personalized question tailored to the candidate's actual projects/skills
    using Groq or OpenAI API if configured. Returns None if credentials are absent or call fails.
    """
    groq_api_key = os.environ.get("GROQ_API_KEY")
    openai_api_key = os.environ.get("OPENAI_API_KEY")

    if not groq_api_key and not openai_api_key:
        return None

    projects = resume_profile.get("projects", [])
    skills = resume_profile.get("extracted_skills", [])

    if not projects and not skills:
        return None

    prompt_context = f"Candidate Domain: {domain}\nTarget Difficulty: {difficulty}\n"
    if projects:
        prompt_context += f"Candidate Real Projects from Resume:\n" + "\n".join(f"- {p}" for p in projects[:3]) + "\n"
    if skills:
        prompt_context += f"Candidate Technical Skills: {', '.join(skills[:10])}\n"

    system_prompt = (
        "You are an expert technical interviewer. Generate ONE technical interview question tailored "
        "specifically to the candidate's actual projects or skills provided. "
        "Strict Requirements:\n"
        "1. Focus on technical reasoning, architectural choices, preprocessing, trade-offs, or evaluation.\n"
        "2. Do NOT invent projects or companies not mentioned.\n"
        "3. Respect the specified domain and difficulty level.\n"
        "4. Output MUST be valid JSON with the following exact keys:\n"
        "   - 'question': The interview question (clear and specific)\n"
        "   - 'topic': Concise 2-4 word topic label\n"
        "   - 'reference_answer': A comprehensive, technically rigorous model answer (3-5 sentences)\n"
        "   - 'expected_concepts': An array of exactly 3 to 4 atomic conceptual facts that must be covered\n"
        "   - 'keywords': An array of 4 to 6 relevant technical keywords\n"
    )

    try:
        raw_response_text = ""
        if groq_api_key:
            from groq import Groq
            client = Groq(api_key=groq_api_key)
            completion = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": f"Generate a personalized technical question based on:\n{prompt_context}"}
                ],
                temperature=0.3,
                response_format={"type": "json_object"}
            )
            raw_response_text = completion.choices[0].message.content
        elif openai_api_key:
            import httpx
            headers = {"Authorization": f"Bearer {openai_api_key}", "Content-Type": "application/json"}
            payload = {
                "model": "gpt-4o-mini",
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": f"Generate a personalized technical question based on:\n{prompt_context}"}
                ],
                "temperature": 0.3,
                "response_format": {"type": "json_object"}
            }
            resp = httpx.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload, timeout=12.0)
            if resp.status_code == 200:
                raw_response_text = resp.json()["choices"][0]["message"]["content"]

        if not raw_response_text:
            return None

        data = json.loads(raw_response_text)
        # Validate schema
        if not data.get("question") or not data.get("reference_answer"):
            return None
        concepts = data.get("expected_concepts", [])
        if not isinstance(concepts, list) or len(concepts) < 2:
            return None

        return {
            "question_id": f"q_custom_{random.randint(1000, 9999)}",
            "question": data["question"].strip(),
            "domain": domain,
            "difficulty": difficulty,
            "topic": data.get("topic", "Project Architecture"),
            "reference_answer": data["reference_answer"].strip(),
            "expected_concepts": [str(c).strip() for c in concepts],
            "keywords": data.get("keywords", []),
            "source": "llm_personalized",
            "is_personalized": True
        }
    except Exception as e:
        # Fall back gracefully on any error
        return None

def create_interview_question_set(
    domain: str,
    difficulty: str,
    count: int = 5,
    resume_profile: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    """
    Creates an end-to-end question set for an interview session.
    Combines personalized question generation (if LLM is available) with curated dataset questions.
    """
    norm_dom = normalize_domain(domain)
    norm_diff = normalize_difficulty(difficulty)
    resume_profile = resume_profile or {}

    skills = resume_profile.get("extracted_skills", [])
    has_projects = bool(resume_profile.get("projects"))

    personalized_question = None
    if has_projects or skills:
        personalized_question = generate_personalized_question_llm(norm_dom, norm_diff, resume_profile)

    dataset_needed = count - (1 if personalized_question else 0)
    dataset_questions = get_dataset_questions(norm_dom, norm_diff, count=dataset_needed, resume_skills=skills)

    final_questions = []
    if personalized_question:
        # Place personalized question at position 2 or 3 for natural interview pacing
        insert_idx = min(1, len(dataset_questions))
        final_questions = dataset_questions[:insert_idx] + [personalized_question] + dataset_questions[insert_idx:]
    else:
        final_questions = dataset_questions[:count]

    is_personalized_run = personalized_question is not None

    return {
        "domain": norm_dom,
        "difficulty": norm_diff,
        "total_questions": len(final_questions),
        "is_personalized": is_personalized_run,
        "generation_source": (
            "Hybrid (Resume-Tailored LLM + Curated Benchmark)"
            if is_personalized_run
            else "Curated Benchmark Dataset (Deterministic Fallback)"
        ),
        "questions": final_questions
    }

if __name__ == "__main__":
    test_set = create_interview_question_set("Machine Learning", "medium", 5)
    print(f"Generated {len(test_set['questions'])} questions.")
    for i, q in enumerate(test_set['questions']):
        print(f"Q{i+1}: [{q['topic']}] {q['question'][:70]}...")
