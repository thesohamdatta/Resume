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

### Candidate-reported Aura work and repository artifacts
- Candidate reports approximately 7-8 physical enclosure versions, exploring basic 3D-printed cases, aluminum in different colors, and other materials before arriving at a working DIY pendant case with a magnetic chest clip. The public repository contains a [CASE.stl model](https://github.com/thesohamdatta/aura/blob/main/hardware/CASE.stl); the artifact alone does not establish prototype count or physical test results.
- Candidate reports Aura app logo/color changes, layout and interface-layer adjustments, and simplification across Tasks, Memory, Settings, and Capture. The public app directory does not contain the screen source needed to independently verify these UI changes.
- Candidate reports combined camera/audio outdoor testing; images were low resolution and the visual evaluation was preliminary. No image-quality, accuracy, or robustness metric is established.
- Candidate estimates about 2 hours from a full charge for the camera-and-audio prototype under average active use, varying with usage. Audio-only runtime is unresolved: earlier recollection of about a day conflicts with a later estimate of about 5 hours; the candidate is unsure. Battery capacity was recalled as around 250 mAh but is uncertain. Do not present either runtime as a measured resume metric.

### Aura website front-end contributions
- Verified candidate-authored commit adds a scroll-based hero interaction with parallax/light animation in JavaScript and CSS: [commit](https://github.com/thesohamdatta/aura/commit/a3367638).
- Verified candidate-authored commits extract reusable visual classes and add design tokens/color-system updates: [component classes](https://github.com/thesohamdatta/aura/commit/4c61f13c), [design tokens](https://github.com/thesohamdatta/aura/commit/2c47f57d).
- Verified candidate-authored commit removes 30+ unused CSS classes/keyframes: [CSS cleanup](https://github.com/thesohamdatta/aura/commit/13cf368c).
- These commits support website/front-end implementation evidence; they do not verify changes to the mobile app's screen source.

## Omi capture-health contribution
- Verified: candidate-authored [Issue #14614](https://github.com/BasedHardware/omi/issues/14614) proposes separating capture-source, transcription, and local-durability status rather than treating recording as one boolean.
- Verified: candidate-authored [fork PR #1](https://github.com/thesohamdatta/omi/pull/1) is open and marked draft. At the reviewed snapshot it adds a pure mobile capture-health projection, focused test code, and specifications across five files.
- Status boundary: the PR is not merged. Its description says Flutter tests, formatting, preflight, and the real user-facing mobile path were not run and remain required. Describe this as draft implementation/proposal work, not a shipped Omi feature or verified app behavior.

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

### Work documented from candidate interview
- Searched books, research papers, articles, theses, patents, past university question papers, university archives, digital-library resources, and open courses.
- Guided students and staff in using OPAC, DELNET, college resources, university archives, MIT OpenCourseWare, NPTEL, SWAYAM, AICTE resources, edX, and similar platforms.
- Scanned physical documents and tagged them by domain; structured folders/directories; maintained digital and offline copies, physical drives, and backups; retrieved and shared requested material.
- Supported day-to-day library operations across departmental locations, including access to computers, printers, scanners, physical holdings, and digital resources.
- Supported orientations, workshops, and educational/commemorative activities by arranging learning materials, guiding attendees on access, and recording activities with photos, videos, and feedback for librarian reporting.
- Prepared a research-paper draft on how students access, consume, and use academic information, with Overleaf/LaTeX, ChatGPT, and research tools; professor reviewed/edited it, then it went through the professor and librarian to the college domain. Publication and formal credit are unknown.

### Candidate-reported estimates — not independently verified
- Digitised/organised resources: candidate now estimates 100+ books, articles, papers, old documents, and related resources. This replaced a prior 3,000+ pages claim that the candidate later described as a random guess. No archive inventory was supplied to verify the total.
- Activities: candidate estimates approximately 22–30 institutional activities, possibly 50+ over a year, including orientations, workshops, and commemorative/educational events. Check the event/archive log before using a firm count.
- Student support: candidate estimated probably 100+ students across campus libraries, but explicitly said the count was unknown. Treat as low-confidence and do not use as a resume metric without records.

### Tool evidence (candidate-reported)
Scanning/printing equipment, Excel, Google Drive, local/offline directories and physical drives, backups, college archive/network resources, OPAC, DELNET, Paperpile, Overleaf/LaTeX, ChatGPT, and other research tools. Confirm exact names (including any internal platforms) before a technical resume makes them prominent.

### Attribution and boundaries
- The role involved research and library support; do not claim sole authorship of professor-led publications.
- The research-paper draft was routed through professor and librarian to the college domain; publication, final destination, and formal credit are unknown.
- Do not claim a measured student-learning or efficiency improvement, exact student reach, or verified resource/event totals without underlying records.
- Do not describe archive organisation as Git/version control.

## Reliance

Official title: Associate  
Dates: Jul 2024 – Oct 2024

### Role and workflow
- Reviewed new and pending customer complaints in the Reliance internal portal, identified the customer, issue type, product/brand, and relevant department, then coordinated investigation and assignment.
- Candidate describes work spanning a five-floor store and multiple product departments, with both online and in-store cases. Common case themes included product queries, membership issues, warehouse/stock delays, shipping or delivery damage, and product-related complaints.
- Contacted or coordinated with brand managers, store managers, sales staff, cashiers, inventory, warehouse/delivery staff, and other store locations.
- Tracked cases, escalated complex issues, followed up with customers and staff, confirmed whether issues were resolved, and recorded outcomes in the portal and supporting files.
- For one recalled cross-store case, travelled to another store to retrieve product/transaction details and coordinated with managers and warehouse/product contacts. The final outcome of this example was not established.

### AI-assisted email workflow
- Candidate used Google Bard as a chat-based writing assistant to draft targeted emails using case, customer, brand, employee, and manager details.
- Previously, complaint details and follow-up relied more heavily on manual workbook records and phone/email communication.
- Candidate manually identified/tagged responsible people and continued to own investigation, assignment, ticket updates, escalations, follow-up, and resolution verification.
- Characterize this as a semi-manual workflow with AI-assisted drafting, not an automated ticketing or case-resolution system.

### Documentation improvement and recognition
- Candidate created a reusable Google Docs format for daily issue documentation intended for customer-service, cashier, and inventory staff.
- Whether other staff adopted it and whether it reduced errors or processing time are unconfirmed.
- Candidate recalls positive feedback from brand and inventory managers for problem-solving and speed. Candidate also recalls HR discussing a possible K2 position during hiring, separate from the role; official title remains Associate.

### Candidate-reported metrics — not independently verified
- Approximately 30–60 new and pending cases reviewed/tracked per day, depending on workload.
- Approximately 80% of shared case workload handled by the candidate, with about 20% handled by another person.
- Approximately 80% of workload described as online-related.
- Before Bard, email drafting recalled as taking about 60–70% of the candidate's working time.
- Candidate estimates Bard reduced email-drafting time by about 60–70%.
- Earlier 30–40% and 60–70% resolution-time improvement figures were mentioned, but the exact measures and basis were unclear; do not use as resume results until clarified.

No independent portal reports, time logs, customer-satisfaction data, or before/after measurements were supplied for these figures. Retain them as candidate-reported estimates with caveats; never imply company-verified KPIs.

### Resume boundaries
- Do not use the historical 50% improvement metric without new evidence.
- Do not present the role as software engineering or advanced SAP administration. SAP use was basic operational use.
- Do not claim Bard automatically assigned staff or updated tickets.
- Do not claim the Google Docs template was adopted or improved measurable outcomes without confirmation.
- Do not claim a confirmed outcome or time saving for the cross-store example.

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
