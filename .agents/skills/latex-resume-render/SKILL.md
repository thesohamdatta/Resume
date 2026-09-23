---
name: latex-resume-render
description: Build the canonical one-page resume PDF from a verified resume source and the repository template.
version: "2.0"
---

# LaTeX Resume Render

This skill owns document rendering, not candidate facts.

## Inputs

- verified resume markdown or approved content source
- target track: `referral`, `startup`, or `mnc`
- canonical template: `templates/v3/`
- output directory

## Rules

1. Read the full canonical template before editing.
2. Use `templates/v3/` as the only active visual template.
3. Keep critical information as real text.
4. Preserve hyperlinks.
5. Do not introduce section rules, decorative graphics, skill bars, photos, or parser-hostile layout.
6. Do not copy fonts, classes, or styles into application folders.
7. Use a local build workspace for compiler output.
8. Never modify canonical facts during rendering.

## Build

Use XeLaTeX when the canonical template requires `fontspec`.

Compile with `-halt-on-error`.

Run the compiler inside a temporary build directory so `.aux`, `.log`, and `.out` files never enter the repository.

## One-page gate

The final PDF must be one page unless the application explicitly requires a different length.

If it exceeds one page:

1. remove the lowest-signal bullet
2. remove repetition
3. reduce wording
4. remove low-value project detail
5. only then adjust spacing/typography

Never make text illegibly small.

## PDF QA

Verify:

- PDF opens
- exactly one page
- text is selectable
- important terms are searchable
- links are present
- no blank page
- no clipping/overflow
- no dummy content
- no section rules
- contact information is correct

The PDF is an output artifact. The repository source remains the canonical document source.
