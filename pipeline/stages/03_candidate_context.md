<!-- Stage 3: Candidate Context — Read by pipeline/run.md -->
# STAGE 03: CANDIDATE CONTEXT

**Your Role:** Read the candidate profile and extract relevant inventory.

## Inputs to Read:
- `data/facts.yaml`
- `content/github/evidence.md`
- `content/github/boundaries.md`

## Execution Rules:
1. ONLY list what is explicitly in `facts.yaml` OR `evidence.md`. Do not infer capabilities from tool names in the skills list alone. (Tool name = weak evidence; GitHub file path/PR number = strong).
2. Evidence type must be exactly one of: Firmware/Embedded | AI/ML | Full-Stack | Mobile | Voice AI | Hardware | Algorithm | Open Source.

## Output Target:
Append to `applications/{Company}_{YYYY-MM}/pipeline_state.md` under a new section `## Stage 03 — Candidate Inventory`

## Output Format (Exact Schema):
```
## Stage 03 — Candidate Inventory

### Strongest evidence (verifiable — GitHub repo, file path, or named artifact exists)
| Project | Evidence | Type |
|---|---|---|
| Aura | FreeRTOS I2S DMA audio capture at 16kHz (firmware/src/mic.cpp) | Firmware/embedded |

### Secondary evidence (real but lighter)
| Project | Evidence | Type |
|---|---|---|

### Hard boundaries (NEVER claim — from boundaries.md)
- [per project]

### Track-specific notes
[anything relevant to the requested track: startup/mnc/midlevel]
```
