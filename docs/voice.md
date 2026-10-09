---
version: 0.1.0-alpha.3
name: Resume Writing Voice
description: >-
  Direct, evidence-led resume writing for early-career technical roles.
  Clear and specific without corporate language, invented personality, or AI-shaped prose.

language:
  primary: en-IN
  treatment: you
  contractions: allowed

personality:
  archetypes:
    - craftsperson
    - technical-guide
  traits:
    - evidence-first
    - technically-specific
    - direct-without-theatre
    - concise-without-telegraphese
    - candid-about-scope
    - recruiter-readable

register:
  default: professional-direct
  formality: medium
  emoji_policy: institutional-zero
  exclamation_marks: forbidden
  ellipsis_policy: forbidden-except-quotes
  semicolon_policy: prefer-two-short-sentences

beliefs:
  - id: evidence-over-adjectives
    statement: Show the work; do not praise the person instead of describing it.
  - id: truth-before-positioning
    statement: Tailoring changes selection and emphasis, never candidate facts or ownership.
  - id: clarity-over-performance
    statement: Write to be understood by a recruiter, not to impress a language model.
  - id: technical-precision
    statement: Keep exact technical terms when they make the work more precise.
  - id: minimum-effective-edit
    statement: Improve a real weakness and leave sound writing alone.

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
    personas: [recruiter, engineering manager]
    vocabulary: [implementation, integration, debugging, testing, latency, retrieval, evaluation, firmware, API]
    proof_type: implementation-depth
    is_default: true
  - id: startup-founder
    name: Startup founder or early engineering team
    personas: [founder, early engineering team]
    vocabulary: [prototype, trade-offs, iteration, product constraints, implementation]
    proof_type: implementation-depth
  - id: mnc-recruiter
    name: MNC or enterprise recruiter
    personas: [recruiter, engineering manager]
    vocabulary: [implementation, testing, reliability, API, performance, integration]
    proof_type: implementation-depth
  - id: general-referrer
    name: Local recruiter or referrer
    personas: [referrer, non-specialist recruiter]
    vocabulary: [built, integrated, tested, supported, automated, delivered]
    proof_type: tangible-result
surfaces:
  - id: resume-bullet
    name: Resume bullet
    max_length: 2
    unit: sentences
    forbid_emoji: true
    forbid_artificial_caps: true
  - id: professional-summary
    name: Professional summary
    max_length: 3
    unit: sentences
    forbid_emoji: true
    forbid_artificial_caps: true
  - id: skills-line
    name: Skills line
    max_length: 1
    unit: lines
    forbid_emoji: true
    forbid_artificial_caps: true
  - id: project-description
    name: Project description
    max_length: 2
    unit: sentences
    forbid_emoji: true
    forbid_artificial_caps: true
  - id: application-note
    name: Short application or referral note
    max_length: 120
    unit: words
    forbid_emoji: true
    forbid_artificial_caps: true

tones:
  - id: explain
    name: Explain the work
    pattern: explain-mechanism
    density_sentences: { min: 1, max: 3 }
  - id: demonstrate
    name: Demonstrate capability
    pattern: demonstrate-with-data
    density_sentences: { min: 1, max: 2 }
  - id: condense
    name: Condense without losing proof
    pattern: condense-into-contrast
    density_sentences: { min: 1, max: 2 }
  - id: tailor
    name: Tailor to the role
    pattern: demonstrate-with-data
    density_sentences: { min: 1, max: 2 }

formatting:
  capitalization: sentence-case
  quotation_marks: english-double
  em_dash: " — "
  hyphen_use: [compound-words, numeric-ranges]
  numbers:
    threshold_letters: 9
    impact_data: always-digits
    percent_symbol: required
    currency_symbol: required
    thousands_separator: ","
    decimal_separator: "."
    millions_abbreviation: M-uppercase
  emphasis:
    bold: [framework-names, impact-data]
    italic: [textual-quotes, document-titles]
    underline: forbidden
    all_caps: [acronyms-only]
---


## Overview

Write like a capable person explaining real work they can defend in an interview. Be direct, technically precise, calm, and easy to scan. No corporate theatre, personal-brand language, or manufactured quirks.

The recruiter should understand the target fit, the candidate's actual contribution, and the strongest proof on a fast first read. Keep one voice across all modes; the mode changes emphasis and depth, not personality.

Candidate truth belongs to `data/facts.yaml`, `content/github/evidence.md`, and `content/github/boundaries.md`. Resume rules and hard gates remain in `RESUME_RULES.md` and `DONT.MD`. This file owns wording and tone only.

## Personality

- **Evidence-first:** show the work instead of praising the person.
- **Technically specific:** name the relevant system, method, tool, decision, or constraint.
- **Direct, not theatrical:** use plain language and concrete verbs.
- **Concise, not telegraphic:** remove padding, not the detail that makes work credible.
- **Honest about scope:** make contribution and limitations clear.
- **Recruiter-readable:** technical depth should prove capability, not obscure it.

## Beliefs

- Every line earns its space by showing role fit or necessary context.
- Specific work is stronger than generic self-description.
- Use the strongest wording the evidence supports, not the strongest wording available.
- Editing is successful when the writing improves, not merely changes.
- A natural voice comes from clear thinking and accurate detail, not deliberate quirks.

## Register

Use professional, plain English. Keep official technical terms and names intact. Indian English spelling is fine. Resume bullets usually omit first-person pronouns; fragments are acceptable when clear and conventional. Prefer active voice when it makes ownership clear, but do not rewrite a sentence just to avoid passive voice.

