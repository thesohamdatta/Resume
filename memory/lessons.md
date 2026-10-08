# Memory — Durable Agent Lessons

Distilled, evidence-backed learnings. History stays in `archive/`; only lessons that change future behavior live here.

## Validated lessons

1. **Evidence-first bullets.** Read `content/github/evidence.md` before resume templates. Exact file paths, algorithms, and metrics should come from evidence.
2. **Downstream-adoption phrasing.** Use "Diagnosed X (Issue #N) → resolved/adopted downstream in PR #M". Never claim authorship of maintainer-merged downstream PRs. All 7 authored Omi PRs are closed unmerged; 3 were maintainer-approved.
3. **Backend verb.** Aura backend is adapted/integrated/extended. Never say it was architected from scratch or that the Omi backend was built from scratch.
4. **Mode formatting.** MNC should remain ASCII-safe where the template requires it. Startup/referral can use normal technical punctuation.
5. **Final validation is terminal.** Resume stop-slop and cover-letter no-AI-slop remain separate passes.
6. **Structural convention.** Tailored outputs sit beside `versions/{mode}/_base.md`; application runs stay under `applications/{Company}_{YYYY-MM}/`; `archive/` is historical only.
7. **One-page trim order.** Remove weak project bullets, redundant tool names, low-signal certifications, and older detail before shrinking typography.
8. **LaTeX template runs.** Adapt supplied templates, compile with pdflatex, enforce one page, and clean generated aux/log/out files. Contact details are template data and should not be invented.
9. **DONT.MD section convention.** Bare §0–§9 are front-matter methodology/rules; §E0–§E22 are engines.
10. **Active experience threshold.** Insufficiently substantial freelance work stays out of active professional history.
11. **Non-tech experience can be useful when specific.** Reliance and PES should use concrete responsibilities rather than generic labels.
12. **Research-role specificity.** Preserve both research/resource discovery and student-facing digital-learning support when relevant.
13. **Official-title rule.** Reliance must remain "Associate" in the master record and final resumes.
14. **Internship attribution rule.** The AI/ML internship is an AICTE program, not employment at Google. Represent the internship as "AICTE" only; do not name the platform provider.
15. **Aura status rule.** Aura remains an independent wearable AI project under development. No customer, funding, production, or unsupported performance claims.
16. **User-supplied template overrides the default renderer.** When the user explicitly says to use an attached template, render on that template. Do not substitute `templates/v3/` and do not produce two variants; deliver exactly one resume. (User correction, 2026-10-08.) Note `TLCresume.sty` needs `texlive-lang-cjk` for `CJKutf8.sty`; it compiles with XeLaTeX; `sections/*.tex` are unused by the master `resume.tex`.
17. **Non-technical JD lens.** For admin/ops/facilities JDs, foreground Reliance (customer ops, records, reporting), PES (3,000+ pages records/digitization), and Aura (independent project management). Omit deep technical stack detail and certifications. Real gaps (events budgeting, travel coordination, vendor liaison) stay omitted, not invented.
18. **MNC punctuation.** `resume-openfont.cls` renders `--` as an en dash; keep ASCII `--` in dates (matches the base and pipeline convention).
