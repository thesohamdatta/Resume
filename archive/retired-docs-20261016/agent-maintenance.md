# Resume Engine Maintenance

Use the existing engineering skills under `.agents/skills/` before introducing new ones.

## Recommended flow

1. Inspect `AGENTS.md`, `SPEC.md`, the relevant workflow, and source owners.
2. Use `improve-codebase-architecture` to identify concrete friction, then `codebase-design` to keep the module interface small and deep.
3. Use `implement-spec` or `tdd` for changes with testable behavior.
4. Use `code-review` against `main` before opening the pull request.
5. Run repository contract checks and inspect actual PDF output when resume rendering changes.

## Guardrails

- Prefer deterministic checks over more prompt text when a rule can be mechanically verified.
- Do not edit vendored skill copies or sync skills merely for appearance.
- Keep the canonical template and facts unchanged unless the task specifically requires an evidence-backed correction.
- Never delete, archive, or rewrite history without impact analysis and approval.
