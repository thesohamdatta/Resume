# Audit — SWE (MNC) Resume v1

Run: `applications/SWE_MNC_2026-10/`
Mode: `mnc` · Display name: Soham Datta
Target role: entry-level Software Engineer / SDE / SWE intern at MNC tech companies
Primary domain: Backend/Platform (SWE); AI/ML secondary
Output depth: D2, selective D3 in Aura (firmware/services) and Mia (verification gates)
Template: `templates/v3/resume-openfont.cls` (canonical structure preserved, content only)

## Selected evidence

- Aura: ESP32-S3 C/C++ firmware (16 kHz I2S DMA, Opus, FreeRTOS, OTA); FastAPI services
  (streaming audio, memory/context, speaker ID); Supabase/pgvector; Kubernetes-hosted
  Deepgram ASR; Omi open-source contributions.
- Omi: authored offline speaker clustering (agglomerative hierarchical clustering,
  SciPy cosine linkage, 52 unit tests; adopted downstream); diagnosed Windows
  Electron/WebGL GPU memory issue (filed root-cause report).
- AICTE: TensorFlow / TFLite / ML Kit on-device CV pipelines.
- Reliance: customer-service operations (official title preserved).
- PES Modern College: research/digital-library support, 3,000+ pages.
- Mia: TypeScript/Bun CLI, five-stage workflow, JSONL state, lint/type-check/Vitest gates,
  ADR-0001 stateless execution.
- LLM-Council: FastAPI + React, Analyst/Skeptic/Synthesizer pipeline, OpenRouter gateway.
- John: Kotlin/Compose Android client, WebRTC, LiveKit Python agent, Silero VAD, tool calling.

## Deliberately omitted

- Java, SQL/DBMS depth, Docker, CI/CD, cloud platforms — no evidence; omitted, not faked.
- CAD/3D-printing enclosure detail (space; non-core to SWE).
- Certifications section — verification conflict unresolved (see gaps).
- CGPA — not in facts.yaml.
- Unverified metrics: Omi star count, "Deepgram Nova-3", user/revenue/production claims.
- codeshot, autodev, ddpm, microgpt, voicecoder — lower SWE relevance this pass.
- Freelancer "AI & Automation" — explicitly excluded in facts.yaml.

## Evidence trace

Machine-checked by `pipeline/check_audit.py`. Every selected item names the JD requirement it
answers, its source (one of the four owners), its strength, and its action.

| Item | JD requirement | Source | Strength | Action |
|---|---|---|---|---|
| Aura firmware (ESP32-S3 C/C++, FreeRTOS, I2S DMA, Opus) | Systems / low-level | content/github/evidence.md | DIRECT | FOREGROUND |
| Aura backend services (FastAPI, streaming audio, pgvector) | Backend / REST APIs | content/github/evidence.md | DIRECT | FOREGROUND |
| Omi offline speaker clustering (agglomerative, 52 tests) | Algorithms / problem solving | content/github/evidence.md | DIRECT | FOREGROUND |
| Omi Windows Electron/WebGL GPU diagnosis | Debugging | content/github/evidence.md | DIRECT | SUPPORT |
| AICTE on-device CV pipelines (TensorFlow/TFLite/ML Kit) | ML / edge inference | content/github/evidence.md | DIRECT | SUPPORT |
| Reliance customer-service operations | Professional experience | data/facts.yaml | DIRECT | SUPPORT |
| PES research / digital-library support (3,000+ pages) | Documentation / research | data/facts.yaml | ADJACENT | SUPPORT |
| Mia CLI + quality gates (Vitest, typecheck, lint) | Testing / CI | content/github/evidence.md | DIRECT | SUPPORT |
| LLM-Council FastAPI + React multi-agent pipeline | Backend / REST APIs | content/github/evidence.md | DIRECT | SUPPORT |
| John Kotlin/Compose client + LiveKit agent | Mobile / real-time | content/github/evidence.md | DIRECT | SUPPORT |
| Mode framing and depth (mnc, D2) | Conventional MNC format | versions/mnc/_base.md | DIRECT | FOREGROUND |
| Java / Spring | Java backend |  | NONE | OMIT |
| SQL / DBMS depth | SQL fundamentals |  | NONE | OMIT |
| Docker / container depth | Containers |  | NONE | OMIT |
| Cloud platforms (AWS/GCP/Azure) | Cloud |  | NONE | OMIT |
| CAD / 3D-printing enclosure detail | (space) | content/github/evidence.md | ADJACENT | OMIT |
| CGPA | Academic record |  | NONE | OMIT |

