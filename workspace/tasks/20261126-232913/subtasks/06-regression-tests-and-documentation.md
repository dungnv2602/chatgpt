# Subtask: Regression coverage and documentation/catalog alignment

## Metadata
- **ID:** 20261126-232913-06
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
Regression coverage and documentation/catalog alignment as part of the accepted ADR-0004 implementation.

## Acceptance Criteria
1. Update Ledger regression suite for all ADR-0004 invariants while maintaining validation/security coverage.
2. Update CI Ledger, Worker, and GitHub Actions skills to use one consistent lifecycle contract.
3. Update workspace README, triage README, templates, task board contract, and Document Type Catalog.
4. Use only repository-authorized hosted checks; do not inspect hosted results until explicit user trigger.
5. Perform remote read-back of every changed file and document unverified tests honestly.
6. Map every ADR-0004 Confirmation criterion to concrete test or repository evidence.

## Progress
- **Current state:** Ready; follow the execution order in the parent subtask index.
- **Evidence:** None recorded.
- **Completion record:** Not Done. Record commit SHA(s), changed paths, and verification evidence on completion.

## Handoff
Execute only this subtask's scope. Record meaningful changes and evidence here and in the parent task. Do not mark Done until every acceptance criterion passes.
