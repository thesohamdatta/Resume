# Ticket — Entry-Point Consolidation

- Map: [Pipeline Simplification Map](../map.md)
- Type: grilling (HITL)
- Status: CLOSED (executed 2026-09-15 on direct user order — decision and execution collapsed into one)
- Claimed-by: — (frontier)

## Question

Four docs re-explain orchestration (`pipeline/APPLY.md`, `pipeline/run.md`,
`pipeline/README.md`, `research/SWARM_RESEARCH.md`) and fixes rot across them. Decide
the entry-point shape for the spec: e.g. one send-as-is doc with the rest as appendices;
or keep four with a stated audience per doc and a single ownership rule. Constraint:
`memory/lessons.md` cites `pipeline/README.md` twice as evidence — history is not rewritten,
so deletion requires re-pointing rationale, not silent edits.

## Resolution (2026-09-15)

`run.md` is the single orchestration reference (gained dependency graph + both design
decisions, moved verbatim); `pipeline/README.md` is now an index stub (quick-start +
audience table, no restated orchestration); `APPLY.md`/`SWARM_RESEARCH.md` untouched
(distinct jobs); two lesson evidence pointers re-pointed to `run.md` with rationale
logged, history otherwise intact.
