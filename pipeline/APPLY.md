# APPLY.md — JD-to-Application Run Prompt

Fill in INPUT, paste the JD, and send this file to the agent.

Follow `AGENTS.md` + `CONTEXT.md`. Candidate facts come only from the canonical evidence system.

## INPUT

- Company: [Company]
- Run folder: `applications/[Company]_[YYYY-MM]/`
- Track: [referral | startup | mnc]
- JD (full text): [...]
- Optional candidate notes: [...]
- Optional domain/depth override: [leave blank unless confirmed by the user]

## WORKFLOW

1. UNDERSTAND — Create/update `input.md` with company, track, JD, and notes.
2. RESEARCH — Research the actual employer and role, or reuse a fresh company dossier.
3. MATCH — Run Stages 02→04 using only canonical candidate facts and evidence.
4. POSITION — Run Stage 05 and decide domain, depth, evidence mix, foreground/compress/omit.
5. HUMAN CHECK — Ask only correctness-critical questions. Never guess ownership, scope, dates, status, certification state, or metrics.
6. TAILOR — Run Stage 06 against the selected active base.
7. VALIDATE — Run Stages 07→10. Any factuality FAIL or drift FAIL blocks delivery.
8. PREPARE — Create interview prep around the role and the claims actually used.
9. LEARN — Record only durable, evidence-backed lessons.

## TRACKS

### referral
Display name: **Soham Karande**

Use for:
- forwarded applications
- relatives/friends/professional referrals
- local networks
- Pune/Jabalpur and similar referral channels

Style:
clear, broad, practical, technically credible.

### startup
Display name: **Soham Datta**

Use for:
- startups
- founder outreach
- early-stage teams
- direct LinkedIn outreach

Style:
strong ownership, building, product sense, technical breadth, ambiguity tolerance.

### mnc
Display name: **Soham Datta**

Use for:
- multinational companies
- enterprise companies
- large technical hiring pipelines

Style:
ATS-safe, precise, conventional, evidence-dense.

## CONTROLLED DOMAIN

Choose exactly one:

- AI/ML
- LLM/Agent Systems
- Voice/Realtime AI
- Backend/Platform
- Embedded/Edge
- Computer Vision
- Full-Stack AI
- Research/Applied AI
- Unknown

The domain changes emphasis, not facts.

## OUTPUT DEPTH

- D1 — scan level
- D2 — engineering level
- D3 — technical-proof level

Default: D2.

Use D3 only when the target role rewards implementation, architecture, debugging, research, systems detail, or similar proof.

## RESEARCH COMPLETION TEST

Research is complete only when it changes at least one of:

- experience evidence selection
- project selection
- bullet depth
- technical skills emphasis
- primary domain
- output depth
- foreground/compress/omit decisions

Research that only repeats company history is not useful for resume tailoring.

## EXPERIENCE / PROJECT PRIORITY

Use the strongest relevant experience first.

Projects support the same story rather than competing with it.

For a technical role:
relevant Experience → supporting Projects → focused Skills.

Do not preserve weak bullets just because they fit a section.

## CLAIM SAFETY

Never invent:

- metrics
- users
- customers
- scale
- funding
- ownership
- production status
- technologies
- qualifications
- employment dates
- project scope
- publications
- certifications

The JD defines relevance.
The evidence defines reality.

## FINAL QUALITY TEST

Before delivery, verify:

1. Target role is obvious.
2. Strongest evidence appears early.
3. Projects reinforce the selected technical domain.
4. Every important claim is defensible.
5. Language is specific and human.
6. The resume is one page unless a documented application need requires otherwise.
7. The final PDF is searchable and visually intact.
8. No stale track/template/path references remain in the output.
