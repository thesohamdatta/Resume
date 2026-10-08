# Handoff: Whole-Project Deep Iteration — 2026-09-14

Facts source remains `data/facts.yaml`. Live-verified this session: Omi 13.5k stars, Issue #12360 OPEN (6 user stories, zero-backend contract), PR #8919 Closed with 52 tests and maintainer approval, profile 62 repos / pinned aura, LLM-Council, I-am-Mia, skills.

## What changed
- `data/facts.yaml`: filled all TBD (mnc/midlevel for aura, mia, voice_ai, llm_council); startup Aura 4 → 6 bullets (added #8918 grounding, #8991/#12360 specs); mnc Aura condensed 5 → 4 bullets with "Adapted" backend language; midlevel Aura 4 → 5 bullets; boundaries extended with #8352, bot-closed issues, forks, draft #12927, live-verified note.
- `content/github/evidence.md`: added PR #7379/#7654/#8442/#8352 details, Issues #7628/#8452/#8453/#8912/#8985, Tier-2 repos (Sarvam, DDPM, Microgpt124M, codeshot file pointers).
- `content/github/boundaries.md`: CAN-claim extended (adapted backend, grounding, specs); CANNOT-claim extended (8352, bot-closed, forks, draft, 8442 unmerged).
- `versions/startup/resume_startup.md`: Aura 4 → 6 bullets (grounding + specs).
- `versions/mnc/_base.md`: Aura 5 → 4 bullets (hardware+firmware combined; adapted backend; diagnostics+grounding combined; specs+approved-PR note); arrows → ASCII "to".
- `versions/midlevel/_base.md`: Aura 4 → 5 bullets (firmware merged into bullet 1, adapted backend, grounding folded into diarization bullet, new specs bullet).

## Wording decisions (binding)
- Backend verb is "Adapted" (mnc/midlevel) / "Integrated" (startup). Never "architected from scratch" or "built the Omi backend".
- Omi phrasing: "merged downstream in #8902", "adopted downstream in #12471 / #12089", "delivered in #7896/#9595/#10236", "draft #12927 NOT merged".
- "Seeed" is the hardware vendor, not a funding claim. "user_name" is a code param, not a user-count claim. "fragile" contains "agi" as substring only.
- MNC keeps ASCII only (no →). Startup/midlevel may keep → (flexible tracks).

## Verification (Stages 07-10, base tracks, no cover letter)
- Stage 07 factuality: PASS with notes — every new claim anchors in facts.yaml/evidence.md; no VC/funding/customer/revenue/production/AGI claims; authored PRs never called merged; banned buzzwords absent (grep hits are substrings only).
- Stage 08 ATS: MNC headings standard, single-column markdown, no tables, contact line complete; bullet count now 4 for Aura (was 5). Startup "Featured Projects" allowed (flexible track). Midlevel 5 Aura bullets noted, acceptable off-ATS.
- Stage 09 pre-pass: no em-dashes in edited lines; no Wh-openers; no "not X but Y"; passive "merged/adopted downstream" retained per truth-tested phrasing.
- Stage 10 drift gate: CLEAR — edits mirror facts.yaml verbatim; no new numbers, repos, dates, or strengthened verbs.
- Known WARNs: MNC bullets 3-4 are dense (3+ lines rendered); accepted for ATS keyword coverage. Startup Aura at 6 bullets is at the one-page limit; next trim candidate is the file-indexing clause if overflow occurs.
