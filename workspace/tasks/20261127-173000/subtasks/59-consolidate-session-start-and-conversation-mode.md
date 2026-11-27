# Subtask: Consolidate Session Start and Conversation Mode

**Template version:** 1.5

## Metadata

- **ID:** 20261127-173000-59
- **Parent Task ID:** 20261127-173000
- **Type:** Decision preparation
- **Status:** In Progress
- **Priority:** P0
- **Origin:** User
- **Approval:** Approved
- **Approval scope/source:** The user's explicit request to make Session Start pointer-only, limit Conversation Mode to settings, relocate duplicated operating rules to their proper Worker or specialist owners, and reassess and reconcile the workflow.
- **Governing ADR(s):** None — this task prepares a decision Draft only. Implementation requires a separately accepted ADR.
- **Dependencies:** None
- **Eligibility / deferral reason:** In Progress — preparing the decision Draft under the user's direct instruction.
- **Required:** Yes
- **Created:** 2026-11-27 23:53 UTC
- **Updated:** 2026-11-27 23:53 UTC
- **Ledger group:** None
- **Legacy Task IDs:** None

This child belongs under the standing Refactor Skills parent because it directly refactors the repository's foundational skill and session instructions.

## 1. Original Prompt

> Session start and conversation mode should be absolutely lean.
>
> Session start should only contisn pointer and reading skills instructions based on my cue. Conversation mode should only have conversation settings.
>
> Identify redundancy in them and relocate to appropriate places in the Worker.
>
> Reassess your workflow, check if it already contains how you should work before, identify gaps why you didn't follow it, reconcile and refactor with what you recently added. No redundancy, refactor and optimize your workflow.

## 2. Subsequent Instructions

None.

## 3. Objective and Scope

Prepare one decision Draft for the requested workflow architecture. The proposal must make Session Start a cue guard and pointer to The Worker, limit Conversation Mode to presentation settings, and place operational authority in The Worker and its existing Worker-owned or specialist references.

The review must reconcile the recently added recovery-cleanup and sequential decision-collection rules with existing task, startup, skill-loading, and CI instructions. It must remove contradictory or duplicated live instructions rather than copy the same rule into another file.

This task authorizes Draft preparation and presentation only. It does not authorize implementation before the user approves the exact Draft revision and its accepted ADR.

## 4. Acceptance Criteria

1. The Draft assesses the current architecture, no-change, full centralization in the Worker, and a Worker-owned single-source architecture that uses existing focused references for detailed procedures.
2. The Draft records the observed instruction conflicts and the correct ownership boundary for each procedure.
3. The Draft identifies all affected canonical files and explains their proposed roles.
4. The Draft preserves cue-controlled initialization, progressive skill loading, the startup P0 batch, user-decision collection before batch execution, immediate temporary-material cleanup, and the existing restrictions on local validation and hosted CI review.
5. The Draft states exact non-goals, implementation order, verification limits, and confirmation criteria.
6. The exact Draft revision is read back and presented for user approval. No operational implementation occurs in this child.

## 5. Decisions and Progress

### 2026-11-27T23:53:02Z — task captured

- Created this decision-preparation child under the persistent Refactor Skills parent.
- Audited Session Start, Conversation Mode, The Worker, Initialization Policy, the Skills Directory index, the document-type catalog, and the task-board contract.
- Found a direct conflict: Session Start step 8 resumes execution after the first blocker answer. Its step 10 and The Worker require all user-resolvable calls to be collected before executing newly unlocked work.
- Found duplicated operational ownership for cleanup, task progression, blocker coordination, approval cues, repository discipline, startup CI handling, skill loading, and the discussion register.
- Next: prepare and present Draft DRAFT-0006. Do not implement until its exact revision receives approval and the resulting ADR is accepted.

## 6. State and Evidence

- **Commit SHA:** Not committed
- **Changed paths:** This task record, its parent subtask index, task board, parent progress record, and the decision Draft.
- **Readback:** Pending.
- **Checks:** Repository source review only. No scripts, tests, lint, or hosted CI review.
- **Limitations:** The audit establishes the content and contradictions in the retrieved branch files. It does not establish hosted validation results or client-side skill-loader behavior.

## 7. Completion

- **Status:** Not Done
- **Completed at:** Not applicable
- **Completion basis:** Draft DRAFT-0006 is read back and presented for an explicit user decision. Implementation remains outside this child.

## 8. Hosted Validation

Conditional: CI remediation only.

- **Status:** Not reviewed
- **Run URL:** Not reviewed

## 9. Handoff

Present DRAFT-0006 for approval. If the user approves its exact revision and scope, promote it to an accepted ADR, then create a separate implementation child linked to that ADR. Do not implement the proposed refactor before that gate passes.

## 10. Ledger Findings

No CI finding is assigned to this decision-preparation task.
