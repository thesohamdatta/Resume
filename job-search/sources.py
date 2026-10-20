"""Permitted, rate-limited job-source adapters.

No requests are made by importing this module. A network request happens only
when the user explicitly starts a search from the CLI.
"""
from __future__ import annotations

import hashlib
import html
import json
from html.parser import HTMLParser
import os
import re
import urllib.error
import urllib.parse
import urllib.request
from datetime import date, datetime, timedelta, timezone
from typing import Any, Callable

from workflow import SKILL_ALIASES, _contains_term

ADZUNA_ENDPOINT = "https://api.adzuna.com/v1/api/jobs/in/search/1"
REMOTIVE_ENDPOINT = "https://remotive.com/api/remote-jobs"
CDAC_JOBS_URL = "https://www.cdac.gov.in/index.aspx?id=current_jobs"
NIELIT_JOBS_URL = "https://www.nielit.in/recruitments"
USER_AGENT = "ResumeJobSearch/1.0 (personal research; source links preserved)"
SOURCE_BUDGETS = {
    "Adzuna": {"minute": 25, "day": 250, "week": 1000, "month": 2500},
    "Remotive": {"minute": 2, "day": 4},
    # Conservative local pacing, not a claim about official portal quotas.
    "CDAC": {"minute": 1, "day": 4},
    "NIELIT": {"minute": 1, "day": 4},
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
        "employer_type": "unknown",
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
            "content_hash": content_digest({"source_url": url, "job": job}),
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
        "employer_type": "unknown",
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


class _RecruitmentHTMLParser(HTMLParser):
    """Small standard-library parser for public recruitment tables and link lists."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.rows: list[dict[str, Any]] = []
        self.links: list[dict[str, Any]] = []
        self._row: dict[str, Any] | None = None
        self._cell: list[str] | None = None
        self._anchor: dict[str, Any] | None = None
        self._row_depth = 0
        self._heading: list[str] | None = None
        self._archived = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs_map = dict(attrs)
        if tag in {"h1", "h2", "h3", "h4", "h5", "h6", "strong", "b"} and self._row is None:
            self._heading = []
        if tag == "tr":
            self._row_depth += 1
            if self._row_depth == 1:
                self._row = {"text": [], "cells": [], "links": [], "archived": self._archived}
                self._cell = None
        elif self._row is not None and tag in {"td", "th"}:
            self._cell = []
        if tag == "a":
            self._anchor = {
                "href": str(attrs_map.get("href") or "").strip(),
                "text": [],
                "archived": self._archived,
            }

    def handle_data(self, data: str) -> None:
        if self._row is not None:
            self._row["text"].append(data)
        if self._cell is not None:
            self._cell.append(data)
        if self._anchor is not None:
            self._anchor["text"].append(data)
        if self._heading is not None:
            self._heading.append(data)

    @staticmethod
    def _join(parts: list[str]) -> str:
        return re.sub(r"\s+", " ", " ".join(parts)).strip()

    def handle_endtag(self, tag: str) -> None:
        if tag == "a" and self._anchor is not None:
            link = {
                "href": self._anchor["href"],
                "text": self._join(self._anchor["text"]),
                "archived": self._anchor["archived"],
            }
            self.links.append(link)
            if self._row is not None:
                self._row["links"].append(link)
            self._anchor = None
        if tag in {"td", "th"} and self._row is not None and self._cell is not None:
            self._row["cells"].append(self._join(self._cell))
            self._cell = None
        if tag == "tr" and self._row_depth:
            self._row_depth -= 1
            if self._row_depth == 0 and self._row is not None:
                self._row["text"] = self._join(self._row["text"])
                self._row["cells"] = [cell for cell in self._row["cells"] if cell]
                self.rows.append(self._row)
                self._row = None
                self._cell = None
        if tag in {"h1", "h2", "h3", "h4", "h5", "h6", "strong", "b"} and self._heading is not None:
            heading = self._join(self._heading).casefold()
            if "archived job" in heading or "past vacancies" in heading:
                self._archived = True
            elif "current job" in heading or "current opening" in heading or "current vacancy" in heading:
                self._archived = False
            self._heading = None


_ROLE_WORDS = re.compile(
    r"\b(engineer|developer|programmer|scientist|research|software|technology|technical|"
    r"information technology|computer|AI engineer|machine learning|data|cyber|electronics|"
    r"project staff|project associate|project engineer|consultant|vacanc(?:y|ies)|recruitment|"
    r"advertisement|advt\.?|position[s]?|post[s]?)\b",
    re.IGNORECASE,
)
_EXCLUDED_LISTING = re.compile(
    r"\b(result of|selected candidates?|shortlisted candidates?|cancell?ation of recruitment|"
    r"cancelled recruitment|admit card|answer key|document verification schedule)\b",
    re.IGNORECASE,
)
_LOCATION_NAMES = (
    "Pune", "Delhi", "New Delhi", "Noida", "Mumbai", "Chennai", "Bengaluru",
    "Bangalore", "Hyderabad", "Kolkata", "Thiruvananthapuram", "Guwahati",
    "Mohali", "Ropar", "Chandigarh", "Imphal", "Patna", "Jaipur", "Lucknow",
    "Bhubaneswar", "Ahmedabad", "Indore", "Nagpur", "Kochi", "Calicut",
)


def _official_row_text(row: dict[str, Any]) -> str:
    return str(row.get("text") or "").strip()


def _is_listing_row(text: str) -> bool:
    if len(text) < 25 or _EXCLUDED_LISTING.search(text):
        return False
    return bool(_ROLE_WORDS.search(text))


def _query_matches(query: str, text: str) -> bool:
    """Loose enough for title variants, strict enough to reject unrelated ads."""
    query = query.strip()
    if not query:
        return True
    normalized = text.casefold()
    requested_skills = extract_skills(query)
    if requested_skills and any(_contains_term(normalized, skill) for skill in requested_skills):
        return True
    terms = [
        term for term in re.findall(r"[a-zA-Z0-9+#.]+", query.casefold())
        if term not in {"junior", "senior", "entry", "level", "role", "job", "jobs", "opening", "openings"}
    ]
    if not terms:
        return True
    threshold = max(1, (len(terms) + 1) // 2)
    return sum(1 for term in terms if _contains_term(normalized, term)) >= threshold


def _official_detail_url(links: list[dict[str, Any]], landing_url: str) -> str:
    """Prefer an official detail/advertisement link, not results or application forms."""
    candidates: list[tuple[int, str]] = []
    for link in links:
        href = str(link.get("href") or "").strip()
        label = str(link.get("text") or "").strip()
        lower = label.casefold()
        if not href or href.startswith(("javascript:", "mailto:", "#")):
            continue
        if _EXCLUDED_LISTING.search(lower):
            continue
        if re.search(r"\b(application proforma|application form|apply online|apply now|registration)\b", lower):
            continue
        absolute = urllib.parse.urljoin(landing_url, href)
        if urllib.parse.urlparse(absolute).scheme not in {"http", "https"}:
            continue
        if "detailed" in lower and ("advertisement" in lower or "advt" in lower):
            rank = 0
        elif re.search(r"\b(advertisement|advt|vacancy notice|recruitment notice)\b", lower):
            rank = 1
        elif _ROLE_WORDS.search(label) and len(label) > 20:
            rank = 2
        elif absolute.lower().endswith(".pdf"):
            rank = 3
        else:
            rank = 4
        candidates.append((rank, absolute))
    return sorted(candidates)[0][1] if candidates else landing_url


def _official_apply_url(links: list[dict[str, Any]], landing_url: str) -> str | None:
    for link in links:
        label = str(link.get("text") or "").strip().casefold()
        href = str(link.get("href") or "").strip()
        if re.search(r"\b(apply online|apply now|online application|register online)\b", label) and href:
            absolute = urllib.parse.urljoin(landing_url, href)
            if urllib.parse.urlparse(absolute).scheme in {"http", "https"}:
                return absolute
    return None


def _parse_date(value: str) -> date | None:
    clean = re.sub(r"(?i)(\d{1,2})(st|nd|rd|th)\b", r"\1", value.strip())
    formats = (
        "%d %B, %Y", "%d %B %Y", "%d %b, %Y", "%d %b %Y",
        "%d/%m/%Y", "%d-%m-%Y", "%Y-%m-%d",
    )
    for fmt in formats:
        try:
            return datetime.strptime(clean, fmt).date()
        except ValueError:
            continue
    return None


def _listing_deadline(row: dict[str, Any], source_name: str, text: str) -> date | None:
    cells = row.get("cells") or []
    if source_name == "NIELIT" and cells:
        # NIELIT's table explicitly labels the last column "Last Date of Application".
        parsed = _parse_date(str(cells[-1]))
        if parsed:
            return parsed
    match = re.search(
        r"(?i)(?:last date(?: of application)?|applications? close[s]?|apply on or before)\s*[:\-]?\s*"
        r"(\d{1,2}(?:st|nd|rd|th)?\s+[A-Za-z]+\s*,?\s+\d{4}|\d{1,2}[/-]\d{1,2}[/-]\d{4})",
        text,
    )
    return _parse_date(match.group(1)) if match else None


def _listing_locations(text: str) -> list[str]:
    if re.search(r"\b(across India|all India|India-wide|various locations)\b", text, re.IGNORECASE):
        return ["India"]
    return [name for name in _LOCATION_NAMES if _contains_term(text, name)]


def _listing_employment_type(text: str) -> str:
    lower = text.casefold()
    if re.search(r"\b(internship|interns|work based learning|wbl)\b", lower):
        return "internship"
    if re.search(r"\b(permanent|regular post|direct recruitment)\b", lower):
        return "full_time"
    if re.search(r"\b(contractual|contract basis|contract position)\b", lower):
        return "contract"
    if re.search(r"\b(temporary|short[- ]term contract)\b", lower):
        return "temporary"
    return "unknown"


def _normalize_official_row(
    row: dict[str, Any],
    source_name: str,
    company: str,
    landing_url: str,
    retrieved_at: str,
) -> dict[str, Any]:
    text = _official_row_text(row)
    cells = row.get("cells") or []
    raw_title = str(cells[1] if len(cells) >= 3 else (cells[0] if cells else text)).strip()
    title = re.sub(r"\s+", " ", re.sub(r"^\s*\d+\s*[.|)]?\s*", "", raw_title)).strip()
    title = title[:180].rstrip() if len(title) > 180 else title
    links = row.get("links") or []
    source_url = _official_detail_url(links, landing_url)
    deadline_date = _listing_deadline(row, source_name, text)
    deadline = None
    status = "unknown"
    retrieved = _parse_call_time(retrieved_at)
    if deadline_date:
        india_tz = timezone(timedelta(minutes=330))
        deadline = datetime.combine(deadline_date, datetime.max.time(), tzinfo=india_tz).isoformat()
        if retrieved and deadline_date >= retrieved.astimezone(india_tz).date():
            status = "open"
    description = text
    document_links = [
        f"{str(link.get('text') or 'Official document')}: {urllib.parse.urljoin(landing_url, str(link.get('href') or ''))}"
        for link in links
        if str(link.get("href") or "").strip()
        and urllib.parse.urlparse(urllib.parse.urljoin(landing_url, str(link.get("href") or ""))).scheme in {"http", "https"}
    ]
    if document_links:
        description += " Official links: " + " | ".join(document_links)
    job_text = f"{title} {description}"
    job = {
        "title": title or f"{source_name} technical recruitment notice",
        "company": company,
        "locations": _listing_locations(job_text),
        "work_mode": infer_work_mode(job_text),
        "employment_type": _listing_employment_type(job_text),
        "employer_type": "public_sector",
        "description": description,
        "skills": extract_skills(job_text),
        "experience_min_years": None,
        "experience_max_years": None,
        "posted_at": None,
        "deadline": deadline,
        # An advertisement is not necessarily an online application endpoint.
        "apply_url": _official_apply_url(links, landing_url),
    }
    identity = f"{source_url}|{title}|{text}"
    posting_id = source_name.casefold() + "-" + hashlib.sha256(identity.encode("utf-8")).hexdigest()[:24]
    return {
        "schema_version": "1.0",
        "posting_id": posting_id,
        "source": {"name": source_name, "url": source_url, "retrieved_at": retrieved_at},
        "job": job,
        "record": {
            "first_seen_at": retrieved_at,
            "last_seen_at": retrieved_at,
            "status": status,
            "content_hash": content_digest({"source_url": source_url, "job": job}),
        },
    }


def parse_official_recruitment_page(
    html_text: str,
    source_name: str,
    landing_url: str,
    query: str,
    retrieved_at: str,
) -> list[dict[str, Any]]:
    """Parse official public recruitment tables without guessing missing fields or status."""
    companies = {
        "CDAC": "Centre for Development of Advanced Computing (C-DAC)",
        "NIELIT": "National Institute of Electronics and Information Technology (NIELIT)",
    }
    if source_name not in companies:
        raise ValueError(f"Unsupported official source: {source_name}")
    parser = _RecruitmentHTMLParser()
    parser.feed(html_text)
    parser.close()

    rows = [row for row in parser.rows if not row.get("archived") and _is_listing_row(_official_row_text(row))]
    if not rows:
        # Some pages use descriptive links rather than tables. Navigation links and
        # result/cancellation notices are excluded; an unrecognized page fails visibly.
        seen: set[str] = set()
        for link in parser.links:
            label = str(link.get("text") or "").strip()
            lower = label.casefold()
            href = str(link.get("href") or "").strip()
            if link.get("archived") or not label or not href or href.startswith(("javascript:", "mailto:", "#")):
                continue
            if lower in {"current jobs", "current job opportunities", "recruitments", "home", "career"}:
                continue
            if _EXCLUDED_LISTING.search(label) or not _ROLE_WORDS.search(label):
                continue
            absolute = urllib.parse.urljoin(landing_url, href)
            if absolute in seen or urllib.parse.urlparse(absolute).scheme not in {"http", "https"}:
                continue
            seen.add(absolute)
            rows.append({"text": label, "cells": [label], "links": [link], "archived": False})
    if not rows:
        raise SourceRequestError(
            "failed",
            f"{source_name} recruitment page did not contain recognizable listing rows; the search is incomplete.",
        )

    postings: list[dict[str, Any]] = []
    for row in rows:
        text = _official_row_text(row)
        if _query_matches(query, text):
            postings.append(_normalize_official_row(row, source_name, companies[source_name], landing_url, retrieved_at))
    return postings


def request_text(url: str, timeout: float = 20.0, opener: Callable[..., Any] | None = None) -> str:
    request = urllib.request.Request(
        url,
        headers={"Accept": "text/html,application/xhtml+xml", "User-Agent": USER_AGENT},
    )
    do_open = opener or urllib.request.urlopen
    try:
        with do_open(request, timeout=timeout) as response:
            raw = response.read()
            charset = "utf-8"
            content_type = response.headers.get("Content-Type", "") if hasattr(response, "headers") else ""
            match = re.search(r"(?i)charset=([A-Za-z0-9._-]+)", content_type)
            if match:
                charset = match.group(1)
            return raw.decode(charset, errors="replace")
    except urllib.error.HTTPError as exc:
        if exc.code in {401, 403, 429}:
            raise SourceRequestError("blocked", f"Official source denied or rate-limited the request (HTTP {exc.code}).") from exc
        raise SourceRequestError("failed", f"Official source request failed (HTTP {exc.code}).") from exc
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        raise SourceRequestError("failed", f"Official source request failed: {type(exc).__name__}.") from exc


def _search_official_source(
    source_name: str,
    landing_url: str,
    query: str,
    limit: int,
    retrieved_at: str,
    opener: Callable[..., Any] | None = None,
) -> dict[str, Any]:
    page = request_text(landing_url, opener=opener)
    postings = parse_official_recruitment_page(page, source_name, landing_url, query, retrieved_at)
    return {
        "source": source_name,
        "status": "success",
        "checked_at": retrieved_at,
        "postings": postings[:max(1, min(int(limit), 50))],
        "error": None,
    }


def search_cdac(
    query: str,
    limit: int,
    retrieved_at: str,
    opener: Callable[..., Any] | None = None,
) -> dict[str, Any]:
    return _search_official_source("CDAC", CDAC_JOBS_URL, query, limit, retrieved_at, opener)


def search_nielit(
    query: str,
    limit: int,
    retrieved_at: str,
    opener: Callable[..., Any] | None = None,
) -> dict[str, Any]:
    return _search_official_source("NIELIT", NIELIT_JOBS_URL, query, limit, retrieved_at, opener)


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
