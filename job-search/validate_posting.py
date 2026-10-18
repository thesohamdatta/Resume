#!/usr/bin/env python3
"""Validate canonical job-posting JSON against the versioned schema."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schemas" / "job-posting.schema.json"


def load_schema() -> dict:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    return schema


def validate_file(path: Path, validator: Draft202012Validator) -> list[str]:
    try:
        instance = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"{path}: cannot read valid JSON: {exc}"]

    errors = sorted(validator.iter_errors(instance), key=lambda err: list(map(str, err.absolute_path)))
    return [
        f"{path}: {'/'.join(map(str, error.absolute_path)) or '<root>'}: {error.message}"
        for error in errors
    ]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", nargs="+", type=Path, help="posting JSON file(s) to validate")
    args = parser.parse_args(argv)

    try:
        validator = Draft202012Validator(load_schema(), format_checker=FormatChecker())
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"FAIL: invalid schema: {exc}", file=sys.stderr)
        return 2

    all_errors: list[str] = []
    for path in args.files:
        errors = validate_file(path, validator)
        if errors:
            all_errors.extend(errors)
        else:
            print(f"PASS: {path} conforms to the canonical job-posting schema")

    if all_errors:
        print("\n".join(all_errors), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
