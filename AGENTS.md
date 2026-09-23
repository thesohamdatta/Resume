# AGENTS.md - Resume Engineering System

Canonical owner of agent behavior for this repository.

This repository is a resume engineering system, not a prose playground. The objective is to turn verified candidate evidence into the smallest, clearest, strongest representation of the candidate for one specific role.

## PRIME OBJECTIVE

Optimize four systems at once:

1. ATS parsing and terminology retrieval
2. Recruiter 5-15 second scan
3. Hiring-manager technical evaluation
4. Human impression

Never optimize one by damaging another. Do not chase an imaginary ATS score. Do not keyword-stuff. Do not paraphrase the job description.

The resume must read like it was written by a technically capable human who actually built, tested, debugged, shipped, researched, and learned from systems.

## SOURCE OF TRUTH

Use this precedence:

USER/TASK
-> APPLICATION INPUT
-> THIS FILE
-> DONT.MD + boundaries.md
-> memory/lessons.md
-> research
-> inference

Candidate facts must come from:

- `data/facts.yaml` = canonical biographical and factual data
- `content/github/evidence.md` = technical proof
- `content/github/boundaries.md` = ownership, attribution, metrics, and claim constraints
- `applications/{Company}_{YYYY-MM}/input.md` = current application specification

User corrections override repository content for the current task.

Never invent missing facts. Never turn:

- exposure into expertise
- contribution into ownership
- prototype into production
- draft into merged work
- course/project work into professional experience
- plausible inference into a fact

Truth outranks persuasion.

## REQUIRED LOADING

For a fresh task:

1. Read `MAP.md`
2. Read `AGENTS.md`
3. Read `CONTEXT.md`
4. Read the relevant application input
5. Before making candidate claims, read `data/facts.yaml`, `content/github/evidence.md`, and `content/github/boundaries.md`
6. Run the workflow in `pipeline/run.md`
7. Apply final hard-fail checks from `DONT.MD`

Do not automatically load unrelated old runs, archive material, or PDFs unless the task specifically requires them.

## ACTIVE RESUME TRACKS

There are exactly three active tracks:

- `referral` = local referrals and forwarded applications; display name `Soham Karande`
- `startup` = startup applications, founder outreach, and direct applications; display name `Soham Datta`
- `mnc` = multinational and enterprise hiring; display name `Soham Datta`

Legacy `local` and `midlevel` material is recovery/history only.

Do not create additional active tracks.

## APPLICATION MODEL

Every application must make three decisions:

### 1. Track

`referral`, `startup`, or `mnc`.

### 2. Primary Technical Domain

Choose one from:

- AI/ML
- LLM/Agent Systems
- Voice/Realtime AI
- Backend/Platform
- Embedded/Edge
- Computer Vision
- Full-Stack AI
- Research/Applied AI
- Unknown

The domain is an emphasis lens, not another resume track.

Derive it from the job description and verified candidate evidence. Do not infer it from company brand or generic title.

If the domain is materially unclear, mark it Unknown and ask before finalizing.

### 3. Output Depth

- D1: scan level. Scope + outcome + core technology.
- D2: engineering level. Outcome + important method + technology. Default for technical hiring.
- D3: technical proof. Implementation detail, architecture, algorithms, tests, constraints, debugging, or research evidence.

The evidence repository may remain D3 even when the final resume is D1/D2.

Defaults:

- referral = D2, use D3 for clearly technical roles or the primary domain
- startup = D2, use D3 when technical depth materially strengthens builder signal
- mnc = D1-D2, use D3 only where the JD explicitly rewards implementation, systems, research, debugging, or architecture depth

## EVIDENCE MODEL

Treat candidate evidence as typed proof:

1. Implementation: code, architecture, integration, tests, infrastructure
2. Design: specs, RFCs, ADRs, workflows, contracts
3. Problem-solving: diagnosis, root cause, fixes
4. Research: literature, experiments, evaluation, papers
5. Product: requirements, UX/product decisions, prototypes

Preserve the underlying type when selecting and compressing evidence.

## EVIDENCE HIERARCHY

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

Do not replace strong evidence with weaker adjectives.

A distinctive technical detail is often stronger than a generic accomplishment claim.

## HUMAN-SIGNAL RULE

Every sentence must materially answer at least one:

- What did the candidate actually do?
- What did they build?
- What problem did they solve?
- What decision did they make?
- What constraint did they operate under?
- What changed because of the work?
- What technical depth does it reveal?
- What ownership does it reveal?
- What evidence makes the claim believable?
- Why is it relevant to this job?

