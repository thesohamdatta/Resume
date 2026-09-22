# MAP.md — Repository Index

One page that answers "where does X live?"

## Agent entry

For a fresh agent with no conversation history:

1. `MAP.md`
2. `AGENTS.md`
3. `CONTEXT.md`
4. `data/facts.yaml`
5. `content/github/evidence.md`
6. `content/github/boundaries.md`

## Active tracks

| Track | Use for | Base |
|---|---|---|
| `local` | Local Indian IT/product companies | `versions/local/_base.md` |
| `mnc` | MNC / enterprise hiring | `versions/mnc/_base.md` |

Legacy `startup` and `midlevel` folders are retained for recovery/history only.

## Application control

Every application has two separate decisions:

1. **Track** = presentation environment (`local` or `mnc`)
2. **Primary Technical Domain** = technical emphasis for this specific job

Optional third decision:
3. **Output Depth** = D1, D2, or D3

The domain is not a third resume track.

## Standard resume section order

```
Header / Contact
Summary
Experience
Projects
Education
Technical Skills
Certifications (only when verified)
```

## Evidence model

`content/github/evidence.md` is the deep proof layer. It may contain D3 implementation detail even when the final resume is D1/D2.

Evidence types:
- Implementation
- Design
- Problem-solving
- Research
- Product

## Run something

| I want to… | Open this |
|---|---|
| Apply for a job | `pipeline/APPLY.md` |
| Understand the 10 stages | `pipeline/run.md` |
| Deep-research a company | `research/SWARM_RESEARCH.md` |
| Re-run one stage | `pipeline/run.md` → Shortcuts |

## Pipeline

01 company research → 02 JD analysis → 03 candidate context → 04 evidence match →
05 positioning/domain-depth gate → 06 resume writer → 07 factuality gate →
08 ATS review → 09 final editor → 10 slop polish

## Outputs

- Tailored resumes: `versions/{local,mnc}/resume_{Company}.md`
- Per-run state: `applications/{Company}_{YYYY-MM}/`
- Company dossiers: `research/companies/{Company}.md`
- Durable lessons: `memory/lessons.md`

## Templates

- `templates/v2-comma-titles/`
- `templates/v3/`
- Retired templates remain under `archive/`

## Do not auto-load

Other runs' `pipeline_state.md`, `archive/`, PDFs, and old research unless specifically required.
