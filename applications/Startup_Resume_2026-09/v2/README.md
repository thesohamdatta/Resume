# Startup Resume v2

Minimal one-page startup resume based on the supplied editorial resume reference.

## Files

- `resume_startup.tex` — main LaTeX source
- `TLCresume.sty` — local minimal style
- `resume_startup.pdf` — final rendered PDF

## Render

Run:

```bash
pdflatex -interaction=nonstopmode -halt-on-error resume_startup.tex
pdflatex -interaction=nonstopmode -halt-on-error resume_startup.tex
```

Keep build artifacts out of the repository. Validate that the final PDF is exactly one page and that extracted text is searchable.
