# Task: Implement ADR-0004 task folders and CI Ledger lifecycle

## Metadata
- **Template version:** 2.0
- **ID:** 20261126-232913
- **Created:** 2026-11-26 23:29 UTC
- **Updated:** 2026-11-27 05:31 UTC
- **Priority:** P0
- **Status:** In Progress
- **Origin:** User
- **Approval:** Approved
- **Governing ADR(s):** [ADR-0004](../../adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md)
- **Current execution:** Yes
- **Dependencies:** None
- **Related tasks:** 20261126-142500; 20261126-090154
- **Ledger group:** None — implementation of accepted architecture
- **Archived:** No

## 1. Original Request
"Approve, execute. Identify the gaps in CI ledger and fix them if any, if it's not working properly then this entire workflow is broken."

Related user direction: "Then make a task a folder instead of a note. Every task should have its subtasks. CI task is one of those subtasks. This makes the definition of done of a CI task different from a regular task."

The user selected commit-based CI remediation completion (Option 1 in the preceding clarification), approved DRAFT-0005 revision 1, and explicitly instructed execution.

## 2. Subsequent Instructions
- **2026-11-27:** User approved DRAFT-0005 revision 1 and its complete scope; promoted to accepted ADR-0004.
- **2026-11-27:** User instructed execution and specifically required identifying and repairing CI Ledger reliability gaps.
- **Standing boundary:** Do not inspect hosted CI results, poll, dispatch, or rerun workflows until the user explicitly triggers results review.
- **Repository boundary:** Repository `dungnv2602/chatgpt`, branch `gpt`, is the sole source of truth. Use remote GitHub operations; do not run repository scripts locally.
- **Decision boundary:** Implement only ADR-0004. Do not implement DRAFT-0003's broader Area/Project architecture or rewrite ADR-0003.
- **Safety:** Do not weaken checks, delete historical archives, or reset Ledger/report data.

## 3. Objective
Implement accepted ADR-0004 completely and restore reliable CI Ledger operation. Convert active tasks to folders with nested subtasks; make CI remediation completion commit-based with hosted validation separate; preserve finding identity across recurrence; harden report ingestion; preserve Worker selection and governance; maintain archive compatibility; verify every changed repository path and contract.

## 4. Requirements
1. Implement all 16 normative lifecycle rules and all Confirmation criteria in ADR-0004.
2. Every active task is a folder containing authoritative `task.md` and `subtasks/README.md`.
3. Every subtask has stable ID, type, status, acceptance criteria, evidence, and completion record.
4. Parent Done is blocked until all required subtasks are Done.
5. CI remediation subtask Done requires verified commit on intended branch plus recorded SHA and summary, not hosted validation.
6. Hosted validation is separate optional metadata and must not retroactively change remediation completion.
7. Ledger `task_refs` point to stable parent Task IDs. Terminal finding identity and resolution history remain retained.
8. Recurrence reopens the same finding identity, preserves prior resolution, and links new remediation work.
9. Ingestion errors are visible and cause non-zero command results; safe partial progress may be published and failed reports remain retryable.
10. Incomplete/pre-finalizer Actions captures remain unprocessed.
11. Unsafe report identifiers and missing indexed complete reports fail closed.
12. New P0 task generation does not displace a valid Worker-selected Current Execution task.
13. Ledger-generated tasks with Governing ADR(s) Pending remain Proposed and cannot execute.
14. New folder archives preserve complete task folders; legacy flat archives remain readable and immutable.
15. Migrate active flat task notes while preserving IDs, content, evidence, approval, progress, and relative links. Do not rewrite historical archives.
16. Update templates, skills, schema, tests, catalog, board, workspace and triage documentation.
17. Read back every changed file, migrated task folder, board link, Ledger record, and archive index entry.
18. Do not inspect hosted CI results until explicit user trigger. Do not claim tests passed unless observed.

## 5. Decisions
- **Governing decision:** Accepted ADR-0004, Option 3.
- **Task boundary:** Parent task is a folder; subtasks are child records within it.
- **CI subtask Done:** Verified remediation commit on intended branch, SHA and summary recorded.
- **Hosted validation:** Separate metadata; not a CI subtask completion prerequisite.
- **Finding recurrence:** Retain finding identity/history; reopen same finding and link new remediation work.
- **Task generation governance:** Generated implementation task remains Proposed while Governing ADR(s) is Pending.
- **Archive compatibility:** New folder archives; legacy flat archived notes remain immutable and readable.
- **Current execution:** This task is selected by explicit user instruction. Previous Current Execution is deselected but remains In Progress.

