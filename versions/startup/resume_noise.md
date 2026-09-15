# Soham Datta
**AI Engineer · Wearable Systems · Full-Stack**  
Pune, India · [LinkedIn](https://www.linkedin.com/in/thesohamdatta/) · [GitHub](https://github.com/thesohamdatta) · [Portfolio](https://sohamdatta.framer.ai)  
[Aura](https://github.com/thesohamdatta/aura) · [Mia](https://github.com/thesohamdatta/Mia) · [Voice AI](https://github.com/thesohamdatta/John) · [LLM-Council](https://github.com/thesohamdatta/LLM-Council)

---

## Experience

### Aura · Founder
*Jun 2025 – Present · Wearable AI · Embedded Systems · Edge Integration · Open Source*

- Designed and 3D-printed custom enclosures packaging a Seeed XIAO ESP32-S3 Sense, ribbon camera, LiPo battery, and mic into a wearable AI pendant. Wrote FreeRTOS event loops for I2S DMA audio capture at 16 kHz with Opus on-device compression and OTA firmware update support.
- Integrated the device with the Omi Glass ecosystem via a FastAPI backend (memory, transcription, knowledge graph, and speaker identification routers) and self-hosted Deepgram Nova-3 ASR on Kubernetes Helm charts.
- Diagnosed an Electron WebGL GPU memory leak on Windows caused by CSS backdrop filters over a React Three Fiber canvas ([Issue #8438](https://github.com/BasedHardware/omi/issues/8438), merged downstream in [PR #8902](https://github.com/BasedHardware/omi/pull/8902)).
- Authored offline agglomerative hierarchical clustering (SciPy cosine linkage, 52 unit tests) to fix speaker drift in 3+ person meetings ([PR #8919](https://github.com/BasedHardware/omi/pull/8919), adopted downstream in [PR #12471](https://github.com/BasedHardware/omi/pull/12471)).

### AI & ML Intern · AICTE via Google
*Oct 2024 – Dec 2024 · Computer Vision · TensorFlow · ML Kit · Edge Deployment*

- Built and evaluated on-device vision models with TensorFlow and Google ML Kit for mobile edge classification; applied transfer learning and data augmentation to reduce inference latency under mobile memory constraints.

### Freelancer · AI & Automation  &  Past Roles
*Sep 2024 – Present · Built AI agent workflows and automation scripts for student and developer projects.*  
*Earlier: Associate at Reliance (Jul–Oct 2024) · Research Assistant, PES Modern College (Sep 2023–Mar 2024)*

---

## Projects

### Voice AI Systems · Real-Time Voice Agents & Mobile Clients
*Python · LiveKit WebRTC · Silero VAD · Kotlin (Android Compose) · TypeScript*  
[John](https://github.com/thesohamdatta/John) · [I-am-Mia](https://github.com/thesohamdatta/I-am-Mia) · [voicecoder](https://github.com/thesohamdatta/voicecoder)

- **John**: native Android Kotlin app (Jetpack Compose) connected to a Python LiveKit agent via WebRTC — client-side Silero VAD for instant barge-in, tool calling for calendar, tasks, and telephony.
- **voicecoder**: VS Code extension for voice-driven code editing with multi-provider LLM fallback (Claude, GPT-4o, Gemini, local Ollama) and real-time token cost tracking.
- Built real-time conversational voice agents with semantic turn detection using LiveKit and ElevenLabs streaming TTS.

### LLM-Council · Multi-Model Consensus Engine
*Python · FastAPI · React · Vite · OpenAI · Anthropic · Gemini · Groq*  
[github.com/thesohamdatta/LLM-Council](https://github.com/thesohamdatta/LLM-Council)

- Built a full-stack multi-LLM system querying OpenAI, Anthropic, Gemini, and Groq concurrently to cross-evaluate and synthesize answers via a 3-stage critique pipeline (Analyst → Skeptic → Synthesizer).
- React/Vite frontend visualizes step-by-step model agreement with streaming output per provider.

### Mia · Personal AI Engineering OS
*TypeScript · Bun · Multi-Host LLM Adapters · Vitest · JSONL State Engine*  
[github.com/thesohamdatta/Mia](https://github.com/thesohamdatta/Mia)

- Built a compiled TypeScript CLI (single Bun binary) running a 5-stage AI engineering harness (grill → spec → plan → review → ship) with unified adapters for Claude, OpenAI, and local models, automated Vitest gates, and immutable JSONL state tracking.

---

## Technical Skills

- **AI & Agents:** LLMs, Tool Calling (MCP), RAG, Prompt Grounding, Multi-Agent Orchestration, Signal Processing
- **Voice & Multimodal:** LiveKit (WebRTC), Silero VAD, Deepgram Nova-3, ElevenLabs, TensorFlow, PyTorch, ML Kit
- **Engineering:** Python (FastAPI, asyncio), TypeScript/JavaScript (React, Node.js, Vite), Kotlin (Android Compose), C/C++ (ESP32/FreeRTOS), REST APIs, Git/GitHub
- **Hardware & Wearables:** 3D CAD (STL), ESP32-S3 Firmware (I2S DMA, Opus, OTA), Wearable Device Packaging, Kubernetes Helm

---

## Education

**University of Pune (SPPU)**  
*B.E. in Artificial Intelligence & Machine Learning · 2022 – Jun 2026 · Pune, India*
