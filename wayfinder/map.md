# Repository Map

## Entry order

1. `MAP.md`
2. `AGENTS.md`
3. `CONTEXT.md`
4. `data/facts.yaml`
5. `content/github/evidence.md`
6. `content/github/boundaries.md`
7. application input
8. `pipeline/run.md`

## Active tracks

| Track | Purpose | Base |
|---|---|---|
| `referral` | Local referrals and forwarded applications | `versions/referral/_base.md` |
| `startup` | Startup/direct/founder applications | `versions/startup/_base.md` |
| `mnc` | MNC/enterprise hiring | `versions/mnc/_base.md` |

Legacy `local` and `midlevel` material is history/recovery only.

## Canonical ownership

- facts → `data/facts.yaml`
- technical proof → `content/github/evidence.md`
- ownership/status boundaries → `content/github/boundaries.md`
- voice → `docs/voice.md`
- hard rules → `DONT.MD`
- orchestration → `pipeline/run.md`
- stage contracts → `pipeline/stages/`
- base resumes → `versions/{referral,startup,mnc}/`
- template → `templates/v3/`
- application state → `applications/{Company}_{YYYY-MM}/`
- research → `research/`
- history → `archive/`

## Design principle

Deterministic work belongs in scripts/CI.
Contextual judgment belongs in the pipeline agents.

Do not maintain multiple active authorities for the same fact or rule.

## Output principle

A tailored resume is an application artifact generated from the canonical evidence system, not a new source of truth.
