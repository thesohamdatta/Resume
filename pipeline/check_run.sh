#!/usr/bin/env bash
# Check one application run against the run contract.
#
# A run is one input.md plus the standard output set. The mode comes from
# input.md, never from a per-JD step. Adding a company must add no file beyond
# input.md -- no step, prompt, or stage.
#
# usage: check_run.sh applications/<Name>_<YYYY-MM>
set -uo pipefail

run="${1:-}"
[ -n "$run" ] || { echo "usage: check_run.sh <run_dir>" >&2; exit 2; }
[ -d "$run" ] || { echo "FAIL: $run: not a directory" >&2; exit 1; }
fail() { echo "FAIL: $run: $*" >&2; exit 1; }

input="$run/input.md"
[ -f "$input" ] || fail "missing input.md (the only file a run requires) (REQ-P1)"

# The mode must be exactly one of the canonical three (REQ-P1, REQ-P2).
mode="$(grep -E '^[[:space:]]*mode:' "$input" | head -1 \
  | sed -E 's/^[[:space:]]*mode:[[:space:]]*//; s/[[:space:]]+$//')"
case "$mode" in
  referral|startup|mnc) ;;
  "") fail "input.md declares no mode (REQ-P1)" ;;
  *) fail "input.md declares unknown mode '$mode' (REQ-P2)" ;;
esac

# The output set is fixed (REQ-O5).
for f in resume.tex extracted.txt audit.md; do
  [ -f "$run/output/$f" ] || fail "output/ is missing $f (REQ-O5)"
done

# The delivered resume must use the canonical template (REQ-C1).
grep -qF 'templates/v3/resume-openfont' "$run/output/resume.tex" \
  || fail "output/resume.tex does not use the canonical template (REQ-C1)"

# The trace must be checkable (REQ-T1).
python3 "$(dirname "$0")/check_audit.py" "$run/output/audit.md" >/dev/null \
  || fail "output/audit.md is not traceable (REQ-T1)"

# A run adds no per-JD step or prompt: the run root holds input.md and output/ only (REQ-P4).
while IFS= read -r entry; do
  name="$(basename "$entry")"
  [ "$name" = "input.md" ] && continue
  [ "$name" = "output" ] && continue
  fail "unexpected per-JD file in run root: $name (REQ-P4: no step per JD)"
done < <(find "$run" -maxdepth 1 -mindepth 1)

echo "PASS: $run meets the run contract"