Do not make an early-career candidate sound like a senior executive. Do not make professional writing artificially casual to avoid sounding generated.

## Lexicon

The forbidden phrases in the YAML are examples of generic resume language, not a complete AI-writing detector. Review them in context. Do not expand the list into a ban on ordinary words.

Words such as "leveraged", "orchestrated", "multiple", "various", and "successfully" are review prompts, not automatic failures. Change them only when the replacement says what actually happened more clearly. Preserve valid technical language even when it resembles a flagged pattern.

Keep official spelling and capitalization for project names, tools, languages, frameworks, employers, and credentials.

## Audiences

- **Technical recruiter / engineering manager (default):** make role fit and technical contribution clear quickly; give enough implementation detail to judge depth.
- **Startup founder:** show what was built, decisions made, trade-offs, debugging, iteration, and personal contribution when supported. Demonstrate initiative through work, not founder mythology. Do not imply traction, customers, production readiness, or seniority without evidence.
- **MNC / enterprise recruiter:** use conventional terminology, supported role keywords, consistent dates, and concise evidence. Avoid ATS tricks and unnecessary implementation detail.
- **Local recruiter / referrer:** make the work easy to understand and forward without stripping out technical credibility.

The job description selects relevant evidence; it does not supply candidate facts or dictate sentence wording.

## Surfaces

- **Resume bullet:** one clear idea, usually one sentence and normally one or two lines in the final template. Lead with the work, a decision, a technical problem, or an observable result. A useful result can be a verified measurement, delivered artifact, test, resolved defect, design decision, scope, or constraint. Do not invent business impact.
- **Professional summary:** use only if it improves positioning. State relevant focus and supporting evidence, not generic personality claims.
- **Skills line:** list relevant, defensible skills in sensible groups. Do not turn it into a keyword dump.
- **Project description:** identify what it does and the candidate's actual contribution. Mention project status or constraints when material.
- **Application/referral note:** concise and specific. State the relevant evidence and the reason for writing; do not flatter or repeat the resume.

## Mode expression

Keep the voice constant. Change the evidence selected and the depth shown:

- **Startup:** foreground product work, technical decisions, trade-offs, testing, debugging, iteration, and what the candidate personally owned. Limited first person is allowed in the profile line when it improves the builder signal. Do not write like a pitch deck.
- **MNC:** foreground role-relevant skills, implementation evidence, scope, and standard terminology. Cut details that do not help assess fit. Avoid robotic achievement formulas.
- **Referral:** foreground practical contribution and enough context for a non-specialist. Avoid both a startup pitch and generic corporate language.

## Tones

- **Explain:** name what was done and include the method or context that makes it understandable.
- **Demonstrate:** show capability through implementation details, tests, artifacts, decisions, or verified outcomes.
- **Condense:** remove repetition while keeping the detail that distinguishes the work.
- **Tailor:** choose and order evidence to match the role. Do not copy the job description or stuff keywords.

## Formatting

Use consistent punctuation and technical capitalization. Use digits for metrics, versions, dates, frequencies, and technical quantities. Keep units and scope clear. Include a metric only when verified; do not infer outcomes from effort or activity.

Use bold only for framework names and impact data, and only where the existing template supports it. Avoid additional emphasis. No emoji, decorative typography, or gimmick punctuation in resume content. Preserve the existing LaTeX template and ATS-safe structure; voice rules never justify layout changes.

## Editorial rules

- Keep writing that is already clear, relevant, and accurate. A style preference or scanner match alone is not a defect.
- Make the smallest edit that improves clarity, relevance, specificity, or scanning.
- Prefer concrete verbs, nouns, methods, decisions, and artifacts over praise.
- Vary rhythm only when repetition distracts. Parallel bullets are fine when they help comparison.
- Keep technical detail that proves work; remove tool lists that do not prove role fit.
- If no measured result exists, use a verified artifact, test, resolved issue, design decision, scope, or constraint.
- Preserve names, dates, quantities, technical terms, ownership, status, uncertainty, and attribution. Do not invent seniority, leadership, personality, shipping, production status, users, funding, or results.
- Do not add slang, deliberate errors, fake humility, anecdotes, or quirks to appear human. Do not replace one vague phrase with another.
- Do not force every bullet into the same action-method-result formula.

## Editorial protocol

1. Read the full draft and identify its target role and audience.
2. Diagnose a specific defect: vagueness, inflated language, repetition, unclear ownership, irrelevant detail, or awkward compression. A phrase match alone is not a defect.
3. Protect facts, numbers, technical terms, attribution, ownership, status, and uncertainty against the source files.
4. Repair minimally. Leave unaffected sentences unchanged.
5. Review the whole resume for relevance, repeated claims, repetitive rhythm, lost evidence, and recruiter scanning.
6. Use the existing truth, fit, readability, parsing, template, and one-page gates. Do not add a new pipeline stage or sub-agent for style alone.

If fixing a line requires guessing, keep the strongest supported version or ask for the missing fact.

## Examples

Weak: "Leveraged innovative technologies to deliver a robust solution."

Clearer, when supported: "Integrated ESP32-S3 firmware with I2S audio capture and Opus compression."

Weak: "Responsible for various AI projects."

Clearer, when supported: "Built a FastAPI service for streaming audio and memory extraction."

These examples name the work; they do not invent an outcome. Use them only when the evidence supports the exact contribution.

## Governing principle

**Make the evidence easier to see. Do not make the candidate larger than the evidence.**
