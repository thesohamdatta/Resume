#!/usr/bin/env python3
"""Check the traceability table in a run's audit.md.

Seam: the exit code. Every selected item must name the JD requirement it answers,
the source it comes from, its strength, and its action. The sources are exactly the
four owners in SPEC.md section 3; anything else is not a source.

An item with no source, or strength NONE, must be OMIT -- dropped, not softened.
"""
from __future__ import annotations

import re
import sys

SOURCES = {
    "data/facts.yaml",
    "content/github/evidence.md",
    "content/github/boundaries.md",
}
MODE_SOURCE = re.compile(r"^versions/[a-z]+/_base\.md$")
STRENGTHS = {"DIRECT", "ADJACENT", "NONE"}
ACTIONS = {"FOREGROUND", "SUPPORT", "OMIT"}
EXPECTED_COLUMNS = ["Item", "JD requirement", "Source", "Strength", "Action"]


def is_source(value: str) -> bool:
    return value in SOURCES or bool(MODE_SOURCE.match(value))


def parse_rows(text: str) -> tuple[list[str], list[list[str]]]:
    """Return (header_cells, data_rows) for the first 'Evidence trace' table."""
    lines = text.splitlines()
    start = None
    for i, line in enumerate(lines):
        if re.match(r"^\s*#{1,6}\s*Evidence trace\s*$", line, re.IGNORECASE):
            start = i + 1
            break
    if start is None:
        raise ValueError("no 'Evidence trace' section found")

    table: list[list[str]] = []
    for line in lines[start:]:
        stripped = line.strip()
        if stripped.startswith("|"):
            cells = [c.strip() for c in stripped.strip("|").split("|")]
            table.append(cells)
        elif table:
            break
    if not table:
        raise ValueError("'Evidence trace' section has no table")

    header = table[0]
    # Drop the markdown separator row (all dashes/colons).
    body = [r for r in table[1:] if not all(re.fullmatch(r":?-{2,}:?", c) for c in r)]
    return header, body


def check(path: str) -> list[str]:
    errors: list[str] = []
    try:
        text = open(path, encoding="utf-8").read()
    except OSError as exc:
        return [f"cannot read {path}: {exc}"]

    try:
        header, rows = parse_rows(text)
    except ValueError as exc:
        return [f"{path}: {exc}"]

    if header != EXPECTED_COLUMNS:
        errors.append(
            f"{path}: trace header must be {' | '.join(EXPECTED_COLUMNS)}"
            f" (got {' | '.join(header)})"
        )
    if not rows:
        errors.append(f"{path}: trace table has no data rows")

    for n, cells in enumerate(rows, start=1):
        if len(cells) != len(EXPECTED_COLUMNS):
            errors.append(f"{path}: row {n} has {len(cells)} columns, expected 5")
            continue
        item, _req, source, strength, action = cells
        where = f"{path}: row {n} ({item or 'unnamed'})"

        if strength not in STRENGTHS:
            errors.append(f"{where}: strength '{strength}' not in {sorted(STRENGTHS)}")
        if action not in ACTIONS:
            errors.append(f"{where}: action '{action}' not in {sorted(ACTIONS)}")

        grounded = is_source(source)
        if source and not grounded:
            errors.append(f"{where}: source '{source}' is not one of the four owners")

        # A shipped item (foreground/support) must trace to a real source and be real.
        if action in {"FOREGROUND", "SUPPORT"}:
            if not source:
                errors.append(f"{where}: {action} item has no source (untraceable)")
            if strength == "NONE":
                errors.append(f"{where}: {action} item has strength NONE (a gap must be OMIT)")

    return errors


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print("usage: check_audit.py <audit.md> [...]", file=sys.stderr)
        return 2
    all_errors: list[str] = []
    for path in argv[1:]:
        errors = check(path)
        if errors:
            all_errors.extend(errors)
        else:
            print(f"PASS: {path} is traceable")
    if all_errors:
        for err in all_errors:
            print(err, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
