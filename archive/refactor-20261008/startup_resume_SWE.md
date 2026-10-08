# Soham Datta

**Software Engineer | Builder | Backend & Systems**

Pune, India · thesohamdatta@gmail.com · +91 9420984066 · [LinkedIn](https://www.linkedin.com/in/thesohamdatta/) · [GitHub](https://github.com/thesohamdatta) · [Portfolio](https://sohamdatta.framer.ai)

Builds and ships software end to end: backend services and developer tooling in Python and TypeScript, plus C/C++ firmware for a wearable AI device built from scratch.

## Experience

### Founder / Builder · Aura
**Jun 2025 – Present** | Wearable AI System · Python, TypeScript, C/C++ · Under Development

- Built the wearable end to end, owning hardware integration, ESP32-S3 C/C++ firmware (16 kHz I2S DMA audio capture, on-device Opus compression, FreeRTOS tasks, OTA updates), and the backend it talks to.
- Implemented FastAPI REST services for streaming audio ingestion, memory/context extraction, and speaker identification, with Supabase/pgvector vector-memory storage and a Deepgram ASR service deployed on Kubernetes.
- Worked inside the Omi open-source ecosystem: authored offline speaker clustering (SciPy cosine linkage) with 52 unit tests, adopted downstream, and diagnosed a Windows Electron/WebGL GPU memory issue with a filed root-cause report.

### AI/ML Intern · AICTE/EduSkills
**Oct 2024 – Dec 2024** | TensorFlow · TensorFlow Lite · Google ML Kit · Android

- Built and tested on-device computer-vision pipelines with TensorFlow, TensorFlow Lite, and Google ML Kit, covering custom object detection, image classification, and Android inference.

### Customer Service Representative · Reliance
**Jul 2024 – Oct 2024** | Customer Operations

- Handled customer-service, POS, membership, voucher, and reporting workflows while coordinating with store teams.

### Research / Library Assistant · PES Modern College
**Sep 2023 – Mar 2024** | Research Support · Digital Library

- Supported research documentation and digitization, organising 3,000+ pages of archive material with LaTeX and DELNET/OPAC tools.

## Projects

### Mia — AI Engineering CLI
**TypeScript · Bun · Vitest · JSONL** · [GitHub](https://github.com/thesohamdatta/Mia)

- Built a TypeScript CLI on Bun running a five-stage engineering workflow (grill, spec, plan, review, ship) with structured skill executors and multi-provider LLM adapters for Claude, Codex, and local models.
- Kept state in an immutable JSONL event log and gated every stage with automated lint, type-check, and Vitest verification; replaced a background daemon with stateless event-driven execution (ADR-0001).

### LLM-Council — Multi-Model Evaluation Service
**Python · FastAPI · React/Vite** · [GitHub](https://github.com/thesohamdatta/LLM-Council)

- Implemented a FastAPI service and React client that compares and synthesizes responses from multiple LLM providers through an Analyst, Skeptic, Synthesizer pipeline, with OpenRouter as the provider gateway.

### John — Realtime Voice Client
**Kotlin · Jetpack Compose · LiveKit · WebRTC · Python** · [GitHub](https://github.com/thesohamdatta/John)

- Built an Android client in Kotlin/Jetpack Compose that connects over WebRTC to a Python LiveKit agent, using Silero VAD for barge-in and turn detection and tool calling for calendar and task actions.

## Education

**B.E. in Artificial Intelligence & Machine Learning**
Savitribai Phule Pune University (SPPU) · 2022 – Jun 2026 · Pune, India

## Technical Skills

**Languages:** Python, TypeScript/JavaScript, C/C++, Kotlin
**Backend & APIs:** FastAPI, REST APIs, WebSockets, MCP (Model Context Protocol)
**Testing & Foundations:** Git/GitHub, Vitest, unit testing, Data Structures & Algorithms, debugging
**Systems:** ESP32-S3, FreeRTOS, I2S/DMA, Opus, OTA, Kubernetes
**Data:** Supabase/pgvector, Redis, Firebase, Pinecone
**AI/ML:** LLMs, Retrieval-Augmented Generation (RAG), tool calling, multi-agent systems, TensorFlow, PyTorch
