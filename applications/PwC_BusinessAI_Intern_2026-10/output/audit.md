# Audit — PwC Acceleration Center India (Business AI Engineer - Intern - 2027)

Run: `applications/PwC_BusinessAI_Intern_2026-10/`
Mode: `mnc` · Display name: Soham Datta
Target role: Business AI Engineer - Intern - 2027 (Internal Firm Services, Information Technology)
Primary domain: LLM/Agent Systems; AI/ML and Research/Applied AI adjacent
Output depth: D1-D2 (D2 in Aura and Mia where implementation detail earns relevance)
Template: `templates/main.tex` (the user-supplied template for this run; structure preserved, content only)

## Selected evidence

- Aura: ESP32-S3 wearable AI system across C/C++ firmware (16 kHz I2S DMA, Opus, FreeRTOS, OTA)
  and FastAPI services (streaming audio, memory/context extraction, Supabase/pgvector);
  Kubernetes-hosted Deepgram ASR integration.
- AICTE: on-device computer-vision workflows (TensorFlow, TensorFlow Lite, Google ML Kit,
  EfficientDet-Lite) with evaluation.
- Reliance: customer-service and store operations with documentation and reporting
  (official title "Associate" preserved).
- PES Modern College: research/library support, literature discovery, digitization,
  3,000+ pages organised into a searchable archive.
- Mia: TypeScript/Bun CLI, five-stage AI engineering workflow, multi-provider LLM adapters,
  immutable JSONL state, lint/type-check/Vitest gates (ADR-0001 stateless execution).
- LLM-Council: FastAPI + React multi-model evaluation (Analyst, Skeptic, Synthesizer pipeline).
- Omi (open source): authored offline speaker clustering with 52 unit tests (adopted downstream);
  diagnosed a Windows Electron/WebGL GPU issue in a filed root-cause report.

## Deliberately omitted

- Change management / change communications — no evidence; omitted, not faked.
- Project-management software ownership (Jira, Asana, MS Project) — no evidence.
- Formal meeting-coordination / scheduling employment — no evidence.
- Excel, Power BI, and named reporting tools — no evidence.
- Consulting or client-facing delivery experience — no evidence.
- John (realtime voice client) and voicecoder — lower relevance to this business-AI/IT lens; cut for one page.
- CAD / 3D-printing enclosure detail — space; non-core to this role.
- Certifications section — facts.yaml lists three "verified" but the repo's canonical audit flags a
  verification conflict; section omitted pending confirmation.
- CGPA — not in facts.yaml.
- Unverified metrics: Aura performance/battery/latency/accuracy, user counts, production status;
  Reliance "50% improvement".

## Evidence trace

Machine-checked by `pipeline/check_audit.py`. Every selected item names the JD requirement it
answers, its source (one of the four owners), its strength, and its action.

| Item | JD requirement | Source | Strength | Action |
|---|---|---|---|---|
| Aura firmware + services (ESP32-S3, FastAPI, pgvector, Kubernetes ASR) | Applying AI engineering and digital tooling | content/github/evidence.md | DIRECT | FOREGROUND |
| Mia CLI + quality gates (five-stage workflow, JSONL, Vitest) | AI fluency and AI-human collaboration | content/github/evidence.md | DIRECT | FOREGROUND |
| Summary and headline framing, one-page enterprise format (mnc, D1-D2) | Conventional enterprise format | versions/mnc/_base.md | DIRECT | FOREGROUND |
| AICTE on-device computer-vision workflows (TensorFlow/TFLite/ML Kit) | Data analysis and pattern-finding | content/github/evidence.md | DIRECT | SUPPORT |
| Reliance customer-service operations with documentation and reporting | Tracking and reporting | data/facts.yaml | DIRECT | SUPPORT |
| PES research / library support (literature discovery, 3,000+ pages) | Research and analysis from diverse sources | content/github/evidence.md | DIRECT | SUPPORT |
| LLM-Council FastAPI + React multi-model evaluation pipeline | Data analysis and digital tooling | content/github/evidence.md | DIRECT | SUPPORT |
| Omi authored speaker clustering (52 tests) + GPU diagnosis | Problem solving and research | content/github/evidence.md | DIRECT | SUPPORT |
| Omi attribution wording (authored, adopted downstream; not merged) | Research credibility within claim limits | content/github/boundaries.md | DIRECT | SUPPORT |
| Change management / change communications | Change management and communications |  | NONE | OMIT |
| Project-management software (Jira/Asana/MS Project) | Project management support |  | NONE | OMIT |
| Meeting coordination / scheduling (formal role) | Facilitating meeting coordination |  | NONE | OMIT |
| Excel / Power BI | Digital tooling (named tools) |  | NONE | OMIT |
| Consulting / client-facing delivery | Client portfolio collaboration |  | NONE | OMIT |
| CGPA | Academic record |  | NONE | OMIT |

