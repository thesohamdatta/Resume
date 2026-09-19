# Resume Workspace

Clean, organized structure for maintaining three resume variants from one factual source.

> New here? Start at **`MAP.md`** — one-page index of entry points, rules, stages, and outputs.

## Structure

```
D:\download\resume\
├── data/
│   └── facts.yaml              # Single source of truth for all biographical data
├── content/
│   ├── github/
│   │   ├── evidence.md         # Technical proof — what you built
│   │   └── boundaries.md       # Truth constraints — what NOT to claim
│   └── handoffs/
│       ├── resume_iteration_2026-09-14.md  # Current decisions and approach
│       ├── resume_handoff.md   # Earlier decisions (grilling phase, superseded)
│       └── refactor_2026-09-14.md  # Structural cleanup log (what moved where)
├── versions/
│   ├── startup/_base.md        # Startup track base (founder-readable, one page)
│   ├── mnc/_base.md            # MNC track base (ATS-first, ASCII only)
│   ├── midlevel/_base.md       # Mid-level track base (balanced, modern)
│   └── {track}/resume_{Company}.md  # Tailored outputs, e.g. startup/resume_Noise_PM.md
├── applications/               # Per-company runs: input.md, pipeline_state.md, cover_letter.md
├── pipeline/                   # JD-to-application runs (fill INPUT in pipeline/APPLY.md) + 10 stages (see pipeline/run.md)
├── research/companies/         # Per-company context (Noise.md) + _template.md
├── templates/                  # LaTeX: v2-comma-titles (pdflatex) + v3 openfont (xelatex) + README (which is which); v1 retired to archive/
├── assets/                     # Source PDFs (user artifacts, keep)
├── .agents/skills/             # Tool skills (stop-slop, pdf — loaded only when needed)
├── archive/                    # Stale/superseded files (never referenced by pipeline)
└── CONTEXT.md                  # Workspace overview
```

## Single Source of Truth

**`data/facts.yaml`** contains:
- Personal info (name, location, links)
- Education (dates, degree, institution)
- Experience (4 active roles)
- Projects (3 systems with repos, technical tags, bullets per track)
- Skills (categorized by domain)
- Truth boundaries (what NOT to claim)

All other files reference this. Changing a date or title requires editing one file only.

## Evidence Files

**`content/github/evidence.md`** — positive technical proof:
- Aura: hardware, firmware, backend, infrastructure details
- Mia: CLI harness, multi-host adapters, state engine
- Voice AI: LiveKit agents, Android app, VS Code extension
- Omi: 21 issues, 7 PRs, 120+ tests, downstream adoption

**`content/github/boundaries.md`** — validation constraints:
- What you can vs cannot claim per project
- Forbidden buzzwords and patterns
- Attribution clarity rules
- Resume audit checklist with regex patterns for automated validation

## Three Tracks

1. **MNC resume**: ATS-first, keywords, conventional — `versions/mnc/_base.md`
2. **Startup resume**: Founder-readable, proof-first — `versions/startup/_base.md`
3. **Mid-level resume**: Balanced, modern — `versions/midlevel/_base.md`

Each track has exactly one canonical base (`_base.md`, the pipeline Stage 06 input).
Tailored per-company outputs sit beside it as `resume_{Company}.md`.
All three pull bullets from `data/facts.yaml` per-track keys (`startup` | `mnc` | `midlevel`).

## Archive

`archive/` holds files the pipeline never reads — kept for recovery, not for use:
- Superseded snapshots (`resume_mnc.md`, `resume_midlevel.md`, `noise_role_research.md`, `noise_cover_letter.md` — suffixed with reason + date)
- Unreferenced duplicates (`boundaries.yaml` — nothing reads it; Stage 07 reads `content/github/boundaries.md`)
- Conversation transcripts, old research, cache files, `pipeline_old/` specs

## Next Steps

1. ~~Create templates for MNC and mid-level tracks~~ — done (`versions/{mnc,midlevel}/_base.md`)
2. Build generation script (`build.js` or `build.py`) to render all three tracks from `facts.yaml`
3. Create validation script (`validate.py`) to check final outputs against `boundaries.md` patterns

## Maintenance

Workflows (update a fact, add evidence, add a constraint, tailor a track) live in **`AGENTS.md` → Maintenance workflows** — single owner, read there.
