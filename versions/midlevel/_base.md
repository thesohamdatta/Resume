# Soham Datta

**Pune, India**
[LinkedIn](https://www.linkedin.com/in/thesohamdatta/) · [GitHub](https://github.com/thesohamdatta) · [Portfolio](https://sohamdatta.framer.ai)

---

## Experience

### Founder · Aura
**Jun 2025 – Present** | Wearable AI · Hardware Prototyping · Edge Integration · Open Source

- Designed 3D-printed wearable AI pendant packaging ESP32-S3 hardware, camera, battery, and microphone in custom CAD enclosures; wrote FreeRTOS firmware for 16 kHz I2S DMA capture with Opus compression and OTA updates.
- Adapted FastAPI backend from the Omi ecosystem with pgvector memory retrieval and Kubernetes-hosted Deepgram Nova-3 ASR; verified end-to-end audio streaming and cloud memory capture.
- Diagnosed Electron WebGL GPU memory leak on Windows caused by CSS backdrop filters ([Issue #8438](https://github.com/BasedHardware/omi/issues/8438), merged downstream in [PR #8902](https://github.com/BasedHardware/omi/pull/8902)).
- Authored offline speaker clustering with SciPy agglomerative clustering and 52 tests ([PR #8919](https://github.com/BasedHardware/omi/pull/8919), adopted in [PR #12471](https://github.com/BasedHardware/omi/pull/12471)); threaded user_name into action-item extraction ([Issue #8918](https://github.com/BasedHardware/omi/issues/8918), adopted in [PR #12089](https://github.com/BasedHardware/omi/pull/12089)).
- Authored Windows file indexing spec ([Issue #8991](https://github.com/BasedHardware/omi/issues/8991), delivered in [#7896/#9595/#10236]) and Markdown export spec ([Issue #12360](https://github.com/BasedHardware/omi/issues/12360) OPEN; draft [PR #12927](https://github.com/BasedHardware/omi/pull/12927) NOT merged).

### AI & ML Intern · AICTE via Google
**Oct 2024 – Dec 2024** | Computer Vision · TensorFlow · ML Kit · Edge Deployment

- Built and evaluated lightweight computer vision models with TensorFlow and Google ML Kit for on-device edge classification.
- Applied transfer learning and data augmentation pipelines to optimise model inference latency and accuracy under mobile memory constraints.

### Associate · Reliance
**Jul 2024 – Oct 2024** | Customer Service · Store Operations · POS · Documentation

- Handled the customer service desk across complaints, coupons, memberships, Reliance cards, digital vouchers, exchanges, documentation, and daily follow-up.
- Worked with brand managers, HR, store managers, and store teams to clarify customer issues, coordinate resolutions, and keep the service desk running.

### Research Assistant · PES Modern College
**Sep 2023 – Mar 2024** | Research Support · Digital Library · Workshops · Documentation

- Supported research and library work with Prof. Sumit Kanfadi, including documentation, article and book organisation, and day-to-day research activities.
- Helped students use digitised learning resources and supported workshops, library activities, and annual activity reporting.

---

## Projects

### Mia · Personal AI Engineering OS
**TypeScript · Bun · Multi-Host LLM Adapters · Vitest · JSONL State Engine**
[GitHub](https://github.com/thesohamdatta/Mia)

- Built compiled, local-first developer CLI in TypeScript (single Bun binary) automating 5-stage AI engineering harness (grill to spec to plan to review to ship).
- Implemented unified host adapters for Anthropic Claude, OpenAI Codex, and local models with automated verification gates (lint, typecheck, Vitest) and immutable JSONL state tracking.
- Eliminated fragile background daemon architecture in favour of stateless event-driven execution ([ADR-0001](https://github.com/thesohamdatta/Mia/blob/main/docs/decisions/ADR-0001-eliminate-daemon.md)).

### Voice AI Systems · Real-Time Voice Agents & Copilots
**LiveKit WebRTC · Silero VAD · ElevenLabs · Python · Kotlin (Android Compose)**
[John](https://github.com/thesohamdatta/John) · [I-am-Mia](https://github.com/thesohamdatta/I-am-Mia) · [voicecoder](https://github.com/thesohamdatta/voicecoder)

- Built real-time WebRTC conversational voice agents using LiveKit, implementing client-side Silero VAD for barge-in interruption and semantic turn detection.
- Developed **John**: native Android Kotlin client (Jetpack Compose) connected to Python LiveKit agent with tool calling for calendar and task automation.
- Developed **voicecoder**: VS Code extension for voice-driven code editing with multi-provider fallback (Claude, GPT-4o, Gemini, local Ollama) and real-time token cost tracking.

### LLM-Council · Multi-Model Consensus Engine
**Python · FastAPI · React · Vite · Multi-Agent Orchestration**
[GitHub](https://github.com/thesohamdatta/LLM-Council)

- Built multi-LLM consensus engine querying OpenAI, Anthropic, Gemini, and Groq concurrently to cross-evaluate and synthesise peer-reviewed answers.
- Implemented 3-stage critique pipeline (Analyst → Skeptic → Synthesizer) with interactive React frontend visualising step-by-step model agreement.

---

## Skills

**AI Agents & LLMs:** AI Agents, LLM Tool Calling (MCP), Prompt Grounding, Context & Memory Graphs, Multi-Agent Consensus, RAG

**Voice & Multimodal AI:** LiveKit (WebRTC), Silero VAD, Streaming STT/TTS (Deepgram, ElevenLabs), Semantic Turn Detection, TensorFlow, ML Kit, Moondream VLM

**Engineering:** Python (FastAPI, PyTorch, asyncio), TypeScript/JavaScript (Node.js, React, Vite), Kotlin (Android Compose), C/C++ (ESP32 basics), REST APIs, Git/GitHub, Vitest

**Hardware & Product:** 3D CAD Modeling (STL), Wearable Device Packaging, Rapid Prototyping, Human-AI Interaction Design

---

## Education

**Bachelor of Engineering (B.E.) · Artificial Intelligence & Machine Learning**
University of Pune (SPPU) · 2022 – Jun 2026 · Pune, India
