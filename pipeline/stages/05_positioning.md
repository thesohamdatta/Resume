<!-- Stage 5: Positioning — Read by pipeline/run.md -->
# STAGE 05: POSITIONING

Define the framing for this application without changing factual history.

## Inputs
- `applications/{Company}_{YYYY-MM}/pipeline_state.md` Stage 04
- `research/companies/{Company}.md`
- `applications/{Company}_{YYYY-MM}/input.md` notes

## Execution rules

1. Primary hook must identify a specific overlap between the candidate's evidence and the company/role.
2. Confirm track as exactly `local` or `mnc`.
3. Section order is fixed for both tracks.
4. Choose which truthful evidence to foreground. Do not invent new evidence.

## Output schema

```
## Stage 05 — Positioning Strategy

### Primary hook
[Specific overlap]

### Secondary angles
- [angle]

### Track confirmed
[local | mnc] — reason if overriding input.md

### Headline for this role
[role-specific headline]

### Resume structure
1. Header / Contact
2. Summary
3. Experience
4. Projects
5. Education
6. Technical Skills
7. Certifications, only when verified

### Cover letter structure
1. Opening
2. Strongest evidence
3. Engineering/project breadth
4. Close

### What to cut from base
- [section/bullet]

### What to foreground
- [specific evidence]
```
