# Voice Guide Skill for Career Documents

## Description

A reusable skill for writing career documents (cold emails, resumes, referral messages) guided by William Zinsser's "On Writing Well" principles, with anti-AI-slop guidance, and adapted for startup/MNC/mid-level contexts. Captures the full voice.md framework including Zinsser's simplicity and clutter-reduction principles, the banned words list, evidence boundaries, the pre-send checklist, and the audience-adaptive voice matrix.

**Trigger phrases**: "Use voice guide for resume", "Write a cold email using my voice guide", "Check this resume bullet for AI slop"

---

## Inputs

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `--context` | enum | Yes | Target company type: `startup`, `mnc`, or `mid-level` |
| `--document-type` | enum | Yes | Document type: `cold-email`, `resume`, or `referral` |
| `--tone-adaptation` | string | Optional | Personal notes on voice characteristics (e.g., "-maxxing terminology, builder warmth, professional tone") |

---

## Outputs

A complete career document generated from the following components:

- **Document body**: Full cold email, resume bullet set, or referral message
- **Evidence-backed bullets**: Using user's actual projects (Aura, Mia, Voice AI, LLM-Council) with GitHub/PR links and verifiable outcomes
- **Zinsser simplicity test**: Applied to every sentence; stripped to cleanest components
- **Banned words check**: Every word scanned against the full banned list; auto-rejection if found
- **Voice consistency filter**: Eve's "subtle + compact + nice" test applied; auto-advice if voice doesn't match
- **Company-type voice adaptation**: Startup (builder-to-bold), MNC (ATS-optimized professional), or Mid-level (balanced)

---

## Goal

Generate a complete, evidence-backed career document that passes all voice guide checks: Zinsser simplicity, banned words evasion, evidence boundaries, and voice consistency — adapted for the specified company context.

---

## Steps

### Step 1: Parse Inputs and Context

- Validate `--context` is one of: `startup`, `mnc`, `mid-level`
- Validate `--document-type` is one of: `cold-email`, `resume`, `referral`
- Extract `--tone-adaptation` notes if provided
- Load the research file: `D:\download\research\resume_voice_tone_by_company_type.md`

### Step 2: Select Company-Type Voice Profile

Based on `--context`, activate the corresponding voice matrix:

| Context | Simplicity Focus | Clutter Rules | Be Yourself | Bullet Formula | Length | Key Banned Words |
|---------|-----------------|---------------|-------------|----------------|--------|------------------|
| `startup` | Builder-focused components | Ban vague tech buzzwords | Express unique builder identity | Action + What Built + Stack + Outcome | 1 page max | passionate, innovative, leveraged, spearheaded, transformative, next-generation, inauthentic fun-maxxing |
| `mnc` | ATS-readable components | Ban non-technical fluff | Maintain professional identity | Action + Metric + Tech + Context | 1-2 pages | scalable, led team without metrics, cutting-edge without specifics, production-ready without proof |
| `mid-level` | Clear professional components | Ban mixed messaging | Authentic but professional | Context + Action + Outcome + Growth | 1-2 pages | mixed messaging, inauthentic personality |

### Step 3: Generate Document Body

Based on `--document-type`:

#### For `cold-email`:

- **Subject line**: One of the context-appropriate patterns:
  - Startup: `Engineer interested in [specific problem company solves]`
  - MNC: `Wearable AI builder — [Company] hardware team`
  - Mid-level: `Seeking [Role] opportunity — [Specific technical fit]`
