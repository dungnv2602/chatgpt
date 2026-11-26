# Subtask: Task folder templates and Worker lifecycle

**Template version:** 1.0

## Metadata
- **ID:** 20261126-232913-01
- **Parent Task ID:** 20261126-232913
- **Type:** Implementation
- **Status:** Done
- **Priority:** P0
- **Origin:** User
- **Approval:** Approved
- **Governing ADR(s):** ADR-0004
- **Dependencies:** None
- **Required:** Yes
- **Created:** 2026-11-26 23:29 UTC
- **Updated:** 2026-11-26 23:31 UTC

## 1. Objective
Create the canonical folder/subtask format and align Worker lifecycle, discovery, selection, and closeout rules.

## 2. Scope
Implement only this subtask within ADR-0004. Parent: [20261126-232913](../task.md). Governing decision: [ADR-0004](../../../../adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md).

## 3. Acceptance Criteria
1. Canonical task-folder and subtask templates exist and are registered in Document Type Catalog.
2. Parent/subtask statuses, ownership, acceptance criteria, evidence, completion records, and parent Done gate are explicit.
3. Worker discovery, selection, progress, handoff, and folder closeout instructions follow ADR-0004.
4. Board/navigation contract supports folder task.md paths while preserving compatibility during migration.
5. All changed templates, catalog entries, and Worker rules are read back.

## 4. Decisions
- Follow ADR-0004.
- Keep implementation evidence separate from hosted validation evidence.
- Do not weaken existing checks or inspect hosted results before explicit user trigger.

## 5. Progress Log
### 2026-11-26 23:31 UTC
- **Action:** Completed the canonical task-folder and Worker lifecycle contract.
- **Result:** All acceptance criteria passed remote read-back.
- **References:** Commit d139653d54269ee6c2df0e39283f30df7030339d.
- **Next:** Continue with subtask 02.

## 6. Current State
Complete. The canonical templates, catalog, Worker policy, and workspace navigation are committed and read back.

## 7. Evidence
- **Commit SHA:** d139653d54269ee6c2df0e39283f30df7030339d
- **Changed paths:** workspace/TASK_TEMPLATE.md; workspace/SUBTASK_TEMPLATE.md; .agent/skills/document-standards/references/document-type-catalog.md; .agent/skills/the-worker/SKILL.md; workspace/README.md
- **Read-back:** All five paths retrieved from branch gpt. Verified template versions, parent/child path coverage, Worker folder creation, commit-based CI completion, governance handoff, finding-history retention, workspace navigation, and task.md board link.
- **Completed at:** 2026-11-26 23:31 UTC

## 8. Completion Record
- **Status:** Done
- **Completed at:** 2026-11-26 23:31 UTC
- **Completion basis:** All five acceptance criteria satisfied and exact changed paths read back.
- **Evidence:** Commit d139653d54269ee6c2df0e39283f30df7030339d.

## 10. Handoff
Proceed to subtask 02 — Ledger task generation and governance handoff.
