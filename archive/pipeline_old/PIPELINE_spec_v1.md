# Resume Application Workflow — Specification v1.0

> **Single entry point:** provide `{company}`, `{JD}`, `{track}`, `{notes}` → receive tailored resume + cover letter, both verified against `facts.yaml`.

---

## 1. File Architecture

```
resume/
├── data/
│   └── facts.yaml                   # canonical source of truth (dates, bullets, links, boundaries)
├── content/
│   ├── github/
│   │   ├── evidence.md              # verifiable technical proof per project
│   │   └── boundaries.md           # what NOT to claim, per project
│   └── handoffs/
│       └── resume_handoff.md        # session-to-session context
├── research/
│   └── companies/
│       ├── _template.md             # blank company context file
│       ├── Noise.md                 # ← pre-built
│       ├── Chrysal.md               # etc.
│       └── {Company}.md            # created by Stage 1 on first run
├── versions/
│   ├── startup/
│   │   ├── resume_startup.md        # base startup resume
│   │   └── resume_{Company}.md     # tailored output
│   ├── mnc/
│   │   └── resume_{Company}.md
│   └── midlevel/
│       └── resume_{Company}.md
└── applications/
    └── {Company}_{YYYY-MM}/
        ├── input.md                 # JD + track + notes (your only input)
        ├── pipeline_state.md        # stage outputs chained here
        └── cover_letter.md          # final cover letter output
```

**Naming conventions:**
- Company files: `PascalCase.md` — e.g., `Noise.md`, `NeoSapien.md`, `SamsungResearch.md`
- Resume outputs: `resume_{Company}.md` — e.g., `resume_Noise.md`
- Application folders: `{Company}_{YYYY-MM}` — e.g., `Noise_2026-09`
- Tracks: `startup` | `mnc` | `midlevel`

---

## 2. Your Input (Per Application)

Create `applications/{Company}_{YYYY-MM}/input.md`:

```markdown
# Application Input

company: Noise
track: startup
jd: |
  [paste full JD text here]
notes: |
  [optional: special framing, things to emphasize, things to avoid]
```

That is the **only file you create**. The pipeline reads everything else.

---

## 3. Pipeline Overview

```
Stage 1: Company Researcher        ─┐
Stage 2: JD Analyzer               ─┤→ (parallel) → Stage 4: Evidence Matcher
Stage 3: Candidate Context Reader  ─┘
                                       ↓
                               Stage 5: Positioning Strategist
                                       ↓
                               Stage 6: Resume Writer
                                       ↓
Stage 7: Factuality Checker       ─┐
Stage 8: ATS/Readability Reviewer ─┘→ (parallel) → Stage 9: Final Editor
```

**Parallelizable:** Stages 1+2+3 run simultaneously. Stages 7+8 run simultaneously.  
**Sequential gates:** Stage 4 waits for 1+2+3. Stage 6 waits for 5. Stage 9 waits for 7+8.

---

## 4. Stage Definitions

---

### Stage 1 — Company Researcher

**Trigger:** First application to this company, or `research/companies/{Company}.md` is stale (>60 days).  
**Skip if:** `{Company}.md` exists and is fresh — pass it directly to Stage 4.

**Reads:**
- Official website, careers page, product pages
- LinkedIn company page
- Credible secondary sources (Reddit, X, news) where available
- The JD from `input.md` (for industry signal)

**Produces:** `research/companies/{Company}.md`

```markdown
# {Company} — Context Layer

## What they make
[products, SKUs, technology stack — hardware/software split]

## Business direction
[growth stage, funding, strategic bets, recent announcements]

## Technology signals
[languages, frameworks, infra, AI/ML tooling used or sought]

## Culture & hiring patterns
[what they say about culture, what their JDs cluster around]

## Relevant to this role
[specific signals that map to the candidate's profile]

## Sources
[URLs, dates]

## Confidence
[HIGH / MEDIUM / LOW per claim — flag anything assumed]
```

**Rules:**
- Every claim needs a source or `[unverified]` tag.
- Flag speculative inferences explicitly.
- Keep the file ≤ 400 words. More is not better.

---

### Stage 2 — JD Analyzer

**Reads:** `input.md` JD text only.

**Produces:** `pipeline_state.md` → section `## JD Signals`

```markdown
## JD Signals

### Required (must appear in resume)
- [explicit requirement 1]
- [explicit requirement 2]

### Preferred (include if honest match exists)
- [preferred skill 1]

### Role archetype
[e.g., "AI-first generalist", "mobile + AI", "hardware-adjacent software"]

### Keywords for ATS (verbatim from JD)
- [keyword 1]
- [keyword 2]

### What this role is NOT asking for
[signals to deprioritize or omit]

### Red flags / traps
[e.g., "asks for Flutter — candidate has none; mark as gap"]
```

