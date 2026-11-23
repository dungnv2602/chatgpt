# Central CI issue ledger

The Ledger is the Worker's event-driven active backlog for distinct lint and GitHub Actions findings. It deduplicates observations, keeps bounded evidence references, creates grouped Worker task records for actionable findings, and retires terminal findings after their linked task archives are verified. It does not execute remediation.

## Finding identity and eligibility

- Lint findings use stable fingerprints. The same finding in both lint scopes maps to one Ledger entry.
- Actions findings use workflow identity, job, step, category, and normalized diagnostic text.
- A workflow conclusion alone does not create a finding. The report must contain an independently classified issue.
- Only complete post-run Actions reports contribute findings. Pre-finalizer captures do not create issues.
- Routine successful runs and cancellation-only runs are not captured by default. A successful run with an independently failed non-blocking step can create a finding. A cancelled run can contribute an independent failure; cancellation and downstream status propagation do not.
- Skipped, neutral, queued, in-progress, and unavailable states do not create findings by themselves.
- Lint task eligibility is based on comparisons with a complete, tooling-valid baseline. Low and informational findings remain Ledger-only.

## Ingestion and publication

The generator reads report paths only from the published lint and Actions indexes. It does not scan report history directories or modify source reports. The capture action ingests lint reports; the diagnostics sweep ingests complete Actions reports and handles archived-task retirement. Both use the non-cancelling `gh-ac-report-writer` concurrency group.

The caller's diagnostics jobs remain job-level `continue-on-error: true` so diagnostic reporting cannot change the source workflow result. Individual composite-action steps do not suppress failures. The scheduled archive-retention cleanup and lint report publishers use the same shared writer group. Workflow jobs that hand off to diagnostics do so sequentially; the lock is released between jobs.

Task and Ledger publication updates the report indexes, Ledger, task files, task board, and `task_refs` atomically within the existing commit/rebase/push flow. Diagnostics ignores Ledger-only, task-board-only, discussion-only, and report-archive-only pushes to avoid loops. It must not ignore `archive/tasks/**` or `.github/archive-retention-index.json`, because indexing a Done task archive is the event that retires its terminal findings.

## Lint baseline and flood control

Each lint scope has its own baseline flag in `ingestion_state.lint_baseline_scopes`.

1. After an explicit clean reset, the first complete full audit in each scope is used as a baseline only. It is marked processed but does not create findings or tasks.
2. A baseline is accepted only when the report is complete, has the expected full-audit mode and commit SHA, and all report-tooling regression checks pass. A Failed lint conclusion is still a valid baseline when the tooling checks pass; lint violations alone do not force another full audit.
3. Later reports use the generator's new/recurring comparison. A genuinely new finding can enter the Ledger. A recurring finding refreshes evidence only when the same finding is already tracked. An untracked recurring finding from the baseline is ignored, preventing the clean start from flooding the task board.
4. If a report is incomplete or its required tooling checks fail, it does not seed the baseline and is not marked processed. The changed-document workflow falls back to another full audit until a valid baseline exists.

The changed-document workflow selects the latest complete tooling-valid report commit as its baseline, not the last successful GitHub Actions conclusion. Lint findings can make the workflow conclusion Failed while the report and baseline remain valid.

## Evidence and bounded state

Evidence rows contain the immutable report path, run URL, observation time, source-run identity, and a concise note. Keep at most five evidence rows per finding: the first observation and the four most recent distinct report paths. Preserve cumulative `occurrence_count`, `first_seen_utc`, and `last_seen_utc` independently of the evidence window.

`ingestion_state.processed_reports` contains only paths still present in active report indexes. The indexes define the active reporting period; archived reports are not rescanned or backfilled.

## Finding lifecycle and task creation

Statuses are:

`open`, `investigating`, `planned`, `fixing`, `verifying`, `resolved`, `accepted`, `false_positive`, and `duplicate`.

New findings start `open`. Severity defaults are:

- Lint hard and advisory-free: `medium`; advisory: `low`; unknown: `informational`.
- Blocking Actions issue with high confidence: `high`; medium confidence: `medium`; low confidence: `low`.
- High-confidence non-blocking Actions issue: `medium`.

Humans may adjust severity when evidence supports the change. The generator preserves human-managed status, owner, severity, resolution, accepted risk, duplicate relationship, and task approval fields.

- An `accepted` finding requires an `accepted_risk` record.
- A `false_positive` finding requires a non-empty `closure_note`.
- A `duplicate` finding requires a different existing `duplicate_of` finding ID.
- A `resolved` finding requires a fix commit, successful relevant validation run URL, validation timestamp, and resolution timestamp.
- New evidence may reopen a resolved finding and preserve its previous resolution in `resolution_history`.

