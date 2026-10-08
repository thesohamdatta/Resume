# PIPELINE.md — Resume Generation Workflow

The one workflow. Every mode uses it unchanged. Each step states what it reads, what it does,
and what it writes.

```
0 INPUT → 1 UNDERSTAND → 2 MATCH → 3 SELECT → 4 WRITE → 5 RENDER → 6 VALIDATE → 7 EXPORT
```

Inputs to the whole pipeline:

- candidate knowledge — `data/facts.yaml`, `content/github/evidence.md`, `content/github/boundaries.md`
- the job description — `applications/{Name}_{YYYY-MM}/input.md`
- the mode — `modes/{mode}.yaml` and `versions/{mode}/_base.md`
- the template — `templates/v3/`
- optional notes — in the application input

Rules live in `RESUME_RULES.md`. The contract lives in `AGENTS.md`.

---

## Step 0 — Input

Read `applications/{Name}_{YYYY-MM}/input.md`. Required: company, exact role, mode
(`startup` | `mnc` | `referral`), and the full JD text.

If the mode is missing, ask. Otherwise proceed.

## Step 1 — Understand the JD

Extract only what changes resume decisions:

```yaml
role:
seniority:
domain:        # one controlled value from RESUME_RULES.md
must_have: []
preferred: []
responsibilities: []
technical_priorities: []
keywords: []   # verbatim from the JD
```

Optional deep company research (dossier in `research/companies/{Company}.md`, same schema as
`research/companies/_template.md`) when the dossier is missing or >60 days old. Research is
never a source of candidate facts. Deep multi-agent research is available via
`research/SWARM_RESEARCH.md`.

Do not write a company essay. Keep the output under 200 words.

## Step 2 — Match JD to candidate knowledge

Build `JD requirement → evidence item → strength → action` using the tables in `RESUME_RULES.md`.
Confirm any real gap against `content/github/boundaries.md` before calling it a gap.

Internal output: high-signal matches, moderate matches, confirmed gaps, evidence to suppress.

## Step 3 — Select (keyed by the mode)

Combine Step 2 with the mode config. Decide:

- Primary Technical Domain (one value)
- Output Depth (D1/D2/D3) — use the mode default unless the JD earns more
- Foreground / Compress / Omit for each piece of evidence

A mode only changes this selection, never the pipeline. If a missing fact would change the
domain, depth, attribution, scope, dates, or certification status, stop and ask (max 3 questions).

Internal output: positioning block with domain, depth, foreground/compress/omit, headline.

## Step 4 — Write

Read first: Step 3 selection, `content/github/evidence.md`, `data/facts.yaml`,
`content/github/boundaries.md`, `versions/{mode}/_base.md`.

Write the draft in the fixed section order (`RESUME_RULES.md`), using the mode's emphasis and
the chosen depth. Include only the technical detail the depth justifies. Use exact numbers only
when verified. Keep most bullets to 1–2 lines. Never change dates, titles, ownership, employer
names, or project scope.

Write the draft to `versions/{mode}/resume_{Company}.md`. Optionally write a cover letter to the
application folder when the run asks for one.

## Step 5 — Render

Populate the canonical template `templates/v3/`. Preserve its structure; replace content only.
Keep critical information as real text; keep hyperlinks; do not add section rules, decorative
graphics, skill bars, or photos. Compile with XeLaTeX inside a temporary build directory so
`.aux`, `.log`, and `.out` never enter the repository.

If the page overflows one page, remove repetition, weak bullets, weak projects, and low-value
metadata before any spacing or type change.

## Step 6 — Validate

Run the four gates from `RESUME_RULES.md` (FACT, FIT, READ, PARSE) plus the one-page check.

- FACT: every claim anchored in `facts.yaml` or `evidence.md`; unknown claim → FAIL; overstated
  but directionally true → WARN (soften before delivery).
- Also enforce `content/github/boundaries.md` (resume audit checklist + truth-tested phrasing)
  and `DONT.MD` hard-fail gate.
- Confirm section order, mode alignment, keyword coverage, one page, and correct filename.

Any FAIL stops delivery. Resolve WARNs by softening or removing the claim.

## Step 7 — Export

Write each mode's base to `versions/{mode}/resume.tex` and compile to a one-page PDF.
Write the application outputs to `applications/{Name}_{YYYY-MM}/output/`:

```
output/
  resume.tex
  resume.pdf
  <Role-named PDF, e.g. Soham_Datta_Software_Engineer.pdf>
  extracted.txt   # plain-text extraction proof
  audit.md        # target role, selected/omitted evidence, JD matches, gate status, gaps
```

Deliver: final resume, any cover letter, and unresolved gaps or factual warnings. Do not deliver
a resume with an unresolved FACT failure.

---

## Running the repo check

```
bash pipeline/validate_resume_repo.sh   # repo contract
bash pipeline/build_base_resumes.sh     # compile the three base resumes, one page each
```

## Human checkpoints

- After Step 3: positioning, domain, and headline
- After Step 6: any FAIL or WARN
- After Step 7: final PDF and claim integrity
