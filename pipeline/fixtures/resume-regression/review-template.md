# Resume regression review

Use this template once per comparison session. Record the baseline and candidate commit SHA. This is a human review pack, not an automated resume-quality score.

## Run identity

- Date:
- Baseline commit: `235a13de04ce48e9600a79f4685b30d6cca375f9`
- Candidate commit:
- Candidate facts version used in each checkout:
- Reviewer:

## Hard gates

Complete for all three cases before judging style:

| Gate | AI/ML | LLM/Agent | General SWE |
|---|---|---|---|
| Evidence trace passes | | | |
| Metric check passes | | | |
| PDF has exactly one page | | | |
| PDF is at most 2,500,000 bytes or has a documented exception | | | |
| Extracted text contains contact details and all visible resume content | | | |
| No broken links, placeholders, or wrong employer/title/dates | | | |
| Every claim survives the candidate-boundary check | | | |

A failed hard gate blocks delivery; do not compensate with a high style score.

## Human comparison

Score each axis from 1 (poor) to 5 (strong). Explain actual differences, not only numbers.

| Axis | AI/ML baseline → candidate | LLM/Agent baseline → candidate | General SWE baseline → candidate |
|---|---|---|---|
| Truth and ownership accuracy | | | |
| JD relevance | | | |
| Recruiter clarity in 5–15 seconds | | | |
| Specific implementation evidence | | | |
| Space efficiency and one-page readability | | | |
| ATS reading order | | | |

## Claim changes

For each case, record important claims added, removed, or weakened. Each change needs a source and a reason.

| Case | Claim changed | Source | Reason | Accepted? |
|---|---|---|---|---|
| | | | | |

## Decision

- Any truth, ownership, status, metric, or eligibility regression? If yes, block.
- Any useful evidence removed without a clear relevance/space reason? If yes, revise.
- Did the candidate become more relevant without weaker factual support?
- Follow-up fixes:
- Final decision: `PASS` / `REVISE` / `BLOCK`

Do not average the scores into a match percentage. One serious truth regression outweighs style improvements.
