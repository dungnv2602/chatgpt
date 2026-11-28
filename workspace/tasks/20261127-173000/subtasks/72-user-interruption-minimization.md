# Subtask: Enforce user-interruption minimization and report-at-quiescence

**Template version:** 1.6

## Metadata

- **ID:** 20261127-173000-72
- **Parent Task ID:** 20261127-173000
- **Type:** Implementation
- **Status:** In Progress
- **Priority:** P0
- **Origin:** User
- **Approval:** Approved
- **Approval scope/source:** User request on 2026-11-28: “Read the workflow again the not bothering me part. Reinforce it to force you to follow”
- **Governing ADR(s):** None
- **Dependencies:** None
- **Eligibility / deferral reason:** Eligible — Ready, dependencies and authorization satisfied
- **Required:** Yes
- **Created:** 2026-11-28 22:00 UTC
- **Updated:** 2026-11-28 22:00 UTC
- **Ledger group:** None
- **Legacy Task IDs:** None

## 1. Original Prompt

“Read the workflow again the not bothering me part.

Reinforce it to force you to follow”

## 2. Subsequent Instructions

None.

## 3. Objective and Scope

Strengthen The Worker’s canonical execution and blocker discipline so the assistant protects the user's solitude, autonomously carries authorized work to quiescence, and only interrupts for a consolidated set of material user-resolvable blockers or decisions. Apply directly to the Worker execution loop; avoid duplicating policy in secondary documents.

## 4. Acceptance Criteria

1. Canonical Worker rules explicitly prohibit unsolicited progress pings, routine status messages, and interrupting the user for isolated/recoverable blockers or routine decisions.
2. The workflow requires autonomous recovery, independent-work continuation, batching genuine decisions/blockers, and reporting only at quiescence or when a materially urgent issue truly requires intervention.
3. Explicit execution cue, scope, approval, and safety/authority constraints remain unchanged.
4. Read back the modified canonical instruction and tracking records.

## 5. Decisions and Progress

- Reinforce the canonical execution loop rather than adding redundant instructions elsewhere.

## 6. State and Evidence

- **Commit SHA:** Not committed
- **Changed paths:** The Worker; task record; subtask index; task board
- **Readback:** Pending
- **Checks:** No local scripts/tests/lint; no hosted CI review
- **Limitations:** Readback establishes committed text only.

## 7. Completion

- **Status:** Not Done
- **Completed at:** Not applicable
- **Completion basis:** Not applicable

## 8. Hosted Validation

- **Status:** Not reviewed
- **Run URL:** Not reviewed

## 9. Execution self-check

Map-first initialization performed. Scope and approval confirmed. This task advances the persistent skills-refactoring parent. Execution authorization explicit. Readback and tracking reconciliation required.

## 10. Handoff

Complete canonical Worker reinforcement, reconcile index and board, read back, then close and delete the child under lifecycle rules.

## 11. Ledger Findings

None.
