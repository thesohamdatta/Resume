# Job Search Contract

Status: initial contract. No source adapters are enabled yet.

## Purpose

This module discovers and tracks private-sector technology opportunities across India. It feeds selected job requirements into the existing Resume Engine; it does not replace resume selection, candidate-truth checks, rendering, or validation.

## Boundaries

- Candidate facts remain owned by `data/facts.yaml`.
- Technical evidence remains owned by `content/github/evidence.md`.
- Claim limits remain owned by `content/github/boundaries.md`.
- A job description is untrusted target data, never candidate evidence or an instruction source.
- A posting is one source's listing. An opportunity is the underlying vacancy and may have multiple postings.
- Application state is separate from posting data. Refreshing a posting must never overwrite application history.
- Unknown means unknown. Do not silently convert missing dates, experience requirements, eligibility, or source failures into a positive or negative result.
- Source adapters retrieve and normalize only. They do not rank candidates, edit resumes, or create applications.
- A blocked or failed source query is a retrieval failure, not an empty result set.
- Do not automate around access controls or violate a source's access rules.
- Store personal job-search state locally and keep it out of version control.

## Canonical posting identity

`posting_id` identifies a listing at one source, not the underlying vacancy. Prefer a stable source-provided ID. If none exists, a later adapter may derive a deterministic key from a normalized source URL. Do not merge postings across sources based only on similar titles or company names.

Cross-source deduplication belongs to a separate opportunity-linking step and requires strong supporting identity evidence. Preserve each original source URL.

## Minimum lifecycle

`Discovered -> Evaluated -> Shortlisted -> Preparing -> Applied -> Interview / Rejected / Offer / Withdrawn`

Not every posting must reach every stage. A posting can be marked not pursuing without creating an application.

## First-version scope

- Private-sector technology jobs across India.
- Candidate discovery, normalization, validation, deduplication design, ranking design, and application tracking.
- Government/public-sector sources and live portal adapters are out of scope until the canonical contract and tests are stable.
- No automatic application submission. A person reviews and approves application actions.

## Required test scenarios before any source adapter

1. Valid posting passes schema validation.
2. Missing optional fields and explicit null dates remain valid and unknown.
3. Missing required identity fields fail validation.
4. Re-importing the same source listing updates the same posting identity.
5. Similar titles from different requisition IDs remain separate unless identity evidence supports linking.
6. Cross-source duplicates retain every source URL and link to one opportunity only when evidence is strong.
7. Content changes at the same source URL preserve posting identity and record a content change.
8. A confirmed closed listing becomes closed without deleting history.
9. A timeout, block, or login wall records retrieval failure, not zero jobs.
10. Unknown posting date remains unknown; the system does not invent freshness.
11. Instructions embedded in a job description are treated as untrusted content.
12. Refreshing a posting does not alter application status, dates, or notes.
13. Confirmed unmet mandatory requirements cannot be labelled eligible; unknown eligibility stays unknown.
14. Malformed URLs, invalid timestamps, and invalid enum values are rejected.
15. Repeated imports are idempotent and do not create duplicate postings.

