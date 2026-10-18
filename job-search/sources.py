"""Permitted, rate-limited job-source adapters.

No requests are made by importing this module. A network request happens only
when the user explicitly starts a search from the CLI.
"""
from __future__ import annotations

import hashlib
import html
import json
import os
import re
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone
from typing import Any, Callable

from workflow import SKILL_ALIASES, _contains_term

ADZUNA_ENDPOINT = "https://api.adzuna.com/v1/api/jobs/in/search/1"
REMOTIVE_ENDPOINT = "https://remotive.com/api/remote-jobs"
USER_AGENT = "ResumeJobSearch/1.0 (personal research; source links preserved)"
SOURCE_BUDGETS = {
    "Adzuna": {"minute": 25, "day": 250, "week": 1000, "month": 2500},
    "Remotive": {"minute": 2, "day": 4},
}


class SourceRequestError(Exception):
    def __init__(self, status: str, message: str) -> None:
        super().__init__(message)
        self.status = status
        self.message = message


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def to_rfc3339(value: Any) -> str | None:
    if not isinstance(value, str) or not value.strip():
        return None
    candidate = value.strip()
    try:
        parsed = datetime.fromisoformat(candidate.replace("Z", "+00:00"))
    except ValueError:
        return None
    # A timezone-less source timestamp is not silently treated as UTC.
    if parsed.tzinfo is None:
        return None
    return parsed.astimezone(timezone.utc).isoformat().replace("+00:00", "Z")


def strip_html(value: Any) -> str:
    if not isinstance(value, str):
        return ""
    unescaped = html.unescape(value)
    without_tags = re.sub(r"<[^>]*>", " ", unescaped)
    return re.sub(r"\s+", " ", without_tags).strip()


def extract_skills(text: str) -> list[str]:
    found = []
    for skill, aliases in SKILL_ALIASES.items():
        if any(_contains_term(text, alias) for alias in aliases) and skill not in found:
            found.append(skill)
    return found


def infer_work_mode(text: str) -> str:
    lower = text.casefold()
    if re.search(r"\b(remote|work from anywhere|fully distributed)\b", lower):
        return "remote"
    if re.search(r"\bhybrid\b", lower):
        return "hybrid"
    if re.search(r"\b(on[- ]?site|onsite|in[- ]office)\b", lower):
        return "onsite"
    return "unknown"


def normalize_employment_type(value: Any) -> str:
    normalized = str(value or "").casefold().replace("-", "_").replace(" ", "_")
    aliases = {
        "full_time": "full_time",
        "permanent": "full_time",
        "part_time": "part_time",
        "contract": "contract",
        "contractor": "contract",
        "freelance": "contract",
        "internship": "internship",
        "temporary": "temporary",
    }
    return aliases.get(normalized, "unknown")


def content_digest(job: dict[str, Any]) -> str:
    material = json.dumps(job, sort_keys=True, ensure_ascii=False, separators=(",", ":"))
    return hashlib.sha256(material.encode("utf-8")).hexdigest()


def normalize_adzuna_job(raw: dict[str, Any], retrieved_at: str) -> dict[str, Any]:
    if not isinstance(raw, dict):
        raise ValueError("Adzuna item must be a JSON object.")
    title = str(raw.get("title") or "").strip()
    company_data = raw.get("company")
    company = str(company_data.get("display_name") or "").strip() if isinstance(company_data, dict) else ""
    url = str(raw.get("redirect_url") or "").strip()
    if not title or not company or not url:
        raise ValueError("Adzuna item is missing title, company, or original listing URL.")

    location_data = raw.get("location")
    location = str(location_data.get("display_name") or "").strip() if isinstance(location_data, dict) else ""
    locations = [location] if location else []
    description = strip_html(raw.get("description"))
    job_text = f"{title} {description}"
    job = {
        "title": title,
        "company": company,
        "locations": locations,
        "work_mode": infer_work_mode(job_text),
        "employment_type": normalize_employment_type(
            raw.get("contract_time") or raw.get("contract_type")
        ),
        "description": description,
        "skills": extract_skills(job_text),
        "experience_min_years": None,
        "experience_max_years": None,
        "posted_at": to_rfc3339(raw.get("created")),
        "deadline": None,
        "apply_url": url,
    }
    provider_id = raw.get("id")
    posting_id = f"adzuna-{provider_id}" if provider_id is not None else "adzuna-" + hashlib.sha256(url.encode()).hexdigest()[:24]
    return {
        "schema_version": "1.0",
        "posting_id": posting_id,
        "source": {"name": "Adzuna", "url": url, "retrieved_at": retrieved_at},
        "job": job,
        "record": {
            "first_seen_at": retrieved_at,
            "last_seen_at": retrieved_at,
            "status": "open",
            "content_hash": content_digest(job),
        },
    }


