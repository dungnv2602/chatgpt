# Subtask: Consolidate Document Standards into The Worker

**Template version:** 1.5

## Metadata

- **ID:** 20261127-102301-01
- **Parent Task ID:** 20261127-102301
- **Type:** Implementation
- **Status:** Paused
- **Priority:** P1
- **Origin:** User
- **Approval:** Approved
- **Approval scope/source:** User approval to template-first workflow correction and explicit request to consolidate Document Standards into The Worker.
- **Governing ADR(s):** None
- **Dependencies:** None
- **Eligibility / deferral reason:** Paused — partial consolidation committed; finishing remaining catalog and index reconciliation after the current P0 queue.
- **Required:** Yes
- **Created:** 2026-11-27 UTC
- **Updated:** 2026-11-27 UTC
- **Ledger group:** None
- **Legacy Task IDs:** 20261127-102301-01

## 1. Original Prompt

> Approve
>
> Consolidate document skill into the Worker

## 2. Subsequent Instructions

- **2026-11-27:** The user requires reading the applicable template before modifying any document. Confirm this rule is explicit in the Worker, not only in Document Standards.

## 3. Objective and Scope

Consolidate document-format governance and template-first execution guidance into The Worker. Remove redundant standalone Document Standards skill activation and maintenance, while preserving required catalog, coverage, schema, validator, and owner-specific responsibilities where necessary.

## 4. Acceptance Criteria

1. The Worker explicitly requires retrieving and reading the applicable canonical template, schema, or embedded contract before editing any document.
2. Document classification, template-first authoring, migration, catalog/coverage maintenance, generator/schema ownership, and validation boundaries are consolidated without losing material requirements.
3. Standalone Document Standards skill activation and maintenance are removed or repurposed after dependency/index/catalog references are reconciled.
4. Skill index, session-start instructions, catalog references, owner workflows, and coverage rules are updated consistently.
5. Redundant governance is removed while responsibilities and limits remain explicit.
6. All changed paths are committed and remotely read back. No unobserved validation is claimed.

## 5. Decisions and Progress

- **Action:** Consolidated template-first gate and governance requirements into The Worker. Replaced the standalone Document Standards skill body with a redirect stub; retained catalog and validator assets. Removed separate skill activation from session start and index references, and updated task board and parent child index.
- **Result:** Remote readback confirms the Worker gate, redirect stub, README, session-start, board, and child index updates. Further reconciliation of catalog/owner references and final closeout remains.
- **References:** `.agent/skills/the-worker/SKILL.md`; `.agent/skills/document-standards/SKILL.md`; `.agent/skills/document-standards/references/document-type-catalog.md`; `.agent/skills/README.md`; `.agent/SESSION_START.md`.
- **Next:** Reconcile remaining catalog references and task-board structure, commit, and read back.

## 6. State and Evidence

- **Commit SHA:** Multiple commits; see consolidation commits in this conversation
- **Changed paths:** `.agent/skills/the-worker/SKILL.md`; `.agent/skills/README.md`; `.agent/SESSION_START.md`; `.agent/skills/document-standards/SKILL.md`; `workspace/task_board.md`; parent subtask index; `workspace/discussion.md`
- **Readback:** Readback confirmed updated Worker, redirect, README, session start, board, and child index
- **Checks:** Not performed
- **Limitations:** No hosted CI results will be inspected.

## 7. Completion

- **Status:** Not Done
- **Completed at:** Not applicable
- **Completion basis:** Not applicable

## 8. Hosted Validation

- **Status:** Not reviewed
- **Run URL:** Not reviewed

## 9. Handoff

Complete the template-first enforcement and consolidate document governance into The Worker. Reconcile all references and catalog rules. Read back committed files; do not inspect hosted CI.

## 10. Ledger Findings

| Finding ID | Severity | Diagnostic | Evidence |
|---|---|---|---|
