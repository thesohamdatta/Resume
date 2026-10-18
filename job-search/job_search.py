#!/usr/bin/env python3
"""Local-first job search for private-sector technology roles in India."""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import sources
import workflow

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_STATE = Path("job-search/state/jobs.json")
EVIDENCE_PATHS = (
    "data/facts.yaml",
    "content/github/evidence.md",
)
APPLICATION_STATUSES = ("Preparing", "Applied", "Interview", "Rejected", "Offer", "Withdrawn")
APPLICATION_TRANSITIONS = {
    None: {"Preparing", "Applied"},
    "Preparing": {"Preparing", "Applied", "Withdrawn"},
    "Applied": {"Applied", "Interview", "Rejected", "Offer", "Withdrawn"},
    "Interview": {"Interview", "Rejected", "Offer", "Withdrawn"},
    "Rejected": set(),
    "Offer": set(),
    "Withdrawn": set(),
}


def timestamp_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def load_candidate_evidence() -> dict[str, str]:
    evidence: dict[str, str] = {}
    for relative in EVIDENCE_PATHS:
        path = REPO_ROOT / relative
        if path.is_file():
            evidence[relative] = path.read_text(encoding="utf-8")
    return evidence


def load_eligibility_checks(path: Path | None) -> dict[str, list[dict[str, Any]]]:
    if path is None or not path.exists():
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"Cannot read eligibility checks from {path}: {exc}") from exc
    if not isinstance(data, dict):
        raise ValueError("Eligibility checks file must be an object keyed by posting ID.")
    return data


def run_search(args: argparse.Namespace) -> dict[str, Any]:
    state = workflow.load_state(args.state)
    checked_at = timestamp_now()
    now = datetime.fromisoformat(checked_at.replace("Z", "+00:00"))
    selected = ["Adzuna", "Remotive"] if args.source == "both" else [args.source]
    source_results: list[dict[str, Any]] = []

    for source_name in selected:
        if source_name == "Adzuna" and not (
            os.environ.get("ADZUNA_APP_ID", "").strip()
            and os.environ.get("ADZUNA_APP_KEY", "").strip()
        ):
            source_results.append({
                "source": "Adzuna", "status": "failed", "checked_at": checked_at,
                "postings": [], "error": "Adzuna credentials are missing. Set ADZUNA_APP_ID and ADZUNA_APP_KEY.",
            })
            continue

        budget_error = sources.source_budget_error(state, source_name, now)
        if budget_error:
            source_results.append({
                "source": source_name, "status": "blocked", "checked_at": checked_at,
                "postings": [], "error": budget_error,
            })
            continue

        sources.record_source_call(state, source_name, now)
        try:
            if source_name == "Adzuna":
                result = sources.search_adzuna(args.query, args.location, args.limit, checked_at)
            else:
                result = sources.search_remotive(args.query, args.limit, checked_at)
        except sources.SourceRequestError as exc:
            result = {
                "source": source_name, "status": exc.status, "checked_at": checked_at,
                "postings": [], "error": exc.message,
            }
        except (ValueError, TypeError) as exc:
            result = {
                "source": source_name, "status": "failed", "checked_at": checked_at,
                "postings": [], "error": f"Could not process source response: {exc}",
            }
        source_results.append(result)

    result = workflow.process_source_results(
        source_results,
        state,
        candidate_evidence=load_candidate_evidence(),
        eligibility_checks_by_posting=load_eligibility_checks(args.eligibility_checks),
    )
    workflow.save_state(args.state, state)
    result["state_path"] = str(args.state)
    result["state_posting_count"] = len(state["postings"])
    return result


def safe_component(value: str) -> str:
    cleaned = re.sub(r"[^A-Za-z0-9]+", "_", value).strip("_")
    return cleaned[:45] or "job"


def safe_header_value(value: str, fallback: str) -> str:
    """Keep imported source text on one line so it cannot add input fields."""
    cleaned = " ".join(str(value).replace("\r", " ").replace("\n", " ").split())
    return cleaned or fallback

def cmd_list(args: argparse.Namespace) -> dict[str, Any]:
    state = workflow.load_state(args.state)
    rows = []
    for posting_id, record in sorted(state["postings"].items()):
        posting = record["current"]
        opportunity_id = workflow.opportunity_id_for_posting(state, posting_id)
        opportunity = state["opportunities"].get(opportunity_id, {})
        application = state["applications"].get(opportunity_id)
        rows.append({
            "posting_id": posting_id,
            "title": posting["job"]["title"],
            "company": posting["job"]["company"],
            "source": posting["source"]["name"],
            "source_url": posting["source"]["url"],
            "posting_status": posting["record"]["status"],
            "decision": opportunity.get("decision", "Discovered"),
            "application_status": application.get("status") if application else None,
            "last_seen_at": posting["record"]["last_seen_at"],
        })
    return {"postings": rows, "count": len(rows), "state_path": str(args.state)}


