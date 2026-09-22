# Resume Pipeline — Run

Given `applications/{Company}_{YYYY-MM}/input.md`, run all 10 stages to produce:
- `versions/{local|mnc}/resume_{Company}.md`
- `applications/{Company}_{YYYY-MM}/cover_letter.md`

## Step 1 — Read input

Extract:
- `company:`
- `track:` MUST be `local` or `mnc`
- `jd:`
- `notes:`

Initialize application state with the selected track.

## Step 2 — Parallel research

Run Stages 01, 02, and 03 in parallel.

## Step 3 — Evidence matching

Run Stage 04.

## Step 4 — Positioning gate

Run Stage 05.

Stage 05 MUST determine:
- Primary Technical Domain
- Output Depth (D1/D2/D3)
- Evidence mix
- Foreground / compress / omit decisions
- Material questions

**Do not enter Stage 06 while a material question is unresolved.**

## Step 5 — Draft

Run Stage 06 using:
- Stage 05 positioning
- `content/github/evidence.md` first
- `data/facts.yaml` as factual constraint
- `versions/{local|mnc}/_base.md` as structural contract

The writer MUST preserve this section order:

Header / Contact → Summary → Experience → Projects → Education → Technical Skills → Certifications when verified.

Use adaptive depth rather than a universal technical-detail level.

## Step 6 — Parallel verification

Run Stage 07 and Stage 08.

Any Stage 07 FAIL stops the pipeline.

## Step 7 — Final edit

Run Stage 09.

## Step 8 — Slop-free polish

Run Stage 10.

Any drift FAIL stops the pipeline. COMPLETE is reached only after the final gate passes.

## Outputs

```
versions/{local|mnc}/resume_{Company}.md
applications/{Company}_{YYYY-MM}/
  cover_letter.md
  pipeline_state.md
  interview_prep.md
```

## Design decisions

- Local and MNC are the only active tracks.
- The section order is shared by both tracks.
- Primary Technical Domain is selected per application.
- Technical depth is adaptive per application.
- Evidence is typed and preserved in the evidence layer.
- No new track may be introduced without an explicit repository-level decision.
- Legacy startup/midlevel material is not an input for new applications.

Evidence-first writing remains mandatory. No claim without an anchor in `facts.yaml` or `content/github/evidence.md`.
