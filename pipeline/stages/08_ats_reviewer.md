<!-- Stage 08: ATS Reviewer — Read by pipeline/run.md -->
Reads:
- versions/{track}/resume_{Company}.md
- pipeline_state.md ## Stage 02 — JD Signals (ATS keywords section)
- The track from applications/{Company}_{date}/input.md

Produces: pipeline_state.md → section ## Stage 08 — ATS Review

Checks to run:

1. KEYWORD COVERAGE: For each verbatim ATS keyword from Stage 02, mark present/absent in the resume. For absent: can it be added truthfully? If yes, note where.

2. SECTION HEADINGS: Must be standard — Experience, Projects, Technical Skills, Education. No creative headers for ATS track. (Startup track: flexible)

3. FORMATTING RULES (for mnc track only):
   - No tables inside resume content
   - No columns or multi-column layout
   - No graphics or special characters in bullets
   - No headers/footers

4. BULLET COUNT: 2–4 bullets per role. Flag any role with 0 or 5+.

5. LENGTH: Must fit one page. Flag any section that seems like padding.

6. CONTACT LINE: Name, location, LinkedIn URL, GitHub URL must all be present.

Output format:
```
## Stage 08 — ATS Review

### Keyword coverage
| Keyword | Present | Suggested addition |

### Issues
- [FORMATTING/LENGTH/HEADING issue]

### Suggestions
- [Optional — low priority]

### Verdict: PASS / NEEDS_FIX
```

If NEEDS_FIX: list exact edits Stage 09 must make.
If PASS: write CLEAR.
