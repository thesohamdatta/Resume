# APPLY.md — JD-to-Application Run Prompt

Fill in INPUT, paste the JD, and send this file to the agent.

You are the resume application agent for Soham Datta. Follow `AGENTS.md` + `CONTEXT.md`.

## INPUT

- Company: [Company]
- Run folder: `applications/[Company]_[YYYY-MM]/`
- Track: [local | mnc]
- JD (full text): [...]

## WORKFLOW

1. UNDERSTAND — Create `input.md` with company, track, full JD, and notes.
2. RESEARCH — Run Stage 01 or reuse a fresh company dossier.
3. MATCH — Run Stages 02→04 using only `facts.yaml` + evidence sources for candidate claims.
4. POSITION — Run Stage 05 and select one specific company↔candidate overlap.
5. TAILOR — Run Stage 06 against the selected active base:
   - `local` → `versions/local/_base.md`
   - `mnc` → `versions/mnc/_base.md`
6. VALIDATE — Run Stages 07→10. Stage 07 FAIL or Stage 10 drift FAIL stops the run.
7. PREPARE — Create interview prep with pitch, likely questions, gap defenses, and company-specific questions.
8. LEARN — Record only evidence-backed durable lessons.

## STRUCTURE CONTRACT

Both local and MNC resumes MUST use:

1. Header / Contact
2. Summary
3. Experience
4. Projects
5. Education
6. Technical Skills
7. Certifications, only if verified

Do not swap Experience/Projects/Education, do not move Skills above Experience, and do not add decorative sections just to fill space.

## TRACK DIFFERENCE

**Local**
- Target: local Indian IT/product companies and smaller engineering teams.
- Clean, human-readable, technical.
- Slightly more product/project context is acceptable.

**MNC**
- Target: multinational and enterprise hiring.
- One page, single column, ATS-safe.
- Conventional headings and formatting.
- No graphics, tables, columns, or decorative symbols carrying meaning.

Never invent metrics, users, scale, funding, ownership, production status, or qualifications.
