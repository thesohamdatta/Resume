#!/usr/bin/env python3
"""Deterministic, offline-first job-search workflow primitives."""
from __future__ import annotations

import copy
import json
import os
import re
import tempfile
from datetime import datetime, timezone
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


def _timestamp(value: str) -> datetime:
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if parsed.tzinfo is None:
        raise ValueError("Timestamps must include a timezone.")
    return parsed.astimezone(timezone.utc)


def upsert_posting(state: dict[str, Any], posting: dict[str, Any]) -> str:
    """Insert or refresh one source listing while preserving prior versions and decisions."""
    errors = validate_posting_object(posting)
    if errors:
        raise ValueError("Invalid posting: " + "; ".join(errors))

    posting_id = posting["posting_id"]
    incoming = copy.deepcopy(posting)
    existing = state["postings"].get(posting_id)
    if existing is None:
        state["postings"][posting_id] = {"current": incoming, "history": []}
        return "inserted"

    previous = existing["current"]
    old_hash = previous["record"].get("content_hash")
    new_hash = incoming["record"].get("content_hash")
    old_status = previous["record"].get("status")
    new_status = incoming["record"].get("status")
    old_url = previous["source"].get("url")
    new_url = incoming["source"].get("url")
    if old_hash != new_hash or old_status != new_status or old_url != new_url:
        if old_hash != new_hash:
            change = "content_changed"
        elif old_status != new_status:
            change = "status_changed"
        else:
            change = "source_url_changed"
        existing["history"].append({
            "posting": copy.deepcopy(previous),
            "change": change,
            "observed_at": incoming["source"]["retrieved_at"],
        })
    incoming["record"]["first_seen_at"] = previous["record"]["first_seen_at"]
    previous_seen = previous["record"]["last_seen_at"]
    incoming_seen = incoming["record"]["last_seen_at"]
    incoming["record"]["last_seen_at"] = (
        incoming_seen if _timestamp(incoming_seen) > _timestamp(previous_seen) else previous_seen
    )
    existing["current"] = incoming
    return "updated" if old_hash != new_hash or old_status != new_status or old_url != new_url else "unchanged"


def evaluate_eligibility(checks: list[dict[str, Any]] | None) -> dict[str, Any]:
    """Evaluate only explicit, reviewed mandatory checks; never guess eligibility."""
    checks = checks or []
    normalized_checks = []
    for original in checks:
        item = copy.deepcopy(original)
        if item.get("status") not in ELIGIBILITY_STATUSES:
            raise ValueError("Each eligibility check needs status met, unmet, or unknown")
        # A positive or negative eligibility judgement needs a reviewable source.
        # Without it, the status is preserved as unknown rather than trusted.
        if item.get("status") in {"met", "unmet"} and not (
            isinstance(item.get("evidence"), str) and item["evidence"].strip()
            and isinstance(item.get("evidence_source"), str) and item["evidence_source"].strip()
        ):
            item["status"] = "unknown"
            item["evidence_warning"] = "No evidence text and evidence source were provided."
        normalized_checks.append(item)

    mandatory = [item for item in normalized_checks if item.get("mandatory") is True]
    if any(item["status"] == "unmet" for item in mandatory):
        status = "Ineligible"
    elif mandatory and all(item["status"] == "met" for item in mandatory):
        status = "Eligible"
    else:
        status = "Unknown"

    reasons = [
        f"{item.get('description', 'Mandatory requirement')}: {item['status']}"
        + (f" (evidence: {item['evidence_source']})" if item.get("evidence_source") and item["status"] != "unknown" else "")
        for item in mandatory
    ]
    if not mandatory:
        reasons.append("No reviewed mandatory requirements are available; eligibility remains unknown.")
    elif status == "Unknown":
        reasons.append("At least one mandatory requirement is not confirmed.")
    return {"status": status, "reasons": reasons, "checks": normalized_checks}


def _contains_term(text: str, term: str) -> bool:
    """Match a phrase as text, avoiding loose single-letter/sub-string matches."""
    normalized_text = " ".join(text.casefold().replace("/", " ").replace("-", " ").split())
    normalized_term = " ".join(term.casefold().replace("/", " ").replace("-", " ").split())
    if not normalized_term:
        return False
    if " " not in normalized_term:
        return re.search(rf"(?<![a-z0-9]){re.escape(normalized_term)}(?![a-z0-9])", normalized_text) is not None
    return normalized_term in normalized_text


NEGATIVE_EVIDENCE = re.compile(
    r"\b(?:do not|don't|never|must not|should not)\s+(?:claim|say|present|describe|use|include|state|imply)\b"
    r"|\b(?:not|never)\s+(?:implemented|shipped|merged|production|verified|available|completed|owned|authored|built|employment)\b"
    r"|\bplanned\b|\broadmap\b|\bpending confirmation\b|\bself[- ]directed audit\b"
    r"|\bunverified\b|\bunsupported\b|\bno verified\b|\bnot proof\b|\bnot a claim\b",
    re.IGNORECASE,
)
EXCLUDED_SOURCE_BLOCKS = {
    "attribution_limits", "constraints", "review_note", "bullets", "bullet",
    "learning", "credentials", "notion_url", "credential_url", "inventory_url",
    "status", "progress_note", "planned", "future_work", "known_gaps",
}