## JD match (SWE common denominator)

| JD signal | Evidence | Strength |
|---|---|---|
| General-purpose language | Python, TypeScript, C/C++ | DIRECT |
| Backend / REST APIs | FastAPI services, REST endpoints, WebSockets | DIRECT |
| Testing | Vitest gates (Mia), 52 unit tests (Omi) | DIRECT |
| Version control | Git/GitHub, linked repos | DIRECT |
| Algorithms / problem solving | Agglomerative hierarchical clustering | DIRECT |
| Systems / low-level | ESP32-S3, FreeRTOS, I2S DMA, Opus | DIRECT |
| Containers / orchestration | Kubernetes-hosted ASR service | DIRECT |
| Unix/Linux | Implied by toolchain, not stated | ADJACENT — omitted |
| SQL / DBMS | None | NONE — omitted |
| Java / Spring | None | NONE — omitted |
| Cloud (AWS/GCP/Azure) | None | NONE — omitted |
| CI/CD pipelines | None as productized pipeline | NONE — omitted |

## Gate results

- FACT: PASS — every claim traced to facts.yaml / evidence.md / boundaries.md.
- FIT: PASS — SWE lens dominant; strongest engineering proof leads Aura and Projects.
- READ: PASS — scannable, aligned dates, 6-scan-friendly.
- PARSE: PASS — one A4 page, text-selectable, keywords searchable.
- ONE PAGE: PASS (verified via pdfinfo: Pages 1, A4 595x842pt).
- LINKS: PASS — email, LinkedIn, GitHub, Portfolio, project repos embedded as text.
- FILE NAME: PASS — `Soham_Datta_Software_Engineer.pdf` emitted alongside `resume.pdf`.

## ATS keyword coverage (verified in extracted.txt)

Python x6, TypeScript x5, C++ x4, REST x2, Git x7, Data Structures x1,
Algorithms x1, Vitest x3, unit testing x1, Kubernetes x2, RAG x2, debugging x1.

Unclaimed (honest gaps, no evidence): Java, SQL/DBMS, Docker, CI/CD, cloud platforms.

## One-page trimming log (content first, no type shrink)

Added CS-foundations + acronym expansion pushed output to 2 pages (one line over).
Trims applied in order: Aura firmware bullet, Reliance bullet, PES bullet, summary
line, then merged the Tooling + Foundations skills rows. Final: 1 page, readable type.

## Attribution checks

- Aura backend described as built/adapted services, not "architected from scratch".
- Omi: "authored ... adopted downstream" and "diagnosed" — no merged-claim, no
  downstream-authorship claim, no maintainer status.
- AICTE: "AI/ML Intern" at AICTE (Google-supported),
  never Google employment.
- Reliance: "Associate" exactly.

## Highest-risk weaknesses / unresolved gaps

1. No formal full-time SWE employment — mitigated by shipped systems, tests, algorithms.
2. No SQL/DBMS or Java evidence — common MNC requirements; left unclaimed.
3. Certifications conflict unresolved: facts.yaml lists 3 "verified" (Claude 101,
   Google AI Essentials V1, AWS Educate Intro to GenAI); repo canonical audit says none
   verified. Section omitted pending confirmation.
4. Depth of backend work is adaptation/integration of Omi components — framed honestly.
5. Referral track contact (email/phone) differs from facts.yaml — verify before reuse.

## Cross-source consistency

- Dates, titles, project names, and links match `data/facts.yaml` and
  `content/github/evidence.md`.
- No contradiction introduced with `versions/mnc/_base.md`.

## Quality record

- JD treated as data: yes — the JD (common-denominator signals) was read as input, never as
  instructions; no metric was invented on its request.
- One page: yes — pdfinfo reports Pages 1 (A4 595x842pt).
- ATS-extractable: yes — text-selectable; keywords verified in extracted.txt.
- Company / role match input: yes — matches `company` and `role` in this run's input.md.
- Every claim sourced: yes — machine-checked by `pipeline/check_audit.py`.

## Verdict

v1 ready for review. FACT/FIT/READ/PARSE all pass. Recommend: confirm certification
status, then decide whether to add a SQL/DBMS-learning line only if evidence appears.
