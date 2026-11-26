#!/usr/bin/env python3
"""Regression tests for Markdown links that contain runtime placeholders."""
import importlib.util
import unittest
from pathlib import Path

SCRIPT = Path(__file__).with_name("check_markdown_anchors.py")
SPEC = importlib.util.spec_from_file_location("check_markdown_anchors", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class MarkdownAnchorTests(unittest.TestCase):
    def test_runtime_template_values_are_not_local_paths(self):
        targets = (
            "{run_url}",
            "$" + "{{ github.server_url }}/owner/repo/actions/runs/1",
            "https://example.invalid/{run_id}",
        )
        for target in targets:
            self.assertIsNone(
                MODULE.resolve_markdown_target(
                    "skills/example.md", target, {"docs/guide.md"}, {"docs/guide.md"}
                ),
                target,
            )

    def test_literal_local_targets_are_still_resolved(self):
        self.assertEqual(
            MODULE.resolve_markdown_target(
                "skills/example.md",
                "../docs/guide.md#setup",
                {"docs/guide.md"},
                {"docs/guide.md"},
            ),
            "docs/guide.md",
        )

    def test_missing_literal_local_targets_remain_visible(self):
        self.assertEqual(
            MODULE.resolve_markdown_target(
                "skills/example.md",
                "../docs/missing.md",
                {"docs/guide.md"},
                {"docs/guide.md"},
            ),
            "docs/missing.md",
        )

    def test_heading_slug_preserves_underscores_inside_code_spans(self):
        anchors = MODULE.heading_anchors("### Step D: Log Every Test Run & Self-Healing Fix (`test_heal` Bucket)")
        self.assertIn("step-d-log-every-test-run--self-healing-fix-test_heal-bucket", anchors)

    def test_heading_slug_retains_plus_signs(self):
        anchors = MODULE.heading_anchors("## Template H — ReAct + Stop Conditions")
        self.assertIn("template-h--react-+-stop-conditions", anchors)


if __name__ == "__main__":
    unittest.main()
