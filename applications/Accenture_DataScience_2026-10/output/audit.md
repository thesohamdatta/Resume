# Audit — Accenture Decision Science Associate (R00361602)

Mode: `mnc` · Lens: LLM / Agent Systems (Generative AI, RAG, agent workflows) · Depth: D2, D3 on RAG/agents/testing
Output: `resume.pdf` (1 page, A4) · `Soham_Datta_Accenture_Decision_Science_Associate.pdf` · `extracted.txt`
Content corrections applied 2026-10-08: Reliance title = **Associate**; internship shown as **AICTE** (no platform provider
named); Aura role = **Founder** (no "Builder"); Aura dates = **Jun 2026 – Present**. Explicit target line removed on request.
AI-pattern pass applied (stop-slop + docs/voice.md): removed rule-of-three lists, "local-first"/"LLM-powered" marketing
suffixes, repeated "Built" openers, em dashes, passive "is gated by", and the adverb "Recently"; varied sentence rhythm.
Summary rewritten to DONT.MD §E5 (S3): states specialization (generative AI / LLM systems), the supporting evidence
(two built systems + an independent wearable AI project), and the target domain (entry-level decision science / applied
generative AI), while staying within the evidence on the page (S4).

## Target role interpretation

Entry-level (0–2 yrs) GenAI/decision-science practitioner. Support: LLM apps via prompts/APIs/frameworks; RAG knowledge
retrieval; conversational AI + agent workflows; functional testing of AI outputs; Azure/AWS AI services; Python + API
integration; Git/standard dev practice; docs, testing, troubleshooting, deployment support.

## Evidence plan (JD requirement → evidence → strength → action)

| JD requirement | Evidence (verified) | Strength | Action |
|---|---|---|---|
| Generative AI / LLM applications | Mia (multi-host LLM adapters, 5-stage harness); LLM-Council; John (LiveKit agent) | DIRECT | Foreground |
| RAG / knowledge retrieval | Aura: memory/context segmentation, knowledge-graph entity/relationship linking, Supabase/pgvector vector memory | DIRECT | Foreground |
| Prompt engineering | LLM-Council multi-model evaluation; Mia prompt-driven harness | DIRECT | Foreground (skills + bullets) |
| Agentic AI / tool calling / workflows | John tool-calling agent; Mia agentic harness; AutoDev-Studio (multi-agent) | DIRECT | Foreground |
| APIs / Python | Aura FastAPI services; John Python agent; LLM-Council FastAPI | DIRECT | Foreground |
| Functional testing / validation of AI outputs | Mia automated lint/typecheck/Vitest gates; Omi 120+ documented tests (52 speaker-clustering) | DIRECT | Foreground (Mia bullet, skills) |
| ML fundamentals | AICTE internship (TensorFlow, TFLite, ML Kit); PyTorch projects (DDPM, Microgpt) | DIRECT | Support |
| Git / development practice | Repo links, Vitest, documented Omi contribution workflow | DIRECT | Support (skills) |
| Cloud AI platforms (Azure/AWS) | AWS Educate: Introduction to Generative AI (verified cert) | ADJACENT | Support (certifications); no platform-depth claim |
| SQL | No verifiable SQL evidence in facts/evidence | NONE | Omit |
| LangChain / LangGraph | Uses model adapters + OpenRouter, not LangChain | NONE | Omit (no false claim) |
| Docker / CI-CD | No verified evidence | NONE | Omit |
| Conversational AI | John (Android voice client + Python LiveKit agent) | DIRECT | Foreground |

## What was foregrounded / compressed / omitted

- **Foreground:** GenAI/RAG/agent evidence (Mia, LLM-Council, John, Aura retrieval pipeline).
- **Compressed:** ESP32-S3 firmware → one supporting bullet inside Aura (embedded is secondary to this JD).
- **Compressed:** Reliance and PES roles → one-line entries (no bullet) to preserve space and honest scope.
- **Omitted:** codeshot, AutoDev-Studio, DDPM, Microgpt, voicecoder (weaker/same-signal than the selected projects).
- **Omitted:** SQL, Docker/CI-CD, LangChain/LangGraph (no evidence).

## Vertical check — one page

- Projects section prioritized GenAI depth (Mia, LLM-Council, John) over breadth.
- Reliance/PES collapsed to compact one-liners.
- Skill groups consolidated; embedded/system specifics kept to one line.

## Gate status

| Gate | Result | Note |
|---|---|---|
| FACT | PASS | Every claim traces to facts.yaml / evidence.md / boundaries.md. Aura = "under development"; Omi attribution not used on the resume (no overreach). |
| FIT | PASS | Headline, summary, first experience bullets, and top projects all serve the GenAI/RAG/agent lens the JD names. |
| READ | PASS | Role → impact visible in the first 5–15 seconds (headline + summary + Aura retrieval bullet). |
| PARSE | PASS | Single column, standard headings, selectable text, 32 KB, links preserved as text. |
| ONE PAGE | PASS | `pdfinfo` → Pages: 1 (A4). |

## Unsupported-claim audit (negative checks)

- No invented metrics, ownership, production status, users, funding, or certification status.
- Aura not described as production or "built from scratch"; Omi backend described as adapted.
- No claim of SQL, LangChain, Docker, or cloud-platform depth.
- Certifications limited to the three verified in `facts.yaml`.
- Website/portfolio titled "Portfolio" (no current employer claimed).

## Highest-risk weaknesses

1. **Cloud platform depth** is absent (only an AWS Educate GenAI intro cert). Interviewers may probe Azure/AWS; answer from the cert + any real usage, not from the resume.
2. **SQL** is a listed must-have with no evidence. Genuine gap.
3. **LangChain/LangGraph** exposure — candidate's agent work uses adapters/OpenRouter; if probed, frame honestly as equivalent concepts, not LangChain experience.
4. Experience depth skews to a personal project (Aura) plus open-curriculum internship. Reliance is non-technical; kept honest and compact.

## Recommendation

Keep, cut, strengthen:
- **Keep:** the GenAI/RAG/agent framing, Aura retrieval bullet, Mia/LLM-Council/John projects.
- **Cut (already):** SQL/LangChain/Docker claims; extra low-signal projects.
- **Strengthen later if evidence appears:** a SQL artifact, an Azure/AWS deployment, or a LangChain/LangGraph build would materially raise fit.
