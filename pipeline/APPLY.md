# APPLY.md — JD-to-Application Run Prompt

Fill in INPUT, paste the JD, and send this file to the agent.

You are the resume application agent for Soham Datta. Follow `AGENTS.md` + `CONTEXT.md`.

## INPUT

- Company: [Company]
- Run folder: `applications/[Company]_[YYYY-MM]/`
- Track: [local | mnc]
- JD (full text): [...]
- Optional candidate notes: [...]
- Optional domain/depth override: [leave blank unless confirmed by user]

## WORKFLOW

1. UNDERSTAND — Create `input.md` with company, track, full JD, and notes.
2. RESEARCH — Run Stage 01 or reuse a fresh company dossier.
3. MATCH — Run Stages 02→04 using only `facts.yaml` + evidence sources for candidate claims.
4. POSITION — Run Stage 05 and explicitly decide Primary Technical Domain, Output Depth, Evidence Mix, and Foreground/Compress/Omit.
5. HUMAN CHECK — Ask only material questions. Do not guess missing ownership, scope, outcomes, dates, certification status, domain, or depth.
6. TAILOR — Run Stage 06 against the selected active base.
7. VALIDATE — Run Stages 07→10. Stage 07 FAIL or Stage 10 drift FAIL stops the run.
8. PREPARE — Create interview prep with pitch, likely questions, gap defenses, and company-specific questions.
9. LEARN — Record only evidence-backed durable lessons.

## STRUCTURE CONTRACT

Both local and MNC resumes MUST use:

1. Header / Contact
2. Summary
3. Experience
4. Projects
5. Education
6. Technical Skills
7. Certifications, only if verified

## ADAPTATION CONTRACT

The active base defines structure, not fixed content.

Per application:
- choose one Primary Technical Domain
- choose D1/D2/D3 output depth
- preserve D3 proof in evidence sources even when output is D1/D2
- foreground the most relevant evidence
- compress adjacent domains
- omit low-signal detail when necessary

### Local
D2 default. D3 when the JD and primary domain reward technical implementation.

### MNC
D1–D2 default. D3 only when the JD clearly rewards technical implementation, systems, research, debugging, architecture, or similar proof.

The MNC resume should be technically credible, not technically exhaustive.

Never invent metrics, users, scale, funding, ownership, production status, or qualifications.