---

### Stage 3 — Candidate Context Reader

**Reads:** `data/facts.yaml`, `content/github/evidence.md`, `content/github/boundaries.md`

**Produces:** `pipeline_state.md` → section `## Candidate Inventory`

```markdown
## Candidate Inventory

### Strongest evidence (verifiable, project-linked)
- [evidence item with project tag]

### Secondary evidence (real but less prominent)
- [evidence item]

### Honest gaps relative to this role
- [gap]: [honest framing if asked]

### Hard boundaries (never claim)
- [from boundaries.md]
```

**Rules:**
- Only list what is in `facts.yaml` or `evidence.md`.
- Do not infer capabilities from tool names alone.

---

### Stage 4 — Evidence Matcher

**Reads:** `## JD Signals` + `## Candidate Inventory` from `pipeline_state.md`

**Produces:** `pipeline_state.md` → section `## Evidence Match`

```markdown
## Evidence Match

### High-signal matches (JD requirement ↔ verifiable evidence)
| JD Requirement | Evidence | Strength |
|---|---|---|
| Real-time voice AI | LiveKit WebRTC + Silero VAD (John, I-am-Mia) | STRONG |
| Android development | Kotlin/Jetpack Compose (John) | STRONG |
| Wearable hardware | Aura ESP32-S3 enclosure | STRONG |
| Full-stack | React + FastAPI (LLM-Council) | MODERATE |

### Honest gaps
| JD Requirement | Gap | How to handle |
|---|---|---|
| Flutter/iOS | None in profile | Acknowledge if asked; do not claim |
| Docker/CI/CD | Not prominent | Omit; mention conceptual familiarity only if asked |

### Deprioritize (in JD but poor match or low signal)
- [item]
```

**Decision rule:** A match is STRONG only if there is a GitHub repo, measurable output, or named artifact behind it. A tool name alone in `skills` is WEAK and should not be matched as evidence.

---

### Stage 5 — Positioning Strategist

**Reads:** `## Evidence Match` + `{Company}.md`

**Produces:** `pipeline_state.md` → section `## Positioning Strategy`

```markdown
## Positioning Strategy

### Primary hook (opens resume headline and cover letter)
[one sentence — the single strongest, most specific match]

### Secondary angles (supporting story)
- [angle 2]
- [angle 3]

### Track selection: {startup | mnc | midlevel}
[confirm or override with rationale]

### Cover letter structure
1. [opening — hook, specific to company]
2. [body 1 — strongest project evidence]
3. [body 2 — software breadth]
4. [close — ask]

### What to cut from base resume
[sections or bullets to drop for relevance; always: Reliance, PES if space is tight]

### Headline variant for this role
[e.g., "AI Engineer · Wearable Systems · Full-Stack"]
```

---

### Stage 6 — Resume Writer

**Reads:** Base resume (`versions/{track}/resume_{track}.md`) + `## Positioning Strategy` + `## Evidence Match` + `facts.yaml`

**Produces:**
- `versions/{track}/resume_{Company}.md`
- `applications/{Company}_{YYYY-MM}/cover_letter.md`

**Rules (hard):**
- Every bullet must exist in `facts.yaml` or `evidence.md`. No new claims.
- No buzzwords: passionate, innovative, cutting-edge, leveraged, spearheaded, transformative, next-generation.
- No invented metrics, users, scale, funding, or status.
- Cover letter: 4 paragraphs max. Hook → Project proof → Software breadth → Ask.
- Resume: one page. Bullets 1–2 lines. No padding.
- Natural voice: concrete verbs (built, designed, integrated, diagnosed, authored). No passive voice.

---

### Stage 7 — Factuality Checker

**Reads:** `resume_{Company}.md` + `cover_letter.md` + `facts.yaml` + `boundaries.md`

**Produces:** `pipeline_state.md` → section `## Factuality Audit`

Check every claim against these rules:

```
PASS if: claim exists verbatim or by clear implication in facts.yaml or evidence.md
WARN if: claim is directionally true but overstated or unprovable
FAIL if: claim not in facts.yaml, boundary violated, metric invented, or title inflated
```

Output format:
```markdown
## Factuality Audit

### PASS
- "Built offline agglomerative clustering with 52 unit tests" → facts.yaml:aura.bullets.startup[3] ✓

### WARN
- "Deep backend expertise" → boundaries.md flags this — soften or remove

### FAIL
- [anything that must be removed before sending]
```

**Gate:** Document does not proceed to Stage 9 until all FAILs are resolved and all WARNs reviewed.

---

### Stage 8 — ATS / Readability Reviewer

**Reads:** `resume_{Company}.md`

**Produces:** `pipeline_state.md` → section `## ATS Review`