If a sentence answers none, delete it.

## WRITING STANDARD

Use:

- specific nouns
- concrete verbs
- technical details
- real constraints
- real decisions
- real trade-offs
- real tools
- verified outcomes
- concise sentences
- controlled rhythm
- high information density

Use the minimum verb strength supported by evidence.

Examples:

- used / integrated when the candidate mainly used a system
- implemented when the candidate wrote the behavior
- designed when the candidate made the design decision
- architected only when the candidate owned the architecture
- deployed only when there is actual deployment evidence
- optimized only when there is evidence of an optimization and its basis

Prefer concrete verbs such as built, implemented, designed, adapted, integrated, diagnosed, debugged, instrumented, benchmarked, tested, validated, deployed, automated, migrated, tuned, prototyped, evaluated, researched, authored, and contributed. Do not rotate them mechanically.

## COLD WRITING

State:

FACT -> ACTION -> CONSEQUENCE/CONSTRAINT

Do not congratulate the candidate. Do not explain why something is impressive.

Avoid:

"Passionately developed an innovative AI system that significantly improved the user experience."

Prefer:

"Built a real-time voice agent with LiveKit and Gemini realtime inference, then integrated ElevenLabs for speech output."

Add a result only when the result is real and supported.

## ANTI-CLICHE / ANTI-SLOP

Aggressively remove generic substitutes for evidence, including:

results-driven, passionate, highly motivated, proven track record, innovative thinker, dynamic professional, detail-oriented, strategic thinker, team player, go-getter, visionary, hard-working, enthusiastic, responsible for, worked on, helped with, involved in, leveraged, utilized, spearheaded, orchestrated, synergized, drove alignment, cutting-edge, next-generation, game-changing, transformative, world-class, mission-driven, seamless, robust, scalable.

These are not forbidden as words. They are rejected when they replace concrete evidence or create synthetic resume language.

Do not attempt to defeat AI detectors. Eliminate the underlying problem: generic writing.

## NATURAL LANGUAGE

Do not make every bullet follow the same grammar.

Avoid repeated:

"Developed X using Y, resulting in Z."

Natural variation is preferred when it improves information density:

"Built..."
"Reduced..."
"Designed..."
"Integrated..."
"Reworked..."
"Benchmarked..."
"Tested..."
"Moved..."
"Replaced..."
"Implemented..."
"Validated..."
"Published..."

Do not vary words merely to look human. Choose the verb that matches the evidence.

## FIRST PERSON POLICY

### Technical / Enterprise mode

Use implied first person:

"Built an ESP32-S3 wearable AI prototype..."

not:

"I built..."

### Startup / Builder mode

Limited first person is allowed in the profile or selected project framing where ownership matters.

Example:

"I build small AI systems at the edge, where hardware constraints, latency, privacy, and model capability meet."

Do not repeat first person throughout the resume.

## OUTPUT MODES

### MODE A - TECHNICAL / ENTERPRISE

Audience:

Recruiter, hiring manager, engineering manager, ATS.

Characteristics:

- one page
- conventional structure
- concise technical evidence
- exact job-relevant terminology
- conservative formatting
- minimal narrative
- minimal first-person language
- strong technical nouns and verbs
- quantified outcomes when verified

### MODE B - STARTUP / BUILDER

Audience:

Founder, startup hiring manager, small engineering team, technical lead.

Characteristics:

- still ATS-readable
- stronger ownership signal
- more visible technical decisions
- more project identity
- slightly more conversational
- selective first person
- unusual technical details where useful

Never become casual or quirky merely to look different.

A distinctive resume should be distinctive because the evidence is distinctive.

## JOB DESCRIPTION ALIGNMENT

Analyze the JD before writing.

Extract:

- exact role title
- primary responsibilities
- must-have skills
- preferred skills
- core technologies
- domain language
- seniority expectations
- repeated concepts
- likely screening terms
- implied technical priorities
- business problem

Then map:

JD requirement -> verified candidate evidence

Rules:

- direct evidence -> foreground
- adjacent evidence -> frame honestly
- no evidence -> omit

Use employer terminology when truthful. Never copy the JD.

## BULLET ENGINE

A bullet should attempt to contain:

ACTION + OBJECT + TECHNICAL CONTEXT + RESULT / CONSTRAINT / SCALE

Not every bullet requires all four.

Prioritize information density over formulaic consistency.

## RESULT DISCIPLINE

Use a metric only when it is verified and meaningful.

Useful evidence includes:

latency, throughput, accuracy, memory, battery life, model size, cost, users, requests, datasets, experiments, test counts, deployment counts, percentages, team size, repository adoption, or downstream implementation.

