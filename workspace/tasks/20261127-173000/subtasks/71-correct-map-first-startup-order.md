# Subtask: Correct map-first startup order

**Template version:** 1.6

## Metadata

- **ID:** 20261127-173000-71
- **Parent Task ID:** 20261127-173000
- **Type:** Implementation
- **Status:** In Progress
- **Priority:** P0
- **Origin:** User
- **Approval:** Approved
- **Approval scope/source:** User's explicit Execute following request to correct startup order so the Workflow Map is read first for overview, before The Worker.
- **Governing ADR(s):** None
- **Dependencies:** None
- **Eligibility / deferral reason:** Eligible — Ready, dependencies and authorization satisfied
- **Required:** Yes
- **Created:** 2026-11-28 15:00 UTC
- **Updated:** 2026-11-28 15:00 UTC
- **Ledger group:** None
- **Legacy Task IDs:** None

## 1. Original Prompt

> The order is wrong, read the map first for overview. Fix it.

## 2. Subsequent Instructions

### 2026-11-28

> Execute

Authorization for this scoped implementation.

## 3. Objective and Scope

Correct the canonical startup sequence and map diagram so the Workflow Map is read for overview immediately after the Session Start cue guard, before The Worker or related references are loaded. Update relevant tracking.

## 4. Acceptance Criteria

1. Session Start explicitly routes /start to read the map before The Worker.
2. The Workflow Map diagram reflects that order.
3. The Worker initialization orchestration matches the canonical map-first sequence.
4. Read back changed owner documents and tracking.

## 5. Decisions and Progress

Correction scope is the startup-order contradiction in Session Start and the map, plus Worker orchestration wording for consistency. Do not expand scope into unrelated startup gates.

## 6. State and Evidence

- **Commit SHA:** Pending
- **Changed paths:** Pending
- **Readback:** Pending
- **Checks:** Not performed
- **Limitations:** No local tests/scripts/lint or hosted CI inspection.

## 7. Completion

- **Status:** Not Done
- **Completed at:** Not applicable
- **Completion basis:** Not applicable

## 8. Hosted Validation

- **Status:** Not reviewed
- **Run URL:** Not reviewed

## 9. Execution self-check

Map-first scope approved by explicit execute cue. Remote repository work only. Preserve unrelated unresolved work and prior verification boundaries.

## 10. Handoff

Correct order, reconcile map and owners, read back, and close this child under the persistent parent lifecycle.

## 11. Ledger Findings

| Finding ID | Severity | Diagnostic | Evidence |
|---|---|---|---|
| None | None | None | None |
