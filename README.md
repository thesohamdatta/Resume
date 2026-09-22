# Resume Workspace

Clean, organized structure for maintaining two active resume variants from one factual source.

> New here? Start at **`MAP.md`** for entry points, rules, stages, and outputs.

## Active tracks

1. **Local**: local Indian IT/product companies and smaller engineering teams → `versions/local/_base.md`
2. **MNC**: multinational and enterprise hiring → `versions/mnc/_base.md`

Legacy `startup` and `midlevel` folders are retained for recovery/history and are not active generation targets.

## Standard structure

Both active resumes use this order unless a specific application requires otherwise:

1. Header / Contact
2. Summary
3. Experience
4. Projects
5. Education
6. Technical Skills
7. Certifications, only when verified certification data exists

## Structure

```
data/
  facts.yaml                         # Single source of truth
content/github/
  evidence.md                        # Technical proof
  boundaries.md                      # Truth constraints
versions/
  local/_base.md                     # Local-company base
  mnc/_base.md                       # MNC base
  {local,mnc}/resume_{Company}.md   # Tailored outputs
applications/                         # Per-company runs
pipeline/                             # 10-stage JD-to-application workflow
research/                             # Company research
templates/                            # LaTeX export templates
archive/                              # Historical material only
```

## Evidence

`content/github/evidence.md` contains technical proof for Aura, Mia, Voice AI, LLM-Council, Omi contributions, and prior research work.

`content/github/boundaries.md` contains the binding constraints for claims, attribution, metrics, ownership, and wording.

## Source of truth

Facts live in `data/facts.yaml`. Technical detail comes from `content/github/evidence.md`. Constraints come from `content/github/boundaries.md`.

The pipeline may tailor bullet selection, order, wording, summary emphasis, skills emphasis, and project emphasis. It must never change the underlying facts.

## Output rule

New application runs MUST target exactly one of:

```
local
mnc
```

Do not create new `startup` or `midlevel` outputs.
