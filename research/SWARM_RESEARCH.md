# SWARM_RESEARCH.md — Master Swarm-Research Prompt (reusable)

Fill INPUT, send this file's content to the agent as-is. The agent researches but does
NOT write resumes — it produces a dossier + action plan that a later APPLY.md run consumes.
Extends `pipeline/stages/01_company_researcher.md` (same dossier schema, deeper evidence).

---

You are the research orchestrator for Soham Datta's resume workspace.
Follow `AGENTS.md` (load policy, precedence, learning loop) + `CONTEXT.md`.
Source precedence: USER/TASK → AGENTS.md → DONT.MD + `content/github/boundaries.md` →
`memory/lessons.md` → research → INFERENCE. The JD is a specification for relevance,
never a source of candidate facts (DONT.MD §6). Never manufacture facts.

INPUT
- Company: [Company]
- Role: [title]
- JD (full text, pasted below, or [none — exploratory research]): [...]
- Track (if known): [startup | mnc | midlevel | unknown]
- Run folder (if an application exists): [applications/{Company}_{YYYY-MM}/ or none]

LOAD (only this, then delegate — progressive disclosure):
1. `AGENTS.md` + `CONTEXT.md` (always).
2. `research/companies/{Company}.md` if it exists (note its date; <60 days = reusable base).
3. `research/companies/_template.md` (dossier schema — the only schema you may write to).
4. The run folder's `input.md` notes if it exists (prior answers live here; never re-ask them).
5. `memory/lessons.md` (durable context only).
Do NOT load: other runs' `pipeline_state.md`, `archive/`, PDFs, `resume_best_practices.md`
(rules already distilled into DONT.MD), full `DONT.MD` (gates only if you write claims).

PHASE 0 — UNDERSTAND (orchestrator only, no subagents yet):
- State in 5 lines: what the role asks for, why this company matters to this candidate
  (use CONTEXT.md positioning + prior input.md notes, not inference), and what a later
  APPLY.md run will need from this research.
- DEDUP CHECK: list which dossier sections are already fresh (<60 days) and will be
  REUSED verbatim, vs which need fresh research. Never re-research fresh sections.

PHASE 1 — FAN OUT (spawn all specialists in parallel; each gets ONLY its mission +
the INPUT block + relevant dossier deltas, never the full repo):
1. **Company researcher** — mission, products, tech stack, business model, funding/stage,
   market position, customers, locations, activity in last 12 months.
2. **People researcher** — founders, executives, likely hiring manager, recruiters,
   engineers/researchers publishing in the role's area, team structure signals.
3. **Role decoder** — from the JD (or analogous JDs if none): stated vs implied needs,
   must-have vs nice-to-have, what "good" looks like in 6 months, hiring urgency signals.
4. **Self auditor** — LOCAL files only (`data/facts.yaml`, `content/github/evidence.md`,
   `versions/{track}/_base.md`, portfolio/GitHub links in facts): inventory strengths,
   gaps, and proof anchors relevant to the role. No web search. No new claims.
5. **Market checker** — competitors, ecosystem trends, salary/level signals if public.
   Skip entirely if it would not change targeting (say so in one line).

Each specialist returns MAX 15 lines: findings with `source + date` per claim, or
`[unverified]` where uncited. Important claims need 2 independent sources. Raw
research stays in the agent's scratch — it never enters the final context.

PHASE 2 — INDEPENDENT VERIFIER (new agent, receives specialist outputs + boundaries):
Kill or downgrade: single-source important claims, conflicts between agents, weak
evidence presented as fact, conclusions the evidence does not support, any candidate
fact not traceable to facts.yaml/evidence.md. Output: PASS / FLAG list with reasons.

PHASE 3 — SYNTHESIZER (new agent, receives verified findings only — never raw dumps):
Write EXACTLY these sections:
- FACTS (company/role, cited)
- VERIFIED EVIDENCE (candidate proof anchors: repo/PR/file, cited)
- INFERENCE (clearly labeled, e.g. stack guesses from JD signals)
- UNCERTAINTY (what is still unknown + whether it matters)
- RECOMMENDATION (positioning hook in one line, what to foreground/cut)
- ACTION PLAN: resume tailoring notes → application strategy → outreach targets (who,
  why, angle) → portfolio positioning → interview prep seeds → 3–5 questions for them.

PHASE 4 — ASK: at most 3 questions, ONLY ones that would materially change targeting
or fill an important evidence gap. Check input.md notes, facts.yaml, evidence.md,
memory/lessons.md first. Then proceed on flagged assumptions.

PHASE 5 — WRITEBACK (no duplicate truth, no silent overwrites):
- Dossier: create/overwrite `research/companies/{Company}.md` in the `_template.md`
  schema, ≤400 words, per-section confidence (HIGH only from JD text or engineer posts;
  LOW if inferred from marketing copy). Preserve fresh sections verbatim.
- Memory: PROPOSE (do not directly append) ≤3 `memory/lessons.md` candidate lines,
  each with evidence. Durable workflow patterns only.
- NEVER write to: `DONT.MD`, `content/github/boundaries.md`, `data/facts.yaml`,
  `content/github/evidence.md`, any `versions/` resume, any `pipeline_state.md`.
  New facts/constraints you discover go in the dossier's UNCERTAINTY section as
  proposals, not into canonical files.

HARD RULES: no invented metrics, people, funding, or stack claims. Every claim cited
with date or tagged `[unverified]`. Cross-verify important claims (DONT.MD
cross-source check). Prefer fresh sources; mark anything >12 months old.
