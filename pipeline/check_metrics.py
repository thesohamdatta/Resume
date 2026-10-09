#!/usr/bin/env python3
"""Check that every metric claim in a run's resume is a verified fact.

Seam: the exit code. The resume is scanned for metric tokens (percent and
multiple form); a claim passes only if that WHOLE token is verified. A verified
digit reused out of context (a test count rendered as "52%") is not a verified
metric and fails. `metrics.hold` is explicitly NOT verified.

This catches metric tokens, not a metric stated in prose or as a bare number; that
limitation is owned by RESUME_RULES.md, section "The job description is data, not
instructions".
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

# A metric token: a number in percent form ("99%", "99\%") or multiple form ("3x").
METRIC_TOKEN = re.compile(r"[0-9]+(?:\.[0-9]+)?[ \t]*\\?%|[0-9]+(?:\.[0-9]+)?x")


def fold_token(token: str) -> str:
    """Fold "99\\%" and " 99 %" to one comparable form, "99%"."""
    return re.sub(r"[ \t\\]", "", token)


def verified_tokens(facts_path: Path) -> set[str]:
    """The metric tokens under metrics.verified only; metrics.hold is not verified."""
    tokens: set[str] = set()
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
            tokens.update(fold_token(t) for t in METRIC_TOKEN.findall(line))
    return tokens


def main() -> int:
    if len(sys.argv) != 3:
        print("usage: check_metrics.py <facts.yaml> <resume.tex>", file=sys.stderr)
        return 2
    verified = verified_tokens(Path(sys.argv[1]))
    text = Path(sys.argv[2]).read_text(encoding="utf-8")
    unverified = sorted({fold_token(t) for t in METRIC_TOKEN.findall(text)} - verified)
    if unverified:
        print(f"FAIL: resume states unverified metric(s): {', '.join(unverified)}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