def normalize_remotive_job(raw: dict[str, Any], retrieved_at: str) -> dict[str, Any]:
    if not isinstance(raw, dict):
        raise ValueError("Remotive item must be a JSON object.")
    title = str(raw.get("title") or "").strip()
    company = str(raw.get("company_name") or "").strip()
    url = str(raw.get("url") or "").strip()
    if not title or not company or not url:
        raise ValueError("Remotive item is missing title, company, or original listing URL.")

    description = strip_html(raw.get("description"))
    location = str(raw.get("candidate_required_location") or "").strip()
    job_text = f"{title} {description} {raw.get('category') or ''}"
    job = {
        "title": title,
        "company": company,
        "locations": [location] if location else [],
        # Every Remotive listing is remote; candidate_required_location records restrictions.
        "work_mode": "remote",
        "employment_type": normalize_employment_type(raw.get("job_type")),
        "description": description,
        "skills": extract_skills(job_text),
        "experience_min_years": None,
        "experience_max_years": None,
        "posted_at": to_rfc3339(raw.get("publication_date")),
        "deadline": None,
        "apply_url": url,
    }
    provider_id = raw.get("id")
    posting_id = f"remotive-{provider_id}" if provider_id is not None else "remotive-" + hashlib.sha256(url.encode()).hexdigest()[:24]
    return {
        "schema_version": "1.0",
        "posting_id": posting_id,
        "source": {"name": "Remotive", "url": url, "retrieved_at": retrieved_at},
        "job": job,
        "record": {
            "first_seen_at": retrieved_at,
            "last_seen_at": retrieved_at,
            "status": "open",
            "content_hash": content_digest(job),
        },
    }


def _parse_call_time(value: str) -> datetime | None:
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except (TypeError, ValueError):
        return None
    if parsed.tzinfo is None:
        return None
    return parsed.astimezone(timezone.utc)


def source_budget_error(
    state: dict[str, Any],
    source: str,
    now: datetime | None = None,
) -> str | None:
    """Return a human-readable rate-limit error if a call would exceed source guidance."""
    budget = SOURCE_BUDGETS.get(source)
    if budget is None:
        return f"No request budget is configured for source {source}."
    now = (now or utc_now()).astimezone(timezone.utc)
    timestamps = [
        parsed for raw in state.get("source_calls", {}).get(source, [])
        if (parsed := _parse_call_time(raw)) is not None
    ]
    windows = {
        "minute": timedelta(minutes=1),
        "day": timedelta(days=1),
        "week": timedelta(days=7),
        "month": timedelta(days=30),
    }
    for window_name, limit in budget.items():
        cutoff = now - windows[window_name]
        count = sum(cutoff < stamp <= now for stamp in timestamps)
        if count >= limit:
            return f"{source} request limit reached for the last {window_name} ({limit} calls); try later."
    return None