## 6. Progress Log
### 2026-11-26 23:29 UTC
- **Action:** Promoted user-approved DRAFT-0005 revision 1 to ADR-0004 using the provisional-record, completeness comparison, accepted read-back, and source deletion sequence.
- **Result:** ADR-0004 accepted; source Draft deleted; ADR index and discussion register updated. Implementation is authorized under this task.
- **References:** `workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md`.
- **Next:** Implement folder-based task records and Ledger lifecycle across the six child subtasks.

### 2026-11-26 23:29 UTC
- **Action:** Re-audited task board and created this implementation task as the first folder-based task with nested child records.
- **Result:** Task-folder architecture is being applied to the implementation task itself. No Ledger implementation files have yet been changed.
- **References:** `workspace/task_board.md`; prior task `20261126-170259-02`; accepted ADR-0004.
- **Next:** Execute subtasks in dependency order, commit coherent changes, and read back every changed path.

### 2026-11-27 00:58 UTC
- **Action:** Completed subtask 05. Migrated all six active flat task records, updated board links, repaired and verified relative evidence links, and implemented atomic retention for indexed task-folder archives with regression coverage.
- **Result:** All six legacy flat paths are absent. All six task folders and subtask indexes, the board, relevant evidence targets, cleanup script, test file, Ledger, and retention index were read back. Hosted tests remain unreviewed by explicit instruction.
- **References:** `workspace/tasks/`; `workspace/task_board.md`; `.github/scripts/cleanup-archive.py`; `.github/scripts/test_cleanup_archive.py`; commits `79cda7d`, `45c3f05`, `e1f2dca`, `80b568e`.
- **Next:** Execute subtask 06 only. Do not inspect hosted CI results until the user triggers results review.

### 2026-11-27 01:10 UTC
- **Action:** Reopened subtask 05 after the final ADR Confirmation audit found that the Ledger has no task-archive reader. The retention workflow alone does not satisfy the requirement for Ledger archive compatibility.
- **Result:** Exact-indexed-path Ledger reading for new folder archives and historical flat archives is now the first incomplete implementation item. Existing migration, retention, documentation, and regression changes remain committed. Hosted results remain unreviewed.
- **References:** ADR-0004 Confirmation criterion 13; `.takeout/reports/triage/scripts/ledger.py`; `.github/archive-retention-index.json`; subtasks 05 and 06.
- **Next:** Implement the archive reader without scanning or rewriting `.archive/`.

### 2026-11-27 01:10 UTC
- **Action:** Completed subtask 05 after implementing the Ledger archive reader. The reader resolves retained folder and historical flat task archives through exact retention-index paths. Recurrence adds a Related tasks link when the prior archive remains retained. Fixed the malformed Ledger function boundary found during source inspection.
- **Result:** Subtask 05 is Done. Regression cases cover both archive formats, no-scan behavior, incomplete indexes, and recurrence links. All relevant files were read back. No tests were run or hosted results reviewed.
- **References:** `.takeout/reports/triage/scripts/ledger.py`; `.takeout/reports/triage/scripts/test_ledger.py`; `.github/scripts/cleanup-archive.py`; `.github/scripts/test_cleanup_archive.py`; commits `7632ed1`, `5e7d051`, `6a443e7`, `0763c16`.
- **Next:** Finish subtask 06 and map all Confirmation criteria. Keep hosted-results review deferred.

### 2026-11-27 01:10 UTC
- **Action:** Completed subtask 06 and mapped all 16 ADR-0004 Confirmation criteria. Added fail-closed checks for missing retained archive-index paths in the cleanup workflow and documented the integrity rule across archive, Worker, CI Ledger, and GitHub Actions guidance.
- **Result:** All six implementation subtasks are Done. Criteria 1–14 are supported by repository evidence. Criterion 15 remains pending hosted review. Criterion 16 is partial because two sampled non-expired archive-index paths are missing. No historical archive file or index entry was changed.
- **References:** Parent Verification matrix; `.github/scripts/cleanup-archive.py`; `.github/scripts/test_cleanup_archive.py`; `.takeout/reports/triage/scripts/ledger.py`; `.takeout/reports/triage/scripts/test_ledger.py`; `.github/archive-retention-index.json`.
- **Next:** Obtain user disposition for missing archive paths, then await explicit hosted-results-review trigger. Do not archive or mark the parent Done yet.

