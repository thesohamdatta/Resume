# Soham Datta
**AI Engineer · Autonomous Agents · Multi-LLM Orchestration · Internal Tooling**  
Pune, India · [LinkedIn](https://www.linkedin.com/in/thesohamdatta/) · [GitHub](https://github.com/thesohamdatta) · [Portfolio](https://sohamdatta.framer.ai)  
*Built:* [Aura](https://github.com/thesohamdatta/aura) · [Mia](https://github.com/thesohamdatta/Mia) · [Voice AI](https://github.com/thesohamdatta/John) · [LLM-Council](https://github.com/thesohamdatta/LLM-Council)

---

## Technical Skills

- **AI Agents & LLMs:** Multi-agent orchestration, tool calling, function calling, structured outputs, multi-step reasoning, autonomous workflows, prompt engineering, RAG systems.
- **AI Backend:** Python (FastAPI, PyTorch, asyncio), LLM APIs (Anthropic Claude, OpenAI, Gemini, Groq), embeddings, vector databases (pgvector).
- **Engineering:** TypeScript/JavaScript (Node.js, React, Vite, Bun), API integrations, webhooks, automation frameworks, data pipelines, web scraping.
- **Voice & Multimodal:** LiveKit WebRTC, Silero VAD, streaming STT/TTS (Deepgram, ElevenLabs), TensorFlow, ML Kit.
- **Infrastructure:** Kubernetes Helm charts, self-hosted ASR, REST APIs, Git/GitHub, automated testing (Vitest).

---

## Experience

### Aura · Founder
*Jun 2025 – Present*  
*Wearable AI · FastAPI Backend · Multi-Step Agentic Workflows · Open Source*
- Built FastAPI backend with autonomous multi-step workflows: transcription ingestion, memory extraction, knowledge graph entity linking, speech profiling, and Model Context Protocol server (`backend/routers/*.py`).
- Integrated self-hosted Deepgram Nova-3 ASR via Kubernetes Helm charts with pgvector migrations for vector memory retrieval.
- Authored speaker grounding workflow threading resolved `user_name` into `extract_action_items()` for task attribution ([Issue #8918](https://github.com/BasedHardware/omi/issues/8918), adopted in [PR #12089](https://github.com/BasedHardware/omi/pull/12089)).
- Implemented offline agglomerative hierarchical clustering (SciPy cosine linkage) with 52 unit tests solving speaker drift in 3+ person meetings ([PR #8919](https://github.com/BasedHardware/omi/pull/8919), adopted in [PR #12471](https://github.com/BasedHardware/omi/pull/12471)).

### AI & ML Intern · AICTE via Google
*Oct 2024 – Dec 2024*  
*Computer Vision · TensorFlow · ML Kit · Edge Deployment*
- Built and evaluated lightweight computer vision models with TensorFlow and Google ML Kit for on-device edge classification.
- Applied transfer learning and data augmentation pipelines to optimize model inference latency and accuracy under mobile memory constraints.

### Freelancer · AI & Automation
*Sep 2024 – Present*  
*Workflow Automation · LLMs · Rapid Prototyping*
- Built custom AI agent workflows and automation scripts for student and community developer projects.

---

## Featured Projects

### Mia · Personal AI Engineering OS
*TypeScript · Bun · Multi-Host LLM Adapters · Vitest · JSONL State Engine*  
[github.com/thesohamdatta/Mia](https://github.com/thesohamdatta/Mia)
- Built a compiled, local-first developer CLI in TypeScript (single Bun binary) automating a 5-stage AI engineering harness (`grill` → `spec` → `plan` → `review` → `ship`).
- Implemented unified host adapters for Anthropic Claude, OpenAI Codex, and local models with automated verification gates (lint, typecheck, Vitest) and immutable JSONL state tracking.
- Eliminated fragile background daemon architecture in favor of stateless event-driven execution ([ADR-0001](https://github.com/thesohamdatta/Mia/blob/main/docs/decisions/ADR-0001-eliminate-daemon.md)).

### LLM-Council · Multi-Model Consensus Engine
*Python · FastAPI · React · Vite · Multi-Agent Orchestration*  
[github.com/thesohamdatta/LLM-Council](https://github.com/thesohamdatta/LLM-Council)
- Built a multi-LLM consensus engine querying OpenAI, Anthropic, Gemini, and Groq concurrently to cross-evaluate and synthesize peer-reviewed answers.
- Implemented a 3-stage critique pipeline (Analyst → Skeptic → Synthesizer) with structured prompting and an interactive React frontend visualizing step-by-step model agreement.

### Voice AI Systems · Real-Time Voice Agents & Copilots
*LiveKit WebRTC · Silero VAD · ElevenLabs · Python · Kotlin (Android Compose)*  
[github.com/thesohamdatta/John](https://github.com/thesohamdatta/John) · [github.com/thesohamdatta/voicecoder](https://github.com/thesohamdatta/voicecoder)
- Built real-time WebRTC conversational voice agents using LiveKit with client-side Silero VAD for instant barge-in interruption and semantic turn detection.
- Developed **John**: native Android Kotlin client (Jetpack Compose) connected to a Python LiveKit agent backend with tool calling for calendar, tasks, and telephony automation (`tools/calendar.py`, `tools/tasks.py`, `tools/phone.py`).
- Developed **voicecoder**: VS Code extension for voice-driven code editing with multi-provider fallback (Claude, GPT-4o, Gemini, local Ollama) and real-time token cost tracking.

### Omi Open-Source Contributions
*21 Issues Authored · 5 Architectural RFCs · 120+ Unit Tests · Downstream Adoption*  
[github.com/BasedHardware/omi](https://github.com/BasedHardware/omi)
- Diagnosed Electron WebGL GPU memory leak on Windows caused by CSS backdrop filters over 3D graph canvases ([Issue #8438](https://github.com/BasedHardware/omi/issues/8438), merged downstream in [PR #8902](https://github.com/BasedHardware/omi/pull/8902)).
- Authored Windows file indexing spec ([Issue #8991](https://github.com/BasedHardware/omi/issues/8991), delivered in merged [#7896/#9595/#10236]).
- Authored 1-click Markdown export spec ([Issue #12360](https://github.com/BasedHardware/omi/issues/12360) OPEN; draft [PR #12927](https://github.com/BasedHardware/omi/pull/12927)).

---

## Education

**University of Pune (SPPU)**  
*Bachelor of Engineering (B.E.) in Artificial Intelligence & Machine Learning*  
*2022 – Jun 2026* · Pune, India
