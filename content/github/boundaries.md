# Truth Boundaries — Resume Claim Control

This file is binding. No resume track may outrun these boundaries.

## Global rules

- Truth outranks persuasion.
- Never turn exposure into expertise.
- Never turn contribution into ownership of an entire system.
- Never turn a prototype into production.
- Never turn a virtual internship into employment at a sponsoring organisation.
- Never turn an approved PR into a merged PR.
- Never turn downstream adoption into direct authorship.
- Never turn academic/research support into sole authorship.
- Never use an unverified metric as a measured KPI.
- Official employment titles remain truthful.
- Project status must remain accurate.

## Aura

### Can claim
- Independent wearable AI project under development.
- Founder role.
- Custom 3D-printed/CAD enclosures.
- ESP32-S3 firmware integration and implementation.
- I2S audio capture, DMA buffering, Opus compression, FreeRTOS event handling, OTA updates.
- Adapted/extended Omi ecosystem software and backend components.
- FastAPI components for streaming audio, memory/context, knowledge graph, MCP, and speaker identification.
- Kubernetes-hosted Deepgram ASR integration.
- Supabase/pgvector vector-memory work.
- Frontend/mobile/interface work.
- Omi open-source issues, proposals, debugging, testing, and downstream adoption evidence.

### Do not claim
- VC funding, investors, customers, users, revenue, or traction.
- Production-scale deployment.
- Complete backend architecture built from scratch.
- "Built the Omi backend."
- Deep backend expertise.
- Verified battery, latency, accuracy, or user metrics.
- Candidate-reported 7-8 enclosure versions may be described as an approximate iteration count, not as a performance result.
- Describe the current case as a candidate-reported working prototype with a magnetic chest clip; do not infer durability, comfort, image quality, or measured reliability.
- Candidate reports Aura interface and branding changes across Tasks, Memory, Settings, and Capture, but the public repository does not include app screen source to verify implementation details. Avoid claiming specific shipped UI behavior unless further evidence is found.
- Candidate's camera-plus-audio runtime estimate is approximate and usage-dependent; audio-only estimates conflict. Do not use either as a resume metric.
- Candidate reports preliminary low-resolution outdoor images and no strong visual test; do not claim vision quality or accuracy.

## Omi open-source contributions

### What this work represents
Omi contributions include issue-based problem identification, technical design/specifications, code in authored PRs, and discussion/review participation. Record each separately. This is not employment at Omi and does not establish maintainer/core-contributor status.

### Current GitHub snapshot
- A prior public GitHub search found 22 issues authored and 7 upstream PRs authored; recheck counts before using them in a submitted resume.
- The 7 authored upstream PRs inspected in October 2026 were closed unmerged; some received maintainer approval or positive review.
- PR #8919 reported 52 passing tests; this is a PR-reported result, not proof of production use or accuracy improvement.
- Do not treat "120+ documented tests" as personal tests without tracing each test to candidate-authored work.
- Omi issue #14614 and the candidate's fork PR #1 are separate from the seven upstream PR count. PR #1 is open/draft and unmerged; its Flutter/app-path verification is outstanding, so do not claim upstream acceptance or shipped behavior.

### Claim rules
Allowed, when source-linked:
- authored a technical issue or specification
- diagnosed a defect and documented evidence
- proposed a design or implementation approach
- implemented code in an unmerged PR
- added tests and responded to review feedback
- a related implementation later appeared in another contributor's PR, when the relationship is evidenced

Do not claim:
- merged 7 PRs, Omi maintainer, or core contributor
- authorship of downstream PRs
- that unmerged PRs shipped
- that another contributor adopted the candidate's idea unless the issue/PR explicitly links or discusses it
- performance gains from a diagnosis unless a merged fix measured those gains and the candidate's role is described accurately

