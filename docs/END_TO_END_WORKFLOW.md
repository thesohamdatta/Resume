# End-to-End Workflow: Job Description → PDF Resume

**Goal**: Simple, complete workflow from job posting to final PDF resume, handling all necessary research, analysis, matching, writing, validation, and rendering.

---

## Overview: The Complete Journey

```
INPUT                    PIPELINE                           OUTPUT
┌─────────────┐         ┌──────────────────────┐          ┌─────────────┐
│ Job URL or  │         │  10-Stage Pipeline   │          │  PDF Resume │
│ JD Text     │────────▶│  + Research Swarm    │─────────▶│  + Cover    │
│ + Company   │         │  + LaTeX Rendering   │          │  + Prep Doc │
└─────────────┘         └──────────────────────┘          └─────────────┘
```

**Time**: ~5-10 minutes (automated with 2-3 human checkpoints)
**Input**: Job description URL or text + company name
**Output**: ATS-optimized PDF resume + cover letter + interview prep document

---

## Phase 1: Input Collection (Manual)

### What You Provide

Create `applications/{Company}_{YYYY-MM}/input.md`:

```yaml
company: [Company Name]
track: [startup | mnc | midlevel]
jd_url: [optional - job posting URL for auto-extraction]
jd: |
  [Full job description text - paste entire posting]
  
notes: |
  [Optional - special targeting instructions]
  - Role: Senior AI Engineer
  - Focus: emphasize Voice AI + real-time systems
  - De-emphasize: backend/infrastructure work
```

**Decision Points**:
- **Track selection**:
  - `startup` → Founder-readable, 1 page, builder-focused (use for: early-stage, seed/Series A, <50 people)
  - `mnc` → ATS-optimized, 1-2 pages, keyword-rich (use for: corporate, established companies, HR screening)
  - `midlevel` → Balanced presentation (use for: growth-stage, Series B+, 50-200 people)

---

## Phase 2: Deep Research (Automated with Verification)

### Stage 0: Research Swarm (Pre-Pipeline)

**When to run**: First time applying to company OR company research >60 days old

```bash
# Check if research exists and is fresh
ls research/companies/{Company}.md
# If missing or stale, run research swarm
```

**Research swarm investigates**:
1. **Company fundamentals**
   - Product/service (what they build, who uses it)
   - Tech stack (languages, frameworks, infrastructure)
   - Recent news (funding, launches, pivots)
   - Glassdoor/culture signals

2. **People intelligence**
   - Hiring manager (LinkedIn, Twitter, GitHub)
   - Team composition (eng:product:design ratio)
   - Engineering blog posts (technical depth signals)

3. **Job context**
   - Why is this role open? (new team, backfill, expansion)
   - Team structure (reporting to whom, team size)
   - Adjacent roles (what else are they hiring?)

**Output**: `research/companies/{Company}.md` (structured dossier)

**Human checkpoint**: Review company research for accuracy
- Verify product description matches your understanding
- Flag any outdated or incorrect information
- Confirm tech stack aligns with JD

---

## Phase 3: Pipeline Execution (10 Stages)

### Stages 01-03: Parallel Foundation (Automated)

**Run simultaneously**:
- **Stage 01**: Company Researcher (reads `research/companies/{Company}.md` or creates new)
- **Stage 02**: JD Analyzer (extracts must-haves, nice-to-haves, keywords, tech stack)
- **Stage 03**: Candidate Context (loads `facts.yaml` + `evidence.md` + `boundaries.md`)

**Output**: `pipeline_state.md` with three analysis sections

### Stage 04: Evidence Matching (Automated)

**Matches**: JD requirements ↔ candidate proof
- STRONG match: exact technology/experience with verifiable proof
- MODERATE match: adjacent/transferable experience
- WEAK match: conceptual overlap only

**Output**: Evidence match table in `pipeline_state.md`

### Stage 05: Positioning Strategy (Semi-Automated)

**Determines**:
- Primary hook (specific company↔candidate overlap)
- What to foreground (strongest matches)
- What to cut (irrelevant or weak)
- Cover letter structure (4 paragraphs)

**Human checkpoint** ✋ — REVIEW BEFORE PROCEEDING
```
After Stage 05 completes, read:
  pipeline_state.md ## Stage 05 — Positioning Strategy

Ask yourself:
- Is the primary hook specific and compelling?
- Does the cover letter structure make sense?
- Are we foregrounding the right projects?

If hook is generic or angle is wrong: edit Stage 05 output, then type "proceed"
If positioning looks good: type "proceed"
```

### Stages 06: Resume Writing (Automated)

