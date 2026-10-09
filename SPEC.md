# SPEC.md — Resume Engine Specification

Status: current · Owner: repository · Supersedes the archived specifications under
`archive/pipeline_old/`.

This file answers one question: what is this system, and exactly what must hold for it to be
correct? It is written for an engineer or an agent who has never seen this repository and does
not care which companies the author has applied to. It describes the system, not a single run.

It does not restate the workflow (`pipeline/README.md`), the rules (`RESUME_RULES.md`), the
contract (`AGENTS.md`), or the per-mode settings (`modes/*.yaml`). Those files remain the
owners of their sections; this file defines the system they implement and the requirements
each of them must satisfy.

---

## 1. Problem

Producing a tailored resume is a selection-and-compilation problem under a hard truth
constraint, done repeatedly under a small context budget.

- The candidate's real work is spread across repositories, issues, pull requests, and
  documents. It is deeper than any one resume needs.
- A job description asks for a fraction of it. The rest is noise or a liability.
- Output is constrained: one page, ATS-readable, and subordinate to a fixed visual template.
- Nothing may be invented. A plausible-sounding metric is worse than no metric.
- Context is finite. Loading every application ever run, or every evidence file, makes the
  agent slower and less accurate, not safer.

The system is therefore a **compiler**: input is a job description plus a mode plus the
candidate truth sources; output is the smallest, strongest, truthful, one-page representation
for that role. The LLM is the judgment layer inside a deterministic pipeline, not the system.

The repository is the **harness** around that compiler: the read order, the truth files, the
gates, and the scripts that make a single agent reliable on a small context budget. Most of the
engineering here is harness and context engineering, not prompt prose.

## 2. Goals and non-goals

Goals:
- One pipeline, parameterized by mode, that turns any job description into a one-page resume.
- Every claim traceable to a source. No invented facts, ever.
- A small active system: few files, one owner per rule, no abstraction without a distinct
  responsibility.
- Reproducible and portable: a fresh clone runs without the author's machine, paths, or history.
- Efficient context: load only what the current task needs.
- Extensible by configuration (a new mode, a new source), not by forking the pipeline.

Non-goals:
- Prose generation, cover letters as a first-class output, or interview coaching.
- Per-company pipelines, per-domain resume formats, or a fourth presentation path.
- Redesigning the visual template.
- Treating the repository as a public product. This is a personal engine; optimizing for
  outside contributors is out of scope.

## 3. Glossary

The system uses these terms in a fixed sense. `AGENTS.md` owns naming; this file owns meaning.

- **Candidate truth** — the verifiable facts about the candidate. It has exactly three parts,
  each with one owner:
  - **Fact** — a biographical or structural constant: name, contact, dates, titles, employers,
    education, certifications, and the approved per-mode bullets. Owner: `data/facts.yaml`.
  - **Evidence** — technical proof: repositories, file paths, algorithms, tests, issue and PR
    numbers. Owner: `content/github/evidence.md`.
  - **Boundary** — a claim, ownership, attribution, metric, or status limit: what must *not* be
    claimed even though it is adjacent to the truth. Owner: `content/github/boundaries.md`.
- **Job description (JD)** — the input specification for relevance. It describes the target;
  it is never a source of candidate truth.
- **Mode** — a presentation and selection configuration: `startup`, `mnc`, or `referral`. A
  mode changes emphasis and depth. It never changes facts and never forks the pipeline. Owner:
  `modes/{mode}.yaml` (settings) and `versions/{mode}/_base.md` (content).
- **Domain** — a relevance lens chosen per JD (AI/ML, LLM/Agent Systems, Voice/Realtime AI,
  Backend/Platform, Embedded/Edge, Computer Vision, Full-Stack AI, Research/Applied AI,
  Unknown). A lens is an input to selection; it is not a mode and never branches the pipeline.
- **Depth** — how much detail a selected item carries: D1 (scope + outcome + core
  technology), D2 (outcome + method + technology), D3 (implementation, architecture,
  algorithms, tests, constraints, debugging).