Check:
- JD keywords present verbatim where matched (from `## JD Signals`)
- Section headings: standard (`Experience`, `Projects`, `Skills`, `Education`)
- No tables, columns, graphics if ATS track selected
- Bullet count per role: 2–4 max
- No orphaned lines, widows, spacing issues
- Reading grade: clear, direct, no jargon without context

---

### Stage 9 — Final Editor

**Reads:** All `## WARN` items from Stage 7 + `## ATS Review` + `resume_{Company}.md` + `cover_letter.md`

**Produces:** Final clean versions of both files.

**Stop-slop pass (mandatory):**
- Remove any adverb.
- Find every passive construction — rewrite with an actor.
- Remove any sentence that starts with a Wh- word (What/Which/Where/When/Who).
- Remove em-dashes.
- Remove "not X, but Y" constructions — state Y directly.
- Cut any sentence that sounds like a pull-quote.
- Vary sentence length — no three consecutive sentences at the same length.
- Read cover letter aloud. If any sentence sounds like an AI wrote it, rewrite it.

---

## 5. Inter-Stage Handoff Schema

All stages write to `applications/{Company}_{YYYY-MM}/pipeline_state.md` under their named section.  
Each stage reads only the sections it needs (listed in its definition above).  
The file is append-only — earlier stages are never overwritten.

```
pipeline_state.md structure:
  ## JD Signals          ← Stage 2
  ## Candidate Inventory ← Stage 3
  ## Evidence Match      ← Stage 4
  ## Positioning Strategy ← Stage 5
  ## Factuality Audit    ← Stage 7
  ## ATS Review          ← Stage 8
```

---

## 6. Company Context File Template

`research/companies/_template.md`:

```markdown
# {Company} — Context Layer
_Last updated: {YYYY-MM-DD}_

## What they make
## Business direction
## Technology signals
## Culture & hiring patterns
## Relevant to this role
## Sources
## Confidence
[HIGH / MEDIUM / LOW per section]
```

---

## 7. Hardcoded Invariants (Never Override)

These rules apply regardless of company, role, or track:

1. **No invented facts.** If it is not in `facts.yaml` or `evidence.md`, it does not appear.
2. **No boundary violations.** `boundaries.md` is an absolute constraint, not a suggestion.
3. **No buzzwords.** The banned list in `facts.yaml#boundaries.general` is exhaustive.
4. **One page.** Non-negotiable for this experience level.
5. **Stop-slop pass always runs.** Stage 9 is never optional.
6. **Aura is self-funded.** Never imply VC funding, customers, revenue, or traction.
7. **Omi PRs.** 7 authored, all closed unmerged. Downstream merges are not authorship.
8. **Mia is not AGI.** It is a personal agent system / developer CLI.

---

## 8. Reuse Checklist (Per Application)

```
[ ] Create applications/{Company}_{YYYY-MM}/input.md with JD + track + notes
[ ] Check if research/companies/{Company}.md exists and is <60 days old
    [ ] If not → run Stage 1 first (or in parallel with 2+3)
[ ] Run Stages 1+2+3 in parallel
[ ] Run Stage 4 → review Evidence Match before proceeding
[ ] Run Stage 5 → review Positioning Strategy (human approval checkpoint)
[ ] Run Stage 6 → draft resume + cover letter
[ ] Run Stages 7+8 in parallel
[ ] Run Stage 9 → final output
[ ] Human review: read cover letter aloud; check resume fits one page
[ ] Archive: move pipeline_state.md to applications/ folder
```

**Human approval checkpoints:** after Stage 5 (positioning) and after Stage 9 (final).  
Everything else runs automatically.

---

## 9. Token Efficiency Rules

- Stage 1 output is ≤400 words. Do not summarize what is obvious.
- Stage 3 reads `facts.yaml` once — do not re-read between stages.
- `{Company}.md` is cached and reused across all applications to that company.
- Stages 7+8 read only the final documents, not the full pipeline state.
- If a stage produces no findings (e.g., no FAIL items in Stage 7), it writes `[CLEAR]` and stops.
- Cover letter is ≤4 paragraphs. Resume bullets are ≤2 lines each. Length limits are hard.

---

## 10. Extending to New Companies

1. Add `applications/{NewCompany}_{YYYY-MM}/input.md`
2. Stage 1 generates `research/companies/{NewCompany}.md` automatically
3. All other stages are company-agnostic — no prompt changes needed
4. If the company is in wearable/medical hardware, add to Stage 5 prompt: *"Lead with Aura's hardware-to-cloud span as primary hook"*
5. If MNC track, confirm ATS-safe formatting in Stage 8 before proceeding

---

_Spec version: 1.0 · September 2026 · D:/download/resume/_
