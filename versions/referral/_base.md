# Soham Karande

**AI Engineer | Software | Machine Learning**

Pune, India · [LinkedIn](https://www.linkedin.com/in/thesohamdatta/) · [GitHub](https://github.com/thesohamdatta) · [Portfolio](https://sohamdatta.framer.ai)

## Summary

AI/ML engineer building practical systems across wearable hardware, voice agents, LLM tooling, and backend integration. Strongest work spans Python, TypeScript, embedded firmware, and applied AI projects.

## Experience

### Founder · Aura
**Jun 2025 – Present** | Wearable AI · Embedded Firmware · AI Backend

- Built Aura as a wearable AI pendant: designed a custom 3D-printed enclosure for an ESP32-S3 with camera, microphone, and LiPo battery.
- Wrote FreeRTOS firmware for 16 kHz I2S DMA audio capture, on-device Opus compression, Wi-Fi/BLE event handling, sleep modes, and OTA updates.
- Adapted the FastAPI backend from the Omi ecosystem to turn raw audio into transcripts, vector memory (pgvector), and speaker identity; wired to Kubernetes-hosted Deepgram Nova-3 ASR for end-to-end hardware-to-cloud audio.
- Diagnosed a Windows WebGL GPU memory leak (Issue #8438), root cause: CSS backdrop-filter over a React Three Fiber canvas; merged downstream in PR #8902. Authored offline agglomerative clustering with 52 unit tests for 3+ speaker diarization (PR #8919); adopted downstream in PR #12471.

### AI & ML Intern · AICTE via Google
**Oct 2024 – Dec 2024** | Computer Vision · TensorFlow · ML Kit

- Built and evaluated lightweight computer-vision models with TensorFlow and Google ML Kit for on-device image classification without internet access.
- Applied transfer learning and data augmentation to achieve workable accuracy under mobile memory constraints.

### Associate · Reliance
**Jul 2024 – Oct 2024**

- Handled the customer-service desk: complaints, memberships, digital vouchers, exchanges, and daily follow-up documentation.
- Coordinated with brand managers, HR, and store teams to resolve customer issues.

### Research Assistant · PES Modern College
**Sep 2023 – Mar 2024**

- Researched open courseware, arXiv, and digital learning platforms across CS, healthcare, and engineering; organised resources for the college archive.
- Supported student workshops, guidance, and awareness activities around digital and open learning resources.

## Projects

### Mia · AI Engineering CLI
**TypeScript · Bun · Multi-Host LLM Adapters · Vitest**
[GitHub](https://github.com/thesohamdatta/Mia)

- Built a compiled, local-first developer CLI (single Bun binary) automating a 5-stage harness: grill, spec, plan, review, ship; unified adapters for Claude, Codex, and local models; immutable JSONL state; automated lint and test gates.

### Voice AI Systems · Real-Time Voice Agents
**Python · LiveKit WebRTC · Silero VAD · Kotlin (Android)**
[GitHub](https://github.com/thesohamdatta/John)

- Built real-time conversational voice agents using LiveKit WebRTC with client-side Silero VAD for barge-in interruption and semantic turn detection.
- Developed John: native Android Kotlin app (Jetpack Compose) connected to a Python LiveKit backend with tool calling for calendar and task automation.

### LLM-Council · Multi-Model Consensus Engine
**Python · FastAPI · React · Multi-Agent Orchestration**
[GitHub](https://github.com/thesohamdatta/LLM-Council)

- Built a multi-LLM consensus engine querying OpenAI, Anthropic, Gemini, and Groq concurrently to cross-evaluate and synthesise peer-reviewed answers.
- Implemented a 3-stage critique pipeline (Analyst → Skeptic → Synthesizer) with an interactive React frontend showing step-by-step model agreement.

## Education

**Bachelor of Engineering (B.E.) · Artificial Intelligence & Machine Learning**
University of Pune (SPPU) · 2022 – Jun 2026 · Pune, India

## Technical Skills

**AI/ML:** AI Agents, LLM Tool Calling (MCP), RAG, Multi-Agent Consensus, Computer Vision, TensorFlow, PyTorch, Silero VAD
**Voice/RT AI:** LiveKit (WebRTC), Deepgram, ElevenLabs, Streaming STT/TTS
**Languages:** Python, TypeScript/JavaScript, Kotlin, C/C++
**Engineering:** FastAPI, React, Bun/Node.js, REST APIs, Git/GitHub, Vitest
**Systems:** ESP32-S3, FreeRTOS, I2S DMA, Opus, OTA, pgvector, Kubernetes
