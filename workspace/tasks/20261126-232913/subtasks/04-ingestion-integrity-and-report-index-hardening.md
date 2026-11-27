# Subtask: Ingestion integrity and report-index hardening

**Template version:** 1.0

## Metadata
- **ID:** 20261126-232913-04
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
- **Updated:** 2026-11-26 23:50 UTC

## 1. Objective
Ingestion integrity and report-index hardening as part of the accepted ADR-0004 implementation.

## 2. Scope
Implement only this subtask within ADR-0004. Parent: [20261126-232913](../task.md). Governing decision: [ADR-0004](../../../../adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md).

## 3. Acceptance Criteria
1. Surface per-report ingestion failures as structured errors and return non-zero after safe partial progress is published.
2. Leave failed reports unprocessed and retryable.
3. Do not mark incomplete or pre-finalizer Actions captures as processed.
4. Validate report/run identifiers before path construction and reject traversal or malformed identifiers.
5. Fail closed when the index references a missing report classified complete.
6. Add regression tests for each failure and retry invariant.

## 4. Decisions
- Follow ADR-0004.
- Preserve existing evidence and validation/security checks.
- Do not inspect hosted results before explicit user trigger.

## 5. Progress Log
### 2026-11-26 23:50 UTC
- **Action:** Began inspection of lint and Actions report indexes and Ledger ingestion behavior.
- **Result:** Current Ledger contains 31 findings and 5 resolved findings. Four resolved findings use ordinary success validation metadata; one uses a custom per-finding success conclusion while the overall workflow failed for unrelated findings. Schema 1.6 migration now preserves that raw conclusion and classifies it as passed without treating the workflow's unrelated failures as the finding's result.
- **References:** .takeout/reports/triage/ledger.json SHA e40aa15986bfe287be44ffb830b32acc4e80cdf1; .takeout/reports/gh_ac_reports/index.json; .takeout/reports/lint_reports/on_changed/index.json.
- **Next:** Validate indexed IDs and paths, preserve incomplete Actions captures for retry, and surface processing errors as non-zero results.

## 6. Current State
In Progress. Index shapes and existing resolved-validation records have been inspected. Report path validation, incomplete-capture retry handling, and failure exit codes remain to be implemented.

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
