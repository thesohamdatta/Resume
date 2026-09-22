# CONTEXT.md — Resume Workspace (Soham Datta)

Primary working folder for building and maintaining two active resume tracks from one factual master profile.

**Single source of truth for biographical facts:** `data/facts.yaml`.

## Active tracks

### local

Targets local Indian IT companies, product companies, engineering consultancies, and smaller AI/software teams.

Positioning: practical AI engineer with hands-on software, AI, voice, embedded, and product experience.

Style: one page, clean, technical, human-readable. Same structure as MNC, with slightly more product/project context.

### mnc

Targets multinational companies and enterprise hiring teams.

Positioning: AI/software engineer with concrete technical evidence across AI/ML, LLM systems, voice, backend, embedded systems, and software engineering.

Style: one page, single-column, ATS-safe, conventional headings, searchable text.

## Required section order for both active tracks

```
Header / Contact
Summary
Experience
Projects
Education
Technical Skills
Certifications (only when verified data exists)
```

This is the default architecture for local and MNC resumes. Do not reorder sections merely to imitate another template.

## Domain terms

**Biographical facts:** `data/facts.yaml`  
**Technical proof:** `content/github/evidence.md`  
**Constraints:** `content/github/boundaries.md`

Decision rule: dates/titles/employers/education → `facts.yaml`; technical depth/proof → `evidence.md`; prohibited claims → `boundaries.md`.

## Domain-specific context

- **Aura | Founder:** independent/self-funded wearable AI pendant effort across hardware, software, backend, and product integration. Backend was adapted from the Omi ecosystem, not built from scratch.
- **Mia:** local-first TypeScript AI engineering CLI/harness. Do not call it AGI or claim production adoption.
- **Voice AI:** LiveKit/WebRTC experiments including John, I-am-Mia, and voicecoder. Keep prototype/experimental scope honest.
- **Omi contribution:** describe issues, RFCs, tests, and proposals accurately. Never claim authorship of downstream maintainer PRs.
- **LLM-Council:** multi-LLM compare/critique/synthesize system. Supporting project.
- **PES Modern College / PS Modern Institute:** research support, digital-resource discovery, student guidance, workshops, and documentation. Do not invent research outputs or audience metrics.

## Writing rules

Short, direct, factual, understated. Concrete verbs. Never invent metrics, users, funding, customers, scale, revenue, production status, ownership, or outcomes.

## Folder layout

- `data/` — canonical facts
- `pipeline/` — 10-stage generation workflow
- `applications/` — per-company runs
- `research/` — company dossiers and external evidence
- `content/github/` — technical proof and boundaries
- `versions/local/` — active local company base and tailored outputs
- `versions/mnc/` — active MNC base and tailored outputs
- `versions/startup/` — legacy only
- `versions/midlevel/` — legacy only
- `templates/` — LaTeX export templates
- `memory/` — durable lessons
- `assets/` — source artifacts

## Active-track rule

New application runs MUST use exactly one of:
- `local`
- `mnc`

Do not use `startup` or `midlevel` for new work.
