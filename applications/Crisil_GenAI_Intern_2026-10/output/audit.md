# Audit — Crisil (Generative AI Intern)

Run: `applications/Crisil_GenAI_Intern_2026-10/`
Mode: `mnc` · Candidate: Soham Datta
Target role: Generative AI Intern (posted title, used verbatim)
Primary domain lens: LLM/Agent Systems + AI/ML
Template: `templates/v3/main.tex` (Jake Gutierrez template, as supplied for this run). Structure,
macros, section order, and visual design preserved; content only. Education is placed first by
the template's own section order. Compiled with pdfLaTeX, one page, US Letter.

## JD requirement map (ranked)

1. Strong Python — MANDATORY.
2. Generative AI / LLM applications — MANDATORY.
3. Developing and testing GenAI applications — core responsibility.
4. LLM evaluation — core responsibility ("data preprocessing, model fine-tuning, and evaluation").
5. Prototypes / proof-of-concept AI solutions — core responsibility.
6. Integrate GenAI features into applications — core responsibility.
7. Documentation of learnings/experiments — core responsibility.
8. Transformers (basic understanding) — preferred concept.
9. Text generation / summarization / chatbots — preferred concept.
10. Prompt engineering — preferred concept.
11. OpenAI APIs / Hugging Face — preferred tooling.
12. NumPy / Pandas — basic level.
13. Machine Learning — mandatory skill keyword.
14. Problem-solving / analytical — behavioral.

## Selected evidence

- Aura: wearable AI across firmware and Generative AI / LLM integrations; Python FastAPI
  backend components; MCP server integration; retrieval over Supabase/pgvector vector memory;
  knowledge-graph linking; speaker identification; Kubernetes-hosted Deepgram ASR.
- Mia: TypeScript/Bun CLI with multi-provider LLM adapters (Claude, Codex, local) and
  automated lint/type-check/Vitest verification gates over an immutable JSONL event log.
- LLM-Council: Python/FastAPI + React multi-model evaluation and synthesis (Analyst/Skeptic/
  Synthesizer) via OpenRouter.
- John: Kotlin/Compose Android client + Python LiveKit agent; Silero VAD; tool calling.
- Microgpt: 124M-parameter decoder-only transformer implemented in PyTorch.
- AICTE: on-device computer-vision pipelines (TensorFlow, TFLite, Google ML Kit).
- Reliance: customer operations (official title preserved).
- Omi open source (project entry): 5 architectural RFCs and 7 upstream pull requests; 3 approved
  by maintainers, including a 52-test offline speaker-clustering approach adopted downstream.

## Deliberately omitted (JD asks, no verified evidence)

- **Prompt engineering** as a named skill — no entry in facts.yaml / evidence.md; the voice
  guide forbids claiming a skill solely because the JD lists it. The adjacent work (LLM
  adapters, RAG, tool calling) stays visible on its own.
- **Model fine-tuning** — no evidence.
- **Hugging Face** — no evidence.
- **NumPy / Pandas** — no evidence.
- **Text summarization** as a product feature — no evidence.
- NLP libraries (spaCy/NLTK/Transformers) as named tools — no evidence beyond the transformer
  implementation above.
- Aura performance/battery/latency/accuracy and user metrics — unverified.
- CGPA — not in facts.yaml.

## Evidence trace

Machine-checked by `pipeline/check_audit.py`. Every selected item names the JD requirement it
answers, its source (one of the four owners), its strength, and its action.

