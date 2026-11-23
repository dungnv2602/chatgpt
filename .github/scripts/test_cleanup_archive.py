#!/usr/bin/env python3
"""Focused tests for indexed archive retention. Uses temporary files only."""

from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path

SCRIPT = Path(__file__).with_name("cleanup-archive.py")
SPEC = importlib.util.spec_from_file_location("cleanup_archive", SCRIPT)
assert SPEC is not None and SPEC.loader is not None
cleanup_archive = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(cleanup_archive)


class ArchiveRetentionTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.index = self.root / ".github" / "archive-retention-index.json"
        self.index.parent.mkdir(parents=True)
        self.archive = self.root / "archive" / "tasks"
        self.archive.mkdir(parents=True)

    def tearDown(self) -> None:
        self.temp.cleanup()

    def write_index(self, records: list[dict[str, str]]) -> None:
        self.index.write_text(
            json.dumps({
                "schema_version": 1,
                "unindexed_records": "preserve",
                "records": records,
            }),
            encoding="utf-8",
        )

    def test_empty_index_does_not_access_archive(self) -> None:
        self.archive.rmdir()
        self.write_index([])
        deleted, changed = cleanup_archive.clean_due_records(
            self.index, self.root, datetime(2027, 1, 1, tzinfo=timezone.utc)
        )
        self.assertEqual(deleted, [])
        self.assertFalse(changed)
        self.assertFalse(self.archive.exists())

    def test_unindexed_legacy_file_is_preserved(self) -> None:
        legacy = self.archive / "legacy-record.md"
        legacy.write_text("legacy", encoding="utf-8")
        self.write_index([])
        deleted, changed = cleanup_archive.clean_due_records(
            self.index, self.root, datetime(2027, 1, 1, tzinfo=timezone.utc)
        )
        self.assertEqual(deleted, [])
        self.assertFalse(changed)
        self.assertTrue(legacy.exists())

    def test_only_due_indexed_file_is_deleted(self) -> None:
        due = self.archive / "due-record.md"
        later = self.archive / "later-record.md"
        legacy = self.archive / "unindexed-record.md"
        for item in (due, later, legacy):
            item.write_text(item.name, encoding="utf-8")

        self.write_index([
            {"path": "archive/tasks/due-record.md", "archived_at": "2026-01-01T00:00:00Z"},
            {"path": "archive/tasks/later-record.md", "archived_at": "2026-12-01T00:00:00Z"},
        ])
        deleted, changed = cleanup_archive.clean_due_records(
            self.index, self.root, datetime(2026, 4, 1, tzinfo=timezone.utc)
        )
        self.assertEqual(deleted, ["archive/tasks/due-record.md"])
        self.assertTrue(changed)
        self.assertFalse(due.exists())
        self.assertTrue(later.exists())
        self.assertTrue(legacy.exists())
        updated = json.loads(self.index.read_text(encoding="utf-8"))
        self.assertEqual(
            updated["records"],
            [{"path": "archive/tasks/later-record.md", "archived_at": "2026-12-01T00:00:00Z"}],
        )

    def test_missing_due_path_is_pruned_without_directory_scan(self) -> None:
        self.write_index([
            {"path": "archive/tasks/already-absent.md", "archived_at": "2026-01-01T00:00:00Z"},
        ])
        deleted, changed = cleanup_archive.clean_due_records(
            self.index, self.root, datetime(2026, 4, 1, tzinfo=timezone.utc)
        )
        self.assertEqual(deleted, [])
        self.assertTrue(changed)
        updated = json.loads(self.index.read_text(encoding="utf-8"))
        self.assertEqual(updated["records"], [])

    def test_non_schedule_event_is_rejected(self) -> None:
        with self.assertRaises(RuntimeError):
            cleanup_archive.require_scheduled_event("workflow_dispatch", "true")
        with self.assertRaises(RuntimeError):
            cleanup_archive.require_scheduled_event("schedule", "false")
        cleanup_archive.require_scheduled_event("schedule", "true")

    def test_unsafe_path_is_rejected(self) -> None:
        self.write_index([
            {"path": "archive/tasks/../../outside.md", "archived_at": "2026-01-01T00:00:00Z"},
        ])
        with self.assertRaises(ValueError):
            cleanup_archive.clean_due_records(
                self.index, self.root, datetime(2026, 4, 1, tzinfo=timezone.utc)
            )


if __name__ == "__main__":
    unittest.main(verbosity=2)
