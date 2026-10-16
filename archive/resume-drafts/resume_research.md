# Resume Research Corpus: Engineering, AI Systems, Voice, Wearables, and Startups

## Executive Summary

This research corpus synthesizes evidence from Tier 1 universities (MIT, Stanford, Harvard, Yale, CMU, UC Berkeley, Princeton, Oxford, Cambridge), official tech hiring frameworks (Google, Amazon, Y Combinator), engineering leaders (Gergely Orosz, Dan Luu, Shawn "Swyx" Wang), and empirical technical recruiting data.

The goal is to provide a comprehensive, source-backed foundation for constructing three distinct resume variants for early-career AI / software builders:
1. **MNC / Large Tech (ATS-First):** Single-column, standard headings, Google XYZ bullet formula, defensible technical keywords, clean parsing.
2. **Early-Stage AI / Wearable Startups:** Founder-readable, high visual and cognitive hierarchy, demonstrating intentional cross-stack breadth (hardware → firmware → voice → agents → UI), ownership, and bias for shipping.
3. **Mid-Level Product Companies:** Clean, modern, conventional single-column structure balancing technical depth with product-oriented engineering narratives.

---

## What Excellent Resumes Have in Common

Across academic career centers and elite technical hiring teams, exceptional engineering resumes share five fundamental traits:

1. **Concrete Deliverables Over Responsibilities:** Strong candidates describe what they *built*, *measured*, and *shipped*, not their job descriptions or aspirational goals.
2. **Cognitive Scannability (<15-Second Rule):** Engineering managers and founders scan resumes in 10 to 30 seconds. Strong resumes use clear typography, standard section titles, and front-loaded bullet points.
3. **Defensible Technical Specificity:** Technologies are named in direct relation to system components (e.g., *"Configured I2S DMA buffers in C++"* vs. *"Experienced in C++"*).
4. **Active, High-Signal Verbs:** Every bullet begins with an unambiguous action verb (*Built, Designed, Integrated, Measured, Debugged*) rather than passive or inflated phrasing (*Assisted with, Spearheaded, Leveraged*).
5. **Calibrated Scope & Honesty:** Top candidates clearly differentiate between what they authored from scratch, what they adapted from open source, and what was inherited from existing infrastructure.

---

## MNC / ATS Research

### Empirical ATS Facts vs. Myths
- **Myth:** "ATS automatically rejects resumes without an 80% keyword match."
  - **Fact:** Modern ATS platforms (Greenhouse, Lever, Workday, Taleo) primarily act as candidate databases and parsing engines. Resumes are parsed into fields for human recruiters and hiring managers to review and filter.
- **Myth:** "Tables, columns, and graphics get resumes instantly disqualified."
  - **Fact:** While ATS parsers can ingest PDFs, complex multi-column tables and text boxes frequently scramble reading order. Single-column layouts consistently achieve 100% parse accuracy across all engines.
- **Myth:** "White-text keyword stuffing tricks the ATS."
  - **Fact:** Modern parsers strip formatting and display raw plain text to the recruiter; hidden text appears as unformatted spam, triggering immediate rejection.

### ATS Best Practices
- **File Format:** PDF generated from clean LaTeX or text documents is standard. Ensure text is selectable (not rasterized images).
- **Layout:** Strict single-column layout without sidebars, text boxes, or floating elements.
- **Standard Headings:** Use canonical headers: `Education`, `Experience`, `Projects`, `Technical Skills`.
- **Contact Details:** Plain text at the top: Name, Email, Phone, Location (City, State/Country), LinkedIn, GitHub, Portfolio URL. Avoid placing contact info inside headers/footers.

---

## Startup Hiring Research

### What Founders and Early Engineering Teams Value
1. **End-to-End Ownership:** Founders look for engineers who can take an ambiguous problem from hardware/concept to a deployed, usable artifact without hand-holding.
2. **Bias for Action & Velocity:** Evidence of building, deploying prototypes, testing with real users, and rapidly iterating.
3. **Intentional Breadth:** A generalist who understands how embedded firmware, WebRTC streams, backend APIs, and frontend interfaces connect is 10x more valuable in early stages than a siloed specialist.
4. **Open-Source Footprint:** Verifiable pull requests, issue triage, and upstream bug discoveries provide immediate proof of technical competence.

### Red Flags for Startup Founders
- Corporate jargon, buzzwords, and vague metrics with no methodology.
- Resumes that read like a passive checklist of tools rather than a record of things shipped.
- Inflated titles (e.g., claiming to be CTO of an unlaunched class project).

---

## AI Engineering Hiring Research

