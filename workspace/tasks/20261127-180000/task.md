# Task Folder: Improve Repository Diagnostic Investigation Process

**Template version:** 2.6

## Metadata

- **ID:** 20261127-180000
- **Created:** 2026-11-27 18:00 UTC
- **Updated:** 2026-11-27 18:00 UTC
- **Priority:** P0
- **Status:** In Progress
- **Origin:** User
- **Approval:** Approved
- **Approval scope/source:** Explicit user instruction: "Fix your process"
- **Governing ADR(s):** None
- **Current execution:** Yes
- **Dependencies:** None
- **Eligibility / deferral reason:** Executing — Ready and authorized
- **Related tasks:** 20261126-142500-03; 20261126-142500-23

## 1. Original Request

Fix your process

## 2. Subsequent Instructions

- 2026-11-27 18:00 UTC — The user clarified the reporting issue: "I don't understand, it's clearly workflow broken, if you want to inspect CI then clearly reports lacking"
- 2026-11-27 18:00 UTC — The user asked: "Fix it, make it sufficient enough for you in the future"
- 2026-11-27 18:00 UTC — The user requested: "Fix your process"

## 3. Objective and Acceptance Criteria

Update The Worker’s repository investigation process so repository-published diagnostic evidence is examined in depth before declaring CI-remediation tasks blocked. Address the distinction between committed diagnostics and restricted hosted CI inspection.

1. Require examination of structured report payloads and complete captured check outputs, not only summaries.
2. Require tracing concrete failure evidence into repository code, tests, workflow and report generation.
3. Treat reporting insufficiency as a reporting-workflow defect to investigate, not an automatic blocker.
4. Define a blocker declaration with specific evidence of what is unavailable and why local repository investigation cannot proceed.
5. Read back the updated process instruction.

## 4. Decisions

- Repository-published report artifacts are available for inspection under existing repository-access rules. This does not authorize hosted CI review.
- Do not run local scripts, tests or lint under the current Worker policy.

## 5. Progress

### 2026-11-27 18:00 UTC

- **Action:** Examined repository Worker, CI Ledger, report files and relevant task records.
- **Result:** The report JSON contained full test tracebacks and exact anchor failure diagnostics. Previous blocker claims relied on task summaries rather than payloads.
- **References:** CI report history referenced in the preceding conversation; related P0 children 03 and 23.
- **Next:** Update The Worker’s investigation protocol and board.

## 6. Current State and Remaining Work

The process correction is being implemented. Local tests and hosted CI review remain prohibited.

## 7. Verification and Evidence

- **Commit SHA:** Not committed
- **Changed paths:** Pending
- **Readback:** Pending
- **Checks:** Not performed
- **Limitations:** Process instruction readback does not prove execution behavior. No local tests or hosted CI review.

## 8. Handoff

Read back all changed files. No hosted CI review or local validation.

## 9. Subtasks

Canonical index: [subtasks/README.md](subtasks/README.md). No subtasks.

## 10. Ledger Findings

| Finding ID | Severity | Diagnostic | Evidence |
|---|---|---|---|