- **Claim** — a statement in the deliverable. Every claim must trace to a source.
- **Traceability** — the property that each claim maps to the fact, evidence, boundary, or mode
  base that supports it.
- **Gate** — a blocking check. A failed gate stops delivery.
- **Deliverable** — the one-page PDF and its source, written under
  `applications/{Name}_{YYYY-MM}/output/`.

## 4. System architecture

```
truth sources ─┐
               ├─► SELECT ─► evidence plan ─► RENDER ─► validate ─► deliver
JD + mode ─────┘        (traceability)      (one page)   (gates)
```

One pipeline, one pass, any JD. The mode parameterizes emphasis and depth; the JD supplies the
lens. Nothing else changes between runs.

| Component | Owns | File |
|---|---|---|
| Contract | read order, precedence, hard constraints | `AGENTS.md` |
| Specification | the system, requirements, invariants, decisions | `SPEC.md` (this file) |
| Workflow | the two phases, the two gates | `pipeline/README.md` |
| Rules | evidence model, modes, voice, ATS, never-invent | `RESUME_RULES.md` |
| Hard checks | enumerated NEVER / HARD FAIL items | `DONT.MD` |
| Voice | language and tone | `docs/voice.md` |
| Facts | candidate facts | `data/facts.yaml` |
| Evidence | technical proof | `content/github/evidence.md` |
| Boundaries | claim / ownership / status limits | `content/github/boundaries.md` |
| Modes | per-mode settings | `modes/{mode}.yaml` |
| Bases | per-mode content | `versions/{mode}/_base.md` |
| Template | the only visual foundation | `templates/v3/` |
| Runs | per-application input and output | `applications/{Name}_{YYYY-MM}/` |
| Checks | deterministic repository validation | `pipeline/validate_resume_repo.sh` |
| Lessons | durable, evidence-backed learnings | `memory/lessons.md` |
| History | superseded material | `archive/` |

Design rule: one owner per responsibility. If two files state the same rule, one copy is
deleted. A new module is added only when it owns a distinct responsibility.

## 5. Requirements

Requirements are numbered so a reviewer can check the system against them. `MUST` is blocking.

### Truth

- **REQ-T1** — Every claim in the deliverable MUST trace to a fact, an evidence item, a
  boundary, or the mode base.
- **REQ-T2** — The system MUST NOT invent metrics, ownership, employers, dates, production
  status, users, funding, or skills.
- **REQ-T3** — Ambiguity that would change domain, depth, attribution, scope, dates, or
  certification status MUST stop the run and be asked, not inferred (max three questions).
- **REQ-T4** — Ownership verb strength MUST match evidence: used < integrated < implemented <
  designed < owned < architected. Open-source status MUST be preserved exactly: issue ≠
  implementation, proposal ≠ merge, approval ≠ merge, downstream adoption ≠ authorship,
  draft ≠ shipped.

### Pipeline

- **REQ-P1** — Exactly one pipeline MUST serve all job descriptions.
- **REQ-P2** — A mode MUST change emphasis, depth, and selection only. It MUST NOT change facts
  or fork the pipeline.
- **REQ-P3** — A domain MUST be chosen per JD from the JD and verified evidence, never from
  company brand or a generic job title.
- **REQ-P4** — A new job description MUST require only a new `input.md`. No step, prompt, or
  file may be added per JD or per company.

### Output

- **REQ-O1** — The deliverable MUST be exactly one page unless the application input explicitly
  requires otherwise.
- **REQ-O2** — The deliverable MUST be ATS-parseable: single column, standard section names in
  the fixed order, selectable text, and contact details in the body, not in a header or footer.
- **REQ-O3** — Output MUST preserve the canonical template's structure and hierarchy. The
  template is not redesigned.
- **REQ-O4** — When the draft exceeds one page, the system MUST remove weak content — repetition,
  weak bullets, weak projects, low-value metadata — before touching spacing or type.
