# AGENTS.md — Agent Behavior + Operating Rules

Canonical owner of how agents work in this repo. `agent.md` and `gemini.md` are pointers here.
This is a document workspace (structured YAML + markdown), not a coding project: no build, no tests, no runtime.

## Repo essence

Two active resume tracks are maintained from one factual source:

- `local`: local Indian IT/product companies and smaller engineering teams
- `mnc`: multinational companies and enterprise hiring teams

Legacy `startup` and `midlevel` folders may remain for history/recovery, but they are not active generation targets.

Domain terms, positioning, and writing rules: `CONTEXT.md`.

## Load policy

- START: `MAP.md`.
- ALWAYS: this file + `CONTEXT.md` + the task's `applications/{Company}_{YYYY-MM}/input.md`.
- PER TASK: `pipeline/run.md`, then only the stages it names. Read `data/facts.yaml`, `content/github/evidence.md`, and `content/github/boundaries.md` when writing or checking claims.
- GATES: `DONT.MD` §9 + §E19 for final validation.
- NEVER auto-load other runs' audit traces, `archive/`, or PDFs unless required by the task.

## Ownership

- Agent behaviour/loading/precedence/learning: this file.
- Project map, domain, positioning, active tracks: `CONTEXT.md`.
- Resume rules/failure prevention: `DONT.MD`.
- Facts: `data/facts.yaml`.
- Proof: `content/github/evidence.md`.
- Constraints: `content/github/boundaries.md`.
- Execution order: `pipeline/run.md`.
- Active outputs: `versions/local/` and `versions/mnc/`.
- Legacy outputs: `versions/startup/` and `versions/midlevel/`, history only.

## Source precedence

`USER/TASK → APPLICATION → THIS FILE → DONT.MD + boundaries.md → memory/lessons.md → research → INFERENCE`.

Truth and explicit requirements override inference. Never manufacture facts to satisfy a stage.

## Resume structure contract

Both active tracks use this default order:

1. Header / contact
2. Summary
3. Experience
4. Projects
5. Education
6. Technical Skills
7. Certifications, only when verified certification data exists

Do not reorder these sections for visual novelty.

### Local track

Use a clean, one-page, human-readable technical resume for local Indian IT/product companies.
Keep the exact section order above. Allow slightly more product/project context and a less ATS-dense writing style than MNC.

### MNC track

Use a one-page, single-column, ATS-safe resume.
Use conventional headings, searchable text, standard formatting, and concise technical bullets.

## Maintenance workflows

- Update a fact: edit `data/facts.yaml` only, then regenerate and validate.
- Add evidence: update `content/github/evidence.md` with verifiable proof.
- Add a constraint: update `content/github/boundaries.md`.
- New application: fill INPUT in `pipeline/APPLY.md`.
- New runs MUST select `local` or `mnc`.

## Agent handoff contract

When entering without conversation history:

1. Read `MAP.md`, `AGENTS.md`, `CONTEXT.md`.
2. Treat `data/facts.yaml` as canonical biography.
3. Read `content/github/evidence.md` and `content/github/boundaries.md` before changing claims.
4. Use detailed evidence files only as supporting proof.
5. Select only `local` or `mnc`.
6. Apply the section-order contract before drafting.
7. Run the defined pipeline and final BOOM gate before delivery.
8. Keep unresolved facts explicit rather than guessing.

## Learning loop

After meaningful work, distill durable lessons into `memory/lessons.md` only with evidence. Prefer consolidating existing entries.

## Dependency note

This file requires `CONTEXT.md`. `CONTEXT.md` requires nothing.
