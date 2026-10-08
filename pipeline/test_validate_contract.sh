#!/usr/bin/env bash
# Contract tests for pipeline/validate_resume_repo.sh.
#
# Seam: the validator's exit code (and its stderr), observed by running it against a
# mutated copy of the repository. Expected outcomes come from SPEC.md REQ-C2 (one owner
# per rule) and the ticket acceptance criteria, not from the validator's implementation.
#
# Each case asserts the validator FAILS on a broken repository and the clean repository
# PASSES. A case whose "broken" copy already passed would be a test that grades nothing.
set -uo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
WORK="$(mktemp -d)"
trap 'rm -rf "$WORK"' EXIT

# One pristine copy, reused per case. Exclude .git, history, and fonts (not needed to validate).
BASE="$WORK/base"
mkdir -p "$BASE"
tar -C "$ROOT" \
  --exclude=.git --exclude=archive --exclude='*.ttf' --exclude='*.otf' \
  -cf - . | tar -C "$BASE" -xf -

FAILURES=0
pass() { echo "PASS: $*"; }
fail() { echo "FAIL: $*" >&2; FAILURES=$((FAILURES + 1)); }

run_validator() { # <dir> -> prints "exit=<n>"
  local dir="$1"
  ( cd "$dir" && bash pipeline/validate_resume_repo.sh ) >/dev/null 2>&1
  echo "exit=$?"
}

expect_pass() { # <desc> <dir>
  local desc="$1" dir="$2" r
  r="$(run_validator "$dir")"
  if [ "$r" = "exit=0" ]; then pass "$desc"; else fail "$desc (expected exit=0, got $r)"; fi
}

expect_fail() { # <desc> <dir>
  local desc="$1" dir="$2" r
  r="$(run_validator "$dir")"
  if [ "$r" != "exit=0" ]; then pass "$desc"; else fail "$desc (expected non-zero exit, got $r)"; fi
}

# --- case: clean repository passes ---
CLEAN="$WORK/clean"; cp -a "$BASE" "$CLEAN"
expect_pass "clean repository validates" "$CLEAN"

# --- case: a duplicated requirement id is rejected (REQ-C2) ---
DUP="$WORK/dup-req"; cp -a "$BASE" "$DUP"
printf '\n- **REQ-T1** — Duplicated on purpose by the contract test.\n' >> "$DUP/SPEC.md"
expect_fail "duplicate requirement id in SPEC.md is rejected" "$DUP"

# --- case: AGENTS.md dropping its SPEC.md reference is rejected ---
NREF="$WORK/no-ref"; cp -a "$BASE" "$NREF"
grep -v 'SPEC.md' "$NREF/AGENTS.md" > "$NREF/AGENTS.md.tmp" && mv "$NREF/AGENTS.md.tmp" "$NREF/AGENTS.md"
expect_fail "AGENTS.md without a SPEC.md reference is rejected" "$NREF"

# --- case: a prior-application reference in SPEC.md is rejected ---
APP="$WORK/prior-app"; cp -a "$BASE" "$APP"
printf '\nTailored for the Amazon Site Admin Assistant role.\n' >> "$APP/SPEC.md"
expect_fail "prior-application reference in SPEC.md is rejected" "$APP"

# --- case: a removed SPEC.md is rejected ---
GONE="$WORK/no-spec"; cp -a "$BASE" "$GONE"
rm -f "$GONE/SPEC.md"
expect_fail "missing SPEC.md is rejected" "$GONE"

# --- case: a fourth mode is rejected (REQ-P2) ---
# The three modes are exactly referral, startup, mnc. There is no fourth.
FOURTH="$WORK/fourth-mode"; cp -a "$BASE" "$FOURTH"
printf 'name_key: quad\n' > "$FOURTH/modes/quad.yaml"
expect_fail "a fourth mode config is rejected" "$FOURTH"

# --- case: a retired mode directory is rejected (REQ-P2) ---
RETIRED="$WORK/retired-mode"; cp -a "$BASE" "$RETIRED"
mkdir -p "$RETIRED/versions/local"
printf '## Summary\n' > "$RETIRED/versions/local/_base.md"
expect_fail "a retired mode directory is rejected" "$RETIRED"

# --- case: a non-canonical section order is rejected (REQ-O2) ---
# Canonical order: Header/Contact, Summary, Experience, Projects, Education,
# Technical Skills, Certifications. A section after a later one is out of order.
BADORDER="$WORK/bad-order"; cp -a "$BASE" "$BADORDER"
printf '\n## Summary\n' >> "$BADORDER/versions/referral/_base.md"
expect_fail "a non-canonical section order is rejected" "$BADORDER"

# --- case: an absolute workstation path in an active file is rejected (REQ-C4) ---
WPATH="$WORK/workstation"; cp -a "$BASE" "$WPATH"
printf '\nBuild artifacts live at /mnt/data/notes.\n' >> "$WPATH/README.md"
expect_fail "an absolute workstation path in an active file is rejected" "$WPATH"

# --- case: the example run's audit is traceable (REQ-T1) ---
# The example audit.md carries an "## Evidence trace" table; every selected item
# names its JD requirement, its source, its strength, and its action.
EXAMPLE_AUDIT="applications/SWE_MNC_2026-10/output/audit.md"
expect_pass "the example run's audit is traceable" "$WORK/clean"

# --- case: removing one source reference breaks traceability (REQ-T1) ---
NOSRC="$WORK/no-source"; cp -a "$BASE" "$NOSRC"
python3 - "$NOSRC/$EXAMPLE_AUDIT" <<'PY'
import sys, re
p = sys.argv[1]
t = open(p).read()
t = t.replace("| content/github/evidence.md |", "|  |", 1)
open(p, "w").write(t)
PY
expect_fail "an audit whose selected item lost its source is rejected" "$NOSRC"

# --- case: an unknown source owner breaks traceability (REQ-T1) ---
BADSRC="$WORK/bad-source"; cp -a "$BASE" "$BADSRC"
python3 - "$BADSRC/$EXAMPLE_AUDIT" <<'PY'
import sys
p = sys.argv[1]
t = open(p).read()
t = t.replace("| content/github/evidence.md |", "| research/README.md |")
open(p, "w").write(t)
PY
expect_fail "an audit citing a non-owner source is rejected" "$BADSRC"

# --- case: an untraceable item shipped instead of dropped breaks traceability (REQ-T1) ---
SHIPPED="$WORK/shipped-gap"; cp -a "$BASE" "$SHIPPED"
python3 - "$SHIPPED/$EXAMPLE_AUDIT" <<'PY'
import sys
p = sys.argv[1]
t = open(p).read()
t = t.replace("| NONE | OMIT |", "| ADJACENT | FOREGROUND |")
open(p, "w").write(t)
PY
expect_fail "an audit foregrounding a sourceless item is rejected" "$SHIPPED"

# --- case: an audit with no trace table is rejected (REQ-O5) ---
NOTABLE="$WORK/no-table"; cp -a "$BASE" "$NOTABLE"
printf '# Audit\n\nNo trace here.\n' > "$NOTABLE/$EXAMPLE_AUDIT"
expect_fail "an audit with no evidence trace table is rejected" "$NOTABLE"

echo
if [ "$FAILURES" -eq 0 ]; then
  echo "All contract tests passed."
  exit 0
fi
echo "$FAILURES contract test(s) failed." >&2
exit 1
