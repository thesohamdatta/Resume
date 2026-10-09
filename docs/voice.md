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
  semicolon_policy: prefer-short-sentences

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
    - term: TypeScript
      never: ["Typescript"]
    - term: TensorFlow Lite
      never: ["Tensorflow Lite"]
  forbidden:
    - phrase: "results-driven professional"
      reason: Generic self-praise without evidence.
    - phrase: "highly motivated professional"
      reason: Generic personality claim instead of relevant work.
    - phrase: "proven track record of success"
      reason: Reputation claim without showing the evidence.
    - phrase: "dynamic professional"
      reason: Empty profile language.
    - phrase: "cutting-edge solutions"
      reason: Hype that does not identify the actual work.
    - phrase: "world-class solutions"
      reason: Unsupported superiority claim.
    - phrase: "revolutionary platform"
      reason: Unsupported hype instead of a concrete description.
    - phrase: "seamless experience"
      reason: Unmeasured quality claim; name the mechanism or verified result.
    - phrase: "Google internship"
      reason: Must not misrepresent the AICTE virtual internship as employment at Google.

audiences:
  - id: technical-recruiter
    name: Technical recruiter or engineering hiring manager
    personas: [recruiter, engineering manager]
    vocabulary: [implementation, integration, debugging, testing, latency, retrieval, evaluation, firmware, API]
    proof_type: implementation-evidence
    is_default: true
  - id: startup-founder
    name: Startup founder or early engineering team
    personas: [founder, early engineering team]
    vocabulary: [prototype, trade-offs, iteration, product constraints, implementation]
    proof_type: ownership-and-decisions
  - id: general-referrer
    name: General recruiter or referrer
    personas: [referrer, non-specialist recruiter]
    vocabulary: [built, integrated, tested, supported, automated, delivered]
    proof_type: clear-work-and-relevance

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
    pattern: instruct
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

Write like a technically capable person describing work they can explain in an interview. Be direct, specific, and calm. No corporate theatre, personal-brand language, or manufactured quirks.

The reader is a recruiter with limited time. Make the work, technical relevance, and level of contribution clear on the first read. This file governs language and tone only. Candidate truth belongs to `data/facts.yaml`, `content/github/evidence.md`, and `content/github/boundaries.md`; resume rules and hard gates remain in `RESUME_RULES.md` and `DONT.MD`.

## Personality

- **Evidence-first:** show the work instead of calling it impressive.
- **Technically specific:** name the relevant system, tool, method, or constraint.
- **Direct without theatre:** use plain verbs; avoid grand claims and fake humility.
- **Concise, not telegraphic:** remove padding, not grammar or useful context.
- **Candid about scope:** make contribution and limitations easy to understand.
- **Recruiter-readable:** technical depth should clarify capability, not bury it.

## Beliefs

- Every line must earn its space by proving fit or providing necessary context.
- Specificity beats adjectives. A real artifact or method is stronger than praise.
- Use the strongest wording the evidence supports, not the strongest wording available.
- A natural voice comes from clear thinking and accurate detail, not deliberate quirks.
- Editing is successful when the writing improves, not when the text changes.

## Register

Use professional, plain English with Indian English spelling where applicable. Keep technical names and standard industry terminology intact. Contractions are allowed when natural, but resume bullets usually do not need them.

Prefer active voice when the actor matters. Passive voice is fine when the result or object matters more than the actor, or when the actor is unknown. Fragments are acceptable in resume bullets when clear and conventional; do not force complete-sentence prose into every line.

Do not make the candidate sound like a senior executive if the evidence describes early-career or independent project work. Do not make the writing artificially casual to avoid sounding generated.

## Lexicon

The forbidden phrases in the YAML are fixed examples of generic resume language, not a complete detector for AI writing. Their presence is a strong reason to revise in resume copy, but a phrase match must still be checked in context. Never expand the list into a universal ban on ordinary words.

Treat terms such as "leveraged", "orchestrated", "multiple", "various", and "successfully" as review prompts, not automatic failures. They can be vague or inflated; they can also be accurate. Replace them only when the replacement states the actual action more clearly. Keep literal technical terms, established terminology, and correct domain language.

Preserve official spelling and capitalization for project names, tools, languages, frameworks, employers, and credentials. Do not write a protected term in a forbidden variant in resume output.

