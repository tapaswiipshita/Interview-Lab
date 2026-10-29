# -*- coding: utf-8 -*-
"""
End-to-End System Test Suite
Tests Resume Parsing (PDF & DOCX), Question Selection & Generation,
Audio Transcription, Answer Evaluation, and Final Report Compilation.
"""

import os
import io
import json
from resume_parser import parse_resume_file
from question_generator import create_interview_question_set, get_dataset_questions
from audio_transcriber import transcribe_audio_file
from session_manager import session_manager
from evaluate_answer import AnswerEvaluator
import docx

def create_sample_docx(file_path: str):
    """Creates a sample DOCX resume for test execution."""
    doc = docx.Document()
    doc.add_heading("Alex Rivera", level=0)
    doc.add_paragraph("Email: alex.rivera@example.com | Phone: 555-987-6543")
    
    doc.add_heading("Education", level=1)
    doc.add_paragraph("B.S. in Computer Science - University of California, Berkeley (2020 - 2024)")
    
    doc.add_heading("Technical Skills", level=1)
    doc.add_paragraph("Python, React, TypeScript, Node.js, FastAPI, PostgreSQL, Docker, Redis, REST API, Git")
    
    doc.add_heading("Projects", level=1)
    p = doc.add_paragraph()
    p.add_run("Real-Time Collaborative Code Editor: ").bold = True
    p.add_run("Built a full-stack platform using WebSockets, FastAPI, and React with operational transformation for concurrent editing.")
    
    doc.save(file_path)

def run_e2e_tests():
    print("=" * 80)
    print("END-TO-END WORKFLOW INTEGRATION TEST")
    print("=" * 80)

    # 1. Test Resume Parsing (DOCX & Text)
    print("\n[TEST 1] Resume Parsing (DOCX & Skills Extraction)...")
    sample_docx = os.path.join("scratch", "sample_alex.docx")
    create_sample_docx(sample_docx)
    profile = parse_resume_file(sample_docx)
    assert profile["success"] is True
    assert profile["candidate_name"] == "Alex Rivera"
    assert "FastAPI" in profile["extracted_skills"]
    assert "React" in profile["extracted_skills"]
    assert profile["suggested_domain"] == "Web Development"
    print(f"  -> SUCCESS: Parsed '{profile['candidate_name']}' with {len(profile['extracted_skills'])} skills. Suggested Domain: {profile['suggested_domain']}")

    # 2. Test Question Filtering by Domain & Difficulty
    print("\n[TEST 2] Question Retrieval Across All Domains & Difficulties...")
    for dom in ["Artificial Intelligence", "Machine Learning", "Web Development", "Data Science"]:
        for diff in ["easy", "medium", "hard"]:
            q_set = create_interview_question_set(dom, diff, count=3, resume_profile=profile)
            assert len(q_set["questions"]) == 3
            assert q_set["questions"][0]["domain"] is not None
            assert q_set["questions"][0]["reference_answer"] != ""
            assert len(q_set["questions"][0]["expected_concepts"]) >= 3
    print("  -> SUCCESS: Validated question retrieval across all 12 combinations (4 domains x 3 levels).")

    # 3. Test LLM Fallback Mechanism
    print("\n[TEST 3] LLM Fallback Verification (Without API Keys)...")
    q_set_fallback = create_interview_question_set("Machine Learning", "medium", count=5, resume_profile=profile)
    assert q_set_fallback["is_personalized"] is False
    assert "Curated Benchmark Dataset" in q_set_fallback["generation_source"]
    assert len(q_set_fallback["questions"]) == 5
    print(f"  -> SUCCESS: Graceful fallback confirmed. Source: '{q_set_fallback['generation_source']}'")

    # 4. Test Audio Transcription Logic
    print("\n[TEST 4] Audio Transcription & Client Speech Recognition Fallback...")
    # Test empty audio
    empty_res = transcribe_audio_file(b"", "empty.webm")
    assert empty_res["success"] is False
    
    # Test with client transcript
    mock_audio_bytes = b"RIFF....WAVEfmt ...."
    client_res = transcribe_audio_file(
        file_bytes=mock_audio_bytes,
        filename="answer.webm",
        client_transcript="Breadth-First Search uses a FIFO queue to visit neighbors level-by-level."
    )
    assert client_res["success"] is True
    assert "FIFO queue" in client_res["transcript"]
    print(f"  -> SUCCESS: Transcription fallback provider: '{client_res['service_used']}'")

    # 5. Test Multi-Question Interview Session
    print("\n[TEST 5] Multi-Question Interview Session Execution...")
    session = session_manager.create_session(
        candidate_profile=profile,
        domain="Web Development",
        difficulty="medium",
        question_count=3
    )
    assert session.session_id is not None
    print(f"  -> Session Created: {session.session_id} | Total Qs: {len(session.questions)}")

    # Answer Question 1: Good technical response
    q1 = session.get_current_question()
    print(f"  -> Answering Q1 [{q1['topic']}]: {q1['question'][:60]}...")
    ref1 = session.questions[0]["reference_answer"]
    res1 = session.submit_answer(ref1)
    assert res1["evaluation"]["score"] >= 90.0
    assert res1["evaluation"]["quality_level"] == "excellent"
    print(f"     Score: {res1['evaluation']['score']}/100 ({res1['evaluation']['quality_level']}) | Has Next: {res1['has_next_question']}")

    # Answer Question 2: Partial response
    q2 = session.get_current_question()
    print(f"  -> Answering Q2 [{q2['topic']}]: {q2['question'][:60]}...")
    partial_ans = session.questions[1]["expected_concepts"][0]
    res2 = session.submit_answer(partial_ans)
    print(f"     Score: {res2['evaluation']['score']}/100 ({res2['evaluation']['quality_level']}) | Has Next: {res2['has_next_question']}")

    # Answer Question 3: Off-topic / empty response
    q3 = session.get_current_question()
    print(f"  -> Answering Q3 [{q3['topic']}]: {q3['question'][:60]}...")
    res3 = session.submit_answer("")
    assert res3["evaluation"]["score"] == 0.0
    assert res3["evaluation"]["quality_level"] == "poor"
    assert res3["is_completed"] is True
    print(f"     Score: {res3['evaluation']['score']}/100 ({res3['evaluation']['quality_level']}) | Session Complete: {res3['is_completed']}")

    # 6. Test Final Comprehensive Report Generation
    print("\n[TEST 6] Final Report Compilation...")
    report = session.generate_final_report()
    assert report["candidate_name"] == "Alex Rivera"
    assert report["total_questions_answered"] == 3
    assert len(report["topic_breakdown"]) == 3
    assert isinstance(report["overall_score"], float)
    assert report["overall_quality_tier"] in ["Excellent", "Good", "Average", "Poor"]
    assert len(report["study_recommendations"]) > 0
    print(f"  -> Overall Score: {report['overall_score']}/100 ({report['overall_quality_tier']})")
    print(f"  -> Topic Performance: {[(t['topic'], t['average_score']) for t in report['topic_breakdown']]}")
    print(f"  -> Study Recommendations: {report['study_recommendations']}")

    print("\n" + "=" * 80)
    print("ALL 6 END-TO-END INTEGRATION TESTS PASSED SUCCESSFULLY!")
    print("=" * 80)

if __name__ == "__main__":
    run_e2e_tests()
