# Resume Engine

A small evidence-first system for generating tailored resumes from a job description and a supplied template.

## The workflow

```text
candidate evidence + JD + template + notes
                    ↓
                 analyze
                    ↓
                  match
                    ↓
                 select
                    ↓
                  write
                    ↓
                  render
                    ↓
                 verify
                    ↓
              resume + audit
```

The goal is not maximum information. It is the smallest clear document that makes the strongest truthful case for the role.

## Fast application workflow

Create: applications/Company_YYYY-MM/input.md

Use the contract in engine/INPUT.md:

```markdown
# Application Input

Company: Example
Role: AI/ML Engineer
Track: mnc

## Job Description

[paste full JD]

## Template

templates/v3/resume.tex

## Optional notes

[anything specific to this application]
```

Then give the application folder to the resume agent with engine/PROMPT.md as its operating contract.

Expected output:

```text
applications/Company_YYYY-MM/output/
├── resume.tex
├── resume.pdf
├── extracted.txt
└── audit.md
```

## Canonical evidence

| Purpose | Source |
|---|---|
| Candidate facts | data/facts.yaml |
| Technical proof | content/github/evidence.md |
| Ownership / attribution boundaries | content/github/boundaries.md |
| Application input | applications/*/input.md |
| Resume engine | engine/PROMPT.md |
| Engine rules | engine/RULES.md |
| Template | templates/ |

Historical resumes and old application runs are reference material, not sources of truth.

## Active tracks

There are three presentation modes:

- referral — Soham Karande; broad and easy to forward
- startup — Soham Datta; stronger ownership and builder signal
- mnc — Soham Datta; conventional, precise, ATS-safe

A track changes emphasis and presentation. It never changes facts.

## Design principle

Evidence is the source. The JD decides relevance. The template decides presentation.

The engine must never invent:

- metrics
- users
- customers
- scale
- technologies
- ownership
- dates
- production status
- qualifications

## Quality gates

Every generated resume must pass:

1. FACT — claims are supported.
2. FIT — relevant evidence is visible.
3. READ — the page is easy to scan.
4. PARSE — the PDF remains coherent when extracted as plain text.

If the page is too full, remove weak information before shrinking typography.

## Repository structure

```text
data/        canonical facts
content/     technical evidence and boundaries
engine/      generation contract and rules
templates/   visual templates
versions/    reusable base tracks
applications/role-specific runs
research/    external research
archive/     historical material
```

Keep the active system small. New rules belong in the engine only when they solve a demonstrated failure.