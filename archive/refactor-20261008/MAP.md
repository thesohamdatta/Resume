# MAP.md - Resume Repository Map

This file answers: where does each piece of the resume system live?

## Agent entry

For a fresh agent:

1. `MAP.md`
2. `AGENTS.md`
3. `CONTEXT.md`
4. `data/facts.yaml`
5. `content/github/evidence.md`
6. `content/github/boundaries.md`
7. Relevant application input
8. `pipeline/run.md`

## Active tracks

| Track | Target | Base |
|---|---|---|
| `referral` | Local referrals and forwarded applications | `versions/referral/_base.md` |\n| `startup` | Startups and founder/direct outreach | `versions/startup/_base.md` |
| `mnc` | MNC/enterprise hiring | `versions/mnc/_base.md` |

Legacy `local` and `midlevel` are recovery/history only.

## Application decisions

Every application has:

1. Track: `referral`, `startup`, or `mnc`
2. Primary Technical Domain: AI/ML, LLM/Agent Systems, Voice/Realtime AI, Backend/Platform, Embedded/Edge, Computer Vision, Full-Stack AI, Research/Applied AI, Unknown
3. Output Depth: D1, D2, or D3

Do not create a new resume track for a domain.

## Source of truth

| Need | Source |
|---|---|
| Biographical facts | `data/facts.yaml` |
| Technical proof | `content/github/evidence.md` |
| Claim/ownership/status boundaries | `content/github/boundaries.md` |
| Application requirements | `applications/{Company}_{YYYY-MM}/input.md` |
| Workflow | `pipeline/run.md` |
| Active referral base | `versions/referral/_base.md` |\n| Active startup base | `versions/startup/_base.md` |
| Active MNC base | `versions/mnc/_base.md` |
| Templates | `templates/` |
| Durable lessons | `memory/lessons.md` |

## Standard resume structure

Header / Contact
-> Summary
-> Experience
-> Projects
-> Education
-> Technical Skills
-> Certifications (only when verified)

## Evidence classes

- Implementation
- Design
- Problem-solving
- Research
- Product

## Pipeline

1. Company research
2. JD analysis
3. Candidate context
4. Evidence mapping
5. Positioning/domain/depth gate
6. Resume writing
7. Factuality gate
8. ATS review
9. Final editor
10. Slop/language polish
11. Final BOOM validation

## Writing contract

The system optimizes:
ATS precision + recruiter scan speed + hiring-manager technical clarity + human credibility.

Write from evidence.

Do not use polish as a substitute for proof.

Every meaningful line should communicate action, artifact, problem, decision, constraint, consequence, technical depth, ownership, evidence, or relevance.

## Output principle

The active resume must be the smallest useful representation of the evidence base for the target role.

Do not make the candidate sound better than the evidence supports.
Make the evidence easier to see.
