<!-- Stage 2: JD Analyzer — Read by pipeline/run.md -->
# STAGE 02: JD ANALYZER

**Your Role:** Parse the provided Job Description (JD) and extract signals.

## Inputs to Read:
- `applications/{Company}_{YYYY-MM}/input.md` (Read ONLY the `jd:` section)

## Execution Rules:
1. Use verbatim keyword extraction only. DO NOT paraphrase JD requirements.
2. Mark a gap ONLY when the requirement clearly has no match in the typical candidate profile.
3. Keep the entire output under 200 words.

## Output Target:
Append to `applications/{Company}_{YYYY-MM}/pipeline_state.md` under a new section `## Stage 02 — JD Signals`

## Output Format (Exact Schema):
```
## Stage 02 — JD Signals

### Required (explicit in JD — must have match)
- item

### Preferred (nice-to-have — include if honest match)
- item

### Role archetype
[e.g. "AI-first generalist", "mobile + AI", "hardware-adjacent software"]

### ATS keywords (verbatim from JD)
- keyword

### Deprioritize (in JD but low-signal for this candidate)
- item

### Gaps flagged
| JD Requirement | Gap | How to handle |
|---|---|---|
```
