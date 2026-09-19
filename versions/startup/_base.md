# Soham Datta
**AI Engineer · Personal AI · Wearable Systems**  
Pune, India · [LinkedIn](https://www.linkedin.com/in/thesohamdatta/) · [GitHub](https://github.com/thesohamdatta) · [Portfolio](https://sohamdatta.framer.ai)  
*Built:* [Aura](https://github.com/thesohamdatta/aura) · [Mia](https://github.com/thesohamdatta/Mia) · [Voice AI](https://github.com/thesohamdatta/John) · [LLM-Council](https://github.com/thesohamdatta/LLM-Council)

---

## Experience

### Aura · Founder
*Jun 2025 – Present*  
*Wearable AI · Hardware Prototyping · Edge Integration · Open Source*
- Designed and 3D-printed custom CAD enclosures packaging a Seeed Studio XIAO ESP32-S3 Sense, ribbon-cable camera, LiPo battery, and mic porting into a wearable pendant form factor.
- Integrated the physical device with the Omi Glass open-source ecosystem, verifying end-to-end audio streaming and cloud memory capture.
- Diagnosed an Electron WebGL GPU memory leak on Windows caused by CSS backdrop filters over 3D graph canvases in Omi (authored [Issue #8438](https://github.com/BasedHardware/omi/issues/8438), merged downstream in [PR #8902](https://github.com/BasedHardware/omi/pull/8902)).
- Authored offline agglomerative hierarchical clustering (SciPy cosine linkage) with 52 unit tests to solve speaker drift in 3+ person meetings ([PR #8919](https://github.com/BasedHardware/omi/pull/8919), adopted downstream in [PR #12471](https://github.com/BasedHardware/omi/pull/12471)).
- Threaded resolved user_name into extract_action_items() to anchor task attribution on the primary user ([Issue #8918](https://github.com/BasedHardware/omi/issues/8918), implemented in [PR #8919](https://github.com/BasedHardware/omi/pull/8919), adopted downstream in [PR #12089](https://github.com/BasedHardware/omi/pull/12089)).
- Authored Windows local file indexing spec ([Issue #8991](https://github.com/BasedHardware/omi/issues/8991), delivered in merged [#7896/#9595/#10236]) and 1-click Markdown export spec ([Issue #12360](https://github.com/BasedHardware/omi/issues/12360) OPEN; draft [PR #12927](https://github.com/BasedHardware/omi/pull/12927) NOT merged).

### AI & ML Intern · AICTE via Google
*Oct 2024 – Dec 2024*  
*Computer Vision · TensorFlow · ML Kit · Edge Deployment*
- Built and evaluated lightweight computer vision models with TensorFlow and Google ML Kit for on-device edge classification.
- Applied transfer learning and data augmentation pipelines to optimise model inference latency and accuracy under mobile memory constraints.

### Past Experience

- **Associate · Reliance** *(Jul 2024 – Oct 2024)*: Handled the customer service desk across complaints, coupons, memberships, Reliance cards, digital vouchers, exchanges, documentation, and daily follow-up. Worked with brand managers, HR, store managers, and store teams to clarify customer issues and coordinate resolutions.
- **Research Assistant · PES Modern College** *(Sep 2023 – Mar 2024)*: Supported research and library work with Prof. Sumit Kanfadi, including documentation, article and book organisation, and day-to-day research activities. Helped students use digitised learning resources and supported workshops, library activities, and annual activity reporting.

---

## Featured Projects

### Mia · Personal AI Engineering OS
*TypeScript · Bun · Multi-Host LLM Adapters · Vitest · JSONL State Engine*  
[github.com/thesohamdatta/Mia](https://github.com/thesohamdatta/Mia)
- Built a compiled, local-first developer CLI in TypeScript (single Bun binary) that automates a 5-stage AI engineering harness (`grill` → `spec` → `plan` → `review` → `ship`).
- Implemented unified host adapters for Anthropic Claude, OpenAI Codex, and local models with automated verification gates (lint, typecheck, Vitest) and immutable JSONL state tracking.
- Eliminated fragile background daemon architecture in favour of stateless event-driven execution ([ADR-0001](https://github.com/thesohamdatta/Mia/blob/main/docs/decisions/ADR-0001-eliminate-daemon.md)).

### Voice AI Systems · Real-Time Voice Agents & Copilots
*LiveKit WebRTC · Silero VAD · ElevenLabs · Python · Kotlin (Android Compose)*  
[github.com/thesohamdatta/John](https://github.com/thesohamdatta/John) · [github.com/thesohamdatta/I-am-Mia](https://github.com/thesohamdatta/I-am-Mia) · [github.com/thesohamdatta/voicecoder](https://github.com/thesohamdatta/voicecoder)
- Built real-time WebRTC conversational voice agents using LiveKit, implementing client-side Silero VAD for instant barge-in interruption and semantic turn detection.
- Developed **John**: a native Android Kotlin client (Jetpack Compose) connected to a Python LiveKit agent with tool calling for calendar and task automation.
- Developed **voicecoder**: a VS Code extension for voice-driven code editing with multi-provider fallback (Claude, GPT-4o, Gemini, local Ollama) and real-time token cost tracking.

### LLM-Council · Multi-Model Consensus Engine
*Python · FastAPI · React · Vite · Multi-Agent Orchestration*  
[github.com/thesohamdatta/LLM-Council](https://github.com/thesohamdatta/LLM-Council)
- Built a multi-LLM consensus engine querying OpenAI, Anthropic, Gemini, and Groq concurrently to cross-evaluate and synthesise peer-reviewed answers.
- Implemented a 3-stage critique pipeline (Analyst → Skeptic → Synthesizer) with an interactive React frontend visualising step-by-step model agreement.

---

## Technical Skills

- **AI & Agents:** AI Agents, LLM Tool Calling (MCP), Prompt Grounding, Context & Memory Graphs, Multi-Agent Consensus, RAG.
- **Voice & Multimodal:** LiveKit (WebRTC), Silero VAD, Streaming STT/TTS (Deepgram, ElevenLabs), Semantic Turn Detection, TensorFlow, ML Kit, Moondream VLM.
- **Engineering & Software:** Python (FastAPI, PyTorch, asyncio), TypeScript / JavaScript (Node.js, React, Vite), Kotlin (Android Compose), C / C++ (ESP32 basics), REST APIs, Git/GitHub, Vitest.
- **Hardware & Product:** 3D CAD Modeling (STL), Wearable Device Packaging, Rapid Prototyping, Human-AI Interaction Design.

---

## Education

**University of Pune (SPPU)**  
*Bachelor of Engineering (B.E.) in Artificial Intelligence & Machine Learning*  
*2022 – Jun 2026* · Pune, India
