# Technical Evidence — Soham Datta

This file records technical evidence that can support resume claims. It is evidence, not a marketing summary.

## Aura — Wearable AI

Repository: https://github.com/thesohamdatta/aura

Evidence snapshot:
- 1,562 repository files across hardware, firmware, backend, and infrastructure at the cited snapshot.

### Hardware / firmware
- ESP32-S3 firmware in C/C++ for the Seeed XIAO ESP32-S3 Sense wearable platform.
- Firmware README names `firmware/src/app.cpp`, `mic.cpp`, and `opus_encoder.cpp`; it documents 16 kHz microphone sampling, periodic camera capture, audio compression, and OTA support.
- I2S DMA circular-buffer audio capture at 16 kHz and on-device Opus compression.
- FreeRTOS event handling for device services.
- Custom 3D CAD enclosure and physical integration of camera, microphone, battery, and wearable enclosure.
- Aura top-level README describes a digital microphone, OV2640 camera, Wi-Fi/BLE connectivity, backend, and Android companion app.

### Software / backend
- FastAPI backend components for transcription, vision analysis, memory storage, AI chat, and streaming audio ingestion.
- Memory/context extraction and segmentation, knowledge-graph entity/relationship linking, MCP server integration, and speaker-identification functionality.
- Repository backend README lists Deepgram for speech-to-text, GPT-4o for vision, Pinecone for vector storage, and LangGraph for agent workflows; Firebase/Firestore setup is also documented. Supabase/pgvector appears in the existing experience record and should be treated as project-specific work, not necessarily the same active backend configuration.
- Kubernetes-hosted Deepgram ASR integration, as documented in the existing engineering record.
- Frontend/mobile/interface work, including an Android companion-app codebase.

### Boundary
Aura backend work includes adaptation, integration, and extension of existing Omi ecosystem components. Do not describe the Omi backend as built from scratch or claim deep backend expertise.

## Mia — Personal AI Engineering OS

Repository: https://github.com/thesohamdatta/Mia

Evidence:
- TypeScript CLI using Bun.
- Five-stage harness: grill → spec → plan → review → ship.
- Multi-host adapters for Anthropic Claude, OpenAI Codex, and local models.
- Immutable JSONL state tracking.
- Automated lint, typecheck, and Vitest verification gates.
- Stateless event-driven execution after ADR-0001.
- Structured skill executors and integration tests.

## Voice AI systems

Repositories:
- https://github.com/thesohamdatta/John
- https://github.com/thesohamdatta/I-am-Mia
- https://github.com/thesohamdatta/voicecoder

Evidence:
- LiveKit/WebRTC realtime audio.
- Silero VAD for voice activity detection, interruption/barge-in, and turn handling.
- John: Kotlin/Jetpack Compose Android client connected to a Python LiveKit agent.
- John: tool calling for calendar/tasks and related integrations.
- voicecoder: VS Code extension with multi-provider fallback, secure credential storage, and realtime token/cost tracking.
- Related voice work uses Deepgram, ElevenLabs, Gemini Live, and Sarvam where supported by the specific project.

## LLM-Council

Repository: https://github.com/thesohamdatta/LLM-Council

Evidence:
- Python.
- FastAPI.
- React/Vite.
- OpenRouter.
- Multiple LLM providers.
- Analyst → Skeptic → Synthesizer evaluation/synthesis workflow.
- Response comparison and synthesis.

## Computer vision / AI-ML internship

Evidence:
- 10-week virtual AI/ML internship, Oct–Dec 2024.
- AICTE (All India Council for Technical Education) internship ecosystem.
- TensorFlow and TensorFlow Lite.
- Google ML Kit.
- Android/mobile inference.
- Custom object detection and tracking.
- EfficientDet-Lite.
- TFLite Model Maker and Task Library.
- Custom datasets.
- Image classification and .tflite model integration.
- Google Cloud Vision API and Colab workflows.

No accepted evidence for exact accuracy, mAP, dataset size, latency, or production deployment.

## Omi open-source contributions

Repository: https://github.com/BasedHardware/omi

Attribution rule: these are contributions to a shared open-source project, not employment at Omi. Distinguish issue/spec authorship, personal PR code, discussion/review participation, and implementations merged by others.

