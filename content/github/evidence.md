# Technical Evidence — Soham Datta

**What was built, verified by code and documentation.**

---

## Primary Projects

### 1. Aura — Wearable AI Pendant System
**Repository:** [github.com/thesohamdatta/aura](https://github.com/thesohamdatta/aura)  
**Evidence:** 1,562 files across hardware, firmware, backend, Kubernetes charts

#### Hardware & Embedded
- **ESP32-S3 Firmware** (C/C++):
  - `firmware/src/mic.cpp` — I2S DMA circular buffer audio capture at 16kHz
  - `firmware/src/opus_encoder.cpp` — On-device Opus compression
  - `firmware/src/main.cpp` — FreeRTOS event loops for Wi-Fi/BLE, battery monitoring, sleep modes
  - `firmware/src/ota.cpp` — Over-the-air firmware updates
  - Binary release: `firmware/releases/aura_glass_firmware.uf2`
- **Physical Enclosure**: Custom 3D CAD `hardware/CASE.stl` for wearable pendant form factor

#### Backend (Python/FastAPI)
- `backend/routers/transcribe.py` — Streaming audio ingestion
- `backend/routers/memories.py` — Context extraction, fact extraction, memory segmentation
- `backend/routers/knowledge_graph.py` — Entity/relationship linking
- `backend/routers/mcp.py` — Model Context Protocol server
- `backend/routers/speech_profile.py` — Speaker identification

#### Infrastructure
- Self-hosted Deepgram Nova-3 ASR Kubernetes Helm charts
- Supabase/pgvector migrations for vector memory storage

---

### 2. Mia — Personal AI Engineering OS
**Repository:** [github.com/thesohamdatta/Mia](https://github.com/thesohamdatta/Mia)  
**Evidence:** TypeScript CLI, Bun runtime, structured state engine

#### Core Implementation
- **5-Stage Harness**: `grill` → `spec` → `plan` → `review` → `ship`
- **Multi-Host Adapters**: Unified interfaces for Anthropic Claude, OpenAI Codex, local models (`core/hosts/registry.ts`; claude/codex/hermes/opencode adapters)
- **Skill executors**: `core/skills/grill|spec|plan|review|ship/execute.ts`; integration suite `tests/integration/core.test.ts`
- **State Management**: Immutable JSONL state tracking (`unified-store.ts`)
- **Verification Gates**: Automated lint, typecheck, Vitest test execution
- **Architecture Decision**: [ADR-0001](https://github.com/thesohamdatta/Mia/blob/main/docs/decisions/ADR-0001-eliminate-daemon.md) — eliminated fragile background daemon in favor of stateless event-driven execution

---

### 3. Voice AI Systems — Real-Time Voice Agents
**Repositories:**
- [github.com/thesohamdatta/John](https://github.com/thesohamdatta/John) — Android + Python LiveKit agent
- [github.com/thesohamdatta/I-am-Mia](https://github.com/thesohamdatta/I-am-Mia) — Python LiveKit conversational agent
- [github.com/thesohamdatta/voicecoder](https://github.com/thesohamdatta/voicecoder) — VS Code voice coding extension

#### Technical Implementation
- **LiveKit WebRTC Integration**: Real-time bidirectional audio streaming
- **Silero VAD**: Client-side voice activity detection for barge-in interruption and semantic turn detection
- **John (Android + Backend)**:
  - Native Kotlin Jetpack Compose UI
  - Official LiveKit Android SDK integration
  - Python LiveKit agent backend with tool calling (calendar, tasks, telephony, web)
  - Express token service
  - File pointers: `android/John/.../MainActivity.kt`, `backend/agent/agent.py`, `tools/calendar.py`, `tools/phone.py`, `tools/tasks.py`
- **voicecoder (VS Code Extension)**:
  - Multi-provider fallback: Claude Sonnet/Opus, GPT-4o, Gemini 2.5 Pro/Flash, local Ollama
  - Real-time token cost tracking
  - Secure credential storage
  - File pointers: `src/extension.ts`, `src/llm/providerFactory.ts`, `src/utils/costTracker.ts`

---

### 4. LLM-Council — Multi-Model Consensus Engine
**Repository:** [github.com/thesohamdatta/LLM-Council](https://github.com/thesohamdatta/LLM-Council)  
**Evidence:** Python FastAPI backend + React Vite frontend

#### Architecture
- **Multi-Provider Streaming**: OpenRouter integration querying OpenAI, Anthropic, Gemini, Groq concurrently
- **3-Stage Critique Pipeline**: Analyst → Skeptic → Synthesizer
- **Frontend**: Interactive React visualization of step-by-step model agreement and peer ranking
- **File pointers**: `backend/council.py`, `backend/openrouter.py`, `backend/prompts/analyst.py`, `skeptic.py`, `synthesizer.py`, `frontend/.../Stage1-3.jsx`, `ChatInterface.jsx`

---

## Omi Open-Source Contributions

**Target Repository:** [BasedHardware/omi](https://github.com/BasedHardware/omi)  
**Contributor:** `@thesohamdatta`

### Verified Metrics
| Category | Count | Details |
|---|:---:|---|
| **Issues Authored** | 21 | 9 Open, 12 Closed |
| **Architectural RFCs** | 5 | Voice pipeline, Virtual Memory OS, Haptics, Context Resumption, Markdown Export |
| **Issues Implemented Downstream** | 5 | GPU fix (#8902 merged), File indexing (#7896/#9595/#10236 merged), Diarization (#12471 adopted), Grounding (#12089 adopted), Markdown export (#12927 draft + Flutter patch, NOT merged) |
| **Pull Requests Authored** | 7 | 0 Merged directly, 7 Closed unmerged |
| **PRs Approved by Maintainers** | 3 | #7379 (Security), #7654 (Web Refactor), #8919 (Diarization) |
| **Unit Tests Authored** | 120+ | 52 Python tests (PR #8919), 89 DB/WebSocket tests (PR #8442), 13 web tests (PR #7654) |

### Key Technical Contributions

#### Issue #8438: Desktop GPU Memory Leak Diagnosis
- **Problem**: 50-60% GPU load on Windows when 3D knowledge graph visible
- **Root Cause Identified**: CSS `backdrop-filter: blur` over React Three Fiber WebGL canvas forced DWM compositor to re-blend entire WebGL region on every sub-pixel update
- **Solution**: Remove backdrop blur, enforce strict resting thresholds
- **Downstream Resolution**: Maintainer merged [PR #8902](https://github.com/BasedHardware/omi/pull/8902) fixing the issue

#### PR #8919: Offline Agglomerative Hierarchical Clustering for Speaker Diarization
- **Implementation**: SciPy cosine linkage clustering to solve speaker drift in 3+ person meetings
- **Testing**: 52 unit tests included
- **Status**: Closed unmerged, but adopted downstream in [PR #12471](https://github.com/BasedHardware/omi/pull/12471)

#### PR #7379: Security Hardening
- **Scope**: replaced bare `eval()` with `ast.literal_eval()` and `json.loads()` across Redis caching layers (`backend/database/redis_db.py`, `backend/migrations/`, `plugins/db.py`), 4 files, +14/-11 lines.
- **Status**: Approved by maintainer `@kodjima33` ("good security cleanup"), closed unmerged by author — never claim merge.

#### PR #7654: Web Application Refactor
- **Scope**: consolidated hardcoded strings, pricing, brand references, schema.org metadata, and user-agent deep-link routing into central `PRODUCT_CONFIG` (`src/constants/product.ts`), 17 files, +330/-98 lines. Resolved #5855, #4709, #4801.
- **Testing**: 13 web integration tests (`web/frontend/src/__tests__/app-store-cleanup.test.mjs`).
- **Status**: Approved by maintainer `@kodjima33`, closed unmerged — never claim merge.

#### PR #8442: Windows Desktop DB Isolation, WebSocket Classification, OCR Pacing
- **Scope**: fixed `getReadonly()` in `db.ts` to honor `OMI_DB_PATH`; refactored WebSocket fatal classification in `omiListen`; ported macOS async `readFile` + `powerMonitor` battery gating + 100ms throttle to `ocrService.ts`. 6 files, +158/-29 lines.
- **Testing**: `db.test.ts` (70 lines) and `omiListen.test.ts` (19 lines).
- **Status**: Maintainer `@Git-on-my-level` verified "all three points are cleanly addressed... work here is good"; closed unmerged — never claim merge.

#### PR #8352: Test Fixture Type Safety (changes-requested)
- **Scope**: replaced unsafe `as unknown as Type` casts with `@total-typescript/shoehorn` across 13 files (+86/-408).
- **Status**: Maintainer `@Git-on-my-level` requested changes (lockfile prune, ESLint override scope, unrelated files); closed unmerged. Never cite as approved.

#### Issue #8029: Voice Interface RFC
- **Audit**: Identified latency and cost bottlenecks in TTS pipeline
  - 10k daily character cap limiting usage to ~30-40 responses/day
  - Hardcoded expensive `eleven_turbo_v2_5` vs faster/cheaper `eleven_flash_v2_5` (~150ms vs ~75ms, ~2x cost gap)
  - Disabled HTTP keep-alive forcing TLS handshakes (+50-100ms overhead)
  - Cross-platform inconsistency between mobile and desktop TTS

#### Issue #8918: Speaker Grounding for Action Items (dossier traceability)
- **Problem**: action-item prompts received generic tags ("Speaker 0"), misattributing tasks.
- **Fix**: threaded resolved `user_name` into `extract_action_items()` with primary-user ownership constraints (implemented in PR #8919).
- **Downstream**: adopted in PR #12089. Closed unmerged on author side — never claim merge.

#### Issue #12360: 1-Click Markdown Export Spec (live-verified 2026-09-14)
- **Status**: OPEN spec by `@thesohamdatta` (opened Aug 28, 2026): problem statement, 6 user stories, formatting contract, client-side architecture, test invariants, explicit out-of-scope section. Omi 13.5k stars at verification.
- **Downstream**: Electron draft PR #12927 follows the #12360 template exactly (confirmed in maintainer review); community Flutter patch submitted. PR is a Draft — NOT merged, never claim merge.

#### Issue #7628: Browser-Native Screen Rewind with Local OCR (OPEN)
- **Spec**: `getDisplayMedia()` loop, 32x32 grayscale diff skipping redundant frames, IndexedDB `omi_timeline` with FIFO cap, Tesseract.js WASM worker, client-side regex PII redaction.
- **Downstream**: documented `lc3py`/Deepgram SDK/Typesense blockers resolved in merged PRs #7660 and #7928 by `@tianmind-studio`.

#### Issue #8452: Dynamic BLE MTU Negotiation (OPEN, p2)
- **Spec**: register BLE MTU callback in `omiGlass/firmware/src/app.cpp`, fragment Opus frames with 1-byte sub-index header. Cross-referenced in Issue #13265.

#### Issue #8453: Windows SQLite OCR Clustering (OPEN)
- **Spec**: query `rewind_frames`, filter taskbar regions, cluster vertically (delta-y < 10px), serialize to Markdown, Levenshtein dedup (>92%). Contributor confirmed `rewind_frames.ocr_lines_json` landed in main.

#### Issue #8912: Windows TTS Output and VAD Barge-In (OPEN)
- **Spec**: port macOS playback to Web Audio/Electron (2-pass chunking, Float32 AudioWorklet, filler phrases, Silero VAD ONNX <120ms). Turn-identity and barge-in landed on Windows in merged PR #10236.

#### Issue #8985: Virtual Memory OS Epic (OPEN architectural RFC)
- **Design**: 4 slices — core-identity cached Anthropic system blocks with 1h TTL, read-only Settings UI, autonomous `update_core_profile` tool, background token compression (>500 tokens), hybrid virtual paging (5 verbatim + 20 summarized).

#### Issue #8991: Windows Local File Indexing Spec
- **Spec**: recursive Node.js `fs` scan (depth 3), SQLite `indexed_files` persistence for macOS parity.
- **Downstream**: delivered across merged PRs #7896/#9595/#10236, verified at HEAD by maintainer.

#### Dossier boundaries (archive audit — binding on future writers)
- PR #12927 is a Draft (needs-maintainer-review) — do not claim merged or shipped.
- Issues #7525, #7546, #7878 closed by automated triage (stale/speculative) — do not claim implementation.
- PR #8352 received changes-requested — do not cite as approved.
- Forks (`about`, `open-wearables`, `podcastfy`, `open-notebook`, `Sentient`, `SAMANTHA-OS1`, `remma-o1`, `NanoSage`, `swift-chat`) — do not claim authorship.

---

## Additional Projects

### AutoDev-Studio
**Repository:** [github.com/thesohamdatta/AutoDev-Studio](https://github.com/thesohamdatta/AutoDev-Studio)  
**Nature:** Autonomous multi-agent software engineering framework  
**Implementation:** Standard Operating Procedures (SOPs), state machines, role-partitioned agents (Planner, Coder, Reviewer, Test Runner)

### codeshot
**Repository:** [github.com/thesohamdatta/codeshot](https://github.com/thesohamdatta/codeshot)  
**Nature:** Computer vision code extraction tool  
**Implementation:** Moondream 2B Vision Language Model in PyTorch extracting formatted code from screenshots (`moondream_handler.py`, `explainer.py`)

### Sarvam-x-Livekit-Agent
**Repository:** [github.com/thesohamdatta/Sarvam-x-Livekit-Agent](https://github.com/thesohamdatta/Sarvam-x-Livekit-Agent)  
**Nature:** Indic language voice pipeline (Hindi, Tamil, Bengali) over LiveKit rooms  
**Implementation:** Python LiveKit agent with Sarvam AI STT/TTS (`agent.py`)

### DDPM-Diffusion-Based-Agent
**Repository:** [github.com/thesohamdatta/DDPM-Diffusion-Based-Agent](https://github.com/thesohamdatta/DDPM-Diffusion-Based-Agent)  
**Nature:** Denoising Diffusion Probabilistic Models from scratch in PyTorch (UNet, beta schedules, reverse sampling)

### Microgpt124M
**Repository:** [github.com/thesohamdatta/Microgpt124M](https://github.com/thesohamdatta/Microgpt124M)  
**Nature:** 124M-parameter decoder-only transformer in PyTorch (multi-head attention, rotary embeddings, causal masking)

---

## Technical Stack Evidence

**Verified by repository file analysis:**

- **Systems & AI Backend**: Python (FastAPI, PyTorch, LiveKit Agents SDK, HuggingFace Transformers, Librosa, asyncio)
- **Agent Harnesses & Web**: TypeScript/JavaScript (Node.js, Express, React, Vite, Biome, Vitest, Knip, VS Code Extension API)
- **Embedded & Edge**: C/C++ (ESP32-S3 firmware, FreeRTOS, I2S DMA, Opus compression, OTA updates)
- **Mobile**: Kotlin (Android Jetpack Compose, LiveKit Android SDK)
- **Infrastructure**: Kubernetes Helm Charts, Supabase/pgvector migrations, self-hosted ASR
- **Voice AI**: LiveKit WebRTC, Silero VAD, Deepgram, ElevenLabs, AssemblyAI STT

---

## Work Experience

### Aura | Founder
**Dates:** Jun 2025 – Present  
**Evidence:** See Aura project section above — hardware, firmware, backend, infrastructure

### AI & ML Intern | AICTE via Google
**Dates:** Oct 2024 – Dec 2024  
**Focus:** Computer vision with TensorFlow and Google ML Kit for on-device edge classification


### Reliance | Associate
**Dates:** Jul 2024 – Oct 2024  
**Evidence:** Customer service desk, store/POS workflows, documentation, and cross-team coordination

- Handled customer-service work across complaints, coupons, memberships, Reliance cards, digital vouchers, exchanges, documentation, and daily follow-up.
- Worked with brand managers, HR, store managers, and store teams to clarify customer issues and coordinate resolutions.

### PES Modern College / PS Modern Institute | Research Assistant
**Dates:** Sep 2023 – Mar 2024  
**Evidence:** Research support, digital-resource research, student guidance, workshops and awareness activities

- Researched literature, digital learning platforms, and freely available resources across computer science, healthcare, mechanical engineering, electrical engineering, and other student learning domains.
- Gathered and organised information on open courseware, free coding-learning resources, research repositories such as arXiv, books, articles, and the college's own digital archive.
- Helped students discover and use these resources through guidance, workshops, and digital-awareness campaigns focused on learning and research in the digital era.
- Supported library and research documentation, including organisation of books/articles and reporting on annual activities.
