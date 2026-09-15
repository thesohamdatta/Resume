---
name: latex-resume-render
description: >
  Render a tailored resume into a PDF via a user-supplied LaTeX template or design
  reference. Use when the user says 'use this template', pastes a .tex path, asks to
  compile/render a resume PDF, demands a LaTeX version, or wants a design from Figma,
  Pinterest, or another image recreated as their resume.
license: MIT
metadata:
  author: Soham Datta
  version: "1.0.0"
allowed-tools:
  Read: "*"
  Edit: "*"
  Write: "*"
  Bash: "pdflatex* xelatex* lualatex*"
---

# LaTeX Resume Render

Turn a tailored resume `.md` into a 1-page PDF using the user's template or design
reference. Fork execution: runs isolated, user steers by re-invoking.

## Inputs

- `$resume_md`: tailored resume markdown (facts-anchored, Stage-07-passed preferred)
- `$template`: `.tex` template path, OR design image/URL (Figma, Pinterest, other)
- `$out_dir`: run folder for `.tex` + `.pdf` output

## Goal

A 1-page searchable PDF + its `.tex` source in `$out_dir`, zero dummy remnants,
zero invented facts. Success artifact: the PDF path.

## Steps

### 1. Inspect template, pick engine

Read the `.tex` fully. If it loads `fontspec` (or custom `.otf` fonts) the engine is
**xelatex** — pdflatex will fail. Otherwise **pdflatex**. Confirm the binary exists;
stop with the missing-toolchain name if not. Note required support files
(`.cls`, `.sty`, `fonts/`).

**Success criteria**: engine named, toolchain confirmed present.

### 2. Adapt content into the template

Replace every dummy row (names, links, bullets, certs) with `$resume_md` content.
Escape `& % # _` in text. Contact block uses confirmed email/phone only — never
invent handles. Omit sections with no anchored proof (e.g. Certifications) rather
than shipping placeholders. If `$template` is a design image, recreate its layout
cues (sections, order, emphasis) in LaTeX instead of filling a `.tex`.

**Success criteria**: grep finds no dummy remnants (Jane/Acme/lorem/W3C/example).

### 3. Resolve support files

Copy `.cls`/`.sty` beside the output `.tex`. Fonts: reference one shared dir, never
re-copy per run. Missing LaTeX packages (e.g. FontAwesome font): write a minimal
local `.sty` stub covering only the glyphs used. Never edit `templates/` pristine
copies or restore points.

**Success criteria**: all `\RequirePackage`/`\input` targets resolve locally.

### 4. Compile, enforce 1 page, clean

Compile with the chosen engine (`-halt-on-error`). While output exceeds 1 page:
cut the lowest-signal block first, recompile, log each cut. Then delete
`.aux`/`.log`/`.out`.

**Success criteria**: PDF is exactly 1 page; no build-junk files remain.
**Rules**: 1-page is enforced during the build, not waived. Log every trim.

### 5. Verify PDF

Read the PDF back: text extracts cleanly (ATS-readable), all sections present,
project links live, no underline/box artifacts unless requested, contact correct.

**Success criteria**: verified PDF path reported to the user.
