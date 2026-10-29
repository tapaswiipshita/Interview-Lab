# -*- coding: utf-8 -*-
"""
Interview Session Manager & Feedback Generator
Coordinates interview state, evaluates candidate answers using the preserved AnswerEvaluator,
and compiles multi-question session reports with topic breakdowns and study suggestions.
"""

import uuid
import time
from typing import Dict, Any, List, Optional
from evaluate_answer import AnswerEvaluator
from question_generator import create_interview_question_set

class InterviewSession:
    """Represents a single active interview session."""

    def __init__(
        self,
        session_id: str,
        candidate_profile: Dict[str, Any],
        domain: str,
        difficulty: str,
        question_count: int = 5
    ):
        self.session_id = session_id
        self.created_at = time.time()
        self.candidate_profile = candidate_profile or {}
        self.domain = domain
        self.difficulty = difficulty
        self.question_count = question_count

        # Create question set
        q_data = create_interview_question_set(domain, difficulty, question_count, candidate_profile)
        self.questions = q_data["questions"]
        self.is_personalized = q_data["is_personalized"]
        self.generation_source = q_data["generation_source"]

        self.current_index = 0
        self.answers: List[Dict[str, Any]] = []
        self.is_completed = False
        self.evaluator = AnswerEvaluator(
            similarity_weight=0.35,
            concept_coverage_weight=0.65,
            concept_match_threshold=0.20
        )

    def get_current_question(self) -> Optional[Dict[str, Any]]:
        """Returns the current active question or None if finished."""
        if self.current_index >= len(self.questions):
            return None
        q = self.questions[self.current_index]
        return {
            "session_id": self.session_id,
            "question_index": self.current_index + 1,
            "total_questions": len(self.questions),
            "question_id": q["question_id"],
            "question": q["question"],
            "topic": q["topic"],
            "domain": q["domain"],
            "difficulty": q["difficulty"],
            "is_personalized": q.get("is_personalized", False)
        }

    def submit_answer(self, transcribed_answer: str) -> Dict[str, Any]:
        """
        Evaluates candidate's transcribed answer for the current question
        using the preserved AnswerEvaluator.
        """
        if self.current_index >= len(self.questions):
            raise IndexError("Interview session is already completed.")

        q = self.questions[self.current_index]

        # Execute evaluation using the proven AnswerEvaluator
        eval_result = self.evaluator.evaluate(
            question=q["question"],
            model_answer=q["reference_answer"],
            expected_concepts=q["expected_concepts"],
            candidate_answer=transcribed_answer,
            keywords=q.get("keywords", []),
            domain=q.get("domain"),
            level=q.get("difficulty"),
            topic_tag=q.get("topic")
        )

        # Generate constructive per-question feedback
        covered_names = [c["concept"] for c in eval_result.get("covered_concepts", [])]
        missing_names = eval_result.get("possible_missing_concepts", [])
        misconceptions = eval_result.get("possible_misconceptions", [])
        warnings = eval_result.get("warnings", [])
        score = eval_result["provisional_score"]
        tier = eval_result["predicted_quality_level"]

        # Formulate actionable diagnostic feedback
        strengths = []
        improvements = []

        if covered_names:
            strengths.append(f"Successfully addressed {len(covered_names)} key concept(s): " + "; ".join(covered_names[:2]))
        if missing_names:
            improvements.append(f"Omitted {len(missing_names)} expected concept(s): " + "; ".join(missing_names[:2]))
        if misconceptions:
            improvements.append("Identified technical inaccuracy: " + misconceptions[0])
        if not transcribed_answer.strip():
            improvements.append("No response audio detected. Provide a spoken explanation.")

        answer_record = {
            "question_index": self.current_index + 1,
            "question_id": q["question_id"],
            "question": q["question"],
            "topic": q["topic"],
            "reference_answer": q["reference_answer"],
            "expected_concepts": q["expected_concepts"],
            "transcribed_answer": transcribed_answer,
            "evaluation": eval_result,
            "score": score,
            "quality_level": tier,
            "strengths": strengths,
            "improvements": improvements,
            "warnings": warnings
        }

        self.answers.append(answer_record)
        self.current_index += 1

        if self.current_index >= len(self.questions):
            self.is_completed = True

        return {
            "session_id": self.session_id,
            "question_index": self.current_index,
            "total_questions": len(self.questions),
            "is_completed": self.is_completed,
            "has_next_question": not self.is_completed,
            "evaluation": {
                "score": score,
                "quality_level": tier,
                "coverage_score": eval_result["concept_coverage_score"],
                "covered_concepts": covered_names,
                "missing_concepts": missing_names,
                "misconceptions": misconceptions,
                "warnings": warnings,
                "strengths": strengths,
                "improvements": improvements,
                "reference_answer": q["reference_answer"]
            }
        }

    def generate_final_report(self) -> Dict[str, Any]:
        """
        Compiles the comprehensive final interview report containing overall metrics,
        topic breakdowns, frequently missing concepts, and suggested follow-up study areas.
        """
        if not self.answers:
            return {
                "session_id": self.session_id,
                "candidate_name": self.candidate_profile.get("candidate_name", "Candidate"),
                "status": "incomplete",
                "message": "No questions have been answered yet."
            }

        scores = [a["score"] for a in self.answers]
        overall_score = round(sum(scores) / len(scores), 1)

        # Quality tier assignment
        if overall_score >= 90.0:
            overall_tier = "Excellent"
        elif overall_score >= 70.0:
            overall_tier = "Good"
        elif overall_score >= 50.0:
            overall_tier = "Average"
        else:
            overall_tier = "Poor"

        # Topic-wise performance aggregation
        topic_scores: Dict[str, List[float]] = {}
        for a in self.answers:
            top = a["topic"]
            topic_scores.setdefault(top, []).append(a["score"])

        topic_breakdown = []
        strongest_topics = []
        weakest_topics = []

        for top, t_scores in topic_scores.items():
            avg_top_score = round(sum(t_scores) / len(t_scores), 1)
            item = {
                "topic": top,
                "average_score": avg_top_score,
                "questions_evaluated": len(t_scores)
            }
            topic_breakdown.append(item)
            if avg_top_score >= 75.0:
                strongest_topics.append(top)
            elif avg_top_score < 65.0:
                weakest_topics.append(top)

        # Frequently missing concepts
        all_missing = []
        for a in self.answers:
            all_missing.extend(a["evaluation"].get("possible_missing_concepts", []))

        # Recommended study topics based on weak topics & missing concepts
        study_recommendations = []
        if weakest_topics:
            for wt in weakest_topics[:3]:
                study_recommendations.append(f"Review core fundamentals and algorithmic derivations for {wt}.")
        if all_missing:
            study_recommendations.append(f"Deepen familiarity with technical trade-offs regarding: {all_missing[0]}.")
        if not study_recommendations:
            study_recommendations.append("Continue practicing advanced edge-case analysis and time/space complexity trade-offs.")

        # Suggested follow-up questions
        followup_questions = []
        for a in self.answers:
            if a["score"] < 70.0:
                followup_questions.append(f"Can you elaborate further on how {a['topic']} behaves under edge-case constraints?")
        if not followup_questions:
            followup_questions.append(f"How would you scale your proposed architecture for {self.domain} in a high-concurrency production setting?")

        return {
            "session_id": self.session_id,
            "candidate_name": self.candidate_profile.get("candidate_name", "Candidate"),
            "domain": self.domain,
            "difficulty": self.difficulty,
            "total_questions_answered": len(self.answers),
            "total_questions": len(self.questions),
            "is_completed": self.is_completed,
            "is_personalized": self.is_personalized,
            "generation_source": self.generation_source,
            "overall_score": overall_score,
            "overall_quality_tier": overall_tier,
            "topic_breakdown": topic_breakdown,
            "strongest_topics": strongest_topics,
            "weakest_topics": weakest_topics,
            "frequently_missing_concepts": list(set(all_missing))[:5],
            "study_recommendations": study_recommendations,
            "suggested_followup_questions": followup_questions[:3],
            "itemized_answers": self.answers
        }


class SessionManager:
    """Singleton session repository managing active interview sessions in memory."""

    def __init__(self):
        self.sessions: Dict[str, InterviewSession] = {}

    def create_session(
        self,
        candidate_profile: Dict[str, Any],
        domain: str,
        difficulty: str,
        question_count: int = 5
    ) -> InterviewSession:
        session_id = str(uuid.uuid4())[:8]
        session = InterviewSession(
            session_id=session_id,
            candidate_profile=candidate_profile,
            domain=domain,
            difficulty=difficulty,
            question_count=question_count
        )
        self.sessions[session_id] = session
        return session

    def get_session(self, session_id: str) -> Optional[InterviewSession]:
        return self.sessions.get(session_id)

session_manager = SessionManager()

if __name__ == "__main__":
    test_session = session_manager.create_session({}, "AI", "easy", 3)
    q1 = test_session.get_current_question()
    print("Session created:", test_session.session_id)
    print("Q1:", q1["question"][:60])
