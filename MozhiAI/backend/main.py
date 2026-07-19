# MozhiAI Backend — FastAPI Server
# Run on any Arm64 machine or Google Colab
# See README.md for setup instructions

from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import time

app = FastAPI(
    title="MozhiAI API",
    description="Offline Multilingual Voice AI for Tamil, Hindi & Telugu",
    version="3.0.0"
)

app.add_middleware(CORSMiddleware,
    allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

@app.get("/")
def root():
    return {
        "project": "MozhiAI",
        "meaning": "Mozhi (மொழி) = Language in Tamil",
        "status": "running ✅",
        "version": "3.0.0",
        "engines": {
            "STT": "Whisper tiny INT4",
            "LLM": "Phi-3 Mini Q4_K_M",
            "TTS": "gTTS Tamil/Hindi/Telugu"
        },
        "languages": ["Tamil (ta)", "Hindi (hi)", "Telugu (te)"]
    }

@app.get("/health")
def health():
    return {"status": "ok", "timestamp": time.time()}

# Full implementation in MozhiAI_Backend.ipynb (Google Colab)
# See README.md for deployment instructions