def positive_evidence_text(content: str) -> str:
    """Remove explicit no-claim, plan, and constraint blocks before keyword matching."""
    positive: list[str] = []
    markdown_skip_level: int | None = None
    yaml_skip_indent: int | None = None

    for line in content.splitlines():
        stripped = line.strip()
        if not stripped:
            continue

        if stripped.startswith("#"):
            level = len(stripped) - len(stripped.lstrip("#"))
            heading = stripped[level:].strip().casefold()
            if markdown_skip_level is not None:
                if level <= markdown_skip_level:
                    markdown_skip_level = None
                else:
                    continue
            if any(term in heading for term in ("do not claim", "claim limits", "boundaries", "planned features")):
                markdown_skip_level = level
            continue
        if markdown_skip_level is not None:
            continue

        indentation = len(line) - len(line.lstrip())
        if yaml_skip_indent is not None:
            if indentation > yaml_skip_indent:
                continue
            yaml_skip_indent = None

        normalized = stripped.rstrip(":").casefold()
        if stripped.endswith(":") and normalized in EXCLUDED_SOURCE_BLOCKS:
            yaml_skip_indent = indentation
            continue
        if ":" in stripped:
            key = stripped.split(":", 1)[0].strip().casefold()
            if key in EXCLUDED_SOURCE_BLOCKS:
                continue
        if NEGATIVE_EVIDENCE.search(stripped):
            continue
        positive.append(stripped)

    return "\n".join(positive)


def evaluate_fit(posting: dict[str, Any], candidate_evidence: dict[str, str]) -> dict[str, Any]:
    skills = list(dict.fromkeys(posting.get("job", {}).get("skills", [])))
    candidate_evidence = {name: positive_evidence_text(text) for name, text in candidate_evidence.items()}
    if not skills:
        return {
            "score": None,
            "matched_skills": [],
            "missing_skills": [],
            "reasons": ["The listing has no structured skills to compare; no fit score was guessed."],
            "evidence_sources": [],
        }

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
        "source": posting["source"]["name"],
        "source_url": posting["source"]["url"],
        "retrieved_at": posting["source"]["retrieved_at"],
        "posting_status": posting["record"]["status"],
        "eligibility": evaluate_eligibility(eligibility_checks),
        "fit": evaluate_fit(posting, candidate_evidence),
    }


def summarize_source_result(result: dict[str, Any]) -> dict[str, Any]:
    status = result.get("status")
    count = len(result.get("postings") or [])
    zero_results = (count == 0) if status == "success" else None
    return {
        "source": result.get("source", "unknown"),
        "status": status,
        "count": count,
        "zero_results": zero_results,
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
        if result.get("status") in {"success", "partial"}:
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



def opportunity_id_for_posting(state: dict[str, Any], posting_id: str) -> str:
    """Return a linked opportunity ID, or the posting ID when it is not linked."""
    for opportunity_id, opportunity in state["opportunities"].items():
        if posting_id in opportunity.get("posting_ids", []):
            return opportunity_id
    return posting_id


def link_postings(
    state: dict[str, Any],
    posting_ids: list[str],
    requisition_id: str,
    evidence_source: str,
) -> str:
    """Explicitly link source listings only when the user supplies shared requisition evidence."""
    ids = sorted(set(posting_ids))
    requisition_id = requisition_id.strip()
    evidence_source = evidence_source.strip()
    if len(ids) < 2:
        raise ValueError("Provide at least two distinct posting IDs to link.")
    if not requisition_id:
        raise ValueError("A shared employer requisition ID is required; title/company similarity is not enough.")
    if not evidence_source:
        raise ValueError("An evidence source URL or reference is required.")

    linked_ids = set(ids)
    prior_opportunity_ids: set[str] = set()
    for posting_id in ids:
        if posting_id not in state["postings"]:
            raise ValueError(f"Unknown posting ID: {posting_id}")
        existing_opportunity_id = opportunity_id_for_posting(state, posting_id)
        existing = state["opportunities"].get(existing_opportunity_id, {})
        if existing_opportunity_id != posting_id and existing:
            prior_opportunity_ids.add(existing_opportunity_id)
            linked_ids.update(existing.get("posting_ids", []))
        if existing.get("decision") not in (None, "Discovered"):
            raise ValueError("Cannot link postings after a shortlist/not-pursuing decision; decide first how to preserve the record.")
        if posting_id in state["applications"] or existing_opportunity_id in state["applications"]:
            raise ValueError("Cannot link postings that already have application records.")
        evidence = existing.get("identity_evidence")
        if evidence and evidence.get("requisition_id") != requisition_id:
            raise ValueError("Conflicting requisition evidence already exists for a posting.")

    for posting_id in linked_ids:
        if posting_id not in state["postings"]:
            raise ValueError(f"Linked opportunity references missing posting: {posting_id}")

    identity_material = "|".join(sorted(linked_ids)) + "|" + requisition_id
    import hashlib
    opportunity_id = "opportunity-" + hashlib.sha256(identity_material.encode("utf-8")).hexdigest()[:16]
    for prior_id in prior_opportunity_ids:
        if prior_id != opportunity_id:
            state["opportunities"].pop(prior_id, None)
    state["opportunities"][opportunity_id] = {
        "posting_ids": sorted(linked_ids),
        "decision": "Discovered",
        "identity_evidence": {
            "type": "shared_employer_requisition_id",
            "requisition_id": requisition_id,
            "evidence_source": evidence_source,
        },
    }
    return opportunity_id

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
