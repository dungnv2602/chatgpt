# Task: Enforce automatic global task closeout and board reconciliation

## Metadata

- **ID:** 20261120-175436
- **Created:** 2026-11-20 17:54 UTC
- **Updated:** 2026-11-20 17:54 UTC
- **Priority:** P1
- **Status:** In Progress
- **Origin:** User
- **Approval:** Approved
- **Current execution:** Yes
- **Dependencies:** None
- **Related tasks:** 20261120-123000
- **Archived:** No

## 1. Original Request

> Something wrong, this should be automatically do by you, can you check your workflow then fix? If you have this strictly con condensed mode then fix, the worker is global

## 2. Subsequent Instructions

None.

## 3. Objective

Correct the global task workflow so task closeout automatically archives the task record and reconciles the task board in every conversation mode. Repair the incomplete closeout state left by the repository documentation audit.

## 4. Requirements

- The Worker remains the single global authority for task operations in Default Mode and Condensed Mode.
- Make archival and task-board reconciliation mandatory parts of one logical closeout transaction.
- Use only canonical task statuses.
- Do not report completion while the active record, archive record, and task board disagree.
- Preserve the seven-entry Historical limit and archive-boundary rules.
- Keep all changes on branch `gpt`.
- Read back every active changed path. Do not inspect archived contents.

## 5. Decisions

- Fix The Worker skill, not Conversation Mode. Conversation Mode controls communication style; The Worker controls task operations in every mode.
- Repair the prior audit closeout as part of this task: archive its record, remove its stale active board entries, and add its historical entry.
- Do not modify `main`.

## 6. Progress Log

### 2026-11-20 17:54 UTC

- **Action:** Inspected the global Worker skill, Conversation Mode skill, workspace rules, task board, completed audit task record, archive policy, and applicable CI state.
- **Result:** The Worker already applied globally, but its closeout instructions did not make the record move and board reconciliation an enforced transaction. The audit record used the non-canonical status "Completed", remained under `workspace/tasks/`, had Archived set to No, and the board still listed it as In Progress and Current Execution. The latest full-lint run #102 and changed-lint run #302 both succeeded. Branch head `864d1b80896394a0d84ff463f919b15057fd484c` has no associated check runs or status entries.
- **References:** `skills/the-worker/SKILL.md`; `skills/conversation-mode/SKILL.md`; `workspace/README.md`; `workspace/task_board.md`; `workspace/tasks/20261120-123000-repository-documentation-audit.md`; `archive/README.md`; `skills/github-actions/SKILL.md`; [run #102](https://github.com/dungnv2602/chatgpt/actions/runs/44781823351); [run #302](https://github.com/dungnv2602/chatgpt/actions/runs/44780350538).
- **Next:** Commit the global Worker closeout gate, archive the completed audit record, create this task record, and reconcile the board. Then read back the active changed paths and verify the commit metadata.

### 2026-11-20 17:55 UTC

- **Action:** Committed the global Worker closeout gate, archived the completed documentation-audit task, and created this workflow-repair task.
- **Result:** Commit `a0e4f8fe526d9c85ea8be8093953fcb2b7d82cd8` updated `skills/the-worker/SKILL.md`, created the audit archive record, removed its active task path, and created this task record. The board still requires reconciliation. Archived contents were not inspected.
- **References:** `skills/the-worker/SKILL.md`; archival commit [a0e4f8fe526d9c85ea8be8093953fcb2b7d82cd8](https://github.com/dungnv2602/chatgpt/commit/a0e4f8fe526d9c85ea8be8093953fcb2b7d82cd8).
- **Next:** Reconcile the board and verify all active changed paths.

## 7. Current State

The global Worker closeout gate is committed. The audit task is archived, its active path is absent, and the board reconciliation is now corrected. Final read-back remains.

### 2026-11-20 17:58 UTC

- **Action:** Read back the Worker skill, task board, active workflow task, and archival commit metadata. Checked the former active audit-task path.
- **Result:** The Worker closeout gate and archive commit are present. The old active audit-task path returns 404, and commit `a0e4f8fe526d9c85ea8be8093953fcb2b7d82cd8` includes the archived record. Read-back found that the first board update placed the audit historical row in Current Execution instead of Historical. This update corrects the row placement. Archived contents were not inspected.
- **References:** `skills/the-worker/SKILL.md`; `workspace/task_board.md`; [archival commit](https://github.com/dungnv2602/chatgpt/commit/a0e4f8fe526d9c85ea8be8093953fcb2b7d82cd8).
- **Next:** Verify the corrected board and task record from branch `gpt`.

## 8. Remaining Work

- Verify the corrected task board, this task record, Worker skill, and branch head.

## 9. Next Actions

1. Fetch and verify all changed active paths and the resulting branch head.
2. Confirm the archival commit contains the archive path using commit metadata only.

## 10. References

- `skills/the-worker/SKILL.md`
- `skills/conversation-mode/SKILL.md`
- `workspace/README.md`
- `workspace/task_board.md`
- `archive/README.md`

## 11. Verification

- **Check:** Global mode ownership and current closeout state.
- **Method:** Read the authoritative files from branch `gpt`.
- **Result:** Confirmed The Worker applies in both modes; confirmed the audit record and board were inconsistent.
- **Limitations:** Repository writes and read-back are pending.

## 12. Handoff Instructions

Continue on branch `gpt`. Finish the board reconciliation, fetch the changed active paths, and verify the commit that contains the archived audit record by commit metadata only. Do not inspect archived contents or modify `main`.
