# Resume Engine

A small, evidence-first engine that turns a job description into one truthful, one-page,
mode-specific resume.

```
run(jd, mode) -> resume.pdf        # exactly one page, ATS-readable, truth-traceable
```

## One pipeline, three modes

Modes: `startup`, `mnc`, `referral`. A mode changes emphasis and selection; it never changes
facts and never forks the pipeline. Settings and display names live in `modes/{mode}.yaml`.

## Quick start

1. Create `applications/{Name}_{YYYY-MM}/input.md` with company, role, mode, and the full JD
   (schema: `applications/_template/input.md`).
2. Follow `pipeline/README.md`: SELECT (build a traceable evidence plan), then RENDER
   (one-page PDF). Rules are in `RESUME_RULES.md`; the contract is `AGENTS.md`.
3. Write outputs to `applications/{Name}_{YYYY-MM}/output/`:
   `resume.tex`, `extracted.txt`, `audit.md`, and exactly one PDF named `Soham Datta.pdf`.

## Architecture

| File | Owns |
|---|---|
| `AGENTS.md` | the agent contract, read order, precedence, hard constraints |
| `SPEC.md` | the system definition, requirements, invariants, and architecture decisions |
| `RESUME_RULES.md` | evidence, modes, voice, ATS, gates, never-invent |
| `pipeline/README.md` | the workflow: two phases, two invariants |
| `modes/{mode}.yaml` | per-mode settings (name key, emphasis, depth) |
| `data/facts.yaml` | candidate facts (single source of truth) |
| `content/github/evidence.md` | technical proof |
| `content/github/boundaries.md` | claim / ownership / status limits |
| `docs/voice.md` | language and tone |
| `DONT.MD` | hard-fail checks |
| `templates/v3/` | the only visual template |
| `versions/{mode}/` | per-mode base content |
| `applications/` | per-application inputs, state, and outputs |
| `research/` | external research (never candidate facts) |
| `memory/lessons.md` | durable lessons |
| `archive/` | history only |

## Validation

```
bash pipeline/validate_resume_repo.sh   # repo contract
bash pipeline/build_base_resumes.sh     # compile the three base resumes, one page each
```

## Design principles

- Evidence is the source. The JD decides relevance. The template decides presentation.
- One owner per rule. Duplicate a rule and one copy is deleted.
- Truth outranks persuasion. Never invent metrics, ownership, dates, or production status.
- One page by default; remove weak content before shrinking type.
- Keep the active system small. Add a rule only when it solves a demonstrated failure.
