# Subtask: Regression coverage and documentation/catalog alignment

**Template version:** 1.0

## Metadata
- **ID:** 20261126-232913-06
- **Parent Task ID:** 20261126-232913
- **Type:** Implementation
- **Status:** Ready
- **Priority:** P0
- **Origin:** User
- **Approval:** Approved
- **Governing ADR(s):** ADR-0004
- **Dependencies:** 20261126-232913-01
- **Required:** Yes
- **Created:** 2026-11-26 23:29 UTC
- **Updated:** 2026-11-26 23:31 UTC

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

## 6. Current State
Ready; implementation has not started.

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
