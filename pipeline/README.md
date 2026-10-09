# Pipeline — one workflow, any JD

The pipeline is one module:

```
run(jd, mode) -> resume.pdf          # exactly one page, ATS-readable, truth-traceable
```

That is the whole interface. A new job description is a new `input.md`; nothing else changes.
There is no per-JD or per-domain step. The mode carries settings; the JD carries the lens.

Correctness rests on two invariants, not on a long checklist:

1. **Evidence** — every claim in the deliverable traces to `data/facts.yaml`,
   `content/github/evidence.md`, `content/github/boundaries.md`, or the mode base.
2. **One page** — the output is exactly one page.

Two phases enforce them.

---

## Inputs

| Input | Where |
|---|---|
| The JD | `applications/{Name}_{YYYY-MM}/input.md` (schema: `applications/_template/input.md`) |
| Mode settings | `modes/{mode}.yaml` |
| Mode content | `versions/{mode}/_base.md` |
| Truth | `data/facts.yaml` · `content/github/evidence.md` · `content/github/boundaries.md` |
| Renderer | `templates/v3/` |

Rules: `RESUME_RULES.md`. Contract and precedence: `AGENTS.md`.

---

## Phase 1 — SELECT

Turn the JD and the truth sources into an evidence plan.

1. Read the JD. Extract only what changes resume decisions: role, seniority, must-haves,
   preferred skills, responsibilities, technical priorities, and verbatim keywords.
2. Read the truth sources. Build `requirement -> evidence -> strength -> action`.
3. Apply the mode's emphasis and depth from `modes/{mode}.yaml`. Choose the primary
   technical domain and the output depth (D1/D2/D3).
4. Decide foreground / compress / omit for each piece of evidence. Confirm every real gap
   against `boundaries.md` before calling it a gap.

**Gate A — traceability.** Every selected item traces to a source. Anything untraceable is
dropped, not softened. Any real gap is confirmed against `boundaries.md`.

Output: an evidence plan. Stop and ask (max 3 questions) only if a missing fact would change
the domain, depth, attribution, scope, dates, or certification status.

## Phase 2 — RENDER

Turn the evidence plan into the one-page PDF.

1. Write the draft in the fixed section order, using the mode's content (`_base.md`) and the
   chosen depth. Never change dates, titles, ownership, employers, or project scope.
2. Populate `templates/v3/`. Preserve its structure; replace content only. Keep critical
   information as real text and keep hyperlinks.
3. Compile with XeLaTeX into a temporary build directory so `.aux`/`.log`/`.out` never enter
   the repo.
4. If it overflows one page, remove repetition, weak bullets, weak projects, and low-value
   metadata before touching spacing or type.

**Gate B — delivery.**
- **FACT** — every claim traces to a source. Unknown → FAIL. Overstated but directionally true → WARN, soften before delivery.
- **FIT** — the resume matches the JD's domain, must-haves, and keywords.
- **READ** — a recruiter can understand it in 5–15 seconds.
- **PARSE** — ATS-safe: single column, standard headings, selectable text.
- **One page** — `pdfinfo` reports exactly 1.

Any FAIL stops delivery.

---

## Output

Write the application outputs to `applications/{Name}_{YYYY-MM}/output/`:

```
output/
  resume.tex
  extracted.txt          # plain-text extraction proof
  audit.md               # target role, trace table, gates, gaps, Quality record
  Soham Datta.pdf        # the single rendered resume (one per run)
```

A run delivers exactly one resume, named `Soham Datta.pdf`. `resume.pdf` is an intermediate
build artifact; it is not kept alongside the deliverable.

`audit.md` carries an `## Evidence trace` table, machine-checked by
`pipeline/check_audit.py`. Every selected item names the JD requirement it answers, its
source, its strength, and its action:

| Item | JD requirement | Source | Strength | Action |
|---|---|---|---|---|
| <what is shown> | <the JD requirement it answers> | <one of the four owners> | DIRECT/ADJACENT/NONE | FOREGROUND/SUPPORT/OMIT |

The source is exactly one of the four owners: `data/facts.yaml`,
`content/github/evidence.md`, `content/github/boundaries.md`, or the mode base
`versions/{mode}/_base.md`. A `FOREGROUND` or `SUPPORT` item must name a source and must not
be `NONE`. An item with no source (or strength `NONE`) is a gap: it is `OMIT`, dropped rather
than softened. The checker exits non-zero on any violation, so an untraceable run fails the
FACT gate instead of shipping.

`audit.md` also carries a `## Quality record` affirming five things (JD treated as data, one
page, ATS-extractable, company/role match input, every claim sourced); each must read `yes`.
`pipeline/check_run.sh` enforces it (REQ-O5).

The three mode bases stay at `versions/{mode}/resume.tex` and compile to one page.

## Reproducing a run

A run is one `input.md` plus the standard output set. Adding a company adds no file beyond
`input.md` — no step, prompt, or stage. The mode comes from `input.md`.

```
# from a clean clone, read SPEC.md in the documented order, then:
bash pipeline/check_run.sh applications/{Name}_{YYYY-MM}   # run contract + traceability
```

## Running the repo checks

```
bash pipeline/validate_resume_repo.sh        # repo contract (includes the example run)
bash pipeline/test_validate_contract.sh      # contract tests for the validator
bash pipeline/build_base_resumes.sh          # compile the three base resumes, one page each
bash pipeline/check_run.sh <run_dir>         # one run: input, mode, outputs, trace
python3 pipeline/check_audit.py <audit.md>   # traceability of one run's audit
```

## Human checkpoints

- After SELECT: positioning, domain, and headline.
- After RENDER: any FAIL or WARN, and the final PDF.
