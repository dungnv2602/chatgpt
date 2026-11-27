# CI Ledger

The CI Ledger records lint and Actions findings, their evidence, attribution, remediation children, recurrence, and resolution. It does not schedule or execute work.

## Ownership

- [The Worker](../../../.agent/skills/the-worker/SKILL.md): task ownership, scheduling, closeout, and activation of all operational references.
- [CI Ledger reference](../../../.agent/skills/the-worker/references/ci-ledger.md): finding identity, intake, attribution, child linkage, recurrence, and integrity.
- [GitHub Actions reference](../../../.agent/skills/the-worker/references/github-actions.md): technical diagnosis, remediation, and workflow operation.

## Data

- `ledger.json`: active finding state.
- `ledger-schema.json`: current Ledger schema.
- `scripts/ledger.py`: event-driven ingestion and child generation.
- `scripts/test_ledger.py`: regression coverage.

Evidence retains the immutable report path, run URL, observation time, source task marker, resolved genuine parent when known, and attribution state. Finding IDs and report paths remain stable.

## Task hierarchy

A user task is the parent. User follow-ups and CI remediation are children. The Ledger never creates synthetic parents for files or workflows.

The source commit must contain one `Task-ID:` trailer. The Ledger resolves a parent ID directly or maps a child ID through Parent Task ID. It creates a P0, Approved, Ready CI child only under a verified active user task. Missing or invalid attribution leaves the finding visible and unassigned.

`task_refs` stores genuine parent IDs; `subtask_refs` stores child IDs; `legacy_task_refs` preserves retired references. The Ledger updates parent finding summaries and child records only. The Worker owns the board and scheduler.

## Boundaries

Read only indexed reports. Do not scan history, backfill, reset, run scripts/tests locally, or inspect hosted CI results. Clean reset and historical backfill require separate explicit authorization. Do not edit immutable source reports.


## Worker ownership and implementation locations

The Worker skill and its references govern this report family's operations. The Ledger generator, tests, schema, and shared eligibility policy are maintained under `.agent/skills/the-worker/`. Ledger state remains here. This is report data, not an independent operational owner.
