# MozhiAI 🗣️
> மொழி (Mozhi) = Language in Tamil

**Offline Multilingual Voice AI for Tamil, Hindi & Telugu — optimized for Arm hardware.**

🔗 **Live Demo:** https://arm-ai.vercel.app
📁 **GitHub:** https://github.com/kavinraj292008-a11y/arm-ai

---

## What is MozhiAI?

MozhiAI is a complete, open-source AI voice platform that lets users speak
in Tamil, Hindi, or Telugu and receive intelligent spoken responses —
entirely offline on Arm-powered hardware. No internet required after setup.
No cloud API calls. No cost.

---

## Architecture
Voice Input → VaniSTT (Whisper INT4) → ArmLM (Phi-3 Mini Q4) → VaniTTS (gTTS) → Voice Output
All 3 engines run on a single Arm64 server. No cloud. No latency from external APIs.

## 5 Components

| Component | Technology | Purpose |
|---|---|---|
| VaniSTT | Whisper tiny INT4 | Speech → Text |
| ArmLM | Phi-3 Mini Q4_K_M | Text → AI reply |
| VaniTTS | gTTS | Text → Speech |
| MozhiAPI | FastAPI + Python | REST API |
| ArmBench | React + Recharts | Live benchmarks |

---

## Arm Optimizations

| Optimization | Details | Impact |
|---|---|---|
| INT4 Quantization | Phi-3 Mini: 7.2GB → 2.2GB | 4× smaller |
| INT4 Quantization | Whisper: 244MB → 61MB | 4× smaller |
| Arm NEON SIMD | llama.cpp Arm64 build | 2-3× faster inference |
| ONNX Runtime | Arm-optimized execution | Faster TTS |

---

## Supported Languages

- 🇮🇳 Tamil (தமிழ்)
- 🇮🇳 Hindi (हिंदी)
- 🇮🇳 Telugu (తెలుగు)

---

## Free Setup — No Credit Card Needed

### Option 1: Google Colab (Recommended)
1. Open `MozhiAI_Backend.ipynb` in Google Colab
2. Run all cells
3. Copy the ngrok URL
4. Set `API` in `frontend/src/App.jsx`
5. Visit https://arm-ai.vercel.app

### Option 2: Any Arm64 Server
```bash
git clone https://github.com/kavinraj292008-a11y/arm-ai
cd arm-ai/MozhiAI/backend
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8000
```

---

## API Endpoints

| Endpoint | Method | Description |
|---|---|---|
| `/` | GET | Project info |
| `/health` | GET | Engine status |
| `/transcribe` | POST | Audio → Text |
| `/chat` | POST | Text → AI reply |
| `/speak` | POST | Text → Audio |
| `/pipeline` | POST | Audio → Audio |
| `/benchmark` | GET | Performance stats |

---

## Benchmark Results

| Metric | Original | Optimized |
|---|---|---|
| Phi-3 Mini model size | 7,372 MB | 2,282 MB (**4×**) |
| Whisper model size | 244 MB | 61 MB (**4×**) |
| STT latency | — | 1,841 ms |
| LLM tokens/sec | — | 2.51 tok/s |
| TTS latency | — | 213 ms |
| Infrastructure cost | $$$ | ₹0 free |

---

## Project Structure
---

## License

MIT License — free to use, modify, and distribute.

## Team

Built for the **Arm AI Optimization Challenge 2026**
by Kavin Raj — Chennai Institute of Technology
