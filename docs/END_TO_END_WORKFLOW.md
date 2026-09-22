# End-to-End Workflow: Job Description → PDF Resume

## Goal

Turn a company + job description into a targeted, factual, one-page resume, cover letter, interview prep, and final PDF.

## Active tracks

Only two tracks are active:

- `local`: Indian local IT/product companies and smaller engineering teams.
- `mnc`: multinational and enterprise hiring.

Legacy `startup` and `midlevel` outputs are not used for new applications.

## Required resume structure

Both tracks use this default order:

1. Header / Contact
2. Summary
3. Experience
4. Projects
5. Education
6. Technical Skills
7. Certifications, only when verified

Do not move Experience, Projects, Education, or Skills around just to imitate another resume.

## Phase 1: Input

Create `applications/{Company}_{YYYY-MM}/input.md`:

```yaml
company: [Company Name]
track: [local | mnc]
jd_url: [optional]
jd: |
  [Full job description]
notes: |
  [Optional targeting notes]
```

## Phase 2: Research

Use `research/SWARM_RESEARCH.md` for deep company research when the dossier is missing or stale.

Research should establish:
- company/product context
- role requirements
- engineering/technology signals
- recent relevant developments
- candidate↔company evidence overlap

Never use company research as a source of candidate facts.

## Phase 3: Pipeline

Run the 10 stages in `pipeline/run.md`:

```
01 company research
02 JD analysis
03 candidate context
04 evidence match
05 positioning
06 resume writer
07 factuality
08 ATS review
09 final editor
10 slop-free polish
```

Stages 01–03 run in parallel. Stages 07–08 run in parallel.

## Phase 4: Writing

Stage 06 must read technical proof before drafting:

1. `content/github/evidence.md`
2. `data/facts.yaml`
3. `content/github/boundaries.md`
4. selected base file:
   - `versions/local/_base.md`
   - `versions/mnc/_base.md`

Write from evidence, not from generic skill names.

Every bullet should make clear:
- what was built/done
- the concrete technology or method
- why it mattered or what it enabled

Never invent metrics, users, ownership, employers, dates, production status, funding, or outcomes.

## Track treatment

### Local

- One page.
- Clean, technical, human-readable.
- Same section order as MNC.
- Slightly more product/project context is acceptable.
- Avoid repetitive keyword stuffing.

### MNC

- One page by default.
- Single column.
- Standard section headings.
- Plain searchable text.
- ATS-safe formatting.
- No tables, graphics, or decorative symbols carrying important meaning.

## Phase 5: Validation

Stage 07 checks every claim against `facts.yaml`, `evidence.md`, and `boundaries.md`.

Any factuality FAIL stops the pipeline.

Stage 08 checks:
- required section order
- ATS readability
- keyword coverage
- contact completeness
- bullet count
- one-page fit
- verified certification status

## Phase 6: Final edit

Stages 09 and 10:
- resolve factuality/ATS issues
- preserve claim strength
- remove slop and generic phrasing
- preserve candidate voice
- keep the required section order

Any drift FAIL stops delivery.

## Phase 7: Rendering

Render the selected markdown resume through the repository LaTeX template.

Validate:
- PDF opens
- text is selectable
- important terms are searchable
- links work
- no overflow/cutoff
- no blank page
- one page
- correct filename

Default filename:

```
Soham_Datta_Resume.pdf
```

For company-specific files:

```
Soham_Datta_Resume_{Company}.pdf
```

## Phase 8: Delivery

Deliver:
- final resume
- cover letter
- interview prep
- any unresolved gaps or factual warnings

Do not deliver a resume that has unresolved factual FAILs.

## Repository outputs

```
versions/{local|mnc}/resume_{Company}.md
versions/{local|mnc}/resume_{Company}.pdf

applications/{Company}_{YYYY-MM}/
  input.md
  pipeline_state.md
  cover_letter.md
  interview_prep.md
```

## Human checkpoints

- After Stage 05: positioning and primary hook
- After Stage 07: factuality FAILs
- After Stage 10: final PDF and claim integrity

## Source authority

```
data/facts.yaml                  = biographical facts
content/github/evidence.md       = technical proof
content/github/boundaries.md     = claim constraints
versions/local/_base.md          = local structure
versions/mnc/_base.md            = MNC structure
pipeline/run.md                  = execution order
DONT.MD                          = resume rules
```

Evidence before inference. Structure before decoration. Truth before polish.
