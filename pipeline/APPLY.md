# Application Run

Use this file as the only application-level setup. The actual generation contract is engine/PROMPT.md.

## Input

- Company: [Company]
- Role: [Exact role]
- Track: [referral | startup | mnc]
- JD: paste the complete job description
- Template: path to LaTeX/template/design
- Notes: optional user instructions

Save as: applications/[Company]_[YYYY-MM]/input.md

## Run

The agent should:

1. Read engine/PROMPT.md.
2. Read engine/RULES.md.
3. Read the canonical evidence sources.
4. Analyze the JD.
5. Map requirements to verified evidence.
6. Select foreground/support/omit content.
7. Write the resume.
8. Render it using the supplied template.
9. Run FACT, FIT, READ, and PARSE checks.
10. Write the final files to applications/[Company]_[YYYY-MM]/output/.

## Output

```text
output/
├── resume.tex
├── resume.pdf
├── extracted.txt
└── audit.md
```

## Human review

Only stop for a question when a missing fact materially changes:

- ownership
- dates/title
- metric
- project scope
- production status
- certification status

Do not stop for cosmetic uncertainty. Make the smallest supported decision and record it in the audit.