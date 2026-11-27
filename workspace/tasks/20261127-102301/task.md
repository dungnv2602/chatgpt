# Task: Consolidate Document Standards into The Worker

## Metadata

- **Template version:** 2.6
- **ID:** 20261127-102301
- **Created:** 2026-11-27 10:23 UTC
- **Updated:** 2026-11-27 10:23 UTC
- **Priority:** P1
- **Status:** Paused
- **Origin:** User
- **Approval:** Approved
- **Approval scope/source:** User approval to template-first workflow correction and explicit request to consolidate Document Standards into The Worker.
- **Governing ADR(s):** None
- **Current execution:** No
- **Dependencies:** None
- **Eligibility / deferral reason:** Paused — partial consolidation committed; deferred behind the active P0 queue.
- **Related tasks:** None

## 1. Original Request

> Approve
>
> Consolidate document skill into the Worker

## 2. Subsequent Instructions

- **2026-11-27:** Before modifying a document, read its applicable template first.
- **2026-11-27:** Corrected parentage. This objective is independent of CI remediation and must not be nested under its CI task parent.

## 3. Objective and Acceptance Criteria

Consolidate document-format governance and template-first execution guidance into The Worker, removing redundant standalone activation while retaining supporting catalog, coverage, schema, validator, and owner responsibilities.

1. Worker mandates template-first document editing.
2. Document-format classes, migration, catalog/coverage, schema/generator ownership and validation limits are retained.
3. Standalone activation and maintenance are removed or redirected.
4. References, catalog and coverage rules are reconciled.
5. Changed files are committed and remotely read back. No unobserved validation is claimed.

## 4. Decisions

- Catalog and validator remain supporting assets, not a separate activated skill.
- This task is Paused behind the active P0 queue.

## 5. Progress

- Partial consolidation commits already exist. Remaining reconciliation is tracked in child 01.

## 6. Current State and Remaining Work

The template-first gate, skill index, session-start and redirect stub are committed. Catalog and remaining references need reconciliation.

## 7. Verification and Evidence

- **Commit SHA:** Existing consolidation commits, as referenced in child 01
- **Changed paths:** As recorded in child 01
- **Readback:** Existing partial readback; completion readback pending
- **Checks:** Not performed
- **Limitations:** No hosted CI review.

## 8. Handoff

Finish child 01 after the active P0 queue. Preserve partial work and read back every change.

## 9. Subtasks

Canonical index: [subtasks/README.md](subtasks/README.md).

## 10. Ledger Findings

| Finding ID | Severity | Diagnostic | Evidence |
|---|---|---|---|