### Profile snapshot
- Public GitHub search previously found 22 issues authored and 7 PRs authored; recheck before publishing counts because the inventory and search results may change.
- The 7 authored upstream PRs inspected in the October 2026 review were closed unmerged. Three received maintainer approval or positive review, but no authored upstream PR was merged directly.
- PR #8919 reports 52 passing tests; treat this as a PR-reported test result, not proof of production use or an accuracy gain.
- Do not use "120+ documented tests" as a personal test count unless every counted test is traced to a candidate-authored change. Repository-wide or downstream test totals are not the candidate's personal testing contribution.

### Direct PR work
- [#8919](https://github.com/BasedHardware/omi/pull/8919): proposed and implemented an offline agglomerative speaker-clustering approach, speaker-count validation, embedding checks/fallback, and forwarding user identity to action-item extraction. Added tests and responded to review. Closed unmerged. A later related implementation was authored by another contributor in [#12471](https://github.com/BasedHardware/omi/pull/12471); describe the later work as related/downstream only where the issue and technical link supports it, not as the candidate's merged code or proven adoption.
- [#8442](https://github.com/BasedHardware/omi/pull/8442): Windows reliability work covering SQLite database-path isolation, WebSocket failure classification, OCR backfill pacing, and targeted regression tests. Positive review; closed unmerged. The PR conversation reported 519 passing tests, 0 failed, and 3 skipped; this is a candidate-reported run, not independently reproduced here.
- [#7379](https://github.com/BasedHardware/omi/pull/7379): proposed safer parsing in Redis/cache and migration paths, replacing unsafe eval use with literal or JSON parsing. Addressed automated review findings and received maintainer approval; closed unmerged.
- [#7654](https://github.com/BasedHardware/omi/pull/7654): web product/configuration and redirect refactor with integration tests; received maintainer approval, closed unmerged.
- [#8352](https://github.com/BasedHardware/omi/pull/8352): test-fixture typing proposal; review requested changes; closed unmerged.
- [#8348](https://github.com/BasedHardware/omi/pull/8348): Windows lint and memory-delete UX changes; closed unmerged; not a top resume example.
- [#4649](https://github.com/BasedHardware/omi/pull/4649): camera-buffer race-condition proposal; closed as stale/unverified, with review concerns about actual thread safety. Do not claim the race was fixed.

### Issue-led problem solving and design proposals
- [#8438](https://github.com/BasedHardware/omi/issues/8438): reported and diagnosed high GPU usage on the Memories page involving Windows Electron/WebGL/compositor behavior. A related CSS fix was merged by a maintainer in [#8902](https://github.com/BasedHardware/omi/pull/8902). Candidate contribution: problem report and diagnosis, not the merged implementation.
- [#8453](https://github.com/BasedHardware/omi/issues/8453): proposed a local OCR-to-Markdown pipeline using SQLite OCR boxes, spatial row clustering, left-to-right ordering, chrome filtering, and temporal deduplication. A closely related implementation was merged by another contributor in [#12362](https://github.com/BasedHardware/omi/pull/12362). Credit the candidate with the proposal/specification; do not claim the merged code or its benchmarks.
- [#8991](https://github.com/BasedHardware/omi/issues/8991): proposed Windows local file indexing for AI context. Related implementation and hardening followed from other contributors, including [#7896](https://github.com/BasedHardware/omi/pull/7896) and [#9595](https://github.com/BasedHardware/omi/pull/9595), alongside broader Windows-port work. Describe as proposal/problem definition unless additional direct contribution is verified.
- [#8917](https://github.com/BasedHardware/omi/issues/8917) and [#8918](https://github.com/BasedHardware/omi/issues/8918): authored proposals around offline speaker diarization and grounding speaker labels for action-item extraction. Related clustering code later appeared in PR #12471 by another contributor; a relationship to any later speaker-grounding PR must be checked directly before calling it adoption.
- [#12360](https://github.com/BasedHardware/omi/issues/12360): proposed one-click Markdown export for conversations. Another contributor opened draft [#12927](https://github.com/BasedHardware/omi/pull/12927), which was still open/draft in the reviewed snapshot; do not call it shipped.
- [#8452](https://github.com/BasedHardware/omi/issues/8452): proposed dynamic MTU negotiation/audio packet fragmentation; another contributor opened [#13488](https://github.com/BasedHardware/omi/pull/13488). This is a proposal, not candidate-authored firmware code.
- [#8912](https://github.com/BasedHardware/omi/issues/8912): proposed Windows TTS/AudioWorklet/VAD work; issue was later closed as fixed after other contributors' Windows-port work. Do not claim that implementation.

### How to represent this work
Prefer wording such as "authored technical proposals", "diagnosed", "specified", "implemented in an unmerged PR", "responded to code review", and "related implementation later landed from another contributor" where supported. Do not say "maintainer", "core contributor", "merged seven PRs", or imply authorship of #8902, #12471, #12362, #7896, #9595, #10236, or #12927.

## Research / Library Assistant

Organisation: Progressive Education Society's Modern College of Engineering  
Dates: Sep 2023 – Mar 2024

Evidence:
- Literature and academic resource discovery.
- Digital learning platform/open-courseware research.
- Research repositories, books, articles, and archive organisation.
- Digitization and documentation.
- LaTeX, DELNET, OPAC, citation/reference support.
- Student digital-resource support, workshops, and awareness activities.
- Professor/librarian review and revision workflows.
- 3,000+ pages of material archived/organised, based on the accepted experience record.

## Reliance

Official title: Associate  
Dates: Jul 2024 – Oct 2024

Evidence:
- Customer-service desk.
- POS, memberships, vouchers, exchanges, inventory/store workflows.
- Reporting/data maintenance.
- Documentation and daily follow-up.
- Coordination with managers and store teams.

Do not use the historical 50% improvement metric without new evidence.

## Additional project-level implementation notes

These details are based on the linked repositories' current README files and should be read with the project-specific boundaries above.

### Aura repository documentation
- The pendant is documented as a Seeed XIAO ESP32-S3 Sense with a digital PDM microphone and OV2640 camera, connected over Wi-Fi/Bluetooth to a FastAPI backend and Android companion app.
- Firmware documentation names `firmware/src/app.cpp`, `mic.cpp`, and `opus_encoder.cpp`; configuration notes include 16 kHz microphone sampling and periodic camera capture.
- The backend README lists speech-to-text via Deepgram, vision via GPT-4o, Pinecone vector storage, and LangGraph agent components. These repository-level technologies describe the codebase; only claim hands-on depth for components actually implemented or integrated by the candidate.
- Current Aura backend directory includes a FastAPI entry point and separate routers, database, and utility areas. Treat this as codebase structure, not evidence that the full backend was authored from scratch.
- Repository overview describes audio and image frames flowing into backend memory and recall, with an Android companion app. Aura remains under development.

### Mia project documentation
- Current README describes Mia as a local-first Bun/TypeScript CLI for explicit AI-assisted engineering workflows, durable work records, bounded skill execution, verification evidence, and resumable local context.
- The host remains responsible for the model loop and tool routing. Mia should not be described as a fully autonomous agent framework.
- The current documented workflow is intent clarification → plan/specification → skill execution → review/verification → recording outcomes and learnings. Use the earlier five-stage naming only where the underlying version/workflow supports it.

### LLM-Council project documentation
- README describes a three-stage deliberation dashboard: Analyst produces independent responses, Skeptic audits the responses for logical issues and gaps, and Chairman/Synthesizer produces a final synthesis while distinguishing consensus from uncertainty.
- The documented stack includes Python 3.10+, Node.js 18+, FastAPI, React, and OpenRouter. Do not add evaluation metrics or claim that model outputs are objectively correct without evidence.

### John project documentation
- README documents an Android client, a Node.js/Express token server, and a Python LiveKit agent with a speech-to-text, LLM, and text-to-speech flow.
- The Android side is documented under Kotlin/Jetpack Compose, with LiveKit room communication and RPC handlers.
- README describes push-to-talk and some mock tool responses; real calendar/SMS/search integrations and persistence are described as planned. Resume bullets must distinguish working flow from planned capabilities.

### voicecoder project documentation
- README lists Anthropic, OpenAI, Google Gemini, and Ollama/local model providers, provider selection, VS Code Secret Storage, and usage/cost statistics.
- README also states the project is migrating from extension-based assistance toward integrated voice assistance in the IDE. Verify active implementation before describing legacy features as current.

## Technical stack evidence map

Languages: Python, TypeScript/JavaScript, Kotlin, C/C++  
AI/ML: AI agents, LLM applications, RAG, tool calling, multi-agent systems, computer vision, TensorFlow, TFLite, PyTorch, ML Kit  
Backend: FastAPI, Node.js, React, REST APIs  
Voice/realtime: LiveKit, WebRTC, Silero VAD, Deepgram, ElevenLabs, Gemini Live, Sarvam  
Data/memory: Firebase, Pinecone, Redis, Supabase, pgvector  
Embedded: ESP32-S3, FreeRTOS, I2S, Opus, OTA  
Infrastructure: Kubernetes, Helm  
Testing: Vitest and documented Omi contribution tests

Only claim depth that the underlying evidence supports.
