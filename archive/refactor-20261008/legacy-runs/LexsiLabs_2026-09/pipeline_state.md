# Pipeline State — Lexsi Labs AI Agent Intern — 2026-09-14
Track: startup
Input: applications/LexsiLabs_2026-09/input.md

## Stage 01 — Company Research: COMPLETE (fresh dossier)
New company; dossier `research/companies/LexsiLabs.md` created 2026-09-14 from lexsi.ai,
GitHub Lexsi-Labs, HuggingFace Lexsi org, arXiv-linked papers, LinkedIn. No 60-day reuse
applies. Confidence: product HIGH, tech signals MEDIUM, culture MEDIUM.

## Stage 02 — JD Analyzer (verbatim signals)
Three tracks: (1) Applied — enterprise workflow agents, tools/data, multi-step, HITL,
prototype→production; (2) R&D + Eval — harness design, eval frameworks, failure modes,
benchmarks, papers; (3) Product/Tooling — AlignTune Agent, AI-Scientist agents, debugging
tools. Requirements: strong Python, hands-on LLMs, interest in agents/eval/alignment/
interpretability/enterprise AI, ambiguity comfort, fast prototyping, paper reading, clear
docs, independent direction. Bonus: agent frameworks, long-horizon agents, eval pipelines,
research, OSS, backend, enterprise data, safety/interpretability. Culture: substance over
polish. Track fit: startup — frontier lab, OSS-first, prototype-to-artifact.

## Stage 03 — Candidate Context (facts.yaml + evidence.md ONLY)
Mia (TS/Bun 5-stage harness, Vitest gates, ADR-0001); LLM-Council (React+FastAPI,
4-provider critique pipeline, agreement viz); John (Kotlin/Compose + LiveKit, tool
calling); voicecoder (multi-provider fallback, cost tracking); I-am-Mia (voice agent);
Aura (wearable system, Omi OSS: 21 issues, 5 adopted, 3/7 approved); AICTE-Google

## Stage 04 — Evidence Match
| JD signal | Evidence | Strength |
|---|---|---|
| Harness design, eval gates | Mia: grill→spec→plan→review→ship, lint/typecheck/Vitest gates | STRONG |
| Evaluation systems, benchmarks | LLM-Council: Analyst→Skeptic→Synthesizer + agreement viz | STRONG |
| Agents over tools/data, multi-step | John: tool calling calendar/tasks/telephony; voicecoder fallback | STRONG |
| Research reading/writing | RFCs, ADR-0001, 21 issue reports with root causes | MODERATE |
| OSS tools | Omi contributions record | STRONG |
| Python backend | FastAPI routers, asyncio (Aura, LLM-Council) | STRONG |
| Alignment/interpretability theory | None in profile | GAP — eval-adjacent interest only |
| Enterprise/tabular data | None in profile | GAP — do not claim |

## Stage 05 — Positioning Strategy (HUMAN CHECKPOINT)
Primary hook: built an AI engineering harness with automated verification gates (Mia) →
Lexsi builds harnesses and eval systems (AlignTune, XAI Evals, red-teaming). One specific
candidate↔company hook: grill→spec→plan→review→ship with Vitest gates maps to their
Agent R&D track (harness design + evaluation infrastructure).
Second: LLM-Council multi-model evaluation → their evaluation-systems work.
Third: applied agents (John, voicecoder) → Applied track; Omi OSS → open-source culture.
Headline: AI Engineer · Agent Systems · Evaluation (startup track).
Cover structure: (1) Lexsi's harness/eval OSS (AlignTune, XAI Evals) + Mia overlap;
(2) proof trio LLM-Council/applied agents/Omi; (3) honest gaps (alignment theory,
enterprise data) framed as adjacent interest, eagerness only; (4) close remote part-time.
Cuts: Reliance/PES one-liners; Aura condensed (wearables off-theme, keep OSS + breadth).

Status: AWAITING HUMAN — answer the questions below to continue to Stage 06.

## Stage 05 answers (user, same day)
Track emphasis: R&D + Eval first. Positioning: PROCEED.

## Stage 06 — Writer Notes
Evidence-first; Mia leads (harness + gates), LLM-Council second (eval), Voice AI third
(applied), Aura condensed to 3 (system breadth + OSS record + RFCs). Flagged for Stage 07:
softened "blocking every stage transition" → facts-verbatim gates; cut "measuring failure
modes" (unverified); cut "disagreement surfaced not averaged" (interpretive); carried
"streaming output per provider" from passed Noise run. Cover follows Stage 05 structure,
AlignTune/XAI Evals descriptions anchored in dossier sources; gaps stated plainly.
Outputs: versions/startup/resume_LexsiLabs.md + cover_letter.md.

## Stage 07 — Factuality: PASS, zero FAILs
All claims anchored (facts.yaml/evidence.md/dossier); Omi downstream phrasing kept;
"final year" enrollment claim cut → "fits around my SPPU schedule"; no invented
metrics/users/scale; no alignment-theory, tabular-data, or enterprise claims.

## Stage 08 — ATS: PASS
Standard single-column md, conventional headings, repo links inline. Startup track.

## Stage 09 — Final Editor: READY_FOR_STAGE_10
Pre-pass trims applied in Stage 06 edits. No meaning changes pending.

## Stage 10 — Slop Polish (terminal): COMPLETE, no drift
Skill A on resume: no banned words, no passive voice, specifics kept. "Harness"
reviewed and KEPT — literal domain term mirrored from Lexsi's own JD (their track is
named harness design), not metaphorical verb use. Skill B Detect on cover: no named
patterns; voice preserved; gaps stated without puffery. Drift gate: no fact/number/
repo/link altered.

Status: COMPLETE.

## v3 render (2026-09-14, user-requested)
Rendered resume_LexsiLabs.md into templates/v3 (resume-openfont) as v3/resume_LexsiLabs.tex
+ 1-page PDF via xelatex (fontspec requires XeLaTeX, not pdflatex). Support files copied
from template (cls/sty/fonts); fontawesome.sty stubbed locally (MiKTeX font missing —
provides \faExternalLink as arrow only). No-ai-slop pass: same verified claims, tense
normalized to present for current roles, no banned words/patterns. Template pristine.
## v3 binary dedup (2026-09-15): run-folder fonts/ copy (1.2MB) deleted; lato/raleway .sty repointed to shared `templates/v3/fonts/` (absolute path); recompiled 1-page PDF verified (text extracts clean). Project headings use `|` separators; header links de-underlined (href kept).
## Hygiene 2026-09-15 (repo-scan method): removed stale `v3/Soham Datta.pdf` (content-identical dup of `resume_LexsiLabs.pdf`, hashes differed on build metadata only); build artifacts clean (no aux/log/out); archive 1.17MB intentional store.