### Selected evidence with attribution
- [Issue #8438](https://github.com/BasedHardware/omi/issues/8438): candidate reported/diagnosed the GPU/compositor problem. Related fix merged by a maintainer in [PR #8902](https://github.com/BasedHardware/omi/pull/8902).
- [PR #8919](https://github.com/BasedHardware/omi/pull/8919): candidate's offline clustering implementation and tests; closed unmerged. Related code by another contributor later merged in [PR #12471](https://github.com/BasedHardware/omi/pull/12471). Do not imply the candidate-authored PR was merged or proven causal.
- [Issue #8453](https://github.com/BasedHardware/omi/issues/8453): candidate's OCR-to-Markdown proposal. Closely related implementation by another contributor merged in [PR #12362](https://github.com/BasedHardware/omi/pull/12362). Benchmarks/tests reported in that PR belong to that implementation, not the candidate.
- [Issue #8991](https://github.com/BasedHardware/omi/issues/8991): candidate's Windows file-indexing specification; related implementation/hardening came from other contributors, including [PR #7896](https://github.com/BasedHardware/omi/pull/7896) and [PR #9595](https://github.com/BasedHardware/omi/pull/9595).
- [Issues #8917](https://github.com/BasedHardware/omi/issues/8917) and [#8918](https://github.com/BasedHardware/omi/issues/8918): diarization and speaker-grounding proposals. Verify direct links before calling any later work an adoption.
- [Issue #12360](https://github.com/BasedHardware/omi/issues/12360): Markdown export proposal; draft [PR #12927](https://github.com/BasedHardware/omi/pull/12927) belonged to another contributor and was not merged in the reviewed snapshot.
- [Issue #8452](https://github.com/BasedHardware/omi/issues/8452): dynamic MTU/audio fragmentation proposal; related [PR #13488](https://github.com/BasedHardware/omi/pull/13488) was authored by another contributor.
- [Issue #8912](https://github.com/BasedHardware/omi/issues/8912): Windows TTS proposal; later closed as fixed after work by other contributors.
- [PR #7379](https://github.com/BasedHardware/omi/pull/7379): safer parsing, maintainer-approved, closed unmerged.
- [PR #7654](https://github.com/BasedHardware/omi/pull/7654): web configuration refactor, maintainer-approved, closed unmerged.
- [PR #8442](https://github.com/BasedHardware/omi/pull/8442): Windows DB/WebSocket/OCR reliability work with targeted tests, positively reviewed, closed unmerged.

## AI/ML virtual internship

### Can claim
- 10-week virtual AI/ML internship, Oct–Dec 2024.
- AICTE (All India Council for Technical Education) internship ecosystem.
- Computer vision, TensorFlow, TensorFlow Lite, Google ML Kit, Android/mobile inference.
- Custom object detection, EfficientDet-Lite, TFLite Model Maker, image classification, Google Cloud Vision API, Colab.

### Do not claim
- Google employee, Google Engineer, or Google ML Engineer.
- Production ML deployment.
- Unsupported accuracy, mAP, latency, dataset size, or model-ownership metrics.

## Research / Library Assistant

### Can claim
- Research / Library Assistant at Progressive Education Society's Modern College of Engineering.
- Sep 2023 – Mar 2024 based on the accepted experience record.
- Literature/resource discovery, research documentation, digitization, archive organisation, LaTeX, DELNET, OPAC, student digital-resource support, workshops and awareness activities.
- 3,000+ pages of material archived/organised when the source figure is retained.

### Do not claim
- Sole authorship of professor-led publications.
- Independent publications without direct evidence.
- Git/version-control engineering.
- Specific student reach, publication counts, or measurable learning outcomes without evidence.

## Reliance

- Official title: Associate; dates Jul 2024 – Oct 2024.
- Can claim customer support operations, end-to-end complaint/ticket coordination, cross-team escalation, customer follow-up, documentation, POS, Excel, and basic SAP use.
- Can describe Google Bard use for email drafting as a practical AI-assisted workflow improvement; it was semi-manual and human-directed, not an automated ticketing or resolution system.
- Candidate-reported estimates may be stored in facts.yaml for future API/resume selection, but must retain explicit candidate-estimate status and caveats:
  - 30–60 new and pending cases reviewed/tracked per day.
  - Approximately 80% of shared workload handled by candidate.
  - Approximately 80% online-related workload.
  - Email writing estimated at 60–70% of working time before Bard.
  - Email-writing time estimated by candidate to have reduced 60–70% with Bard.
- These metrics were not independently measured or verified. Do not present them as company-confirmed performance KPIs or state them without attribution/caveat.
- Earlier 30–40% and 60–70% resolution-time improvement figures are ambiguous and remain on hold until their exact meaning is clear.
- Do not invent customer satisfaction scores, business/revenue impact, error reductions, time savings outside the candidate estimate, or resolution rates.
- Do not claim Bard automatically assigned employees, changed ticket status, or resolved complaints; candidate retained manual control of assignment, escalation, follow-up, and closure.
- Candidate created a Google Docs documentation template; adoption and measurable effect are unconfirmed.
- Candidate recalls a cross-store investigation involving travel to another store to retrieve product/transaction details; final outcome was not established.
- Do not treat the K2 discussion as a confirmed title, promotion, or held position. Official title remains Associate.
- Do not present this role as software engineering or advanced SAP administration.

## Mia

### Can claim
- TypeScript/Bun CLI.
- 5-stage harness: grill → spec → plan → review → ship.
- Multi-host LLM adapters.
- Immutable JSONL state.
- Verification gates.
- Stateless event-driven execution.

### Do not claim
- Production deployment.
- Fully autonomous software engineering.
- Adoption/user metrics without evidence.

## Voice projects

### Can claim
- LiveKit/WebRTC voice-agent systems.
- Silero VAD for barge-in/turn detection.
- John Android Kotlin + Python LiveKit agent.
- voicecoder VS Code extension with multi-provider fallback and token/cost tracking.

### Do not claim
- Production voice platform or verified real-user scale.

## Project documentation boundaries

- Aura repository documentation lists FastAPI, Deepgram, GPT-4o vision, Pinecone, and LangGraph in its backend overview. The broader evidence record also documents Supabase/pgvector work. Do not imply every listed provider was used in the same active configuration; confirm the specific component and version before making a resume claim.
- Aura firmware README describes camera capture, audio capture, BLE/audio streaming, and OTA support. Use implementation-level specifics only where they are supported by the code or contribution history.
- Mia's current README describes a local-first engineering workflow tool. The host owns model execution and tool routing. Do not call Mia fully autonomous, and use the current workflow wording rather than stale stage names unless a specific version is being described.
- John documentation distinguishes implemented voice interaction and mocked tool responses from integrations marked planned. Do not claim real calendar, SMS, search, or persistence integrations as shipped without current implementation evidence.
- VoiceCoder documentation says the project is migrating from a VS Code extension toward integrated IDE voice assistance. Verify the present implementation before describing older extension features as active.
- LLM-Council documentation describes staged analysis, critique, and synthesis. Do not claim objective correctness, quantified model-quality gains, or evaluation benchmark results without measurements.

## General writing constraints

Avoid generic buzzwords such as passionate, innovative, cutting-edge, leveraged, spearheaded, transformative, next-generation, disruptive, game-changing, revolutionary.

Prefer concrete verbs:
built, designed, implemented, integrated, adapted, investigated, tested, authored, evaluated, contributed, supported, iterated.
