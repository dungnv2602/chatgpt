#!/usr/bin/env python3
"""Tests for exact-path, 90-day task-folder and individual archive retention."""
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
  (self.root/"workspace/archive"/"task").mkdir(parents=True)
  (self.root/"workspace/archive"/"reports"/"lint_reports"/"run-1").mkdir(parents=True)
 def tearDown(self): self.temp.cleanup()
 def write(self,records):
  self.index.write_text(json.dumps({"schema_version":1,"unindexed_records":"preserve","records":records}),encoding="utf-8")
 def rec(self,path,stamp): return {"path":path,"archived_at_utc":stamp}
 def run_clean(self): return cleanup.clean_due_records(self.index,self.root,datetime(2026,4,1,tzinfo=timezone.utc))
 def test_empty_index_does_not_scan_archive(self):
  (self.root/"workspace/archive"/"task").rmdir(); self.write([])
  deleted,changed=self.run_clean(); self.assertEqual(deleted,[]); self.assertFalse(changed)
  self.assertFalse((self.root/"workspace/archive"/"task").exists())
 def test_unindexed_files_are_preserved(self):
  p=self.root/"workspace/archive"/"reports"/"lint_reports"/"run-1"/"legacy.md"; p.write_text("legacy")
  self.write([]); deleted,changed=self.run_clean()
  self.assertEqual(deleted,[]); self.assertFalse(changed); self.assertTrue(p.exists())
 def test_task_folder_archive_expires_as_one_unit_and_legacy_files_remain_individual(self):
  legacy_task=self.root/"workspace/archive"/"task"/"due-legacy.md"
  due_folder=self.root/"workspace/archive"/"task"/"20261127-010000"
  later_folder=self.root/"workspace/archive"/"task"/"20261127-020000"
  report=self.root/"workspace/archive"/"reports"/"lint_reports"/"run-1"/"report.md"
  later_report=self.root/"workspace/archive"/"reports"/"lint_reports"/"run-1"/"later.json"
  legacy_report=self.root/"workspace/archive"/"reports"/"lint_reports"/"run-1"/"legacy.log"
  due_paths=[due_folder/"task.md",due_folder/"subtasks"/"README.md",due_folder/"subtasks"/"01-main-work.md"]
  later_paths=[later_folder/"task.md",later_folder/"subtasks"/"README.md",later_folder/"subtasks"/"01-main-work.md"]
  for folder,paths in ((due_folder,due_paths),(later_folder,later_paths)):
   (folder/"subtasks").mkdir(parents=True)
   for item in paths: item.write_text(item.name)
  for item in (legacy_task,report,later_report,legacy_report): item.write_text(item.name)
  due_stamp="2026-01-01T00:00:00Z"
  later_stamp="2026-02-01T00:00:00Z"
  records=[self.rec("workspace/archive/task/due-legacy.md",due_stamp)]
  records.extend(self.rec(item.relative_to(self.root).as_posix(),due_stamp) for item in due_paths)
  records.extend(self.rec(item.relative_to(self.root).as_posix(),later_stamp) for item in later_paths)
  records.extend([
   self.rec("workspace/archive/reports/lint_reports/run-1/report.md",due_stamp),
   self.rec("workspace/archive/reports/lint_reports/run-1/later.json",later_stamp)
  ])
  self.write(records)
  deleted,changed=self.run_clean()
  expected={"workspace/archive/task/due-legacy.md",*(item.relative_to(self.root).as_posix() for item in due_paths),"workspace/archive/reports/lint_reports/run-1/report.md"}
  self.assertEqual(set(deleted),expected)
  self.assertTrue(changed)
  self.assertFalse(legacy_task.exists())
  self.assertTrue(all(not item.exists() for item in due_paths))
  self.assertTrue(all(item.exists() for item in later_paths))
  self.assertTrue(later_report.exists())
  self.assertTrue(legacy_report.exists())
  self.assertEqual(
   {item["path"] for item in json.loads(self.index.read_text())["records"]},
   {*(item.relative_to(self.root).as_posix() for item in later_paths),"workspace/archive/reports/lint_reports/run-1/later.json"}
  )

 def test_task_folder_archive_requires_parent_and_subtask_index_entries(self):
  folder=self.root/"workspace/archive"/"task"/"incomplete"
  (folder/"subtasks").mkdir(parents=True)
  (folder/"task.md").write_text("parent")
  self.write([self.rec("workspace/archive/task/incomplete/task.md","2026-01-01T00:00:00Z")])
  with self.assertRaisesRegex(ValueError,"index is incomplete"):
   self.run_clean()

 def test_task_folder_archive_requires_one_timestamp(self):
  folder=self.root/"workspace/archive"/"task"/"mixed"
  (folder/"subtasks").mkdir(parents=True)
  (folder/"task.md").write_text("parent")
  (folder/"subtasks"/"README.md").write_text("index")
  self.write([
   self.rec("workspace/archive/task/mixed/task.md","2026-01-01T00:00:00Z"),
   self.rec("workspace/archive/task/mixed/subtasks/README.md","2026-01-02T00:00:00Z")
  ])
  with self.assertRaisesRegex(ValueError,"must share one archived_at_utc timestamp"):
   self.run_clean()

 def test_missing_task_folder_file_fails_closed(self):
  folder=self.root/"workspace/archive"/"task"/"missing-child"
  (folder/"subtasks").mkdir(parents=True)
  parent=folder/"task.md"
  index=folder/"subtasks"/"README.md"
  parent.write_text("parent")
  index.write_text("index")
  stamp="2026-01-01T00:00:00Z"
  self.write([
   self.rec("workspace/archive/task/missing-child/task.md",stamp),
   self.rec("workspace/archive/task/missing-child/subtasks/README.md",stamp),
   self.rec("workspace/archive/task/missing-child/subtasks/01-missing.md",stamp)
  ])
  with self.assertRaisesRegex(ValueError,"Task-folder archive file is missing"):
   self.run_clean()
  self.assertTrue(parent.exists())
  self.assertTrue(index.exists())
  self.assertEqual(len(json.loads(self.index.read_text())["records"]),3)

 def test_missing_nonexpired_indexed_file_fails_closed(self):
  missing=self.root/"workspace/archive"/"task"/"20261122-070000-missing.md"
  stamp="2026-02-01T00:00:00Z"
  self.write([self.rec("workspace/archive/task/20261122-070000-missing.md",stamp)])
  with self.assertRaisesRegex(ValueError,"missing before retention expiry"):
   self.run_clean()
  self.assertEqual(len(json.loads(self.index.read_text())["records"]),1)

 def test_missing_expired_file_prunes_index_entry(self):
  self.write([self.rec("workspace/archive/reports/absent.json","2026-01-01T00:00:00Z")])
  deleted,changed=self.run_clean(); self.assertEqual(deleted,[]); self.assertTrue(changed)
  self.assertEqual(json.loads(self.index.read_text())["records"],[])

 def test_symlinked_parent_directory_is_rejected(self):
  link=self.root/"workspace/archive"/"reports"/"linked"
  outside=self.root/"outside"; outside.mkdir()
  link.symlink_to(outside,target_is_directory=True)
  target=outside/"report.md"; target.write_text("protected")
  self.write([self.rec("workspace/archive/reports/linked/report.md","2026-01-01T00:00:00Z")])
  with self.assertRaises(ValueError): self.run_clean()
  self.assertTrue(target.exists())
 def test_schedule_only(self):
  with self.assertRaises(RuntimeError): cleanup.require_scheduled_event("workflow_dispatch","true")
  with self.assertRaises(RuntimeError): cleanup.require_scheduled_event("schedule","false")
  cleanup.require_scheduled_event("schedule","true")
 def test_unsafe_paths_rejected(self):
  for p in ("workspace/archive/reports/../../outside.md","workspace/archive/task/../workspace/archive/reports/x.md","workspace/archive/reports/.gitkeep","workspace/archive/task/","workspace/archive/task/20261127-010000","workspace/archive/task/20261127-010000/subtasks"):
   self.write([self.rec(p,"2026-01-01T00:00:00Z")])
   with self.assertRaises(ValueError): self.run_clean()

if __name__=="__main__": unittest.main(verbosity=2)
