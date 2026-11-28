# Subtask: Prevent Worker skill-governance drift

**Template version:** 1.6

## Metadata

- **ID:** 20261127-173000-65
- **Parent Task ID:** 20261127-173000
- **Type:** Implementation
- **Status:** In Progress
- **Priority:** P1
- **Origin:** User
- **Approval:** Approved
- **Approval scope/source:** User approved the prevention plan: enforce a fail-closed Worker ownership gate, extend catalog validation to governed non-Markdown artifacts, add mandatory automated checks, and add regression tests. Execution was authorized by the standalone cue “Execute” on 2026-11-28.
- **Governing ADR(s):** ADR-0008 (implementation architecture context)
- **Dependencies:** None
- **Eligibility / deferral reason:** Eligible — In Progress, selected as Current Execution; dependencies and authorization satisfied
- **Required:** Yes
- **Created:** 2026-11-28 10:33 UTC
- **Updated:** 2026-11-28 10:41 UTC
- **Ledger group:** None
- **Legacy Task IDs:** None

## 1. Original Prompt

> Approve. This still doesn't satisfy me. How do you prevent the case you didn't respect skills standard?

## 2. Subsequent Instructions

- **2026-11-28 (approval timestamp unavailable):** “Approve”
- **2026-11-28 (clarification timestamp unavailable):** “Do you create a new task for this after my cue?”
- **2026-11-28 10:33:34 UTC:** “Execute”

The approved scope is the prevention plan stated in the assistant response immediately before approval. Approval records scope. The standalone execution cue authorizes implementation.

## 3. Objective and Scope

Prevent future repository work from bypassing the Agent Skill Authoring standard or Worker document-governance process. Correct the ADR-0008 policy and contract placement mistake. Establish procedural, structural, automated, and regression controls.

This child belongs to the persistent Refactor Skills parent because it materially revises Worker skill governance and its supporting validator. It also supports the ADR-0008 implementation parent by correcting the ownership and validation architecture. Do not move ADR-0008 implementation files or weaken its accepted security requirements.

In scope:

- Add a mandatory, fail-closed pre-creation ownership and placement decision to The Worker.
- Make the Agent Skill Authoring workflow's template-first and ownership checks explicit in the relevant procedure.
- Move Worker-owned task-validation policy, schema, adapter configuration, and explanatory instructions into canonical Worker skill locations.
- Keep GitHub Actions workflow definitions under `.github/workflows/`.
- Extend the document catalog and validator to cover explicitly governed non-Markdown artifacts.
- Add regression tests for valid and invalid locations, missing registrations, duplicates, unknown artifact types, stale paths, and workflow exemptions.
- Ensure the document-standards workflow runs the expanded regression suite and validator for relevant changes.
- Reconcile references, indexes, and task tracking.

Out of scope:

- Changing ADR-0008's validation semantics, security model, or terminal outcomes.
- Claiming external branch protection or ruleset enforcement without evidence.
- Running local repository scripts, tests, or lint, or inspecting, dispatching, polling, or waiting for hosted CI.
- Deleting or retiring `.takeout/reports/`.

## 4. Acceptance Criteria

1. The Worker requires explicit owner, document type, canonical location, and format-source checks before any repository artifact is created or moved.
2. The gate clearly distinguishes canonical ownership from runtime consumption. Worker-owned policy and contracts reside in the Worker skill. GitHub workflow definitions remain in `.github/workflows/`.
3. Agent Skill Authoring and Worker instructions do not conflict or duplicate policy unnecessarily. The Worker remains the operational authority.
4. The document catalog registers the governed non-Markdown artifact families and their canonical owners and allowed locations.
5. The validator fails closed for unregistered governed artifacts, incorrect locations, duplicate canonical contracts, stale canonical references, and unknown governed types. It accepts legitimate GitHub workflow files.
6. Regression tests cover positive and negative cases, including the original JSON-under-`.github/` failure mode.
7. The document-standards workflow invokes the regression suite and validator for all relevant changes without weakening existing coverage.
8. All changed files, local references, and task indexes are read back from branch `gpt`. The task records unperformed validation honestly.
9. No external protection, hosted validation, or runtime behavior is claimed without direct evidence.

