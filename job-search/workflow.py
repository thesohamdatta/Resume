#!/usr/bin/env python3
"""Deterministic, offline-first job-search workflow primitives."""
from __future__ import annotations

import copy
import json
import os
import tempfile
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parent
SCHEMA_PATH = ROOT / "schemas" / "job-posting.schema.json"
ELIGIBILITY_STATUSES = {"met", "unmet", "unknown"}

SKILL_ALIASES: dict[str, tuple[str, ...]] = {
    "Python": ("python",),
    "Java": ("java",),
    "TypeScript": ("typescript",),
    "JavaScript": ("javascript",),
    "Kotlin": ("kotlin",),
    "C/C++": ("c/c++", "c++", "c plus plus"),
    "FastAPI": ("fastapi",),
    "React": ("react", "react.js", "reactjs"),
    "Node.js": ("node.js", "nodejs"),
    "REST APIs": ("rest api", "rest apis"),
    "Git/GitHub": ("git", "github"),
    "Machine Learning": ("machine learning", "ml"),
    "Generative AI": ("generative ai", "genai"),
    "LLM applications": ("llm", "large language model"),
    "RAG": ("rag", "retrieval augmented generation"),
    "AI agents": ("ai agent", "agentic"),
    "Computer Vision": ("computer vision",),
    "TensorFlow": ("tensorflow",),
    "TensorFlow Lite": ("tensorflow lite", "tflite"),
    "PyTorch": ("pytorch",),
    "Google ML Kit": ("google ml kit", "ml kit"),
    "LiveKit": ("livekit",),
    "WebRTC": ("webrtc",),
    "Kubernetes": ("kubernetes",),
    "Docker": ("docker",),
    "AWS": ("aws", "amazon web services"),
    "SQL": ("sql",),
    "Automation": ("automation",),
    "FastAPI": ("fastapi",),
}


def load_schema() -> dict[str, Any]:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    return schema


def validate_posting_object(posting: dict[str, Any]) -> list[str]:
    validator = Draft202012Validator(load_schema(), format_checker=FormatChecker())
    errors = sorted(
        validator.iter_errors(posting),
        key=lambda error: list(map(str, error.absolute_path)),
    )
    return [
        f"{'/'.join(map(str, error.absolute_path)) or '<root>'}: {error.message}"
        for error in errors
    ]


def empty_state() -> dict[str, Any]:
    return {
        "schema_version": 1,
        "postings": {},
        "opportunities": {},
        "applications": {},
        "source_calls": {},
    }


def load_state(path: Path) -> dict[str, Any]:
    if not path.exists():
        return empty_state()
    try:
        state = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"Cannot read job-search state at {path}: {exc}") from exc
    if not isinstance(state, dict) or state.get("schema_version") != 1:
        raise ValueError(f"Unsupported or invalid job-search state file: {path}")
    for key in ("postings", "opportunities", "applications", "source_calls"):
        if not isinstance(state.get(key), dict):
            raise ValueError(f"Invalid job-search state: '{key}' must be an object")
    return state


def save_state(path: Path, state: dict[str, Any]) -> None:
    """Write state atomically so an interrupted write does not truncate history."""
    path.parent.mkdir(parents=True, exist_ok=True)
    serialized = json.dumps(state, indent=2, ensure_ascii=False, sort_keys=True) + "\n"
    fd, temp_name = tempfile.mkstemp(prefix=f".{path.name}.", suffix=".tmp", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            handle.write(serialized)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temp_name, path)
    except Exception:
        try:
            os.unlink(temp_name)
        except OSError:
            pass
        raise


