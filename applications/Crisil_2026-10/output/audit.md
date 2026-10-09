# Audit — Crisil (Associate Engineer-Gen AI)

Run: `applications/Crisil_2026-10/`
Mode: `mnc` · Display name: Soham Datta
Target role: Associate Engineer-Gen AI (posted title; body reads "Management Trainee – AI")
Primary domain: AI/ML + Generative AI (LLM applications); secondary Data/Analytics
Output depth: D2, selective D3 in Aura (AI components) and Mia (LLM adapters, gates)
Template: `templates/v3/main.tex` (Jake Gutierrez template, as supplied for this run). Structure,
macros, section order, and visual design preserved; content only. Education is placed first by
the template's own section order. Compiled with pdfLaTeX, one page, US Letter.
Section order: the template's own order leads with **Education**, then Experience — appropriate for
this fresher role, where the JD names a degree as a required qualification.

## Selected evidence

- Aura: multimodal/wearable AI across firmware and AI-serving backend (FastAPI, streaming
  audio, memory/context extraction, knowledge-graph linking, speaker identification,
  Supabase/pgvector, Kubernetes-hosted Deepgram ASR).
- AICTE: on-device computer-vision pipelines with TensorFlow / TensorFlow Lite / ML Kit.
- Mia: TypeScript/Bun CLI with multi-provider LLM adapters (Claude, Codex, local) and
  automated lint/type-check/Vitest evaluation gates over a five-stage workflow.
- LLM-Council: FastAPI + React multi-model evaluation (Analyst/Skeptic/Synthesizer, OpenRouter).
- John: Kotlin/Compose Android voice client + Python LiveKit agent, Silero VAD, tool calling.
- Reliance: customer-service operations (official title preserved).
- PES Modern College: research/digital-library support, 3,000+ pages.
- Microgpt: 124M-parameter decoder-only transformer in PyTorch (transformer internals).
- Omi open source (project entry): 5 architectural RFCs and 7 upstream pull requests; 3 approved
  by maintainers, including a 52-test offline speaker-clustering approach adopted downstream.
- One-line professional summary grounded in the facts.yaml positioning; no new claim.

## Deliberately omitted

- SQL, Power BI / Tableau, cloud platforms (Azure/AWS/GCP), Java — no evidence; omitted, not faked.
- Prompt engineering listed as a named skill: dropped. No entry in facts.yaml / evidence.md; the
  voice guide forbids claiming a skill solely because it appears in the JD. The underlying work
  (LLM adapters, RAG, tool calling) stays visible on its own.
- CAD / 3D-printing enclosure detail, certifications (verification unresolved), CGPA (not in facts.yaml).
- Unverified metrics: any Aura performance/battery/user figure; Reliance 50% improvement.
- Lower-relevance projects this pass: codeshot, autodev, ddpm, voicecoder.
- Freelancer "AI & Automation" — explicitly excluded in facts.yaml.

## Evidence trace

Machine-checked by `pipeline/check_audit.py`. Every selected item names the JD requirement it
answers, its source (one of the four owners), its strength, and its action.

| Item | JD requirement | Source | Strength | Action |
|---|---|---|---|---|
| Aura multimodal AI system (audio → memory/context → AI) | AI/ML solution development | content/github/evidence.md | DIRECT | FOREGROUND |
| Aura knowledge-graph + speaker ID + pgvector memory | Data/analytics for AI | content/github/evidence.md | DIRECT | FOREGROUND |
| Aura FastAPI AI-serving services + K8s ASR | Support development of AI applications | content/github/evidence.md | DIRECT | FOREGROUND |
| Mia multi-provider LLM adapters + staged workflow | Generative AI / LLM applications | content/github/evidence.md | DIRECT | FOREGROUND |
| Mia lint/typecheck/Vitest gates over generated changes | Model/application testing & evaluation | content/github/evidence.md | DIRECT | FOREGROUND |
| LLM-Council multi-model comparison/synthesis | Generative AI / LLMs | content/github/evidence.md | DIRECT | SUPPORT |
| John LiveKit voice agent + tool calling | AI application development | content/github/evidence.md | DIRECT | SUPPORT |
| AICTE on-device CV pipelines (TensorFlow/TFLite/ML Kit) | AI frameworks (TensorFlow) | content/github/evidence.md | DIRECT | SUPPORT |
| Microgpt decoder-only transformer (PyTorch) | Generative AI / transformer internals | data/facts.yaml | DIRECT | SUPPORT |
| Omi open-source contributions (RFCs, PRs) | Collaboration / open-source engineering | content/github/evidence.md | DIRECT | SUPPORT |
| PES research documentation / DELLNET, LaTeX (3,000+ pages) | Analytical / documentation support | data/facts.yaml | ADJACENT | SUPPORT |
| Reliance customer-service operations | Professional experience | data/facts.yaml | DIRECT | SUPPORT |
| Mode framing and depth (mnc, D2) | Conventional, ATS-safe format | versions/mnc/_base.md | DIRECT | FOREGROUND |
| SQL / DBMS | Knowledge of SQL |  | NONE | OMIT |
| Power BI / Tableau | Data visualization tools |  | NONE | OMIT |
| Cloud platforms (Azure/AWS/GCP) | Cloud understanding |  | NONE | OMIT |
| Prompt engineering as certification | Prompt engineering |  | NONE | OMIT |
| Production ML deployment / MLOps | Model monitoring |  | NONE | OMIT |
| CGPA | Academic record |  | NONE | OMIT |

