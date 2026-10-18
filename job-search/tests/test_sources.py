from __future__ import annotations

import sys
import unittest
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import sources  # noqa: E402
import workflow  # noqa: E402


class SourceAdapterTests(unittest.TestCase):
    def test_adzuna_normalization_preserves_source_url_and_unknown_work_mode(self) -> None:
        posting = sources.normalize_adzuna_job({
            "id": 142,
            "title": "Junior Python Engineer",
            "company": {"display_name": "Example Ltd"},
            "redirect_url": "https://example.com/jobs/142",
            "location": {"display_name": "Pune, Maharashtra"},
            "description": "<p>Build Python and FastAPI services.</p>",
            "contract_time": "full_time",
            "created": "2026-10-18T10:00:00Z",
        }, "2026-10-19T10:00:00Z")
        self.assertEqual(posting["posting_id"], "adzuna-142")
        self.assertEqual(posting["source"]["url"], "https://example.com/jobs/142")
        self.assertEqual(posting["job"]["work_mode"], "unknown")
        self.assertEqual(posting["job"]["employment_type"], "full_time")
        self.assertEqual(posting["job"]["skills"], ["Python", "FastAPI"])
        self.assertNotIn("<p>", posting["job"]["description"])
        self.assertEqual(workflow.validate_posting_object(posting), [])

    def test_remotive_normalization_keeps_remote_location_and_source_attribution(self) -> None:
        posting = sources.normalize_remotive_job({
            "id": 88,
            "title": "Python Developer",
            "company_name": "Remote Example",
            "url": "https://remotive.com/remote-jobs/software-dev/python-developer-88",
            "candidate_required_location": "Worldwide",
            "job_type": "contract",
            "category": "Software Development",
            "publication_date": "2026-10-18T10:00:00Z",
            "description": "<p>Use Python and REST APIs.</p>",
        }, "2026-10-19T10:00:00Z")
        self.assertEqual(posting["source"]["name"], "Remotive")
        self.assertEqual(posting["source"]["url"], "https://remotive.com/remote-jobs/software-dev/python-developer-88")
        self.assertEqual(posting["job"]["work_mode"], "remote")
        self.assertEqual(posting["job"]["locations"], ["Worldwide"])
        self.assertEqual(posting["job"]["employment_type"], "contract")
        self.assertEqual(workflow.validate_posting_object(posting), [])

    def test_timezone_free_source_date_stays_unknown(self) -> None:
        self.assertIsNone(sources.to_rfc3339("2026-10-18T10:00:00"))

    def test_invalid_source_item_is_rejected_clearly(self) -> None:
        with self.assertRaisesRegex(ValueError, "title, company, or original listing URL"):
            sources.normalize_adzuna_job({"id": 123, "title": "Engineer"}, "2026-10-19T10:00:00Z")

    def test_remotive_daily_limit_is_enforced_before_request(self) -> None:
        now = datetime(2026, 10, 19, 10, 0, tzinfo=timezone.utc)
        state = workflow.empty_state()
        state["source_calls"]["Remotive"] = [
            "2026-10-19T01:00:00Z",
            "2026-10-19T02:00:00Z",
            "2026-10-19T03:00:00Z",
            "2026-10-19T04:00:00Z",
        ]
        self.assertIn("last day", sources.source_budget_error(state, "Remotive", now))

    def test_old_calls_do_not_trigger_daily_limit(self) -> None:
        now = datetime(2026, 10, 19, 10, 0, tzinfo=timezone.utc)
        state = workflow.empty_state()
        state["source_calls"]["Remotive"] = [
            "2026-10-17T01:00:00Z",
            "2026-10-17T02:00:00Z",
            "2026-10-17T03:00:00Z",
            "2026-10-17T04:00:00Z",
        ]
        self.assertIsNone(sources.source_budget_error(state, "Remotive", now))


if __name__ == "__main__":
    unittest.main()
