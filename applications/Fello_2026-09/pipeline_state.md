# Pipeline State — Fello — 2026-09-15
Track: startup
Input: applications/Fello_2026-09/input.md

---

## Stage 01 — Company Research
COMPLETED — see research/companies/Fello.md

## Stage 02 — JD Signals

### Required (explicit in JD — must have match)
- Strong software engineering ability, ship working systems quickly
- Hands-on experience building with modern LLMs (OpenAI, Anthropic, open models)
- Experience building AI agents, copilots, or automated workflows
- Strong prompt engineering skills, structured prompting and reliability
- Experience integrating APIs, webhooks, and external systems
- Ability to work with structured and unstructured data
- Experience with automation tools (N8N, Make, Zapier or similar)
- Web scraping, enrichment systems, and data pipelines
- Strong builder mindset, learn fast, experiment fast, ship fast
- High agency, figure things out independently

### Preferred (nice-to-have — include if honest match)
- Experience with vector databases, embeddings, retrieval systems
- Experience building multi-step agent workflows
- Actively build AI projects outside of work
- Use AI coding tools as part of daily workflow

### Role archetype
AI-native builder — autonomous agent specialist focused on internal GTM tooling (not customer product)

### ATS keywords (verbatim from JD)
- AI agents, copilots, autonomous systems
- LLM, tool use, function calling, structured outputs, multi-step reasoning
- RAG, retrieval systems, embeddings, vector databases
- FastAPI, Python
- HubSpot integrations
- Web scraping, data pipelines, enrichment
- Automation workflows
- Prompt engineering
- High agency

### Deprioritize (in JD but low-signal for this candidate)
- N8N/Make/Zapier experience (have automation via code, not these specific tools)
- Real estate domain knowledge (not required, AI skills are what matters)

### Gaps flagged
| JD Requirement | Gap | How to handle |
|---|---|---|
| N8N/Make/Zapier experience | No direct experience with these specific tools | Frame as "automation frameworks" — have built custom Python automation, FastAPI workflows, and agentic pipelines; the underlying concepts (webhooks, API orchestration, triggers) are identical |
| HubSpot integration | No prior HubSpot work | Frame as eagerness to learn; have integrated multiple external APIs (Deepgram, OpenAI, Anthropic, LiveKit); HubSpot is just another REST API with webhooks |

## Stage 03 — Candidate Inventory

