# Application Resume Prompt

Use this as the reusable operating prompt for any job application in this repository.

## Objective

Given the application input in `applications/{Company}_{YYYY-MM}/input.md`, produce the strongest truthful one-page resume for that exact role.

Do not write a generic resume. Treat the job description as targeting data, not as facts about the candidate.

## Read first

Follow this order:

1. `AGENTS.md`
2. `SPEC.md`
3. `pipeline/README.md`
4. `RESUME_RULES.md`
5. `DONT.MD`
6. `data/facts.yaml`
7. `content/github/evidence.md`
8. `content/github/boundaries.md`
9. `docs/voice.md`
10. `memory/lessons.md` when relevant
11. The target `applications/{Company}_{YYYY-MM}/input.md`
12. The selected mode in `modes/{mode}.yaml`

## Process

1. Extract the real hiring signals from the JD.
2. Map each important requirement to verified candidate evidence.
3. Classify each match as DIRECT, ADJACENT, or NONE.
4. Foreground DIRECT evidence, use ADJACENT evidence only with honest framing, and omit NONE.
5. Prefer implementation, measurable results, concrete technical decisions, and demonstrated ownership over generic claims.
6. Select the smallest evidence set that makes the candidate credible.
7. Keep the existing LaTeX template and one-page layout. Do not redesign the visual system.
8. Keep the resume ATS-readable and single-column.
9. Use exact role terminology where it is truthful, especially for the headline and skills.
10. Do not keyword-stuff or copy sentences from the JD.
11. Do not invent metrics, responsibilities, technologies, dates, employers, users, production status, ownership, certifications, or outcomes.
12. Run the repository validation pipeline before delivery.

## Writing standard

Write FACT → ACTION → CONSEQUENCE/CONSTRAINT.

Use concrete verbs and technical nouns. Avoid empty phrases such as “passionate”, “results-driven”, “highly motivated”, “leveraged”, “cutting-edge”, “responsible for”, and similar filler when they replace evidence.

Keep the language concise, natural, and evidence-dense.

## Output

Produce the normal application output defined by the repository pipeline.

Also ensure the final resume answers three questions quickly:

- Why does this candidate fit this exact role?
- What have they actually built or implemented?
- What evidence supports the claims?

If a requested qualification is not supported by the source of truth, omit it rather than manufacture it.
