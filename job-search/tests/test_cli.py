from __future__ import annotations

import sys
import tempfile
import unittest
from argparse import Namespace
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT.parent))

import job_search  # noqa: E402
import workflow  # noqa: E402


def posting() -> dict:
    timestamp = "2026-10-19T10:00:00Z"
    return {
        "schema_version": "1.0",
        "posting_id": "fixture-123",
        "source": {
            "name": "FixtureSource",
            "url": "https://example.com/jobs/fixture-123",
            "retrieved_at": timestamp,
        },
        "job": {
            "title": "Junior AI Engineer",
            "company": "Example Technologies",
            "locations": ["India"],
            "work_mode": "unknown",
            "employment_type": "full_time",
            "description": "Build Python APIs.\nUse machine learning carefully.",
            "skills": ["Python"],
            "experience_min_years": None,
            "experience_max_years": None,
            "posted_at": None,
            "deadline": None,
            "apply_url": "https://example.com/apply/fixture-123",
        },
        "record": {
            "first_seen_at": timestamp,
            "last_seen_at": timestamp,
            "status": "open",
            "content_hash": "a" * 64,
        },
    }


class JobSearchCliTests(unittest.TestCase):
    def test_handoff_requires_shortlist(self) -> None:
        state = workflow.empty_state()
        workflow.upsert_posting(state, posting())
        with tempfile.TemporaryDirectory() as temp:
            state_path = Path(temp) / "jobs.json"
            workflow.save_state(state_path, state)
            args = Namespace(posting_id="fixture-123", state=state_path, mode="mnc", run_name="test-handoff")
            with patch.object(job_search, "REPO_ROOT", Path(temp)):
                with self.assertRaisesRegex(ValueError, "Only a shortlisted opportunity"):
                    job_search.cmd_handoff(args)

    def test_handoff_creates_standard_input_and_does_not_submit(self) -> None:
        state = workflow.empty_state()
        workflow.upsert_posting(state, posting())
        state["opportunities"]["fixture-123"] = {
            "posting_ids": ["fixture-123"],
            "decision": "Shortlisted",
        }
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            state_path = root / "state" / "jobs.json"
            workflow.save_state(state_path, state)
            args = Namespace(posting_id="fixture-123", state=state_path, mode="mnc", run_name="test-handoff")
            with patch.object(job_search, "REPO_ROOT", root):
                result = job_search.cmd_handoff(args)
            input_path = root / "applications" / "test-handoff" / "input.md"
            self.assertTrue(input_path.is_file())
            content = input_path.read_text(encoding="utf-8")
            self.assertIn("company: Example Technologies", content)
            self.assertIn("mode: mnc", content)
            self.assertIn("role: Junior AI Engineer", content)
            self.assertIn("jd_url: https://example.com/jobs/fixture-123", content)
            self.assertIn("Build Python APIs.", content)
            self.assertFalse(result["automatic_submission"])
            saved = workflow.load_state(state_path)
            self.assertEqual(saved["applications"]["fixture-123"]["status"], "Preparing")

    def test_handoff_refuses_to_overwrite_existing_run_directory(self) -> None:
        state = workflow.empty_state()
        workflow.upsert_posting(state, posting())
        state["opportunities"]["fixture-123"] = {
            "posting_ids": ["fixture-123"],
            "decision": "Shortlisted",
        }
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            run_dir = root / "applications" / "test-handoff"
            run_dir.mkdir(parents=True)
            existing = run_dir / "keep.txt"
            existing.write_text("preserve", encoding="utf-8")
            state_path = root / "state" / "jobs.json"
            workflow.save_state(state_path, state)
            args = Namespace(posting_id="fixture-123", state=state_path, mode="mnc", run_name="test-handoff")
            with patch.object(job_search, "REPO_ROOT", root):
                with self.assertRaisesRegex(ValueError, "already exists and was not overwritten"):
                    job_search.cmd_handoff(args)
            self.assertEqual(existing.read_text(encoding="utf-8"), "preserve")

    def test_application_status_cannot_move_backwards(self) -> None:
        state = workflow.empty_state()
        workflow.upsert_posting(state, posting())
        state["opportunities"]["fixture-123"] = {
            "posting_ids": ["fixture-123"],
            "decision": "Shortlisted",
        }
        state["applications"]["fixture-123"] = {
            "posting_id": "fixture-123",
            "status": "Interview",
            "notes": "Panel scheduled",
        }
        with tempfile.TemporaryDirectory() as temp:
            state_path = Path(temp) / "jobs.json"
            workflow.save_state(state_path, state)
            args = Namespace(posting_id="fixture-123", state=state_path, status="Applied", notes=None)
            with self.assertRaisesRegex(ValueError, "Invalid application status transition"):
                job_search.cmd_application(args)


    def test_untrusted_multiline_title_and_company_cannot_inject_input_fields(self) -> None:
        item = posting()
        item["job"]["company"] = "Example Technologies\nmode: startup"
        item["job"]["title"] = "Junior AI Engineer\ncompany: Different Company"
        state = workflow.empty_state()
        workflow.upsert_posting(state, item)
        state["opportunities"]["fixture-123"] = {
            "posting_ids": ["fixture-123"],
            "decision": "Shortlisted",
        }
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            state_path = root / "state" / "jobs.json"
            workflow.save_state(state_path, state)
            args = Namespace(posting_id="fixture-123", state=state_path, mode="mnc", run_name="safe-input")
            with patch.object(job_search, "REPO_ROOT", root):
                job_search.cmd_handoff(args)
            generated = (root / "applications" / "safe-input" / "input.md").read_text(encoding="utf-8")
            self.assertEqual(generated.count("mode:"), 1)
            self.assertEqual(generated.count("company:"), 1)
            self.assertIn("company: Example Technologies mode: startup", generated)
            self.assertIn("role: Junior AI Engineer company: Different Company", generated)


    def test_list_filters_preserve_unknown_values_as_unknown(self) -> None:
        state = workflow.empty_state()
        unknown = posting()
        unknown["job"]["work_mode"] = "unknown"
        unknown["job"]["experience_min_years"] = None
        workflow.upsert_posting(state, unknown)
        known_high_requirement = posting()
        known_high_requirement["posting_id"] = "fixture-456"
        known_high_requirement["source"]["url"] = "https://example.com/jobs/fixture-456"
        known_high_requirement["job"]["title"] = "Junior AI Engineer II"
        known_high_requirement["job"]["work_mode"] = "remote"
        known_high_requirement["job"]["locations"] = ["India"]
        known_high_requirement["job"]["experience_min_years"] = 4
        known_high_requirement["job"]["apply_url"] = "https://example.com/apply/fixture-456"
        workflow.upsert_posting(state, known_high_requirement)
        with tempfile.TemporaryDirectory() as temp:
            state_path = Path(temp) / "jobs.json"
            workflow.save_state(state_path, state)
            args = Namespace(
                state=state_path,
                role="AI",
                location="Ind",
                work_mode="remote",
                employment_type=None,
                max_experience=2,
            )
            result = job_search.cmd_list(args)
        self.assertEqual(result["count"], 1)
        self.assertEqual(result["postings"][0]["posting_id"], "fixture-123")
        self.assertEqual(result["postings"][0]["filter_status"], "Unknown")
        self.assertIn("work_mode", result["postings"][0]["filter_notes"])
        self.assertIn("experience_min_years", result["postings"][0]["filter_notes"])


if __name__ == "__main__":
    unittest.main()