def cmd_decision(args: argparse.Namespace) -> dict[str, Any]:
    state = workflow.load_state(args.state)
    posting_id = args.posting_id
    if posting_id not in state["postings"]:
        raise ValueError(f"Unknown posting ID: {posting_id}")
    opportunity_id = workflow.opportunity_id_for_posting(state, posting_id)
    if opportunity_id in state["applications"]:
        raise ValueError("This opportunity already has an application record; do not move it back to a pre-application decision.")
    opportunity = state["opportunities"].get(opportunity_id)
    if not opportunity:
        opportunity = {"posting_ids": [posting_id]}
        state["opportunities"][opportunity_id] = opportunity
    opportunity["decision"] = "Shortlisted" if args.decision == "shortlist" else "Not pursuing"
    opportunity["updated_at"] = timestamp_now()
    workflow.save_state(args.state, state)
    return {"posting_id": posting_id, "opportunity_id": opportunity_id, "decision": opportunity["decision"]}


def cmd_application(args: argparse.Namespace) -> dict[str, Any]:
    state = workflow.load_state(args.state)
    posting_id = args.posting_id
    if posting_id not in state["postings"]:
        raise ValueError(f"Unknown posting ID: {posting_id}")
    opportunity_id = workflow.opportunity_id_for_posting(state, posting_id)
    opportunity = state["opportunities"].get(opportunity_id)
    if not opportunity or opportunity.get("decision") != "Shortlisted":
        raise ValueError("Shortlist the opportunity before tracking an application.")
    now = timestamp_now()
    application = state["applications"].get(opportunity_id, {
        "opportunity_id": opportunity_id,
        "posting_id": posting_id,
        "posting_ids": opportunity.get("posting_ids", [posting_id]),
        "created_at": now,
        "notes": "",
    })
    previous_status = application.get("status")
    if args.status not in APPLICATION_TRANSITIONS.get(previous_status, set()):
        raise ValueError(f"Invalid application status transition: {previous_status or 'None'} -> {args.status}")
    application["status"] = args.status
    application["updated_at"] = now
    if args.notes is not None:
        application["notes"] = args.notes
    if args.status in {"Applied", "Interview", "Rejected", "Offer", "Withdrawn"}:
        application.setdefault("applied_at", now)
    state["applications"][opportunity_id] = application
    workflow.save_state(args.state, state)
    return application