Based on Swyx's *AI Engineer* taxonomy and hiring patterns at applied AI companies:
- **Core Focus:** Bridging the gap between raw foundation models and reliable user-facing software.
- **Key Competencies:** Context window management, prompt engineering & evaluation harnesses, semantic caching, vector retrieval (RAG), structured JSON outputs, latency optimization, and tool/function calling.
- **Signals Valued:** Evaluation frameworks, handling edge cases, deterministic fallback mechanisms, and cost/token monitoring.

---

## Agentic AI Hiring Research

- **Core Focus:** Autonomous multi-step execution loops, memory graphs, state machines, and code execution environments.
- **Key Technical Signals:**
  - Dynamic tool calling and schema definition (e.g., Model Context Protocol / MCP).
  - Human-in-the-loop safety gates, rollback mechanisms, and execution sandboxes.
  - Socratic interview / constraint extraction workflows prior to code generation.
  - Rejection of fragile infinite loops in favor of structured DAG execution.

---

## Voice AI / Speech Hiring Research

Synthesized from hiring criteria at ElevenLabs, Deepgram, Cartesia, and AssemblyAI:
- **Key Technical Competencies:**
  - **WebRTC & Real-Time Audio:** Bidirectional streaming, room orchestration, jitter buffer handling.
  - **Latency Optimization:** End-to-end voice-to-voice latency reduction (<500ms target), streaming STT/TTS chunking.
  - **Voice Activity Detection (VAD) & Barge-In:** Client-side interruption handling (Silero VAD) to allow natural conversational turn-taking.
  - **Audio Formats & Codecs:** Opus compression, 16kHz 16-bit PCM streaming, I2S microphone sampling.

---

## Wearable / Hardware + AI Hiring Research

- **Core Competencies:** Edge microcontrollers (ESP32-S3, ARM Cortex), FreeRTOS task scheduling, DMA buffers, low-power BLE/Wi-Fi states, 3D CAD modeling (STL/STEP), and thermal/enclosure constraints.
- **Key Project Signals:**
  - Demonstrating the complete hardware-to-cloud loop: physical microphone → on-device Opus compression → socket streaming → ASR/LLM inference → memory persistence.
  - Prototyping physical enclosures tailored to human ergonomics.

---

## Fresher / New Graduate Research

- **Section Hierarchy:** `Education` and `Technical Skills` or `Featured Projects` should appear near the top if formal work history is limited.
- **Projects as Primary Evidence:** Substantial, end-to-end technical projects with live links, source code, and architectural documentation substitute for years of commercial experience.
- **Avoid "Academic Toy" Traps:** Frame coursework and internships around production practices: automated testing, CI/CD, modular architecture, and edge-case handling.

---

## University Guidance

