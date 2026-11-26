# Task: Promote CI Ledger governance into a task-activated skill and define Worker-owned P0 batch execution

## Metadata

- **Template version:** 1.3
- **ID:** 20261126-223106
- **Created:** 2026-11-26 22:31 UTC
- **Updated:** 2026-11-26 22:31 UTC
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

- **Action:** Recorded approved implementation scope after assessment.
- **Result:** Skill ownership and Worker batch-execution placement approved. Existing README contains conflicting task-generation authorization language that will be reconciled during consolidation.
- **References:** `.agent/skills/the-worker/SKILL.md`, `.agent/skills/github-actions/SKILL.md`, `.takeout/reports/triage/README.md`.
- **Next:** Implement the Ledger skill, update owning references and Worker orchestration, then read back each commit.

## 7. Current State

Implementation is approved and in progress. Baseline and task-activated documentation standards were retrieved.

## 8. Remaining Work

- Implement skill and Worker procedure.
- Update README, indexes, and catalog.
- Commit and read back all changed paths.

## 9. Next Actions

1. Write the CI Ledger skill and reconcile triage README policy.
2. Update The Worker, skill index, and document-type catalog.
3. Read back and verify all changes and commits.

## 10. References

- `.agent/skills/the-worker/SKILL.md`
- `.agent/skills/github-actions/SKILL.md`
- `.takeout/reports/triage/README.md`
- `.takeout/reports/triage/ledger.json`

## 11. Verification

- **Check:** Repository file read-back.
- **Method:** GitHub API on branch `gpt`.
- **Result:** Pending.
- **Limitations:** Hosted validation will not be reviewed in this phase.

## 12. Handoff Instructions

Finish the approved consolidation. Preserve CI ingestion and publication behavior. Do not poll, dispatch, rerun, or inspect hosted CI results after commit. Keep this task open until later validation is reviewed if required.

## 13. Ledger Findings

_Not applicable._
