# Subtask: CI remediation — Review present-perfect findings in workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md

**Template version:** 1.0

Store this record under its parent task's `subtasks/` directory.

## Metadata

- **ID:** 20261127-013151-34-01
- **Parent Task ID:** 20261127-013151-34
- **Type:** CI remediation
- **Status:** Proposed
- **Priority:** P0
- **Origin:** Assistant
- **Approval:** Approved
- **Governing ADR(s):** Pending — no accepted ADR authorizes edits to immutable decision content. User decision required.
- **Dependencies:** None
- **Required:** Yes
- **Created:** 2026-11-27 01:31 UTC
- **Updated:** 2026-11-27 05:31 UTC

Allowed statuses: Proposed, Ready, In Progress, Blocked, Paused, Done, Cancelled. A parent cannot be Done while a required subtask is not Done.

## 1. Objective

Remediate the CI finding group ci-e9ea5614f5298964 and record a verified fix commit.

## 2. Scope

Inspect the linked report evidence, diagnose the actionable finding group, implement the authorized fix, commit it to the intended branch, and record the commit SHA and concise summary. Hosted validation is tracked separately and is not a completion prerequisite. Parent task: 20261127-013151-34.

## 3. Acceptance Criteria

1. Worker separately authorizes remediation after decision-governance review.
2. The fix is committed to the intended branch and the commit is verified.
3. The commit SHA and remediation summary are recorded.
4. This subtask is marked Done only after these criteria pass; hosted validation remains separate metadata.

## 4. Decisions

- **Completion rule:** Commit-based Done under ADR-0004.
- **Hosted validation:** Separate Pending/Passed/Failed metadata. It is not a Done gate.
- **Standing P0 authorization:** Approved for mandatory processing. Accepted ADR linkage remains a prerequisite for source changes.

## 5. Progress Log

### 2026-11-27 01:31 UTC

- **Action:** Created a Proposed CI remediation subtask from Ledger finding group.
- **Result:** 1 finding(s) linked; no remediation is authorized or claimed.
- **References:** .takeout/reports/triage/ledger.json and parent task Ledger Findings.
- **Next:** Worker review, accepted ADR linkage, and separate execution approval.

### 2026-11-27 05:31 UTC

- **Action:** Reviewed the target accepted ADR under Decision Governance.
- **Result:** The finding requires a wording change to immutable ADR-0004 decision content. No accepted ADR covers this change. The user's standing P0 instruction authorizes mandatory processing, but it does not waive accepted-ADR governance. No source edit or fix commit was made. Keep this subtask Proposed.
- **References:** `.agent/skills/decision-governance/SKILL.md`; `workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md`; parent task Ledger Findings.
- **Next:** Obtain user approval for a separate Draft/ADR before any source change.

## 6. Current State
Proposed. Execution is approved as mandatory P0 work, but the required accepted decision coverage is missing. No remediation commit exists. Do not edit accepted ADR-0004 decision content.

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

Keep Proposed. Resume only after the user approves a separate Draft/ADR and it reaches accepted status. Do not inspect hosted validation results until the user explicitly triggers results review.
