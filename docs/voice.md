---
name: Resume Writing Voice
language:
  primary: en-IN
  treatment: you
  contractions: allowed
personality:
  traits:
    - evidence-first
    - technically-specific
    - direct-and-unshowy
    - concise-without-telegraphese
    - candid-about-scope
    - recruiter-readable
register:
  formality: professional
  emoji: never
beliefs:
  - id: evidence-over-adjectives
    statement: A concrete, verifiable detail is stronger than a claim about being exceptional.
  - id: truth-before-positioning
    statement: Tailoring changes selection and emphasis, never candidate facts, ownership, or status.
  - id: relevance-is-earned
    statement: Every line must help establish fit for this role or provide necessary context.
  - id: defendable-in-interview
    statement: Every claim must be explainable by the candidate using real work and evidence.
  - id: plain-language-technical-depth
    statement: Use exact technical language where it adds signal; explain or remove jargon that does not.
lexicon:
  protected_terms:
    - term: Aura
      never: ["AURA", "aura"]
    - term: Mia
      never: ["MIA"]
    - term: Omi
      never: ["OMI"]
    - term: AICTE
      never: ["AICTE internship at Google", "Google internship"]
    - term: TypeScript
      never: ["Typescript"]
    - term: TensorFlow Lite
      never: ["Tensorflow Lite"]
  forbidden:
    - phrase: "passionate"
      reason: Generic self-description; replace with relevant work or omit.
    - phrase: "innovative"
      reason: Unsupported praise; state what was actually built or changed.
    - phrase: "cutting-edge"
      reason: Hype rather than evidence.
    - phrase: "results-driven"
      reason: Generic professional claim.
    - phrase: "highly motivated"
      reason: Generic personality claim.
    - phrase: "proven track record"
      reason: Claims reputation instead of showing evidence.
    - phrase: "dynamic professional"
      reason: Empty profile language.
    - phrase: "leveraged"
      reason: Prefer the direct verb such as used, integrated, or applied.
    - phrase: "utilized"
      reason: Prefer used or applied.
    - phrase: "spearheaded"
      reason: Inflates leadership unless supported by explicit ownership evidence.
    - phrase: "orchestrated"
      reason: Inflated verb unless orchestration is the literal technical work.
    - phrase: "seamless"
      reason: Unmeasured quality claim.
    - phrase: "world-class"
      reason: Unsupported superiority claim.
    - phrase: "revolutionary"
      reason: Unsupported hype.
    - phrase: "next-generation"
      reason: Generic marketing language.
    - phrase: "synergized"
      reason: Corporate filler.
    - phrase: "worked on"
      reason: Too vague when a more specific action is known.
    - phrase: "responsible for"
      reason: Duty framing; prefer the actual action.
    - phrase: "successfully"
      reason: Usually adds no evidence.
    - phrase: "various"
      reason: Hides the actual scope.
    - phrase: "multiple"
      reason: Quantify or name the actual scope when evidence permits.
audiences:
  - id: technical-recruiter
    name: Technical recruiter or engineering hiring manager
    vocabulary: [implementation, integration, debugging, testing, architecture, latency, retrieval, evaluation, firmware, API]
    is_default: true
  - id: startup-founder
    name: Startup founder or early engineering team
    vocabulary: [ownership, trade-offs, prototype, iteration, product constraints, end-to-end implementation]
  - id: general-referrer
    name: General recruiter or referrer
    vocabulary: [built, integrated, tested, supported, automated, delivered]
surfaces:
  - id: resume-bullet
    name: Resume bullet
    max_length: 2
    unit: sentences
    forbid_emoji: true
  - id: professional-summary
    name: Professional summary
    max_length: 3
    unit: sentences
    forbid_emoji: true
  - id: skills-line
    name: Skills line
    max_length: 1
    unit: sentences
    forbid_emoji: true
  - id: project-description
    name: Project description
    max_length: 2
    unit: sentences
    forbid_emoji: true
  - id: application-note
    name: Short application or referral note
    max_length: 120
    unit: words
    forbid_emoji: true
tones:
  - id: explain
    description: State what the work is and why it matters, using the shortest useful explanation.
  - id: demonstrate
    description: Show capability through artifacts, methods, constraints, and outcomes rather than self-praise.
  - id: condense
    description: Remove repeated context while preserving the distinguishing technical evidence.
  - id: tailor
    description: Surface evidence that directly matches the role; do not imitate the job description.
