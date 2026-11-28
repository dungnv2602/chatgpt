# Subtask: Enforce execution-cue and decision-logging gates

**Template version:** 1.6

## Metadata

- **ID:** 20261127-173000-63
- **Parent Task ID:** 20261127-173000
- **Type:** Implementation
- **Status:** In Progress
- **Priority:** P0
- **Origin:** User
- **Approval:** Approved
- **Approval scope/source:** Explicit user instruction and execution cue in this conversation.
- **Governing ADR(s):** None
- **Dependencies:** None
- **Eligibility / deferral reason:** Eligible — approved and no dependencies
- **Required:** Yes
- **Created:** 2026-11-28 00:51 UTC
- **Updated:** 2026-11-28 00:51 UTC
- **Ledger group:** None
- **Legacy Task IDs:** None

## 1. Original Prompt

> My only cue for your execution is "execute", exclude the rest. And "approve" means log my approval, doesn't mean you're allowed to execute right away.
>
> Add one more thing, my cue is case-insensitive.

## 2. Subsequent Instructions

- **2026-11-28:** User explicitly stated **Execute**. The cue is case-insensitive. This authorizes the scope of this subtask.

## 3. Objective and Scope

Tighten The Worker so that only the case-insensitive, explicit execution cue `execute` authorizes execution. Approval, decision-navigation cues, and other instructions must be recorded or routed without triggering execution. Update related templates and tracking records.

## 4. Acceptance Criteria

1. Worker defines the sole execution cue, case-insensitive matching, and clear exclusions.
2. Approval is recorded but cannot itself trigger execution.
3. Decision navigation logs the instruction, leaves the decision unanswered/blocker unresolved, and advances without execution.
4. The decision-collection phase must complete before the authorized execution batch starts.
5. Associated templates reflect these rules without duplicating operational ownership.
6. Changes are read back and tracking reconciled.

## 5. Decisions and Progress

- **Execution cue:** `execute`, case-insensitive. Explicit cue given by the user in this conversation.
- **Approval:** Record only, no execution.
- **Navigation:** `Next` is decision-queue navigation only.

## 6. State and Evidence

- **Commit SHA:** Implementation commits in progress.
- **Changed paths:** The Worker, parent/subtask templates, board template, discussion template, child index, task board, parent task, and this child record.
- **Readback:** Pending.
- **Checks:** Not performed.
- **Limitations:** No local or hosted validation.

## 7. Completion

- **Status:** Not Done
- **Completed at:** Not applicable
- **Completion basis:** Not applicable

## 8. Hosted Validation

- **Status:** Not reviewed
- **Run URL:** Not reviewed

## 9. Execution self-check

Canonical Worker authority and task template verified. Scope explicitly approved. Parentage confirmed. No dependencies. Decision-collection semantics are part of the implementation. Readback and cleanup required.

## 10. Handoff

Implement the cue gate in The Worker, associated templates, and active tracking records; read back and close out.

## 11. Ledger Findings

| Finding ID | Severity | Diagnostic | Evidence |
|---|---|---|---|
