# AGENTS.md — Agent Behavior + Operating Rules

Canonical owner of how agents work in this repo. `agent.md` and `gemini.md` are pointers here.
This is a document workspace (structured YAML + markdown), not a coding project: no build, no tests, no runtime.

## Repo essence

Three resume tracks (startup, MNC, mid-level) generated from `data/facts.yaml` via `pipeline/run.md`.
Domain terms, positioning, and writing rules: `CONTEXT.md` (load it with this file).

## Load policy (progressive disclosure)

- START: `MAP.md` (one-page index — where everything lives).
- ALWAYS: this file + `CONTEXT.md` + the task's `applications/{Company}_{YYYY-MM}/input.md`.
- PER TASK: `pipeline/run.md`, then only the stages it names. `data/facts.yaml` + `content/github/evidence.md` + `content/github/boundaries.md` when writing or checking claims.
- GATES: `DONT.MD` §9 (rule index) + §E19 (BOOM gate) for final validation — not a full read. Full `DONT.MD` only when a gate fails or a new rule is needed.
- RARELY: `research/README.md` index (external evidence), `memory/lessons.md` (after meaningful work), `templates/` (LaTeX export only).
- NEVER auto-load: other runs' `applications/*/pipeline_state.md` (audit traces), `archive/` (history), PDFs unless the task is PDF work, `.agents/skills/*` except the two Stage 10 names.

## Ownership (one owner per knowledge type)

- Behavior/loading/precedence/learning: this file.
- Project map + domain + positioning: `CONTEXT.md`.
- Resume rules / failure prevention: `DONT.MD` (canonical — never restate its rules elsewhere).
- Facts: `data/facts.yaml`. Proof: `content/github/evidence.md`. Constraints: `content/github/boundaries.md`.
- Execution order: `pipeline/run.md` (DONT.MD §§0-2 are methodology invariants, not the execution sequence).
- Tool skills: `.agents/skills/*` (installed via `skills-lock.json` — do not move).
- Outputs: `versions/{track}/` (`_base.md` + `resume_{Company}.md`). Active state: `applications/*/`.

## Source precedence

`USER/TASK → APPLICATION (input.md notes/track) → THIS FILE → DONT.MD + boundaries.md → memory/lessons.md → research → INFERENCE`. Truth and explicit requirements always override inference. Never manufacture facts to satisfy a stage.

## Maintenance workflows

- Update a fact: edit `data/facts.yaml` only → regenerate outputs → validate against `boundaries.md`.
- Add evidence: `content/github/evidence.md` with verifiable proof (repo links, file paths, code refs).
- Add a constraint: `content/github/boundaries.md` + regex if automatable.
- New company run: fill INPUT in `pipeline/APPLY.md` and send it to the agent (creates `applications/{Company}_{YYYY-MM}/input.md` and runs the full workflow).
- Deep research (new/stale dossier, people + outreach intel needed): fill INPUT in `research/SWARM_RESEARCH.md` and send it as-is before APPLY.md.
- Roadmap (human-owned, see README): build script rendering tracks from `facts.yaml`; `validate.py` against `boundaries.md` patterns.

## Learning loop (controlled)

After meaningful work, distill durable lessons into `memory/lessons.md` ONLY with evidence (repeated failure, validated improvement, new convention, corrected rule, workflow pattern). Prefer consolidating existing entries over appending. Never rewrite rules after every task; never change `DONT.MD` or `boundaries.md` without a verified case. Log each durable change as one line: date + what + evidence.

## Where new knowledge belongs

Resume rule → `DONT.MD`. Fact → `facts.yaml`. Proof → `evidence.md`. Constraint → `boundaries.md`. Company dossier → `research/companies/{Company}.md` (Stage 01 schema). Run trace → `applications/*/pipeline_state.md`. Durable agent lesson → `memory/lessons.md`. Everything else → ask whether it earns a file.

## Dependency note

This file requires `CONTEXT.md`. `CONTEXT.md` requires nothing (its mention of this file is discovery, not a dependency). No load cycles.