**Evidence-first bullet writing**:
1. Read `evidence.md` for deep technical detail (file paths, algorithms, PR numbers)
2. Read `facts.yaml` for biographical skeleton (dates, titles)
3. Apply `voice.md` (Core Principles + Banned Words + Evidence Boundaries)
4. Write bullets: WHAT built + WHAT technology + WHY it matters
5. Max 2 lines per bullet, 3-4 bullets per role

**Writes**:
- `versions/{track}/resume_{Company}.md` (markdown resume)
- `applications/{Company}_{YYYY-MM}/cover_letter.md` (≤300 words)

### Stages 07-08: Parallel Validation (Automated)

**Run simultaneously**:
- **Stage 07**: Factuality Checker (anchors every claim in facts.yaml or evidence.md)
- **Stage 08**: ATS Reviewer (single column, standard headings, keyword density)

**Hard gate** 🚫 — STOP IF STAGE 07 FAILS
```
If Stage 07 produces FAIL items:
  STOP — do not proceed to Stage 09

Review FAILs:
- Claim has no anchor? Add to evidence.md or delete claim
- Claim overstated? Weaken to match proof
- Metric invented? Remove or replace with truthful estimate

After fixing: re-run from Stage 06
```

### Stage 09: Final Editor (Automated)

**Applies**:
- ATS fixes from Stage 08 (heading standardization, keyword placement)
- Factuality corrections from Stage 07 (claim adjustments)
- Structure polish (bullet order, section flow)

**Writes**: `Status: READY_FOR_STAGE_10`

### Stage 10: Slop-Free Polish (Automated)

**Unified voice.md pass**:
1. Load `voice.md` (full)
2. Detect context from Stage 05 (startup/mnc/midlevel)
3. Select Voice Matrix bullet formula
4. Apply rules:
   - Banned Words → Zinsser replacements
   - Core Principles (Simplicity, Clutter, Be Yourself)
   - Evidence Boundaries enforcement
5. Resume pass (strict hygiene, zero em dashes, no passive voice)
6. Cover letter pass (voice-preserving, cap 300 words)
7. Drift gate (diff vs facts.yaml/evidence.md)
8. Pre-Send Checklist (5 mandatory items)

**Drift gate** 🚫 — STOP IF DRIFT DETECTED
```
If Stage 10 logs drift FAIL:
  STOP — slop fix altered claim strength

Revert flagged edit, log FAIL, surface to human
```

**Writes**: `Status: COMPLETE`

---

## Phase 4: PDF Rendering (Automated)

### LaTeX Compilation

**Input**: `versions/{track}/resume_{Company}.md`
**Template**: `templates/v2-comma-titles/main.tex` (or v3 for custom fonts)

**Steps**:
1. Convert markdown bullets → LaTeX formatting
2. Inject into template sections (Experience, Projects, Skills, Education)
3. Compile with `pdflatex` (3 passes for references)
4. Verify single page (startup track only)
5. Clean aux/log/out files

**Output**: `versions/{track}/resume_{Company}.pdf`

**Quality checks**:
- Text selectable (not image-based)
- Links clickable (GitHub, LinkedIn, portfolio)
- Ctrl+F works for keywords
- No overfull hboxes (text overflow)
- Single page (startup) or 1-2 pages (mnc/midlevel)

### Cover Letter Rendering

**Input**: `applications/{Company}_{YYYY-MM}/cover_letter.md`
**Format**: Simple PDF or markdown (depends on submission method)

---

## Phase 5: Interview Prep (Automated)

### Generate `interview_prep.md`

**Sections**:
1. **Pitch** (10-second role-specific elevator pitch)
2. **Likely questions** (table with Answer angle + Evidence anchor)
3. **Gap defenses** (flagged gaps + honest framing)
4. **Questions for them** (3-5 specific company-research questions)

**Output**: `applications/{Company}_{YYYY-MM}/interview_prep.md`

---

## Phase 6: Delivery (Manual)

### Final Checklist

Before submitting:
- [ ] PDF opens correctly
- [ ] Text is selectable
- [ ] All links work (GitHub, LinkedIn, portfolio)
- [ ] Ctrl+F finds key technologies from JD
- [ ] Contact info correct (email, phone, location)
- [ ] Filename: `FirstName_LastName_Resume.pdf`
- [ ] No typos (Stage 10 catches most, but double-check)
- [ ] Cover letter addresses correct company/role

### Submit

1. Upload PDF to application portal
2. Paste cover letter into text box (if required)
3. Save `interview_prep.md` for later reference

---

## Context Management Strategy

### Problem: Large Context Windows

**Challenge**: Full pipeline reads:
- Company research (~5-10 pages)
- JD analysis (~2-3 pages)
- facts.yaml + evidence.md (~10-15 pages)
- boundaries.md (~3-5 pages)
- voice.md (~2 pages)
- Stage outputs (cumulative ~20 pages by Stage 10)

