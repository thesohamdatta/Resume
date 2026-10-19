# Job source assessment: India-wide technology search

Research date: 2026-10-19

## Recommendation

Use **Adzuna India as the first source** and **Remotive as a complementary second source**.

This choice is based on documented API access, the fields available for normalization, and source limits. It is not a claim that either source has complete coverage of Indian entry-level jobs.

## 1. Adzuna API (first source)

**Coverage and fields.** Adzuna documents a job-search endpoint at `/jobs/{country}/search/{page}`, plus query parameters and structured results. The country-specific route supports building an India search. Its API quickstart requires an `app_id` and `app_key`. See [API overview](https://developer.adzuna.com/overview), [search endpoint](https://developer.adzuna.com/docs/search), and [interactive API documentation](https://developer.adzuna.com/activedocs).

**Access and limits.** The published default limits are 25 requests/minute, 250/day, 1,000/week, and 2,500/month; Adzuna says it may change them. Its terms allow personal research, subject to terms, and describe attribution requirements for publishing ads. See [Adzuna API terms](https://developer.adzuna.com/docs/terms_of_service).

**Why first.** It offers a country-scoped job-search endpoint and structured company, location, description, URL, and date fields that fit the canonical posting model. It requires user-provided API credentials, so the adapter should report a clear setup error and never store credentials in local job data or Git.

**Limits / risks.** Coverage, result freshness, and the exact fields returned for India must be checked during a manual smoke test. API results may point to a redirect URL; preserve it and do not claim it is a direct employer application link unless verified.

## 2. Remotive public API (second source)

**Coverage and fields.** Remotive documents a public endpoint at `https://remotive.com/api/remote-jobs` returning active remote listings, including source URL, title, company, category, employment type (often optional), publication date, candidate-required location, salary text, and HTML description. Filters include search, category, company, and limit. See [Remotive public API docs](https://remotive.com/remote-jobs/api) and [API reference](https://github.com/remotive-com/remote-jobs-api).

**Access and limits.** Remotive says results are delayed by 24 hours, recommends at most four API calls per day, and blocks excessive request rates above two per minute. It requires that listings link to the Remotive listing and credit Remotive when displayed; the public API must not be used to submit jobs to third-party job sites. See the [documented terms and rate guidance](https://github.com/remotive-com/remote-jobs-api#terms-of-services).

**Why second.** It adds remote-only opportunities and supports an unauthenticated adapter, complementing the broader India-oriented source. Preserve the original Remotive URL, make the source attribution visible, and do not re-publish listings to a third-party board.

**Limits / risks.** This is a remote-only source, not a replacement for local onsite/hybrid vacancies. Location restrictions are supplied as text and must not be interpreted as “worldwide” unless the source says so.

## Other options considered

- **Jooble API:** official documentation exists, but its current help article says keys are region-specific and the free plan has a lifetime quota of 500 requests. This makes it a weaker first source for repeated personal searches. See [Jooble REST API documentation](https://jooblehelpcenter.freshdesk.com/en/support/solutions/articles/60001448238-rest-api-documentation).
- **Employer career boards:** authoritative for a specific vacancy, but each employer may expose a different API or page. Add these later as narrow adapters where they materially expand coverage.
- **Login-based boards / general web scraping:** not selected for the first adapters. The workflow must not bypass login walls, rate limits, or access controls.

## Implementation rules

- Adapters fetch and normalize only; evaluation and candidate fit remain in the shared workflow.
- CI uses fixtures and fakes, never live portals.
- A source failure or access block is visible and is not treated as a successful zero-result search.
- Keep API credentials in environment variables; do not write them into tracked config, logs, fixtures, or application state.
- The user triggers searches manually. No polling loop or background scraping is enabled by default.
- Keep each source URL, source retrieval time, and source status with the resulting posting.
