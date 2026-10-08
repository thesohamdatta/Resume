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

echo
if [ "$FAILURES" -eq 0 ]; then
  echo "All contract tests passed."
  exit 0
fi
echo "$FAILURES contract test(s) failed." >&2
exit 1