**Total context**: ~50-60 pages per application

### Solution: Progressive Disclosure

**Principle**: Load files ONLY when stage needs them

**Stage-by-stage loading**:
- **Stage 01**: Company research (new or existing)
- **Stage 02**: JD text only
- **Stage 03**: facts.yaml (skeleton), evidence.md (summary), boundaries.md (rules)
- **Stage 04**: Stage 01+02+03 outputs (summaries only)
- **Stage 05**: Stage 04 match table + company research (focused)
- **Stage 06**: evidence.md (FULL for technical depth), facts.yaml (templates), voice.md (Core + Banned + Boundaries)
- **Stage 07**: Resume draft + facts.yaml + evidence.md (for anchoring)
- **Stage 08**: Resume draft only (ATS scan)
- **Stage 09**: Stage 07+08 outputs (fix list)
- **Stage 10**: Resume + cover drafts + voice.md (full) + Stage 05 context detection

**Memory optimization**:
- Stages 01-03 outputs → compressed summaries after Stage 04
- evidence.md → full load only at Stage 06 (bullet writing)
- facts.yaml → skeleton at Stage 03, templates at Stage 06
- Company research → summary at Stage 04, focused re-read at Stage 05 if needed

---

## Parallel Execution Strategy

### What Runs in Parallel

**Block 1: Foundation** (Stages 01+02+03)
```
Stage 01 (Company) ─┐
Stage 02 (JD)       ├─→ wait for all three → Stage 04
Stage 03 (Candidate)┘
```

**Block 2: Validation** (Stages 07+08)
```
Stage 07 (Factuality)─┐
Stage 08 (ATS)        ├─→ wait for both → Stage 09
```

**Sequential stages**:
- Stage 04 (needs 01+02+03)
- Stage 05 (needs 04)
- Stage 06 (needs 05)
- Stage 09 (needs 07+08)
- Stage 10 (needs 09)

**Execution time**:
- Parallel blocks: ~2-3 min each
- Sequential stages: ~1-2 min each
- Total: 5-10 minutes (assuming no human edits at checkpoints)

---

## Quality Assurance: Three-Layer Defense

### Layer 1: Input Validation (Stage 02)

**Prevents**: Garbage in → garbage out
- JD parsing errors (missing requirements)
- Track mismatch (corporate JD but startup track selected)
- Incomplete JD (truncated posting)

### Layer 2: Factuality Gate (Stage 07)

**Prevents**: Fabricated claims
- Every claim → anchor in facts.yaml or evidence.md
- Metrics verified (test counts, latency numbers, PR numbers)
- Ownership accurate (never "architected" when "adapted")
- No invented users, scale, funding, production status

**Hard stop**: Any FAIL blocks progression to Stage 09

### Layer 3: Voice/Slop Gate (Stage 10)

**Prevents**: AI-generated slop
- Banned words (passionate, innovative, leveraged, spearheaded)
- Evidence Boundaries (project-specific overclaims)
- Drift from facts (Stage 10 edits must preserve claim strength)

**Hard stop**: Any drift FAIL stops delivery

---

## Human Checkpoints Summary

| Checkpoint | When | Review | Decision |
|------------|------|--------|----------|
| **Research review** | After research swarm | Company dossier accuracy | Fix or proceed |
| **Positioning** | After Stage 05 | Primary hook + cover structure | Edit or proceed |
| **Factuality** | After Stage 07 | FAIL items | Fix or proceed |
| **Final review** | After Stage 10 | PDF quality + drift check | Submit or iterate |

**Philosophy**: Human-in-the-loop at decision points, automated everywhere else

---

## Error Recovery Playbook

### Scenario 1: Stage 07 FAIL (No Anchor)

**Problem**: Claim has no anchor in facts.yaml or evidence.md
**Solution**:
1. Is claim true? → Add proof to evidence.md, re-run from Stage 06
2. Is claim overstated? → Weaken claim, re-run from Stage 06
3. Is claim false? → Delete claim, re-run from Stage 06

### Scenario 2: Stage 10 Drift FAIL

**Problem**: Slop fix altered claim strength
**Solution**:
1. Revert Stage 10 edit
2. Manually fix slop word while preserving claim
3. Re-run Stage 10 with updated draft

### Scenario 3: JD Changes Mid-Application

**Problem**: Company updates job posting after pipeline started
**Solution**:
1. Update `input.md` with new JD text
2. Re-run Stage 02 (JD Analyzer) only
3. Re-run Stage 04 → Stage 10 (skip company research if <7 days old)

### Scenario 4: Multiple Applications to Same Company

**Problem**: Sept application → resume_Company.md, Nov application → overwrites
**Solution** (choose one):
- **Option A**: Add date to filename → `resume_Company_2026-09.md`
- **Option B**: Keep outputs ONLY in `applications/` folder (no `versions/` copy)

