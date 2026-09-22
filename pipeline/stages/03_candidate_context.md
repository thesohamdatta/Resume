<!-- Stage 3: Candidate Context — Read by pipeline/run.md -->
# STAGE 03: CANDIDATE CONTEXT

Read:
- `data/facts.yaml`
- `content/github/evidence.md`
- `content/github/boundaries.md`

Only report supported candidate evidence.

## Track-specific notes

The only active tracks are:
- `local`
- `mnc`

For both tracks, identify evidence relevant to the required resume order:
Header → Summary → Experience → Projects → Education → Technical Skills → Certifications when verified.

Do not infer certifications, skills, metrics, ownership, or outcomes from names alone.

## Output

Append to `applications/{Company}_{YYYY-MM}/pipeline_state.md`:

```
## Stage 03 — Candidate Inventory

### Strongest evidence
| Project | Evidence | Type |
|---|---|---|

### Secondary evidence
| Project | Evidence | Type |
|---|---|---|

### Hard boundaries
- [from boundaries.md]

### Track-specific notes
- Track: local | mnc
- Structure: Header → Summary → Experience → Projects → Education → Technical Skills → Certifications when verified
```
