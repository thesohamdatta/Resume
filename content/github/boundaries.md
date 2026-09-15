# Truth Boundaries — What NOT to Claim

**Strict constraints on resume claims to prevent overclaiming.**

---

## Aura

### What You CAN Claim
- Designed and 3D-printed custom CAD enclosures for wearable pendant
- Integrated physical device with Omi Glass open-source ecosystem
- Built ESP32-S3 firmware (I2S audio, Opus compression, OTA updates)
- Adapted FastAPI backend from Omi ecosystem with memory/transcription/knowledge graph routers; integrated Kubernetes-hosted Deepgram ASR
- Diagnosed GPU memory leak (Issue #8438) → merged downstream (PR #8902)
- Authored speaker clustering algorithm with 52 tests (PR #8919) → adopted downstream (PR #12471)
- Authored speaker grounding for action items (Issue #8918 → PR #12089), file indexing spec (Issue #8991 → #7896/#9595/#10236), Markdown export spec (Issue #12360 OPEN → draft PR #12927 NOT merged)

### What You CANNOT Claim
- ❌ VC funding, investors, or being "funded"
- ❌ Customers, users, revenue, or traction
- ❌ Production deployment or "in production"
- ❌ Deep backend expertise — backend was adapted/tweaked from existing infrastructure, not built from scratch
- ❌ "Built the Omi backend" — you built YOUR backend integrating WITH Omi ecosystem
- ❌ Team size beyond yourself (it's a solo self-funded effort)

### Positioning Language
- ✅ "Founder" (signals ownership + agency)
- ✅ "Independent" / "Self-funded"
- ❌ "Creator" (rejected — less clear)
- ❌ "CEO" / "Co-founder" (no company, no cofounders)

---

## Omi Open-Source Contributions

### What You CAN Claim
- Authored 21 issues including 5 architectural RFCs
- Authored 7 pull requests with 120+ unit tests
- 3 PRs approved by maintainers (security, web refactor, diarization)
- Diagnosed WebGL GPU memory leak (Issue #8438) → maintainer fixed in merged PR #8902
- Authored offline hierarchical clustering for speaker diarization (PR #8919) → adopted downstream in PR #12471
- Contributed frontend/design work and technical issue reports to Omi ecosystem

### What You CANNOT Claim
- ❌ "Merged 7 PRs" — ALL 7 authored PRs were closed unmerged
- ❌ Direct authorship of downstream merged PRs — you authored issues/proposals that INFORMED them
- ❌ Core contributor / maintainer status
- ❌ PR #8902, #12471, #12089, #12927 as YOUR work — these were authored by others based on your issue reports
- ❌ PR #8352 as approved — it received CHANGES_REQUESTED (lockfile prune, ESLint scope, unrelated files)
- ❌ Issues #7525, #7546, #7878 as implemented — closed by automated triage as stale/speculative
- ❌ Forks (about, open-wearables, podcastfy, open-notebook, Sentient, SAMANTHA-OS1, remma-o1, NanoSage, swift-chat) as authorship
- ❌ PR #12927 as merged or shipped — it is a Draft (needs-maintainer-review)
- ❌ PR #8442 as merged — positively reviewed ("work here is good") but closed unmerged

### Truth-Tested Phrasing
- ✅ "Diagnosed GPU memory leak (Issue #8438), merged downstream in PR #8902"
- ✅ "Authored speaker clustering algorithm (PR #8919), adopted downstream in PR #12471"
- ❌ "Fixed GPU memory leak in PR #8902" — you didn't author that PR
- ❌ "Merged diarization improvements" — your PR was closed unmerged

---

## Mia

### What You CAN Claim
- Built TypeScript CLI with 5-stage harness (grill → spec → plan → review → ship)
- Implemented multi-host LLM adapters (Claude, Codex, local models)
- Immutable JSONL state tracking
- Automated verification gates (lint, typecheck, Vitest)
- Eliminated daemon architecture (ADR-0001)

### What You CANNOT Claim
- ❌ AGI or "artificial general intelligence"
- ❌ Production-ready or stable — it's "working but rapidly changing/developing"
- ❌ Used by others / open-source adoption metrics

---

## Voice AI Projects

### What You CAN Claim
- Built real-time WebRTC voice agents using LiveKit
- Implemented Silero VAD for barge-in and turn detection
- John: Native Android Kotlin app + Python LiveKit agent with tool calling
- voicecoder: VS Code extension with multi-provider fallback and token tracking

### What You CANNOT Claim
- ❌ Production deployment or real users
- ❌ "Voice AI product" without context that these are experiments/prototypes

---

## General Writing Constraints

### Banned Buzzwords
Never use these words:
- passionate
- innovative
- cutting-edge
- leveraged
- spearheaded
- transformative
- next-generation
- disruptive
- game-changing
- revolutionary

### Banned Metrics (Unless Verified)
- ❌ X% improvement / accuracy / performance gain
- ❌ "N users" or "N customers"
- ❌ "Production scale" or "enterprise deployment"
- ❌ Revenue, funding, valuation
- ❌ Team size beyond what's verifiable

### Approved Style
- Short, direct, factual, understated
- Concrete verbs: built, designed, implemented, integrated, diagnosed
- Specific technical terms over vague claims
- "Built X using Y and Z" > "Leveraged cutting-edge Y to architect transformative X"

---

## Experience Claims

### AICTE via Google Internship (Oct–Dec 2024)
- ✅ Built and evaluated computer vision models with TensorFlow and ML Kit
- ✅ Applied transfer learning and data augmentation
- ❌ Do NOT inflate to "ML Engineer" or "Google Engineer"

### Freelancer AI & Automation (Sep 2024–Present)
- ✅ Built custom AI agent workflows for student/community projects
- ❌ Do NOT claim "consulting" or "clients" or revenue
- ❌ Do NOT inflate to "AI solutions for enterprises"

### Reliance Associate (Jul–Oct 2024)
- ✅ Managed store inventory, POS workflows, floor operations
- ❌ Low signal for AI roles — keep ultra-concise or omit from startup resume

### PES Modern College Research Assistant (Sep 2023–Mar 2024)
- ✅ Coordinated literature digitization and archival workflows
- ❌ Low signal for AI roles — keep ultra-concise or omit from startup resume

---

## Education

### University of Pune (SPPU)
- ✅ B.E. in Artificial Intelligence & Machine Learning
- ✅ 2022 – Jun 2026
- ❌ Do NOT claim "graduating 2026" after Jun 2026 has passed
- ❌ Do NOT add GPA unless verified and strong

---

## Validation Patterns (for automated checking)

Forbidden patterns in final resume text:

```regex
# Funding claims
/(VC|venture|funded|raised|seed|Series [A-Z]|investor)/i near "Aura"

# Customer/user claims
/(customer|user|client|deployed|production|enterprise)/i near "Aura" or "Mia"

# Merged PR claims
/(merged|shipped|landed)/i near "PR #(8919|7379|7654|8442|4649|8918|8917)"

# AGI claims
/AGI|artificial general intelligence/i near "Mia"

# Scale metrics without evidence
/\d+[%x]+ (improvement|faster|accuracy|users|customers)/

# Buzzwords
/(passionate|innovative|cutting-edge|leveraged|spearheaded|transformative|next-generation)/i
```

---

## Attribution Clarity

When discussing Omi contributions in interviews or detailed contexts:

**CORRECT:**
> "I diagnosed a GPU memory leak in the Omi desktop app (Issue #8438) by identifying that CSS backdrop filters over WebGL canvases were forcing compositor re-blending. A maintainer implemented the fix in PR #8902 which was merged."

**INCORRECT:**
> "I fixed the GPU memory leak and it was merged in PR #8902."

**CORRECT:**
> "I authored an offline speaker diarization algorithm using SciPy agglomerative hierarchical clustering (PR #8919, 52 unit tests). The approach was adopted by another contributor in a downstream merged PR."

**INCORRECT:**
> "I contributed speaker diarization that was merged into Omi."

---

## Resume Audit Checklist

Before publishing any resume variant, verify:

- [ ] No VC/funding/investor language near Aura
- [ ] No customer/user/production claims for personal projects
- [ ] Omi PR claims accurately distinguish between authored vs downstream adoption
- [ ] No "AGI" near Mia
- [ ] No fabricated metrics (%, users, speed improvements)
- [ ] No buzzwords from banned list
- [ ] Dates are accurate (check against `data/facts.yaml`)
- [ ] All technical claims trace to `evidence.md` proof
- [ ] Backend depth claims are modest ("integrated", "adapted", not "architected from scratch")
