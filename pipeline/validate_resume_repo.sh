#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
fail() { echo "FAIL: $*" >&2; exit 1; }
ok() { echo "PASS: $*"; }

# Fail if a pattern matches any of the given files (paths relative to $ROOT).
assert_absent() {
  local desc="$1" pattern="$2"; shift 2
  local hits
  hits="$(cd "$ROOT" && grep -rnE --binary-files=without-match "$pattern" -- "$@" 2>/dev/null || true)"
  [ -z "$hits" ] || { echo "$hits"; fail "$desc"; }
  ok "$desc"
}

MODES=(referral startup mnc)

# --- canonical module set ---
CANON=(
  AGENTS.md
  SPEC.md
  RESUME_RULES.md
  pipeline/README.md
  README.md
  DONT.MD
  docs/voice.md
  data/facts.yaml
  content/github/evidence.md
  content/github/boundaries.md
  modes/referral.yaml
  modes/startup.yaml
  modes/mnc.yaml
  templates/v3/resume-openfont.cls
  templates/v3/resume.tex
  pipeline/check_run.sh
  pipeline/check_audit.py
)
for f in "${CANON[@]}"; do
  test -f "$ROOT/$f" || fail "missing canonical module: $f"
done
ok "canonical module set present"

# --- specification contract ---
# The spec is the system definition; the contract must reference it and it must not drift.
grep -qF 'SPEC.md' "$ROOT/AGENTS.md" \
  || fail "AGENTS.md does not reference SPEC.md (the system definition owner)"
ok "AGENTS.md references SPEC.md"

spec_defs="$(grep -oE '^\s*-\s*\*\*REQ-[A-Z]+[0-9]+' "$ROOT/SPEC.md" \
  | grep -oE 'REQ-[A-Z]+[0-9]+' | sort)"
if [ -z "$spec_defs" ]; then
  fail "SPEC.md defines no requirements (expected '- **REQ-...' definitions)"
fi
spec_dups="$(printf '%s\n' "$spec_defs" | uniq -d)"
[ -z "$spec_dups" ] || { echo "$spec_dups"; fail "SPEC.md defines a requirement id more than once"; }
ok "SPEC.md requirement ids are unique"

assert_absent "SPEC.md contains no prior-application reference" \
  '[Aa]mazon|[Aa]ccenture|applications/[A-Za-z0-9]+_20[0-9][0-9]-' \
  SPEC.md

# --- three modes: config + base + template usage ---
for mode in "${MODES[@]}"; do
  test -f "$ROOT/modes/$mode.yaml" || fail "missing mode config: $mode"
  test -f "$ROOT/versions/$mode/_base.md" || fail "missing $mode base"
  test -f "$ROOT/versions/$mode/resume.tex" || fail "missing $mode resume.tex"
  grep -qF '\documentclass{../../templates/v3/resume-openfont}' "$ROOT/versions/$mode/resume.tex" \
    || fail "$mode does not use the canonical template"
  grep -qE '^name_key:' "$ROOT/modes/$mode.yaml" || fail "$mode config missing name_key"
done
ok "all three modes have a config, a base, and use templates/v3"

# --- modes are exactly the canonical three (REQ-P2) ---
expected_modes="$(printf '%s\n' "${MODES[@]}" | sort)"
mode_files="$(cd "$ROOT" && find modes -maxdepth 1 -name '*.yaml' | sed 's#.*/##; s#\.yaml$##' | sort)"
[ "$mode_files" = "$expected_modes" ] \
  || { echo "$mode_files"; fail "modes/ must contain exactly: ${MODES[*]} (no fourth or retired mode)"; }
ok "mode configs are exactly the canonical three"

version_dirs="$(cd "$ROOT" && find versions -maxdepth 1 -mindepth 1 -type d | sed 's#.*/##' | sort)"
[ "$version_dirs" = "$expected_modes" ] \
  || { echo "$version_dirs"; fail "versions/ must contain exactly: ${MODES[*]} (no fourth or retired mode)"; }
ok "version directories are exactly the canonical three"

# --- fixed section order, stated once (REQ-O2) ---
ORDER_TEXT='Header / Contact → Summary → Experience → Projects → Education → Technical Skills'
order_owners="$(cd "$ROOT" && grep -lF "$ORDER_TEXT" -- \
  AGENTS.md SPEC.md README.md RESUME_RULES.md DONT.MD docs/voice.md pipeline/README.md 2>/dev/null || true)"
order_count="$(printf '%s\n' "$order_owners" | grep -c . || true)"
[ "$order_count" -eq 1 ] \
  || { echo "$order_owners"; fail "the section order must be stated by exactly one active owner (found $order_count)"; }
ok "section order is stated once ($(printf '%s\n' "$order_owners" | head -1))"

