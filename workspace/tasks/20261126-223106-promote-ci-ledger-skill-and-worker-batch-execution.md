# Task: Promote CI Ledger governance into a task-activated skill and define Worker-owned P0 batch execution

## Metadata

- **Template version:** 1.3
- **ID:** 20261126-223106
- **Created:** 2026-11-26 22:31 UTC
- **Updated:** 2026-11-26 22:35 UTC
- **Priority:** P1
- **Status:** In Progress
- **Origin:** User
- **Approval:** Approved
- **Governing ADR(s):** None — skill and operating-policy consolidation
- **Current execution:** No
- **Dependencies:** None
- **Related tasks:** None
- **Ledger group:** None
- **Archived:** No

## 1. Original Request

Assess if CI Ledger should be promoted to become a skill.

## 2. Subsequent Instructions

- **2026-11-27:** User approved promoting CI Ledger into an independent, task-activated skill.
- **2026-11-27:** User approved placing batch execution of CI-generated P0 tasks in The Worker, not the Ledger or GitHub Actions skill.

## 3. Objective

Promote CI Ledger finding governance, intake, identity, task generation, lifecycle, evidence, and retirement rules into a task-activated Agent Skill. Add Worker-owned orchestration policy for batch execution of eligible CI-generated P0 tasks.

## 4. Requirements

- Create `.agent/skills/ci-ledger/SKILL.md`.
- Keep Ledger activation task-scoped and absent from baseline initialization.
- Retain the Worker as task selection, task-record, task-board, execution-sequencing, and closeout authority.
- Retain GitHub Actions as CI diagnosis, remediation, recurrence prevention, workflow, and validation authority.
- Consolidate contradictory task-intake/approval rules into a coherent skill policy.
- Keep triage README concise and focused on the data contract, schema, paths, and policy navigation.
- Add Worker-owned batch execution rules, including authorization gates, sequential execution, dependency/conflict handling, task continuity, and deferred results-review.
- Update skill index and document-type catalog references.
- Preserve the existing Ledger ingestion/publication architecture. Do not redesign scripts, schema, or workflows.
- Commit and read back all changed files. Do not run or poll CI results.

## 5. Decisions

- CI Ledger is an independent task-activated skill.
- Batch orchestration of Ledger-generated CI P0 tasks is owned by The Worker.
- GitHub Actions owns technical CI remediation procedure, not batch orchestration.
- Results-review remains user-triggered after the batch's remediation commits.

## 6. Progress Log

### 2026-11-26 22:31 UTC

- **Action:** Created the CI Ledger skill and consolidated Worker batch orchestration. Simplified the triage README and integrated skill discovery and catalog references.
- **Result:** Core policy changes are committed. Index integration and read-back verification remain.
- **References:** `.agent/skills/ci-ledger/SKILL.md`, `.agent/skills/the-worker/SKILL.md`, `.takeout/reports/triage/README.md`, `.agent/skills/README.md`, `.agent/skills/document-standards/references/document-type-catalog.md`.
- **Next:** Read back all changed paths, reconcile any defects, and verify commits.

### 2026-11-26 22:34 UTC

- **Action:** Created `.agent/skills/ci-ledger/SKILL.md`, added Worker batch orchestration, simplified the triage README, integrated the skill index and catalog, and reconciled the board entry.
- **Result:** Changes committed. Read-back checks confirmed core sections. A board duplicate was detected and corrected. Final exact-path verification remains.
- **References:** Commits `36afbf6`, `4ef2dce`, `5f8e356`, `fefb388`, `31ed6bb`, `ddfeb09`, `535aa8e`.
- **Next:** Verify exact contents, link integrity, and task-board state. Update the task and register.

### 2026-11-26 22:35 UTC

- **Action:** Read back the final skill, Worker, GitHub Actions skill, Ledger README, skill index, document catalog, board, and task record from branch `gpt`.
- **Result:** Manual checks passed for skill metadata and scope, Ledger task handoff and lifecycle sections, Worker-owned sequencing and deferred-review boundary, GitHub Actions technical-only scope, README navigation, skill discovery, catalog entry, and board indexing. The board lists this task only under In Progress. Hosted CI and official skill validation were not run or reviewed.
- **References:** `.agent/skills/ci-ledger/SKILL.md`, `.agent/skills/the-worker/SKILL.md`, `.agent/skills/github-actions/SKILL.md`, `.takeout/reports/triage/README.md`, `.agent/skills/README.md`, `.agent/skills/document-standards/references/document-type-catalog.md`, `workspace/task_board.md`. Commits: `36afbf6`, `4ef2dce`, `5f8e356`, `fefb388`, `31ed6bb`, `ddfeb09`, `535aa8e`, `c43a75a`, `9aea617`.
- **Next:** Update the discussion register and retain this task pending deferred validation review.

## 7. Current State

The new CI Ledger skill and Worker batch-execution procedure are committed. The triage README, skill index, and document catalog were updated. Task-board indexing was reconciled. Read-back verification is in progress.

## 8. Remaining Work

- Verify all changed paths and the task board.
- Check links and policy consistency.

## 9. Next Actions

1. Verify the final board and changed-file read-back.
2. Record verification and commit references.
3. Update the discussion register.

## 10. References

- `.agent/skills/the-worker/SKILL.md`
- `.agent/skills/github-actions/SKILL.md`
- `.takeout/reports/triage/README.md`
- `.takeout/reports/triage/ledger.json`

## 11. Verification

- **Check:** Manual skill, policy, reference, index, catalog, and task-board consistency.
- **Method:** Exact-path fetch and read-back through GitHub API on branch `gpt`.
- **Result:** Passed. Read-back confirmed required sections, links, task-activated discovery, the Worker-owned batch procedure, and the board's single In Progress entry.
- **Limitations:** The official Agent Skills validator and linter were not run. Hosted CI results remain deferred and were not inspected.

## 12. Handoff Instructions

Finish the approved consolidation. Preserve CI ingestion and publication behavior. Do not poll, dispatch, rerun, or inspect hosted CI results after commit. Keep this task open until later validation is reviewed if required.

## 13. Ledger Findings

_Not applicable._