| Institution | Bullet Formula & Philosophy | Layout & Length | Project Guidance |
|---|---|---|---|
| **MIT** | Action Verb + Technical Task + Measured Result | 1 Page; tight margins (0.5–0.75"); single column | Emphasize hardware/software builds, lab research, and quantifiable performance gains |
| **Harvard** | Action Verb + Context + Result (No personal pronouns) | 1 Page; standard serif/sans-serif fonts; clean hierarchy | Focus on scope of responsibility, analytical depth, and clear outcomes |
| **Yale** | Concise, high-density bullets; eliminate fluff | 1 Page; standard section titles | Highlight technical stack and real-world applicability |
| **Stanford** | System architecture + implementation details | 1 Page; clean whitespace balance | Group by project domain (AI, Systems, Web); link to public code |
| **CMU** | Technology tags per project; algorithmic & systems rigor | 1 Page; highly technical scannability | Detail data structures, latency, hardware interfaces, and ML frameworks |
| **UC Berkeley** | Direct ATS compatibility; clear engineering deliverables | 1 Page; ATS-safe single column | Focus on software engineering fundamentals, Git workflows, and open-source contributions |
| **Princeton** | Structured chronological format; verified evidence | 1 Page; conservative styling | Clear delineation between research, internships, and extracurricular engineering |
| **Oxford / Cambridge** | Rigorous technical accuracy; factual understatements | 1–2 Pages (UK/EU standard; 1 page for US/Global tech) | Academic rigor, mathematical foundations, and concrete system implementations |

---

## Anti-AI-Slop Writing Research

### Banned AI Slop Words vs. Strong Engineering Verbs
| Banned Buzzword / AI Slop | Why It Fails | Preferred Engineering Verb | Concrete Example |
|---|---|---|---|
| *Spearheaded* | Overused corporate cliché; masks actual technical contribution | **Built / Led / Designed** | *Designed 3D-printed pendant enclosure in CAD* |
| *Leveraged* | Passive tool-dropping; implies effortless integration | **Integrated / Configured / Implemented** | *Configured I2S DMA buffers for 16kHz audio capture* |
| *Innovative / Cutting-Edge* | Subjective self-praise; conveys zero technical information | **[Omit and describe the mechanism]** | *Implemented offline agglomerative clustering for speaker diarization* |
| *Passionate / Results-Driven* | Empty resume filler; adds no credibility | **[Omit completely]** | *Shipped native Android client with LiveKit voice agent* |
| *Transformative* | Unverifiable hyperbole | **Tested / Measured / Reduced** | *Reduced audio packet payload by 70% using on-device Opus compression* |

---

## Metrics & Evidence Guidelines

1. **Use Metrics ONLY When Methodologically Defensible:**
   - **Good:** *"Reduced audio stream bandwidth by ~70% via on-device Opus encoding."* (Defensible calculation based on PCM vs. Opus bitrates).
   - **Weak:** *"Improved model accuracy significantly."* (Vague, lacks baseline).
   - **Dangerous / Unverified:** *"Achieved 95% accuracy and 50% efficiency gain."* (Red flag unless dataset, baseline, and evaluation methodology are explicitly stated).
2. **Qualitative Technical Outcomes Are Stronger Than Invented Metrics:**
   - Describe architectural trade-offs, bug fixes, or solved edge cases rather than inventing artificial percentages.

---

## Technical Depth vs. Breadth

For generalist builders across hardware, firmware, AI, and frontend:
- **Frame as Intentional Integration, Not Accidental Chaos:** Position breadth as the ability to design and deliver full-stack products from physical enclosure to cloud intelligence.
- **Anchor with Verifiable Depth in Key Modules:** Prove depth through specific low-level details (e.g., FreeRTOS task loops, WebRTC interruption handling, ADR architectural decisions) while demonstrating end-to-end integration.

---

## MNC vs. Startup vs. Mid-Level Comparison

| Dimension | MNC / Large Tech (1) | Startup / Wearables (2) | Mid-Level Product (3) |
|---|---|---|---|
| **Target Role** | AI Engineer, SWE, ML Engineer | Founding AI/Wearable Engineer, Generalist Builder | AI/Software Engineer |
| **Layout** | ATS-first single-column (LaTeX/DOCX) | Modern, compact, founder-readable (Enji-style hierarchy) | Clean, modern single-column |
| **Core Signal** | Technical rigor, standard frameworks, ATS keywords | Velocity, end-to-end ownership, product instinct | Solid engineering practices, clean code, teamwork |
| **Project Emphasis** | Scalability, ML pipelines, edge deployment | Aura hardware/firmware, Mia agent loop, voice agents | System reliability, modular design, full-stack flow |
| **Tone** | Objective, technical, standardized | Direct, human, understated, founder-level | Professional, balanced, clear |

---

## Critique of User's Resume History & Strategy

### Strengths
1. **Exceptional Multimodal Builder Footprint:** Demonstrable hardware CAD, ESP32 firmware, real-time WebRTC audio pipelines, and TypeScript agent harnesses.
2. **Verified Open-Source Impact:** Genuine contributions to upstream Omi (`BasedHardware/omi`), including GPU memory leak diagnosis and speaker diarization PRs.
3. **Commitment to Credibility:** Deliberate decision to strip inflated legacy metrics and avoid corporate buzzwords.

### Weaknesses & Traps to Avoid
1. **Backend Exaggeration Risk:** Aura's backend inherits heavily from upstream Omi. Do not claim deep distributed backend architecture; frame as cloud integration and pipeline customization.
2. **Tool-Listing Trap:** Listing 20+ AI frameworks creates the impression of a surface-level wrapper engineer. Group technologies strictly by functional domain.
3. **Legacy Experience Distraction:** Non-technical past roles (Reliance retail, PES library assistant) take up valuable space and should be reduced to 1 concise line each or omitted.

---

## High-Confidence Recommendations

1. **Adopt Google XYZ Bullet Structure:** Frame every bullet around concrete technical action and tangible system behavior.
2. **Lock the Startup Resume Layout:** Use a high-density, compact structure inspired by the Enji Kusnadi layout (left section labels, right content, clean tag hierarchy).
3. **Emphasize Verifiable Upstream Contributions:** Explicitly highlight Omi PRs and technical discoveries (#8438 GPU fix, #8919 diarization) under Experience/Open-Source.
4. **Maintain Three Distinct Variants:** Keep MNC ATS-safe, Startup founder-focused, and Mid-Level balanced.