### Strongest evidence (verifiable — GitHub repo, file path, or named artifact exists)
| Project | Evidence | Type |
|---|---|---|
| Aura | FastAPI routers for transcription, memories, knowledge_graph, speech_profile, MCP server (backend/routers/*.py) | AI/ML |
| Aura | Autonomous speaker clustering: SciPy agglomerative clustering, 52 unit tests (PR #8919, adopted in #12471) | Algorithm |
| Aura | Multi-step workflow: threaded user_name into action-item extraction (Issue #8918, adopted in PR #12089) | AI/ML |
| Aura | Self-hosted Deepgram Nova-3 ASR Kubernetes Helm charts, pgvector migrations | AI/ML |
| Aura | FreeRTOS I2S DMA audio capture at 16kHz (firmware/src/mic.cpp), Opus compression | Firmware/Embedded |
| Mia | 5-stage AI engineering harness (grill→spec→plan→review→ship) compiled TypeScript CLI | AI/ML |
| Mia | Unified host adapters for Anthropic Claude, OpenAI Codex, local models (core/hosts/registry.ts) | AI/ML |
| Mia | Immutable JSONL state tracking, automated verification gates (Vitest) | Full-Stack |
| LLM-Council | Multi-LLM consensus engine querying OpenAI, Anthropic, Gemini, Groq concurrently | AI/ML |
| LLM-Council | 3-stage critique pipeline (Analyst→Skeptic→Synthesizer) with React frontend | AI/ML |
| Voice AI (John) | LiveKit WebRTC Python agent with tool calling (calendar, tasks, telephony) — tools/*.py | AI/ML |
| Voice AI (John) | Native Kotlin Android app (Jetpack Compose) with LiveKit SDK integration | Mobile |
| Voice AI (voicecoder) | VS Code extension with multi-provider fallback (Claude, GPT-4o, Gemini, Ollama), token cost tracking | AI/ML |
| Omi contributions | 21 issues authored (9 open, 12 closed), 5 architectural RFCs, 120+ unit tests authored | Open Source |
| Omi contributions | GPU memory leak diagnosis (Issue #8438, merged in PR #8902) | Open Source |
| Omi contributions | Windows file indexing spec (Issue #8991, delivered in PRs #7896/#9595/#10236) | Open Source |

### Secondary evidence (real but lighter)
| Project | Evidence | Type |
|---|---|---|
| AutoDev-Studio | Autonomous multi-agent framework with role-partitioned agents (Planner, Coder, Reviewer) | AI/ML |
| codeshot | Moondream 2B Vision Language Model (PyTorch) for code extraction from screenshots | AI/ML |
| DDPM-Diffusion | Denoising Diffusion Probabilistic Models from scratch (UNet, beta schedules, reverse sampling) | AI/ML |
| Microgpt124M | 124M-parameter decoder-only transformer (multi-head attention, rotary embeddings) | AI/ML |

### Hard boundaries (NEVER claim — from boundaries.md)
- Aura: self-funded, no customers/revenue yet, not VC-backed
- Aura backend: adapted from Omi ecosystem — claim "integrated/adapted/extended," NOT "architected from scratch"
- Omi PRs: 0 merged directly into main (7 closed unmerged); downstream adoption counts but never claim "merged"
- Omi PR #8352: received changes-requested, NOT approved
- Omi forks: do NOT claim authorship of forked repos

### Track-specific notes
- Startup track appropriate: Fello is VC-backed, hyper-growth, B2B SaaS
- Emphasize speed of shipping, autonomous building, high agency
- Frame as AI-native builder who thinks in systems
- Highlight open-source contributions as proof of real-world impact

---

## Stage 04 — Evidence Match

### High-signal matches (JD requirement ↔ verifiable evidence)
| JD Requirement | Evidence item | Strength | Evidence type |
|---|---|---|---|
| Build AI agents, copilots, autonomous systems | Aura: FastAPI routers (transcription, memories, knowledge_graph, MCP server) | STRONG | AI/ML |
| Multi-step reasoning, autonomous workflows | Aura: speaker grounding workflow (Issue #8918 → PR #12089 adopted) | STRONG | AI/ML |
| Multi-step reasoning, autonomous workflows | Mia: 5-stage harness (grill→spec→plan→review→ship) | STRONG | AI/ML |
| Tool use, function calling | Voice AI (John): Python LiveKit agent with tool calling (calendar, tasks, telephony) | STRONG | AI/ML |
| Retrieval systems, RAG, embeddings, vector databases | Aura: pgvector migrations, memory retrieval system | STRONG | AI/ML |
| Integrating APIs, webhooks, external systems | Mia: Unified host adapters (Anthropic Claude, OpenAI Codex, local models) | STRONG | AI/ML |
| Integrating APIs, webhooks, external systems | Aura: Deepgram Nova-3 ASR integration, Kubernetes Helm charts | STRONG | AI/ML |
| Strong prompt engineering, structured outputs | LLM-Council: 3-stage critique pipeline (Analyst→Skeptic→Synthesizer) | STRONG | AI/ML |
| Ship working systems quickly | Mia: compiled TypeScript CLI (single Bun binary) | STRONG | Full-Stack |
| Work with structured and unstructured data | Aura: autonomous speaker clustering (SciPy agglomerative, 52 tests) | STRONG | Algorithm |
| Rapidly prototype, test, deploy | Multiple projects shipped (Aura, Mia, LLM-Council, John, voicecoder) | STRONG | AI/ML |
| Build reusable frameworks, agent architectures | Mia: immutable JSONL state tracking, verification gates (Vitest) | STRONG | Full-Stack |
| Experience with modern LLMs (OpenAI, Anthropic) | LLM-Council: concurrent queries to OpenAI, Anthropic, Gemini, Groq | STRONG | AI/ML |
| Actively build AI projects outside of work | 21 Omi issues authored, 5 architectural RFCs, 120+ tests | STRONG | Open Source |
| Use AI coding tools daily | voicecoder: VS Code extension with multi-provider fallback | STRONG | AI/ML |

### Moderate matches (real but less specific to JD phrasing)
| JD Requirement | Evidence item | Strength |
|---|---|---|
| Design and deploy autonomous agents | AutoDev-Studio: multi-agent framework (Planner, Coder, Reviewer) | MODERATE |
| Web scraping, data pipelines | codeshot: Moondream VLM for code extraction from screenshots | MODERATE |
| Continuously improve agents | Omi: GPU leak diagnosis (Issue #8438), file indexing spec (Issue #8991) | MODERATE |
| Own systems end-to-end | Aura: hardware (ESP32) + firmware + backend + infrastructure | MODERATE |

### Confirmed gaps
| JD Requirement | Gap status | Interview framing |
|---|---|---|
| N8N/Make/Zapier experience | No direct tool experience | "I've built automation via code — FastAPI workflows, Python scripts, agentic pipelines. The underlying concepts (webhooks, API orchestration, event triggers) are identical to N8N/Make. I'm eager to learn these specific tools if they're part of your stack." |
| HubSpot integration | No prior HubSpot work | "I haven't worked with HubSpot specifically, but I've integrated multiple external APIs (Deepgram, OpenAI, Anthropic, LiveKit). HubSpot's REST API and webhooks follow the same patterns. Eager to dive in." |
| Real estate domain | No real estate experience | "Real estate domain is new to me, but the AI engineering skills — agents, tool calling, retrieval systems — are exactly what you need. I learn domains quickly by building." |

### Evidence to suppress (real but low-relevance to this role)
- Firmware/embedded work (ESP32, FreeRTOS) — not relevant to GTM internal tooling
- Hardware prototyping (3D CAD, wearable packaging) — not relevant
- Mobile development (Android Kotlin) — not relevant to this role
- Academic internship details — keep lightweight

---

## Stage 05 — Positioning Strategy

### Primary hook
I build autonomous AI agents that execute real business workflows — my Aura backend handles multi-step reasoning (speaker grounding, context extraction), my Mia harness orchestrates 5-stage agentic pipelines, and my LLM-Council implements cross-model consensus systems, exactly the kind of internal GTM tooling that powers Fello's revenue operations.

### Secondary angles (2–3 max)
- RAG/retrieval systems experience: built pgvector memory retrieval for Aura, integrated Deepgram ASR and multiple LLM providers
- Open-source proof of real-world impact: 21 Omi issues authored, 5 architectural RFCs, downstream adoption of speaker clustering and workflow automation
- AI-native builder mindset: ship fast, learn new tooling weekly, think in systems not scripts

### Track confirmed
startup — Fello is VC-backed, hyper-growth, B2B SaaS; startup track emphasizes speed, autonomy, high agency

### Headline for this role
AI Engineer · Autonomous Agents · Multi-LLM Orchestration · Internal Tooling

### Cover letter structure
1. Opening: "I build autonomous AI agents that execute real business workflows. My backend systems handle multi-step reasoning, tool calling, and retrieval — exactly the kind of internal GTM tooling that powers revenue operations at scale."
2. Body 1: Aura + Mia evidence — FastAPI backends with memory graphs, 5-stage agentic harness, multi-LLM orchestration (LLM-Council)
3. Body 2: Breadth — API integrations (Deepgram, Anthropic, OpenAI), open-source contributions (Omi ecosystem), rapid prototyping across voice agents, VS Code extensions, multi-agent frameworks
4. Close: "I'd love to build the AI systems that make Fello's sales and ops teams more efficient. Let's talk."

### What to cut from base resume
- Hardware/firmware details (ESP32, FreeRTOS, 3D CAD) — not relevant to GTM internal tooling
- Mobile app details (Android Kotlin Jetpack Compose) — not relevant
- Academic internship lightweight (AICTE via Google) — one line max
- Reliance retail job — remove entirely
- PES research assistant — remove entirely

### What to foreground (from evidence — not currently in base resume)
- FastAPI routers: transcription, memories, knowledge_graph, MCP server (backend/routers/*.py)
- Multi-step workflow: speaker grounding (Issue #8918 → PR #12089)
- Windows file indexing spec (Issue #8991, delivered in PRs #7896/#9595/#10236)
- 120+ unit tests authored across projects
- Concurrent multi-LLM queries in LLM-Council
- Tool calling in John (calendar, tasks, telephony)
- Kubernetes Helm charts for Deepgram ASR
- VS Code extension with token cost tracking

---

