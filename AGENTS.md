# AGENTS.md — Resume Engine Contract

Single entry point. Read this file, then follow `pipeline/README.md`.

## What this is

A resume engine. Give it a job description and pick one mode; it produces the smallest,
strongest, truthful, one-page resume for that role. It is a compiler, not a prose generator.

Note on naming: the three modes are `startup`, `mnc`, `referral`. Display names and mode
settings live in `modes/{mode}.yaml`; this file does not restate them.

## Product

```
JD → select relevant candidate knowledge → render one-page resume → validate → deliver
```

One pipeline, three modes. A mode changes emphasis and selection; it never changes facts and
never forks the pipeline. Details live in `pipeline/README.md`, not here.

## Read order for a fresh task

1. `AGENTS.md` (this file)
2. `SPEC.md` — the system definition, requirements, and invariants (read once for orientation)
3. `pipeline/README.md` — the workflow you actually run
4. `RESUME_RULES.md`
5. `data/facts.yaml`
6. `content/github/evidence.md`
7. `content/github/boundaries.md`
8. the application input `applications/{Name}_{YYYY-MM}/input.md`
9. the mode config `modes/{mode}.yaml`

Do not load archived material or old runs unless the task requires them.

## Source of truth

| Need | Source |
|---|---|
| System definition, requirements, decisions | `SPEC.md` |
| Candidate facts | `data/facts.yaml` |
| Technical proof | `content/github/evidence.md` |
| Claim / ownership / status limits | `content/github/boundaries.md` |
| Mode settings | `modes/{mode}.yaml` + `versions/{mode}/_base.md` |
| Workflow | `pipeline/README.md` |
| Domain rules | `RESUME_RULES.md` |
| Hard rules | `DONT.MD` |
| Voice | `docs/voice.md` |
| Application requirements | `applications/{Name}_{YYYY-MM}/input.md` |
| Visual template | `templates/v3/` |
| Durable lessons | `memory/lessons.md` |
| Agent skills | `.agents/skills/` |

## Precedence

```
USER/TASK → APPLICATION INPUT → AGENTS.md → RESUME_RULES.md + boundaries.md
→ memory/lessons.md → research → inference
```

User corrections override repository content for the current task.

## Hard constraints

1. Truth outranks persuasion. Never invent metrics, ownership, employers, dates, production
   status, users, funding, or skills.
2. The template is the visual foundation. Do not redesign it.
3. The resume must stay ATS-parseable: single column, standard headings, selectable text,
   contact details in the body.
4. One page by default. Remove weak content before shrinking type.

Full rules: `RESUME_RULES.md`. Hard-fail checks: `DONT.MD`.

## Workflow

`pipeline/README.md` defines the pipeline: two phases (SELECT, RENDER), two invariants
(traceability, one page). Do not restate it here.

## Validation

Run `pipeline/validate_resume_repo.sh` before delivery. Build with `pipeline/build_base_resumes.sh`.
The FACT / FIT / READ / PARSE gates are defined in `RESUME_RULES.md`.

## Skills

Agent skills live in `.agents/skills/`. Local skills this repo owns: `latex-resume-render`
(produces the deliverable PDF) and `voice-guide`; neither is tracked in `skills-lock.json`.
Vendored skills are pinned there: `stop-slop` (prose), `find-skills`, `pdf`, and the
`mattpocock/skills` set (MIT) that supplies the engineering workflow (triage, specs,
tickets, TDD, review, PR, research).

Re-sync the Matt Pocock set into `.agents/skills/`:

```bash
npx skills@latest add mattpocock/skills -a universal -y --copy -s '*'
```

Never hand-edit a vendored skill; the next sync overwrites it. Skills are optional
tooling: the contract in this file and `RESUME_RULES.md` still governs every run, and no
skill overrides a hard constraint.

## Maintenance

- Keep one owner per rule. If two files state the same rule, delete one.
- Add a new rule only when it solves a demonstrated failure.
- History goes to `archive/`, never silently deleted.
- Do not add modules, wrappers, or abstraction layers that do not own a distinct responsibility.
