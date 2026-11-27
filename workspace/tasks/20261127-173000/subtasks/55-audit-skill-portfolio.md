# Subtask: Audit the skill portfolio and identify refactoring priorities

**Template version:** 1.5

## Metadata

- **ID:** 20261127-173000-55
- **Parent Task ID:** 20261127-173000
- **Type:** Analysis
- **Status:** In Progress
- **Priority:** P0
- **Origin:** User
- **Approval:** Approved
- **Approval scope/source:** Explicit instruction to proceed with the persistent Refactor Skills task.
- **Governing ADR(s):** None — repository audit only. Any decision-dependent implementation requires its own accepted ADR.
- **Dependencies:** None
- **Eligibility / deferral reason:** In Progress — selected as the next Refactor Skills deliverable under the user's explicit instruction.
- **Required:** Yes
- **Created:** 2026-11-27 17:35 UTC
- **Updated:** 2026-11-27 17:35 UTC
- **Ledger group:** None
- **Legacy Task IDs:** None

## 1. Original Prompt

> Then proceed to the task "refactor skills"

## 2. Subsequent Instructions

The full user instruction, including the report-format correction and `/start` cue, is preserved in the parent task's Subsequent Instructions.

## 3. Objective and Scope

Audit the active Agent Skills portfolio and define the next evidence-based refactoring sequence.

Review every skill's name, description, purpose, activation, ownership, dependencies, references, scripts, and assets. Identify duplicate responsibilities, conflicting instructions, unnecessary specialist skills, unclear activation boundaries, stale references, and gaps in the loading hierarchy.

Keep The Worker as the sole owner of cross-cutting repository operations. Do not merge distinct specialist capabilities merely to reduce the skill count. Preserve conditional initialization and user-defined activation cues.

Record findings and recommendations in this task. Create separate child subtasks for distinct implementation deliverables. Prepare a Draft and wait for user approval when a recommendation changes accepted policy or architecture.

## 4. Acceptance Criteria

1. Inventory every active skill directory and its frontmatter.
2. Map each skill's responsibility, activation condition, owner, and dependencies.
3. Identify overlap, duplication, contradictions, stale references, and missing dependencies with exact repository paths.
4. Distinguish verified repository facts from interpretation and recommendations.
5. Produce a sequenced refactoring plan with scope, risks, dependencies, and expected outcomes.
6. Identify decision-dependent changes and keep them out of implementation until the user approves the required Draft and ADR.
7. Read back the completed audit and record the commit and limitations.

## 5. Decisions and Progress

- **Execution:** P0 and Approved under the user's explicit instruction to continue Refactor Skills.
- **Method:** Inspect repository files remotely. Do not run local scripts, tests, or lint. Do not inspect hosted CI results.
- **Boundary:** Audit first. Do not mass-edit skills or change activation policy without an approved task and, where required, an accepted ADR.

## 6. State and Evidence

- **Commit SHA:** Not committed.
- **Changed paths:** This task record and its parent indexes.
- **Readback:** Pending.
- **Checks:** Not performed.
- **Limitations:** No local validation or hosted CI review.

## 7. Completion

- **Status:** Not Done
- **Completed at:** Not applicable
- **Completion basis:** Not applicable

## 8. Hosted Validation

Not applicable.

## 9. Handoff

Complete the skill inventory and responsibility map. Then recommend the next implementation child. Do not modify unrelated skills during the audit.

## 10. Ledger Findings

Not applicable. This task does not remediate a CI finding.