formatting:
  capitalization: Standard technical capitalization; preserve official project, framework, employer, and credential names.
  numbers: Use verified numbers with units or clear scope. Never infer a metric from context.
  emphasis: Use sparingly; no decorative emphasis in resume prose.
  punctuation: Prefer standard ASCII punctuation when required by the LaTeX/template or MNC mode.
---

# Purpose

This guide governs the writing of resumes and short career materials in this repository. It complements `RESUME_RULES.md`; it does not own candidate facts, mode selection, ATS constraints, pipeline gates, or the visual template.

The resume should read like a technically capable early-career builder explaining real work clearly. It should not sound like a personal brand campaign or a generated list of achievements.

## Writing model

Prefer the smallest useful statement of:

**Action + actual work + relevant method/detail + verified outcome or constraint.**

This is a thinking aid, not a mandatory sentence template. A bullet can lead with the technical problem, design decision, artifact, or result when that makes the evidence clearer. Do not force every bullet into the same structure.

Examples are patterns, not claims about the candidate:

- Specific: "Implemented I2S DMA audio capture at 16 kHz on ESP32-S3 firmware."
- Vague: "Leveraged cutting-edge embedded technologies to deliver a robust audio solution."
- Specific: "Adapted existing backend components for streaming audio and memory/context processing."
- Overstated: "Architected a scalable backend from scratch."

## Evidence and ownership

Use the strongest verb the evidence supports, no stronger:

- used / studied: exposure or application
- tested / investigated / diagnosed: analysis or verification
- contributed / adapted / integrated: work within an existing system
- implemented / built: direct implementation
- designed: a documented design or decision
- owned / led / architected: only where responsibility and scope are explicitly supported

Do not convert a proposal into an implementation, approval into a merge, downstream adoption into authorship, a prototype into a production system, or a virtual program into employment at a partner company.

A number is allowed only when its value, source, and meaning are verified. If no metric exists, use the concrete artifact, method, scope, decision, constraint, or observable result. Never write a placeholder metric as if it were real.

## Naturalness without gimmicks

Avoid generic claims, inflated verbs, repeated sentence rhythms, adjective piles, forced storytelling, and keyword clouds. Do not add slang, deliberate typos, fake humility, or quirky language to appear human.

Keep meaningful technical nouns. A distinctive implementation detail is useful when it supports the target role; an exhaustive tool list is not. Keep bullets short enough to scan, but do not delete the detail that makes the work credible.

Do not rewrite a sound sentence just to make it different. Make the smallest edit that improves truth, relevance, clarity, evidence, or space efficiency.

## Tailoring

The job description determines which supported evidence matters. It does not supply candidate facts or dictate sentence wording.

- Match important requirements to specific evidence before drafting.
- Prefer direct evidence; label adjacent experience honestly.
- Use exact role-relevant terminology where naturally supported.
- Do not keyword-stuff, mimic JD sentences, or claim a skill solely because it appears in the JD.
- A mode changes emphasis and depth only. It never changes facts or the candidate's status.

## Mode expression

- **Startup:** foreground product decisions, implementation ownership, technical trade-offs, iteration, and range when evidence supports them. Avoid founder mythology and hype.
- **MNC:** use conventional terminology, clear role keywords, consistent dates, concise evidence-rich bullets, and parser-friendly wording. Do not write for an imagined ATS score.
- **Referral:** make the work and value clear to a non-specialist without erasing technical credibility.

These are emphasis differences, not three different personalities.

## Final editorial pass

For each line ask:

1. Is every claim supported by a canonical source?
2. Does this line help with the target role?
3. Is the action and ownership level clear?
4. Is there a concrete method, artifact, result, or constraint?
5. Can the candidate defend it in an interview?
6. Can any words be removed without losing meaning?
7. Does the wording sound natural when read aloud, without becoming casual?
8. Does it preserve the template, mode, and ATS constraints?

If a line is already clear and accurate, keep it. Voice lint is a review aid, not permission to alter facts. The hard gates and source rules remain in `RESUME_RULES.md`, `content/github/boundaries.md`, and `DONT.MD`.

## Governing principle

**Make the evidence easier to see. Do not make the candidate larger than the evidence.**
