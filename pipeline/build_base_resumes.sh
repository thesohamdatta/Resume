#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"

for track in referral startup mnc; do
  dir="$ROOT/versions/$track"
  echo "Building $track"
  (
    cd "$dir"
    xelatex -interaction=nonstopmode -halt-on-error resume.tex >/tmp/resume_$track.log 2>&1
    xelatex -interaction=nonstopmode -halt-on-error resume.tex >/tmp/resume_$track-2.log 2>&1
    pages="$(pdfinfo resume.pdf | awk '/^Pages:/ {print $2}')"
    test "$pages" = "1"
    rm -f resume.aux resume.log resume.out
  )
done

echo "All three base resumes compiled as one-page PDFs."
