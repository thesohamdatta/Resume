# Domain Docs

How engineering skills should consume this repository's domain documentation.

## Before exploring

- Read `AGENTS.md` for the repository contract and reading order.
- Read `SPEC.md` and the relevant section of `pipeline/README.md` for resume-engine behavior.
- Read relevant ADRs under `docs/adr/` if they exist.
- Read the job-search specification in GitHub issue #62 and relevant implementation notes when working on job search.
- If glossary or ADR files do not exist, proceed without creating them just for setup.

## Layout

This is a single-context repository. If a glossary is added later, use root `GLOSSARY.md`; architectural decisions belong under `docs/adr/`.

## Use the project's language

Preserve established terms and ownership:
- The Resume Engine is the existing selection-and-compilation pipeline.
- A job-search posting is one source listing.
- An opportunity is the underlying vacancy that may have multiple postings.
- An application is the user's pursuit record and lifecycle.
- Candidate facts, technical evidence, and claim boundaries remain separate sources of truth.

Use the definitions in the spec and existing source files; do not create competing definitions.
