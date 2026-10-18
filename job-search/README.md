# Job Search

A local-first workflow for finding and tracking private-sector technology jobs across India. It feeds shortlisted jobs into the existing Resume Engine; it does not replace that pipeline.

## Requirements

- Python 3.10 or later.
- Install the one pinned dependency set:

  ```bash
  python3 -m pip install -r job-search/requirements.txt
  ```

- Live Adzuna search additionally requires an Adzuna app ID/key. Set `ADZUNA_APP_ID` and `ADZUNA_APP_KEY` as environment variables. Do not put them in tracked files or state.
- No credentials are needed to run the fixtures or use the local tracking commands.

## Try it offline first

Run from the repository root:

```bash
python3 job-search/job_search.py run-fixtures --state /tmp/job-search-state.json --eligibility-checks /tmp/no-eligibility-checks.json
python3 job-search/job_search.py list --state /tmp/job-search-state.json
```

The included fixture demonstrates a posting, a valid empty result from one source, and a blocked source. It makes no network requests. For a tracked real-user run, omit `--state`; state is saved under ignored `job-search/state/jobs.json`.

## Search

```bash
# India-wide query through Adzuna; needs its API credentials.
python3 job-search/job_search.py search --source Adzuna --query "junior Python AI engineer" --location India

# Supplement with remote-only Remotive results.
python3 job-search/job_search.py search --source Remotive --query "Python AI engineer"

# Try both; each source reports its own success, block, or failure.
python3 job-search/job_search.py search --source both --query "Java backend developer" --location India
```

A live call is made only when `search` is explicitly run. The Adzuna adapter requires credentials. Remotive contains remote-only jobs, delays listings, and must be credited when results are displayed. Source limits are recorded in `research/job-search-sources-2026-10.md`; the local request history avoids exceeding the documented budgets in normal single-user use. Use one CLI process at a time to avoid racing local state.

## Review and track a posting

The CLI displays posting IDs in its JSON output and `list` command:

```bash
python3 job-search/job_search.py list
python3 job-search/job_search.py list --role "AI Engineer" --location Pune --work-mode hybrid --max-experience 2
python3 job-search/job_search.py link-postings adzuna-123 remotive-123 --requisition-id EMP-REQ-42 --evidence-source "https://employer.example/careers/EMP-REQ-42"
python3 job-search/job_search.py shortlist adzuna-123
python3 job-search/job_search.py not-pursuing adzuna-123
python3 job-search/job_search.py mark-closed adzuna-123 --evidence-source "https://employer.example/careers/closure-notice"
python3 job-search/job_search.py application adzuna-123 --status Applied --notes "Applied through employer website"
```

Application records are separate from posting records. A refresh can update a posting and save prior content in its history without overwriting application status or notes. Use `mark-closed` only after checking the listing or a closure notice; it requires an evidence reference and keeps the prior open version. An absent listing in a search does not itself prove closure.

The `list` filters support role-title text, location text, work mode, employment type, and the maximum confirmed minimum-experience requirement. If the source does not provide a filter field, that listing remains visible with `filter_status: Unknown` rather than being treated as a match or discarded. Known conflicts with a filter are excluded.

## Eligibility and fit

Fit is an explainable text-match aid, not a claim of proficiency. Each listed job skill has equal weight: `score = 100 × matched skills / listed skills`, rounded to a whole percent. A match means the skill phrase was found in the currently loaded candidate facts or technical evidence after explicit claim-limit/planning notes are excluded. It does not measure depth or semantic relevance. An absent skill is shown as missing evidence, not proof the candidate lacks it. If the listing has no structured skills or no positive candidate evidence is available, the score is `null` rather than a guessed zero.

Eligibility is separate. Without explicit, evidence-backed checks, the result remains `Unknown`. You can supply a local JSON file keyed by posting ID using this shape:

```json
{
  "adzuna-123": [
    {
      "description": "Required degree",
      "mandatory": true,
      "status": "met",
      "evidence": "B.E. in Artificial Intelligence & Machine Learning is completed.",
      "evidence_source": "data/facts.yaml: education"
    }
  ]
}
```

Each check's `status` is `met`, `unmet`, or `unknown`. A met/unmet value without both evidence text and evidence source is demoted to `unknown`. Only reviewed mandatory requirements count; all reviewed mandatory checks must be met before eligibility can be `Eligible`. Keep this file local and do not commit personal job decisions or notes.

## Connect a shortlisted role to the Resume Engine

```bash
python3 job-search/job_search.py handoff adzuna-123 --mode mnc
```

The command requires a shortlisted posting, creates the standard `applications/<run-name>/input.md`, and records the application as `Preparing`. It does not submit any application. Verify the original listing, ensure the full job description is present (source snippets may be incomplete), then run the existing workflow and checks described in `pipeline/README.md`. Select `startup`, `mnc`, or `referral`; the job description never changes candidate facts.

## Commands

```text
validate <posting.json>...
run-fixtures [--fixtures PATH] [--state PATH]
search --source Adzuna|Remotive|both --query TEXT [--location India] [--limit N]
list [--role TEXT] [--location TEXT] [--work-mode MODE] [--employment-type TYPE] [--max-experience YEARS] [--state PATH]
mark-closed POSTING_ID --evidence-source URL
link-postings POSTING_ID POSTING_ID... --requisition-id ID --evidence-source URL
shortlist POSTING_ID
not-pursuing POSTING_ID
application POSTING_ID --status Preparing|Applied|Interview|Rejected|Offer|Withdrawn [--notes TEXT]
handoff POSTING_ID --mode startup|mnc|referral [--run-name NAME]
```

## Boundaries

- No automatic application submission.
- No scraping around login walls, source limits or blocked access.
- No live portal calls in CI. Tests use fixtures and fake responses.
- Cross-source linking is always explicit and requires the same verified employer requisition ID plus a reference to the evidence. Similar titles or company names are not sufficient.
- Candidate facts remain in `data/facts.yaml`; technical proof in `content/github/evidence.md`; claim limits in `content/github/boundaries.md`.
- A job description is untrusted target data, not a candidate-truth source.
- For source limits and links, see [the job-source research note](../research/job-search-sources-2026-10.md).
