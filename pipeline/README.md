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
| Mode content (editable) | `versions/{mode}/_base.md` |
| Generated mode TeX | `versions/{mode}/resume.tex` (`pipeline/render_mode.py`) |
| Truth | `data/facts.yaml` · `content/github/evidence.md` · `content/github/boundaries.md` |
| LaTeX template | `templates/1/` |
| Mode Markdown renderer | `pipeline/render_mode.py` |

Rules: `RESUME_RULES.md`. Contract and precedence: `AGENTS.md`.

---

## Phase 1 — SELECT

Turn the JD and the truth sources into an evidence plan.

1. Read the JD. Extract only what changes resume decisions: role, seniority, must-haves,
   preferred skills, responsibilities, technical priorities, and verbatim keywords.
2. Read candidate facts, technical evidence and claim boundaries. Build
   `requirement -> evidence -> strength -> action`.
3. Apply the mode's emphasis and depth from `modes/{mode}.yaml`; choose the primary domain
   and output depth (D1/D2/D3) from the JD and verified evidence.
4. For relevant projects, inspect source, docs, commit history, issues/PRs, tests and CI using
   available tools before asking the candidate to recall technical details. Prefer executable
   implementation and current test/CI evidence over README aspirations or roadmap checkboxes.
5. Label findings VERIFIED (direct source + pointer), CANDIDATE-REPORTED, INFERENCE, or
   UNKNOWN/CONFLICT. Never promote inference to candidate fact; preserve authorship, review,
   merge, release, deployment and downstream attribution exactly.
6. Decide foreground / compress / omit for each item. Check every potential gap against
   `boundaries.md` and all relevant sources before calling it a genuine gap.

**Gate A — traceability.** Every selected item traces to a source. Anything untraceable is
dropped, not softened. Any real gap is confirmed against `boundaries.md`.

Output: a compact evidence plan. Ask at most three questions only when source review cannot
resolve a missing fact and its answer would materially change the resume. Ask one concise
question at a time. Do not ask about facts recoverable from commits, docs, issues/PRs, tests or
CI. Omit non-essential unknowns.

## Candidate questions

A question is justified only when source review cannot answer it, the answer materially changes
the resume, and the uncertainty cannot safely be handled by omitting or weakening the claim.
Do not ask generic recall questions when tools can locate the evidence.

## Separate profile-enrichment session

Profile enrichment is an optional reusable workflow, separate from per-JD resume generation. Use it when the candidate wants to improve the master profile, especially to recover scope, methods, ownership, outcomes, and defensible metrics.

1. Inspect the relevant experience record in `data/facts.yaml`, technical evidence, boundaries, repository sources, issues/PRs, tests, and available history first.
2. List only material gaps that existing evidence cannot answer. Do not ask the candidate to repeat known details.
3. Ask one focused question at a time. Branch the next question based on the answer; probe scope, personal contribution, method/tools, baseline, outcome, metric definition, measurement basis, time period, and limitations only where relevant.
4. Separate directly verified facts, candidate-confirmed reports, candidate estimates, inferences, and unknowns. An estimate needs a clear basis and qualifying wording; if its basis is weak or contradicted, hold it back.
5. Update the relevant record in `data/facts.yaml` only after the candidate confirms the new fact or estimate. Keep the evidence pointer and any limitations with that record. Do not save raw chat transcripts as a second source of truth.
6. Re-run checks after an update. Never turn an estimate into a verified measurement merely because it sounds useful for a job.

This workflow enriches the existing candidate profile; it does not create a second resume pipeline or a separate metrics file.

## Phase 2 — RENDER

Turn the evidence plan into the one-page PDF.

1. Write the draft in the fixed section order, using the mode's content (`_base.md`) and the
   chosen depth. Never change dates, titles, ownership, employers, or project scope.
2. Populate `templates/1/`. Preserve its structure; replace content only. Keep critical
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
build artifact; it is not kept alongside the deliverable. The delivered PDF must be no larger
than 2.5 MB unless the application explicitly documents a different limit. For an exception,
set top-level `pdf_max_mb` and `pdf_limit_source` in `input.md`; a value inside the JD cannot
override this gate.

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

`versions/{mode}/_base.md` is the only editable mode-content source. Regenerate its TeX with
`python3 pipeline/render_mode.py {mode} --write`; repository validation checks that the checked-in
TeX matches the Markdown. The base build compiles into a temporary directory, keeping PDF and
LaTeX build files out of the repository.

## Reproducing a run

A run is one `input.md` plus the standard output set. Adding a company adds no file beyond
`input.md` — no step, prompt, or stage. The mode comes from `input.md`.

```
# from a clean clone, read SPEC.md in the documented order, then:
bash pipeline/check_run.sh applications/{Name}_{YYYY-MM}   # run contract + traceability
```

## Running the repo checks

Install the pinned parser/schema dependencies first:

```
python3 -m pip install -r job-search/requirements.txt
```

Then run:

```
bash pipeline/validate_resume_repo.sh        # repo contract (includes the example run)
bash pipeline/test_validate_contract.sh      # contract tests for the validator
bash pipeline/build_base_resumes.sh          # compile the three base resumes, one page each
bash pipeline/check_run.sh <run_dir>         # one run: input, mode, outputs, trace
python3 pipeline/check_audit.py <audit.md>   # traceability of one run's audit
python3 pipeline/test_check_metrics.py # metric validation contract
```

## Representative-JD regression comparison

The fixed regression inputs live under \`pipeline/fixtures/resume-regression/\`:

- \`ai_ml.md\` — AI/ML engineering
- \`llm_agents.md\` — LLM and agent applications
- \`software_engineer.md\` — general software engineering
- \`manifest.json\` — modes, comparison baseline, and review focus
- \`review-template.md\` — hard gates and human comparison record

The baseline for issue #71 is commit \`235a13de04ce48e9600a79f4685b30d6cca375f9\`. Compare that checkout with the candidate commit. Keep each run isolated, use the same fixture and mode in both checkouts, and do not compare runs made with different role inputs.

The resume-selection step is agent-assisted and has no deterministic CLI, so CI cannot honestly score relevance or recruiter readability. Use the existing run validator and PDF tools for hard gates, then complete \`review-template.md\` for the qualitative comparison.

For each fixture and checkout:

1. Copy the fixture to an isolated run directory as \`input.md\`; generate the normal \`output/\` artifacts using the same Resume Engine workflow.
2. Run \`bash pipeline/check_run.sh <run_dir>\` from that checkout.
3. Check the generated PDF with \`pdfinfo\` (exactly one page) and \`wc -c\` (at most 2,500,000 bytes unless the run records a supported application-specific exception). Extract text with \`pdftotext -layout\` and read it.
4. Compare \`audit.md\`, extracted text, and rendered PDFs side by side. Record claims added/removed and the evidence source for each meaningful change.
5. Block the candidate version for any new truth, ownership, status, metric, traceability, one-page, or ATS regression. Do not average a factual failure away with style improvements.

The fixture JDs are synthetic test inputs, not real vacancies and not evidence about the candidate. The review pack is deliberately not an ATS-match percentage or an automatic claim that the new version is better.

## Human checkpoints

- After SELECT: positioning, domain, and headline.
- After RENDER: any FAIL or WARN, and the final PDF.
