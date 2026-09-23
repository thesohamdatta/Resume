# Omi Open-Source Contribution Record

This file is a reusable evidence layer for the resume and portfolio. It records public Omi issues and pull requests authored by @thesohamdatta and distinguishes candidate-authored work from downstream maintainer work.

Repository: https://github.com/BasedHardware/omi
Contributor: @thesohamdatta

## Contribution summary

- 21 issues authored
- 5 architectural RFCs
- 7 pull requests authored
- 3 pull requests approved by maintainers
- 120+ tests authored across relevant contributions
- Omi work is supporting engineering evidence under Aura, not a separate employment role

## Resume-relevant issues and PRs

### GPU / desktop performance

- Issue #8438 — Electron/WebGL GPU memory leak diagnosis
  https://github.com/BasedHardware/omi/issues/8438
  Candidate contribution: diagnosed the Windows Electron/WebGL GPU memory problem and documented the root cause.
  Downstream implementation: PR #8902
  https://github.com/BasedHardware/omi/pull/8902
  Attribution: PR #8902 was not authored by the candidate.

### Speaker diarization and action-item grounding

- PR #8919 — offline speaker diarization + action-item attribution
  https://github.com/BasedHardware/omi/pull/8919
  Candidate contribution: authored the offline agglomerative hierarchical clustering approach and user-identity grounding changes.
  Verification: 52 tests.
  Status: closed unmerged.

- Issue #8918 — speaker grounding for action items
  https://github.com/BasedHardware/omi/issues/8918
  Candidate contribution: identified the missing primary-user identity in action-item extraction.
  Downstream implementation: PR #12089
  https://github.com/BasedHardware/omi/pull/12089
  Attribution: PR #12089 was not authored by the candidate.

### Security

- PR #7379 — replace unsafe eval() with ast.literal_eval()/json.loads()
  https://github.com/BasedHardware/omi/pull/7379
  Candidate contribution: security hardening across Redis-related paths.
  Status: approved by a maintainer, closed unmerged.

### Web application architecture

- PR #7654 — centralize product, pricing, branding, metadata, and redirect configuration
  https://github.com/BasedHardware/omi/pull/7654
  Candidate contribution: consolidated configuration and deep-link behavior and added 13 integration tests.
  Status: approved by a maintainer, closed unmerged.

### Windows desktop / OCR / database isolation

- PR #8442 — DB path isolation, WebSocket fatal classification, OCR backfill pacing
  https://github.com/BasedHardware/omi/pull/8442
  Candidate contribution: authored the proposed fixes and tests across desktop Windows paths.
  Status: positively reviewed, closed unmerged.

### Test fixture type safety

- PR #8352 — safer TypeScript test fixtures
  https://github.com/BasedHardware/omi/pull/8352
  Candidate contribution: proposed replacement of unsafe type assertions with typed fixture helpers.
  Status: changes requested, closed unmerged.
  Do not use this PR as evidence of approval.

## Architectural issues / RFCs

- Issue #8029 — Voice interface RFC
  https://github.com/BasedHardware/omi/issues/8029
  Focus: TTS latency, cost, connection reuse, and cross-platform voice behavior.

- Issue #8452 — dynamic BLE MTU negotiation
  https://github.com/BasedHardware/omi/issues/8452
  Focus: BLE MTU negotiation and Opus frame fragmentation.

- Issue #8453 — Windows SQLite OCR clustering
  https://github.com/BasedHardware/omi/issues/8453
  Focus: OCR line clustering and Markdown-oriented extraction.

- Issue #8912 — Windows TTS output and VAD barge-in
  https://github.com/BasedHardware/omi/issues/8912
  Focus: desktop audio playback, Silero VAD, and interruption handling.

- Issue #8985 — Virtual Memory OS
  https://github.com/BasedHardware/omi/issues/8985
  Focus: persistent agent memory, profile updates, compression, and virtual paging.

- Issue #8991 — Windows local file indexing
  https://github.com/BasedHardware/omi/issues/8991
  Focus: local recursive file indexing and SQLite persistence.
  Downstream work: PRs #7896, #9595, and #10236.

- Issue #12300 — ambient context resumption
  https://github.com/BasedHardware/omi/issues/12300
  Focus: returning concise context and next actions when a user resumes work.

- Issue #12360 — one-click Markdown summary export
  https://github.com/BasedHardware/omi/issues/12360
  Focus: a self-contained Markdown packet for sharing conversation takeaways and action items.
  Status: open specification; downstream implementation remains separate and is not candidate-authored.

- Issue #7628 — browser-native screen rewind with local OCR
  https://github.com/BasedHardware/omi/issues/7628
  Focus: local screen rewind, OCR, IndexedDB retention, frame deduplication, and local PII handling.

## Claim rules

Use:
- "authored" for candidate-authored issues, RFCs, and PRs.
- "diagnosed" for the GPU investigation.
- "approved" only for PRs explicitly approved by maintainers.
- "closed unmerged" when relevant to prevent ambiguity.
- "addressed downstream" or "adopted downstream" when another PR implemented the idea.

Never claim:
- merged candidate PRs when they were closed unmerged
- authorship of downstream PRs
- maintainer status
- production deployment
- customer or user counts
- downstream implementation as direct candidate ownership
