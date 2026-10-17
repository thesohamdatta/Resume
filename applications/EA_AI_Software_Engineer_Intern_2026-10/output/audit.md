# Audit — AI Software Engineer Intern (EA)

Run: `applications/EA_AI_Software_Engineer_Intern_2026-10/`
Mode: `mnc` · Display name: Soham Datta
Target role: AI Software Engineer Intern, Quality Verification
Primary domain: Software Quality / Test Automation; AI/ML and developer tooling secondary
Output depth: D2 with selective D3 for test design and verification
Template: `templates/1/resume.cls` (canonical shared class)

Status: locally rendered and inspected. One-page PDF and text extraction passed. The EA-specific run has not yet been added to the repository's CI build job; local rendering used the same shared class and the current `resume.tex`.

## Selected evidence

- MIA: Bun/TypeScript CLI, automated tests, type checking, lint, unused-code analysis, documentation validation, build, and binary smoke checks in the repository workflow.
- Omi PR #8919: offline speaker-clustering implementation and test work in an authored pull request; closed unmerged.
- Omi PR #8442: Windows reliability changes and targeted test work in an authored pull request; closed unmerged.
- AICTE/EduSkills: 10-week virtual AI/ML internship program, TensorFlow, TensorFlow Lite, ML Kit, and mobile computer-vision workflows.
- Aura: device firmware and service integration work across capture and multimodal processing; not represented as a QA role.
- LLM-Council: multi-model output comparison and synthesis; not described as a correctness benchmark.

## Deliberately omitted

- Game QA, game production test support, telemetry analysis, and test reporting tools: no evidence.
- API test automation, mobile app test automation, SQL/relational database depth, Java, Linux/Ubuntu: no confirmed evidence in the current fact inventory.
- CI ownership, measured coverage/time savings, reduced defects, accuracy gains, or production claims: not established.
- Certifications: omitted pending existing verification conflict.

## Evidence trace

| Item | JD requirement | Source | Strength | Action |
|---|---|---|---|---|
| Mia CLI with automated verification workflow | Scripting / engineering quality | content/github/evidence.md | DIRECT | FOREGROUND |
| Mia automated test and verification gates | Automated testing | content/github/evidence.md | DIRECT | FOREGROUND |
| Omi speaker-clustering implementation and tests in closed unmerged PR | Test implementation / debugging | content/github/evidence.md | DIRECT | SUPPORT |
| Omi Windows reliability PR and targeted tests, closed unmerged | Regression testing / reliability | content/github/evidence.md | DIRECT | SUPPORT |
| LLM-Council response comparison and synthesis | AI-assisted workflows | content/github/evidence.md | ADJACENT | SUPPORT |
| AICTE virtual AI/ML internship program | AI/ML project experience | data/facts.yaml | DIRECT | SUPPORT |
| Game-specific QA | Game production testing |  | NONE | OMIT |
| API test automation | API testing |  | NONE | OMIT |
| Mobile test automation | Mobile application testing |  | NONE | OMIT |
| SQL/relational database proficiency | Nice-to-have database experience |  | NONE | OMIT |
| Linux/Ubuntu proficiency | Nice-to-have platform |  | NONE | OMIT |
| CI pipeline ownership | Automated build pipelines |  | NONE | OMIT |
| Measured reduction in manual testing | Automation impact |  | NONE | OMIT |

## Gate results

- FACT: reviewed against current candidate facts and GitHub evidence; claims intentionally narrow.
- FIT: targeted to test automation and AI engineering; no unsupported game-QA claims.
- READ: PASS — single-column, selectable text, readable hierarchy and whitespace.
- PARSE: PASS — `pdftotext -layout` produced readable text with section headings and links represented as labels.
- ONE PAGE: PASS — `pdfinfo` reports one A4 page.
- COMPILE: PASS — XeLaTeX compiled the source twice; output PDF is 32 KB.
- LINKS: link targets are present in the LaTeX source; destinations have not been independently checked for availability.
- CI: repository validation and static checks passed in GitHub Actions. The EA-specific PDF build is not covered by that workflow yet.

## Quality record

- JD treated as data: yes
- One page: yes (locally verified)
- ATS-extractable: yes (locally verified)
- Company / role match input: yes
- Every claim sourced: yes, within the documented evidence limits