---

## Tool Integration: What Automates What

### Research Swarm (Pre-Pipeline)
- **WebSearch**: Company news, funding, tech blog
- **WebFetch**: Job posting HTML, company careers page
- **Read**: Existing company dossiers (if <60 days old)

### Stage 01: Company Researcher
- **Read**: `research/companies/{Company}.md` (if exists)
- **WebSearch**: Company + "tech stack", "engineering blog", "recent news"
- **Write**: Company dossier (if new)

### Stage 02: JD Analyzer
- **Read**: `input.md` (JD text)
- **Grep**: Keyword extraction via patterns

### Stage 03: Candidate Context
- **Read**: `facts.yaml`, `evidence.md`, `boundaries.md`

### Stages 04-10: Pipeline Core
- **Read**: Progressive file loading per stage
- **Write**: `pipeline_state.md` (append per stage)
- **Edit**: Resume/cover drafts (Stages 06, 09, 10)

### LaTeX Rendering
- **Read**: Markdown resume
- **Bash**: `pdflatex` compilation (3 passes)
- **Write**: PDF output

---

## File Structure: Where Everything Lives

```
applications/{Company}_{YYYY-MM}/
├── input.md                    ← YOUR INPUT (JD + track + notes)
├── pipeline_state.md           ← Full audit trace (keep for reference)
├── cover_letter.md             ← Generated cover letter
└── interview_prep.md           ← Interview preparation document

versions/{track}/
├── _base.md                    ← Track template (startup/mnc/midlevel)
├── resume_{Company}.md         ← Markdown resume (tailored)
└── resume_{Company}.pdf        ← Final PDF (rendered from .md)

research/companies/
└── {Company}.md                ← Company dossier (60-day freshness)

data/
├── facts.yaml                  ← Biographical skeleton (dates, titles)
└── evidence.md                 ← Technical proof (PRs, files, algorithms)

content/github/
├── evidence.md                 ← Deep technical detail
└── boundaries.md               ← Constraints (what NOT to claim)

voice.md                        ← Voice authority (tone, banned words, formulas)
DONT.MD                         ← Resume rules (E0-E22 engines)
```

---

## Quick Start: First Application

### Step 1: Create input file
```bash
mkdir -p applications/Acme_2026-09
nano applications/Acme_2026-09/input.md
```

Paste:
```yaml
company: Acme Inc
track: mnc
jd: |
  [Full job description]
```

### Step 2: Run pipeline
```
Run the resume pipeline for Acme application in applications/Acme_2026-09/
```

### Step 3: Review checkpoints
- After Stage 05: Check positioning, type "proceed"
- After Stage 07: No FAILs? Proceed automatically
- After Stage 10: Review final PDF

### Step 4: Render PDF
```bash
cd templates/v2-comma-titles
# Convert markdown → LaTeX → PDF
pdflatex -interaction=nonstopmode resume_Acme.tex
```

### Step 5: Submit
- Upload PDF to application portal
- Save interview_prep.md for later

---

## Advanced: Multi-Company Batch Processing

### Workflow for 5+ Applications

**Day 1: Research Batch**
- Compile list of 5-10 target companies
- Run research swarm for all (parallel)
- Review dossiers for accuracy

**Day 2-3: Application Batch**
- Create `input.md` for each (JD + track)
- Run pipelines in parallel (5 at once)
- Review Stage 05 positioning for all
- Fix Stage 07 FAILs as they appear

**Day 4: Rendering Batch**
- Compile all PDFs
- Review for formatting consistency
- Submit applications

**Efficiency gain**: Amortize research/setup cost across batch

---

## Metrics: Pipeline Performance

**Target benchmarks**:
- Stage 01-03 (parallel): 2-3 minutes
- Stage 04-06: 2-3 minutes
- Stage 07-08 (parallel): 1-2 minutes
- Stage 09-10: 1-2 minutes
- PDF rendering: 30 seconds
- **Total**: 5-10 minutes per application

**Quality benchmarks**:
- Stage 07 FAIL rate: <10% (good evidence.md coverage)
- Stage 10 drift FAIL rate: <5% (clean Stage 06 writing)
- Human edit rate at Stage 05: ~30% (positioning refinement)

---

## Next Steps: Research Integration

**Pending research agent completion**:
- Internet best practices for resume generation workflows
- ATS optimization techniques (2024-2026)
- Context management strategies for large pipelines
- Quality assurance approaches (factuality, slop prevention)
- Markdown→PDF rendering options (LaTeX vs Pandoc vs Typst)

**Will inform**:
- Refinements to stage ordering
- Additional validation gates
- Alternative rendering pipelines
- Batch processing optimizations
