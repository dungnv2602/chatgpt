# Discussion Register

## Current Step
Complete the archive-root migration and verify the new workspace/archive layout and scheduled retention workflow. DRAFT-0006 and DRAFT-0007 revision 1 are approved; ADR promotion remains a separate governance step. Preserve the authorization gates for tasks 20261126-090154 and 20261126-232913.

## Open Discussions

- **2026-11-27 06:10 UTC:** Prepared [DRAFT-0007 revision 1](draft/DRAFT-0007-editorial-successor-for-adr-0004.md) for the 34 ADR-0004 editorial findings. It proposes a superseding editorial successor while preserving the accepted outcome, scope, lifecycle rules, and Confirmation states. User approval is pending.
- **2026-11-27 06:10 UTC:** Prepared [DRAFT-0006 revision 1](draft/DRAFT-0006-editorial-successor-for-adr-0003.md) for the 31 ADR-0003 editorial findings. It proposes a superseding editorial successor while preserving the accepted outcome, scope, and Confirmation states. User approval is pending. Task 170259-03 is Done and remains closed.
- **2026-11-27 05:31 UTC:** [20261126-090154](tasks/20261126-090154/task.md) is Blocked. Five of six ADR-0003 Confirmation criteria are verified. Criterion 4 requires an explicit user-authorized read-only full-repository reference search.
- **2026-11-27 05:31 UTC:** [20261126-232913](tasks/20261126-232913/task.md) has all six implementation subtasks Done. ADR-0004 Confirmation criterion 16 is Verified. Criterion 15 remains Pending until the user explicitly triggers hosted Ledger regression and Document Type Catalog results review.
- **2026-11-27 01:10 UTC:** At least two non-expired entries in `.github/archive-retention-index.json` reference historical flat task files that return NOT_FOUND: `workspace/archive/task/20261123043747-audit-template-placement-and-enforce-template-first-workflow.md` and `workspace/archive/task/20261123-041640-worker-mode-independent-and-lint-report-formats.md`. The Ledger reader and retention workflow now fail closed on missing retained paths. Historical files and index entries remain unchanged. User direction is required before recovery or index removal.
- **2026-11-26 15:00 UTC:** DRAFT-0002 revision 4 remains in review. Its wording corrections passed hosted lint. The decision and implementation scope remain unapproved.

## Reports

- **2026-11-27 06:10 UTC:** Created DRAFT-0006 and DRAFT-0007 as separate in-review proposals. Each assesses the no-change, companion-note, and superseding-successor options. Indexed both Drafts and linked them from Open Discussions. Read-back and reference checks remain pending.
- **2026-11-27 05:31 UTC:** Resolved archived P0 finding `gha-f04b588b537a96b00c56b6ae` for task 20261126-145133. Verified fix commit `07214aa44105022ade3a42317d60ecba9e235e1a` remains on branch `gpt` and the workflow retains the bounded five-attempt publication retry. Read back the Ledger resolution. Hosted validation remains Pending and was not reviewed.
- **2026-11-27 05:31 UTC:** Reconciled eight active Ledger-generated P0 tasks. All remain mandatory and execution-approved. Their Proposed status now matches accepted-ADR governance. The board points to the valid Current Execution task. The CI Ledger, Decision Governance, workspace guide, board, templates, and catalog now state the same rule. Read-back checks passed. No source remediation or hosted CI results review was performed.

- **2026-11-27:** User directed retirement of the former root archive directory. The migration relocates archived ADRs into `workspace/adr/`, preserves task and report archives under `workspace/archive/`, and updates the retention index and readers. Two historical flat task index entries remain missing and must continue to fail closed.
