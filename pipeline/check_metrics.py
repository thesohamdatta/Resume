#!/usr/bin/env python3
"""Reject resume percentages/multipliers not justified by a candidate metric record.

Each supported metric lives in the relevant record in data/facts.yaml with a
value, status, basis, and use limit. Unrelated percentages cannot authorize claims.
Estimates require both a defensible basis and explicit qualified-use wording.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:  # pragma: no cover - actionable error for incomplete installs
    yaml = None

METRIC_TOKEN = re.compile(r"[0-9]+(?:\.[0-9]+)?[ \t]*\\?%|[0-9]+(?:\.[0-9]+)?x", re.IGNORECASE)
METRIC_KEYS = {"metric", "metrics", "measured_metrics", "quantified_outcomes"}
BLOCKED_KEYS = {
    "hold", "held", "unverified", "excluded", "attribution_limits",
    "constraints", "prohibited", "negative_claims", "future_work",
    "do_not_claim", "unsupported_claims",
}
ESTIMATE_STATUSES = {"candidate_estimate", "candidate_confirmed_estimate", "estimated"}
QUALIFIED_USE = re.compile(r"\b(approx(?:imate(?:ly)?)?|estimate(?:d)?|qualified|only if qualified|as an estimate)\b", re.IGNORECASE)


def fold_token(token: str) -> str:
    """Normalize TeX escaping and whitespace, e.g. '99\\%' -> '99%'."""
    return re.sub(r"[ \t\\]", "", token).lower()


def _has_hold_instruction(record: dict[str, Any]) -> bool:
    for key, value in record.items():
        normalized = str(key).strip().lower().replace("-", "_")
        if normalized in {"resume_use", "claim_status", "metric_status", "verification_status", "status", "confidence"} and isinstance(value, str):
            text = value.strip().lower().replace("-", "_")
            if text.startswith(("hold", "do not use", "unverified", "exclude", "prohibited", "unknown", "unsupported", "low confidence")):
                return True
    return False


def _record_value_tokens(record: dict[str, Any]) -> set[str]:
    """Read only the metric value, never a number mentioned in its evidence or note."""
    if _has_hold_instruction(record):
        return set()
    value = record.get("value")
    if not isinstance(value, (str, int, float)) or isinstance(value, bool):
        return set()

    status = str(
        record.get("status")
        or record.get("verification_status")
        or record.get("metric_status")
        or record.get("claim_status")
        or ""
    ).strip().lower().replace("-", "_")
    basis = record.get("basis") or record.get("measurement_basis") or record.get("evidence_source")
    if not isinstance(basis, str) or not basis.strip():
        return set()

    if status in {"verified", "candidate_confirmed"}:
        pass
    elif status in ESTIMATE_STATUSES:
        use = record.get("resume_use")
        if not isinstance(use, str) or not QUALIFIED_USE.search(use):
            return set()
    else:
        # Missing, unknown, and unverified statuses are not an allow decision.
        return set()

    if isinstance(value, str):
        return {fold_token(token) for token in METRIC_TOKEN.findall(value)}
    return {fold_token(token) for token in METRIC_TOKEN.findall(str(value))}


def _tokens_in_metric_container(value: Any) -> set[str]:
    """Walk a metric collection and authorize only individually valid metric records."""
    if isinstance(value, dict):
        if "value" in value:
            return _record_value_tokens(value)
        tokens: set[str] = set()
        for key, child in value.items():
            normalized = str(key).strip().lower().replace("-", "_")
            if normalized in BLOCKED_KEYS:
                continue
            tokens.update(_tokens_in_metric_container(child))
        return tokens
    if isinstance(value, (list, tuple)):
        tokens: set[str] = set()
        for child in value:
            tokens.update(_tokens_in_metric_container(child))
        return tokens
    # Bare strings directly under metrics aren't sufficiently described to authorize a claim.
    return set()


def _candidate_metric_tokens(value: Any) -> set[str]:
    """Find metric collections in candidate facts while ignoring unrelated prose."""
    tokens: set[str] = set()
    if isinstance(value, dict):
        for key, child in value.items():
            normalized = str(key).strip().lower().replace("-", "_")
            if normalized in BLOCKED_KEYS:
                continue
            if normalized in METRIC_KEYS:
                tokens.update(_tokens_in_metric_container(child))
            else:
                tokens.update(_candidate_metric_tokens(child))
    elif isinstance(value, (list, tuple)):
        for child in value:
            tokens.update(_candidate_metric_tokens(child))
    return tokens


def _all_metric_tokens(value: Any) -> set[str]:
    """Extract tokens from a restriction so the corresponding value remains blocked."""
    tokens: set[str] = set()
    if isinstance(value, dict):
        for child in value.values():
            tokens.update(_all_metric_tokens(child))
    elif isinstance(value, (list, tuple)):
        for child in value:
            tokens.update(_all_metric_tokens(child))
    elif isinstance(value, str):
        tokens.update(fold_token(token) for token in METRIC_TOKEN.findall(value))
    return tokens


def restricted_tokens(value: Any) -> set[str]:
    """Collect blocked tokens across candidate facts; any explicit restriction wins."""
    tokens: set[str] = set()
    if isinstance(value, dict):
        if _has_hold_instruction(value):
            return _all_metric_tokens(value)
        if "value" in value:
            # A permitted metric's measurement basis may mention thresholds or
            # unrelated numbers; only its explicit restrictions should block tokens.
            for key, child in value.items():
                normalized = str(key).strip().lower().replace("-", "_")
                if normalized in BLOCKED_KEYS:
                    tokens.update(_all_metric_tokens(child))
            return tokens
        for key, child in value.items():
            normalized = str(key).strip().lower().replace("-", "_")
            if normalized in BLOCKED_KEYS:
                tokens.update(_all_metric_tokens(child))
            else:
                tokens.update(restricted_tokens(child))
    elif isinstance(value, (list, tuple)):
        for child in value:
            tokens.update(restricted_tokens(child))
    return tokens


def allowed_metric_tokens(facts_path: Path) -> set[str]:
    """Return authorized percent/multiplier tokens; explicit restrictions always win."""
    if yaml is None:
        raise RuntimeError("PyYAML is required for metric validation; install job-search/requirements.txt.")
    try:
        facts = yaml.safe_load(facts_path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, yaml.YAMLError) as exc:
        raise ValueError(f"cannot parse candidate facts YAML: {exc}") from exc
    if not isinstance(facts, dict):
        raise ValueError("candidate facts YAML must be a mapping")
    return _candidate_metric_tokens(facts) - restricted_tokens(facts)


def main() -> int:
    if len(sys.argv) != 3:
        print("usage: check_metrics.py <facts.yaml> <resume.tex>", file=sys.stderr)
        return 2
    try:
        allowed = allowed_metric_tokens(Path(sys.argv[1]))
        resume = Path(sys.argv[2]).read_text(encoding="utf-8")
    except (OSError, UnicodeError, ValueError, RuntimeError) as exc:
        print(f"FAIL: cannot validate metrics: {exc}", file=sys.stderr)
        return 2

    claimed = {fold_token(token) for token in METRIC_TOKEN.findall(resume)}
    unverified = sorted(claimed - allowed)
    if unverified:
        print(f"FAIL: resume states unsupported metric(s): {', '.join(unverified)}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
