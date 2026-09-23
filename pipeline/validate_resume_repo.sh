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

ACTIVE_DOCS=(
  "$ROOT/AGENTS.md"
  "$ROOT/CONTEXT.md"
  "$ROOT/MAP.md"
  "$ROOT/README.md"
  "$ROOT/pipeline"
  "$ROOT/docs/voice.md"
  "$ROOT/docs/agent.md"
  "$ROOT/.agents/skills/voice-guide"
  "$ROOT/.agents/skills/latex-resume-render"
  "$ROOT/versions/referral"
  "$ROOT/versions/startup"
  "$ROOT/versions/mnc"
  "$ROOT/templates/v3"
)

if grep -RInE 'D:\\download|/mnt/data|C:\\Users' "${ACTIVE_DOCS[@]}" >/tmp/resume-path-check 2>/dev/null; then
  cat /tmp/resume-path-check
  fail "active docs contain workstation paths"
fi
ok "no workstation paths in active system"

if grep -RInE 'versions/local|mid-level|midlevel|only two active tracks|exactly two active tracks|\[local \| mnc\]' "${ACTIVE_DOCS[@]}" >/tmp/resume-track-check 2>/dev/null; then
  cat /tmp/resume-track-check
  fail "active system contains stale track contract"
fi
ok "active system uses current track vocabulary"

if grep -RInE '3D-printed|custom CAD enclosure|custom CAD' "$ROOT/versions/referral" "$ROOT/versions/startup" "$ROOT/versions/mnc" >/tmp/resume-positioning-check 2>/dev/null; then
  cat /tmp/resume-positioning-check
  fail "active base resume contains deprecated low-signal hardware framing"
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
  fail "tracked LaTeX build artifacts found"
fi
ok "no tracked LaTeX build artifacts"

ok "repository resume contract passed"
