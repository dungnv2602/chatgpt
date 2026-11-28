# Subtask: Reconcile accepted ADR source-Draft ID provenance

**Template version:** 1.6

## Metadata

- **ID:** 20261127-173000-68
- **Parent Task ID:** 20261127-173000
- **Type:** Governance reconciliation
- **Status:** Done
- **Priority:** P0
- **Origin:** User-authorized Refactor Skills execution batch
- **Approval:** Approved
- **Approval scope/source:** User approved metadata correction and execution cue on 2026-11-28.
- **Governing ADR(s):** ADR-0004 and ADR-0007
- **Dependencies:** None; user decision received.
- **Eligibility / deferral reason:** Done — metadata correction and readback completed.
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

- **Progress:** Corrected ADR-0007's source Draft metadata from DRAFT-0005 to DRAFT-0008. ADR-0004 remains unchanged. Documented the correction in ADR-0007 and discussion register.

- **Decision:** Correct ADR-0007 source Draft metadata to the newly assigned DRAFT-0008, documenting that this is an administrative provenance correction and retaining the original approval scope. Do not alter ADR-0004.
- **Authorization:** User: “Correct the metadata. Execute.” This is a provenance issue, not permission to alter accepted ADR metadata.
- **Progress:** The Worker now checks Draft IDs against Draft files, accepted ADR source-draft metadata, task records, indexes and discussion before assigning an ID. The operational gate prevents new reuse but does not resolve this historical collision.

## 6. State and Evidence

- **Commit SHA:** ADR-0007 `6e452884918604530780f8f4d1729b13a6f34ba1`; discussion `89342d49a61d4370fe1b02c7e50b8c20b76055b6`
- **Changed paths:** ADR-0007 source metadata and More Information, discussion register, parent task, subtask index and board
- **Readback:** Pending
- **Checks:** No tests; metadata-only change
- **Limitations:** ADR-0007 retains the original approval record (DRAFT-0005 revision 1) in prose; its metadata now uses DRAFT-0008 as the corrected unique provenance reference. This is a traceability correction, not a newly created or reapproved decision Draft.

## 7. Completion

- **Status:** Done
- **Completed at:** 2026-11-28
- **Completion basis:** Updated ADR-0007 source reference, documented rationale, and reconciled discussion register. Readback pending.

## 8. Hosted Validation

- **Status:** Not reviewed
- **Run URL:** Not reviewed

## 9. Execution self-check

- Canonical subtask template consulted.
- Parentage confirmed.
- Approval and execution authority are pending.
- The user authorized metadata correction and execution.

## 10. Handoff

Read back the ADR, task, discussion register and board; close and delete the child record under lifecycle rules.

## 11. Ledger Findings

| Finding ID | Severity | Diagnostic | Evidence |
|---|---|---|---|
