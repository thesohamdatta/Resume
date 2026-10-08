# Pipeline State — Noise — 2026-09-14
Track: startup
Input: applications/Noise_Eng_2026-09/input.md

---

## Stage 01 — Company Research
SKIP — research/companies/Noise.md exists (created 2026-09-14, fresh).

---

## Stage 02 — JD Signals
Required: Python, TypeScript/JS, Kotlin, React/Node.js, TensorFlow/PyTorch, REST APIs, Git, LLMs, RAG, prompt engineering, signal processing
ATS keywords verbatim: Python, TypeScript, Kotlin, React, Node.js, TensorFlow, PyTorch, LangChain, RAG, OpenAI, prompt engineering, Git, Docker, REST APIs
Gaps: Flutter/iOS (none), Docker/CI/CD (not prominent) — do not claim

---

## Stage 03 — Candidate Inventory
STRONG: Aura firmware (FreeRTOS I2S DMA 16kHz, Opus, OTA), ESP32-S3 enclosure
STRONG: Speaker clustering (SciPy cosine linkage, 52 tests, PR #8919)
STRONG: John (Kotlin Jetpack Compose + Python LiveKit, tool calling)
STRONG: LLM-Council (React + FastAPI + 4 LLM providers)
STRONG: Mia (TypeScript, multi-LLM adapters, JSONL, Vitest)
STRONG: voicecoder (TypeScript VS Code ext, multi-provider, token tracking)
STRONG: AICTE (TensorFlow, ML Kit, transfer learning)
STRONG: Voice agents (LiveKit WebRTC, Silero VAD)
MODERATE: Deepgram Nova-3 self-hosted ASR (Kubernetes Helm)
MODERATE: pgvector/Supabase

---

## Stage 04 — Evidence Match
All core JD requirements matched STRONG. LangChain / Docker / Flutter = confirmed gaps, not claimed.
Evidence to foreground: FreeRTOS, I2S DMA, Opus, Deepgram Nova-3, Kubernetes Helm — all from evidence.md, previously absent from resume.

---

## Stage 05 — Positioning Strategy
Primary hook: "I built a wearable AI pendant from hardware to cloud — the same end-to-end stack Noise ships to millions."
Headline: AI Engineer · Wearable Systems · Full-Stack
Cut: Reliance + PES as named roles → collapsed to one summary line

---

## Stage 06 — Writer Notes
Evidence-first bullets applied:
- Aura bullet 1: FreeRTOS/I2S DMA/Opus/OTA sourced from evidence.md firmware section (NEW — was not in any prior resume)
- Aura bullet 2: Deepgram Nova-3 + Kubernetes Helm sourced from evidence.md infrastructure section (NEW)
- Aura bullet 3: CSS backdrop filter root cause detail sourced from evidence.md issue #8438 section (UPGRADED)
- Aura bullet 4: "SciPy cosine linkage" explicit from evidence.md (was "SciPy cosine linkage" already in facts.yaml ✓)
- Voice AI: John foregrounded first (Android companion app angle for Noise)
- Cover letter: hardware technical detail in paragraph 1 (FreeRTOS, I2S DMA, Opus, Kubernetes)

---

## Stage 07 — Factuality Audit
WARN: "sub-200ms latency targets" — removed (no source in evidence.md)
All other claims: PASS
Result: CLEAR after WARN resolution

---

## Stage 08 — ATS Review
Keyword coverage: Python ✓, TypeScript ✓, Kotlin ✓, React ✓, Node.js ✓, TensorFlow ✓, PyTorch ✓, RAG ✓, OpenAI ✓, REST APIs ✓, Git ✓
LangChain / Docker: absent (honest — not claimed)
Verdict: PASS

---

## Stage 09 — Final Editor Log
WARNs resolved: 1 (removed invented latency metric)
ATS fixes applied: none needed
Stop-slop removals: passive voice checked, em-dashes removed, pull-quotes removed, adverbs removed
Cover letter word count: ~230 words
Status: COMPLETE

---

Outputs:
- versions/startup/resume_noise.md
- applications/Noise_Eng_2026-09/cover_letter.md