- **Body**: Intimate transaction (Zinsser) with:
  - One clear point (Know what you're trying to say)
  - No more, no less (Say exactly that)
  - Context-appropriate tone (bold for startup, professional for MNC, balanced for mid-level)
  - Evidence mentions (Aura, Mia, Voice AI, LLM-Council) with specific, verifiable details
  - Clear ask (15-min call, referral, application)
  - No banned words

#### For `resume`:

- **Header**: Name, contact info, GitHub, portfolio
- **Sections**: Selected based on context:
  - Startup: Skills & Projects first (Experience secondary)
  - MNC: Experience → Skills → Projects → Education
  - Mid-level: Balanced, highlighting progression
- **Bullets**: Generated using the context-appropriate formula, each:
  - Evidence-backed (Aura, Mia, Voice AI, LLM-Council projects)
  - Passing Zinsser simplicity test
  - Free of banned words
  - Matching Eve's "subtle + compact + nice" test
- **Evidence boundaries**: Enforced per the tables (Aura = hardware/firmware/enclosure/3 PRs; Mia = CLI/5-stage/harness/ADR-0001; Voice AI = real-time agents/Silero VAD/LiveKit; LLM-Council = contributing models)

#### For `referral`:

- **Template**: Adapted from the voice.md template with context-appropriate modifications:
  - Startup: Can include builder voice, project excitement, genuine interest in their problem
  - MNC: Strictly professional, technical credentials, clear role fit
  - Mid-level: Balanced — authentic but professional
- **One-liner**: User's actual projects with specific, verifiable details
- **No pressure closing**: Appreciation for any help

### Step 4: Apply Zinsser Simplicity Test

For every sentence:

1. Identify the single clear point
2. Strip to cleanest components — remove words that serve no function
3. Replace long words with short equivalents
4. Remove adverbs that carry the same meaning as the verb
5. Remove passive constructions that leave the reader unsure
6. Cut redundant prepositions
7. If further cutting loses the point — keep it; otherwise, cut

### Step 5: Banned Words Check

Scan the entire document against the full banned words list (context-specific). If any banned word is found:

- Auto-reject that word/phrase
- Suggest the Zinsser + Eve replacement from the guide
- Flag the sentence for rewrite
- **Never** allow: "passionate about AI", "innovative solution", "leveraged TensorFlow", "spearheaded project", "cutting-edge technology", "responsible for X", "worked on Y", "significantly improved", "greatly enhanced", "substantially reduced", "scalable system", "production-ready platform", "expert in Z", "guru of V"

### Step 6: Evidence Boundary Check

Verify every claim against the evidence boundaries table:

| Project | CAN Claim | CANNOT Claim |
|---------|-----------|--------------|
| Aura | Hardware design, firmware, enclosure, Omi integration, 3 merged PRs | VC funding, customers, revenue, production scale |
| Mia | CLI tool, 5-stage harness, unified adapters, JSONL state, ADR-0001 | AGI, "production-ready platform," enterprise adoption |
| Voice AI | Real-time agents, Silero VAD, LiveKit, multi-provider fallback | "Production voice assistant," user metrics you don't have |
| LLM-Council | Contributing models | AGI, "expert," vague leadership claims |
| Internships | Specific models, transfer learning, edge optimization | "Led team," "architected system" for 3-month internship |

### Step 7: Voice Consistency Filter (Eve's Test)

Apply Eve's adapted test: "Is this me? Would I actually say this? Is it subtle + compact + nice?"

- If the document sounds inauthentic → advise on editing toward genuine voice
- If builder warmth is present but not inauthentic "fun-maxxing" → keep, label as adaptive
- If professional tone is needed (MNC) → ensure no casual elements that break ATS or reader expectation
- If mid-level balance is needed → ensure neither startup flair nor MNC stiffness dominates

### Step 8: Pre-Send Checklist Validation

Run the full pre-send checklist (from voice.md) with context filters:

- [ ] Company-specific: Named their product, tech, or problem by name?
- [ ] Evidence-backed: 2-3 concrete achievements with GitHub/PR links?
- [ ] Honest scope: No "production," "scale," "users" claims without proof?
- [ ] No banned words: Scanned each item?
- [ ] Clear ask: 15-min call? Referral? Application submitted?
- [ ] Contact info: GitHub, LinkedIn, portfolio in signature?
- [ ] Subject line: Specific, not generic?
- [ ] Attachments: Resume (PDF), portfolio link — not .docx, not zip?
- [ ] Zinsser simplicity test: Can I strip this sentence further?
- [ ] Resume length: Context-appropriate?
- [ ] Quantified metrics: Every claim verifiable with links or numbers?
- [ ] Voice consistency: Does this sound like me?
- [ ] Eve filter: "Is this subtle + compact + nice?"
- [ ] Company-type voice alignment: Does this match expectations?

### Step 9: Output Formatting

Present the generated document with:

- Full body text
- Bulleted list of evidence references (with GitHub/PR links where applicable)
- Zinsser simplicity audit summary (which sentences were stripped, which earned keep)
- Banned words audit (none found, or list of what was replaced)
- Voice consistency score/advisory (Eve test result)
- Company-type voice alignment confirmation
- Pre-send checklist status (pass/fail with notes)

---

## Success Criteria

The skill output is successful when ALL of the following are met:

- [ ] Document is complete and well-structured for the specified `--document-type`
- [ ] All bullets/claims are evidence-backed against the user's actual projects (Aura, Mia, Voice AI, LLM-Council)
- [ ] Zinsser simplicity test passed: every sentence strips to cleanest components without losing the point
- [ ] Banned words check: zero banned words present; all replaced with context-appropriate alternatives
- [ ] Evidence boundaries respected: no claims beyond what's verifiable for each project
- [ ] Voice consistency: Eve's "subtle + compact + nice" test passed, or advised edits toward authentic voice
- [ ] Company-type voice alignment: document matches expectations for startup/MNC/mid-level context
- [ ] Pre-send checklist: all items pass with context-specific filters enabled
- [ ] Trigger phrase compatibility: the output would satisfy someone asking "Use voice guide for resume" / "Write a cold email using my voice guide" / "Check this resume bullet for AI slop"

---

## References

1. **voice.md guide**: `D:\download\voice\voice.md` — Foundation principles, banned words, evidence boundaries, voice matrix, pre-send checklist
2. **Research file**: `D:\download\research\resume_voice_tone_by_company_type.md` — Startup vs MNC vs Mid-level voice differences, bullet formula comparisons, audience-adaptive voice matrix
3. **William Zinsser, "On Writing Well"** — Clear thinking → clear writing, simplicity, clutter reduction
4. **Evidence boundaries** (from voice.md): Aura, Mia, Voice AI, LLM-Council, Internships, General
5. **Banned words list** (from voice.md): 20+ entries with Zinsser + Eve + Research replacements
6. **Voice matrix** (from voice.md): Company-type voice adaptation principles
7. **Pre-send checklist** (from voice.md): 20+ validation items
8. **Eve's voice principles**: Fun as design value, two registers (startup vs MNC), subtle + compact + nice

---

## Trigger Phrases

These phrases will invoke the voice guide skill:

- "Use voice guide for resume"
- "Write a cold email using my voice guide"
- "Check this resume bullet for AI slop"
- "Apply voice principles to my cold email"
- "Generate a referral message in my voice"
- "Write a startup resume bullet"
- "Make this MNC-ready"
- "Check for AI slop in my writing"
- "Apply Zinsser simplicity to my resume"
- "Voice guide, startup context"
- "Voice guide, MNC context"
- "Voice guide, mid-level context"