# Pipeline Grilling Session (archived)

Historical artifact. Recovered from `.claude/scratch/pipeline_grilling_session.html` on the
`refactor/resume-engine-v1` branch. This is the domain-modeling and architectural review that
preceded the current specification; it is provenance, not active guidance. The active system
definition lives in `SPEC.md`.

---

Pipeline Grilling Session 

 Resume Pipeline Grilling Session 
 Domain modeling + architectural decisions + edge cases 

 🎯 Session Scope 
 Improving the 10-stage resume pipeline through: 

 Terminology precision (glossary challenges) 
 Edge case scenario testing 
 Architectural decision review 
 Voice.md integration validation 

 📖 Domain Model Review 

 Current Glossary (CONTEXT.md) 

 Q1: What is a "Track"? 
 Your glossary defines three tracks: startup , mnc , mid-level . 
 Challenge: Are these three different resume formats (layout/style), three different targeting strategies (audience/tone), or three different output artifacts (different facts emphasized)? 
 Code says: versions/{track}/_base.md suggests structural templates. 
 voice.md says: Voice Matrix applies different bullet formulas per track (startup/MNC/mid). 
 Clarify: Is a track a presentation variant (same facts, different layout) or a selection strategy (different facts foregrounded)? 

 Q2: What is "Evidence"? 
 You use "evidence" in multiple contexts: 

 content/github/evidence.md — technical proof (file paths, PRs, algorithms) 
 Stage 04 — Evidence Matcher (STRONG/MODERATE/WEAK) 
 Stage 06 — "evidence-first bullets" 
 voice.md — "Evidence Boundaries" 

 Challenge: Is "evidence" the raw technical detail (before it enters resume), the matched proof for a JD requirement , or the verifiable claim in the resume ? 
 Proposed distinction: 

 Proof = raw technical detail (evidence.md, boundaries.md) 
 Match = JD requirement ↔ proof mapping (Stage 04) 
 Claim = resume bullet anchored in proof (Stage 06, 07) 

 Q3: What is "Positioning"? 
 Stage 05 is called "Positioning Strategy" and produces: 

 Primary hook (company-specific) 
 Cover letter structure 
 What to foreground/cut 

 Challenge: Is positioning a one-time strategic decision per company , or a per-application framing ? Can the same company have multiple positionings if targeting different roles? 
 Scenario: Company X has two openings — "AI Engineer" and "Staff AI Engineer". Same positioning? 

 Q4: Stage 10 vs voice.md conflict 
 Your pipeline/run.md line 82 still says: 
 "Reads: Stage 09 outputs + both slop skills (stop-slop for resume, no-ai-slop for cover letter)." 
 But we just unified Stage 10 to use voice.md directly. 
 Issue: run.md is now stale. Design decision comment line 145-150 also references the old dual-skill approach. 
 Fix needed: Update run.md to reflect voice.md unified approach. 

 🧪 Edge Case Scenarios 

 Scenario 1: JD changes mid-application 
 Setup: You run the pipeline for Company X with JD version 1. Two days later, they update the JD (new required skill added). 
 Questions: 

 Does applications/{Company}_{YYYY-MM}/input.md get updated with new JD? 
 Do you re-run the full pipeline, or just Stage 02 → Stage 10? 
 What happens to pipeline_state.md ? Append new sections or overwrite? 

 Current design: No clear guidance in run.md or APPLY.md . 

 Scenario 2: Stage 07 FAIL with no fix path 
 Setup: Stage 07 Factuality Checker flags a claim as FAIL: "No anchor in facts.yaml or evidence.md". 
 But: The claim is actually true — it's just not documented yet. 
 Questions: 

 Does the user manually add to evidence.md, then re-run Stage 07? 
 Or does Stage 07 have a "defer" option (mark as needs-evidence, let it through with warning)? 
 What if the true fact can't be verified externally (e.g., internship project with no public artifact)? 

 Current design: Hard stop on any FAIL (line 70). No escape hatch. 

 Scenario 3: Multiple applications to same company 
 Setup: Apply to Company X in September (AI Engineer role). Apply again in November (Senior AI Engineer role). 
 Questions: 

 Do both use research/companies/{Company}.md ? (Yes, probably.) 
 Do both live in applications/Company_2026-09/ and applications/Company_2026-11/ ? (Yes, per naming.) 
 But: versions/{track}/resume_Company.md has NO date. Second application overwrites first? 

 Issue: versions/{track}/resume_{Company}.md naming loses temporal context. You can't compare "what we sent in Sept" vs "what we sent in Nov". 
 Proposed fix: Either add date to versions path, or keep outputs ONLY in applications/ folder. 

 Scenario 4: Voice.md banned word in facts.yaml template 
 Setup: facts.yaml has a pre-written bullet template containing "leveraged" (voice.md banned word). 
 Questions: 

 Does Stage 06 (Writer) use the template as-is and let Stage 10 fix it? 
 Or does Stage 06 apply voice.md rules upfront? 
 What if Stage 10's fix changes the claim strength (drift)? 

 Current design: Stage 06 loads voice.md "as tone authority" but still uses facts.yaml templates. Stage 10 fixes slop. Potential drift between stages. 

 Scenario 5: Parallel Stage 01+02+03 — one fails 
 Setup: Stage 01 (Company Research) hits API rate limit and fails. Stage 02+03 complete successfully. 
 Questions: 

 Does the pipeline abort entirely? 
 Or does Stage 04 (Evidence Matcher) proceed with incomplete company context? 
 How does pipeline_state.md reflect partial completion? 

 Current design: run.md says "run all three simultaneously" but doesn't specify failure handling. 

 🔍 Architectural Tensions 

 Tension 1: Facts vs Evidence vs Claims 
 Problem: Three overlapping sources of truth: 

 data/facts.yaml — "canonical facts" (dates, titles, companies, bullets) 
 content/github/evidence.md — technical depth (file paths, algorithms) 
 content/github/boundaries.md — constraints (what NOT to claim) 

 Confusion point: Stage 06 says "read evidence.md BEFORE facts.yaml" — why are they separate? Why not one master source? 
 Hypothesis: facts.yaml is biographical skeleton (dates, titles). evidence.md is technical detail (code, PRs, implementations). boundaries.md is negative constraints (don't claim X). 
 Clarity needed: When does a new piece of information go into which file? 

 Tension 2: Stage 09 vs Stage 10 — redundant polish? 
 Stage 09: "Final Editor" — reads Stage 07+08 audit, makes edits. 
 Stage 10: "Slop-Free Polish" — applies voice.md rules, drift gate. 
 Question: Why two editing stages? Could Stage 09 be merged into Stage 10? 
 Current justification (memory/lessons.md line 11): "Stage 09 keeps only a quick pre-pass. Stage 10 is terminal." 
 Counter-argument: If Stage 10 is authoritative, why does Stage 09 exist? What can Stage 09 do that Stage 10 cannot? 
 Possible answer: Stage 09 handles structural fixes (ATS issues, factual corrections). Stage 10 handles language polish (voice, slop). Different concerns. 

 Tension 3: Human checkpoints — when to stop? 
 Your run.md has 4 human checkpoints: 

 After Stage Review When to Stop 

 Stage 05 Primary hook If hook is generic 
 Stage 07 Factuality FAILs If any FAIL exists (hard gate) 
 Stage 09 Final resume If pre-pass missed something 
 Stage 10 Slop polish log If drift FAIL 

 Question: Are these checkpoints approval gates (pipeline waits for human "proceed") or audit points (human can review but pipeline continues)? 
 Current wording: Stage 05 says "Type 'proceed' to continue" (approval gate). Stage 07 says "stop" (hard gate). Stage 09/10 unclear. 
 Design choice needed: Should the pipeline be fully automated (human reviews outputs after completion) or human-in-the-loop (waits at each gate)? 

 💡 Improvement Recommendations 

 Recommendation 1: Unify Stage 09 + Stage 10 
 Rationale: Two separate editing stages create confusion about which is authoritative. Stage 10 already handles voice, slop, and drift — it can also handle ATS fixes. 
 Proposed merge: 

 Keep Stage 08 (ATS Reviewer) as analyzer only 
 Delete Stage 09 (Final Editor) 
 Expand Stage 10 to handle ATS fixes + voice.md polish + drift gate 
 Rename Stage 10 to "Final Polish" (not "Slop-Free" — broader scope) 

 Benefit: Single authoritative editing stage. Clearer pipeline flow. 

 Recommendation 2: Add date to output filenames 
 Problem: versions/{track}/resume_Company.md overwrites previous applications to same company. 
 Proposed fix: Change output to versions/{track}/resume_Company_YYYY-MM.md 
 Benefit: Temporal auditability. Can compare what was sent in Sept vs Nov. 
 Alternative: Keep outputs ONLY in applications/{Company}_{YYYY-MM}/ folder. Don't duplicate in versions/ . 

 Recommendation 3: Clarify facts.yaml vs evidence.md split 
 Add to CONTEXT.md glossary: 

 Biographical facts (facts.yaml): dates, titles, companies, education, certifications — things that go on every resume regardless of role. 
 Technical proof (evidence.md): file paths, function names, algorithms, PR numbers, test counts — deep technical detail used to write evidence-rich bullets. 
 Constraints (boundaries.md): negative rules — what NOT to claim (e.g., "never say 'built Omi backend from scratch'"). 

 Decision rule: If it's a date or title → facts.yaml. If it's technical depth → evidence.md. If it's a don't claim X → boundaries.md. 

 Recommendation 4: Update run.md for voice.md integration 
 Action items: 

 Update line 82: change "both slop skills" → "voice.md unified" 
 Update lines 145-150: remove dual-skill design decision, replace with voice.md rationale 
 Update Step 8 description to mention voice.md context detection 

 Recommendation 5: Add Stage 07 "defer" option 
 Problem: Stage 07 hard-stops on any FAIL, even if the claim is true but just not documented yet. 
 Proposed enhancement: Stage 07 output has three states per claim: 

 PASS — anchored in facts.yaml or evidence.md 
 FAIL — no anchor, must fix or delete (hard stop) 
 DEFER — claim marked as "needs evidence" but allowed to proceed with warning flag 

 Use case: True internship claim with no public artifact. Flag as DEFER, include in resume with asterisk, add to evidence.md later. 

 📝 ADR Candidates 

 ADR-0001: Evidence-first bullet writing 
 Status: Decided (documented in pipeline/run.md line 151, memory/lessons.md line 7) 
 Context: Stage 06 must choose between two sources: pre-written bullets in facts.yaml vs raw technical detail in evidence.md. 
 Decision: Read evidence.md BEFORE facts.yaml. Bullets derive from evidence technical depth (file names, algorithms), not templates. 
 Rationale: Evidence-first surfaces invisible technical detail. Templates are skeletal — evidence is specific. 
 Consequences: Bullets are more technical, more credible, but require evidence.md to be complete. 
 Recommendation: This is a good ADR candidate — hard to reverse, surprising without context, real trade-off. Consider writing formal ADR. 

 ADR-0002: voice.md as single source of truth (NEW) 
 Status: Just decided (2026-09-15) 
 Context: Stage 10 used two separate skills (stop-slop for resume, no-ai-slop for cover). Maintenance burden, context confusion. 
 Decision: Unify Stage 10 to load voice.md directly. Context-aware via Voice Matrix. Single tone authority. 
 Rationale: One file to update, no skill dependencies, Voice Matrix auto-selects based on track (startup/MNC/mid). 
 Consequences: Simpler maintenance, but voice.md must stay complete. Stage 10 now has more responsibility. 
 Recommendation: Write this as ADR-0002 to document the unified approach. 

 ADR-0003: Why Stage 09 + Stage 10 are separate (QUESTIONABLE) 
 Status: Implicit (not formally documented) 
 Context: Two editing stages — Stage 09 (Final Editor) and Stage 10 (Slop-Free Polish) — seem redundant. 
 Claimed rationale: Stage 09 handles structural fixes (ATS, factuality). Stage 10 handles language polish (voice, slop). 
 Question: Is this separation really necessary? Or can Stage 10 do both? 
 Recommendation: Either write formal ADR defending the split, OR merge them per Recommendation 1. 

 🎬 Next Steps 

 ✅ Quick Wins (do now) 

 Update run.md to reflect voice.md integration 
 Add glossary clarifications to CONTEXT.md (Track, Evidence, Positioning) 
 Fix output filename collision (add date or move to applications/) 

 🤔 Decisions Needed 

 Merge Stage 09+10 or keep separate? (need rationale) 
 Add Stage 07 DEFER option or keep hard stop? 
 Pipeline = fully automated or human-in-the-loop? 

 📋 ADRs to Write 

 ADR-0001: Evidence-first bullets (formalize existing decision) 
 ADR-0002: voice.md unified (document new decision) 
 ADR-0003: Stage 09+10 split (IF keeping separate) 

 🧪 Edge Cases to Test 

 JD changes mid-application (re-run protocol) 
 Stage 07 FAIL with unverifiable-but-true claim 
 Multiple applications to same company (output naming) 
 Parallel stage failure handling (Stage 01 rate limit) 

 