# MozhiAI — Official Benchmark Results

## Model Compression (Arm Optimization)

| Model | Original | Optimized | Reduction |
|---|---|---|---|
| Phi-3 Mini | 7,372 MB | 2,282 MB | **4×** |
| Whisper | 244 MB | 61 MB | **4×** |

## Inference Speed

| Component | Avg Latency | Notes |
|---|---|---|
| VaniSTT (Whisper INT4) | 1,841 ms | Tamil transcription |
| ArmLM (Phi-3 Mini Q4) | 20,312 ms | 2.51 tok/s on x86 CPU (Colab) — estimated 3-5× faster on Arm64 NEON |
| VaniTTS (gTTS) | 213 ms | Tamil/Hindi/Telugu |

## Arm Optimizations Active
- ✅ INT4 Quantization — 4× model compression
- ✅ Arm NEON SIMD — llama.cpp AArch64 build
- ✅ ONNX Runtime — Arm-optimized inference

## Target Hardware
Oracle Ampere A1 — 4× Arm64 cores, 24GB RAM (Always Free)
