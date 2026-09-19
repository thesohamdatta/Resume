# CONTEXT.md — Resume Workspace (Soham Datta)

Primary working folder for building and maintaining resumes. Single factual master profile, three output tracks.

**Single source of truth for biographical facts:** `data/facts.yaml` — all dates, titles, companies, links, and bullets live there.

## Tracks

**Track** = presentation variant (same biographical facts, different layout/tone/bullet formulas for different audiences). Three tracks:

- **startup**: Founder-readable, minimal/editorial, one page. Targets: NeoSapien, Omi, Bengaluru early-stage AI/wearable startups. Hero: Aura. Proof: Mia + Voice AI. Bullet formula (voice.md): Action + What Built + Stack + Verifiable Outcome.
- **mnc**: ATS-first, single-column, conventional headings. Targets: AI Engineer, Software Engineer, Agentic AI, Voice AI, ML. Plain PDF. Bullet formula (voice.md): Action + Outcome/Metric + Technology + Context.
- **midlevel**: Same facts as MNC, cleaner modern presentation, less stylized than startup. Bullet formula (voice.md): Context + Action + Outcome + Growth.

## Domain terms

**Knowledge sources (three distinct purposes):**
- **Biographical facts** (`data/facts.yaml`): dates, titles, companies, education, certifications — skeleton that goes on every resume regardless of role.
- **Technical proof** (`content/github/evidence.md`): file paths, function names, algorithms, PR numbers, test counts — deep technical detail used to write evidence-rich bullets.
- **Constraints** (`content/github/boundaries.md`): negative rules — what NOT to claim (e.g., "never say 'built Omi backend from scratch'").

**Decision rule**: Date or title → facts.yaml. Technical depth → evidence.md. "Don't claim X" → boundaries.md.

Domain-specific context:

- **Aura | Founder**: Independent self-funded wearable AI pendant effort across hardware, software, backend. Owns enclosure/form-factor iteration, device+AI+backend integration software, frontend/design contribution to Omi ecosystem. Not VC-funded, no customers/revenue claimed. Backend depth developing — do not overstate.
- **Mia**: Personal agent system (TypeScript CLI/harness) using context, tools, code execution, orchestration. Repo: `thesohamdatta/Mia`. Do not call it AGI.
- **I-am-Mia**: Separate Python LiveKit real-time voice agent. Do not conflate with Mia.
- **Voice AI Agents**: Experiments with LiveKit, ElevenLabs, Gemini Live, Deepgram. Focus: natural personal-assistant interaction.
- **Omi contribution**: Frontend/design work, issues/PRs in `BasedHardware/omi`. Mention inside Aura only, never as separate experience. All 7 authored PRs were closed unmerged; 3 approved. Downstream merges by others (e.g. PR #8902 GPU fix, PR #12471 diarization, PR #12089 grounding, PR #12927 markdown export) are not direct authorship.
- **LLM-Council**: Multi-LLM compare/critique/synthesize system. Supporting project, MNC track.
- **PES Modern College / PS Modern Institute — Research Assistant**: Researched literature, digital learning platforms, open courseware, free coding resources, research repositories such as arXiv, books, articles, and the college's own digital archive. Helped students discover and use resources across computer science, healthcare, mechanical engineering, electrical engineering, and related domains through guidance, workshops, and digital-awareness campaigns. Do not claim ownership of platforms/archive or unverified audience or outcome metrics.
- **Positioning**: AI Engineer · Personal AI · Wearable Systems. Story: built wearable system → built agent system → works across software/AI/hardware/product.

## Writing rules

Short, direct, factual, understated. Concrete verbs. Never invent metrics, users, funding, customers, revenue, scale, or production status. No buzzwords: passionate, innovative, cutting-edge, leveraged, spearheaded, transformative, next-generation.

## Folder layout

- `data/` — `facts.yaml`, canonical facts (dates, titles, companies, bullets per track).
- `pipeline/` — executable 10-stage generation workflow (`run.md` orchestrates `stages/`).
- `applications/` — per-company runs (`input.md`, `pipeline_state.md`, `cover_letter.md`).
- `research/` — external evidence + company dossiers (see `research/README.md` index).
- `content/github/` — GitHub project research + Omi contribution dossier and truth boundaries.
- `content/handoffs/` — conversation handoffs, source of truth for wording decisions.
- `versions/{startup,mnc,midlevel}/` — one `_base.md` per track + tailored `resume_{Company}.md` outputs.
- `templates/` — LaTeX variants: `v2-comma-titles` (pdflatex) + `v3` openfont (xelatex); see `templates/v3/README.md`. v1 retired to `archive/`.
- `.agents/skills/` — tool skills (`stop-slop`, `pdf` — loaded only when the task needs them).
- `memory/` — durable agent lessons (see `AGENTS.md` learning loop).
- `assets/` — source PDFs (user artifacts, keep). Superseded research drafts live in `archive/`.
- `docs/` — reference PDFs.
