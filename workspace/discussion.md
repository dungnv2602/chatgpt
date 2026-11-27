# Discussion Register

## Current Step

_No active step._

## Open Discussions

- **2026-11-27:** User confirmed permanent removal of `workspace/archive/` and retirement of task/report archiving. Completed or cancelled task folders must be deleted directly after closeout checks. No archive copy, retention index, scheduled cleanup, or Historical board row is permitted.
- **2026-11-27:** Formal governance follow-up remains open. Accepted ADR-0004 and approved DRAFT-0007 still describe legacy task-archive compatibility. The operational workflow now follows the user's newer deletion instruction, but accepted ADR decision content was not edited. A superseding decision record is required to reconcile the formal ADR history.
- **2026-11-27 06:10 UTC:** Prepared [DRAFT-0007 revision 1](draft/DRAFT-0007-editorial-successor-for-adr-0004.md) for the 34 ADR-0004 editorial findings. It proposes a superseding editorial successor while preserving the accepted outcome, scope, lifecycle rules, and Confirmation states. User approved revision 1 and Option 3; promotion remains a separate governance step.
- **2026-11-27 06:10 UTC:** Prepared [DRAFT-0006 revision 1](draft/DRAFT-0006-editorial-successor-for-adr-0003.md) for the 31 ADR-0003 editorial findings. It proposes a superseding editorial successor while preserving the accepted outcome, scope, and Confirmation states. User approved revision 1 and Option 3; promotion remains a separate governance step. Task 170259-03 is Done and remains closed.
- **2026-11-27 05:31 UTC:** [20261126-090154](tasks/20261126-090154/task.md) is Blocked. Five of six ADR-0003 Confirmation criteria are verified. Criterion 4 requires an explicit user-authorized read-only full-repository reference search.
- **2026-11-27 05:31 UTC:** [20261126-232913](tasks/20261126-232913/task.md) has all six implementation subtasks Done. ADR-0004 Confirmation criterion 16 is Verified. Criterion 15 remains Pending until the user explicitly triggers hosted Ledger regression and Document Type Catalog results review.
- **2026-11-27:** The legacy retention index contained 52 entries for missing files. The user subsequently authorized deletion of the entire archive tree and retirement of retention. The obsolete index and cleanup workflow are removed with the archive.
- **2026-11-26 15:00 UTC:** DRAFT-0002 revision 4 remains in review. Its wording corrections passed hosted lint. The decision and implementation scope remain unapproved.

## Reports

- **2026-11-27 07:15 UTC:** Completed the mandatory startup P0 batch eligibility review. The task board has no Ready P0 tasks. Eight active Ledger-generated P0 task groups remain Proposed because accepted ADR coverage is pending for edits to ADR-0003 and ADR-0004. No eligible remediation could proceed. No source changes or hosted CI results review were performed.
- **2026-11-27 06:10 UTC:** Created DRAFT-0006 and DRAFT-0007 as separate in-review proposals. Each assesses the no-change, companion-note, and superseding-successor options. Indexed both Drafts and linked them from Open Discussions. Read-back and reference checks remain pending.
- **2026-11-27 05:31 UTC:** Resolved archived P0 finding `gha-f04b588b537a96b00c56b6ae` for task 20261126-145133. Verified fix commit `07214aa44105022ade3a42317d60ecba9e235e1a` remains on branch `gpt` and the workflow retains the bounded five-attempt publication retry. Read back the Ledger resolution. Hosted validation remains Pending and was not reviewed.

- **2026-11-27:** Updated task closeout, CI Ledger recurrence, workspace navigation, task template, board, Document Type Catalog, GitHub Actions policy, and Markdown link validation for direct deletion. Removed the archive retention workflow, cleanup tooling, index/state, and the complete `workspace/archive/` tree. Commits: `cf40560361853df9a6b2550e72e55d236a1aace9`, `62d27d93857812c7340ad3afce23ba435af0cf55`, and `2ae31d2ed356edc660d6708a6340f8c450705f5d`. Automated workflows may run on push; no CI results were inspected.