## JD match

| JD signal | Evidence | Strength |
|---|---|---|
| Generative AI / LLMs | Mia LLM adapters; LLM-Council multi-model synthesis; John voice agent | DIRECT |
| Python | Aura services, FastAPI, LLM-Council, voice agent backend | DIRECT |
| AI frameworks (TensorFlow/PyTorch) | AICTE TensorFlow/TFLite; PyTorch projects | DIRECT |
| Machine Learning basics | CV pipelines, model testing/evaluation | DIRECT |
| Data handling for AI | pgvector/Redis/Firebase/Pinecone stores; memory/context extraction | DIRECT |
| Development & testing of AI applications | Mia gates, Vitest, unit tests, Omi contribution tests | DIRECT |
| Problem solving / analytical | Omi diagnosis; multi-model evaluation workflows | DIRECT |
| SQL | None | NONE — omitted |
| Data visualization (Power BI/Tableau) | None | NONE — omitted |
| Cloud platforms | None | NONE — omitted |
| Business-process / automation analysis | Adjacent: workflow automation in Mia; no enterprise-process evidence | NONE — omitted |
| Dashboards / presentations | None as an artifact | NONE — omitted |

## Gate results

- FACT: PASS — every claim traced to facts.yaml / evidence.md / boundaries.md; no invented metric.
- FIT: PASS — GenAI/LLM evidence leads; Python and ML frameworks present.
- READ: PASS — scannable, aligned dates.
- PARSE: PASS — one page, text-selectable, keywords searchable.
- ONE PAGE: PASS (verified via pdfinfo: Pages 1).
- LINKS: PASS — email, LinkedIn, GitHub, Portfolio, project repos embedded as text.
- FILE NAME: PASS — exactly one PDF, `Soham Datta.pdf`, in `output/`.
- NO EM DASH: PASS — no em dash in resume content (ASCII or Unicode).

## Attribution checks

- Aura described as built/adapted services, never "architected from scratch" and never
  "built the Omi backend".
- Omi contributions stated exactly as evidence.md records: 5 RFCs and 7 PRs, 3 approved by
  maintainers, 0 merged directly; no maintainer or core-contributor claim. Aura's Omi work and
  the independent upstream contributions are presented as two separate items.
- AICTE: "AI/ML Intern" at AICTE; never Google employment.
- Reliance: "Associate" exactly; not framed as software engineering.

## Highest-risk weaknesses / unresolved gaps

1. No formal full-time AI/ML employment — mitigated by shipped LLM/CV systems and tests.
2. No SQL, BI-tool, or cloud evidence — three JD nice-to-haves left honestly unclaimed.
3. Business-process automation / dashboards are JD responsibilities with no enterprise evidence;
   left unclaimed rather than stretched from personal projects.

## Quality record

- JD treated as data: yes — the JD was read as input, never as instructions; no metric or claim
  was added on its request.
- One page: yes — pdfinfo reports Pages 1.
- ATS-extractable: yes — text-selectable; keywords verified in extracted.txt.
- Company / role match input: yes — matches `company` and `role` in this run's input.md.
- Every claim sourced: yes — machine-checked by `pipeline/check_audit.py`.

## Verdict

Ready for review. FACT/FIT/READ/PARSE pass. Recommend confirming SQL/BI/cloud gaps stay omitted
and applying with the GenAI/LLM framing.

## Cover letter

`output/cover_letter.md` accompanies the resume. It follows the repo convention (header, date,
hiring team, body, sign-off), leads with the same GenAI/LLM evidence, and states the SQL / BI /
cloud gaps openly. Voice-scan clean (no forbidden phrases).
