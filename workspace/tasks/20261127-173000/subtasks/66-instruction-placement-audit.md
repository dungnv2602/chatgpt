# Subtask: Instruction placement audit and stale-content prevention

**Template version:** 1.6

## Metadata

- **ID:** 20261127-173000-66
- **Parent Task ID:** 20261127-173000
- **Type:** Implementation
- **Status:** Ready
- **Priority:** P0
- **Origin:** User
- **Approval:** Approved
- **Approval scope/source:** User's explicit request in this conversation to create these two subtasks under Refactor Skills.
- **Governing ADR(s):** None
- **Dependencies:** None
- **Eligibility / deferral reason:** Ready — execution cue pending for the prepared batch
- **Required:** Yes
- **Created:** 2026-11-28 15:00 UTC
- **Updated:** 2026-11-28 15:00 UTC
- **Ledger group:** None
- **Legacy Task IDs:** None

## 1. Original Prompt

Scan all file contents, especially contents inside README.md files in the repo, assess and relocate what should be put into skills, what should be put into the Worker. The goal is to eliminate and prevent stale instructions and relocate what should belong to the workflow process but was wrongly put outside, be it a file or content inside a document. And suggest how to prevent this happen again in the future.

## 2. Subsequent Instructions

- **2026-11-28:** Task captured under the persistent Refactor Skills parent. Approval records scope; the standalone case-insensitive `execute` cue is still required to begin implementation.

## 3. Objective and Scope

Perform a repository-wide content audit, with particular attention to README files, for procedural instructions, duplicated operational rules, outdated instructions, misplaced workflow policy, and skill-specific content. Relocate content to The Worker or the appropriate skill/reference owner and replace secondary copies with concise pointers where appropriate. Propose prevention mechanisms.

## 4. Acceptance Criteria

1. Inventory repository file contents and README documents, identify instruction-like content, duplication, stale or conflicting rules, and ownership violations.\n2. Classify each actionable instruction by canonical owner (Worker, specific skill/reference, template, catalog, or pointer-only location).\n3. Relocate and reconcile content with minimal disruption and preserve non-instructional README purpose.\n4. Reconcile links, indexes, templates, and affected documents after relocation.\n5. Propose and implement (within scope) drift-prevention mechanisms such as ownership boundaries, template/README audits, structural validation, or review gates.\n6. Commit and read back changes. Provide an audit summary, prevention proposal/implementation, evidence, and remaining limitations.

## 5. Decisions and Progress

- **Decision:** Preserve the request and its scope as this child. Do not begin implementation until the explicit standalone execution cue authorizes the prepared batch.
- **Progress:** Task record prepared from the canonical subtask template.

## 6. State and Evidence

- **Commit SHA:** Not committed
- **Changed paths:** Task record, parent subtask index, task board, parent task tracking
- **Readback:** Pending commit
- **Checks:** Not performed
- **Limitations:** This record captures scope only; implementation and repository audit remain pending.

## 7. Completion

- **Status:** Not Done
- **Completed at:** Not applicable
- **Completion basis:** Not applicable

## 8. Hosted Validation

- **Status:** Not reviewed
- **Run URL:** Not reviewed

## 9. Execution self-check

- Canonical template consulted: `.agent/skills/the-worker/assets/SUBTASK_TEMPLATE.md`.
- Parentage confirmed: Refactor Skills.
- Scope and acceptance criteria recorded.
- Execution authorization cue: pending.

## 10. Handoff

Await the explicit standalone `execute` cue. Upon authorization, perform the scope audit autonomously, and reconcile records and evidence.

## 11. Ledger Findings

| Finding ID | Severity | Diagnostic | Evidence |
|---|---|---|---|