## Worker task handoff

Task creation is part of report ingestion, not a later manual review step.

1. Create tasks only for newly identified actionable findings with severity `medium`, `high`, or `critical` and a task-eligible status. Do not create tasks from the initial full-audit baseline or from untracked recurring baseline findings.
2. Group lint findings by source file and rule. Group Actions findings by workflow path, job, step, and category.
3. Render each task from `workspace/TASK_TEMPLATE.md`. New tasks start Assistant-originated and Proposed, add one row to `workspace/task_board.md`, and record the task ID in each finding's `task_refs`.
4. Reuse an active task for the same remediation group. Later evidence refreshes a linked task but does not create duplicate proposals.
5. Automated task creation is an intake and handoff only. It does not approve source changes or authorize remediation.
6. Task records contain finding IDs, concise diagnostics, and report links, not copied logs or full occurrence histories.

Keep finding state separate from task state: use finding status `planned` when a Ready task exists, `fixing` during remediation, and `verifying` while hosted validation is pending.

## Task resolution and Ledger retirement

The Worker must not close a Ledger-generated task as Done while any finding in its Ledger Findings section remains non-terminal.

When a task is ready to close:

1. Record the required terminal state for every linked finding. `resolved` requires fix and validation evidence; `accepted` requires risk acceptance; `false_positive` requires a closure note; `duplicate` requires a valid target.
2. Move the evidence files needed by the archived task record to `archive/reports/`, update report-family indexes, and update the task's evidence links to their archived paths. Index each exact report file for 90-day retention.
3. Archive the task as Done and register its exact archive path in `.github/archive-retention-index.json`. Keep the archived task record immutable.
4. The resulting `archive/tasks/**` push triggers the diagnostics sweep. The Ledger reads only exact task paths in the retention index. It removes linked findings from the active Ledger only when every finding in each archived Done task is terminal and every task in each finding's `task_refs` is itself archived Done.
5. Findings remain active when a task is merely Proposed, Ready, In Progress, Blocked, Paused, or Cancelled; when an archived task is not Done; or when any finding covered by the task is non-terminal.
6. Do not manually remove findings or run a periodic retirement scan. The archived task record and its archived report links preserve the historical audit trail.

New evidence arriving after a prior task is archived can reopen a previously resolved finding and create a new Proposed task when no active remediation group exists.

## Actions incomplete-capture retry policy

The diagnostics reporter retries an incomplete post-run capture no more than three times, with at least one hour between automatic attempts. Once the limit is reached, it removes the run from the pending queue and records it in `exhausted_run_ids`. An operator may submit a new explicit request after reviewing the incomplete evidence.

A manual request is consumed into `requests/processed/` after one capture result, including an incomplete result. If the capture remains incomplete and the automatic retry budget remains, the run stays in the normal pending queue; the request itself is not replayed every sweep. A complete report is never recaptured merely because a request uses force mode.

## Historical backfill and clean-start reset

Normal report rollover does not clear the Ledger or import old findings. It preserves open-finding evidence and processed state while removing old report periods from active indexes. Historical backfill requires a separate approved task.

A full clean-start reset is allowed only after an explicit user instruction. It removes active generated report payloads and all prior `archive/reports/**` content, resets the three report indexes to an empty reporting period, replaces the Ledger with no findings and no processed paths, and marks both lint baselines unseeded. It also removes report entries from the shared archive-retention index. It preserves scripts, schemas, templates, workflow definitions, operating guides, task archives, task-retention entries, and unrelated tasks.

The first complete tooling-valid full audit in each lint scope after reset establishes the new baseline without task creation. Do not backfill or taskify the prior reporting period.

## Canonical schema and tests

- Schema: `ledger-schema.json` (version `1.4.0`).
- Generator: `scripts/ledger.py`.
- Regression tests: `scripts/test_ledger.py`.
- Hosted execution: GitHub Actions. Do not run repository scripts locally.
- Task rendering regression: the lint fingerprint/idempotency test renders against the current canonical template and checks its versioned metadata.
- Baseline tests verify that the first full audit does not create findings, untracked recurring findings are ignored, and later new findings create grouped tasks.
- Evidence tests verify that evidence is bounded while occurrence counts remain cumulative.
- Retirement tests verify that terminal findings are removed only after linked task archives are indexed Done.
- Failure visibility: source-workflow diagnostics jobs remain non-blocking at job level; composite-action steps do not use step-level `continue-on-error`.
