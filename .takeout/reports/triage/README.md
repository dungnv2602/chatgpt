# CI Ledger data and navigation

The CI Ledger tracks distinct findings from lint reports and GitHub Actions diagnostics. It stores active finding state, bounded evidence references, stable parent-task links, resolution history, and separate hosted-validation metadata. The Ledger does not execute remediation. It creates Proposed work-target parent folders with CI remediation subtasks. One parent represents one affected file or workflow; each stable remediation group is a child. P0 is priority, not execution approval. A CI remediation is resolved on a verified fix commit. Hosted validation is separate metadata.

## Ownership

- **CI Ledger skill:** `.agent/skills/ci-ledger/SKILL.md` — finding governance, intake, identity, eligibility, evidence, task generation and linkage, lifecycle, resolution, recurrence retention, reset, and integrity.
- **The Worker:** task selection, authorization, batch orchestration, task records, board, progress, and closeout.
- **GitHub Actions skill:** technical CI diagnosis, remediation, recurrence prevention, workflow operations, and validation.
- **Data:** `ledger.json`.
- **Schema:** `ledger-schema.json` (version 1.6.0).
- **Generator:** `scripts/ledger.py`.
- **Regression tests:** `scripts/test_ledger.py`.

## Data contract

The data file stores:

- `schema_version` and `updated_at_utc`.
- `findings`: distinct finding records, including identity, source family, category, title, lifecycle status, severity, owner, first/last observation, cumulative occurrence count, bounded evidence, resolution, resolution history, duplicate relationship, accepted risk, task references, and task grouping.
- `ingestion_state`: processed report paths, lint baseline flags by scope, pending capture state, and other generator-managed ingestion metadata.

Finding IDs and report paths are stable references. Evidence rows retain the source report path, run URL, observation time, source-run identity, and concise note. The generator owns the structured format and schema validation. It rejects malformed index identities and missing indexed complete reports, leaves incomplete Actions captures retryable, and returns non-zero when report processing errors occur.

## Task and archive lifecycle

- Every task folder contains `task.md` and `subtasks/README.md`. Child records live under `subtasks/`.
- The Ledger creates one parent per affected file or workflow and one typed CI remediation child per stable finding group. It never creates standalone per-rule, per-step, or per-finding CI tasks.
- `task_refs` stores parent IDs, `subtask_refs` stores child IDs, and `legacy_task_refs` preserves IDs retired during hierarchy migration.
- The Ledger stores stable parent Task IDs in `task_refs`. It does not store child subtask IDs there.
- The Worker closes a parent only after every required subtask is Done and the complete folder archive is verified.
- New task archives include the parent, subtask index, and every child record. Index every exact file path with one shared UTC timestamp. Cleanup retains and deletes the folder as one unit.
- Historical flat task archives remain immutable and readable. Do not convert them.
- The Ledger resolves retained prior task archives through exact paths in the retention index. It reads both folder archives and historical flat task files. It does not scan archive directories.
- When recurrence creates a new parent, the Ledger links any retained prior archive in Related tasks. It keeps prior task references even after archive retention expires.
- Archiving never removes terminal finding identities, resolution history, or prior task references. New evidence can reopen the same finding identity.


## Report navigation

- [Report-family index](../README.md)
- [Lint reports](../lint_reports/README.md)
- [GitHub Actions diagnostics](../gh_ac_reports/README.md)
- [CI Ledger skill](../../../.agent/skills/ci-ledger/SKILL.md)
- [GitHub Actions skill](../../../.agent/skills/github-actions/SKILL.md)
- [The Worker](../../../.agent/skills/the-worker/SKILL.md)

## Operating boundary

Read the CI Ledger skill for all operational rules. Do not modify source reports or Ledger state outside the approved generator/publication flow. Do not scan historical report directories, backfill reports, or reset the Ledger without explicit authorization. Do not run scripts or tests locally.