### 2026-11-27 01:10 UTC
- **Action:** Final archive-index audit found at least two non-expired historical flat task paths that return NOT_FOUND. Added fail-closed validation for missing retained index paths in the cleanup workflow and a regression test. Updated the archive, Worker, CI Ledger, GitHub Actions, and discussion guidance. Reconciled the two migrated task links in the discussion register.
- **Result:** No historical archive file or retention-index entry was modified. The cleanup workflow now surfaces missing retained files instead of silently passing or pruning them. Parent Confirmation item 16 remains partial pending user direction.
- **References:** `.github/scripts/cleanup-archive.py`; `.github/scripts/test_cleanup_archive.py`; `.archive/README.md`; `.agent/skills/the-worker/SKILL.md`; `.agent/skills/ci-ledger/SKILL.md`; `.agent/skills/github-actions/SKILL.md`; `workspace/discussion.md`.
- **Next:** Wait for user direction on recovery or index-entry removal. Do not inspect hosted results.

## 7. Current State
- ADR-0004 is accepted and indexed.
- This task is Approved, P0, In Progress, and Current Execution.
- All six required implementation subtasks are Done.
- The Ledger generator, commit-based resolution and recurrence, ingestion integrity, active-task folder migration, atomic folder retention, indexed folder and flat archive reading, regression coverage, and documentation/catalog alignment are implemented.
- Historical archive-index integrity is verified. Confirmation criterion 16 is Verified by the exact-index audit and commit 25e72ef8c229ff7e99a9b10267314d6efe0b710b.
- Confirmation criterion 15 remains Pending because hosted Ledger regression and Document Type Catalog results have not been reviewed. No hosted pass is claimed.

## 8. Remaining Work
- Hosted Ledger regression and Document Type Catalog results remain unreviewed pending the user's explicit results-review trigger.

## 9. Next Actions
1. Wait for the user's explicit hosted-results-review trigger. Do not inspect or dispatch workflows before it.
2. Complete parent archive closeout after Confirmation criterion 15 is satisfied.

## 10. References
- [ADR-0004](../../adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md)
- [Task board](../../task_board.md)
- [CI Ledger skill](../../../.agent/skills/ci-ledger/SKILL.md)
- [Worker skill](../../../.agent/skills/the-worker/SKILL.md)
- [GitHub Actions skill](../../../.agent/skills/github-actions/SKILL.md)
- [Ledger implementation](../../../.takeout/reports/triage/scripts/ledger.py)
- [Ledger schema](../../../.takeout/reports/triage/ledger-schema.json)
- [Ledger tests](../../../.takeout/reports/triage/scripts/test_ledger.py)

## 11. Verification
- **Check:** ADR-0004 promotion, source Draft deletion, ADR index, and task/archive consistency.
- **Method:** GitHub branch read-back of the accepted ADR, indexes, active task folders, task board, discussion register, and archive-retention index.
- **Result:** ADR-0004 accepted. DRAFT-0005 deleted after read-back. All six subtasks Done. Confirmation criteria 1–14 are Verified. Criterion 15 remains Pending. Criterion 16 is Verified after commit 25e72ef8c229ff7e99a9b10267314d6efe0b710b.
- **Limitations:** No local tests were run. Hosted Ledger regression and Document Type Catalog results were not inspected. Do not claim hosted validation.

## 12. Handoff Instructions
Resume only after the user explicitly triggers hosted-results review. Do not dispatch, poll, rerun, or inspect hosted CI results before that trigger. After criterion 15 passes, complete parent archive closeout and verify the full folder archive. Use remote GitHub operations only. Do not run repository scripts locally. Do not expand into DRAFT-0003.

## 13. Subtasks
See [subtasks/README.md](subtasks/README.md) for the canonical child list and execution order.
