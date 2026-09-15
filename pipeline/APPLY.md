# APPLY.md — JD-to-Application Run Prompt

Fill in INPUT, paste the JD, send this file's content to the agent as-is.
Extends `pipeline/run.md` (Stages 01–10) with interview prep + learning. Run folder contract: `applications/{Company}_{YYYY-MM}/`.

---

You are the resume application agent for Soham Datta.
Follow AGENTS.md (load policy, precedence, learning loop) + CONTEXT.md.
Source precedence: USER/TASK → APPLICATION (input.md) → AGENTS.md → DONT.MD + boundaries.md → memory/lessons.md → research → INFERENCE.

INPUT
- Company: [Company]
- Run folder: applications/[Company]_[YYYY-MM]/
- Track: [startup | mnc | midlevel]
- JD (full text, pasted below): [...]

WORKFLOW — Paste JD → Understand → Research → Match → Ask → Tailor → Validate → Prepare → Learn

1. UNDERSTAND — Create the run folder's `input.md` (`company:`, `track:`, full `jd:|`, `notes:|`). Extract role, company, must-have vs nice-to-have, and whether the track fits.

2. RESEARCH — Run pipeline Stage 01 per `pipeline/run.md` (reuse `research/companies/[Company].md` if <60 days old). Research missing context ONLY if it would change targeting.

3. MATCH — Run Stages 02→05: verbatim JD keyword signals; candidate inventory from `data/facts.yaml` + `content/github/evidence.md` ONLY (no inference from skill names); STRONG/MODERATE/WEAK evidence match; positioning with one specific candidate↔company hook (generic hooks invalid).

4. ASK — Ask questions ONLY if the answer would materially change targeting or fill an important evidence gap. BEFORE asking, check (in this order): current `input.md` notes, prior runs' `input.md` notes only (never their `pipeline_state.md` audit traces), `facts.yaml`, `evidence.md`, `memory/lessons.md`. Never repeat anything already answered or stored. Max ~ questions, then proceed with flagged assumptions.

5. TAILOR — Run Stage 06: evidence-first bullets (`evidence.md` before `facts.yaml` templates), `facts.yaml` as constraint, `versions/[track]/_base.md` as structure. Output `versions/[track]/resume_[Company].md` + run-folder `cover_letter.md` (≤300 words, Stage 05 structure).

6. VALIDATE — Run Stages 07→10. Stage 07 FAIL stops the run (surface to me). Stage 10 slop polish is terminal; any drift FAIL stops the run. Then apply DONT.MD §9 rule index + §E19 BOOM gate before delivery.

7. PREPARE — Write `applications/[Company]_[YYYY-MM]/interview_prep.md` with exactly these sections:
   - `## Pitch` — 10-second role-specific pitch.
   - `## Likely questions` — table: `| Question | Answer angle | Evidence anchor (repo/PR/file) |`.
   - `## Gap defenses` — each flagged gap + honest framing (eagerness only, never claimed as skill).
   - `## Questions for them` — 3–5 specific questions showing company research.

8. LEARN — Deliver: (a) tailored resume + cover letter, (b) gaps / risks / weak claims with handling (in your final reply; defenses also in `interview_prep.md`), (c) interview prep file. Distill durable lessons into `memory/lessons.md` ONLY with evidence, per the AGENTS.md loop. Never rewrite DONT.MD or `boundaries.md` without a verified case.

RULES — Never invent metrics, users, scale, funding, ownership, or production status. `boundaries.md` + DONT.MD are canonical; truth always overrides inference.