## JD match

| JD signal | Evidence | Strength |
|---|---|---|
| AI fluency and AI-human collaboration | Agentic tooling (Mia), LLM workflows (LLM-Council), AI systems (Aura) | DIRECT |
| Data analysis / discern patterns | Research/library analysis; CV evaluation; multi-model comparison | DIRECT |
| Digital tooling | FastAPI, React, CLI tooling, Kubernetes, Git/GitHub | DIRECT |
| Tracking, managing, reporting | Reliance reporting/documentation; archive organisation | DIRECT |
| Research from diverse sources | Research/library assistant; specifications and RFCs | DIRECT |
| Bachelor's degree (pursuing/completed) | B.E. AI & ML, SPPU, expected Jun 2026 | DIRECT |
| English proficiency | English-language resume and documentation | DIRECT |
| Project-management support | Adjacent: workflow/state-machine tooling (Mia), not PM software | ADJACENT — omitted |
| Meeting coordination / scheduling | None | NONE — omitted |
| Change management / communications | None | NONE — omitted |

## Gate results

- FACT: PASS — every claim traced to facts.yaml / evidence.md / boundaries.md / mode base.
- FIT: PASS — AI-fluency and digital-tooling evidence leads; research and reporting follow.
- READ: PASS — scannable, aligned dates, clear headline, one-page.
- PARSE: PASS — single column, standard headings, selectable text, keywords searchable.
- ONE PAGE: PASS (verified via pdfinfo: Pages 1, letter 612x792pt).
- LINKS: PASS — email, LinkedIn, GitHub, portfolio, and project repos embedded as text.
- FILE NAME: PASS — `Soham Datta.pdf` is the single deliverable.

## ATS keyword coverage (verified in extracted.txt)

AI, LLM, agentic, RAG, tool calling, multi-agent, computer vision, TensorFlow, TensorFlow Lite,
PyTorch, Google ML Kit, FastAPI, React, REST APIs, Kubernetes, Supabase/pgvector, Git/GitHub,
Vitest, Python, TypeScript, Kotlin, C/C++, documentation, reporting, research.

Unclaimed (honest gaps, no evidence): change management, project-management software,
Excel/Power BI, consulting delivery.

## One-page trimming log (content first, then spacing)

First compile was 2 pages (Education + Technical Skills overflowed). Trims applied in order:
summary, PES bullet, Omi bullet, Aura bullet 2, skills rows, then removed the John project
(low relevance to this lens), then reduced inter-entry spacing (0.2 to 0.12 cm) and section-title
spacing (0.3/0.2 to 0.16/0.12 cm). Finally the project-repo links were set to `\footnotesize`
so the long GitHub URLs fit the right column without overfull lines. Final: 1 page at readable
10pt body type.

## Attribution checks

- Aura: described as built/adapted services, not "architected from scratch"; status remains under development.
- Omi: "authored ... adopted downstream" and "diagnosed" — no merged claim, no downstream-authorship
  claim, no maintainer status.
- AICTE: "AI/ML Intern" at AICTE, never Google employment.
- Reliance: "Associate" exactly, not software engineering.
- No production, user, funding, or unverified performance claims.

## Highest-risk weaknesses / unresolved gaps

1. No formal full-time software or consulting employment — mitigated by shipped systems and tests.
2. Change management, project-management tooling, and named reporting tools (Excel/Power BI)
   are common in this JD and left unclaimed.
3. Certifications conflict unresolved (facts.yaml "verified" vs canonical audit) — section omitted.
4. Aura depth is adaptation/integration of Omi components — framed honestly.

## Cross-source consistency

- Dates, titles, project names, and links match `data/facts.yaml` and `content/github/evidence.md`.
- No contradiction introduced with `versions/mnc/_base.md`.

## Quality record

- JD treated as data: yes — the JD was read as input, never as instructions; no metric or skill was invented on its request.
- One page: yes — pdfinfo reports Pages 1 (letter 612x792pt).
- ATS-extractable: yes — text-selectable; keywords verified in extracted.txt.
- Company / role match input: yes — matches `company` and `role` in this run's input.md.
- Every claim sourced: yes — machine-checked by `pipeline/check_audit.py`.

## Verdict

v1 ready for review. FACT/FIT/READ/PARSE all pass; one page confirmed.
