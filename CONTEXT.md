# CONTEXT.md - Resume Workspace

Primary working folder for building and maintaining active resume tracks from one factual master profile.

## Core principle

The resume is an evidence representation, not a writing exercise.

The system must optimize for:
- ATS retrieval
- recruiter scan
- technical hiring-manager evaluation
- human credibility

The strongest line is not the most polished line. It is the line that lets the reader see exactly what the candidate did.

## Source of truth

- `data/facts.yaml`: canonical biographical facts and approved resume data
- `content/github/evidence.md`: deep technical proof
- `content/github/boundaries.md`: claim, ownership, attribution, metric, and status constraints
- `applications/{Company}_{YYYY-MM}/input.md`: current application requirements
- `pipeline/`: execution workflow
- `versions/local/`: local-company outputs
- `versions/mnc/`: MNC/enterprise outputs

Source precedence:

USER/TASK -> APPLICATION -> AGENTS.md -> DONT.MD + boundaries.md -> memory/lessons.md -> research -> inference

Never use inference to manufacture candidate evidence.

## Active tracks

### referral

Targets forwarded/local-network applications.

Positioning:
Practical AI/software engineer with broad, understandable technical evidence.

Display name:
**Soham Karande**

### startup

Targets startups, founder outreach, direct applications, and small technical teams.

Positioning:
Builder with strong ownership across AI, software, systems, and product.

Display name:
**Soham Datta**

### mnc

Targets multinational and enterprise hiring teams.

Positioning:
AI/software engineer with precise technical evidence and conventional ATS-safe presentation.

Display name:
**Soham Datta**

There are exactly three active tracks. No domain may create a fourth track.

## Standard section order

Both active tracks default to:

1. Header / Contact
2. Summary
3. Experience
4. Projects
5. Education
6. Technical Skills
7. Certifications, only when verified

Do not reorder for visual novelty.

## Application model

Every application chooses:

### Track
`local` or `mnc`

### Primary Technical Domain

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

The domain is an emphasis lens, not a third resume track.

Derive it from the actual JD and verified candidate evidence. A company name or generic job title is not enough.

### Output Depth

- D1: scan level
- D2: engineering level
- D3: technical-proof level

Defaults:
- local: D2, D3 for strongly technical roles
- mnc: D1-D2, D3 only where implementation/research/systems depth is directly relevant

The evidence repository may retain D3 detail even when the resume uses D1 or D2.

## Evidence model

Candidate proof is classified as:

1. Implementation
2. Design
3. Problem-solving
4. Research
5. Product

Evidence classes are not decorative labels. Preserve them when selecting content so the writer knows what type of proof a claim represents.

## Evidence hierarchy

Prefer:

1. measured result
2. shipped artifact
3. quantified scope
4. technical decision
5. specific implementation detail
6. demonstrated ownership
7. process improvement
8. credible qualitative outcome
9. general responsibility

Specificity beats adjectives.

## Human-signal rule

A sentence earns space only when it materially explains at least one:

- action
- artifact
- problem
- decision
- constraint
- consequence
- technical depth
- ownership
- proof
- relevance

Otherwise cut it.

## Writing standard

Use:
- specific nouns
- concrete verbs
- implementation details
- real constraints
- real decisions
- real trade-offs
- verified tools
- verified outcomes
- concise sentences
- irregular but controlled rhythm
- high information density

Never make the candidate sound better than the evidence supports.

Avoid:
- motivational language
- corporate filler
- empty confidence
- ornamental adjectives
- generic storytelling
- fake sophistication
- repetitive Action + Method + Result formulas
- synonym swapping
- keyword stuffing

Cliche language may be used only when unavoidable as a literal technical term. Otherwise replace it with evidence.

## Writing modes

### Technical / Enterprise

Recruiter + hiring manager + ATS.

Use conventional terminology, minimal narrative, standard headings, concise bullets, high evidence density, and little/no first-person writing.

### Startup / Builder

Founder + small technical team.

