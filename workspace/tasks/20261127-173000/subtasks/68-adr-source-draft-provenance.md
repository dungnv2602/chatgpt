# Subtask: Reconcile accepted ADR source-Draft ID provenance

**Template version:** 1.6

## Metadata

- **ID:** 20261127-173000-68
- **Parent Task ID:** 20261127-173000
- **Type:** Governance reconciliation
- **Status:** In Progress
- **Priority:** P0
- **Origin:** User-authorized Refactor Skills execution batch
- **Approval:** Approved
- **Approval scope/source:** User approved metadata correction and execution cue on 2026-11-28.
- **Governing ADR(s):** ADR-0004 and ADR-0007
- **Dependencies:** None; user decision received.
- **Eligibility / deferral reason:** In Progress — correction authorized.
- **Required:** Yes
- **Created:** 2026-11-28
- **Updated:** 2026-11-28
- **Ledger group:** None
- **Legacy Task IDs:** None

## 1. Original Prompt

Reconcile the duplicate source-Draft provenance recorded by accepted ADR-0004 and ADR-0007, both of which reference DRAFT-0005.

## 2. Subsequent Instructions

- **2026-11-28:** The Worker confirmed the accepted ADRs share the source-Draft ID DRAFT-0005. The source draft was deleted after promotion, and the ID was subsequently reused. The current record must preserve both accepted decisions without guessing which metadata reference to correct.

## 3. Objective and Scope

Resolve or formally preserve the historical source-Draft ID collision between ADR-0004 and ADR-0007. Do not alter accepted decision content. A metadata-only correction requires explicit user authorization.

## 4. Acceptance Criteria

1. Record the user's decision on whether to correct ADR-0004's source-Draft metadata or retain the collision with a durable explanatory reference.
2. Apply only the authorized metadata/reference correction. Preserve both accepted decisions and their approved content.
3. Reconcile the ADR index, task records and discussion register.
4. Read back the changed paths and record commit evidence and limitations.

## 5. Decisions and Progress

- **Decision:** Correct ADR-0007 source Draft metadata to the newly assigned DRAFT-0008, documenting that this is an administrative provenance correction and retaining the original approval scope. Do not alter ADR-0004.
- **Authorization:** User: “Correct the metadata. Execute.” This is a provenance issue, not permission to alter accepted ADR metadata.
- **Progress:** The Worker now checks Draft IDs against Draft files, accepted ADR source-draft metadata, task records, indexes and discussion before assigning an ID. The operational gate prevents new reuse but does not resolve this historical collision.

## 6. State and Evidence

- **Commit SHA:** Not committed
- **Changed paths:** Accepted ADR metadata/references, index and task tracking only after decision
- **Readback:** Not performed
- **Checks:** Not performed
- **Limitations:** User decision is required before correction.

## 7. Completion

- **Status:** Not Done
- **Completed at:** Not applicable
- **Completion basis:** Not applicable

## 8. Hosted Validation

- **Status:** Not reviewed
- **Run URL:** Not reviewed

## 9. Execution self-check

- Canonical subtask template consulted.
- Parentage confirmed.
- Approval and execution authority are pending.
- The task remains Proposed and cannot execute until the user decision and a fresh standalone `execute` cue.

## 10. Handoff

Present the exact provenance conflict and ask for the user's choice at batch quiescence. Do not change accepted ADR metadata without authorization.

## 11. Ledger Findings

| Finding ID | Severity | Diagnostic | Evidence |
|---|---|---|---|
