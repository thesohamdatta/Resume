<!-- Stage 1: Company Researcher — Read by pipeline/run.md -->
# STAGE 01: COMPANY RESEARCH

**Your Role:** Research the target company and produce/update its context file.

## Inputs to Read:
- `applications/{Company}_{YYYY-MM}/input.md` (Extract company name and Job Description (JD))
- Web sources (Use web search to research the company)

## Execution Rules:
1. **Check skip condition:** If `research/companies/{Company}.md` exists AND was modified within the last 60 days, write exactly `SKIP` to `applications/{Company}_{YYYY-MM}/pipeline_state.md` under the heading `## Stage 01` and stop execution.
2. Every claim in the output needs a cited source or an `[unverified]` tag.
3. Keep the output file under 400 words.
4. Flag any speculative inferences explicitly.

## Output Target:
Create or overwrite `research/companies/{Company}.md`

## Output Format (Exact Schema):
```
# {Company} — Context Layer
_Last updated: {YYYY-MM-DD}_

## What they make
## Business direction  
## Technology signals
## Culture & hiring patterns
## Relevant to this role
## Sources
## Confidence [HIGH/MEDIUM/LOW per section]
```
