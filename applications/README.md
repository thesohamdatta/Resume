# Application runs

Each new application starts with one `input.md` using [`_template/input.md`](_template/input.md).
The input names the company, exact role, mode, and full job description. Research remains linked
from the input or its run notes; it does not become a second candidate-truth source.

A completed run stores its standard deliverables in `output/`: `resume.tex`, `extracted.txt`,
`audit.md`, and `Soham Datta.pdf`. A run is current-contract only after
`pipeline/check_run.sh applications/{Name}_{YYYY-MM}` passes. The validator currently exercises
`SWE_MNC_2026-10` as its repository example.

## Existing runs

Older runs are retained in place because their contents include application-specific history.
Their folder shape does not imply that they pass the current contract.

| Status | Runs |
|---|---|
| Contract example | `SWE_MNC_2026-10` |
| Current-format snapshots, not in the repository check | `SWE_Referral_2026-10`, `SWE_Startup_2026-10`, `Accenture_DataScience_2026-10`, `Crisil_GenAI_Intern_2026-10`, `Virtusa_Architect_2026-10` |
| Partial, draft, or legacy application material | `Crisil_2026-10`, `Fello_2026-09`, `HCLTech_2026-09`, `LexsiLabs_2026-09`, `Myntra_2026-09`, `Noise_Eng_2026-09`, `Noise_Fullstack_2026-09`, `Noise_PM_2026-09`, `PNGJewellers_2026-09`, `Resume_Canonical_2026-09` |

Do not move or remove an older run as part of routine cleanup. If it is retired, record the
decision and preserve its history under `archive/`.
