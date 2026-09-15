# LaTeX Templates

- **`v2-comma-titles/`** (sibling folder) — TLCresume base, comma title style (`Founder, Aura`), 4-bullet Aura. Newer draft (`resume_preview_v2.png`). Build: `pdflatex resume.tex` inside the folder.
- **`v3/`** (this folder) — resume-openfont base (Lato/Raleway, Deedy-style). Build: `xelatex resume.tex` (fontspec — pdflatex will NOT work). Fonts live in `v3/fonts/` — the shared copy; run folders must reference it, never re-copy.
- **`archive/templates-v1-dash-titles-20260915/`** — retired 2026-09-15: older `---`-title draft + `original_backup/` pristine restore point. Recoverable, never referenced by the pipeline.

Do not commit `.aux` / `.log` / `.out` files. Previews: `resume.pdf` + `resume_preview*.png` per live variant.
