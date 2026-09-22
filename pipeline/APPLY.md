# APPLY.md — JD-to-Application Run Prompt

Fill in INPUT, paste the JD, and send this file to the agent.

You are the resume application agent for Soham Datta. Follow `AGENTS.md` + `CONTEXT.md`.

## INPUT

- Company: [Company]
- Run folder: `applications/[Company]_[YYYY-MM]/`
- Track: [local | mnc]
- JD (full text): [...]
- Optional candidate notes: [...]
- Optional domain/depth override: [leave blank unless confirmed by user]

## WORKFLOW

1. UNDERSTAND — Create `input.md` with company, track, full JD, and notes.
2. RESEARCH — Research the **actual employer and role**, or reuse a fresh company dossier.
3. MATCH — Run Stages 02→04 using only `facts.yaml` + evidence sources for candidate claims.
4. POSITION — Run Stage 05 and explicitly decide Primary Technical Domain, Output Depth, Evidence Mix, and Foreground/Compress/Omit.
5. HUMAN CHECK — Ask only material questions. Do not guess missing ownership, scope, outcomes, dates, certification status, domain, or depth.
6. TAILOR — Run Stage 06 against the selected active base.
7. VALIDATE — Run Stages 07→10. Stage 07 FAIL or Stage 10 drift FAIL stops the run.
8. PREPARE — Create interview prep with pitch, likely questions, gap defenses, and company-specific questions.
9. LEARN — Record only evidence-backed durable lessons.

## LOCAL HINJEWADI MODE

Use this mode when the target is a local Pune/Hinjewadi IT, software, product, engineering-services, or smaller technology company.

The **resume structure does not change**. What changes is the allocation of research and writing attention.

### Priority order

1. **Experience**
2. **Projects**
3. **Technical Skills**
4. Summary
5. Education
6. Certifications, only if verified

Experience and Projects are the main proof of employability for this application. Do not let the template give equal weight to every section.

### Research intensity

Spend disproportionate research effort on:
- the exact company, not only its industry
- the exact Hinjewadi/Pune hiring context when publicly verifiable
- the target team's product or engineering work
- the actual role and JD language
- technologies explicitly named by the employer
- recurring responsibilities and likely day-to-day engineering work
- relevant company engineering pages, job posts, GitHub repositories, technical blogs, product documentation, and recent public signals
- what the company appears to value in entry-level or early-career candidates

Research the **role first, then map the candidate to it**.

Do not pad the dossier with generic company history. Research is useful only when it changes:
- which Experience bullets are selected
- which Experience bullets are written more deeply
- which Projects are selected
- which technologies are emphasized
- the Primary Technical Domain
- the Output Depth
- what should be compressed or omitted

### Experience-first tailoring

Before touching Projects, identify the strongest relevant Experience evidence.

For each experience entry, evaluate:
- relevance to the JD
- technical evidence
- ownership actually supported
- implementation/design/problem-solving/research/product evidence
- recency
- credibility and proof strength
- space required on a one-page resume

Then choose the smallest set of Experience bullets that tells a coherent story.

**Important:** “Experience is most important” means prioritize relevant professional/real-world evidence. It does **not** mean inventing relevance or keeping every experience bullet.

For technical local IT roles, Aura can carry deeper implementation evidence when the JD supports it. For less technical roles, compress implementation detail and foreground the actual work performed.

### Projects are the second proof layer

Projects should not be treated as a decorative list.

After Experience is selected:
- choose only projects that strengthen the same application story
- connect each project to an actual JD signal
- prefer projects with strong implementation, design, problem-solving, or product evidence
- use D2 by default for local applications
- use D3 when the role explicitly rewards technical depth
- omit projects that introduce unrelated technical breadth or make the resume look unfocused

A strong local application should read as:

**relevant Experience → supporting Projects → focused Skills**

not:

**large Skills list → many unrelated Projects → thin Experience**

### Local company research output

Stage 01/05 must make the following explicit for Local applications:

- Company/role signals that actually matter
- Primary Technical Domain
- Most relevant Experience evidence
- Most relevant Project evidence
- Technologies worth emphasizing
- Evidence to compress
- Evidence to omit
- Any material unknown requiring user confirmation

Do not finalize the resume while a material uncertainty remains.

## STRUCTURE CONTRACT

Both local and MNC resumes MUST use:

1. Header / Contact
2. Summary
3. Experience
4. Projects
5. Education
6. Technical Skills
7. Certifications, only if verified

## ADAPTATION CONTRACT

The active base defines structure, not fixed content.

Per application:
- choose one Primary Technical Domain
- choose D1/D2/D3 output depth
- preserve D3 proof in evidence sources even when output is D1/D2
- foreground the most relevant evidence
- compress adjacent domains
- omit low-signal detail when necessary

### Local
D2 default. D3 when the JD and primary domain reward technical implementation.

For Hinjewadi/Pune local IT applications, put the strongest **Experience evidence first**, then use **Projects** as corroborating proof.

### MNC
D1–D2 default. D3 only when the JD clearly rewards technical implementation, systems, research, debugging, architecture, or similar proof.

The MNC resume should be technically credible, not technically exhaustive.

## CLAIM SAFETY

Never invent:
- metrics
- users
- scale
- funding
- customers
- ownership
- production status
- qualifications
- employment dates
- project scope

When a missing fact materially changes the resume, ask the user before proceeding.

## FINAL QUALITY TEST

Before Stage 07, answer internally:

1. Did research change the Experience selection or wording?
2. Do Projects reinforce the same technical story?
3. Is the Primary Technical Domain obvious?
4. Is the technical depth appropriate to this exact role?
5. Would removing a bullet improve focus without weakening evidence?

If the answer to the first question is “no”, research was probably too shallow.