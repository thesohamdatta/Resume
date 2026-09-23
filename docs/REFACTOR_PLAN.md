# Resume System Refactor Plan

_Last reviewed: 2026-09-23_

## Current assessment

The repository has strong evidence discipline, but several generations of the system still coexist.

### Main problems

1. **Duplicated authority**
   AGENTS, CONTEXT, APPLY, stage files, and the voice skill repeat overlapping rules. Older track assumptions remain in places.

2. **External workstation dependencies**
   Some agent instructions still refer to local Windows paths. A cloned repository must not depend on the author's workstation layout.

3. **Application folders contain build machinery**
   Fello contains copied fonts, LaTeX styles/classes, multiple experimental .tex files, and compiler artifacts. Application state should not own template runtime assets.

4. **Evidence/presentation drift risk**
   facts.yaml, technical evidence, and boundaries are the correct source layers, but active resume files repeat facts and can drift.

5. **Template authority is not fully enforced**
   v3 is intended to be canonical, while older templates and application copies remain active-looking.

6. **No deterministic repository gate**
   A build script exists, but there is no lightweight validation for stale terminology, workstation paths, build junk, dummy content, or template drift.

## Target architecture

Candidate facts
→ Technical evidence
→ Claim boundaries
→ Application input
→ JD/company research
→ Evidence match
→ Positioning
→ Content selection
→ Humanized writing
→ Canonical template
→ Deterministic validation
→ PDF

## Canonical ownership

- Candidate facts: data/facts.yaml
- Technical proof: content/github/evidence.md
- Ownership/status limits: content/github/boundaries.md
- Voice: docs/voice.md
- Hard rules: DONT.MD
- Agent contract: AGENTS.md
- Repository map: MAP.md
- Orchestration: pipeline/run.md
- Stage contracts: pipeline/stages/
- Base tracks: versions/referral, versions/startup, versions/mnc
- Visual template: templates/v3
- Application state: applications/{Company}_{YYYY-MM}
- Research: research/
- History: archive/

## Implementation order

### Phase 1: Contract cleanup
Remove stale local/mid-level references from active instructions.
Remove external workstation paths.
Make referral/startup/mnc universal.
Make docs/voice.md the only voice authority.
Make templates/v3 the only active template.

### Phase 2: Application isolation
Keep application folders limited to inputs, state, final content, and application-specific artifacts.
Do not keep copied fonts, .sty files, compiler logs, .aux/.out files, or experimental template variants there.

### Phase 3: Deterministic validation
Validate:
- three active tracks
- no legacy track references in active docs
- no workstation paths
- no tracked compiler junk
- no dummy template content
- canonical template usage
- no horizontal section rules
- no CAD/3D-printing language in active base resumes
- one-page output when a LaTeX toolchain is available

### Phase 4: Evidence normalization
Add a small claim ledger:
claim_id → source → evidence_type → status → allowed_wording

Keep deep GitHub evidence separate.

### Phase 5: Tailoring engine
Make each application run reproducible:
input.md → pipeline_state.md → selected evidence → final resume.md → PDF

Do not create permanent base resumes for individual companies.

## Refactor rules

- Delete duplication before adding structure.
- Preserve useful history in archive/.
- Keep active instructions short.
- Put deterministic checks in scripts/CI.
- Keep contextual judgment in agents.
- Never weaken factuality rules during cleanup.
- Never change candidate history as a side effect of refactoring.

## Success criteria

A new session should be able to clone the repository and determine:
1. where the candidate facts live
2. where proof lives
3. which three tracks are active
4. how a JD is processed
5. how the resume is written and humanized
6. how the PDF is built
7. how the result is validated

without reading obsolete application runs or knowing the author's machine paths.
