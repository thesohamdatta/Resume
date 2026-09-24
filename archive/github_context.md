# GitHub Research — Soham Datta

## Executive Summary

- **Subject**: Soham Datta (`thesohamdatta`)
- **Primary Domain**: AI systems, real-time voice agents, wearable hardware prototyping, developer tooling, and agent orchestration.
- **Audited Repositories**: 62 public repositories, including upstream open-source activity in `BasedHardware/omi`.
- **Primary Finding**: Soham exhibits genuine end-to-end builder capability across physical enclosures, embedded firmware (ESP32-S3), real-time WebRTC audio pipelines (LiveKit), and agent orchestration harnesses (TypeScript/Python). 
- **Critical Caveat**: There is an imbalance between bread-and-butter application prototyping and deep distributed systems engineering. Backend infrastructure in projects like `aura` is largely adapted from open-source baselines (Omi ecosystem), and several repositories are forks or proof-of-concept experiments with minimal test coverage and no production telemetry. Claims must reflect hands-on prototyping and integration, not enterprise-scale distributed architecture.

---

## Profile Overview

- **GitHub Profile**: [https://github.com/thesohamdatta](https://github.com/thesohamdatta)
- **Account Creation**: January 29, 2024
- **Public Repositories**: 62
- **Followers / Following**: 4 followers / 34 following
- **Portfolio**: [http://sohamdatta.framer.ai/](http://sohamdatta.framer.ai/)
- **Pinned Repositories**:
  1. [`aura`](https://github.com/thesohamdatta/aura) — Open-source AI wearable pendant ecosystem.
  2. [`LLM-Council`](https://github.com/thesohamdatta/LLM-Council) — Multi-model consensus and peer critique engine.
  3. [`I-am-Mia`](https://github.com/thesohamdatta/I-am-Mia) — Real-time conversational voice agent using LiveKit.
  4. [`skills`](https://github.com/thesohamdatta/skills) — Prompt and agent skill definitions.

---

## Top Projects

The top repositories ranked by code volume, architectural complexity, and demonstrable original engineering:

| Rank | Repository | Primary Stack | Core Focus | Evidence Level |
|---|---|---|---|---|
| 1 | [`aura`](https://github.com/thesohamdatta/aura) | C++, Python, FastAPI, FreeRTOS | Wearable AI pendant, firmware, audio streaming, memory graph | High (1,562 files, CAD STL, firmware code) |
| 2 | [`Mia`](https://github.com/thesohamdatta/Mia) | TypeScript, Node.js, Vitest | Agent execution harness, multi-host LLM adapters, SDLC pipeline | High (Original TypeScript architecture, ADRs) |
| 3 | [`LLM-Council`](https://github.com/thesohamdatta/LLM-Council) | Python, FastAPI, React, Vite | Parallel multi-LLM consensus & peer ranking interface | High (Functional async backend + React UI) |
| 4 | [`John`](https://github.com/thesohamdatta/John) | Kotlin, Android Compose, LiveKit, Python | Android voice client + LiveKit backend agent with tool calling | High (Native Android codebase + Python agent) |
| 5 | [`voicecoder`](https://github.com/thesohamdatta/voicecoder) | TypeScript, VS Code API | Voice-driven IDE coding assistant across Claude/GPT/Gemini/Ollama | Medium-High (Functional extension implementation) |
| 6 | [`codeshot`](https://github.com/thesohamdatta/codeshot) | Python, PyTorch, Moondream 2B | Screen/image code block extraction using Vision-Language Model | Medium (Working local CLI tool) |

---

## Aura

- **Repository**: [`thesohamdatta/aura`](https://github.com/thesohamdatta/aura)
- **Concept**: Screenless wearable pendant capturing ambient audio, streaming compressed packets to cloud services, and building an evolving personal memory graph.
- **Hardware & Embedded Layer**:
  - Target Hardware: Seeed Studio XIAO ESP32-S3 Sense (Xtensa dual-core LX7 @ 240MHz, 8MB PSRAM, 8MB Flash).
  - Code Evidence:
    - `firmware/src/mic.cpp` / `mic.h`: Configures I2S DMA circular buffers for continuous 16kHz 16-bit PCM audio acquisition.
    - `firmware/src/opus_encoder.cpp` / `opus_encoder.h`: Implements on-device Opus compression to reduce network bandwidth.
    - `firmware/src/main.cpp`: FreeRTOS task loops managing audio streaming sockets, BLE/Wi-Fi states, and battery voltage ADC sampling.
    - `firmware/src/ota.cpp`: Over-the-air firmware update handler.
    - `hardware/CASE.stl`: 3D CAD enclosure model tailored for pendant form factor.
    - `firmware/releases/aura_glass_firmware.uf2`: Compiled binary firmware release artifact.
- **Backend & Cloud Layer**:
  - Framework: Asynchronous Python FastAPI.
  - Code Evidence:
    - `backend/routers/transcribe.py`: Streaming audio ingestion endpoint.
    - `backend/routers/memories.py`: Fact extraction and semantic memory chunking.
    - `backend/routers/knowledge_graph.py`: Relationship linking between entities, people, dates, and topics.
    - `backend/routers/mcp.py` & `backend/routers/mcp_sse.py`: Model Context Protocol server exposing tools to LLMs.
    - `backend/migrations/005_backfill_memory_vectors.py`: pgvector vector similarity index migrations.
    - `backend/charts/backend-listen/` & `backend/charts/deepgram-self-hosted/nova-3/`: Kubernetes Helm charts for deploying API ingress, autoscaling, and self-hosted Deepgram Nova-3 ASR.
- **Verification Note on Authorship**:
  - The software architecture and backend routes closely mirror the open-source Omi ecosystem (`BasedHardware/omi`).
  - What Soham genuinely contributed/built: Physical CAD enclosure design (`CASE.stl`), hardware assembly and pin mapping, local firmware builds, custom endpoint adjustments, and testing the end-to-end loop.
  - What was inherited/adapted: Core FastAPI router structure, ASR streaming protocols, and Kubernetes Helm definitions originate from Omi upstream.

---

## Mia

The "Mia" personal agent project spans two distinct repositories:

### 1. `Mia` (Agent CLI & Execution Engine)
- **Repository**: [`thesohamdatta/Mia`](https://github.com/thesohamdatta/Mia)
- **Architecture**: A modular CLI and development harness built in TypeScript, configured with Biome, Knip, and Vitest.
- **Code Evidence**:
  - Multi-Host LLM Adapters (`core/hosts/`):
    - `base-adapter.ts` & `registry.ts`: Common interface defining streaming, tool dispatch, and error isolation.
    - `claude-adapter.ts`: Anthropic Claude Code / SDK integration.
    - `codex-adapter.ts`: OpenAI GPT / Codex provider adapter.
    - `hermes-adapter.ts`: Local model execution adapter.
    - `opencode-adapter.ts`: OpenCode runtime integration.
  - Skill Lifecycle Modules (`core/skills/`):
    - `grill/execute.ts`: Interactive Socratic questioning phase to extract constraints before code generation.
    - `spec/execute.ts` & `plan/execute.ts`: Generation of specifications and test plans.
    - `review/execute.ts` & `ship/execute.ts`: Automated quality verification (lint, typecheck, test suites, git commit/PR creation).
  - Persistence Engine (`core/state/`):
    - `unified-store.ts`, `jsonl-store.ts`: Immutable JSONL execution logging and rollback state tracking.
  - Architectural Discipline:
    - `docs/decisions/ADR-0001-eliminate-daemon.md`: Formal Architectural Decision Record replacing a persistent daemon with stateless event-driven CLI invocations.
    - `tests/integration/core.test.ts`: Integration test suite using Vitest.

### 2. `I-am-Mia` (Real-Time Conversational Voice Agent)
- **Repository**: [`thesohamdatta/I-am-Mia`](https://github.com/thesohamdatta/I-am-Mia)
- **Implementation**: Python, LiveKit Agents SDK (`livekit-agents`), Silero VAD, Deepgram STT, OpenAI/Groq LLM, ElevenLabs TTS.
- **Code Evidence**:
  - `agent.py`: Asynchronous LiveKit room worker handling WebRTC audio streams, barge-in interruption, and latency tuning.
  - `soul.py`: Persona prompts and context assembly.
  - `tools.py`: Function tools decorated with LiveKit's `@function_tool` decorator.

---

## Voice AI Work

Soham has repeated, hands-on implementation experience with the LiveKit WebRTC ecosystem across Python, TypeScript, and Android Kotlin:

| Repository | Tech Stack | Mechanism | Verifiable Evidence |
|---|---|---|---|
| [`I-am-Mia`](https://github.com/thesohamdatta/I-am-Mia) | Python, LiveKit Agents, Silero VAD, ElevenLabs | WebRTC room participant, voice interruption handling, tool execution | `agent.py`, `tools.py` |
| [`John`](https://github.com/thesohamdatta/John) | Kotlin (Android Compose), Python, LiveKit Server SDK, Express | Full client-server voice ecosystem: Android client + token server + tool-calling LiveKit agent | `MainActivity.kt`, `backend/agent/agent.py` |
| [`Livekit-web-agent`](https://github.com/thesohamdatta/Livekit-web-agent) | TypeScript, Next.js, LiveKit Client SDK | Browser-based WebRTC microphone capture, audio playback, visualizer | `src/components/`, `src/hooks/` |
| [`Sarvam-x-Livekit-Agent`](https://github.com/thesohamdatta/Sarvam-x-Livekit-Agent) | Python, LiveKit Agents, Sarvam AI APIs | Indic language voice pipeline (Hindi, Tamil, Bengali) over LiveKit rooms | `agent.py`, pipeline handlers |
| [`Project-Eve`](https://github.com/thesohamdatta/Project-Eve) | Python, LiveKit, Cartesia / ElevenLabs | Conversational companion prototype with prosody/emotional tuning | `agent.py`, system prompts |
| [`voicecoder`](https://github.com/thesohamdatta/voicecoder) | TypeScript, VS Code API | Voice-to-code push-to-talk extension with token cost monitoring | `src/extension.ts`, `src/utils/costTracker.ts` |
| [`assembly-ai-speech-agent`](https://github.com/thesohamdatta/assembly-ai-speech-agent) | Python, LiveKit, AssemblyAI Streaming API | Low-latency streaming STT integration in WebRTC audio rooms | `agent.py` |
| [`audio-restore`](https://github.com/thesohamdatta/audio-restore) | Python, PyTorch, Librosa | Audio signal denoising and speech enhancement algorithms | Jupyter notebooks / scripts |

---

## Omi / Open Source Contributions

- **Target Repository**: [`BasedHardware/omi`](https://github.com/BasedHardware/omi)
- **Verified Metrics**:
  - **Issues Authored**: 21 issues (9 open, 12 closed).
  - **Architectural RFCs & Epics**: 5 authored (#8029, #8985, #9228, #12300, #12360).
  - **Solutions Implemented Downstream by Maintainers**: 5 issues directly resulted in downstream code landings by maintainers or community members.
  - **Pull Requests Authored**: 7 PRs (0 merged directly to `main`, 3 formally approved by maintainers, 7 closed unmerged).
  - **Authored Tests**: 120+ unit and integration test lines across PR branches.

### Key High-Signal Contributions in Omi:
1. **Issue #8438 (GPU Bottleneck Discovery & Fix)**:
   - Root Cause Identified: Found that wrapping React Three Fiber WebGL canvas inside `.surface-card` with CSS `backdrop-filter: blur` forced the Windows Desktop Window Manager (DWM) to recomposite the entire canvas on every DOM tick, causing 50–60%+ continuous GPU load.
   - Downstream Landing: Maintainer `@kodjima33` authored and merged [PR #8902](https://github.com/BasedHardware/omi/pull/8902) referencing and adopting this exact resolution.
2. **Issue #8917 & PR #8919 (Agglomerative Speaker Diarization)**:
   - Problem: Online centroid diarization drifted and merged speakers during 3+ person meetings.
   - Solution: Authored offline Agglomerative Hierarchical Clustering (SciPy average linkage, cosine distance).
   - Code: 52 unit tests written. Adopted downstream in merged PR [#12471](https://github.com/BasedHardware/omi/pull/12471).
3. **Issue #8918 & PR #8919 (User Identity Grounding for Action Items)**:
   - Problem: Action item prompts received generic tags ("Speaker 0"), causing hallucinated task assignment.
   - Solution: Threaded verified user profiles into action item extraction prompts. Adopted downstream in merged PR [#12089](https://github.com/BasedHardware/omi/pull/12089).
4. **Issue #7628 (Browser-Native Screen Rewind & Dependency Audit)**:
   - Documented critical dependency breaks on Windows (`lc3py` missing on PyPI, Deepgram SDK v7 breaking changes). Led directly to merged fixes in PR [#7660](https://github.com/BasedHardware/omi/pull/7660) and PR [#7928](https://github.com/BasedHardware/omi/pull/7928).
5. **Issue #8985 (Virtual Memory OS Epic)**:
   - Authored detailed multi-tiered memory architecture for LLM agent loops, introducing ephemeral cached Anthropic system blocks and hybrid virtual paging.

---

## Other Relevant Projects

- **[`LLM-Council`](https://github.com/thesohamdatta/LLM-Council)**:
  - Multi-agent debate framework querying OpenAI, Anthropic, Gemini, and Groq in parallel.
  - Strips identity markers and runs a 3-stage peer critique (Analyst → Skeptic → Synthesizer).
  - Clean Vite/React frontend visualizing stage-by-stage consensus.
- **[`AutoDev-Studio`](https://github.com/thesohamdatta/AutoDev-Studio)**:
  - Multi-agent software engineering framework executing Standard Operating Procedures (`src/core/sop/workflow.json`) via role-partitioned agents (Planner, Coder, Reviewer, Test Runner).
- **[`codeshot`](https://github.com/thesohamdatta/codeshot)**:
  - Computer vision desktop utility using Moondream 2B (`moondream_handler.py`) to parse clean code blocks directly from IDE screenshots without conventional OCR artifacts.
- **[`DDPM-Diffusion-Based-Agent`](https://github.com/thesohamdatta/DDPM-Diffusion-Based-Agent)**:
  - Mathematical implementation of Denoising Diffusion Probabilistic Models from scratch in PyTorch (UNet, beta schedules, reverse sampling).
- **[`Arxiv-Sanity-Modern`](https://github.com/thesohamdatta/Arxiv-Sanity-Modern)**:
  - Local-first research discovery tool indexing arXiv papers using vector embeddings.

---

## Verified Technology Stack

Technologies verified by direct code presence in repositories:

- **Languages**: Python (FastAPI, PyTorch, asyncio), TypeScript / JavaScript (Node.js, Express, React, Vite), Kotlin (Android Jetpack Compose), C / C++ (ESP32-S3 FreeRTOS).
- **AI & Agent Frameworks**: LiveKit Agents SDK, Anthropic Claude API / MCP, OpenAI API, Groq, Silero VAD, Deepgram STT, ElevenLabs TTS, Hugging Face Transformers, Moondream 2B VLM.
- **Databases & Vector Retrieval**: Supabase / PostgreSQL (`pgvector`), SQLite (`indexed_files`, `rewind_frames`), Pinecone.
- **Hardware & Embedded**: Seeed Studio XIAO ESP32-S3 Sense, I2S DMA buffers, on-device Opus compression, 3D CAD modeling (STL).
- **Tooling & Infrastructure**: Git/GitHub, Docker, Kubernetes Helm charts, Biome, Vitest, VS Code Extension API.

---

## Architecture & Engineering Patterns

1. **Continuous Real-Time Streaming (WebRTC / I2S)**:
   - Streaming circular DMA buffers on edge hardware (`mic.cpp`).
   - Bidirectional real-time WebRTC audio rooms via LiveKit with client-side VAD barge-in interruption (`I-am-Mia`, `John`, `Livekit-web-agent`).
2. **Quality Gates & SDLC Automation**:
   - `Mia` formalizes code generation into a 5-step pipeline: Grill (Socratic interview) → Spec → Plan → Review (tests/lint) → Ship (PR).
   - Rejection of long-running unmanaged background daemons in favor of stateless CLI execution (`ADR-0001`).
3. **Consensus & Peer Critique**:
   - Parallel multi-provider LLM querying with anonymized peer ranking and synthesis (`LLM-Council`).
4. **Local-First & Privacy-Preserving Fallbacks**:
   - Local VLM code parsing (`codeshot`), local file indexing with regex PII scrubbing (`Omi #7628`), and local model execution adapters (`Mia/hermes-adapter.ts`).

---

## Ownership / Authorship Analysis

To distinguish independent work from borrowed or AI-assisted scaffolding:

| Category | Repositories | Evidence of Originality | Nuance / AI Involvement |
|---|---|---|---|
| **Original Architecture & Build** | `Mia`, `LLM-Council`, `John`, `voicecoder`, `codeshot` | Unique folder structures, custom adapters, custom UI components, specific architectural trade-offs documented in ADRs. | Code exhibits patterns of AI-assisted scaffolding (e.g. structured comments, boilerplate generation), but system integration and wiring are original. |
| **Hybrid (Open-Source Core + Custom Hardware/Integration)** | `aura` | Custom 3D printable CAD enclosure (`CASE.stl`), hardware pinout wiring, compiled binaries, local end-to-end testing. | Backend routers and Kubernetes Helm charts are largely derived from `BasedHardware/omi` open-source architecture. |
| **Open-Source Contributions (RFCs & PRs)** | `BasedHardware/omi` | 21 authored issues, detailed GPU/compositor diagnosis, 120+ unit test lines, architectural proposals. | PRs were closed unmerged directly to `main`, but core bug diagnoses and algorithmic proposals were adopted downstream by maintainers. |
| **Forked / Reference Repositories** | `open-wearables`, `about`, `podcastfy`, `open-notebook`, `Sentient`, `SAMANTHA-OS1`, `remma-o1` | Upstream codebases with minimal to zero commit delta. | **Do NOT claim authorship.** These are study references or forks. |

---

## Resume-Worthy Evidence

High-signal facts ready to be used as evidence:
- Designed and 3D-printed physical wearable enclosures (`CASE.stl`) and configured ESP32-S3 firmware to stream Opus-compressed audio over Wi-Fi/BLE (`aura`).
- Built an autonomous engineering CLI in TypeScript with multi-host model adapters (Claude, Codex, Hermes) and immutable JSONL state tracking (`Mia`).
- Authored the root-cause diagnosis for a 50%+ GPU leak in Electron/WebGL by isolating backdrop blur from the 3D graph canvas, adopted upstream in Omi PR #8902 (`omi`).
- Designed and implemented an offline agglomerative hierarchical clustering algorithm with 52 unit tests to solve speaker drift in 3+ speaker audio recordings (`omi PR #8919`).
- Developed a cross-platform voice assistant featuring a native Android Kotlin UI (Jetpack Compose), Express token server, and LiveKit Python tool-calling agent (`John`).
- Built an interactive multi-LLM consensus engine querying 4 model providers in parallel with anonymized peer review stages and a React interface (`LLM-Council`).
- Built a local vision utility utilizing Moondream 2B to extract clean executable code from screenshots without standard OCR degradation (`codeshot`).

---

## Startup-Relevant Evidence

For founders at early-stage AI/wearable startups (NeoSapien, Omi, Bengaluru/SF startups):
- **End-to-End Prototyping Speed**: Able to take a hardware concept from 3D CAD design → ESP32-S3 flashing → mobile/WebRTC streaming → LLM backend.
- **Deep Immersion in Wearable AI**: Intimate familiarity with battery constraints, BLE MTU fragmentation, microphone I2S DMA buffers, and wearable form factors.
- **Ecosystem Contributor**: Proven ability to jump into a complex 15,000+ star open-source repo (`omi`), locate performance bottlenecks, write unit tests, and interact with core maintainers.
- **Builder Mentality**: Doesn't wait for product managers; designs CLI tools (`Mia`), VS Code extensions (`voicecoder`), and multi-model consensus dashboards (`LLM-Council`) to automate his own workflow.

---

## MNC-Relevant Evidence

For ATS screening and technical recruiters at large companies (Google, Microsoft, NVIDIA, Qualcomm):
- **Systems & Edge Programming**: C/C++ FreeRTOS firmware programming on Xtensa ESP32-S3 microcontrollers, I2S audio sampling, Opus codec compression.
- **Software Engineering Hygiene**: Strict TypeScript type-checking, Vitest test suites, Biome linter integration, and formal Architectural Decision Records (ADRs).
- **Core Computer Vision & ML**: Hands-on mathematical implementation of PyTorch diffusion models (`DDPM`) and transformer decoder blocks (`Microgpt124M`), supplemented by AICTE/Google computer vision work (TensorFlow, ML Kit).
- **API & Cloud Integration**: Asynchronous Python FastAPI development, PostgreSQL (`pgvector`) migrations, Docker containerization, and Kubernetes Helm chart configurations.

---

## Projects to Omit

Do NOT feature the following repositories on resumes; they are low-signal, forks, or incomplete:

1. **`about`**: Fork of Humane AI pin documentation with no code delta.
2. **`open-wearables`**: Fork of health data aggregator without original contributions.
3. **`podcastfy`** & **`open-notebook`**: Unmodified forks of open-source NotebookLM tools.
4. **`Sentient`**, **`SAMANTHA-OS1`**, **`remma-o1`**, **`NanoSage`**: Unmodified forks of third-party agent repos.
5. **`OS-ONE`** & **`Aura-soul.md-`**: Theoretical Markdown/LaTeX documents without running code or kernel implementations.
6. **`skills-introduction-to-git`** & **`B.E-Project-Report-Pune-University-Latex-Templates`**: Elementary git exercises and college report templates.
7. **`testtoken`**: Scratchpad repository for testing API tokens.

---

## Claims to Avoid

1. **Do NOT claim commercial manufacturing or retail scale for Aura**:
   - *Reality*: Aura is a functional self-funded prototype on Seeed Studio breakout boards with 3D-printed cases, not a mass-produced consumer hardware product.
2. **Do NOT claim millions of users or production cloud scale**:
   - *Reality*: There are no telemetry records or server metrics indicating high-volume daily active users across any repository.
3. **Do NOT claim merged PR status in Omi main branch**:
   - *Reality*: 7 PRs were authored; none were merged directly by Soham into `main`. The truthful claim is: *"Authored architectural RFCs, bug diagnoses, and algorithms (such as GPU compositor fix and offline diarization) that were adopted and merged downstream by maintainers."*
4. **Do NOT claim to have built a custom distributed cloud backend from scratch for Aura**:
   - *Reality*: The backend is adapted from the open-source Omi ecosystem. Claim ownership of integration, endpoint adaptations, and hardware-to-cloud verification.
5. **Do NOT claim `OS-ONE` is a working operating system**:
   - *Reality*: It is a research paper/specification in LaTeX.

---

## Technical Weaknesses

1. **Lack of Automated Testing in Application Repos**:
   - While `Mia` has Vitest suites and Omi PRs contained unit tests, repositories like `aura`, `LLM-Council`, `John`, and `voicecoder` contain very few or no automated unit/integration tests.
2. **Backend Engineering Depth**:
   - Backend implementations rely primarily on high-level Python FastAPI wrappers and third-party SDK calls. There is little low-level database tuning, custom distributed consensus, or complex caching logic.
3. **Heavy Reliance on Third-Party Cloud APIs**:
   - Intelligence across voice projects is almost entirely outsourced to external API providers (LiveKit Cloud, Deepgram, ElevenLabs, OpenAI, Groq) rather than self-hosted or fine-tuned on-premise models.
4. **Repo Maintenance & Polish**:
   - Many repositories have 0 stars, missing release binaries, and generic commit messages (`"update"`, `"fix"`), indicating rapid personal hacking rather than production OSS maintenance.

---

## Interview Questions & Truthful Defenses

1. **"In Aura, did you write the entire backend yourself?"**
   - *Defensible Answer*: "No. The backend architecture is adapted from the open-source Omi ecosystem. My focus was designing the physical 3D enclosure, writing the ESP32-S3 firmware for I2S audio capture and Opus compression, and adapting the backend endpoints to handle my specific hardware streaming pipeline."
2. **"Why were your Omi PRs closed unmerged?"**
   - *Defensible Answer*: "In large open-source repos, discussions often move fast. In several cases—like the WebGL GPU memory leak (#8438) and the agglomerative diarization algorithm (#8917)—my issue diagnosis and PR code provided the exact blueprint, which core maintainers then refined and committed directly to `main`."
3. **"How does Mia isolate code execution during software tasks?"**
   - *Defensible Answer*: "Mia executes terminal tasks via child process subshells managed by its skill runner (`core/skills/ship/execute.ts`). It captures stdout/stderr and runs automated verification gates (lint, build, typecheck). It is designed as a developer CLI harness rather than a multi-tenant sandboxed cloud hypervisor."
4. **"What latency did you achieve in your LiveKit voice agent experiments?"**
   - *Defensible Answer*: "Using LiveKit WebRTC with Silero VAD for barge-in, Deepgram streaming STT, Groq for fast LLM inference, and ElevenLabs/Cartesia TTS, end-to-end voice-to-voice latency sat between 600ms and 900ms depending on geographic network hops."

---

## Resume Evidence Bank

Specific, code-verified technical snippets ready for future resume construction:

- **Aura (Firmware / Hardware)**:
  `ESP32-S3` · `C++` · `FreeRTOS` · `I2S DMA` · `Opus Codec` · `3D CAD (STL)`
  *Configured FreeRTOS tasks to capture 16kHz audio via I2S DMA buffers, applied on-device Opus compression, and designed custom 3D pendant enclosures (`CASE.stl`).*

- **Aura (Cloud / Integration)**:
  `FastAPI` · `pgvector` · `Kubernetes Helm` · `Deepgram ASR`
  *Adapted FastAPI endpoints and pgvector migrations for semantic memory retrieval; integrated Helm charts for deploying self-hosted Deepgram Nova-3 ASR clusters.*

- **Mia (Agent Harness)**:
  `TypeScript` · `Node.js` · `Vitest` · `JSONL` · `MCP`
  *Architected an extensible agent CLI in TypeScript with unified adapters for Claude, Codex, and local models; implemented immutable JSONL state rollback and Vitest suites.*

- **Omi (Open-Source Systems & Audio)**:
  `SciPy` · `Diarization` · `Electron / WebGL` · `Chromium Compositor`
  *Identified a 50%+ GPU compositor leak on Windows by decoupling Three.js WebGL canvas from backdrop blur filters (adopted in Omi PR #8902); authored agglomerative speaker clustering algorithms with 52 unit tests.*

- **John (Cross-Platform Voice)**:
  `Kotlin` · `Android Jetpack Compose` · `LiveKit WebRTC` · `Python`
  *Built an end-to-end voice assistant pairing an Android Kotlin client with an Express token server and a Python LiveKit tool-calling agent for calendar and task automation.*

- **LLM-Council (Consensus Engine)**:
  `Python` · `FastAPI` · `React` · `Vite` · `Parallel Async`
  *Engineered an asynchronous consensus system querying 4 LLM providers in parallel, running a 3-stage peer critique (Analyst, Skeptic, Synthesizer) rendered on a Vite/React interface.*

---

## Source Links

### Core Repositories
- [thesohamdatta/aura](https://github.com/thesohamdatta/aura)
- [thesohamdatta/Mia](https://github.com/thesohamdatta/Mia)
- [thesohamdatta/LLM-Council](https://github.com/thesohamdatta/LLM-Council)
- [thesohamdatta/John](https://github.com/thesohamdatta/John)
- [thesohamdatta/voicecoder](https://github.com/thesohamdatta/voicecoder)
- [thesohamdatta/I-am-Mia](https://github.com/thesohamdatta/I-am-Mia)
- [thesohamdatta/codeshot](https://github.com/thesohamdatta/codeshot)
- [thesohamdatta/AutoDev-Studio](https://github.com/thesohamdatta/AutoDev-Studio)
- [thesohamdatta/DDPM-Diffusion-Based-Agent](https://github.com/thesohamdatta/DDPM-Diffusion-Based-Agent)

### Upstream Omi Contributions & Pull Requests
- [Omi Issue #8438 — Desktop GPU Leak Diagnosis](https://github.com/BasedHardware/omi/issues/8438)
- [Omi PR #8902 — Merged Downstream Resolution by Maintainer](https://github.com/BasedHardware/omi/pull/8902)
- [Omi Issue #8917 — Agglomerative Diarization Proposal](https://github.com/BasedHardware/omi/issues/8917)
- [Omi PR #8919 — Authored Diarization Implementation & Tests](https://github.com/BasedHardware/omi/pull/8919)
- [Omi PR #12471 — Downstream Diarization Landing](https://github.com/BasedHardware/omi/pull/12471)
- [Omi Issue #7628 — Screen Rewind & Dependency Audit](https://github.com/BasedHardware/omi/issues/7628)
- [Omi PR #7660 — Merged Dependency Fix](https://github.com/BasedHardware/omi/pull/7660)
- [Omi Issue #8985 — Virtual Memory OS Architectural Epic](https://github.com/BasedHardware/omi/issues/8985)
- [Omi Issue #8452 — BLE Dynamic MTU Negotiation](https://github.com/BasedHardware/omi/issues/8452)
