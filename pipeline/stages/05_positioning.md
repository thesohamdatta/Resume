<!-- Stage 5: Positioning — Read by pipeline/run.md -->
# STAGE 05: POSITIONING

**Your Role:** Define the strategic framing for this specific application.

## Inputs to Read:
- `applications/{Company}_{YYYY-MM}/pipeline_state.md` (Read `## Stage 04 — Evidence Match`)
- `research/companies/{Company}.md`
- `applications/{Company}_{YYYY-MM}/input.md` (Read ONLY the `notes:` section)

## Execution Rules:
1. CRITICAL: The primary hook MUST name a specific overlap between the candidate's work and the company's product. Generic hooks like "I am passionate about AI" are invalid — reject and rewrite.

## Output Target:
Append to `applications/{Company}_{YYYY-MM}/pipeline_state.md` under a new section `## Stage 05 — Positioning Strategy`

## Output Format (Exact Schema):
```
## Stage 05 — Positioning Strategy

### Primary hook
[One sentence. Most specific, strongest match between candidate and this company. No buzzwords.]

### Secondary angles (2–3 max)
- angle

### Track confirmed
[startup | mnc | midlevel] — state if overriding input.md track and why

### Headline for this role
[e.g. "AI Engineer · Wearable Systems · Full-Stack"]

### Cover letter structure
1. Opening: [hook — specific to company, ≤2 sentences]
2. Body 1: [strongest project evidence]
3. Body 2: [software/engineering breadth]
4. Close: [direct ask, ≤1 sentence]

### What to cut from base resume
- [section or bullet] — reason

### What to foreground (from evidence — not currently in base resume)
- [specific technical detail from evidence.md that should appear]
```
