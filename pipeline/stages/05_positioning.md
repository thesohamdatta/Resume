# STAGE 05: POSITIONING

Define the framing for this application without changing factual history.

## Inputs
- `applications/{Company}_{YYYY-MM}/pipeline_state.md` Stage 04
- `research/companies/{Company}.md`
- `applications/{Company}_{YYYY-MM}/input.md` notes
- `CONTEXT.md`

## Decision sequence

1. Identify the strongest JD signals.
2. Select exactly one **Primary Technical Domain** from the controlled vocabulary in `CONTEXT.md`.
3. Select **Output Depth**:
   - D1 Executive/scan
   - D2 Engineering
   - D3 Technical-proof
4. Build an **Evidence Mix** across Implementation, Design, Problem-solving, Research, and Product.
5. Decide:
   - **Foreground** = directly relevant, strongest proof
   - **Compress** = useful but secondary
   - **Omit** = distracting or too weak for this application
6. Check whether any missing fact materially affects the decisions above.
7. Ask at most 3 questions only when the answer would change the domain, depth, attribution, scope, dates, certification status, or another correctness-critical point.

## Track guidance

### Local
Default D2. D3 is appropriate for a clearly technical role or when the primary domain is implementation-heavy.

### MNC
Default D1–D2. Use D3 only when the JD explicitly rewards implementation, systems, research, debugging, architecture, or similar depth.

The MNC rule is **not** "remove technical truth." It is "show only the technical detail that earns relevance."

## Output schema

```
## Stage 05 — Positioning Strategy

### Primary Technical Domain
[one controlled-domain value]

### Output Depth
[D1 | D2 | D3]

### Primary hook
[Specific overlap]

### Evidence mix
- Implementation: [foreground/compress/omit]
- Design: [foreground/compress/omit]
- Problem-solving: [foreground/compress/omit]
- Research: [foreground/compress/omit]
- Product: [foreground/compress/omit]

### Foreground
- [specific evidence]

### Compress
- [specific evidence]

### Omit
- [specific evidence]

### Track confirmed
[local | mnc]

### Headline for this role
[role-specific headline]

### Material questions
- [question or "none"]

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
3. Relevant engineering breadth
4. Close
```

## Stop condition

If a material question is unresolved, stop before Stage 06 and collect the answer. Do not guess.