Remain ATS-readable while showing more ownership, technical choices, constraints, and project identity. Limited first person is acceptable in profile/project framing.

Distinctiveness comes from evidence, not quirky formatting.

## Cold writing

Use:

FACT -> ACTION -> CONSEQUENCE / CONSTRAINT

Do not congratulate the candidate.

Do not tell the reader that a result is impressive. Show the mechanism that makes it meaningful.

## Technical credibility

For every technical claim ask:

Could the candidate explain exactly how this worked in an interview?

If not:
- weaken the verb
- remove the claim
- or locate better evidence

Never use:
architected, designed, implemented, optimized, deployed, led, or owned when the evidence only supports exposure, contribution, or usage.

For open-source work, preserve status and attribution precisely:
- issue authored
- specification authored
- PR authored
- maintainer reviewed
- maintainer approved
- downstream adopted
- merged
- draft
- closed/unmerged

These states are not interchangeable.

## Job-description alignment

Before drafting, extract:

- exact role title
- responsibilities
- must-have skills
- preferred skills
- core technologies
- domain terms
- seniority
- repeated concepts
- likely screening terms
- implied technical priorities
- business problem

Then map each requirement to verified candidate evidence.

Rules:
- direct evidence -> foreground
- adjacent evidence -> frame honestly
- no evidence -> omit

Use job terminology when truthful. Never copy the JD into the candidate's history.

## Skills

Skills are supporting evidence, not inventory.

Prioritize:
1. target-job relevance
2. proven usage
3. depth
4. recency
5. relevance to selected domain

Every major listed skill must be defensible in an interview.

## Projects

Choose projects by:
- target relevance
- technical depth
- evidence quality
- differentiation

For AI roles, favor systems work involving agents, LLMs, inference, retrieval, multimodal/voice systems, evaluation, backend/platform engineering, infrastructure, research, and hardware/software integration.

Do not include a project simply because its name sounds impressive.

## Metrics

Only use verified metrics.

Allowed examples:
latency, throughput, accuracy, memory use, battery life, model size, cost, test count, dataset size, deployment count, requests, users, percentage change, team size, repository adoption, downstream implementation.

Never reverse-engineer a convenient number.

When no metric exists, use:
- truthful scale
- observable outcome
- implementation detail
- real constraint

## ATS

Keep:
- standard section names
- searchable text
- predictable reading order
- standard date formats
- clean headings
- text-based PDF
- readable fonts
- conventional links
- one-column structure when parser safety is uncertain

Avoid:
- photos
- skill bars
- text embedded in images
- invisible keywords
- decorative icons replacing text
- complex tables where parser order may break
- critical contact data in headers/footers

Plain-text extraction test:
If formatting disappears, the resume must still be understandable.

## Template

When a template exists:
- preserve its structure
- preserve its visual hierarchy
- edit content inside it
- do not redesign without a real problem to solve

The same candidate should emerge, only clearer and more precise.

## Editing passes

Run independently:

1. Evidence
2. Relevance
3. Language
4. Density
5. Humanity
6. ATS
7. Hiring-manager scan
8. Interview defensibility
9. Cross-source consistency
10. Final BOOM Gate

## Final BOOM Gate

Before submission, verify:
- no fabricated facts
- no unsupported ownership
- no invented metrics
- no status inflation
- no contradictory dates/titles
- no JD copying
- no parser-hostile structure
- no obvious AI slop
- no unexplained critical gaps
- all high-value claims trace to evidence

## Human checkpoint

Before final writing, produce:
- Primary Technical Domain
- Output Depth
- Evidence Mix
- Foreground
- Compress
- Omit
- Material questions

If a material question is unresolved, stop before final drafting.

## Final output contract

A completed run must provide:

1. Target-role interpretation
2. Resume strategy
3. Selected evidence
4. Final resume content
5. ATS audit
6. Human-reader audit
7. AI-language audit
8. Unsupported-claim audit
9. Highest-risk weaknesses
10. Keep / cut / strengthen recommendation

## Master principle

Make the reader see more truth, not more polish.
