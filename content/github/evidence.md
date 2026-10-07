# Technical Evidence — Soham Datta

This file records technical evidence that can support resume claims. It is evidence, not a marketing summary.

## Aura — Wearable AI

Repository: https://github.com/thesohamdatta/aura

Evidence snapshot:
- 1,562 repository files across hardware, firmware, backend, and infrastructure at the cited snapshot.

### Hardware / firmware
- ESP32-S3 firmware in C/C++.
- I2S DMA circular-buffer audio capture at 16 kHz.
- On-device Opus compression.
- FreeRTOS event handling for device services.
- OTA firmware update support.
- Custom 3D CAD enclosure for the wearable form factor.
- Physical integration of camera, microphone, battery, and wearable enclosure.

### Software / backend
- FastAPI backend components.
- Streaming audio ingestion.
- Memory/context extraction and segmentation.
- Knowledge-graph entity/relationship linking.
- MCP server integration.
- Speaker-identification functionality.
- Kubernetes-hosted Deepgram ASR integration.
- Supabase/pgvector vector-memory storage.
- Frontend/mobile/interface work.

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
- AICTE/EduSkills ecosystem, supported by Google for Developers.
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

Summary:
- 21 issues authored.
- 5 architectural RFCs.
- 7 PRs authored.
- 3 authored PRs approved by maintainers.
- 0 authored PRs merged directly.
- 120+ documented tests.
- 52 tests in the speaker-clustering contribution.

Selected evidence:
- Issue #8438: diagnosed Windows Electron/WebGL GPU/compositor issue; downstream resolution in PR #8902.
- PR #8919: authored offline speaker clustering with 52 tests; closed unmerged; approach adopted downstream in PR #12471.
- Issue #8918: authored speaker-grounding proposal; adopted downstream in PR #12089.
- Issue #8991: authored Windows local file-indexing specification; downstream implementation followed.
- Issue #12360: authored Markdown export specification; draft PR #12927 not merged.
- PR #7379: security hardening, maintainer-approved, closed unmerged.
- PR #7654: web/configuration refactor with 13 integration tests, maintainer-approved, closed unmerged.
- PR #8442: Windows database/OCR/WebSocket work and tests, positively reviewed, closed unmerged.
- PR #8352: type-safety changes requested, closed unmerged.

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

Official title: Customer Service Representative  
Dates: Jul 2024 – Oct 2024

Evidence:
- Customer-service desk.
- POS, memberships, vouchers, exchanges, inventory/store workflows.
- Reporting/data maintenance.
- Documentation and daily follow-up.
- Coordination with managers and store teams.

Do not use the historical 50% improvement metric without new evidence.

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
