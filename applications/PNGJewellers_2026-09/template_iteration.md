# PNG Jewellers — Figma Template Iteration

Source template: A4-Resume.pdf supplied in conversation.

## What the template actually gives us

A4 portrait, two-column editorial layout.

### Left column
1. About Me
2. Education
3. Projects
4. Social Media

### Right column
1. Experience
2. Social Media continuation

Header:
- Name
- Portfolio / E-mail / phone
- Portrait on the right

The supplied template currently contains placeholder education copy, a placeholder "Social Media" block, visible "-> Link" labels, and the old name "Soham Karande". These are template/demo artifacts and must not survive in the final PNG version.

## Iteration principles

1. Preserve the visual system. Do not redesign the Figma template.
2. Reduce technical density. The candidate should read as an applied AI/product engineer, not an infrastructure specialist.
3. Put customer/product relevance ahead of implementation detail.
4. Keep the right column dominant because Experience is the strongest evidence.
5. Keep Projects short enough that the left column breathes.
6. Remove redundant social links from the body if they already appear in the header.
7. Use project titles as links instead of visible "-> Link" labels.
8. Do not show raw GitHub URLs.
9. Do not mention 3D printing, CAD enclosures, FreeRTOS, I2S, Opus, Kubernetes, pgvector, or long Omi issue/PR lists in this PNG version.
10. Keep technically credible terms where they help recognition: computer vision, LLMs, TensorFlow, Python, TypeScript, voice interfaces.
11. Do not invent a PNG AI job description. The current official careers page does not show an AI opening.
12. Preserve white space. Empty space is preferable to compressed text.

## Recommended header

Name:
Soham Datta

Role line:
AI Engineer · AI & Digital Products

Meta:
Pune, India · E-mail · LinkedIn · GitHub

Keep the portrait only if it is part of the intended final Figma design. Do not enlarge it.

## Recommended left column

### About Me
AI/ML engineer building practical software across computer vision, LLMs, voice interfaces, and multimodal products. Interested in applying AI to better digital and customer experiences.

Target: 3–4 short lines in the existing text width.

### Education
Savitribai Phule Pune University
B.E. Artificial Intelligence & Machine Learning
2022 – Jun 2026 · Pune

Remove the placeholder paragraph entirely.

### Projects

#### Mia · Personal AI Engineering OS
TypeScript · Bun · LLMs · Vitest
Created a local-first tool for structured AI engineering workflows, model integration, and automated checks.
Added adapters for Claude, Codex, and local models with persistent state tracking.

#### LLM-Council · Multi-Model AI
Python · FastAPI · React
Developed a system that compares responses from multiple LLMs to support structured evaluation.
Added a three-stage review flow for inspecting model outputs.

#### Voice AI Systems · Realtime AI
LiveKit · WebRTC · Python
Developed realtime voice agents with turn detection and tool calling for assistant workflows.
Connected a mobile client to a Python voice agent for interactive tasks.

### Bottom-left replacement
Replace the current Social Media block with either:

Preferred:
CERTIFICATIONS
AWS Educate AI/ML Scholar
Google Generative AI
AWS Cloud Practitioner

Only include these after exact certificate titles are verified. Keep each to one line.

If certification verification is not complete, use:
LINKS
LinkedIn · GitHub · Portfolio

Do not duplicate links if they are already visible in the header.

## Recommended right column

### Experience

#### Aura · Founder
Jun 2025 – Present · Pune

- Developed a wearable AI product combining multimodal capture, AI services, memory, and companion software.
- Integrated transcription, context extraction, knowledge processing, and retrieval into one product workflow.
- Investigated a Windows WebGL performance issue in the Omi ecosystem; the diagnosis was later fixed downstream.

#### AI & ML Intern · AICTE via Google
Oct 2024 – Dec 2024 · Remote

- Developed lightweight computer-vision models with TensorFlow and Google ML Kit for on-device classification.
- Applied transfer learning and data augmentation for mobile-constrained inference.

#### Associate · Reliance
Jul 2024 – Oct 2024 · Pune

- Managed customer-service workflows across memberships, vouchers, exchanges, documentation, and follow-up.
- Coordinated with store, HR, brand, and management teams to resolve customer issues.

#### Research Assistant · PES Modern College
Sep 2023 – Mar 2024 · Pune

For the PNG version, keep this role only if the Figma page still has comfortable vertical space.

Preferred compact version:
- Researched and organized digital learning resources, papers, and open courseware for the college archive.
- Ran workshops helping students discover resources such as arXiv and open courseware.

If the page becomes crowded, remove this role before shrinking the font.

## Why this version fits PNG

PNG's current careers page says the company has been expanding its online presence and has operated an e-commerce store since 2013. Its stated values include collaboration and customer centricity. The public company material also shows a significant digital/e-commerce focus.

Therefore the resume should make three things immediately visible:
1. Can build AI-enabled software.
2. Understands products and real users.
3. Has direct retail/customer-service exposure.

This is why Reliance stays even though it is not a technology role.

## Character and layout budget

Header role: <= 35 characters
About Me: <= 250 characters
Experience bullet: target 90–125 characters
Aura: 3 bullets max
Other roles: 2 bullets max
Project: 2 bullets max
Project title: <= 42 characters where possible
Tech line: <= 45 characters
Certification line: <= 32 characters

Do not solve overflow by reducing font size first.
Order of compression:
1. Remove redundant words.
2. Remove low-value bullet.
3. Remove PES role if necessary.
4. Reduce project descriptions.
5. Only then adjust typography.

## Final content hierarchy

1. Aura / Founder
2. AICTE via Google
3. Reliance
4. Projects
5. Education
6. Certifications
7. Skills

The visual template should remain unchanged. The iteration is primarily content hierarchy, density, and wording.
