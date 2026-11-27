# Task: Remove the standalone latest lint report copy

**Template version:** 2.6

## Metadata

- **ID:** 20261127-173500
- **Created:** 2026-11-27 17:40 UTC
- **Updated:** 2026-11-27 17:40 UTC
- **Priority:** P0
- **Status:** Proposed
- **Origin:** User
- **Approval:** Approved
- **Approval scope/source:** Explicit user instruction to delete `.takeout/reports/latest-lint-report.json`.
- **Governing ADR(s):** Pending — DRAFT-0005
- **Current execution:** No
- **Dependencies:** User approval of DRAFT-0005 revision 1 and promotion to an accepted ADR.
- **Eligibility / deferral reason:** Proposed — implementation would change accepted ADR-0003. Do not modify the report file, generator, workflows, or consumers until the new ADR reaches accepted status.
- **Related tasks:** ADR-0003; Refactor Skills parent 20261127-173000 (subsequent workstream instruction only).

## 1. Original Request

> `.takeout/reports/latest-lint-report.json`
>
> Delete this as we agreed on the format

## 2. Subsequent Instructions

> Then proceed to the task "refactor skills"
>
> /start

The Refactor Skills workstream continues under its own parent. This report-layout task remains separate because its objective does not refactor repository skills.

## 3. Objective and Acceptance Criteria

Remove the standalone latest lint report JSON and use the unified `.takeout/reports/index.json` as the only locator for the latest lint report.

1. Obtain approval for DRAFT-0005 revision 1 and promote it to a new accepted ADR. Keep ADR-0003 immutable.
2. Stop the lint generator from writing the standalone latest JSON file.
3. Resolve the latest eligible lint baseline from the shared index and its `history_path`.
4. Update both lint workflows, regression tests, and active report documentation.
5. Delete `.takeout/reports/latest-lint-report.json`.
6. Read back all changed paths and confirm no active producer or consumer depends on the deleted path.
7. Do not inspect hosted CI results or run local tests.

## 4. Decisions

- **Proposal:** DRAFT-0005 revision 1 recommends an index-only latest-report locator.
- **Decision status:** Pending user approval.
- **Execution status:** Proposed. Task approval does not replace decision approval.

## 5. Progress

### 2026-11-27 17:40 UTC

- **Action:** Created this independent parent after correcting its objective-based hierarchy.
- **Result:** DRAFT-0005 revision 1 is in review. No implementation changes have been made.
- **References:** [DRAFT-0005](../draft/DRAFT-0005-unified-index-without-latest-lint-copy.md); [ADR-0003](../adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md).
- **Next:** Wait for approval of the exact Draft revision. Promote the decision before implementation.

## 6. Current State and Remaining Work

The accepted ADR-0003 requires one latest lint JSON file. DRAFT-0005 proposes to supersede that requirement. Implementation remains blocked until the user approves the Draft and the resulting ADR reaches accepted status.

## 7. Verification and Evidence

- **Commit SHA:** Not committed.
- **Changed paths:** Task record and task index only.
- **Readback:** Pending.
- **Checks:** Not performed.
- **Limitations:** No tests or hosted validation were performed.

## 8. Handoff

Wait for the user's decision on DRAFT-0005 revision 1. Do not implement the proposal before the new ADR reaches accepted status.

## 9. Subtasks

Canonical index: [subtasks/README.md](subtasks/README.md).

## 10. Ledger Findings

Not applicable.
