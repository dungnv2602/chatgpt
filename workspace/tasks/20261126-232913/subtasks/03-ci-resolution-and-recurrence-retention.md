# Subtask: Commit-based CI resolution and recurrence retention

**Template version:** 1.0

## Metadata
- **ID:** 20261126-232913-03
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
- **Updated:** 2026-11-26 23:50 UTC

## 1. Objective
Implement commit-based CI resolution and durable finding identity/history across recurrence.

## 2. Scope
Implement only this subtask within ADR-0004. Parent: [20261126-232913](../task.md). Governing decision: [ADR-0004](../../../../adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md).

## 3. Acceptance Criteria
1. Allow resolved findings with a verified remediation commit and resolved timestamp without requiring successful hosted validation.
2. Represent hosted validation separately as optional, schema-validated metadata.
3. Make CI subtask Done require verified intended-branch commit SHA and remediation summary.
4. Retain terminal finding identity and resolution history after task archival; remove destructive retirement behavior.
5. On recurrence, preserve prior resolution history and append new parent task references without invalidating old remediation records.
6. Add regression tests for commit-only resolution, validation states, recurrence, and archive retention.

## 4. Decisions
- Follow ADR-0004.
- Keep implementation evidence separate from hosted validation evidence.
- Do not weaken existing checks or inspect hosted results before explicit user trigger.

## 5. Progress Log
### 2026-11-26 23:31 UTC
- **Action:** Registered this implementation subtask and its acceptance criteria.
- **Result:** Ready; no implementation changes for this subtask yet.
- **References:** ADR-0004 and parent task folder.
- **Next:** Execute after dependencies are complete.

## 6. Current State
Done. Commit-based resolution, optional validation metadata, schema migration from 1.5.0, recurrence history retention, and removal of destructive retirement are implemented. Regression coverage is updated but unrun.

## 8. Completion Record
- **Status:** Done
- **Completed at:** 2026-11-26 23:50 UTC
- **Completion basis:** All six acceptance criteria are implemented and regression coverage exists. Remote read-back verified. Tests were not executed.
- **Evidence:** Ledger SHA e2f423983c7339d746b561f116fe38d0219792c3; schema SHA 2532b58d6dd529e4d22dc755e0247676d2f38231; test SHA b93d6f31e2f0c8b2c3a8d9be06b0bf624cd006b4.

## 7. Evidence
- **Commit SHA:** Not applicable yet.
- **Changed paths:** None.
- **Read-back:** Not performed.
- **Other evidence:** None.

## 8. Completion Record
- **Status:** Ready
- **Completed at:** Not applicable
- **Completion basis:** Not Done.
- **Evidence:** Not applicable.

## 10. Handoff
Follow the parent subtask index. Record exact commits and read-back evidence. Do not mark Done until all acceptance criteria pass.
