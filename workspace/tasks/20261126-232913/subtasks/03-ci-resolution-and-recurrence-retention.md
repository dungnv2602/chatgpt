# Subtask: Commit-based CI resolution and recurrence retention

## Metadata
- **ID:** 20261126-232913-03
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
Commit-based CI resolution and recurrence retention as part of the accepted ADR-0004 implementation.

## Acceptance Criteria
1. Allow resolved findings with a verified remediation commit and resolved timestamp without requiring successful hosted validation.
2. Represent hosted validation separately as optional, schema-validated metadata.
3. Make CI subtask Done require verified intended-branch commit SHA and remediation summary.
4. Retain terminal finding identity and resolution history after task archival; remove destructive retirement behavior.
5. On recurrence, preserve prior resolution history and append new parent task references without invalidating old remediation records.
6. Add regression tests for commit-only resolution, validation states, recurrence, and archive retention.

## Progress
- **Current state:** Ready; follow the execution order in the parent subtask index.
- **Evidence:** None recorded.
- **Completion record:** Not Done. Record commit SHA(s), changed paths, and verification evidence on completion.

## Handoff
Execute only this subtask's scope. Record meaningful changes and evidence here and in the parent task. Do not mark Done until every acceptance criterion passes.
