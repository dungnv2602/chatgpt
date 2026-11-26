# Subtask: Ledger task generation and governance handoff

## Metadata
- **ID:** 20261126-232913-02
- **Parent:** [20261126-232913](../task.md)
- **Type:** Implementation
- **Status:** Ready
- **Priority:** P0
- **Approval:** Approved
- **Governing ADR:** [ADR-0004](../../../adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md)
- **Created:** 2026-11-26 23:29 UTC
- **Updated:** 2026-11-26 23:29 UTC
- **Required:** Yes

## Objective
Make Ledger-generated task folders, CI subtasks, task refs, task discovery, board links, and governance states consistent.

## Acceptance Criteria
1. Generate a parent task folder and typed CI remediation subtask for each eligible grouped finding.
2. Ledger `task_refs` identify stable parent Task IDs.
3. Generated implementation tasks remain Proposed with Governing ADR(s) Pending until Worker review and accepted ADR linkage.
4. Folder task discovery and task.md board links work.
5. New P0 generation preserves valid Worker-selected Current Execution.
6. Regression tests cover folder generation, task_refs, governance gating, and current-task preservation.

## Progress
- **Current state:** Ready; blocked only by subtask 01's canonical folder and lifecycle contract.
- **Evidence:** None recorded.
- **Completion record:** Not Done. Record commit SHA and verification evidence on completion.

## Handoff
Do not mark generated tasks Approved or In Progress merely because the Ledger creates them. Keep Worker authorization separate from finding generation.
