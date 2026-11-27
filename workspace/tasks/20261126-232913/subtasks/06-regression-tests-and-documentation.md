# Subtask: Regression coverage and documentation/catalog alignment

**Template version:** 1.0

## Metadata
- **ID:** 20261126-232913-06
- **Parent Task ID:** 20261126-232913
- **Type:** Implementation
- **Status:** In Progress
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
In Progress. Regression and documentation changes are committed and read back. Final ADR confirmation mapping and task closeout remain.

## 7. Evidence
- **Commit SHA:** Multiple remote commits. Key commits include `79cda7d`, `7632ed1`, `5e7d051`, `6a443e7`, `13132e7`, `0763c16`, and the documentation commits recorded in history.
- **Changed paths:** Ledger and archive regression suites, Ledger archive reader, cleanup script, CI Ledger/Worker/GitHub Actions skills, workspace and triage READMEs, archive README, task board, Document Type Catalog, parent/subtask records, and discussion register.
- **Read-back:** Every changed file was read back after its update. Task and subtask templates were checked and already satisfy ADR-0004.
- **Other evidence:** No local tests or scripts were executed. Hosted results remain unreviewed by explicit instruction.

## 8. Completion Record
- **Status:** Ready
- **Completed at:** Not applicable
- **Completion basis:** Not Done.
- **Evidence:** Not applicable.

## 10. Handoff
Follow the parent subtask index. Record exact commits and read-back evidence. Do not mark Done until all acceptance criteria pass.
