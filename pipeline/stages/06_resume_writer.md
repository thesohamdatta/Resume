<!-- Stage 06: Resume Writer — Read by pipeline/run.md -->
# STAGE 06: RESUME WRITER

This stage owns the draft, not the facts.

## Read first

1. Stage 04 — Evidence Match
2. Stage 05 — Positioning
3. `content/github/evidence.md`
4. `data/facts.yaml`
5. Active base:
   - `versions/local/_base.md`
   - `versions/mnc/_base.md`

## Required resume order

The generated resume MUST use this exact default order:

1. Header / Contact
2. Summary
3. Experience
4. Projects
5. Education
6. Technical Skills
7. Certifications, only when verified certification data exists

This order applies to both local and MNC tracks.

## Track treatment

### Local
- One page.
- Clean and human-readable.
- Keep strong technical detail.
- Give projects enough context for a local IT/product recruiter to understand what was built.
- Avoid unnecessary ATS keyword repetition.

### MNC
- One page.
- Single column.
- Conventional headings.
- ATS-safe plain text structure.
- Use standard technical terminology and concise bullets.
- No visual formatting that can hide or confuse important text.

## Evidence-first bullet rules

- Start from evidence, then write the bullet.
- Include what was built/done, the concrete technology/method, and the observable result or purpose.
- Use exact numbers only when verified.
- Keep most bullets to 1–2 lines.
- Avoid passive voice and generic duty statements.
- Enforce `DONT.MD` and `content/github/boundaries.md`.
- Never change dates, titles, ownership, employer names, or project scope.

## Certifications

Only create the Certifications section when verified certification data exists in an approved source. A course, badge, or listed skill is not automatically a certification.

## Output

Write `versions/{local|mnc}/resume_{Company}.md` and the application cover letter.
