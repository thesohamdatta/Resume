<!-- Stage 09: Final Editor — Read by pipeline/run.md -->
Reads:
- versions/{track}/resume_{Company}.md
- applications/{Company}_{date}/cover_letter.md
- pipeline_state.md ## Stage 07 — Factuality Audit (resolve WARNs)
- pipeline_state.md ## Stage 08 — ATS Review (apply NEEDS_FIX items)

Produces: Final clean versions of both files (overwrite in place).
Also produces: pipeline_state.md → section ## Stage 09 — Final Editor Log

Run this checklist IN ORDER — do not skip any item:

**FACTUALITY RESOLUTION:**
- For every WARN from Stage 07: soften the claim to remove the overstatement, or remove the bullet entirely
- For every FAIL from Stage 07: the pipeline should not have reached here — flag to human and stop

**ATS FIXES:**
- Apply every NEEDS_FIX item from Stage 08 to the resume

**STOP-SLOP PRE-PASS (quick hygiene only — Stage 10 runs the full skill-based polish):**
1. Remove every adverb
2. Find every passive construction — rewrite with an actor ("was built" → "built")
3. Remove any sentence starting with a Wh- word (What/Which/Where/When/Who) — restructure
4. Remove all em-dashes — replace with comma or period or restructure the sentence
5. Cut every "not X, but Y" or "not just X" construction — state Y directly
6. Cut any sentence that sounds like a pull-quote or would look good on a poster
7. Check sentence length variety — if 3 consecutive sentences match length within 3 words, break one
8. Cover letter: read each paragraph aloud. Flag any sentence that sounds like an AI wrote it and rewrite it.

**FINAL CHECKS:**
- One page: if resume exceeds one page, identify the lowest-signal bullet and remove it
- Cover letter: count words — must be ≤300. If over: trim the most padded sentence from each paragraph.
- Verify the primary hook from Stage 05 appears in cover letter opening paragraph
- Verify resume headline matches Stage 05 confirmed headline
- Voice check: run `D:\download\voice\voice.md` Pre-Send Checklist (company-specific, evidence-backed, honest scope, no banned words, clear ask) on both files

**Final Editor Log format:**
```
## Stage 09 — Final Editor Log
WARNs resolved: [list]
ATS fixes applied: [list]
Stop-slop removals: [count and description]
Final word count (cover letter): [N]
Status: READY_FOR_STAGE_10
```

When Status: READY_FOR_STAGE_10 is written, hand off to Stage 10. The pipeline is done only when Stage 10 writes Status: COMPLETE.
