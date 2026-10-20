#!/usr/bin/env python3
"""Regression tests for fact-based metric validation."""
from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).with_name("check_metrics.py")
SPEC = importlib.util.spec_from_file_location("check_metrics", SCRIPT)
assert SPEC and SPEC.loader
check_metrics = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(check_metrics)


class MetricValidationTests(unittest.TestCase):
    def facts(self, folder: str, content: str) -> Path:
        path = Path(folder) / "facts.yaml"
        path.write_text(content, encoding="utf-8")
        return path

    def test_verified_metric_with_basis_is_allowed(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            facts = self.facts(temp, '''
experience:
  - id: sample
    metrics:
      resolution_rate:
        value: "90% of routine cases resolved"
        status: verified
        basis: "Reviewed ticket records for the stated period."
''')
            self.assertEqual(check_metrics.allowed_metric_tokens(facts), {"90%"})

    def test_candidate_estimate_needs_basis_and_qualified_use(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            facts = self.facts(temp, '''
experience:
  - id: sample
    metrics:
      resolution_rate:
        value: "approximately 90%"
        status: candidate_estimate
        basis: "Candidate estimate from a defined sample of routine cases."
        resume_use: "May be included only as an approximate estimate."
''')
            self.assertEqual(check_metrics.allowed_metric_tokens(facts), {"90%"})

    def test_candidate_estimate_marked_hold_is_not_allowed(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            facts = self.facts(temp, '''
experience:
  - id: support
    metrics:
      resolution_rate:
        value: "approximately 90%"
        status: candidate_estimate
        basis: "Candidate estimate; no sample count available."
        resume_use: "Hold until the candidate can explain the basis and scope."
''')
            self.assertNotIn("90%", check_metrics.allowed_metric_tokens(facts))

    def test_estimate_without_basis_or_qualified_use_is_not_allowed(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            facts = self.facts(temp, '''
experience:
  - id: support
    metrics:
      resolution_rate:
        value: "90%"
        status: candidate_estimate
        basis: ""
        resume_use: "Use as a precise result."
''')
            self.assertEqual(check_metrics.allowed_metric_tokens(facts), set())

    def test_missing_status_or_basis_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            facts = self.facts(temp, '''
project:
  metrics:
    speedup:
      value: "3x faster"
      basis: "An informal observation without a recorded comparison."
''')
            self.assertEqual(check_metrics.allowed_metric_tokens(facts), set())

    def test_restricted_metric_wins_even_if_same_token_appears_elsewhere(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            facts = self.facts(temp, '''
experience:
  - id: example
    metrics:
      performance_change:
        value: "40% improvement"
        status: verified
        basis: "Synthetic fixture baseline."
    constraints:
      - "50% improvement claim remains unverified"
    attribution_limits:
      - "Do not claim 40% improvement"
''')
            tokens = check_metrics.allowed_metric_tokens(facts)
            self.assertNotIn("40%", tokens)
            self.assertNotIn("50%", tokens)

    def test_explicitly_unverified_metric_record_is_blocked(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            facts = self.facts(temp, '''
experience:
  - id: example
    metrics:
      latency_change:
        value: "40% improvement"
        status: unverified
        basis: "No independent measurement is available."
''')
            self.assertNotIn("40%", check_metrics.allowed_metric_tokens(facts))

    def test_percentage_in_unrelated_candidate_prose_is_not_metric_authority(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            facts = self.facts(temp, '''
credentials:
  learning:
    progress_note: "about 60% complete as recorded in Notion"
''')
            self.assertEqual(check_metrics.allowed_metric_tokens(facts), set())

    def test_dates_counts_and_versions_are_not_metric_tokens(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            facts = self.facts(temp, '''
education:
  dates: "2024-2025"
project:
  version: "v3"
open_source:
  summary:
    issues_authored: 22
    tests_reported: 52
''')
            self.assertEqual(check_metrics.allowed_metric_tokens(facts), set())

    def test_numbers_in_basis_do_not_authorize_other_metric_claims(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            facts = self.facts(temp, '''
project:
  metrics:
    success_rate:
      value: "90% on the named evaluation set"
      status: verified
      basis: "Compared against a prior 40% threshold that is not a measured result."
''')
            self.assertEqual(check_metrics.allowed_metric_tokens(facts), {"90%"})

    def test_multiplier_in_candidate_metric_is_allowed_with_basis(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            facts = self.facts(temp, '''
project:
  metrics:
    throughput:
      value: "3x faster"
      status: verified
      basis: "Measured against the named baseline in a repeatable benchmark."
''')
            self.assertEqual(check_metrics.allowed_metric_tokens(facts), {"3x"})

    def test_invalid_yaml_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            facts = self.facts(temp, "experience: [not closed")
            with self.assertRaises(ValueError):
                check_metrics.allowed_metric_tokens(facts)


if __name__ == "__main__":
    unittest.main()
