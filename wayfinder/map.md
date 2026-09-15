# Wayfinder Map — Pipeline Simplification Map

Tracker: local-markdown (`wayfinder/` in this repo). Labels expressed as file fields.
Convention: map = `map.md`; tickets = `tickets/*.md` with header (Type, Status, Blocked-by).
Frontier = open + unblocked + unclaimed tickets. Claim by setting `Claimed-by` before work.
Never resolve more than one ticket per session (research tickets excepted).

## Destination

A locked build spec for the simplest pipeline that reliably produces an excellent,
evidence-backed, tailored resume — one document a later session can execute without
re-deciding anything. Planning only; no execution in this map.

## Notes

- Domain: this repo (`D:\download\resume`). Every session consults `AGENTS.md` + `MAP.md` first.
- Standing preference: user decides, agent proposes with a recommendation. One question at a time (grilling discipline).
- Prior art: single-session review last turn implemented the `§E` engine-prefix rename (lesson 9) — numbering is settled, structure is not.
- Ticket types: grilling (HITL, default), research (AFK subagent), prototype (HITL), task (either).

## Decisions so far

- [Entry-Point Consolidation](tickets/02-entry-consolidation.md) — `run.md` owns orchestration, README is a stub; executed 2026-09-15 on direct order.

## Not yet specified

- Resume-content quality bar: how "excellent" is judged in the spec (beyond Stage 10 as-is?).
- Template future: v2 vs v3, shared-fonts rule durability, who owns template choice per run.
- Voice authority boundary: `D:\download\voice\voice.md` governs tone today — does the spec keep an external-dir dependency?
- Per-stage token budgets and failure-handling behavior (retry? stop? degrade?).
- Whether the four entry docs' audiences (sender / orchestrator / human / researcher) stay distinct.

## Out of scope

- Building/executing the simplified pipeline (map ends at the locked spec; execution is a fresh effort).
- Rule-by-rule content audit of `DONT.MD` (66 rules stay authoritative throughout this map).
- New resume tracks or new output formats.