- **REQ-O5** — A completed run MUST produce `resume.tex`, `extracted.txt`, `audit.md`, and
  exactly one rendered PDF named `Soham Datta.pdf` under the run's `output/` directory. There is
  one resume per run; `resume.pdf` is an intermediate build artifact, not a second deliverable.
  The `audit.md` MUST carry a Quality record affirming five things: the JD was treated as data,
  the resume is one page, its text is ATS-extractable, the company and role match the input, and
  every claim is sourced.

### Context and efficiency

- **REQ-C1** — The system MUST load only the files a run needs, following the read order in
  `AGENTS.md`. Archived material and unrelated runs MUST NOT be loaded unless the task requires
  them.
- **REQ-C2** — A rule, a source, or a prompt MUST have one owner. Duplicates MUST be removed.
- **REQ-C3** — The active system MUST stay small. Complexity (an extra stage, a wrapper, a
  sub-agent, a tool) MUST be added only when it demonstrably improves an outcome, and MUST be
  removed when it does not.
- **REQ-C4** — The system MUST remain portable: no absolute workstation paths, no dependency on
  the author's history or local machine layout.

### Verification

- **REQ-V1** — The system MUST expose a deterministic repository check that fails closed on
  contract violations (`pipeline/validate_resume_repo.sh`).
- **REQ-V2** — The system MUST expose a build that compiles each mode base to a one-page PDF
  (`pipeline/build_base_resumes.sh`).
- **REQ-V3** — Delivery MUST be blocked by a failed gate: FACT, FIT, READ, PARSE, or one page.
- **REQ-V4** — Validation MUST be reproducible: the same repository MUST produce the same gate
  result on a clean clone.

## 6. Invariants

These hold across every run, every mode, and every edit.

1. Truth outranks persuasion.
2. Candidate facts are not created, only selected, compressed, or rephrased.
3. Boundary limits are absolute, not advisory.
4. The template is the visual foundation and is not redesigned.
5. The deliverable is one page by default.
6. The resume remains ATS-parseable.
7. One owner per rule.
8. History is preserved in `archive/`, never silently deleted.
9. Active instructions stay short; deterministic checks live in scripts.
10. Context is a budget; load the smallest high-signal set.

## 7. Architecture decisions

Each decision meets three conditions: hard to reverse, surprising without context, and a real
trade-off. Decisions that meet fewer than three live only in the conversation.

- **ADR-1 — One pipeline, modes as configuration.** Rejected: a separate pipeline per mode or
  domain. Modes were previously implemented as forks, which duplicated rules and drifted.
  Trade-off: modes cannot diverge structurally; they earn distinctiveness through selection.
- **ADR-2 — Three truth layers, not one master file.** Facts are structural constants, evidence
  is technical proof, boundaries are negative constraints. Merging them was rejected: it
  produced repeated facts that drifted and hid "do not claim" rules inside positive content.
  Trade-off: a fact must be filed in the right layer; the boundary file must be read.
- **ADR-3 — Evidence-first bullets.** Bullets are derived from technical evidence, not from
  pre-written templates, so that invisible proof surfaces. Trade-off: evidence must be complete
  or bullets weaken.
- **ADR-4 — Procedural pipeline, not an autonomous agent loop.** The phases are fixed code
  paths; the LLM supplies judgment inside them. This follows the Anthropic guidance to prefer a
  workflow when the steps are predictable and to keep the simplest solution that works. It is
  also the deterministic pipeline of `DONT.MD` P8. Trade-off: less dynamic replanning.
- **ADR-5 — Single agent, sectioned stages, not a swarm.** One agent runs the pipeline; stages
  are prompts, not separate autonomous agents. Adopting the OpenAI guidance to maximize a
  single agent before adding more. Trade-off: no parallel autonomy.
- **ADR-6 — Deterministic checks in scripts, judgment in the agent.** Shell validation, the
  LaTeX build, the page-count check, and the extraction test are code. Only the parts that need
  judgment are prompts. Trade-off: some rules are enforced twice, once as prose and once as a
  script; the script wins on conflict.