def upsert_posting(state: dict[str, Any], posting: dict[str, Any]) -> str:
    """Insert or refresh one source listing while preserving prior versions and decisions."""
    errors = validate_posting_object(posting)
    if errors:
        raise ValueError("Invalid posting: " + "; ".join(errors))

    posting_id = posting["posting_id"]
    incoming = copy.deepcopy(posting)
    existing = state["postings"].get(posting_id)
    if existing is None:
        incoming["record"]["first_seen_at"] = posting["record"].get("first_seen_at") or posting["source"]["retrieved_at"]
        state["postings"][posting_id] = {"current": incoming, "history": []}
        return "inserted"

    previous = existing["current"]
    old_hash = previous["record"].get("content_hash")
    new_hash = incoming["record"].get("content_hash")
    old_status = previous["record"].get("status")
    new_status = incoming["record"].get("status")
    if old_hash != new_hash or old_status != new_status:
        existing["history"].append({
            "posting": copy.deepcopy(previous),
            "change": "content_changed" if old_hash != new_hash else "status_changed",
            "observed_at": incoming["source"]["retrieved_at"],
        })
    incoming["record"]["first_seen_at"] = previous["record"]["first_seen_at"]
    incoming["record"]["last_seen_at"] = max(
        str(previous["record"].get("last_seen_at", "")),
        str(incoming["record"].get("last_seen_at", "")),
    )
    existing["current"] = incoming
    return "updated" if old_hash != new_hash or old_status != new_status else "unchanged"


def evaluate_eligibility(checks: list[dict[str, Any]] | None) -> dict[str, Any]:
    """Evaluate only explicit, reviewed mandatory checks; never guess eligibility."""
    checks = checks or []
    for item in checks:
        if item.get("status") not in ELIGIBILITY_STATUSES:
            raise ValueError("Each eligibility check needs status met, unmet, or unknown")

    mandatory = [item for item in checks if item.get("mandatory") is True]
    if any(item["status"] == "unmet" for item in mandatory):
        status = "Ineligible"
    elif mandatory and all(item["status"] == "met" for item in mandatory):
        status = "Eligible"
    else:
        status = "Unknown"

    reasons = [
        f"{item.get('description', 'Mandatory requirement')}: {item['status']}"
        for item in mandatory
    ]
    if not mandatory:
        reasons.append("No reviewed mandatory requirements are available; eligibility remains unknown.")
    elif status == "Unknown":
        reasons.append("At least one mandatory requirement is not confirmed.")
    return {"status": status, "reasons": reasons, "checks": copy.deepcopy(checks)}


def _contains_term(text: str, term: str) -> bool:
    """Match a phrase as text, avoiding loose single-letter/sub-string matches."""
    normalized_text = " ".join(text.casefold().replace("/", " ").replace("-", " ").split())
    normalized_term = " ".join(term.casefold().replace("/", " ").replace("-", " ").split())
    if not normalized_term:
        return False
    if " " not in normalized_term and len(normalized_term) <= 3:
        import re
        return re.search(rf"(?<![a-z0-9]){re.escape(normalized_term)}(?![a-z0-9])", normalized_text) is not None
    return normalized_term in normalized_text


def evaluate_fit(posting: dict[str, Any], candidate_evidence: dict[str, str]) -> dict[str, Any]:
    skills = list(dict.fromkeys(posting.get("job", {}).get("skills", [])))
    if not skills:
        return {
            "score": None,
            "matched_skills": [],
            "missing_skills": [],
            "reasons": ["The listing has no structured skills to compare; no fit score was guessed."],
            "evidence_sources": [],
        }

    combined = "\n".join(candidate_evidence.values())
    matched: list[str] = []
    missing: list[str] = []
    reasons: list[str] = []
    evidence_sources: set[str] = set()
    for skill in skills:
        aliases = SKILL_ALIASES.get(skill, (skill,))
        matched_in_sources = [
            name for name, content in candidate_evidence.items()
            if any(_contains_term(content, alias) for alias in aliases)
        ]
        if matched_in_sources:
            matched.append(skill)
            evidence_sources.update(matched_in_sources)
            reasons.append(
                f"Direct text match for {skill} in " + ", ".join(sorted(matched_in_sources)) + "."
            )
        else:
            missing.append(skill)
    score = round(100 * len(matched) / len(skills))
    if missing:
        reasons.append(
            "No direct text match found in the loaded candidate-evidence sources for: "
            + ", ".join(missing)
            + ". This is missing evidence, not proof the candidate lacks the skill."
        )
    return {
        "score": score,
        "matched_skills": matched,
        "missing_skills": missing,
        "reasons": reasons,
        "evidence_sources": sorted(evidence_sources),
    }