## Audiences

- **Technical recruiter / engineering manager (default):** lead with relevant work, then the technical detail needed to understand its depth.
- **Startup founder:** show product judgement, actual implementation, trade-offs, and iteration when supported. Avoid founder mythology and hype.
- **General referrer:** explain the work in plain language without erasing the technical substance.

These are differences in emphasis, not different personalities. The job description selects relevant evidence; it does not supply candidate facts or dictate the sentence wording.

## Surfaces

- **Resume bullet:** one clear idea, usually one sentence; use a second only when it adds necessary context. Lead with the work, a decision, a technical problem, or an observable result—whichever makes the evidence easiest to grasp.
- **Professional summary:** use only when it improves positioning. State relevant focus and supporting evidence; avoid objectives and generic self-description.
- **Skills line:** list relevant, defensible skills in sensible groups. Do not turn it into a keyword dump.
- **Project description:** identify what the project does and the candidate's actual contribution. Mention status or constraints when they affect the claim.
- **Application/referral note:** short, specific, and human. State the role, relevant evidence, and clear ask when one is needed. Do not use flattery or a generic pitch.

## Tones

- **Explain:** name what was done and include the method or context that makes it understandable.
- **Demonstrate:** show capability through implementation details, tests, artifacts, decisions, or verified outcomes.
- **Condense:** remove repeated context while keeping the detail that distinguishes the work.
- **Tailor:** choose and order evidence to match the role. Do not copy the job description or stuff keywords.

## Formatting

Use standard technical capitalization, consistent punctuation, and readable grammar. Use digits for metrics, versions, dates, frequencies, and technical quantities. Keep units and scope clear. Use metrics only when verified; do not infer results from effort or activity.

Use bold sparingly where the template supports it. Do not use emoji, decorative typography, exclamation marks, or gimmick punctuation in resume content. Preserve the existing LaTeX template and ATS-safe structure; voice rules never justify layout changes.

## Editing principles

**Do**
- Keep a bullet that is already clear, relevant, and accurate.
- Make the smallest edit that fixes a real problem.
- Prefer concrete verbs, objects, and methods over praise.
- Vary sentence openings when repetition becomes noticeable; do not force variation where parallel structure improves scanning.
- Preserve technical detail that demonstrates real work.
- Use a verified result when available; otherwise state the concrete artifact, scope, constraint, or decision.

**Don't**
- Add achievements, metrics, ownership, production status, users, funding, or personality that the source does not support.
- Replace a vague phrase with another vague phrase.
- Add fake anecdotes, fake humility, slang, deliberate errors, or "human" quirks.
- Remove a necessary caveat or turn uncertainty into certainty.
- Rewrite a sentence solely because it contains a suspected AI tell.
- Force every bullet into the same action-method-result template.
- Use inflated language to compensate for missing evidence.

## Editorial protocol

1. **Read the full draft.** Understand its purpose, target role, and register before editing.
2. **Diagnose.** Identify the exact span that is vague, inflated, repetitive, unclear, or irrelevant. A detector match alone is not a defect.
3. **Protect.** Check names, dates, numbers, technical terms, ownership, status, scope, uncertainty, and attribution against the source files.
4. **Repair minimally.** Change only the text needed to fix the confirmed defect. Leave good sentences unchanged.
5. **Review the whole resume.** Check for repeated rhythms, duplicate claims, unexplained jargon, awkward compression, and lost technical evidence.
6. **Validate.** Re-check truth, role fit, readability, ATS extraction, template constraints, and one-page output using the repository's existing gates.

If the defect cannot be fixed without guessing, preserve the claim at its supported level or ask for the missing fact. Do not add a new stage or sub-agent to the resume pipeline for style alone; use the existing review and validation path.

## Do's and Don'ts

**Weak:** "Leveraged innovative technologies to deliver a robust solution."

**Better, when supported:** "Integrated ESP32-S3 firmware with I2S audio capture and Opus compression."

The second version is better because it names the work. It does not claim an outcome the source has not established.

**Weak:** "Responsible for various AI projects."

**Better, when supported:** "Built a FastAPI service for streaming audio and memory extraction."

Do not use the better example unless the source evidence supports that exact contribution.

## Governing principle

**Make the evidence easier to see. Do not make the candidate larger than the evidence.**
