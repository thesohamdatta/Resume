# Resume Pipeline

Given an application input, generate the correct resume from the canonical evidence system.

## Required sequence

1. Read application input
2. Load candidate facts
3. Load technical evidence
4. Load ownership/status boundaries
5. Analyze company and JD
6. Select track: `referral`, `startup`, or `mnc`
7. Select Primary Technical Domain
8. Select Output Depth: D1/D2/D3
9. Build JD → Evidence map
10. Select foreground / compress / omit content
11. Draft resume content
12. Run factuality gate
13. Populate canonical LaTeX template
14. Compile to PDF
15. Run visual QA
16. Run ATS/text QA
17. Run cross-version consistency QA
18. Run final hard-fail gate

## Track rules

### referral
Broad, clear, practical, easy to forward. Display name: **Soham Karande**.

### startup
Strongest ownership and builder signal. Distinctive through evidence, not gimmicks. Display name: **Soham Datta**.

### mnc
Conventional, ATS-safe, technically precise, evidence-dense. Display name: **Soham Datta**.

## Domain

Choose one:

- AI/ML
- LLM/Agent Systems
- Voice/Realtime AI
- Backend/Platform
- Embedded/Edge
- Computer Vision
- Full-Stack AI
- Research/Applied AI
- Unknown

The domain is an emphasis lens, not a separate resume track.

## Depth

- D1 — scope + outcome/core technology
- D2 — engineering method + technology
- D3 — architecture/implementation/tests/constraints where directly relevant

Default: D2.

## Evidence rule

Map:

`JD requirement → verified evidence`

Direct evidence is foregrounded.
Adjacent evidence is framed honestly.
No evidence is omitted.

## Required outputs

```
versions/{track}/resume_{Company}.md
applications/{Company}_{YYYY-MM}/
  input.md
  pipeline_state.md
  interview_prep.md
`
