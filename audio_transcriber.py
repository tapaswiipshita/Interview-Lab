# -*- coding: utf-8 -*-
"""
Audio Transcription Service for AI Mock Interview Evaluation System
Supports server-side transcription using Groq/OpenAI Whisper API when configured,
and gracefully harmonizes with browser-side Web Speech API when offline.
"""

import os
import tempfile
from typing import Dict, Any, Optional

def transcribe_audio_file(
    file_bytes: bytes,
    filename: str,
    client_transcript: Optional[str] = None
) -> Dict[str, Any]:
    """
    Transcribes audio bytes into text.
    Prioritizes Groq Whisper API (whisper-large-v3) or OpenAI Whisper API.
    Falls back to client_transcript (from browser Web Speech API) if keys are unavailable.
    """
    if not file_bytes or len(file_bytes) == 0:
        return {
            "success": False,
            "transcript": "",
            "service_used": "none",
            "error": "Empty audio recording received."
        }

    groq_api_key = os.environ.get("GROQ_API_KEY")
    openai_api_key = os.environ.get("OPENAI_API_KEY")

    # 1. Try Groq Whisper API (Ultra-fast whisper-large-v3)
    if groq_api_key:
        try:
            from groq import Groq
            client = Groq(api_key=groq_api_key)
            ext = os.path.splitext(filename)[1].lower() or ".webm"
            with tempfile.NamedTemporaryFile(suffix=ext, delete=False) as tmp:
                tmp.write(file_bytes)
                tmp_path = tmp.name

            try:
                with open(tmp_path, "rb") as audio_file:
                    transcription = client.audio.transcriptions.create(
                        model="whisper-large-v3",
                        file=audio_file,
                        response_format="text"
                    )
                transcript_text = str(transcription).strip()
                return {
                    "success": True,
                    "transcript": transcript_text,
                    "service_used": "Groq Whisper (whisper-large-v3)",
                    "audio_size_bytes": len(file_bytes)
                }
            finally:
                if os.path.exists(tmp_path):
                    os.remove(tmp_path)
        except Exception as e:
            # Fall back to client transcript or next service
            pass

    # 2. Try OpenAI Whisper API
    if openai_api_key:
        try:
            import httpx
            ext = os.path.splitext(filename)[1].lower() or ".webm"
            with tempfile.NamedTemporaryFile(suffix=ext, delete=False) as tmp:
                tmp.write(file_bytes)
                tmp_path = tmp.name

            try:
                with open(tmp_path, "rb") as audio_file:
                    files = {"file": (filename, audio_file, "audio/webm")}
                    data = {"model": "whisper-1"}
                    headers = {"Authorization": f"Bearer {openai_api_key}"}
                    resp = httpx.post(
                        "https://api.openai.com/v1/audio/transcriptions",
                        headers=headers,
                        files=files,
                        data=data,
                        timeout=15.0
                    )
                if resp.status_code == 200:
                    return {
                        "success": True,
                        "transcript": resp.json().get("text", "").strip(),
                        "service_used": "OpenAI Whisper (whisper-1)",
                        "audio_size_bytes": len(file_bytes)
                    }
            finally:
                if os.path.exists(tmp_path):
                    os.remove(tmp_path)
        except Exception as e:
            pass

    # 3. Fallback: Browser Web Speech API transcript provided with audio
    if client_transcript and client_transcript.strip():
        return {
            "success": True,
            "transcript": client_transcript.strip(),
            "service_used": "Browser Native Web Speech API (Client-side)",
            "audio_size_bytes": len(file_bytes)
        }

    return {
        "success": False,
        "transcript": "",
        "service_used": "none",
        "error": (
            "No server-side speech-to-text API key (GROQ_API_KEY / OPENAI_API_KEY) found, "
            "and no browser Web Speech transcript was detected. "
            "Please ensure microphone speech recognition is allowed in your browser."
        )
    }

if __name__ == "__main__":
    print("Audio Transcriber Module ready.")
