#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"

for mode in referral startup mnc; do
  dir="$ROOT/versions/$mode"
  echo "Building $mode"
  (
    cd "$dir"
    for _ in 1 2; do   # two passes: LaTeX needs both for a stable page count
      xelatex -interaction=nonstopmode -halt-on-error resume.tex >/tmp/resume_$mode.log 2>&1
    done
    pages="$(pdfinfo resume.pdf | awk '/^Pages:/ {print $2}')"
    test "$pages" = "1"
    rm -f resume.aux resume.log resume.out
  )
done

echo "All three base resumes compiled as one-page PDFs."