def cmd_handoff(args: argparse.Namespace) -> dict[str, Any]:
    state = workflow.load_state(args.state)
    posting_id = args.posting_id
    if posting_id not in state["postings"]:
        raise ValueError(f"Unknown posting ID: {posting_id}")
    opportunity_id = workflow.opportunity_id_for_posting(state, posting_id)
    opportunity = state["opportunities"].get(opportunity_id)
    if not opportunity or opportunity.get("decision") != "Shortlisted":
        raise ValueError("Only a shortlisted opportunity can be handed to the Resume Engine.")

    posting = state["postings"][posting_id]["current"]
    now = datetime.now(timezone.utc)
    run_name = args.run_name or (
        f"{safe_component(posting['job']['company'])}_"
        f"{safe_component(posting['job']['title'])}_{now.strftime('%Y-%m')}"
    )
    if not re.fullmatch(r"[A-Za-z0-9_-]{1,120}", run_name):
        raise ValueError("Run name may contain only letters, numbers, underscores, and hyphens.")
    run_dir = REPO_ROOT / "applications" / run_name
    input_path = run_dir / "input.md"
    if run_dir.exists():
        raise ValueError(f"Application run directory already exists and was not overwritten: {run_dir.relative_to(REPO_ROOT)}")
    existing_application = state["applications"].get(opportunity_id)
    if existing_application and existing_application.get("resume_input"):
        raise ValueError("A Resume Engine input is already recorded for this opportunity; it was not replaced.")

    job = posting["job"]
    source = posting["source"]
    jd_lines = (job.get("description") or "").replace("\r", "").split("\n")
    jd_block = "\n".join("  " + line for line in jd_lines)
    notes = (
        f"Discovered through {source['name']} at {source['retrieved_at']}. "
        "Verify the original listing and requirements before preparing the resume. "
        "The source description may not contain every detail from the employer's full posting."
    )
    content = (
        "# Application Input\n\n"
        f"company: {job['company']}\n"
        f"mode: {args.mode}\n"
        f"role: {job['title']}\n"
        f"jd_url: {source['url']}\n"
        "jd: |\n"
        f"{jd_block}\n"
        "notes: |\n"
        f"  {notes}\n"
    )
    run_dir.mkdir(parents=True, exist_ok=True)
    input_path.write_text(content, encoding="utf-8")
    application = state["applications"].get(opportunity_id, {
        "opportunity_id": opportunity_id,
        "posting_id": posting_id,
        "posting_ids": opportunity.get("posting_ids", [posting_id]),
        "created_at": timestamp_now(),
        "notes": "",
    })
    application["status"] = "Preparing"
    application["updated_at"] = timestamp_now()
    application["resume_input"] = str(input_path.relative_to(REPO_ROOT))
    state["applications"][opportunity_id] = application
    workflow.save_state(args.state, state)
    return {
        "posting_id": posting_id,
        "status": "Preparing",
        "input": str(input_path.relative_to(REPO_ROOT)),
        "mode": args.mode,
        "source_url": source["url"],
        "automatic_submission": False,
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)

    validate = sub.add_parser("validate", help="Validate one or more canonical posting JSON files.")
    validate.add_argument("files", nargs="+", type=Path)

    fixtures = sub.add_parser("run-fixtures", help="Run the deterministic offline workflow on a fixture result file.")
    fixtures.add_argument("--fixtures", type=Path, default=Path("job-search/fixtures/sample-search-results.json"))
    fixtures.add_argument("--state", type=Path, default=DEFAULT_STATE)
    fixtures.add_argument("--eligibility-checks", type=Path, default=Path("job-search/state/eligibility-checks.json"))

    search = sub.add_parser("search", help="Search permitted live sources. No search runs during import or setup.")
    search.add_argument("--source", choices=("Adzuna", "Remotive", "both"), default="both")
    search.add_argument("--query", required=True, help="Role or technology keywords.")
    search.add_argument("--location", default="India", help="Adzuna location query; defaults to India.")
    search.add_argument("--limit", type=int, default=20)
    search.add_argument("--state", type=Path, default=DEFAULT_STATE)
    search.add_argument("--eligibility-checks", type=Path, default=Path("job-search/state/eligibility-checks.json"))

    listing = sub.add_parser("list", help="List saved postings and separate application status.")
    listing.add_argument("--state", type=Path, default=DEFAULT_STATE)

    link = sub.add_parser("link-postings", help="Link listings only when a shared employer requisition ID is verified.")
    link.add_argument("posting_ids", nargs="+")
    link.add_argument("--requisition-id", required=True)
    link.add_argument("--evidence-source", required=True, help="URL or source reference supporting the shared requisition ID.")
    link.add_argument("--state", type=Path, default=DEFAULT_STATE)

    decision = sub.add_parser("shortlist", help="Shortlist a saved posting for possible application preparation.")
    decision.add_argument("posting_id")
    decision.add_argument("--state", type=Path, default=DEFAULT_STATE)
    decision.set_defaults(decision="shortlist")

    reject = sub.add_parser("not-pursuing", help="Mark a posting as not pursuing before an application exists.")
    reject.add_argument("posting_id")
    reject.add_argument("--state", type=Path, default=DEFAULT_STATE)
    reject.set_defaults(decision="not-pursuing")

    application = sub.add_parser("application", help="Record the user's application progress; this does not submit an application.")
    application.add_argument("posting_id")
    application.add_argument("--status", choices=APPLICATION_STATUSES, required=True)
    application.add_argument("--notes")
    application.add_argument("--state", type=Path, default=DEFAULT_STATE)

    handoff = sub.add_parser("handoff", help="Create the standard Resume Engine input for a shortlisted posting.")
    handoff.add_argument("posting_id")
    handoff.add_argument("--mode", choices=("startup", "mnc", "referral"), required=True)
    handoff.add_argument("--run-name")
    handoff.add_argument("--state", type=Path, default=DEFAULT_STATE)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        if args.command == "validate":
            validator = workflow.load_schema()
            from jsonschema import Draft202012Validator, FormatChecker
            compiled = Draft202012Validator(validator, format_checker=FormatChecker())
            failures: list[str] = []
            for path in args.files:
                try:
                    data = json.loads(path.read_text(encoding="utf-8"))
                except (OSError, json.JSONDecodeError) as exc:
                    failures.append(f"{path}: cannot read JSON: {exc}")
                    continue
                errors = sorted(compiled.iter_errors(data), key=lambda error: list(map(str, error.absolute_path)))
                if errors:
                    failures.extend(f"{path}: {'/'.join(map(str, error.absolute_path)) or '<root>'}: {error.message}" for error in errors)
                else:
                    print(f"PASS: {path}")
            if failures:
                print("\n".join(failures), file=sys.stderr)
                return 1
            return 0
        if args.command == "run-fixtures":
            result = workflow.run_fixture_workflow(
                args.fixtures, args.state,
                candidate_evidence=load_candidate_evidence(),
                eligibility_checks_by_posting=load_eligibility_checks(args.eligibility_checks),
            )
        elif args.command == "search":
            if args.limit < 1:
                raise ValueError("--limit must be positive")
            result = run_search(args)
        elif args.command == "list":
            result = cmd_list(args)
        elif args.command == "link-postings":
            state = workflow.load_state(args.state)
            opportunity_id = workflow.link_postings(
                state, args.posting_ids, args.requisition_id, args.evidence_source
            )
            workflow.save_state(args.state, state)
            result = {"opportunity_id": opportunity_id, **state["opportunities"][opportunity_id]}
        elif args.command in {"shortlist", "not-pursuing"}:
            result = cmd_decision(args)
        elif args.command == "application":
            result = cmd_application(args)
        elif args.command == "handoff":
            result = cmd_handoff(args)
        else:
            parser.error("Unknown command")
            return 2
    except (OSError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
