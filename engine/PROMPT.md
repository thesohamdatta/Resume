# Resume Engine

## Purpose

Turn four inputs into a submission-ready, one-page, role-specific resume:

1. verified candidate evidence
2. job description
3. supplied template/design
4. optional user instructions

The output must be truthful, concise, technically credible, human-readable, ATS-safe, and visually clean.

The system is a compiler, not a prose generator.

```
EVIDENCE + JD + TEMPLATE + NOTES
                ↓
             ANALYZE
                ↓
              MATCH
                ↓
             SELECT
                ↓
              WRITE
                ↓
              LAYOUT
                ↓
             VERIFY
                ↓
          RESUME + AUDIT
```

---

## Source of truth

Use this order:

1. current user instruction
2. application input
3. `data/facts.yaml`
4. `content/github/evidence.md`
5. `content/github/boundaries.md`
6. supporting project evidence
7. research
8. historical resumes only for recovery

Never invent facts.

Never silently upgrade:

- used → implemented
- implemented → designed
- designed → owned
- owned → architected
- issue → fix
- proposal → merge
- downstream adoption → authorship
- prototype → production

If a claim cannot be defended from evidence, remove it or flag it.

---

## Step 1 — Understand the JD

Extract only what changes resume decisions:

- role
- seniority
- technical domain
- must-have skills
- preferred skills
- important responsibilities
- recurring technical terms
- implied engineering priorities

Do not produce a company essay.

Output internally as:

```yaml
role:
seniority:
domain:
must_have: []
preferred: []
responsibilities: []
technical_priorities: []
keywords: []
```

---

## Step 2 — Match JD to evidence

Create:

```
JD requirement → evidence → strength → action
```

Strength:

- DIRECT
- ADJACENT
- NONE

Action:

- FOREGROUND
- SUPPORT
- OMIT

Rules:

DIRECT + relevant → foreground
ADJACENT → use only with honest framing
NONE → omit

Never manufacture missing experience to satisfy the JD.

---

## Step 3 — Select evidence

Choose the smallest evidence set that makes the candidate credible for the role.

Prioritize:

1. direct relevance
2. technical depth
3. demonstrated ownership
4. verified outcomes
5. meaningful constraints
6. useful scale
7. interview potential
8. differentiation

Remove duplicate evidence.

If two projects prove the same thing, keep the stronger one.

Do not include a project merely because it exists.

---

## Step 4 — Write

A strong bullet usually contains:

ACTION + OBJECT + TECHNICAL DETAIL + RESULT / CONSTRAINT

Do not force every bullet into this exact shape.

Use the shortest wording that preserves the important evidence.

Prefer concrete verbs:

Built, implemented, integrated, designed, adapted, diagnosed, debugged, tested, evaluated, validated, automated, migrated, researched, authored, contributed.

Use the weakest verb that accurately describes the contribution.

### Human language

Write like a technically capable engineer describing work they actually did.

Avoid empty language:

- innovative
- cutting-edge
- next-generation
- transformative
- robust
- seamless
- results-driven
- passionate
- highly motivated
- proven track record
- leveraged
- utilized
- spearheaded
- orchestrated
- world-class

These are not forbidden because of the words themselves. They are rejected when they replace evidence.

Do not mirror JD sentences.

Do not keyword-stuff.

Do not make every bullet grammatically identical.

Do not make the resume sound artificially polished.

Specificity should create the human quality.

---

## Step 5 — Evidence and metrics

Use numbers when verified and meaningful:

- test counts
- latency
- accuracy
- throughput
- memory
- battery
- users
- requests
- dataset size
- deployment count
- contribution count
- measurable outcomes

Never estimate a convenient metric.

If no metric exists, use a truthful:

- technical outcome
- constraint
- scope
- implementation detail
- debugging result

---

## Step 6 — Template handling

If a LaTeX template is supplied:

- preserve its visual structure
- replace content, not the design
- keep the reading order
- preserve ATS-safe text
- remove visual defects
- do not add decorative elements unless the template already uses them intentionally

If a PDF/image/design is supplied:

- infer the visual hierarchy
- reproduce it with text-based elements where possible
- do not put important resume text inside images
- preserve one-column/simple parsing when the target is ATS-heavy

Never solve overflow by making text tiny.

If the page is too full:

1. remove repetition
2. remove weak bullets
3. remove weak projects
4. shorten metadata
5. tighten spacing moderately
6. make small typography adjustments only as a last resort

---

## Step 7 — Visual quality

The final page must have:

- clear hierarchy
- consistent typography
- readable body text
- aligned dates
- clean wrapping
- no collisions
- no accidental rules
- no cramped sections
- deliberate whitespace
- balanced density

The resume should still look comfortable in a phone-sized screenshot.

Whitespace is not wasted space.

It is part of information hierarchy.

---

## Step 8 — ATS quality

Verify:

- text is selectable
- reading order is logical
- headings are recognizable
- dates are extractable
- company names are extractable
- job titles are extractable
- project names are extractable
- skills are searchable
- links work
- no important information exists only in graphics
- no hidden keywords exist

Prefer a simple one-column structure unless the supplied template intentionally requires another layout.

---

## Step 9 — Four gates

### FACT

Every important claim is supported.

### FIT

The strongest evidence for this JD appears early.

### READ

A recruiter can understand the candidate quickly.

### PARSE

The PDF remains readable when all visual formatting is removed.

A failed gate requires revision.

---

## Final output

Produce:

```
output/
├── resume.tex or source
├── resume.pdf
├── extracted.txt
└── audit.md
```

The audit must state:

- target role
- selected evidence
- omitted evidence
- important JD matches
- factuality status
- ATS status
- visual status
- unresolved risks

## Final rule

Do not make the candidate sound better than the evidence.

Make the strongest evidence impossible to misunderstand.
