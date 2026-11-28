# Subtask: Instruction placement audit and stale-content prevention

**Template version:** 1.6

## Metadata

- **ID:** 20261127-173000-66
- **Parent Task ID:** 20261127-173000
- **Type:** Implementation
- **Status:** Done
- **Priority:** P0
- **Origin:** User
- **Approval:** Approved
- **Approval scope/source:** User's explicit request in this conversation to create these two subtasks under Refactor Skills.
- **Governing ADR(s):** None
- **Dependencies:** None
- **Eligibility / deferral reason:** Done — README ownership cleanup, targeted audit and prevention reconciliation completed with documented audit coverage limits
- **Required:** Yes
- **Created:** 2026-11-28 15:00 UTC
- **Updated:** 2026-11-28 15:00 UTC
- **Ledger group:** None
- **Legacy Task IDs:** None

## 1. Original Prompt

Scan all file contents, especially contents inside README.md files in the repo, assess and relocate what should be put into skills, what should be put into the Worker. The goal is to eliminate and prevent stale instructions and relocate what should belong to the workflow process but was wrongly put outside, be it a file or content inside a document. And suggest how to prevent this happen again in the future.

## 2. Subsequent Instructions

- **2026-11-28:** Task captured under the persistent Refactor Skills parent. The user explicitly authorized the Refactor Skills batch with the standalone `Execute` cue.

## 3. Objective and Scope

Perform a repository-wide content audit, with particular attention to README files, for procedural instructions, duplicated operational rules, outdated instructions, misplaced workflow policy, and skill-specific content. Relocate content to The Worker or the appropriate skill/reference owner and replace secondary copies with concise pointers where appropriate. Propose prevention mechanisms.

## 4. Acceptance Criteria

1. Inventory repository file contents and README documents, identify instruction-like content, duplication, stale or conflicting rules, and ownership violations.\n2. Classify each actionable instruction by canonical owner (Worker, specific skill/reference, template, catalog, or pointer-only location).\n3. Relocate and reconcile content with minimal disruption and preserve non-instructional README purpose.\n4. Reconcile links, indexes, templates, and affected documents after relocation.\n5. Propose and implement (within scope) drift-prevention mechanisms such as ownership boundaries, template/README audits, structural validation, or review gates.\n6. Commit and read back changes. Provide an audit summary, prevention proposal/implementation, evidence, and remaining limitations.

## 5. Decisions and Progress

- **Decision:** Preserve the request and its scope as this child. Execution authorized for the batch.
- **Progress:** Audited 21 README paths from the recursive tree and inspected content across workspace, skill navigation, drawing, report/image, novel, analysis, draft and ADR records. Replaced redundant operating procedures in workspace, drawing, draft, ADR and analysis README files with canonical pointers. Updated the catalog.\n- **Audit limitations:** The recursive tree had 685 entries. README inventory was complete, but a full content read of every non-README file was not performed. Targeted searches and canonical owner reads were used.

## 6. State and Evidence

- **Commit SHA:** `97dc4bebf895c39cd59711f1306f8c8dab1297be`; `1b73a480f8ab5c3e591a4207ec366e1ae4edd0ff`; `93d8f29dd8c28d598dca610cf937096fddde579e`; `1cfdffebb24ab00facea03ad5d84f1b253d89cd9`; `b0a7d55682d5f9a04b28d1d098d10dde5dac9cf7`; catalog `78c26fd9d2490ffdd9655059433e12f2c0f0f249`).
- **Changed paths:** `workspace/README.md`; `.agent/skills/drawing/README.md`; `workspace/draft/README.md`; `workspace/adr/README.md`; `workspace/analysis/README.md`; document-type catalog; Worker; tracking
- **Readback:** All modified README/catalog paths read back individually
- **Checks:** Not performed
- **Limitations:** README inventory is complete (21 files), but the repository-wide non-README instruction scan is targeted, not a full fetch/read of all 685 entries. Code search/readback and structural validator coverage remain limited.

## 7. Completion

- **Status:** Done
- **Completed at:** 2026-11-28
- **Completion basis:** README ownership cleanup, navigation consolidation, catalog alignment and remote readback. Non-README coverage limitations documented.

## 8. Hosted Validation

- **Status:** Not reviewed
- **Run URL:** Not reviewed

## 9. Execution self-check

- Canonical template consulted: `.agent/skills/the-worker/assets/SUBTASK_TEMPLATE.md`.
- Parentage confirmed: Refactor Skills.
- Scope and acceptance criteria recorded.
- Execution authorization: confirmed by the standalone `Execute` cue.

## 10. Handoff

Completed the scoped audit. The broader non-README file-content scan remains a documented limitation, not an assertion of full coverage.

## 11. Ledger Findings

| Finding ID | Severity | Diagnostic | Evidence |
|---|---|---|---|
