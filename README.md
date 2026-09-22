# Resume Workspace

Evidence-first resume engineering system for Soham Datta.

The repository maintains active local-company and MNC/enterprise resumes from one factual source, then tailors them to individual roles without changing the underlying evidence.

> Start with `MAP.md`. It defines the repository map, source hierarchy, application model, and workflow.

## Core rule

**Make the reader see more truth, not more polish.**

The system is optimized for four audiences at once:

- ATS/parser
- Recruiter scan
- Technical hiring manager
- Human reader

It does not optimize for an imaginary ATS score or for generic resume polish.

## Active tracks

| Track | Purpose | Base |
|---|---|---|
| Local | Local Indian IT/product companies and smaller engineering teams | `versions/local/_base.md` |
| MNC | Multinational and enterprise hiring | `versions/mnc/_base.md` |

Legacy `startup` and `midlevel` material is retained for recovery/history only.

## Source hierarchy

`data/facts.yaml` is the canonical fact layer.

`content/github/evidence.md` contains technical proof.

`content/github/boundaries.md` controls ownership, attribution, metrics, status, and claim safety.

Application-specific requirements live under `applications/`.

The resume writer may select, order, compress, and rewrite supported evidence. It may not manufacture facts.

## Standard structure

Both active tracks default to:

1. Header / Contact
2. Summary
3. Experience
4. Projects
5. Education
6. Technical Skills
7. Certifications, only when verified

The structure stays stable. The emphasis changes per role.

## Application model

Each application chooses:

- Track: `local` or `mnc`
- Primary Technical Domain
- Output Depth: D1, D2, or D3

Primary domains:

AI/ML, LLM/Agent Systems, Voice/Realtime AI, Backend/Platform, Embedded/Edge, Computer Vision, Full-Stack AI, Research/Applied AI, Unknown.

The domain is an emphasis lens, not a new resume track.

## Writing system

Resume language should be:

- direct
- specific
- evidence-led
- technically credible
- compact
- human
- easy to scan

Prefer concrete nouns, concrete verbs, implementation details, constraints, decisions, mechanisms, and verified outcomes.

Avoid generic career language, corporate filler, unsupported confidence, empty adjectives, repetitive Action + Method + Result formulas, JD copying, and keyword stuffing.

Do not make every bullet sound alike. Natural variation is useful when it improves clarity.

## Evidence standard

Evidence priority:

1. measured result
2. shipped artifact
3. quantified scope
4. technical decision
5. implementation detail
6. ownership
7. process improvement
8. qualitative outcome
9. generic responsibility

Use the strongest evidence available.

Never invent metrics, users, customers, technologies, responsibilities, job titles, dates, ownership, deployment status, production status, publication status, certifications, or research findings.

## Technical credibility

Every significant claim should survive:

**"Could the candidate explain exactly how this worked in an interview?"**

Open-source contributions must preserve exact attribution and status. Authored, approved, adopted downstream, merged, draft, and closed/unmerged are different states.

## Workflow

`pipeline/run.md` defines the execution sequence.

The current workflow is:

research -> JD analysis -> candidate context -> evidence match -> positioning/domain/depth gate -> writing -> factuality -> ATS -> final edit -> language/slop validation -> BOOM gate

A material uncertainty blocks final drafting until it is resolved.

## Templates

LaTeX templates live under `templates/`.

Current v3 is the resume-openfont base using XeLaTeX. It is a template layer only. Content decisions remain governed by the evidence and application system.

## Repository layout

```
data/                  canonical facts
content/github/        technical proof and boundaries
versions/local/        active local base + tailored resumes
versions/mnc/          active MNC base + tailored resumes
applications/          per-company runs
pipeline/              generation and application workflow
research/              company and role research
templates/             LaTeX export templates
memory/                durable lessons
archive/               historical material only
```

## Output rule

New application runs must target exactly one of:

```
local
mnc
```

No new resume track should be introduced just because a role has a different technical domain.

## Quality bar

A finished resume must be:

ATS-readable, technically credible, specific, compact, distinctive through evidence, targeted, easy to scan, hard to misunderstand, interview-defensible, and free of unsupported claims and obvious AI-generated slop.