Never reverse-engineer a convenient metric from weak evidence.

When no metric exists, use:

- truthful scale
- observable outcome
- implementation detail
- concrete constraint

## IMPACT THROUGH MECHANISM

Weak:

"Improved privacy."

Strong:

"Kept continuous audio processing on-device and limited cloud transmission to user-triggered or event-driven captures."

Mechanisms make claims believable.

## TECHNICAL CREDIBILITY TEST

For every major technical statement ask:

"Could the candidate explain exactly how this worked in an interview?"

If no, weaken or delete.

Ownership is not interchangeable with contribution.

For open-source work distinguish clearly between:

- authored issue/spec
- authored PR
- maintainer review
- maintainer approval
- downstream adoption
- merged work
- draft work
- closed/unmerged work

Never claim a downstream maintainer PR as candidate-authored work unless evidence explicitly supports it.

## SKILLS

Do not create giant technology inventories.

Prioritize skills by:

1. target job requirements
2. proven usage
3. depth
4. recency
5. relevance

Every major skill must be interview-defensible.

Prefer grouped, searchable categories over an indiscriminate list.

## PROJECT SELECTION

Select projects by:

- relevance
- technical depth
- proof
- differentiation

For AI roles, prioritize evidence showing:

systems thinking, model integration, inference, agents, retrieval, multimodal systems, voice systems, backend/platform engineering, evaluation, research, infrastructure, hardware/software integration.

Do not include projects because the name sounds impressive.

## INFORMATION ARCHITECTURE

Default active-track order:

1. Header / Contact
2. Summary
3. Experience
4. Projects
5. Education
6. Technical Skills
7. Certifications, only when verified

Do not reorder sections for novelty.

Give more space to a strong technical system than to a minor certificate.

## ATS / FILE SAFETY

Default to:

- standard section names
- predictable reading order
- standard dates
- text-based PDF
- readable fonts
- searchable text
- conservative hierarchy
- no photos
- no skill bars
- no decorative icons that replace text
- no critical contact information in headers/footers
- no invisible keywords
- no text embedded in images
- no complex layout when parser safety is uncertain

Run a plain-text extraction test:

If all formatting disappears, the resume must still make sense.

## TEMPLATE RULE

When a template exists:

- preserve its intended structure
- preserve its visual hierarchy
- optimize content inside the template
- do not redesign merely to look different

The candidate should look like the same person became more precise.

## EDITING PASSES

Run these separately:

### Pass 1 - Evidence
Extract every factual claim. Delete unsupported claims.

### Pass 2 - Relevance
Map every claim to the target role. Cut low-value evidence.

### Pass 3 - Language
Replace vague language with specific language.

### Pass 4 - Density
Remove unnecessary words without removing meaning.

### Pass 5 - Humanity
Break repetitive AI-like sentence patterns. Remove synthetic symmetry.

### Pass 6 - ATS
Check section names, reading order, searchable text, terminology, and parser safety.

### Pass 7 - Hiring Manager
Ask:

"What is this candidate actually unusually good at?"

That answer must become visible within seconds.

### Pass 8 - Interview Defensibility
Challenge every major claim against the evidence repository.

### Pass 9 - Cross-source consistency
Check dates, titles, project names, links, scope, status, ownership, and metrics against the source of truth.

### Pass 10 - Final BOOM Gate
Apply the hard-fail rules in DONT.MD.

## ASK-BEFORE-ASSUME

Stop and ask the user when a missing fact materially changes:

- primary technical domain
- output depth
- ownership or attribution
- certification status
- employment dates or job title
- quantified outcomes
- project scope
- prototype vs production status

Otherwise proceed with the supported evidence and omit unsupported details.

Never create a plausible bridge across a gap.

## NEVER INVENT

Never invent:

- metrics
- responsibilities
- technologies
- job titles
- employment dates
- leadership
- team size
- users
- customers
- funding
- revenue
- awards
- publications
- certification status
- research findings
- performance improvements
- production status
- ownership
- deployment status

## FINAL OUTPUT CONTRACT

When asked to engineer a resume, return:

1. Target-role interpretation
2. Resume strategy
3. Selected evidence
4. Final resume content
5. ATS audit
6. Human-reader audit
7. AI-language audit
8. Unsupported-claim audit
9. Highest-risk weaknesses
10. Final recommendation on what to keep, cut, or strengthen

## MASTER PRINCIPLE

Do not make the candidate sound better than they are.

Make the reader see more clearly how good the evidence already is.

Every word must earn its space.
