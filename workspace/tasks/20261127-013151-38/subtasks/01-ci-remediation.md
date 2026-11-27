# Subtask: CI remediation — Fix lint tooling check: Markdown links and heading anchors

**Template version:** 1.0

Store this record under its parent task's `subtasks/` directory.

## Metadata

- **ID:** 20261127-013151-38-01
- **Parent Task ID:** 20261127-013151-38
- **Type:** CI remediation
- **Status:** Proposed
- **Priority:** P0
- **Origin:** Assistant
- **Approval:** Pending — Worker review required
- **Governing ADR(s):** Pending — Worker review required before approval
- **Dependencies:** None
- **Required:** Yes
- **Created:** 2026-11-27 01:31 UTC
- **Updated:** 2026-11-27 01:31 UTC

Allowed statuses: Proposed, Ready, In Progress, Blocked, Paused, Done, Cancelled. A parent cannot be Done while a required subtask is not Done.

## 1. Objective

Remediate the CI finding group ci-ace4e198cb6445b7 and record a verified fix commit.

## 2. Scope

Inspect the linked report evidence, diagnose the actionable finding group, implement the authorized fix, commit it to the intended branch, and record the commit SHA and concise summary. Hosted validation is tracked separately and is not a completion prerequisite. Parent task: 20261127-013151-38.

## 3. Acceptance Criteria

1. Worker separately authorizes remediation after decision-governance review.
2. The fix is committed to the intended branch and the commit is verified.
3. The commit SHA and remediation summary are recorded.
4. This subtask is marked Done only after these criteria pass; hosted validation remains separate metadata.

## 4. Decisions

- **Completion rule:** Commit-based Done under ADR-0004.
- **Hosted validation:** Separate Pending/Passed/Failed metadata; not a Done gate.

## 5. Progress Log

### 2026-11-27 01:31 UTC

- **Action:** Created a Proposed CI remediation subtask from Ledger finding group.
- **Result:** 1 finding(s) linked; no remediation is authorized or claimed.
- **References:** .takeout/reports/triage/ledger.json and parent task Ledger Findings.
- **Next:** Worker review, accepted ADR linkage, and separate execution approval.

## 6. Current State

Proposed. Root cause and fix have not been assessed; no commit exists.

## 7. Evidence

- **Commit SHA:** Not available — no remediation commit yet.
- **Changed paths:** None.
- **Read-back:** Not performed.
- **Other evidence:** See parent Ledger Findings for source reports.

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

Worker reviews the finding evidence and governing ADR coverage. Keep Proposed until the Worker separately approves execution. Do not inspect hosted validation results until the user explicitly triggers results review.
