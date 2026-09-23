# End-to-End Workflow: Job Description → PDF Resume

## Goal

Turn a company + job description into a targeted, factual, one-page resume, cover letter, interview prep, and final PDF.

## Active tracks

Three tracks are active:

- `referral`: forwarded/local-network applications; display name `Soham Karande`.
- `startup`: startups, founder outreach, and direct applications; display name `Soham Datta`.
- `mnc`: multinational and enterprise hiring; display name `Soham Datta`.

Legacy `local` and `midlevel` outputs are recovery/history only.

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
track: [referral | startup | mnc]
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
   - `versions/referral/_base.md`
   - `versions/startup/_base.md`
   - `versions/mnc/_base.md`

Write from evidence, not from generic skill names.

Every bullet should make clear:
- what was built/done
- the concrete technology or method
- why it mattered or what it enabled

Never invent metrics, users, ownership, employers, dates, production status, funding, or outcomes.

## Track treatment

### Referral

- One page.
- Clear, practical, broad technical signal.
- Easy to forward and scan.
- Do not present as a startup pitch.

### Startup

- One page.
- Stronger ownership and builder signal.
- More visible technical decisions and project identity.
- Distinctive through evidence, not gimmicks.

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
versions/{referral|startup|mnc}/resume_{Company}.md
versions/{referral|startup|mnc}/resume_{Company}.pdf

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
versions/referral/_base.md      = referral structure
versions/startup/_base.md       = startup structure
versions/mnc/_base.md            = MNC structure
pipeline/run.md                  = execution order
DONT.MD                          = resume rules
```

Evidence before inference. Structure before decoration. Truth before polish.
