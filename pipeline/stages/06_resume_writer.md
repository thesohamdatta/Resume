<!-- Stage 06: Resume Writer — Read by pipeline/run.md -->
# STAGE 06: RESUME WRITER INSTRUCTIONS

This is the most important stage. Evidence-first bullet writing.

Reads:
1. pipeline_state.md ## Stage 04 — Evidence Match (which evidence items are matched)
2. pipeline_state.md ## Stage 05 — Positioning Strategy (what to foreground, what to cut, headline, cover letter structure)
3. content/github/evidence.md (DEEP technical detail — read this first before writing any bullet)
4. data/facts.yaml (truth-tested templates and hard facts — use as constraint, not as bullet source)
5. versions/{track}/_base.md (base resume structure to modify)

Produces:
- versions/{track}/resume_{Company}.md
- applications/{Company}_{date}/cover_letter.md
- pipeline_state.md → section ## Stage 06 — Writer Notes (decisions made, things flagged for Stage 07)

The prompt should instruct:

STEP 1 — Evidence lookup (before writing anything):
For each matched evidence item in Stage 04, go to evidence.md and extract the SPECIFIC technical details:
- Function names, file paths, data structures (e.g. firmware/src/mic.cpp, I2S DMA circular buffer)
- Algorithms at the specific level (not "clustering" — "agglomerative hierarchical clustering (SciPy cosine linkage)")
- Exact numbers from evidence (52 unit tests, 120+ tests, 16 kHz)
- Specific tools at the version/API level (FreeRTOS, Opus compression, Deepgram Nova-3, pgvector)

STEP 2 — Bullet writing rules:
- Start from the evidence detail, work backward to the bullet
- Every bullet must have: WHAT was built + WHAT technology specifically + WHY it matters or WHAT it does
- Max 2 lines per bullet
- No passive voice. No "was built" — "built"
- Language: DONT.MD §E12 (anti-slop) + boundaries.md banned list — no buzzwords
- Voice: load `D:\download\voice\voice.md` as tone authority
  - Core Principles: Simplicity (strip to cleanest), Clutter (cut 50%), Be Yourself (builder identity)
  - Banned Words: zero tolerance — auto-replace with Zinsser table (voice.md §Banned Words → Zinsser Replacements)
  - Evidence Boundaries: hard constraints per project (voice.md §Evidence Boundaries table) — never overclaim
  - Facts/skills still come ONLY from evidence.md + facts.yaml — voice.md example blocks are illustrative, never claim sources
- Metrics: DONT.MD §5 metric rule — never invent numbers, users, scale, or production status
- Cap bullets per role: 3-4 max

STEP 3 — Cover letter rules:
- Follow the structure from Stage 05 Positioning Strategy exactly
- 4 paragraphs max
- Opening paragraph: name the specific company product + the candidate's specific overlap
- Never open with "I am writing to apply" or "I am excited to"
- Read aloud mentally — if any sentence sounds like AI wrote it, rewrite it
- Length: ≤300 words total

STEP 4 — Writer Notes for Stage 07:
- List every claim that came from evidence.md (not facts.yaml templates) so Stage 07 can verify them
- Flag anything that felt like a stretch

Hard rules (non-negotiable):
1. No bullet may appear in the resume if it has no anchor in facts.yaml OR evidence.md
2. Enforce content/github/boundaries.md in full — audit checklist, truth-tested phrasing, backend-verb and Omi-attribution constraints (never restated here; that file is canonical)
3. Final gate: DONT.MD §E19 HARD GATE before producing outputs
