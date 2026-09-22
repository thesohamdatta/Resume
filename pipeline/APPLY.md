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

Experience and Projects are the primary evidence layers for this application. Do not let the template give equal weight to every section.

### Research intensity

Spend disproportionate research effort on:

- the exact employer, not only its industry
- the exact role and JD language
- the relevant Pune/Hinjewadi office or team context when publicly verifiable
- the target team's products, services, or engineering work
- technologies explicitly named by the employer
- recurring responsibilities and likely day-to-day work
- relevant company engineering pages, job posts, GitHub repositories, technical blogs, product documentation, and recent public signals
- what the company appears to value in entry-level or early-career candidates

Research the **role first, then the candidate-to-role match**.

Do not spend research time on generic company history that cannot affect resume decisions.

Research is complete only when it can explain how the findings change at least one of:

- Experience bullet selection
- Experience bullet depth
- Project selection
- Project depth
- technical skills emphasis
- Primary Technical Domain
- Output Depth
- Foreground / Compress / Omit decisions

### Experience-first tailoring

**Experience is the highest-priority resume section for Local Hinjewadi applications.**

Before selecting Projects, evaluate every relevant experience entry against:

- direct JD relevance
- technical relevance
- ownership actually supported
- Implementation / Design / Problem-solving / Research / Product evidence
- recency
- proof strength
- credibility
- available page space
- whether the experience demonstrates work that transfers to the target role

Then choose the smallest set of strong Experience bullets that forms a coherent story.

Do not keep weak or generic bullets merely because the section is important.

Do not manufacture relevance. A non-technical role can remain useful when it demonstrates real work, coordination, documentation, customer-facing problem solving, or another capability that the JD actually values.

For a technical local IT role, use Aura's deeper implementation evidence only where the JD supports it. The evidence repository stays detailed; the resume shows only the appropriate depth.

### Project-second tailoring

Projects are the **second-priority evidence layer**, not decoration.

After Experience is selected:

- choose projects that reinforce the same Primary Technical Domain
- map each selected project to a real JD signal
- prefer projects with strong implementation, design, problem-solving, research, or product evidence
- use D2 by default for local applications
- use D3 only when the role explicitly rewards technical implementation or technical proof
- remove unrelated project breadth when it weakens the overall story
- keep project descriptions concrete and short enough to preserve Experience space

The intended reading order is:

**relevant Experience → supporting Projects → focused Skills**

not:

**large Skills list → many Projects → thin Experience**

### Local research-to-writing contract

Before Stage 06, Stage 05 must explicitly provide:

- company/role signals that matter
- Primary Technical Domain
- Output Depth
- strongest Experience evidence
- strongest Project evidence
- technologies worth emphasizing
- evidence to compress
- evidence to omit
- material unknowns requiring user confirmation

If research cannot distinguish which experience and projects matter most, return to research before writing.

Do not finalize while a material uncertainty remains.

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

For Hinjewadi/Pune local IT applications, **Experience is the primary proof layer and Projects are the supporting proof layer**.

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

1. Did the research materially change the Experience selection or wording?
2. Do Projects reinforce the same technical story?
3. Is the Primary Technical Domain obvious?
4. Is the technical depth appropriate to this exact role?
5. Does the resume give more attention to strong Experience than to Skills or decorative content?
6. Would removing a low-signal Project or bullet improve focus without weakening evidence?

If the first answer is “no”, research was probably too shallow.