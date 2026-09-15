# Memory — Durable Agent Lessons

Distilled, evidence-backed learnings. History stays in `content/handoffs/`; only lessons that change future behavior live here. Protocol: `AGENTS.md` → Learning loop.

## Validated lessons

1. **Evidence-first bullets.** Read `content/github/evidence.md` before `facts.yaml` templates when drafting — file paths, algorithms, and exact numbers invisible in the resume surface this way. (Evidence: Noise_Eng run, bullets 1–3 NEW/UPGRADED from evidence; `pipeline/run.md` design decision.)
2. **Downstream-adoption phrasing.** "Diagnosed X (Issue #N) → merged/adopted downstream in PR #M". Never claim authorship of maintainer-merged PRs; all 7 authored Omi PRs closed unmerged, 3 approved. (Evidence: `content/github/boundaries.md` truth-tested phrasing.)
3. **Backend verb.** Aura backend is Adapted/Integrated/Extended — never "architected from scratch" or "built the Omi backend". (Evidence: handoff `resume_iteration_2026-09-14.md`, binding decision.)
4. **Track formatting.** MNC is ASCII-only (no →); startup/midlevel may keep →. (Evidence: same handoff.)
5. **Stage 10 is terminal and split.** Resume → `stop-slop`, cover letter → `no-ai-slop`; never swap. Stage 09 keeps only a quick pre-pass. (Evidence: `pipeline/run.md`, stage 10 drift gate.)
6. **Structural convention.** Tailored outputs sit beside `versions/{track}/_base.md`; every run logs `applications/{Company}_{YYYY-MM}/` (input, pipeline_state, cover_letter); `archive/` is never referenced by the pipeline. (Evidence: handoff `refactor_2026-09-14.md`.)
7. **Page-limit trim order.** Startup Aura at 6 bullets is at the one-page limit; first trim candidate is the file-indexing clause. MNC Aura density (3+ line bullets) accepted for ATS coverage. (Evidence: iteration handoff WARNs.)
8. **LaTeX template runs.** When the user supplies a .tex template: adapt content into it (never ship dummy rows), compile with pdflatex, enforce 1 page, clean aux/log/out. Contact email/phone live in repo templates, not facts.yaml — confirm with user before use; drop unstored handles (LeetCode) and unanchored sections (Certifications) rather than inventing. (Evidence: Noise_Fullstack_2026-09 run, rezume.tex → 1-page PDF.)
9. **DONT.MD section convention.** Bare `§0–§9` = front-matter methodology/rules; `§E0–§E22` = engines (renamed 2026-09-15 to end collisions on §5/§6/§9). Cite with the prefix always. (Evidence: verified rename diff — 23 headers, zero content drift; backup `archive/DONT.MD.bak-pre-enumber-20260915`.)

## Changelog

- 2026-09-14: seeded from iteration + refactor handoffs (7 lessons, no rule changes).
