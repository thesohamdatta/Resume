# Mode versions

Each canonical mode has one editable content file and one generated LaTeX snapshot:

| Mode | Editable content | Generated TeX |
|---|---|---|
| Startup | [`startup/_base.md`](startup/_base.md) | [`startup/resume.tex`](startup/resume.tex) |
| MNC | [`mnc/_base.md`](mnc/_base.md) | [`mnc/resume.tex`](mnc/resume.tex) |
| Referral | [`referral/_base.md`](referral/_base.md) | [`referral/resume.tex`](referral/resume.tex) |

Edit `_base.md`. Regenerate with `python3 pipeline/render_mode.py <mode> --write`; the
repository validator checks that the generated TeX is current. The mode configuration lives in
`modes/{mode}.yaml`. Application-specific selections belong in their run folder, not here.
