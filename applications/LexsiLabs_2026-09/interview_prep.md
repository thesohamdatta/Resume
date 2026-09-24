# Interview Prep — Lexsi Labs, AI Agent Intern

## Pitch
I build agentic systems with verification baked in — a 5-stage engineering harness with automated gates, a multi-model evaluation pipeline, and applied voice agents with tool calling — and I contribute back to the open-source ecosystems I build on.

## Likely questions
| Question | Answer angle | Evidence anchor (repo/PR/file) |
|---|---|---|
| Walk us through Mia's harness | Stages, gates, why each gate exists, what failures it caught | Mia repo, ADR-0001 |
| How do you evaluate agent output? | Cross-model critique, agreement viz, inspectable stages | LLM-Council repo |
| How does John use tools? | LiveKit agent, calendar/tasks/telephony calls, barge-in path | John repo |
| Failure modes you've seen in agents? | Provider outages (→ voicecoder fallback), daemon fragility (→ ADR-0001), speaker drift (→ clustering fix) | voicecoder, Mia, Omi PR #8919 |
| How do you read a new large codebase? | Omi: 21 root-caused issues before PRs; RFC-first | Omi issues #8438, #12360 |
| Alignment/interpretability background? | Gap defense below; eval-adjacent, honest about depth | — |
| Enterprise/tabular data experience? | Gap defense below | — |
| Why Lexsi, why part-time remote? | OSS culture fit (AlignTune/XAI Evals are public work), schedule fit | — |

## Gap defenses
- **Alignment/interpretability theory:** not claimed. Framing: no safety papers; closest verified work is evaluation infrastructure (cross-model critique, verification gates) — interest in the area, depth to be built on the job, eagerness only.
- **Enterprise/tabular data:** not claimed. Framing: data work so far is memory graphs, pgvector retrieval, and transcription pipelines on personal-scale systems; no enterprise data scale claimed.
- **Long-horizon agents:** partial. Framing: Mia's 5-stage runs are bounded multi-step, not long-horizon; honest about the gap, architecture thinking transfers.

## Questions for them
1. Which of the three intern tracks has the most urgent open problems right now — applied, R&D/eval, or tooling?
2. How do AlignTune and XAI Evals get used internally — are interns expected to contribute to those repos directly?
3. What does evaluation infrastructure look like day-to-day — benchmarks run in CI, ad-hoc red-teaming, or both?
4. How are part-time remote interns integrated — async-first, or overlapping hours with Mumbai?
5. What would a strong intern artifact look like at the end — paper, merged OSS tool, or production component?
