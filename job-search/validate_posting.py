#!/usr/bin/env python3
"""Validate canonical job-posting JSON against the shared posting contract."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parent
SCHEMA_PATH = ROOT / "schemas" / "job-posting.schema.json"
sys.path.insert(0, str(ROOT))
import workflow  # noqa: E402


def load_schema() -> dict:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    return schema


def validate_posting_object(posting: dict) -> list[str]:
    """Expose the shared schema and cross-field checks for library callers."""
    return workflow.validate_posting_object(posting)


def validate_file(path: Path) -> list[str]:
    try:
        instance = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"{path}: cannot read valid JSON: {exc}"]

    return [
        f"{path}: {error}"
        for error in validate_posting_object(instance)
    ]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", nargs="+", type=Path, help="posting JSON file(s) to validate")
    args = parser.parse_args(argv)

    try:
        load_schema()
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"FAIL: invalid schema: {exc}", file=sys.stderr)
        return 2

    all_errors: list[str] = []
    for path in args.files:
        errors = validate_file(path)
        if errors:
            all_errors.extend(errors)
        else:
            print(f"PASS: {path} conforms to the canonical job-posting contract")

    if all_errors:
        print("\n".join(all_errors), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