- **ADR-7 — Deterministic-first, documented in prose.** Anything that can be checked by code
  is code: the repository contract, the build, the page count, the extraction test. Prose
  carries only what needs judgment. Trade-off: the prose still governs the parts a script cannot
  reach, so it must stay short.

## 8. Context engineering

Context is a finite resource with diminishing returns. Reliability comes from loading the
smallest high-signal set, not the largest. The system applies four techniques.

1. **Read order.** `AGENTS.md` defines an ordered list. A run loads the contract, then the
   workflow, then the rules, then the truth sources, then the application input, then the mode.
   Everything else is loaded only if the task needs it. This is progressive disclosure: names
   and paths first, full content on relevance.
2. **Just-in-time truth.** Truth files hold lightweight, referenceable facts and evidence. The
   agent reads the part a JD makes relevant rather than pre-loading all history.
3. **Structured state.** A run's `audit.md` and any working notes persist selection decisions
   outside the conversation, so an interrupted run can resume without re-deriving them.
4. **Isolation.** Archived runs, other applications, and unrelated evidence never enter a run's
   context. Isolation is a correctness property: unrelated history biases selection.

Anti-patterns the system rejects: loading `archive/` by default, restating rules in multiple
files, growing the contract until instructions are ignored, and passing raw evidence dumps
instead of distilled findings.

## 9. Orchestration (optional, and bounded)

The default path is a single agent running SELECT then RENDER. Orchestration is an optional
pattern applied only when a run genuinely benefits, and never a reason to fork the pipeline.

Allowed patterns, each with its fit condition:

- **Prompt chaining** — when a phase decomposes into fixed subtasks that are each easier than
  the whole (for example: extract JD signals, then match evidence, then write).
- **Routing** — when an input clearly belongs to one of a few categories (for example: choosing
  the domain lens).
- **Parallel sectioning** — when subtasks are independent (for example: gathering company
  context and reading candidate evidence at the same time).
- **Evaluator-optimizer** — when there are clear evaluation criteria (for example: a draft
  checked against the gates, revised, and re-checked).
- **Orchestrator-workers** — only when the subtasks cannot be predicted in advance. This is the
  exception, not the default.

Bounds that always apply:

- A sub-agent returns a distilled summary, not a raw dump.
- Every orchestrated step terminates on a gate or a fixed iteration limit.
- No step may author candidate facts. Facts enter only through the truth files.
- If orchestration cannot be justified by a named, demonstrated failure, do not add it.

## 10. MCP and tools

MCP servers and tools are means, not requirements. The system works without any of them.

- A tool or MCP server is added only when it removes a demonstrated failure (for example, a
  repository tool that returns file and PR evidence the agent would otherwise fetch by hand).
- A tool MUST return high-signal, token-efficient output. Overlapping or excessive tools
  distract the agent and waste context.
- A tool MUST NOT be a source of candidate facts. Facts come only from the truth files. A tool
  may confirm or locate evidence; it may not introduce a claim.
- Tool errors MUST steer toward an actionable fix and MUST fail closed on anything that would
  affect a fact or a gate.

## 11. Traceability

Every claim carries an implicit pointer to its source. The audit record makes the pointer
explicit.

For each selected item the run records: the JD requirement it answers, the source it comes
from, its strength (DIRECT / ADJACENT / NONE), and its action (FOREGROUND / SUPPORT / OMIT).
Anything untraceable is dropped, not softened. A real gap is confirmed against
`content/github/boundaries.md` before it is called a gap.

The `audit.md` requirement (REQ-O5) is the traceability artifact: target role, selected and
omitted evidence, JD matches, gate status, and unresolved gaps.

## 12. Validation gates

A gate is blocking. Any failure stops delivery.

