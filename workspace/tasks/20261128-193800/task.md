# Task: Permanent CI remediation fallback parent

## Metadata

- **Template version:** 2.8
- **ID:** 20261128-193800
- **Created:** 2026-11-28 12:38 UTC
- **Updated:** 2026-11-28 12:38 UTC
- **Priority:** P1
- **Status:** In Progress
- **Origin:** System
- **Approval:** Approved
- **Approval scope/source:** Standing authorization from accepted ADR-0008 for the permanent fallback parent used only when source Task-ID attribution cannot resolve.
- **Governing ADR(s):** ADR-0008
- **Current execution:** No
- **Dependencies:** None
- **Eligibility / deferral reason:** Permanent system-owned fallback parent; never selected for execution. It only receives P0 CI-remediation children when source attribution is missing, invalid, ambiguous, or inactive.
- **Related tasks:** 20261128-230000

## Validation Contract

```json
{
  "contract_revision": "1",
  "checks": []
}
```

## 1. Original Request

Accepted ADR-0008 requires one permanent fallback parent for CI findings whose source task cannot be safely attributed. This system-owned parent is created under the ADR-0008 implementation task.

## 2. Subsequent Instructions

- **2026-11-28:** ADR-0008 is the authority for this permanent fallback parent. It is not a user work request and must never become Current Execution.

## 3. Objective and Acceptance Criteria

Maintain one permanent parent for actionable CI remediation when the source Task-ID is missing, malformed, ambiguous, points to a deleted/inactive task, or cannot be resolved through a child to its genuine parent.

1. The Worker-owned task-validation policy identifies this exact fallback parent ID.
2. Valid active user-originated parent attribution always takes precedence; otherwise use this fallback without guessing.
3. Create or reuse one P0, Approved child per distinct actionable root cause under this parent.
4. The parent remains active, non-current, and is never marked Done, Cancelled, or deleted by routine lifecycle cleanup.
5. Successful, cancelled, superseded, and non-actionable attempts create no child here.

## 4. Decisions

- This parent is system-owned (Origin: System), not a synthetic user task.
- It is the sole fallback parent for ADR-0008 CI remediation.
- Do not use the current execution pointer, changed files, workflow names, branch, or timing to infer attribution.
- Do not create additional fallback parents or delete this parent.

## 5. Progress

### 2026-11-28 12:38 UTC

- **Action:** Create the permanent fallback parent required by ADR-0008.
- **Result:** This record is the sole designated fallback parent. Policy and Worker/Ledger routing will be bound to this ID.
- **References:** ADR-0008 items 15–19; Worker task-validation policy.
- **Next:** Preserve this parent while completing only actionable fallback remediation children.

## 6. Current State and Remaining Work

Permanent container for unattributed actionable CI findings. Not a task execution target. It remains In Progress so it cannot be treated as a completed/deleted parent. Children carry the executable remediation work.

## 7. Verification and Evidence

- **Commit SHA:** Not committed
- **Changed paths:** This task record and subtasks index
- **Readback:** Pending
- **Checks:** Not performed
- **Limitations:** No CI finding has been attributed or diagnosed by this parent creation.

## 8. Execution self-check

- Parent exists only because ADR-0008 explicitly requires a permanent fallback.
- Origin is System; no user-originated task or parentage is fabricated.
- The record is excluded from Current Execution and the eligible queue.
- Routine cleanup must preserve this parent.

## 9. Handoff

Use only for actionable CI remediation whose source attribution cannot resolve. Never select this parent for execution or delete it.

## 10. Subtasks

Canonical index: [subtasks/README.md](subtasks/README.md).

## 11. Ledger Findings

| Finding ID | Severity | Diagnostic | Evidence |
|---|---|---|---|
| None | — | None yet | — |