section_rank() {
  case "$1" in
    Summary) echo 1 ;;
    Experience) echo 2 ;;
    *Projects*) echo 3 ;;
    Education) echo 4 ;;
    *Technical\ Skills*) echo 5 ;;
    Certifications) echo 6 ;;
    *) echo 0 ;;
  esac
}
for mode in "${MODES[@]}"; do
  base="$ROOT/versions/$mode/_base.md"
  prev=0
  while IFS= read -r heading; do
    [ -n "$heading" ] || continue
    rank="$(section_rank "$heading")"
    [ "$rank" -ne 0 ] || fail "$mode base has a non-canonical section: $heading"
    [ "$rank" -gt "$prev" ] || fail "$mode base sections are out of canonical order at: $heading"
    prev="$rank"
  done < <(grep -E '^## ' "$base" | sed -E 's/^## +//')
done
ok "base resume sections follow the canonical order"

# --- example run: output contract, traceability, reproducibility (REQ-P1/P4/O5/T1/C1) ---
# The example run demonstrates the whole path; older runs predate the contract.
EXAMPLE="applications/SWE_MNC_2026-10"
bash "$ROOT/pipeline/check_run.sh" "$ROOT/$EXAMPLE" || fail "example run violates the run contract"
ok "example run meets the run contract"

# --- retirement: old pipeline surfaces and drifting twins must be gone ---
test -e "$ROOT/PIPELINE.md" && fail "root PIPELINE.md should be retired"
test -e "$ROOT/prompts" && fail "prompts/ should be retired"
for mode in "${MODES[@]}"; do
  test -e "$ROOT/versions/$mode/resume_SWE.md" && fail "$mode resume_SWE.md twin should be retired"
done
ok "old pipeline surface and resume_SWE twins are retired"

# --- mode configs hold settings only (no restated identity) ---
assert_absent "mode configs do not restate display name or headline" \
  '^display_name:|^headline:' \
  modes/referral.yaml modes/startup.yaml modes/mnc.yaml

# --- run inputs use the mode vocabulary, not the retired 'track' ---
assert_absent "application inputs use mode: not track:" \
  '^track:' \
  applications/_template/input.md applications/SWE_MNC_2026-10/input.md \
  applications/SWE_Referral_2026-10/input.md applications/SWE_Startup_2026-10/input.md

# --- no competing pipeline / obsolete modules in the active tree ---
OBSOLETE=(engine MAP.md CONTEXT.md wayfinder docs/agent.md docs/gemini.md docs/END_TO_END_WORKFLOW.md)
for o in "${OBSOLETE[@]}"; do
  test -e "$ROOT/$o" && fail "obsolete module present in active tree: $o"
done
ok "no competing/obsolete modules in the active tree"

# --- active docs: no removed-module references, workstation paths, or stale vocabulary ---
ACTIVE_FILES=(
  AGENTS.md SPEC.md README.md RESUME_RULES.md DONT.MD
  docs/voice.md
  modes/referral.yaml modes/startup.yaml modes/mnc.yaml
  templates/v3/resume.tex
  versions/referral/_base.md versions/referral/resume.tex
  versions/startup/_base.md versions/startup/resume.tex
  versions/mnc/_base.md versions/mnc/resume.tex
)
assert_absent "active files do not reference removed modules" \
  'engine/PROMPT|engine/RULES|pipeline/run\.md|pipeline/APPLY|pipeline/stages|CONTEXT\.md|MAP\.md|wayfinder|\bPIPELINE\.md|prompts/' \
  "${ACTIVE_FILES[@]}"
assert_absent "active files are portable" \
  '[A-Za-z]:\\|/mnt/data|/home/|~/|\\\\[A-Za-z]' \
  "${ACTIVE_FILES[@]}"
assert_absent "active files contain no prior-application reference" \
  'applications/[A-Za-z0-9]+_20[0-9][0-9]-' \
  "${ACTIVE_FILES[@]}"
assert_absent "active system uses current mode vocabulary" \
  'versions/local|versions/midlevel|mid-level' \
  "${ACTIVE_FILES[@]}"

# --- base resumes must not use the deprecated low-signal framing ---
assert_absent "active base resumes contain no deprecated CAD/enclosure framing" \
  '3D-printed|custom CAD enclosure|custom CAD' \
  versions/referral/_base.md versions/startup/_base.md versions/mnc/_base.md

# --- template integrity ---
assert_absent "canonical template has no horizontal section rules" \
  '\\hrule|\\titlerule' \
  templates/v3/resume-openfont.cls

assert_absent "canonical template contains no dummy content" \
  'Jane Doe|Anycompany|dummy-certification|Project 1|lorem ipsum' \
  templates/v3

# --- no tracked build junk in active surfaces ---
if git -C "$ROOT" ls-files templates/v3 versions/referral versions/startup versions/mnc pipeline modes | \
   grep -E '\.(aux|log|out|synctex\.gz|fls|fdb_latexmk)$' >/tmp/resume-build-check 2>/dev/null; then
  cat /tmp/resume-build-check
  fail "tracked LaTeX build artifacts found in active surfaces"
fi
ok "no tracked LaTeX build artifacts in active surfaces"

ok "repository resume contract passed"
