# Soham Datta

Pune, India · [LinkedIn](https://www.linkedin.com/in/thesohamdatta/) · [GitHub](https://github.com/thesohamdatta) · [Portfolio](https://sohamdatta.framer.ai)

---

## Experience

### Founder · Aura
**Jun 2025 – Present** | Wearable AI · Hardware Prototyping · Edge Integration · Open Source

- Designed and 3D-printed custom enclosures for a wearable AI pendant (Seeed XIAO ESP32-S3 Sense) packaging camera, LiPo battery, and mic; wrote FreeRTOS event loops for I2S DMA audio capture at 16 kHz with Opus compression and OTA updates.
- Adapted FastAPI backend from the Omi ecosystem (memory, transcription, knowledge graph, speaker identification routers) with pgvector migrations and Kubernetes-hosted Deepgram Nova-3 ASR; verified hardware-to-cloud audio streaming.
- Diagnosed Electron WebGL GPU memory leak on Windows (authored [Issue #8438](https://github.com/BasedHardware/omi/issues/8438), merged downstream in [PR #8902](https://github.com/BasedHardware/omi/pull/8902)); authored offline SciPy agglomerative clustering with 52 tests for 3+ speaker diarization ([PR #8919](https://github.com/BasedHardware/omi/pull/8919), adopted in [PR #12471](https://github.com/BasedHardware/omi/pull/12471)); threaded user_name into action-item extraction ([Issue #8918](https://github.com/BasedHardware/omi/issues/8918), adopted in [PR #12089](https://github.com/BasedHardware/omi/pull/12089)).
- Authored Windows file indexing spec ([Issue #8991](https://github.com/BasedHardware/omi/issues/8991), delivered in [#7896/#9595/#10236]) and Markdown export spec ([Issue #12360](https://github.com/BasedHardware/omi/issues/12360) OPEN; draft [PR #12927](https://github.com/BasedHardware/omi/pull/12927) NOT merged). Security hardening ([PR #7379](https://github.com/BasedHardware/omi/pull/7379)) and web refactor ([PR #7654](https://github.com/BasedHardware/omi/pull/7654)) approved, closed unmerged.

### AI & ML Intern · AICTE via Google
**Oct 2024 – Dec 2024** | Computer Vision · TensorFlow · ML Kit · Edge Deployment

- Built and evaluated lightweight on-device vision models with TensorFlow and Google ML Kit for mobile edge classification.
- Applied transfer learning and data augmentation to optimize inference latency under mobile memory constraints.

### Freelancer · AI & Automation
**Sep 2024 – Present**

- Built custom AI agent workflows and automation scripts for student and community developer projects.

### Associate · Reliance
**Jul 2024 – Oct 2024**
- Managed store inventory systems, POS workflows, and daily floor operations.

### Research Assistant · PES Modern College
**Sep 2023 – Mar 2024**
- Coordinated academic literature digitization and digital library archival workflows.

---

## Technical Skills

**AI Agents & LLMs:** AI Agents, LLM Tool Calling (MCP), Prompt Grounding, Context & Memory Graphs, Multi-Agent Orchestration, RAG

**Voice & Multimodal AI:** LiveKit (WebRTC), Silero VAD, Streaming STT/TTS (Deepgram, ElevenLabs), TensorFlow, ML Kit, Moondream VLM

**Software Engineering:** Python (FastAPI, PyTorch, asyncio), TypeScript/JavaScript (Node.js, React, Vite), Kotlin (Android Compose), C/C++ (ESP32/FreeRTOS), REST APIs, Git/GitHub, Vitest

**Hardware & Wearables:** 3D CAD (STL), Wearable Device Packaging, ESP32-S3 Firmware, Rapid Prototyping

---

## Projects

### Mia · Personal AI Engineering OS
**TypeScript · Bun · Multi-Host LLM Adapters · Vitest · JSONL State Engine**  
[GitHub](https://github.com/thesohamdatta/Mia)

- Built a compiled TypeScript CLI (single Bun binary) automating a 5-stage AI engineering harness (grill to spec to plan to review to ship) with unified host adapters for Anthropic Claude, OpenAI Codex, and local models.
- Implemented immutable JSONL state tracking, automated verification gates (lint, typecheck, Vitest), and eliminated fragile background daemon architecture via stateless event-driven execution.

### Voice AI Systems · Real-Time Voice Agents & Copilots
**LiveKit WebRTC · Silero VAD · ElevenLabs · Python · Kotlin (Android Compose)**  
[John](https://github.com/thesohamdatta/John) · [I-am-Mia](https://github.com/thesohamdatta/I-am-Mia) · [voicecoder](https://github.com/thesohamdatta/voicecoder)

- Built real-time WebRTC conversational voice agents using LiveKit with client-side Silero VAD for barge-in interruption and semantic turn detection.
- Developed **John**: native Android Kotlin app (Jetpack Compose) connected to a Python LiveKit agent with tool calling for calendar, tasks, and telephony.
- Developed **voicecoder**: VS Code extension for voice-driven code editing with multi-provider fallback (Claude, GPT-4o, Gemini, local Ollama) and real-time token cost tracking.

### LLM-Council · Multi-Model Consensus Engine
**Python · FastAPI · React · Vite · Multi-Agent Orchestration**  
[GitHub](https://github.com/thesohamdatta/LLM-Council)

- Built a multi-LLM consensus engine querying OpenAI, Anthropic, Gemini, and Groq concurrently to cross-evaluate and synthesize peer-reviewed answers.
- Implemented a 3-stage critique pipeline (Analyst to Skeptic to Synthesizer) with an interactive React frontend visualizing step-by-step model agreement.

---

## Education

**Bachelor of Engineering (B.E.) · Artificial Intelligence & Machine Learning**  
University of Pune (SPPU) · 2022 – Jun 2026 · Pune, India
