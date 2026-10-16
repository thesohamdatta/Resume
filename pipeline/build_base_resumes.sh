#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
BUILD_ROOT="${RESUME_BUILD_DIR:-${TMPDIR:-/tmp}/resume-base-build}"
mkdir -p "$BUILD_ROOT"
PY=""
if command -v python3 >/dev/null 2>&1 && python3 -c 'import sys' 2>/dev/null; then
  PY=python3
elif command -v python >/dev/null 2>&1 && python -c 'import sys' 2>/dev/null; then
  PY=python
fi
[ -n "$PY" ] || { echo "FAIL: no working Python interpreter found" >&2; exit 1; }

for mode in referral startup mnc; do
  dir="$ROOT/versions/$mode"
  echo "Building $mode"
  "$PY" "$ROOT/pipeline/render_mode.py" "$mode" --write
  (
    cd "$dir"
    build_dir="$BUILD_ROOT/$mode"
    mkdir -p "$build_dir"
    for _ in 1 2; do   # two passes: LaTeX needs both for a stable page count
      xelatex -output-directory="$build_dir" -interaction=nonstopmode -halt-on-error resume.tex >"$BUILD_ROOT/$mode.log" 2>&1
    done
    pages="$(pdfinfo "$build_dir/resume.pdf" | awk '/^Pages:/ {print $2}')"
    if [ "$pages" != "1" ]; then
      echo "FAIL: $mode compiled to $pages pages, expected exactly 1" >&2
      exit 1
    fi
  )
done

echo "All three base resumes compiled as one-page PDFs in $BUILD_ROOT."
