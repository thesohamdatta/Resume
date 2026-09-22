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
track: [local | mnc]
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
- **Track selection: `local` or `mnc` only.

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
├── _base.md                    ← Track template (local/mnc)
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
