# -*- coding: utf-8 -*-
"""
FastAPI Application Backend for AI Mock Interview Evaluation System
Provides complete REST API endpoints for:
  - Resume upload and parsing (PDF/DOCX)
  - Interview configuration & question generation
  - Voice audio transcription (Whisper API / Web Speech fallback)
  - Evaluation via preserved AnswerEvaluator
  - Final interview report generation
  - Serving the interactive frontend UI
"""

import os
import tempfile
import uvicorn
from fastapi import FastAPI, UploadFile, File, Form, HTTPException, Request
from fastapi.responses import JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict, Any, List, Optional
from dotenv import load_dotenv

load_dotenv()

from resume_parser import parse_resume_file
from session_manager import session_manager
from audio_transcriber import transcribe_audio_file

app = FastAPI(
    title="AI Mock Interview Evaluation System",
    description="End-to-end technical interview simulation with voice input, atomic concept evaluation, and personalized feedback.",
    version="2.0.0"
)

# Enable CORS for browser access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

STATIC_DIR = os.path.join(os.path.dirname(__file__), "static")
os.makedirs(STATIC_DIR, exist_ok=True)

# Mount static directory
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

# ==============================================================================
# PYDANTIC SCHEMAS
# ==============================================================================

class StartInterviewRequest(BaseModel):
    domain: str
    difficulty: str = "medium"
    question_count: int = 5
    candidate_profile: Optional[Dict[str, Any]] = None

class SubmitAnswerRequest(BaseModel):
    transcribed_answer: str

# ==============================================================================
# API ENDPOINTS
# ==============================================================================

@app.get("/")
async def serve_index():
    """Serves the main single-page web application."""
    index_file = os.path.join(STATIC_DIR, "index.html")
    if os.path.exists(index_file):
        return FileResponse(index_file)
    return {"message": "AI Mock Interview Evaluation System API is running. UI file loading..."}

@app.get("/api/health")
async def health_check():
    """Returns system status and API configuration."""
    has_groq = bool(os.environ.get("GROQ_API_KEY"))
    has_openai = bool(os.environ.get("OPENAI_API_KEY"))
    return {
        "status": "healthy",
        "llm_configured": has_groq or has_openai,
        "transcription_provider": "Groq Whisper" if has_groq else ("OpenAI Whisper" if has_openai else "Native Browser Web Speech API"),
        "active_sessions": len(session_manager.sessions)
    }

@app.post("/api/resume/upload")
async def upload_resume(file: UploadFile = File(...)):
    """
    Parses an uploaded PDF or DOCX resume.
    Extracts skills, projects, education, experience, and contact metadata.
    """
    allowed_exts = [".pdf", ".docx", ".doc", ".txt"]
    ext = os.path.splitext(file.filename)[1].lower()
    if ext not in allowed_exts:
        raise HTTPException(
            status_code=400,
            detail=f"Unsupported file format '{ext}'. Please upload a PDF or DOCX resume."
        )

    try:
        content = await file.read()
        if len(content) == 0:
            raise HTTPException(status_code=400, detail="Uploaded file is empty.")

        with tempfile.NamedTemporaryFile(suffix=ext, delete=False) as tmp:
            tmp.write(content)
            tmp_path = tmp.name

        try:
            profile = parse_resume_file(tmp_path)
            profile["filename"] = file.filename
            return JSONResponse(content=profile)
        finally:
            if os.path.exists(tmp_path):
                os.remove(tmp_path)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to parse resume: {str(e)}")

@app.post("/api/interview/start")
async def start_interview(payload: StartInterviewRequest):
    """
    Initializes a new interview session.
    Filters questions by domain/difficulty and generates personalized questions if resume is present.
    """
    try:
        session = session_manager.create_session(
            candidate_profile=payload.candidate_profile or {},
            domain=payload.domain,
            difficulty=payload.difficulty,
            question_count=max(1, min(15, payload.question_count))
        )
        first_q = session.get_current_question()
        return {
            "session_id": session.session_id,
            "total_questions": len(session.questions),
            "domain": session.domain,
            "difficulty": session.difficulty,
            "is_personalized": session.is_personalized,
            "generation_source": session.generation_source,
            "current_question": first_q
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to start interview: {str(e)}")

@app.get("/api/interview/{session_id}/question")
async def get_question(session_id: str):
    """Retrieves the current active question for an ongoing session."""
    session = session_manager.get_session(session_id)
    if not session:
        raise HTTPException(status_code=404, detail="Interview session not found.")

    q = session.get_current_question()
    if not q:
        return {
            "session_id": session_id,
            "is_completed": True,
            "message": "All interview questions have been answered. Ready to generate report."
        }
    return q

@app.post("/api/interview/{session_id}/answer")
async def submit_answer(session_id: str, payload: SubmitAnswerRequest):
    """
    Submits a candidate's transcribed answer.
    Evaluates via the preserved AnswerEvaluator and returns itemized feedback.
    """
    session = session_manager.get_session(session_id)
    if not session:
        raise HTTPException(status_code=404, detail="Interview session not found.")

    try:
        eval_result = session.submit_answer(payload.transcribed_answer)
        return eval_result
    except IndexError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Evaluation failed: {str(e)}")

@app.post("/api/transcribe")
async def transcribe_audio(
    audio_file: UploadFile = File(...),
    client_transcript: Optional[str] = Form(None)
):
    """
    Transcribes uploaded voice audio from browser microphone.
    Utilizes server Whisper API (if configured) or native Web Speech API fallback.
    """
    try:
        file_bytes = await audio_file.read()
        res = transcribe_audio_file(
            file_bytes=file_bytes,
            filename=audio_file.filename,
            client_transcript=client_transcript
        )
        if not res["success"] and not client_transcript:
            raise HTTPException(status_code=400, detail=res["error"])
        return res
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Audio transcription failed: {str(e)}")

@app.get("/api/interview/{session_id}/report")
async def get_final_report(session_id: str):
    """Generates the comprehensive final report for a completed session."""
    session = session_manager.get_session(session_id)
    if not session:
        raise HTTPException(status_code=404, detail="Interview session not found.")

    report = session.generate_final_report()
    return report

if __name__ == "__main__":
    host = os.environ.get("HOST", "127.0.0.1")
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host=host, port=port, reload=True)
