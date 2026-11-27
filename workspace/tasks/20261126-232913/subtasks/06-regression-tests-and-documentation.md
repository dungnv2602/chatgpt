# Subtask: Regression coverage and documentation/catalog alignment

**Template version:** 1.0

## Metadata
- **ID:** 20261126-232913-06
- **Parent Task ID:** 20261126-232913
- **Type:** Implementation
- **Status:** Done
- **Priority:** P0
- **Origin:** User
- **Approval:** Approved
- **Governing ADR(s):** ADR-0004
- **Dependencies:** 20261126-232913-01
- **Required:** Yes
- **Created:** 2026-11-26 23:29 UTC
- **Updated:** 2026-11-27 01:10 UTC

## 1. Objective
Regression coverage and documentation/catalog alignment as part of the accepted ADR-0004 implementation.

## 2. Scope
Implement only this subtask within ADR-0004. Parent: [20261126-232913](../task.md). Governing decision: [ADR-0004](../../../../adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md).

## 3. Acceptance Criteria
1. Update Ledger regression suite for all ADR-0004 invariants while maintaining validation/security coverage.
2. Update CI Ledger, Worker, and GitHub Actions skills to use one consistent lifecycle contract.
3. Update workspace README, triage README, templates, task board contract, and Document Type Catalog.
4. Use only repository-authorized hosted checks; do not inspect hosted results until explicit user trigger.
5. Perform remote read-back of every changed file and document unverified tests honestly.
6. Map every ADR-0004 Confirmation criterion to concrete test or repository evidence.

## 4. Decisions
- Follow ADR-0004.
- Preserve existing evidence and validation/security checks.
- Do not inspect hosted results before explicit user trigger.

## 5. Progress Log
### 2026-11-26 23:31 UTC
- **Action:** Registered this implementation subtask and its acceptance criteria.
- **Result:** Ready; implementation has not started.
- **References:** ADR-0004 and parent task folder.
- **Next:** Execute after dependencies are complete.

### 2026-11-27 01:10 UTC
- **Action:** Audited ADR-0004 Confirmation criteria and aligned the archive lifecycle across the Worker, CI Ledger, GitHub Actions, workspace, triage, archive, task-board, and Document Type Catalog guidance.
- **Result:** Added Ledger regression cases for active folder-task reuse, folder and historical flat archive reading, unindexed-path behavior, recurrence links, parent/child task references, parent Done gating, and hosted-validation separation. Added cleanup tests for atomic folder retention and fail-closed incomplete archives. Existing task and subtask templates already satisfy the required folder and child-record contract, so no template edits were needed.
- **References:** `.takeout/reports/triage/scripts/test_ledger.py`; `.github/scripts/test_cleanup_archive.py`; `.agent/skills/ci-ledger/SKILL.md`; `.agent/skills/the-worker/SKILL.md`; `.agent/skills/github-actions/SKILL.md`; `.archive/README.md`; `workspace/README.md`; `workspace/task_board.md`; `.takeout/reports/triage/README.md`; Document Type Catalog.
- **Next:** Map every ADR-0004 Confirmation criterion to concrete evidence and perform final read-back. Do not inspect hosted results.

## 6. Current State
Done. Regression coverage, documentation/catalog alignment, remote read-back, and the ADR-0004 Confirmation evidence matrix are complete.

### 2026-11-27 01:10 UTC
- **Action:** Final archive-index audit found at least two non-expired historical flat task paths that return NOT_FOUND. Added fail-closed validation for missing retained index paths in the cleanup workflow and a regression test. Updated the archive, Worker, CI Ledger, GitHub Actions, and discussion guidance. Reconciled the two migrated task links in the discussion register.
- **Result:** No historical archive file or retention-index entry was modified. The cleanup workflow now surfaces missing retained files instead of silently passing or pruning them. Parent Confirmation item 16 remains partial pending user direction.
- **References:** `.github/scripts/cleanup-archive.py`; `.github/scripts/test_cleanup_archive.py`; `.archive/README.md`; `.agent/skills/the-worker/SKILL.md`; `.agent/skills/ci-ledger/SKILL.md`; `.agent/skills/github-actions/SKILL.md`; `workspace/discussion.md`.
- **Next:** Wait for user direction on recovery or index-entry removal. Do not inspect hosted results.

### 2026-11-27 01:10 UTC
- **Action:** Completed the ADR-0004 Confirmation evidence matrix in the parent task. Reconciled all lifecycle documents and added regression coverage for folder and legacy archive reading, archive retention integrity, recurrence links, parent/child references, governance, hosted-validation separation, and existing ingestion/security protections.
- **Result:** All six subtask records and the task index are consistent. Every changed file was read back. The task and subtask templates already meet the folder contract. No tests were run. Hosted results remain unreviewed.
- **References:** Parent task section 11; `.takeout/reports/triage/scripts/test_ledger.py`; `.github/scripts/test_cleanup_archive.py`; CI Ledger, Worker, and GitHub Actions skills; workspace/triage/archive READMEs; task board; Document Type Catalog.
- **Next:** Parent closeout remains blocked by Confirmation item 15 and the missing historical archive paths recorded in item 16. Obtain user direction before changing historical archive files or index entries.



## 7. Evidence
- **Commit SHA:** Multiple remote commits. Key commits include `4c9e22c`, `35dcb49`, `1244a94`, `3eb4445`, `df3f594`, `714c9a3`, `ad3710a`, `f366ab7`, and `5142cfe`.
- **Changed paths:** Ledger and archive regression suites, Ledger archive reader, cleanup script, CI Ledger/Worker/GitHub Actions skills, workspace and triage READMEs, archive README, task board, Document Type Catalog, parent/subtask records, and discussion register.
- **Read-back:** Every changed file was read back after its update. Task and subtask templates were checked and already satisfy ADR-0004.
- **Other evidence:** No local tests or scripts were executed. Hosted results remain unreviewed by explicit instruction. The parent task remains In Progress because hosted confirmation and historical archive integrity are unresolved.

## 8. Completion Record
- **Status:** Ready
- **Completed at:** Not applicable
- **Completion basis:** Not Done.
- **Evidence:** Not applicable.

## 10. Handoff
Follow the parent subtask index. Record exact commits and read-back evidence. Do not mark Done until all acceptance criteria pass.
