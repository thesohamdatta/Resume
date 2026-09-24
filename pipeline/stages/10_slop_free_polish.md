<!-- Stage 10: Slop-Free Polish (voice.md unified) — Read by pipeline/run.md. Terminal stage. -->
Reads:
- versions/{track}/resume_{Company}.md (post-Stage 09)
- applications/{Company}_{date}/cover_letter.md (post-Stage 09)
- docs/voice.md (single voice authority)
- pipeline_state.md ## Stage 05 — Positioning Strategy (for target context detection)
- pipeline_state.md ## Stage 09 — Final Editor Log
- data/facts.yaml + content/github/evidence.md (no-drift anchors — see Stage 07 boundaries)

Produces: final overwrites of both files in place.
Also produces: pipeline_state.md → section ## Stage 10 — Slop-Free Polish

VOICE CONTEXT (loaded from docs/voice.md):
- Core voice: simple, direct, specific, compact, technically grounded
- Anti-slop: remove filler, generic claims, repeated formulas, and artificial symmetry
- Ownership: preserve the evidence-supported verb strength
- Track adaptation: startup / referral / mnc
- Humanization: apply the Humanization Rules and Zinsser test

HARD RULE: never invent or alter facts. Numbers, repo names, file paths, titles,
dates, metrics, and claim strength must stay exactly as Stage 07/09 approved.
If a slop fix would change meaning, revert that fix and log it. A slop pass that
drifts from facts.yaml/evidence.md is a FAIL.

Run IN ORDER — do not skip:

**LOAD:**
1. Read voice.md fully before touching any draft.
2. Read pipeline_state.md Stage 05 → target company type (startup/referral/mnc).
3. Read the full resume and cover letter before editing.

**DETECT CONTEXT:**
4. From Stage 05 Positioning Strategy, identify target: startup | referral | mnc
5. Select the track-specific voice from docs/voice.md:
   - Startup: ownership + building + technical decisions
   - Referral: clarity + breadth + practical technical signal
   - MNC: technical precision + conventional ATS-readable language

**APPLY RULES (both resume + cover letter):**
6. Banned Words scan: every word in voice.md Banned Words table → replace with
   Zinsser alternative. Zero tolerance. Log each replacement.
7. Humanization rules (docs/voice.md):
   - Strip words that do not add meaning.
   - Replace abstract language with the concrete thing that happened.
   - Preserve useful technical details.
   - Do not manufacture personality.
8. Evidence Boundaries (voice.md §Evidence Boundaries table): audit every claim
   against facts.yaml/evidence.md. Flag any overclaim (e.g. "production-ready
   platform" when project is self-funded prototype).

**RESUME PASS (strict hygiene):**
9. Adverbs out, passive → active with human actor ("was built" → "built")
10. No Wh- openers ("What I did" → direct statement)
11. No throat-clearing ("Here is what" → cut)
12. No binary contrasts ("not X, it is Y" → state Y directly)
13. Varied sentence length (no monotone rhythm)
14. No punchy one-liner endings
15. Zero em dashes (use comma or period only)
16. Vague declaratives → specific thing (voice.md examples)
17. Narrator voice → direct fact
18. GUARDS: keep standard headings, single column, hyperlinks, technical
    specificity (function names, tools, versions, numbers). "Be specific"
    wins over brevity — never smooth useful detail into generic importance.

**COVER LETTER PASS (voice-preserving):**
19. Minimum effective edit only: fix banned words, unclear passages.
20. Leave strong human sentences alone.
21. Keep writer's vocabulary, cadence, bluntness, humor.
22. Cap 300 words (trim most padded sentence per paragraph if over).
23. Banned-outright words (voice.md list): delve, foster, leverage, utilize,
    facilitate, empower, streamline, robust, cutting-edge, paradigm shift,
    game changer, this is huge, this changes everything, tapestry, realm, beacon,
    multifaceted, meticulous, intricate, paramount, transformative, elevate,
    embark, supercharge, harness, ever-evolving, passionate, innovative,
    spearheaded, next-generation. Delete unless quoted as examples.

**DRIFT GATE:**
24. Diff every edited line vs facts.yaml/evidence.md. Any new claim, new number,
    or strengthened verb (e.g. "helped" → "led") with no anchor: revert that
    edit, log FAIL, stop, surface to human. Do not proceed.

**PRE-SEND CHECKLIST (voice.md items 1,2,3,9,11):**
25. Company-specific: Named their product/tech/problem by name?
26. Evidence-backed: 2-3 concrete achievements with GitHub/PR links?
27. Honest scope: No "production," "scale," "users" without proof?
28. Zinsser test: Can I strip this sentence further without losing the point?
29. Context match: Startup=bold/builder | Referral=broad/clear | MNC=ATS/pro?

**Slop-Free Polish log format:**
```
## Stage 10 — Slop-Free Polish (voice.md unified)
Context: {startup|referral|mnc} from Stage 05
Voice profile: {bullet formula from Voice Matrix}
Banned/filler language removed: [count, summary]
Resume edits: [what changed summary]
Cover edits: [what changed summary]
Pre-Send Checklist: [PASS/FAIL per item 25-29]
Drift check: [CLEAR / FAIL with anchors]
Status: COMPLETE
```

When Status: COMPLETE is written, the pipeline is done.
