# AGENTS.md — Agent Behavior + Operating Rules

Canonical owner of how agents work in this repo. `agent.md` and `gemini.md` are pointers here.
This is a document workspace (structured YAML + markdown), not a coding project: no build, no tests, no runtime.

## Repo essence

Two active resume tracks are maintained from one factual source:

- `local`: local Indian IT/product companies and smaller engineering teams
- `mnc`: multinational companies and enterprise hiring teams

Legacy `startup` and `midlevel` folders may remain for history/recovery, but they are not active generation targets.

Domain terms, positioning, evidence architecture, and writing rules: `CONTEXT.md`.

## Load policy

- START: `MAP.md`.
- ALWAYS: this file + `CONTEXT.md` + the task's `applications/{Company}_{YYYY-MM}/input.md`.
- PER TASK: `pipeline/run.md`, then only the stages it names.
- Before candidate claims: read `data/facts.yaml`, `content/github/evidence.md`, and `content/github/boundaries.md`.
- GATES: `DONT.MD` §9 + §E19 for final validation.
- NEVER auto-load other runs' audit traces, `archive/`, or PDFs unless required.

## Ownership

- Agent behavior/loading/precedence/learning: this file.
- Project map, active tracks, domain model, depth model, evidence taxonomy: `CONTEXT.md`.
- Resume rules/failure prevention: `DONT.MD`.
- Facts: `data/facts.yaml`.
- Proof/evidence: `content/github/evidence.md`.
- Claim constraints: `content/github/boundaries.md`.
- Execution order: `pipeline/run.md`.
- Active outputs: `versions/local/` and `versions/mnc/`.
- Legacy outputs: `versions/startup/` and `versions/midlevel/`, history only.

## Source precedence

`USER/TASK → APPLICATION → THIS FILE → DONT.MD + boundaries.md → memory/lessons.md → research → INFERENCE`.

Truth and explicit requirements override inference. Never manufacture facts to satisfy a stage.

## Resume structure contract

Both active tracks default to:

1. Header / contact
2. Summary
3. Experience
4. Projects
5. Education
6. Technical Skills
7. Certifications, only when verified certification data exists

Do not reorder sections for visual novelty.

## Domain-first application model

Every application MUST choose one **Primary Technical Domain** before drafting.

The domain is an emphasis lens, not a new resume track. Examples include:
- AI/ML
- LLM/Agent Systems
- Voice/Realtime AI
- Backend/Platform
- Embedded/Edge
- Computer Vision

The chosen domain determines which verified evidence is foregrounded and which strong but less relevant evidence is compressed or omitted.

Do not assume the domain from a company name alone. Derive it from the JD and candidate evidence. If the JD does not make the domain clear, mark it `unknown` and ask before finalizing.

## Depth model

Technical detail is **adaptive**, not globally shallow or globally deep.

Use three output depths:
- **D1 — Executive/scan:** outcome, scope, core technology. Minimal implementation detail.
- **D2 — Engineering:** outcome + important implementation method + technology. Default for technical hiring.
- **D3 — Technical-proof:** implementation details, architecture, algorithms, tests, constraints, or debugging evidence. Use selectively when the JD rewards technical depth.

Rule: the evidence layer may be D3 even when the resume output is D1/D2. Never throw away evidence simply because one resume does not show it.

Track defaults:
- Local: D2 by default; D3 for a clearly technical role or a primary-domain project.
- MNC: D1–D2 by default; D3 only where the JD explicitly rewards implementation depth or research/engineering proof.

## Evidence taxonomy

Treat candidate proof as typed evidence:
1. **Implementation** — code, architecture, integration, tests, infrastructure.
2. **Design** — specs, RFCs, ADRs, workflows, interface contracts.
3. **Problem-solving** — bugs, debugging, root-cause analysis, fixes.
4. **Research** — literature review, experiments, papers, evaluation.
5. **Product** — requirements, user stories, UX/product decisions, prototypes.

Evidence types are complementary. A resume bullet may combine types, but the pipeline should preserve the underlying type.

## Ask-before-assume rule

Ask the user when a missing fact would materially change:
- primary technical domain,
- depth level,
- ownership/attribution,
- certification status,
- employment dates/title,
- quantified outcomes,
- project scope,
- whether a prototype was deployed/productionized.

Never invent a bridge across a missing fact. Record `[needs user confirmation]` and proceed only where the uncertainty does not affect correctness.

## Human checkpoint

Before final resume writing, Stage 05 must produce:
- Primary Technical Domain
- Output Depth
- Evidence mix
- Foreground / compress / omit decisions
- Any material question for the user

If a material question is unresolved, stop before Stage 06.
