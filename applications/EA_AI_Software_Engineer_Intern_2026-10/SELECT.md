# SELECT — EA AI Software Engineer Intern

Status: rendered locally and validated as a one-page PDF; see `output/audit.md`. The EA-specific run is not yet included in the repository CI PDF-build job.

## Target lens

Primary: Software Quality / Test Automation  
Secondary: AI/ML Engineering and developer tooling  
Mode: `mnc` (conventional, ATS-friendly, evidence dense)  
Depth: D2 with selective D3 for testing and verification evidence.

The original EA Role ID 215929 is closed. This run is reusable for similar open quality engineering, test automation, or AI software engineering internships.

## Requirement-to-evidence map

| JD signal | Evidence source | Strength | Selection |
|---|---|---|---|
| Python / JavaScript / scripting | `data/facts.yaml`; MIA TypeScript/Bun and Python/FastAPI projects in `content/github/evidence.md` | DIRECT | FOREGROUND |
| Automated testing / regression tests | MIA automated tests and verification gates; Omi authored PRs #8919 and #8442 with targeted tests, both unmerged | DIRECT for authored test work; preserve PR status | FOREGROUND |
| Git/GitHub | Candidate repositories and PR history in `content/github/evidence.md` | DIRECT | FOREGROUND |
| Build pipelines / CI | MIA `.github/workflows/ci.yml` source and CI results; confirm contribution scope before saying owned/maintained | ADJACENT pending personal contribution attribution | SUPPORT or OMIT |
| AI/ML project experience | AICTE virtual internship and LLM-Council evidence | DIRECT | SUPPORT |
| AI output quality/correctness evaluation | LLM-Council Analyst/Skeptic/Synthesizer workflow compares and synthesizes multiple model outputs; not evidence of calibrated correctness scoring | ADJACENT | SUPPORT with narrow wording |
| API testing / mobile automation | Related APIs and Android projects exist, but explicit test automation coverage not established in evidence inventory | NONE until direct source proves it | OMIT |
| Game QA / telemetry / logs | No evidence currently documented | NONE | OMIT |
| SQL / relational DB / Linux | No confirmed depth in resume evidence | NONE | OMIT |
| OOP | Project code is object-oriented-capable TypeScript/Python/Kotlin, but specific demonstrated OOP claim should be tied to implementation | ADJACENT | Support only if source-backed |

## Safe bullet candidates

Use only after checking the referenced source and candidate authorship.

- Built a Bun/TypeScript CLI for AI-assisted engineering workflows with automated tests, type checking, linting, unused-code analysis, build verification, and a compiled-binary smoke test.
- Added regression tests around explicit workflow contracts, including invalid lifecycle transitions and architectural boundaries, where the relevant change is candidate-authored.
- Implemented offline speaker-clustering and validation logic with tests in an authored Omi pull request that remained unmerged; keep the unmerged status explicit if included.
- Built a multi-model LLM workflow using Analyst, Skeptic, and Synthesizer stages to compare and synthesize model responses; do not claim objective correctness improvement without measured evaluation evidence.
- Completed a 10-week virtual AI/ML internship through the AICTE/EduSkills ecosystem, working with TensorFlow, TensorFlow Lite, ML Kit, and mobile computer-vision workflows.

## Non-claims and boundaries

- Do not claim game testing, game-production QA, or test coverage improvements.
- Do not claim personal ownership of all MIA CI infrastructure solely because the repository contains it.
- Do not claim the Omi PRs were merged or that downstream implementations were authored by the candidate.
- Do not claim 52 passing tests as proof of a merged or shipped feature; the count is tied to a closed unmerged PR.
- Do not claim AI outputs were validated for correctness, consistency, or usefulness unless an actual criteria-based evaluation is directly evidenced.
- Do not invent coverage, time savings, defects caught, reliability gains, or performance metrics.

## Render decision

Do not modify a mode base. This is a per-application run, as the Resume Engine contract requires. Next execution step is to run SELECT/RENDER using this input, create the standard output set, validate the trace and PDF, inspect extracted text and visual layout, then update this draft with measured gate results. Any unknowns remain omitted.
