#!/usr/bin/env python3
"""Tests for exact-path, 90-day individual archive retention."""
from __future__ import annotations
import importlib.util, json, tempfile, unittest
from datetime import datetime, timezone
from pathlib import Path
SCRIPT=Path(__file__).with_name("cleanup-archive.py")
SPEC=importlib.util.spec_from_file_location("cleanup_archive",SCRIPT)
assert SPEC and SPEC.loader
cleanup=importlib.util.module_from_spec(SPEC); SPEC.loader.exec_module(cleanup)

class ArchiveRetentionTests(unittest.TestCase):
 def setUp(self):
  self.temp=tempfile.TemporaryDirectory(); self.root=Path(self.temp.name)
  self.index=self.root/".github"/"archive-retention-index.json"; self.index.parent.mkdir(parents=True)
  (self.root/".archive"/"task").mkdir(parents=True)
  (self.root/".archive"/"reports"/"lint_reports"/"run-1").mkdir(parents=True)
 def tearDown(self): self.temp.cleanup()
 def write(self,records):
  self.index.write_text(json.dumps({"schema_version":1,"unindexed_records":"preserve","records":records}),encoding="utf-8")
 def rec(self,path,stamp): return {"path":path,"archived_at_utc":stamp}
 def run_clean(self): return cleanup.clean_due_records(self.index,self.root,datetime(2026,4,1,tzinfo=timezone.utc))
 def test_empty_index_does_not_scan_archive(self):
  (self.root/".archive"/"task").rmdir(); self.write([])
  deleted,changed=self.run_clean(); self.assertEqual(deleted,[]); self.assertFalse(changed)
  self.assertFalse((self.root/".archive"/"task").exists())
 def test_unindexed_files_are_preserved(self):
  p=self.root/".archive"/"reports"/"lint_reports"/"run-1"/"legacy.md"; p.write_text("legacy")
  self.write([]); deleted,changed=self.run_clean()
  self.assertEqual(deleted,[]); self.assertFalse(changed); self.assertTrue(p.exists())
 def test_only_individually_due_task_and_report_files_are_deleted(self):
  task=self.root/".archive"/"task"/"due.md"
  report=self.root/".archive"/"reports"/"lint_reports"/"run-1"/"report.md"
  later=self.root/".archive"/"reports"/"lint_reports"/"run-1"/"later.json"
  legacy=self.root/".archive"/"reports"/"lint_reports"/"run-1"/"legacy.log"
  for p in (task,report,later,legacy): p.write_text(p.name)
  self.write([self.rec(".archive/task/due.md","2026-01-01T00:00:00Z"),self.rec(".archive/reports/lint_reports/run-1/report.md","2026-01-01T00:00:00Z"),self.rec(".archive/reports/lint_reports/run-1/later.json","2026-12-01T00:00:00Z")])
  deleted,changed=self.run_clean()
  self.assertEqual(set(deleted),{".archive/task/due.md",".archive/reports/lint_reports/run-1/report.md"})
  self.assertTrue(changed); self.assertFalse(task.exists()); self.assertFalse(report.exists())
  self.assertTrue(later.exists()); self.assertTrue(legacy.exists())
  self.assertEqual(len(json.loads(self.index.read_text())["records"]),1)
 def test_missing_expired_file_prunes_index_entry(self):
  self.write([self.rec(".archive/reports/absent.json","2026-01-01T00:00:00Z")])
  deleted,changed=self.run_clean(); self.assertEqual(deleted,[]); self.assertTrue(changed)
  self.assertEqual(json.loads(self.index.read_text())["records"],[])

 def test_symlinked_parent_directory_is_rejected(self):
  link=self.root/".archive"/"reports"/"linked"
  outside=self.root/"outside"; outside.mkdir()
  link.symlink_to(outside,target_is_directory=True)
  target=outside/"report.md"; target.write_text("protected")
  self.write([self.rec(".archive/reports/linked/report.md","2026-01-01T00:00:00Z")])
  with self.assertRaises(ValueError): self.run_clean()
  self.assertTrue(target.exists())
 def test_schedule_only(self):
  with self.assertRaises(RuntimeError): cleanup.require_scheduled_event("workflow_dispatch","true")
  with self.assertRaises(RuntimeError): cleanup.require_scheduled_event("schedule","false")
  cleanup.require_scheduled_event("schedule","true")
 def test_unsafe_paths_rejected(self):
  for p in ("..archive/reports/../../outside.md",".archive/task/../.archive/reports/x.md",".archive/reports/x.md","..archive/reports/.gitkeep",".archive/task/"):
   self.write([self.rec(p,"2026-01-01T00:00:00Z")])
   with self.assertRaises(ValueError): self.run_clean()

if __name__=="__main__": unittest.main(verbosity=2)
