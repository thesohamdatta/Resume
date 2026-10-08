#!/usr/bin/env python3
"""Check that every metric in a run's resume is a verified fact.

Seam: the exit code. The resume is scanned for numeric metric tokens; each must
appear in `metrics.verified` of data/facts.yaml. `metrics.hold` is explicitly NOT
verified, so a held number (e.g. the Reliance improvement) fails.

Honest limitation: this catches numeric tokens in percent and multiple form
(`40%`, `3x`). It does NOT catch a metric stated in prose ("doubled throughput")
or a bare number ("served 1,000 users"). Preventing those is the judgment rule in
RESUME_RULES.md, enforced by human review at delivery, not by this check.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

METRIC_TOKEN = re.compile(r"[0-9]+(?:\.[0-9]+)?[ \t]*\\?%|[0-9]+(?:\.[0-9]+)?x")
NUMBER = re.compile(r"[0-9]+(?:\.[0-9]+)?")


def verified_numbers(facts_path: Path) -> set[str]:
    """Numbers under metrics.verified only; metrics.hold is not verified."""
    numbers: set[str] = set()
    in_metrics = in_verified = False
    for line in facts_path.read_text(encoding="utf-8").splitlines():
        if re.match(r"^metrics:", line):
            in_metrics = True
            continue
        if not in_metrics:
            continue
        if re.match(r"^[A-Za-z]", line):
            break
        if re.match(r"^  verified:", line):
            in_verified = True
            continue
        if re.match(r"^  [A-Za-z_]+:", line):
            in_verified = False
            continue
        if in_verified:
            numbers.update(NUMBER.findall(line.replace(",", "")))
    return numbers


def main() -> int:
    if len(sys.argv) != 3:
        print("usage: check_metrics.py <facts.yaml> <resume.tex>", file=sys.stderr)
        return 2
    verified = verified_numbers(Path(sys.argv[1]))
    text = Path(sys.argv[2]).read_text(encoding="utf-8")
    unverified = sorted({NUMBER.search(t).group() for t in METRIC_TOKEN.findall(text)} - verified)
    if unverified:
        print(f"FAIL: resume states unverified metric(s): {', '.join(unverified)}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
