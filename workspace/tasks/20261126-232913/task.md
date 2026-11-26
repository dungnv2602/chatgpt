# Task: Implement ADR-0004 task folders and CI Ledger lifecycle

## Metadata
- **Template version:** 1.3 (folder-based implementation task; canonical folder template is part of this task)
- **ID:** 20261126-232913
- **Created:** 2026-11-26 23:29 UTC
- **Updated:** 2026-11-26 23:29 UTC
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

## 7. Current State
- ADR-0004 is accepted and indexed.
- This task is Approved, P0, In Progress, and Current Execution.
- Six implementation subtasks are registered in this folder.
- The CI Ledger still has the defects identified during static audit; no remediation code has yet been changed.
- No hosted workflow has been run or inspected for this implementation.

## 8. Remaining Work
- All six subtasks remain incomplete.
- Active flat task records have not yet been migrated.
- Templates, generator, schema, skills, archive reader/writer, tests, and catalog have not yet been updated.
- Hosted regression results remain intentionally unreviewed pending explicit user trigger.

## 9. Next Actions
1. Implement canonical folder and subtask templates plus Worker lifecycle rules.
2. Update Ledger task generation and task governance handoff.
3. Implement commit-based resolution and recurrence retention.
4. Harden ingestion and report-index integrity.
5. Migrate active tasks and update folder archive compatibility.
6. Add regression coverage and update catalog/workspace/triage documentation.
7. Perform complete remote read-back, commit, and stop before hosted results review.

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
- **Check:** ADR-0004 promotion, source Draft deletion, and ADR index.
- **Method:** GitHub branch read-back of the accepted ADR, index, Draft index, and discussion register.
- **Result:** ADR-0004 accepted; DRAFT-0005 deleted after read-back; indexes updated.
- **Limitations:** This verifies decision promotion only, not implementation or runtime behavior.

## 12. Handoff Instructions
Resume from the first incomplete child subtask in `subtasks/README.md`. Follow ADR-0004 and do not expand into DRAFT-0003. Use remote GitHub operations only. Do not run repository scripts locally. Do not dispatch, poll, rerun, or inspect hosted CI results until the user explicitly triggers results review. Commit and read back each coherent change. Keep the parent In Progress until every required child is Done and the folder archive is verified.

## 13. Subtasks
See [subtasks/README.md](subtasks/README.md) for the canonical child list and execution order.
