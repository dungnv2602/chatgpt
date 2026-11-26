# Subtask: [Title]

**Template version:** 1.0

Store this record under its parent task's `subtasks/` directory.

## Metadata

- **ID:** <parent-task-id>-NN
- **Parent Task ID:** YYYYMMDD-HHMMSS
- **Type:** Implementation
- **Status:** Ready
- **Priority:** P2
- **Origin:** User
- **Approval:** Approved
- **Governing ADR(s):** None — non-implementation subtask
- **Dependencies:** None
- **Required:** Yes
- **Created:** YYYY-MM-DD HH:MM UTC
- **Updated:** YYYY-MM-DD HH:MM UTC

Allowed statuses: Proposed, Ready, In Progress, Blocked, Paused, Done, Cancelled. A parent cannot be Done while a required subtask is not Done.

## 1. Objective

[State this subtask's independently completable outcome.]

## 2. Scope

[Define exact work included and excluded. Link the parent and governing ADR.]

## 3. Acceptance Criteria

1. [Observable criterion.]
2. [Observable criterion.]

## 4. Decisions

[Record approved decisions, rationale, and unresolved questions.]

## 5. Progress Log

### YYYY-MM-DD HH:MM UTC

- **Action:** [What changed or was checked.]
- **Result:** [Observed outcome.]
- **References:** [Exact paths, commits, URLs, or source IDs.]
- **Next:** [Next action.]

## 6. Current State

[Verified state of this subtask.]

## 7. Evidence

- **Commit SHA:** [Required for code-remediation completion when applicable.]
- **Changed paths:** [Exact paths.]
- **Read-back:** [Exact verification result.]
- **Other evidence:** [Relevant source or test evidence.]

## 8. Completion Record

- **Status:** Not Done
- **Completed at:** Not applicable
- **Completion basis:** Not applicable
- **Evidence:** Not applicable

A regular subtask is Done when its own acceptance criteria are satisfied and its work/evidence are recorded.

## 9. Hosted Validation

Conditional: CI remediation subtask only.

- **Status:** Pending
- **Run URL:** Not reviewed
- **Reviewed at:** Not reviewed

Hosted validation is separate from remediation completion. Do not keep a CI remediation subtask open solely because hosted validation is pending. Do not inspect hosted results until the user explicitly triggers results review.

## 10. Handoff

[Exact next action, remaining work, dependencies, and constraints.]
