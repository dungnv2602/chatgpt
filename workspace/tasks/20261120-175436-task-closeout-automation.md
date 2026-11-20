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

## 7. Current State

The required workflow change and closeout repair are being applied to branch `gpt`.

## 8. Remaining Work

- Commit and verify the Worker skill change.
- Complete the audit task archival and board reconciliation.
- Verify the task board, this task record, and branch head.

## 9. Next Actions

1. Commit the global Worker closeout procedure and archive the completed audit record.
2. Reconcile the task board and add this task as Current Execution.
3. Fetch and verify all changed active paths and the resulting branch head.

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
