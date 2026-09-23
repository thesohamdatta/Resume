#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
fail() { echo "FAIL: $*" >&2; exit 1; }
ok() { echo "PASS: $*"; }

for track in referral startup mnc; do
  test -f "$ROOT/versions/$track/_base.md" || fail "missing $track base"
  test -f "$ROOT/versions/$track/resume.tex" || fail "missing $track resume.tex"
  grep -qF '\documentclass{../../templates/v3/resume-openfont}' "$ROOT/versions/$track/resume.tex"     || fail "$track does not use canonical template"
done
ok "all three active tracks exist and use templates/v3"

ACTIVE_FILES=(
  AGENTS.md
  CONTEXT.md
  MAP.md
  README.md
  DONT.MD
  docs/voice.md
  docs/agent.md
  pipeline/APPLY.md
  pipeline/run.md
  pipeline/stages/10_slop_free_polish.md
  .agents/skills/voice-guide/SKILL.md
  .agents/skills/latex-resume-render/SKILL.md
  templates/v3/resume.tex
  templates/v3/resume-openfont.cls
  versions/referral/_base.md
  versions/referral/resume.tex
  versions/startup/_base.md
  versions/startup/resume.tex
  versions/mnc/_base.md
  versions/mnc/resume.tex
)

if grep -nE 'D:\\\\download|[A-Za-z]:\\\\Users\\\\|/mnt/data' -- "${ACTIVE_FILES[@]}" >/tmp/resume-path-check 2>/dev/null; then
  cat /tmp/resume-path-check
  fail "active system contains workstation paths"
fi
ok "active system is portable"

if grep -nE 'versions/local|versions/midlevel|mid-level' -- "${ACTIVE_FILES[@]}" >/tmp/resume-track-check 2>/dev/null; then
  cat /tmp/resume-track-check
  fail "active system contains stale track terminology"
fi
ok "active system uses current track vocabulary"

if grep -nE '3D-printed|custom CAD enclosure|custom CAD' versions/referral/_base.md versions/startup/_base.md versions/mnc/_base.md >/tmp/resume-positioning-check 2>/dev/null; then
  cat /tmp/resume-positioning-check
  fail "active base resumes contain deprecated low-signal hardware framing"
fi
ok "active base resumes contain no deprecated CAD/enclosure framing"

if grep -nE '\\hrule|\\titlerule' "$ROOT/templates/v3/resume-openfont.cls" >/tmp/resume-rule-check 2>/dev/null; then
  cat /tmp/resume-rule-check
  fail "canonical template contains horizontal section rules"
fi
ok "canonical template has no horizontal section rules"

if grep -RInE 'Jane Doe|Anycompany|dummy-certification|Project 1|lorem ipsum' "$ROOT/templates/v3" >/tmp/resume-dummy-check 2>/dev/null; then
  cat /tmp/resume-dummy-check
  fail "canonical template contains dummy content"
fi
ok "canonical template contains no dummy content"

if git -C "$ROOT" ls-files | grep -E '\.(aux|log|out|synctex\.gz|fls|fdb_latexmk)$' >/tmp/resume-build-check 2>/dev/null; then
  cat /tmp/resume-build-check
  fail "tracked LaTeX build artifacts found in active surfaces"
fi
ok "no tracked LaTeX build artifacts in active surfaces"

ok "repository resume contract passed"