def evaluate_posting(
    posting: dict[str, Any],
    candidate_evidence: dict[str, str] | None = None,
    eligibility_checks: list[dict[str, Any]] | None = None,
) -> dict[str, Any]:
    candidate_evidence = candidate_evidence or {}
    return {
        "posting_id": posting["posting_id"],
        "title": posting["job"]["title"],
        "company": posting["job"]["company"],
        "source_url": posting["source"]["url"],
        "retrieved_at": posting["source"]["retrieved_at"],
        "posting_status": posting["record"]["status"],
        "eligibility": evaluate_eligibility(eligibility_checks),
        "fit": evaluate_fit(posting, candidate_evidence),
    }


def summarize_source_result(result: dict[str, Any]) -> dict[str, Any]:
    status = result.get("status")
    count = len(result.get("postings") or [])
    return {
        "source": result.get("source", "unknown"),
        "status": status,
        "count": count,
        "zero_results": (status == "success" and count == 0) if status in {"success", "blocked", "failed"} else None,
        "error": result.get("error"),
    }


def process_source_results(
    source_results: list[dict[str, Any]],
    state: dict[str, Any],
    candidate_evidence: dict[str, str] | None = None,
    eligibility_checks_by_posting: dict[str, list[dict[str, Any]]] | None = None,
) -> dict[str, Any]:
    summaries: list[dict[str, Any]] = []
    evaluations: list[dict[str, Any]] = []
    changes = {"inserted": 0, "updated": 0, "unchanged": 0, "invalid": 0}
    candidate_evidence = candidate_evidence or {}
    eligibility_checks_by_posting = eligibility_checks_by_posting or {}

    for result in source_results:
        summary = summarize_source_result(result)
        errors: list[str] = []
        if result.get("status") == "success":
            for index, posting in enumerate(result.get("postings") or []):
                validation_errors = validate_posting_object(posting)
                if validation_errors:
                    changes["invalid"] += 1
                    errors.append(f"Posting {index + 1}: " + "; ".join(validation_errors))
                    continue
                change = upsert_posting(state, posting)
                changes[change] += 1
                evaluations.append(evaluate_posting(
                    posting,
                    candidate_evidence=candidate_evidence,
                    eligibility_checks=eligibility_checks_by_posting.get(posting["posting_id"], []),
                ))
        summary["validation_errors"] = errors
        if errors and summary["status"] == "success":
            summary["status"] = "partial"
            summary["zero_results"] = False
        summaries.append(summary)

    # Eligibility remains a separate, visible sort key; fit cannot rescue ineligibility.
    eligibility_order = {"Eligible": 0, "Unknown": 1, "Ineligible": 2}
    evaluations.sort(key=lambda row: (
        eligibility_order[row["eligibility"]["status"]],
        -(row["fit"]["score"] if row["fit"]["score"] is not None else -1),
        row["company"].casefold(),
        row["title"].casefold(),
    ))
    return {"sources": summaries, "evaluations": evaluations, "changes": changes}


def run_fixture_workflow(
    fixture_path: Path,
    state_path: Path,
    candidate_evidence: dict[str, str] | None = None,
    eligibility_checks_by_posting: dict[str, list[dict[str, Any]]] | None = None,
) -> dict[str, Any]:
    try:
        fixture = json.loads(fixture_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"Cannot read fixture results from {fixture_path}: {exc}") from exc
    if fixture.get("schema_version") != "1.0" or not isinstance(fixture.get("sources"), list):
        raise ValueError("Fixture file must have schema_version '1.0' and a sources array")
    state = load_state(state_path)
    result = process_source_results(
        fixture["sources"], state,
        candidate_evidence=candidate_evidence,
        eligibility_checks_by_posting=eligibility_checks_by_posting,
    )
    save_state(state_path, state)
    result["state_path"] = str(state_path)
    result["state_posting_count"] = len(state["postings"])
    return result
