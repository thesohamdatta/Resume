<!-- run.md — Pipeline Entry Point: reads input.md and chains all 10 stages -->

# Resume Pipeline — Run

## What this does

Given `applications/{Company}_{YYYY-MM}/input.md`, this orchestrates all 10 stages to produce:
- `versions/{track}/resume_{Company}.md`
- `applications/{Company}_{YYYY-MM}/cover_letter.md`

## How to invoke

Tell the agent:
> Run the resume pipeline for [Company] application in `applications/{Company}_{YYYY-MM}/`.

The agent reads this file and executes the stages in order.

---

## Stage Execution Order

### Step 1 — Read input
Read `applications/{Company}_{YYYY-MM}/input.md`. Extract:
- `company:` → determines which company context file to use/create
- `track:` → determines which base resume to modify (`startup` | `mnc` | `midlevel`)
- `jd:` → full job description text
- `notes:` → special framing instructions

Initialize `applications/{Company}_{YYYY-MM}/pipeline_state.md` with a header:
```
# Pipeline State — {Company} — {YYYY-MM-DD}
Track: {track}
Input: applications/{Company}_{YYYY-MM}/input.md
```

### Step 2 — Parallel block (run all three simultaneously)

Execute all three stages at once — they do not depend on each other:

- **Stage 01**: Read and execute `pipeline/stages/01_company_researcher.md`
- **Stage 02**: Read and execute `pipeline/stages/02_jd_analyzer.md`  
- **Stage 03**: Read and execute `pipeline/stages/03_candidate_context.md`

Each appends its section to `pipeline_state.md`.

### Step 3 — Evidence matching

Execute `pipeline/stages/04_evidence_matcher.md`.  
Reads: pipeline_state.md §Stage 01, §Stage 02, §Stage 03.

### Step 4 — Positioning

Execute `pipeline/stages/05_positioning.md`.  
Reads: pipeline_state.md §Stage 04 + company context file.

**⚠ Human checkpoint**: Read `pipeline_state.md ## Stage 05 — Positioning Strategy`. If the primary hook or cover letter structure is wrong, edit Stage 05's output before continuing. Type "proceed" to continue.

### Step 5 — Draft

Execute `pipeline/stages/06_resume_writer.md`.  
Reads: pipeline_state.md §Stage 05 + evidence.md + facts.yaml + `versions/{track}/_base.md`.

### Step 6 — Parallel verification (run both simultaneously)

- **Stage 07**: Execute `pipeline/stages/07_factuality_checker.md`
- **Stage 08**: Execute `pipeline/stages/08_ats_reviewer.md`

Both append to `pipeline_state.md`.

**⚠ Gate**: If Stage 07 produces any FAIL items, stop. Do not proceed to Stage 09. Surface the FAILs to the human for resolution.

### Step 7 — Final edit

Execute `pipeline/stages/09_final_editor.md`.  
Reads: pipeline_state.md §Stage 07 + §Stage 08.

Stage 09 writes `Status: READY_FOR_STAGE_10` (not COMPLETE).

### Step 8 — Slop-free polish (terminal)

Execute `pipeline/stages/10_slop_free_polish.md`.  
Reads: Stage 09 outputs + voice.md (unified voice authority with context-aware Voice Matrix).

**⚠ Gate**: If Stage 10 logs any drift FAIL, stop. Revert the flagged edit and surface to the human.

When Stage 10 writes `Status: COMPLETE`, the pipeline is done.

---

## Outputs

```
versions/{track}/resume_{Company}.md     ← tailored resume
applications/{Company}_{YYYY-MM}/
  cover_letter.md                         ← cover letter
  pipeline_state.md                       ← full stage trace (keep for audit)
```

---

## Human checkpoints

| After stage | What to review | When to stop |
|---|---|---|
| Stage 05 | Primary hook, cover letter structure | If hook is generic or wrong angle |
| Stage 07 | Factuality audit FAILs | If any FAIL exists |
| Stage 09 | Final resume + cover letter | If pre-pass missed something (Stage 10 is authoritative) |
| Stage 10 | Slop polish log + drift check | If any drift FAIL, or voice was flattened |

---

## Shortcuts

**Re-run one stage only** (e.g., after editing positioning):
> Re-run Stage 06 using the current pipeline_state.md for `applications/{Company}_{YYYY-MM}/`.

**Re-run slop polish only** (e.g., after hand-editing the resume):
> Re-run Stage 10 using the current pipeline_state.md for `applications/{Company}_{YYYY-MM}/`.

**Skip company research** (company context file already exists and is fresh):
> Skip Stage 01 for this run — use existing `research/companies/{Company}.md`.

**Start from scratch for a company**:
> Delete `research/companies/{Company}.md` and re-run the full pipeline.

---

## Stage dependency graph

```
01 (company research) ─┐
02 (JD analysis)       ├─→ 04 (evidence match) → 05 (positioning) → 06 (writer)
03 (candidate context) ┘                                                  ↓
                                                               07 (factuality) ─┐
                                                               08 (ATS review)  ─┤→ 09 (final editor) → 10 (slop-free polish)
```

Stages 01+02+03 run in parallel.
Stages 07+08 run in parallel.

---

## Design decisions (do not re-litigate per run)

**Voice.md as single source of truth (Stage 10).** Unified tone authority:
- Loads `voice.md` directly (no external skill dependencies)
- Context-aware via Voice Matrix: auto-selects bullet formula based on track (startup/MNC/mid-level from Stage 05)
- Applies Core Principles (Simplicity, Clutter, Be Yourself) + Banned Words → Zinsser replacements
- Enforces Evidence Boundaries (hard constraints per project — never overclaim)
- Resume pass: strict hygiene, technical specificity preserved
- Cover letter pass: minimum effective edit, writer voice preserved, cap 300 words

Hard rule overriding all edits: no invented or altered facts — every edited line must still anchor in `data/facts.yaml` or `content/github/evidence.md`. Drift = FAIL, stop for human. Stage 09 keeps only a quick pre-pass; Stage 10 is the authoritative slop gate.

**Evidence-first bullets.** Stage 06 reads `content/github/evidence.md` BEFORE writing any bullet. Bullets derive from evidence technical depth (file names, algorithms, implementation details), not from the pre-written templates in `facts.yaml`. See [ADR note in archive/pipeline_old/PIPELINE_spec_v1.md] for the prior approach.
