<!-- Stage 07: Factuality Checker — Read by pipeline/run.md -->
Reads:
- versions/{track}/resume_{Company}.md (the draft)
- applications/{Company}_{date}/cover_letter.md (the draft)
- data/facts.yaml (canonical source)
- content/github/evidence.md (technical proof)
- content/github/boundaries.md (constraint rules)
- pipeline_state.md ## Stage 06 — Writer Notes

Produces: pipeline_state.md → section ## Stage 07 — Factuality Audit

For every claim in the resume and cover letter, run these checks:

FORM: | Claim | Source | Status | Action |

Status values:
- PASS: claim exists in facts.yaml or evidence.md verbatim or by clear technical implication
- WARN: directionally true but potentially overstated — flag for human review
- FAIL: no anchor in facts.yaml or evidence.md, or explicit boundary violation

Mandatory boundary checks (run every time, regardless of draft content):
Enforce content/github/boundaries.md → Resume Audit Checklist (all 9 items) plus its truth-tested phrasing section. boundaries.md is canonical — never restate its items here.
Then run DONT.MD §E19 HARD GATE as the second net.

If any FAIL exists: document must NOT proceed to Stage 09. Human must resolve.
If only WARNs: proceed but list all for human review at Stage 09.
If all PASS: write CLEAR and stop.
