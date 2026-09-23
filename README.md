# Resume Workspace

Evidence-first resume engineering system for Soham.

The repository converts one verified body of candidate evidence into three one-page resume tracks:

- `referral` — forwarded/local-network applications
- `startup` — startups, founder outreach, direct applications
- `mnc` — multinational and enterprise hiring

The system separates candidate facts, technical evidence, claim boundaries, application context, and document presentation.

## Core rule

**Make the reader see more truth, not more polish.**

The system optimizes for:
- ATS parsing
- recruiter scan speed
- technical hiring-manager evaluation
- human credibility

It does not optimize for imaginary ATS scores, keyword stuffing, or generic resume polish.

## Source hierarchy

| Need | Canonical source |
|---|---|
| Biographical facts | `data/facts.yaml` |
| Technical proof | `content/github/evidence.md` |
| Ownership / status / attribution boundaries | `content/github/boundaries.md` |
| Application requirements | `applications/{Company}_{YYYY-MM}/input.md` |
| Pipeline | `pipeline/run.md` |
| Durable lessons | `memory/lessons.md` |
| Document layout | canonical template under `templates/` |

Historical resumes are recovery material only. They never override the evidence layer.

## Active tracks

| Track | Purpose | Display name |
|---|---|---|
| `referral` | Local referrals and forwarded applications | **Soham Karande** |
| `startup` | Startup, founder, direct outreach | **Soham Datta** |
| `mnc` | MNC and enterprise hiring | **Soham Datta** |

Track selection changes emphasis, ordering, wording, and depth. It never changes facts.

## Application model

Every run determines:

1. Track
2. Primary technical domain
3. Output depth
4. Evidence mapping
5. Content selection

Primary technical domains:

AI/ML, LLM/Agent Systems, Voice/Realtime AI, Backend/Platform, Embedded/Edge, Computer Vision, Full-Stack AI, Research/Applied AI, Unknown.

Output depth:

- D1 — scan level
- D2 — engineering level
- D3 — technical proof

## Standard structure

Default section order:

1. Header / Contact
2. Summary
3. Experience
4. Projects
5. Education
6. Technical Skills
7. Certifications, only when verified

The order stays stable unless a real application requirement justifies a change.

## Writing system

Write like a technically capable human:

- concrete nouns
- accurate verbs
- technical details
- real constraints
- verified outcomes
- concise sentences
- natural rhythm

Do not use polish as a substitute for evidence.

## Evidence standard

A claim should survive:

**Could Soham explain exactly how this worked in an interview?**

Preserve distinctions between:

- contribution and ownership
- issue and implementation
- approval and merge
- downstream adoption and authorship
- prototype and production
- tool exposure and proficiency

## Repository layout

```
data/                  canonical facts
content/               technical proof and boundaries
versions/              active track bases and tailored outputs
applications/          per-company application runs
pipeline/              generation workflow
research/              external research
memory/                durable lessons
templates/             canonical LaTeX template + references
archive/               historical material only
```

## Output principle

The active resume should be the smallest useful representation of the evidence base for the target role.

Make the evidence easier to see.
Do not make the candidate sound better than the evidence supports.
