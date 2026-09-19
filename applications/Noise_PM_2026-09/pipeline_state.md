# Pipeline State — Noise PM — 2026-09-14
Track: startup
Input: applications/Noise_PM_2026-09/input.md

---

## Stage 01 — Company Research
SKIP — research/companies/Noise.md exists (updated 2026-09-14, fresh, under 60 days). Reused for this PM role; product and hiring context carries over.

---

## Stage 02 — JD Signals

### Required (explicit in JD — must have match)
- Write and refine PRDs, user stories, feature specs
- Market and competitor research (consumer tech / wearables / audio)
- Wireframes and prototypes in Figma, user-needs-grounded feedback
- Product and user data analysis using SQL; track feature performance
- Backlogs, sprint progress, schedules using Jira
- Gather and synthesize user feedback (app reviews, support tickets, surveys)
- Experimentation and A/B testing, hypothesis to results
- Presentations and reports for stakeholders
- Go-to-market planning for launches and rollouts

### Preferred (nice-to-have — include if honest match)
- Consumer tech / electronics interest
- Attention to detail
- Written and verbal communication (clear PRDs, confident presenting)
- Engineering / Business / Design degree (candidate: B.E. AI and ML, SPPU, 2022 – Jun 2026)
- Curious, self-driven, comfortable with ambiguity

### Role archetype
"builder-turned-PM generalist, wearable-adjacent, measurement-led"

### ATS keywords (verbatim from JD)
- PRD, Product Requirement Documents, user stories, feature specs
- market research, competitor research
- Figma, wireframes, prototypes
- SQL, data-backed decisions, feature performance
- Jira, backlogs, sprint
- user feedback, app reviews, support tickets, surveys
- A/B testing, experimentation, hypothesis
- presentations, reports, stakeholders
- go-to-market

### Deprioritize (in JD but low-signal for this candidate)
- None structural; tool gaps below are handled honestly, not hidden.

### Gaps flagged
| JD Requirement | Gap | How to handle |
|---|---|---|
| SQL | No SQL in evidence | Do not claim; JD allows eagerness — cover letter expresses it, resume shows adjacent data work (Python measurement, token tracking) |
| Figma | No Figma in evidence | Do not claim; Framer portfolio shows design-tool fluency; eagerness in cover letter |
| Jira / sprints | No Jira in evidence | Do not claim; RFC-plus-issue workflow is the honest analogue |
| A/B testing | No true A/B runs | Do not claim; show hypothesis-driven measurement instead |
| Go-to-market | No GTM work | Do not claim; 0-to-1 shipping mindset is the honest analogue |

---

## Stage 03 — Candidate Inventory

