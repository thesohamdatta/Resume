# Soham Datta
**AI Engineer · Agent Systems · Evaluation**
Pune, India · [LinkedIn](https://www.linkedin.com/in/thesohamdatta/) · [GitHub](https://github.com/thesohamdatta) · [Portfolio](https://sohamdatta.framer.ai)
[Mia](https://github.com/thesohamdatta/Mia) · [LLM-Council](https://github.com/thesohamdatta/LLM-Council) · [Voice AI](https://github.com/thesohamdatta/John) · [Aura](https://github.com/thesohamdatta/aura)

---

## Experience

### Aura · Founder
*Jun 2025 – Present · Agent-adjacent systems · Edge Integration · Open Source*

- Design and ship a wearable AI system end to end: ESP32-S3 firmware (FreeRTOS I2S DMA audio at 16 kHz, Opus compression, OTA updates), FastAPI backend with MCP server and memory routers, and self-hosted Deepgram Nova-3 ASR on Kubernetes Helm charts.
- Contribute to the 13.5k-star Omi open-source ecosystem: 21 issue reports with root causes, 5 adopted downstream (speaker clustering fix with 52 unit tests, WebGL leak diagnosis, action-item grounding), 3 of 7 authored PRs maintainer-approved.
- Authored architectural RFCs and decision records (Mia ADR-0001) covering voice pipelines, memory systems, and harness design tradeoffs.

### AI & ML Intern · AICTE via Google
*Oct 2024 – Dec 2024 · Computer Vision · TensorFlow · ML Kit · Edge Deployment*

- Built and evaluated on-device vision models with TensorFlow and Google ML Kit, trading inference latency against accuracy under mobile memory limits.

*Earlier: Associate at Reliance (Jul–Oct 2024) · Research Assistant, PES Modern College (Sep 2023–Mar 2024)*

---

## Projects

### Mia · Personal AI Engineering OS
*TypeScript · Bun · Multi-Host LLM Adapters · Vitest · JSONL State Engine*
[github.com/thesohamdatta/Mia](https://github.com/thesohamdatta/Mia)

- Built a compiled TypeScript CLI running a 5-stage engineering harness (grill → spec → plan → review → ship) with unified adapters for Claude, OpenAI, and local models and automated verification gates (lint, typecheck, Vitest).
- Implemented immutable JSONL state tracking for auditability; recorded the daemon-removal architecture decision in ADR-0001.

### LLM-Council · Multi-Model Consensus Engine
*Python · FastAPI · React · Vite · Multi-Agent Orchestration*
[github.com/thesohamdatta/LLM-Council](https://github.com/thesohamdatta/LLM-Council)

- Built a system that cross-evaluates answers from OpenAI, Anthropic, Gemini, and Groq through an Analyst → Skeptic → Synthesizer critique pipeline, with a React frontend visualizing step-by-step model agreement.
- Designed the pipeline so each stage's verdict stays inspectable in the step-by-step agreement visualization.

### Voice AI Systems · Real-Time Agents & Tool Use
*Python · LiveKit WebRTC · Silero VAD · Kotlin (Android Compose) · TypeScript*
[John](https://github.com/thesohamdatta/John) · [I-am-Mia](https://github.com/thesohamdatta/I-am-Mia) · [voicecoder](https://github.com/thesohamdatta/voicecoder)

- **John**: native Android app (Kotlin/Jetpack Compose) connected to a Python LiveKit agent with tool calling for calendar, tasks, and telephony; client-side Silero VAD for instant barge-in.
- **voicecoder**: VS Code extension for voice-driven editing with multi-provider fallback (Claude, GPT-4o, Gemini, local Ollama) and real-time token cost tracking per feature use.

---

## Technical Skills

- **Agents & Eval:** Multi-agent orchestration, verification-gated harnesses, model cross-evaluation, LLM tool calling (MCP), RAG, prompt grounding.
- **Engineering:** Python (FastAPI, asyncio), TypeScript/JavaScript (Node.js, React, Vite, Bun), Kotlin (Android Compose), C/C++ (ESP32/FreeRTOS), REST APIs, Git/GitHub, Vitest.
- **ML & Voice:** TensorFlow, PyTorch, ML Kit, LiveKit (WebRTC), Silero VAD, Deepgram Nova-3, ElevenLabs.
- **Practice:** Architectural RFCs, decision records (ADR), issue triage with root causes, reproducible state tracking, cost/latency audits.

---

## Education

**University of Pune (SPPU)**
*B.E. in Artificial Intelligence & Machine Learning · 2022 – Jun 2026 · Pune, India*