| Gate | Question | Owner |
|---|---|---|
| FACT | Does every claim trace to a source? | `RESUME_RULES.md` |
| FIT | Does the strongest relevant evidence appear early and match the JD? | `RESUME_RULES.md` |
| READ | Can a recruiter understand the candidate in seconds? | `RESUME_RULES.md` |
| PARSE | Does the PDF remain readable when formatting is removed? | `RESUME_RULES.md` |
| ONE PAGE | Does `pdfinfo` report exactly one page? | `pipeline/build_base_resumes.sh` |

Deterministic checks (REQ-V1, REQ-V2) run before delivery: the repository contract check, the
one-page build for each mode base, the plain-text extraction test, and the LaTeX build-artifact
check. Prose gates and script checks must agree; on conflict, the script is authoritative and
the prose is corrected.

## 13. Repository map

```
AGENTS.md              contract: read order, precedence, hard constraints
SPEC.md                this file: system, requirements, invariants, decisions
RESUME_RULES.md        domain rules: evidence, modes, voice, ATS, never-invent
DONT.MD                hard-fail checks
README.md              entry overview
docs/voice.md          language and tone
data/facts.yaml        candidate facts
content/github/        evidence.md, boundaries.md, and related proof
modes/{mode}.yaml      per-mode settings
versions/{mode}/       per-mode base content and rendered base
templates/v3/          the only visual template
pipeline/              workflow, validation, build
applications/          per-run inputs and outputs
research/              external research (never candidate facts)
memory/                durable lessons
archive/               history only
```

## 14. Adding capability

The system grows by configuration and by deletion, not by accretion.

- **A new mode** — add `modes/{mode}.yaml` and `versions/{mode}/_base.md`. Do not add a stage.
- **A new evidence source** — add it to the truth layer it belongs to and let the read order
  pick it up. Do not create a parallel truth file.
- **A new rule** — add it only when it solves a demonstrated failure, and give it one owner.
- **A new tool or MCP server** — add it only under §10.
- **Retirement** — when a file loses its distinct responsibility, delete it; preserve its
  history in `archive/`.

A fresh clone must be able to answer: where facts live, where proof lives, which modes are
active, how a JD is processed, how the resume is written, how the PDF is built, and how the
result is validated — without reading any prior application run.

## 15. Acceptance criteria

The system is conformant when all of the following are true.

1. `pipeline/validate_resume_repo.sh` passes on a clean clone.
2. `pipeline/build_base_resumes.sh` compiles each mode base to exactly one page (REQ-V2).
3. A new `input.md` alone is enough to run the pipeline (REQ-P4).
4. A spot-checked claim in any deliverable traces to a truth source (REQ-T1).
5. No active file references a retired module, a workstation path, or a superseded term
   (REQ-C4).
6. An untraceable claim blocks delivery (REQ-V3).
7. The active surface contains one owner per rule (REQ-C2).

## References

The harness and context-engineering decisions in this specification follow published guidance
from the model vendors:

- Anthropic, *Building Effective Agents* — prefer a workflow over an agent when the steps are
  predictable; add complexity only when it demonstrably improves outcomes; supply a ground-truth
  feedback loop and stopping conditions. Basis for ADR-4 and §9.
- Anthropic, *Effective context engineering for AI agents* — context is a finite resource; load
  the smallest high-signal set; use just-in-time retrieval, structured note-taking, and distilled
  sub-agent summaries. Basis for §8 and §9.
- Anthropic, *Writing effective tools for agents* — few, distinct, token-efficient tools; tool
  errors should steer toward a fix. Basis for §10.
- Anthropic, *Agent Skills* and *Claude Code best practices* — progressive disclosure; keep
  configuration small, because a bloated contract is ignored; give the agent a way to verify its
  work. Basis for §8 and REQ-C3.
- OpenAI, *A practical guide to building agents* — maximize a single agent's capability before
  adding more; guardrails are a layered defense; plan for human intervention. Basis for ADR-5
  and the gate design in §12.

These are principles, not dependencies. The system cites them to justify a decision; it does
not require the reader to know them.