def record_source_call(state: dict[str, Any], source: str, timestamp: datetime | None = None) -> None:
    stamp = (timestamp or utc_now()).astimezone(timezone.utc).isoformat().replace("+00:00", "Z")
    state.setdefault("source_calls", {}).setdefault(source, []).append(stamp)
    # Keep enough history to enforce the longest window without allowing unbounded growth.
    cutoff = (timestamp or utc_now()).astimezone(timezone.utc) - timedelta(days=31)
    kept = []
    for raw in state["source_calls"][source]:
        parsed = _parse_call_time(raw)
        if parsed is None or parsed >= cutoff:
            kept.append(raw)
    state["source_calls"][source] = kept


def request_json(url: str, timeout: float = 20.0, opener: Callable[..., Any] | None = None) -> Any:
    request = urllib.request.Request(url, headers={"Accept": "application/json", "User-Agent": USER_AGENT})
    do_open = opener or urllib.request.urlopen
    try:
        with do_open(request, timeout=timeout) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        if exc.code in {401, 403, 429}:
            raise SourceRequestError("blocked", f"Source denied or rate-limited the request (HTTP {exc.code}).") from exc
        raise SourceRequestError("failed", f"Source request failed (HTTP {exc.code}).") from exc
    except (urllib.error.URLError, TimeoutError, OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise SourceRequestError("failed", f"Source request failed: {type(exc).__name__}.") from exc


def _items_from_payload(payload: Any, key: str, source: str) -> list[dict[str, Any]]:
    if not isinstance(payload, dict) or not isinstance(payload.get(key), list):
        raise SourceRequestError("failed", f"{source} returned an unexpected response shape; the search is incomplete.")
    items = payload[key]
    return items


def search_adzuna(query: str, location: str, limit: int, retrieved_at: str,
                  opener: Callable[..., Any] | None = None) -> dict[str, Any]:
    app_id = os.environ.get("ADZUNA_APP_ID", "").strip()
    app_key = os.environ.get("ADZUNA_APP_KEY", "").strip()
    if not app_id or not app_key:
        raise SourceRequestError("failed", "Adzuna credentials are missing. Set ADZUNA_APP_ID and ADZUNA_APP_KEY.")
    params = {
        "app_id": app_id,
        "app_key": app_key,
        "results_per_page": max(1, min(int(limit), 50)),
        "what": query,
        "where": location,
        "content-type": "application/json",
    }
    url = ADZUNA_ENDPOINT + "?" + urllib.parse.urlencode(params)
    payload = request_json(url, opener=opener)
    raw_jobs = _items_from_payload(payload, "results", "Adzuna")
    postings, invalid = [], []
    for index, item in enumerate(raw_jobs):
        try:
            postings.append(normalize_adzuna_job(item, retrieved_at))
        except (AttributeError, TypeError, ValueError) as exc:
            invalid.append(f"Adzuna result {index + 1} ignored: {exc}")
    result = {"source": "Adzuna", "status": "success", "checked_at": retrieved_at,
              "postings": postings, "error": None}
    if invalid:
        result["status"] = "partial"
        result["error"] = "; ".join(invalid)
    return result


def search_remotive(query: str, limit: int, retrieved_at: str,
                    opener: Callable[..., Any] | None = None) -> dict[str, Any]:
    params = {"search": query, "limit": max(1, min(int(limit), 100))}
    url = REMOTIVE_ENDPOINT + "?" + urllib.parse.urlencode(params)
    payload = request_json(url, opener=opener)
    raw_jobs = _items_from_payload(payload, "jobs", "Remotive")
    postings, invalid = [], []
    for index, item in enumerate(raw_jobs):
        try:
            postings.append(normalize_remotive_job(item, retrieved_at))
        except (AttributeError, TypeError, ValueError) as exc:
            invalid.append(f"Remotive result {index + 1} ignored: {exc}")
    result = {"source": "Remotive", "status": "success", "checked_at": retrieved_at,
              "postings": postings, "error": None}
    if invalid:
        result["status"] = "partial"
        result["error"] = "; ".join(invalid)
    return result
