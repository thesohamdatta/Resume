# Soham Datta
Pune, India · [Portfolio](https://sohamdatta.framer.ai) · [LinkedIn](https://www.linkedin.com/in/thesohamdatta/) · [GitHub](https://github.com/thesohamdatta)  
thesohamdatta@gmail.com · +91 9420984066

---

## Summary

AI engineering graduate (B.E. AI & ML, SPPU 2026) building wearable and voice AI systems end to end: ESP32-S3 firmware, FastAPI backends, React frontends, and native Android clients. Open-source contributor in the Omi wearable ecosystem.

---

## Technical Skills

- **Languages:** Python, TypeScript/JavaScript, Kotlin, C/C++
- **Frameworks:** React, Node.js, FastAPI, Android Jetpack Compose
- **AI/ML:** LLM tool calling (MCP), RAG, multi-agent orchestration, TensorFlow, PyTorch, ML Kit
- **Dev Tools:** Git/GitHub, REST APIs, Vitest, Supabase/pgvector, Kubernetes Helm

---

## Experience

### Aura — Founder
*Jun 2025 – Present · Wearable AI Pendant: ESP32-S3 Firmware, FastAPI Backend, Open Source · Pune, India*

- Designed and 3D-printed custom enclosures packaging a Seeed XIAO ESP32-S3 Sense, ribbon camera, LiPo battery, and mic into a wearable AI pendant. Wrote FreeRTOS event loops for I2S DMA audio capture at 16 kHz with Opus on-device compression and OTA firmware updates.
- Integrated the device with the Omi Glass ecosystem via a FastAPI backend (memory, transcription, knowledge graph, and speaker identification routers) and self-hosted Deepgram Nova-3 ASR on Kubernetes Helm charts.
- Diagnosed an Electron WebGL GPU memory leak on Windows caused by CSS backdrop filters over a React Three Fiber canvas ([Issue #8438](https://github.com/BasedHardware/omi/issues/8438), merged downstream in [PR #8902](https://github.com/BasedHardware/omi/pull/8902)).
- Authored offline agglomerative hierarchical clustering (SciPy cosine linkage, 52 unit tests) fixing speaker drift in 3+ person meetings ([PR #8919](https://github.com/BasedHardware/omi/pull/8919), adopted downstream in [PR #12471](https://github.com/BasedHardware/omi/pull/12471)).

### AI & ML Intern — AICTE via Google
*Oct 2024 – Dec 2024 · Computer Vision: TensorFlow, ML Kit, Edge Deployment · Remote, India*

- Built and evaluated on-device vision models with TensorFlow and Google ML Kit for mobile edge classification.
- Applied transfer learning and data augmentation to trade inference latency against accuracy under mobile memory limits.

## Education

**University of Pune (SPPU)** · Pune, India  
*B.E. in Artificial Intelligence & Machine Learning · 2022 – Jun 2026*

---

## Projects

### John — Android Voice Client
*Kotlin, Jetpack Compose, Python, LiveKit* · [Source Code](https://github.com/thesohamdatta/John)

- Native Android Kotlin app (Jetpack Compose) connected to a Python LiveKit agent via WebRTC, with client-side Silero VAD for instant barge-in, semantic turn detection, and tool calling for calendar, tasks, and telephony.

### LLM-Council — Multi-Model Consensus Engine
*Python, FastAPI, React, Vite* · [Source Code](https://github.com/thesohamdatta/LLM-Council)

- Full-stack multi-LLM system querying OpenAI, Anthropic, Gemini, and Groq concurrently to cross-evaluate and synthesize answers via a 3-stage critique pipeline (Analyst, Skeptic, Synthesizer).
- React/Vite frontend visualizes step-by-step model agreement with streaming output per provider.
