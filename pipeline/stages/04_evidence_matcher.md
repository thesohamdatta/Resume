<!-- Stage 4: Evidence Matcher — Read by pipeline/run.md -->
# STAGE 04: EVIDENCE MATCHER

**Your Role:** Match JD requirements to candidate evidence.

## Inputs to Read:
- `applications/{Company}_{YYYY-MM}/pipeline_state.md` (Read `## Stage 02 — JD Signals` AND `## Stage 03 — Candidate Inventory`)
- `research/companies/{Company}.md`

## Execution Rules:
1. Strength definitions:
   - STRONG: GitHub repo + specific file/PR/algorithm + directly maps to JD requirement
   - MODERATE: GitHub repo exists, maps to JD but less direct
   - WEAK: Tool name in skills only — do not use as evidence
2. A WEAK match must NOT be listed as High-signal. List it only under Moderate or suppress it.

## Output Target:
Append to `applications/{Company}_{YYYY-MM}/pipeline_state.md` under a new section `## Stage 04 — Evidence Match`

## Output Format (Exact Schema):
```
## Stage 04 — Evidence Match

### High-signal matches (JD requirement ↔ verifiable evidence)
| JD Requirement | Evidence item | Strength | Evidence type |
|---|---|---|---|

### Moderate matches (real but less specific to JD phrasing)
| JD Requirement | Evidence item | Strength |
|---|---|---|

### Confirmed gaps
| JD Requirement | Gap status | Interview framing |
|---|---|---|

### Evidence to suppress (real but low-relevance to this role)
- item
```
