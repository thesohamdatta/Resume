# MAP.md — Repository Index

One page that answers "where does X live?" Read this before exploring.

## Agent entry

For a fresh agent with no conversation history, use this order:

1. `MAP.md`
2. `AGENTS.md`
3. `CONTEXT.md`
4. `data/facts.yaml`
5. `content/github/evidence.md`
6. `content/github/boundaries.md`

Detailed role evidence lives under `content/github/`; it supports the evidence layer but does not override `data/facts.yaml`.

## Run something
| I want to… | Open this |
|---|---|
| Apply for a job (full workflow) | `pipeline/APPLY.md` |
| Understand the 10 stages | `pipeline/run.md` |
| Deep-research a new/stale company first | `research/SWARM_RESEARCH.md` |
| Re-run one stage / polish only | `pipeline/run.md` → Shortcuts |

## Know the rules
| Question | Answer lives in |
|---|---|
| How do agents behave here? | `AGENTS.md` (canonical) |
| What is this project / domain terms? | `CONTEXT.md` |
| Resume rules, what never to do? | `DONT.MD` (canonical, do not restate elsewhere) |
| What is true about the candidate? | `data/facts.yaml` |
| What is proven (repos/PRs/files)? | `content/github/evidence.md` |
| What must never be claimed? | `content/github/boundaries.md` |
| Detailed PES research-role evidence? | `content/github/experience_ps_modern_institute.md` |

## Pipeline stages (in order)
01 company research → 02 JD analysis → 03 candidate context → 04 evidence match →
05 positioning (human checkpoint) → 06 resume writer → 07 factuality gate →
08 ATS review → 09 final editor → 10 slop polish (terminal)

## Where outputs go
- Tailored resumes: `versions/{startup,mnc,midlevel}/resume_{Company}.md` (+ `_base.md` per track)
- Per-run state: `applications/{Company}_{YYYY-MM}/` (`input.md`, `pipeline_state.md`, `cover_letter.md`, `interview_prep.md`)
- Company dossiers: `research/companies/{Company}.md` (schema: `research/companies/_template.md`)
- Durable lessons: `memory/lessons.md` (evidence-backed only)

## Templates (LaTeX)
- `templates/v2-comma-titles/` — TLCresume, pdflatex
- `templates/v3/` — openfont (Lato/Raleway), xelatex only; `v3/fonts/` is the shared copy — never re-copy per run
- Retired: `archive/templates-v1-dash-titles-20260915/` (recoverable, never referenced)
- Never commit `.aux`/`.log`/`.out`

## Do not auto-load
Other runs' `pipeline_state.md`, `archive/`, PDFs, `research/resume_best_practices.md` (distilled into `DONT.MD` already).