### Strongest evidence (verifiable — GitHub repo, file path, or named artifact exists)
| Project | Evidence | Type |
|---|---|---|
| Aura | 5 architectural RFCs in Omi (voice pipeline, virtual memory OS, haptics, context resumption, markdown export) — spec documents | Open Source |
| Aura/Omi | 21 authored issues incl. #8438 (GPU root cause: CSS backdrop-filter over WebGL) and #8029 (TTS cost/latency audit: 10k char cap, eleven_flash vs turbo, +50-100ms TLS) | Open Source |
| Aura | Offline agglomerative hierarchical clustering, SciPy cosine linkage, 52 unit tests (PR #8919, adopted downstream #12471) | Algorithm |
| Aura | End-to-end pendant: CAD enclosure, ESP32-S3 firmware (FreeRTOS I2S DMA 16kHz, Opus, OTA), FastAPI backend, self-hosted Deepgram Nova-3 ASR on Kubernetes Helm | Hardware |
| Mia | 5-stage harness (grill-spec-plan-review-ship), multi-host adapters, Vitest gates, JSONL state, ADR-0001 decision doc | Full-Stack |
| Voice AI | John: Kotlin Jetpack Compose Android app + Python LiveKit agent with tool calling | Mobile |
| Voice AI | voicecoder: multi-provider fallback with real-time token cost tracking | Full-Stack |
| LLM-Council | 4-provider concurrent eval, Analyst-Skeptic-Synthesizer pipeline, React agreement visualization | Full-Stack |
| AICTE-Google | TensorFlow + ML Kit on-device evals; transfer learning and augmentation for latency/accuracy tradeoffs | AI/ML |

### Secondary evidence (real but lighter)
| Project | Evidence | Type |
|---|---|---|
| Portfolio | sohamdatta.framer.ai portfolio + Human-AI Interaction Design practice | Full-Stack |
| Aura backend | Supabase/pgvector migrations for vector memory | Full-Stack |
| codeshot | Moondream VLM code extraction (suppressed for this role — low relevance) | AI/ML |

### Hard boundaries (NEVER claim — from boundaries.md)
- No VC/funding/customers/revenue/traction for Aura; no production claims for personal projects
- Omi: 7 authored PRs closed unmerged; downstream merges (#8902, #12471) are not authorship — use truth-tested phrasing only
- No AGI near Mia; no fabricated metrics; no banned buzzwords
- Aura backend: integrated/adapted/extended, never architected-from-scratch
- Do not claim SQL, Figma, Jira, A/B testing, or GTM (confirmed gaps)

### Track-specific notes
Startup track, one page. PM framing foregrounds RFCs, issues, and measurement. Reliance + PES collapse to one line. codeshot suppressed.

---

## Stage 04 — Evidence Match

### High-signal matches (JD requirement ↔ verifiable evidence)
| JD Requirement | Evidence item | Strength | Evidence type |
|---|---|---|---|
| PRDs / specs | 5 architectural RFCs (voice pipeline, virtual memory OS, haptics, context resumption, markdown export) | STRONG | Open Source |
| Competitor research | TTS vendor audit with cost and latency numbers (#8029) | STRONG | Voice AI |
| Consumer tech interest | Built wearable pendant end to end in the exact category Noise sells | STRONG | Hardware |
| User feedback synthesis | 21 authored issues with root-cause diagnoses | STRONG | Open Source |
| Data-backed decisions | Latency/accuracy evals (AICTE), token cost tracking (voicecoder), TTS measurements | STRONG | AI/ML |
| Presentations / reports | RFCs plus ADR-0001 decision documentation | STRONG | Full-Stack |
| Work with design + engineering | Solo 0-to-1 across CAD, firmware, backend, cloud; Framer portfolio | STRONG | Hardware |

### Moderate matches (real but less specific to JD phrasing)
| JD Requirement | Evidence item | Strength |
|---|---|---|
| Wireframes / prototypes | Framer portfolio and interaction-design practice (Figma itself not evidenced) | MODERATE (partial) |
| Experimentation | Hypothesis-driven measurement and iteration; no true A/B runs | MODERATE (partial) |

### Confirmed gaps
| JD Requirement | Gap status | Interview framing |
|---|---|---|
| SQL | Not evidenced; JD allows eagerness | Adjacent data work in Python; fastest-learning-curve claim only in cover letter, never as skill |
| Figma | Not evidenced | Framer fluency transfers; eagerness only |
| Jira / backlog / sprint | Not evidenced | RFC-plus-issue workflow as honest analogue |
| Go-to-market | Not evidenced | 0-to-1 shipping mindset as honest analogue |

### Evidence to suppress (real but low-relevance to this role)
- Reliance Associate and PES Research Assistant as named roles (one summary line)
- codeshot detail
- Omi PR-number deep cuts beyond #8438/#8919 truth-tested phrasings
- Kubernetes Helm beyond one mention

---

## Stage 05 — Positioning Strategy

### Primary hook
Built a wearable AI pendant from CAD to cloud — writing the RFC-style specs and user-issue diagnoses a Noise PM writes daily — now applying that builder lens to products used by millions.

### Secondary angles (2–3 max)
- Measurement-led: cost/latency audits, eval tradeoffs, and feature-usage tracking (token costs) as data-backed-decision proof
- Design-adjacent engineer: Framer portfolio plus interaction-design practice; honest eagerness on Figma

### Track confirmed
startup — one page, minimal; no override.

### Headline for this role
AI Engineering Graduate · Wearable Systems Builder

### Cover letter structure
1. Opening: hook — Aura pendant in Noise's exact category, ≤2 sentences
2. Body 1: spec plus user-feedback evidence (RFCs, 21 issues, TTS audit)
3. Body 2: data breadth (evals, token tracking) plus honest eagerness on SQL/Figma/Jira
4. Close: direct ask, ≤1 sentence

### What to cut from base resume
- Reliance + PES as named roles — one summary line (low signal for PM)
- LLM-Council to one bullet; Mia to one bullet (room for RFC/issue evidence)
- Omi PR numbers beyond #8438/#8919 phrasings

### What to foreground (from evidence — not currently in base resume)
- 5 architectural RFCs by topic; 21 authored issues
- TTS audit numbers (10k cap, flash-vs-turbo, +50-100ms)
- voicecoder token cost tracking as feature-performance tracking
- Framer portfolio as design-tool fluency

---

## Stage 06 — Writer Notes
Evidence-first bullets applied (PM framing):
- Aura bullet 1: CAD enclosure plus FreeRTOS/I2S DMA/Opus/OTA from evidence.md firmware section; FastAPI routers plus cloud memory capture from facts.yaml plus evidence backend section
- Aura bullet 2: 5 RFC topics plus 21-issue count from evidence.md Omi metrics table; root-cause framing from #8438/#8029 sections
- Aura bullet 3: TTS audit numbers (10k cap, flash-vs-turbo, +50-100ms) from #8029; clustering plus 52 tests from #8919; Nova-3 Helm from infra section
- Aura bullet 4: GPU diagnosis phrasing kept to truth-tested form (Issue #8438, merged downstream PR #8902)
- AICTE bullet reframed as latency-vs-accuracy experimentation (PM data signal), facts.yaml-anchored
- John foregrounded in Projects (companion-app angle); voicecoder token tracking kept as feature-performance tracking
- Flagged for Stage 07: cover phrases "daily" and "prototype in Framer" (precision check)

---

## Stage 07 — Factuality Audit
| Claim | Source | Status | Action |
|---|---|---|---|
| CAD enclosure, ESP32-S3 firmware stack, FastAPI backend, cloud capture | facts.yaml aura + evidence.md firmware/backend | PASS | keep |
| 5 RFCs by topic, 21 issues | evidence.md Omi metrics table | PASS | keep |
| TTS audit numbers, 52 tests, #8919/#12471, #8438/#8902 phrasings | evidence.md + boundaries.md truth-tested forms | PASS | keep |
| "analyze data in Python daily" | frequency unverified | WARN | softened to "analyze data in Python" |
| "prototype in Framer" | portfolio built in Framer; prototyping verb imprecise | WARN | changed to "built my portfolio in Framer" |
| SQL/Figma/Jira gaps stated as gaps | confirmed absent from evidence (true negative) | PASS | keep |
Result: CLEAR after WARN resolution. No FAILs. No banned buzzwords. No invented metrics.

---

## Stage 08 — ATS Review

### Keyword coverage
| Keyword | Present | Suggested addition |
|---|---|---|
| feature specs | yes (RFC parenthetical) | — |
| reports, experiments, prototypes/prototyping | yes | — |
| PRD, user stories | partial (RFC equivalence, honestly adjacent — not claimed) | none truthful |
| SQL, Figma, Jira, sprint, backlogs | absent (honest gaps) | none truthful |
| A/B testing, go-to-market, presentations, stakeholders | absent/partial | none truthful |
| market/competitor research, wireframes | partial (vendor audit; Framer) | none truthful |

### Issues
- None blocking. Single column, standard headings, no tables/columns/graphics, hyperlinked URLs.

### Suggestions
- Keep gaps visible via honest cover-letter framing (done).

### Verdict: PASS

---

## Stage 09 — Final Editor Log
WARNs resolved: 2 ("daily" frequency, "prototype in Framer" precision)
ATS fixes applied: "feature specs" equivalence added to RFC bullet; "rapid prototyping" added to skills (facts-tag anchored)
Stop-slop removals (pre-pass): "directly" cut; "concurrently" restructured out; em-dash removed from RFC bullet
Final word count (cover letter): ~200 words (cap 300)
Hook check: primary hook opens cover paragraph 1. Headline check: matches Stage 05.
Status: READY_FOR_STAGE_10

---

## Stage 10 — Slop-Free Polish (/unslop: no-ai-slop Edit + stop-slop strict)
Detect hits (no-ai-slop patterns, quoted lines):
- Em dash as rhythm crutch | "issue trackers — I will close those three tool gaps" | split into two sentences (FIXED)
- Adverb "directly" delaying the point | "learned its tradeoffs directly" | cut verb (FIXED in Stage 09)
- Adverb "concurrently" | "querying ... concurrently to cross-evaluate" | restructured to "cross-evaluates answers from" (FIXED in Stage 09)
- No binary contrasts, throat-clearing openers, faux-insight setups, colon reveals, importance puffery, weasel attribution, rhetorical setups, kicker lines, or recap endings found. No banned-outright words found.
- Kept deliberately (voice): "dress it up", "builder lens", "the hard way" cut already — human phrasing preserved per minimum-effective-edit rule.
Resume edits (stop-slop): 3 (feature-specs parens, rapid prototyping skill, concurrent restructure) plus zero-em-dash verification across all bullets.
Cover edits (no-ai-slop): What changed — cut "directly" and the em dash; softened two precision WARNs; everything else left intact as written.
Eval self-check: PASS — point preserved, no new claims, voice intact, active voice, concrete specifics, ends on concrete ask, full draft plus What-changed present (this log). Checks run twice (post-09, post-10).
Drift check: CLEAR — em-dash split and adverb cuts alter no facts; all lines still anchor in facts.yaml/evidence.md.
Status: COMPLETE

---

Outputs:
- versions/startup/resume_Noise_PM.md
- applications/Noise_PM_2026-09/cover_letter.md

---

## Research backfill (2026-09-14) — dossier deep dive + live verification
Sources: archive/github_context.md, archive/omi_github_evidence_report.md, archive/GITHUB_RESEARCH_REPORT_SOHAM_DATTA.md, plus live GitHub spot-checks of Issue #12360 and PR #12927.
Live-verified: #12360 OPEN by @thesohamdatta (Aug 28, 2026) with problem statement, 6 user stories, formatting contract, client-side architecture, test invariants, out-of-scope section; PR #12927 Draft by @Donovoi explicitly following the #12360 template exactly (maintainer review confirms match; needs-maintainer-review, NOT merged); Omi repo at 13.5k stars / 2.4k forks.
evidence.md enriched: downstream PR numbers in metrics table; new subsections #8918, #12360, #8991; dossier-boundaries note (#12927 draft, bot-closed #7525/#7546/#7878, #8352 changes-requested, forks); file pointers for Mia (registry.ts, skill executors), John (MainActivity.kt, tools/), voicecoder (costTracker.ts), LLM-Council (council.py, prompts, Stage1-3.jsx).

---

## Stage 07 re-audit (iteration claims)
| Claim | Source | Status |
|---|---|---|
| RFCs with user stories | #12360 User Stories section (live-verified, 6 stories) | PASS |
| 13.5k-star repo | Live repo header, verified 2026-09-14 | PASS |
| #12360 built out (Electron draft, Flutter patch) | #12927 draft + maintainer review (live) + dossier Flutter patch; no merge claimed | PASS |
| Speaker-attribution adopted downstream (#12089) | Dossier traceability matrix | PASS |
| 3 of 7 PRs maintainer-approved (closed unmerged) | evidence.md metrics + facts.yaml boundaries | PASS |
| Flash-vs-turbo 2x gap | Dossier #8029 audit (~150ms vs ~75ms) | PASS |
| Skills (21 reports, 5 adopted downstream) | evidence.md metrics table | PASS |
| Cover spec-shipped sentence | Same sources as above; ~225 words total | PASS |
Result: CLEAR. No FAILs. Helm clause dropped per suppress guidance — no impact.

---

## Stage 08 delta (iteration)
- "user stories" now present verbatim (was partial). PRD remains honestly adjacent via RFC equivalence. All other keywords/gaps unchanged.
### Verdict: PASS (unchanged)

---

## Stage 09 delta (iteration)
- Applied: bullets 2-4 rewrite, skills downstream count, cover spec-shipped sentence.
- Pre-pass: no new adverbs, no em dashes in resume, hook/headline intact.

---

## Stage 10 re-polish (/unslop on changed lines)
Detect hits:
- Em dashes in new cover sentence | "specs — the markdown-export proposal ... — were built out" | rewritten with commas (FIXED)
- Colon label "Specs that shipped through others:" | label use, uppercase continuation, concrete items follow | kept per Skill B colon rule (labels allowed)
- No banned words, contrasts, throat-clearing, puffery, or weasel attribution in new lines.
Eval self-check: PASS. Drift check: CLEAR — zero fact changes, only precision upgrades from listed sources.
Status: COMPLETE
