# Resume Engine

A small, evidence-first engine that turns a job description into one truthful, one-page, mode-specific resume.

```
run(jd, mode) -> resume.pdf  # exactly one page, ATS-readable, truth-traceable
```

## One pipeline, three modes

Modes: `startup`, `mnc`, `referral`. A mode changes emphasis and selection; it never changes facts and never forks the pipeline. Settings live in `modes/{mode}.yaml`.

## Quick start

1. Create `applications/{Name}_{YYYY-MM}/input.md` with company, role, mode, and the full JD. Use `applications/_template/input.md` as the schema.
2. Follow `pipeline/README.md`: SELECT builds a traceable evidence plan, then RENDER creates the one-page PDF. Rules live in `RESUME_RULES.md`; `AGENTS.md` is the agent entry point.
3. Write outputs to `applications/{Name}_{YYYY-MM}/output/`: `resume.tex`, `extracted.txt`, `audit.md`, and exactly one PDF named `Soham Datta.pdf`.

## Source of truth

| Responsibility | Owner |
|---|---|
| Agent contract and read order | `AGENTS.md` |
| Requirements and architectural decisions | `SPEC.md` |
| Resume rules, evidence gates, ATS and truth constraints | `RESUME_RULES.md` |
| Execution workflow | `pipeline/README.md` |
| Candidate facts | `data/facts.yaml` |
| Technical proof | `content/github/evidence.md` |
| Claim and ownership limits | `content/github/boundaries.md` |
| Voice and language | `docs/voice.md` |
| Hard resume constraints | `DONT.MD` |
| Mode settings and base content | `modes/{mode}.yaml`, `versions/{mode}/_base.md` |
| Canonical visual template | `templates/v3/` |
| Application input and output | `applications/{Name}_{YYYY-MM}/` |
| External research, not candidate facts | `research/` |
| Durable lessons | `memory/lessons.md` |
| Historical material | `archive/` |

Each rule and each candidate fact should have one authoritative owner. Link to that owner rather than copying content into another file.

## Validation

```bash
bash pipeline/validate_resume_repo.sh   # repository structure and invariants
bash pipeline/test_validate_contract.sh # validator regression tests
bash pipeline/build_base_resumes.sh     # compile all mode bases and check page count
bash pipeline/check_run.sh applications/{Name}_{YYYY-MM}
```

Before delivery, also inspect the rendered PDF and extracted text. A successful LaTeX compile alone does not prove that the resume is one page, visually clean, or readable by parsers.

## Design principles

- Evidence is the source. The JD determines relevance. The approved template determines presentation.
- Truth outranks persuasion. Never invent metrics, ownership, dates, skills, or production status.
- Tailor what is selected and emphasized, not the candidate's history.
- Keep the resume to one page by default. Remove weak content before reducing type size.
- Keep active instructions short and load detailed sources only when needed.
- Do not create folders, skills, templates, or abstraction layers without a distinct responsibility.