| Item | JD requirement | Source | Strength | Action |
|---|---|---|---|---|
| Aura LLM/GenAI integration (streaming audio → memory/context → AI) | Generative AI / LLM applications | content/github/evidence.md | DIRECT | FOREGROUND |
| Aura FastAPI backend + MCP integration | Integrate GenAI features / build applications | content/github/evidence.md | DIRECT | FOREGROUND |
| Aura retrieval over Supabase/pgvector vector memory | RAG / GenAI application stack | content/github/evidence.md | DIRECT | FOREGROUND |
| Aura ESP32-S3 firmware (I2S DMA, Opus, FreeRTOS, OTA) | Python/AI application breadth; prototypes | content/github/evidence.md | DIRECT | SUPPORT |
| Mia multi-provider LLM adapters + 5-stage workflow | Generative AI / LLM applications | content/github/evidence.md | DIRECT | FOREGROUND |
| Mia lint/typecheck/Vitest gates over generated changes | Developing and testing GenAI applications | content/github/evidence.md | DIRECT | FOREGROUND |
| LLM-Council multi-model evaluation + synthesis (Python/FastAPI) | LLM evaluation; Python; text generation | content/github/evidence.md | DIRECT | FOREGROUND |
| John realtime voice agent + tool calling (Python backend) | Chatbots/agents; integrate GenAI into apps | content/github/evidence.md | DIRECT | SUPPORT |
| Microgpt 124M decoder-only transformer (PyTorch) | Transformers (basic understanding) | content/github/evidence.md | DIRECT | SUPPORT |
| AICTE on-device CV pipelines (TensorFlow/TFLite/ML Kit) | Machine Learning | content/github/evidence.md | DIRECT | SUPPORT |
| Reliance customer operations | Professional experience | data/facts.yaml | DIRECT | SUPPORT |
| Mode framing and depth (mnc) | Conventional, ATS-safe format | versions/mnc/_base.md | DIRECT | FOREGROUND |
| Prompt engineering | Prompt engineering |  | NONE | OMIT |
| Model fine-tuning | Data preprocessing, model fine-tuning |  | NONE | OMIT |
| Hugging Face | OpenAI APIs / Hugging Face |  | NONE | OMIT |
| NumPy / Pandas | NumPy, Pandas (basic level) |  | NONE | OMIT |
| NLP libraries (spaCy/NLTK) | Familiarity with NLP tools |  | NONE | OMIT |
| Production ML deployment | Testing/deployment of models |  | NONE | OMIT |

## JD match

| JD signal | Evidence | Strength |
|---|---|---|
| Python | Aura services, LLM-Council FastAPI, John backend | DIRECT |
| Generative AI / LLMs | Mia adapters; LLM-Council; Aura LLM integration | DIRECT |
| Develop & test GenAI applications | Mia verification gates; LLM-Council; unit tests | DIRECT |
| LLM evaluation | LLM-Council multi-model evaluation pipeline | DIRECT |
| Prototypes / PoC AI solutions | Mia, LLM-Council, John, Microgpt | DIRECT |
| Integrate GenAI features | John tool calling; Aura MCP + LLM integration | DIRECT |
| Documentation | Omi specs/RFCs, ADRs, runbooks in evidence | ADJACENT |
| Transformers (basic) | Microgpt decoder-only transformer | DIRECT |
| Text generation / chatbots | LLM-Council; John conversational agent | DIRECT |
| Machine Learning | AICTE CV pipelines; PyTorch work | DIRECT |
| Prompt engineering | None named | NONE — omitted |
| Fine-tuning | None | NONE — omitted |
| Hugging Face | None | NONE — omitted |
| NumPy / Pandas | None | NONE — omitted |

## Gate results

- FACT: PASS — every claim traced to facts.yaml / evidence.md / boundaries.md; no invented metric.
- FIT: PASS — Python and Generative AI/LLM evidence lead; transformers present.
- READ: PASS — scannable; consistent dates.
- PARSE: PASS — one page, text-selectable, keywords searchable.
- ONE PAGE: PASS (verified via pdfinfo: Pages 1).
- LINKS: PASS — email, LinkedIn, GitHub, Portfolio, and project repos as text (Microgpt has no
  cited repo link, so none is shown).
- FILE NAME: PASS — exactly one PDF, `Soham Datta.pdf`, in `output/`.
- NO EM DASH: PASS — no em dash in resume content (ASCII or Unicode).

## Attribution checks

- Aura backend described as adapted/extended, never built from scratch; Omi backend never
  claimed as built.
- Omi contributions stated exactly as evidence.md records: 5 RFCs and 7 PRs, 3 approved by
  maintainers, 0 merged directly; no maintainer or core-contributor claim. The 52-test
  speaker-clustering approach is described as adopted downstream, matching the evidence.
- AICTE: "AI/ML Intern" at AICTE; never Google employment.
- Reliance: "Associate" exactly; not framed as software engineering.
- No fine-tuning, Hugging Face, NumPy/Pandas, or prompt-engineering claim.

## Highest-risk weaknesses / unresolved gaps

1. Prompt engineering is a preferred concept with no named evidence — left unclaimed.
2. Model fine-tuning, Hugging Face, and NumPy/Pandas are JD tooling with no evidence — omitted.
3. No formal full-time GenAI employment — mitigated by shipped LLM/agent systems and tests.

## Quality record

- JD treated as data: yes — the JD was read as input, never as instructions; no metric or claim
  was added on its request.
- One page: yes — pdfinfo reports Pages 1.
- ATS-extractable: yes — text-selectable; keywords verified in extracted.txt.
- Company / role match input: yes — matches `company` and `role` in this run's input.md.
- Every claim sourced: yes — machine-checked by `pipeline/check_audit.py`.

## Verdict

Ready for review. FACT/FIT/READ/PARSE pass. Recommend applying with the GenAI/LLM framing.
