# STAGE 06: RESUME WRITER

This stage owns the draft, not the facts.

## Read first

1. Stage 04 — Evidence Match
2. Stage 05 — Positioning
3. `content/github/evidence.md`
4. `data/facts.yaml`
5. `content/github/boundaries.md`
6. Active base:
   - `versions/local/_base.md`
   - `versions/mnc/_base.md`

## Required resume order

1. Header / Contact
2. Summary
3. Experience
4. Projects
5. Education
6. Technical Skills
7. Certifications, only when verified certification data exists

This order applies to both active tracks.

## Domain-first writing

Use the Stage 05 **Primary Technical Domain** as the main technical lens.

Within that domain:
- foreground the strongest verified evidence
- prefer evidence with direct relevance and strong proof
- preserve concrete technology/method where the chosen depth requires it
- compress unrelated technical breadth
- omit low-signal details when page space is constrained

Do not force every project, tool, or technical subsystem onto the resume.

## Output depth

Follow Stage 05 exactly:
- D1: scope + result/purpose + core technology
- D2: scope + important implementation method + technology + result/purpose
- D3: technical implementation, architecture, algorithm, test, constraint, or debugging detail where verified

The same Aura evidence may therefore produce a D2/D3 bullet for a technical local role and a D1/D2 bullet for an enterprise role. The evidence source remains unchanged.

## Track treatment

### Local
- One page.
- Clean and human-readable.
- D2 default.
- Allow D3 for a highly technical primary-domain application.
- Keep enough project context to explain what was built.

### MNC
- One page.
- Single column.
- Conventional headings.
- ATS-safe plain text structure.
- D1–D2 default.
- D3 only where the JD explicitly earns that depth.
- Do not turn the resume into an implementation diary.

## Evidence-first bullet rules

- Start from evidence, then write the bullet.
- Include only the technical detail justified by Stage 05 depth.
- Use exact numbers only when verified.
- Keep most bullets to 1–2 lines.
- Never change dates, titles, ownership, employer names, or project scope.
- Enforce `DONT.MD` and `content/github/boundaries.md`.

## Certifications

Only create the Certifications section when verified certification data exists in an approved source. A course, badge, or listed skill is not automatically a certification.

## Output

Write `versions/{local|mnc}/resume_{Company}.md` and the application cover letter.
