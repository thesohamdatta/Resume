<!-- run.md — Pipeline Entry Point: reads input.md and chains all 10 stages -->

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

Initialize the application state with the selected track.

## Step 2 — Parallel research

Run Stages 01, 02, and 03 in parallel.

## Step 3 — Evidence matching

Run Stage 04.

## Step 4 — Positioning

Run Stage 05.

Positioning may change emphasis, but never the resume's factual history.

## Step 5 — Draft

Run Stage 06 using:
- Stage 05 positioning
- `content/github/evidence.md` first
- `data/facts.yaml` as factual constraint
- `versions/{local|mnc}/_base.md` as the structural contract

The writer MUST preserve this section order:

```
Header / Contact
Summary
Experience
Projects
Education
Technical Skills
Certifications (only when verified)
```

For local applications, use slightly more product/project context and less ATS keyword density.

For MNC applications, use conventional headings, single-column ATS-safe structure, searchable text, and concise technical bullets.

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
- The base file defines presentation structure; evidence defines technical truth.
- No new track may be introduced without an explicit repository-level decision.
- Legacy startup/midlevel material is not an input for new applications.

Evidence-first writing remains mandatory. No claim without an anchor in `facts.yaml` or `content/github/evidence.md`.
