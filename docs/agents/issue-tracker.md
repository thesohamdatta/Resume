# Issue tracker: GitHub

Issues and specs for this repository live in GitHub Issues. Use the connected GitHub tools or `gh` CLI for issue operations.

## Conventions

- Read issues with the full body and comments before implementing them.
- Publish one issue per implementation ticket.
- Link implementation issues to their parent spec as sub-issues when GitHub supports it; otherwise include `Part of #<parent>`.
- Represent blockers with GitHub's native issue dependencies when available. If unavailable, include a clear `Blocked by: #<n>` line in each issue body.
- Apply `ready-for-agent` to implementation tickets that are ready to implement.
- Do not close or rewrite a parent issue when publishing its child tickets.
- Close tickets only when their acceptance criteria are verified and the issue tracker supports the close operation.

## Pull requests as a triage surface

**PRs as a request surface: no.** Pull requests are implementation/review artifacts, not feature requests.

## Integration

- The repository is `thesohamdatta/Resume`.
- The default branch is `main`.
- Multi-ticket implementations should use a shared integration branch and a reviewable pull request when appropriate.