## 5. Decisions and Progress

### 2026-11-28 — task captured and activated

- **Action:** Created this child under the persistent Refactor Skills parent.
- **Reason:** The deliverable materially changes Worker skill governance and the document catalog validator.
- **Approval:** The user approved the four-part prevention plan. The standalone “Execute” cue authorized implementation.

### 2026-11-28 — task identity correction

- **Action:** Corrected the child ID from 64 to 65 after inspecting the persistent parent history.
- **Reason:** Child 64 had already been used and closed. Its record had been deleted under the parent lifecycle, so the empty index did not indicate that the ID was available.
- **Tracking limitation:** The first implementation commits were created with the reused Task-ID trailer `20261127-173000-64`. Git history is immutable. The record, index, and board now use the correct ID 65. Subsequent commits use the corrected Task-ID trailer. The earlier commits remain valid content evidence but have incorrect task attribution.

### 2026-11-28 — implementation progress

- **Ownership:** Moved the policy, schema, and adapter registry into `.agent/skills/the-worker/assets/task-validation/`. Moved the explanatory guide into Worker references. Removed the old duplicate files from `.github/`.
- **Worker gate:** Made canonical ownership and allowed placement mandatory before creating or moving any repository artifact. Clarified that consumer paths do not establish ownership.
- **Authoring standard:** Added an explicit Worker document-governance prerequisite before writing skill-owned artifacts.
- **Catalog and validator:** Added explicit coverage for all non-Markdown files under `.agent/skills/` and `.github/`. Each current file maps to exactly one registered artifact family, owner, and placement rule.
- **Regression coverage:** Added positive and negative cases for correct placement, misplaced GitHub policy, unregistered files, duplicate rules, unknown artifact types, stale owners, invalid suffixes, path traversal, stale rules, and valid workflow exemptions.
- **Workflow:** Expanded the document-standards push path filter to include all of `.github/**`. The workflow already runs the catalog regression suite and validator.
- **Tracking:** Updated ADR-0008 subtask 01 with the current canonical locations. The prior paths remain historical provenance.

## 6. State and Evidence

- **Commit SHA:** Latest task-specific commit pending final readback.
- **Changed paths:** Worker skill, Agent Skill Authoring skill, document-type catalog, catalog validator and tests, Worker asset index, task-validation JSON assets and reference guide, document-standards workflow, ADR-0008 subtask 01, task index, and task board.
- **Readback:** All implementation paths and the deleted old paths have been read back or verified. Final branch-head and task-tracking readback remain.
- **Checks:** JSON syntax and repository-tree path/owner/placement coverage were checked through remote reads. Repository tests, scripts, lint, and hosted workflow results were not run or inspected.
- **Limitations:** Branch protection or ruleset enforcement remains an external prerequisite and has not been established. No runtime behavior or hosted validation success is claimed. Initial commits carry the reused child-64 trailer as documented above.

## 7. Completion

- **Status:** Not Done
- **Completed at:** Not applicable
- **Completion basis:** Not applicable

## 8. Hosted Validation

- **Status:** Not reviewed
- **Run URL:** Not reviewed

## 9. Execution self-check

- Canonical instruction owner: The Worker.
- Task-specific standard: Agent Skill Authoring.
- Repository writing standard: ASD-STE100 repository policy.
- Parentage: Persistent Refactor Skills parent, confirmed by its explicit standing scope.
- Approval: User approved the defined prevention scope.
- Execution cue: Standalone “Execute” received.
- Dependencies: None identified.
- Conflict check: Preserve ADR-0008 semantics and all existing validation coverage.
- Verification: Remote branch readback only. Do not run local scripts, tests, or lint.
- Cleanup: Do not delete canonical report evidence or unrelated files.

## 10. Handoff

Complete final reference and task-index reconciliation. Verify the branch head and all changed paths. Record the unperformed checks and external protection limitation. Close the child under the persistent Refactor Skills lifecycle after readback.

## 11. Ledger Findings

| Finding ID | Severity | Diagnostic | Evidence |
|---|---|---|---|
| None | — | No findings attributed yet | — |
