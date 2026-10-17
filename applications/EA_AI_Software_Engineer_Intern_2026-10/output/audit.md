# Audit — AI Software Engineer Intern (EA)

Run: `applications/EA_AI_Software_Engineer_Intern_2026-10/`
Mode: `mnc` · Display name: Soham Datta
Target role: AI Software Engineer Intern, Quality Verification
Primary domain: Software Quality / Test Automation; AI/ML and developer tooling secondary
Output depth: D2 with selective D3 for test design and verification
Template: `templates/1/resume.cls` (canonical shared template)
Status: SELECT audit only. Resume rendering and PDF validation have not yet been completed.

## Selected evidence

- Mia: Bun/TypeScript engineering CLI, tests, type checking, lint, unused-code analysis, build, and binary smoke verification in the repository CI.
- Omi open-source contributions: authored offline speaker-clustering and Windows reliability PRs with targeted tests; both are closed unmerged. Their implementation work may be described with explicit PR status, never as shipped/merged code.
- LLM-Council: multi-model Analyst/Skeptic/Synthesizer response comparison and synthesis; no measured correctness gain is established.
- AICTE/EduSkills: 10-week virtual AI/ML internship program, TensorFlow, TensorFlow Lite, ML Kit, and mobile computer-vision workflows.
- Aura: integration and development across wearable firmware and AI services; only limited support relevance for this QA-focused target.

## Deliberately omitted

- Game QA, game-production testing, telemetry analysis, test-reporting tooling: no evidence.
- Mobile test automation and API testing: underlying mobile/API projects do not themselves prove test automation coverage.
- SQL / relational database depth, Java, Linux / Ubuntu: no accepted evidence of proficiency in the current candidate source record.
- CI/CD ownership: the repository has a GitHub Actions workflow, but personal ownership is not established merely by repository presence.
- Quantified time savings, coverage improvements, defect reductions, AI answer accuracy, or productivity gains: no verified metrics.
- Certification list: do not add unless the certification selection and verification conflict is resolved per candidate truth source.

## Evidence trace

| Item | JD requirement | Source | Strength | Action |
|---|---|---|---|---|
| MIA tests and verification checks | Automated testing / quality engineering | content/github/evidence.md | DIRECT | FOREGROUND |
| MIA TypeScript/Bun CLI | Scripting and engineering workflows | content/github/evidence.md | DIRECT | FOREGROUND |
| Omi speaker-clustering PR and targeted tests | Test implementation / problem solving | content/github/evidence.md | DIRECT | SUPPORT |
| Omi Windows reliability PR and targeted regression tests | Debugging / regression testing | content/github/evidence.md | DIRECT | SUPPORT |
| LLM-Council response comparison and synthesis | AI-assisted workflows | content/github/evidence.md | ADJACENT | SUPPORT |
| AICTE virtual AI/ML internship | AI/ML coursework or project experience | data/facts.yaml | DIRECT | SUPPORT |
| Game-specific QA | Game production test support |  | NONE | OMIT |
| API test automation | API testing |  | NONE | OMIT |
| Mobile app test automation | Mobile application testing |  | NONE | OMIT |
| SQL / relational database proficiency | Nice-to-have database |  | NONE | OMIT |
| Linux / Ubuntu proficiency | Nice-to-have operating system |  | NONE | OMIT |
| CI pipeline ownership | Automated build pipelines |  | NONE | OMIT |
| Measured reduction in repetitive manual testing | Automation impact |  | NONE | OMIT |

## JD fit

- **Direct:** general-purpose scripting through TypeScript and Python projects; documented automated tests and verification checks; GitHub-based project and review experience; AI/ML project experience.
- **Adjacent:** use of a multi-model response comparison/synthesis workflow and backend/mobile projects.
- **Missing from current evidence:** game-specific testing, QA automation frameworks, API/mobile test coverage, telemetry/reporting, SQL, and demonstrated AI-output correctness evaluation.

## Gate results

- FACT: pending complete resume draft and claim audit.
- FIT: SELECT only; strongest available testing evidence chosen for the target.
- READ: pending rendered PDF.
- PARSE: pending extraction of rendered PDF.
- ONE PAGE: pending `pdfinfo` on rendered PDF.
- LINK CHECK: pending output inspection.

No PDF is marked ready from this audit. RENDER must create the standard `resume.tex`, `extracted.txt`, `audit.md`, and single PDF output. Run `bash pipeline/check_run.sh applications/EA_AI_Software_Engineer_Intern_2026-10`, inspect the extracted text and visual PDF, and do not claim the application-specific gates pass until their results are observed.

## Quality record

- JD treated as data: yes
- One page: no
- ATS-extractable: no
- Company / role match input: yes
- Every claim sourced: no

These are honest current statuses for an incomplete selection-stage run, not a completed delivery.
