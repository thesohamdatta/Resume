# Soham Datta
**AI Engineering Graduate · Wearable Systems Builder**
Pune, India · [LinkedIn](https://www.linkedin.com/in/thesohamdatta/) · [GitHub](https://github.com/thesohamdatta) · [Portfolio](https://sohamdatta.framer.ai)
[Aura](https://github.com/thesohamdatta/aura) · [Mia](https://github.com/thesohamdatta/Mia) · [Voice AI](https://github.com/thesohamdatta/John) · [LLM-Council](https://github.com/thesohamdatta/LLM-Council)

---

## Experience

### Aura · Founder
*Jun 2025 – Present · Wearable AI · Consumer Hardware · Open Source*

- Design and ship a wearable AI pendant end to end: custom CAD enclosure, ESP32-S3 firmware (FreeRTOS I2S DMA audio at 16 kHz, Opus compression, OTA updates), FastAPI backend, and cloud memory capture.
- Write architectural RFCs (feature specs with user stories covering voice pipeline, virtual memory OS, haptics, context resumption, markdown export) and author 21 issue reports diagnosing user-facing bugs with root causes in a 13.5k-star open-source repo.
- Specs that shipped through others: markdown-export proposal ([Issue #12360](https://github.com/BasedHardware/omi/issues/12360)) built out by community contributors (Electron draft, Flutter patch); speaker-attribution and clustering fixes adopted downstream ([PR #12089](https://github.com/BasedHardware/omi/pull/12089), [PR #12471](https://github.com/BasedHardware/omi/pull/12471)). 3 of 7 authored PRs maintainer-approved (closed unmerged).
- Diagnosed an Electron WebGL GPU memory leak on Windows to CSS backdrop filters over a 3D canvas ([Issue #8438](https://github.com/BasedHardware/omi/issues/8438), merged downstream in [PR #8902](https://github.com/BasedHardware/omi/pull/8902)); voice-pipeline cost/latency audit (10k cap, flash-versus-turbo 2x gap, +50–100ms TLS) with the clustering fix backed by 52 unit tests.

### AI & ML Intern · AICTE via Google
*Oct 2024 – Dec 2024 · Computer Vision · TensorFlow · ML Kit · Edge Deployment*

- Built and evaluated on-device vision models with TensorFlow and Google ML Kit, running transfer-learning and augmentation experiments to trade inference latency against accuracy under mobile memory limits.

### Freelancer · AI & Automation, plus Earlier Roles
*Freelance Sep 2024 – Present: AI agent workflows and automation scripts for student and developer projects.*
*Earlier: Associate at Reliance (Jul–Oct 2024) · Research Assistant, PES Modern College (Sep 2023–Mar 2024).*

---

## Projects

### Voice AI Systems · Real-Time Voice Agents and Mobile Clients
*Python · LiveKit WebRTC · Silero VAD · Kotlin (Android Compose) · TypeScript*
[John](https://github.com/thesohamdatta/John) · [I-am-Mia](https://github.com/thesohamdatta/I-am-Mia) · [voicecoder](https://github.com/thesohamdatta/voicecoder)

- **John**: native Android app (Kotlin/Jetpack Compose) connected to a Python LiveKit agent with tool calling for calendar and tasks; client-side Silero VAD for instant barge-in.
- **voicecoder**: VS Code extension for voice-driven editing with multi-provider fallback (Claude, GPT-4o, Gemini, local Ollama) and real-time token cost tracking per feature use.

### Mia · Personal AI Engineering OS
*TypeScript · Bun · Multi-Host LLM Adapters · Vitest · JSONL State Engine*
[github.com/thesohamdatta/Mia](https://github.com/thesohamdatta/Mia)

- Built a compiled TypeScript CLI running a 5-stage engineering harness (grill → spec → plan → review → ship) with unified model adapters, automated Vitest gates, and immutable JSONL state; recorded the daemon-removal decision in ADR-0001.

### LLM-Council · Multi-Model Consensus Engine
*Python · FastAPI · React · Vite · Multi-Agent Orchestration*
[github.com/thesohamdatta/LLM-Council](https://github.com/thesohamdatta/LLM-Council)

- Built a system that cross-evaluates answers from OpenAI, Anthropic, Gemini, and Groq through an Analyst → Skeptic → Synthesizer pipeline, with a React frontend visualizing model agreement.

---

## Product and Technical Skills

- **Spec and Feedback:** architectural RFCs, issue triage (21 reports, 5 adopted downstream), root-cause write-ups, decision docs (ADR).
- **Data and Measurement:** latency/accuracy tradeoffs, cost/latency audits, usage tracking (token costs), Python analysis.
- **Build:** Python (FastAPI, asyncio), TypeScript/JavaScript (React, Node.js, Vite), Kotlin (Android Compose), C/C++ (ESP32/FreeRTOS), REST APIs, Git/GitHub.
- **Design and Hardware:** Framer portfolio, interaction design, rapid prototyping, 3D CAD (STL), wearable device packaging.

---

## Education

**University of Pune (SPPU)**
*B.E. in Artificial Intelligence & Machine Learning · 2022 – Jun 2026 · Pune, India*
