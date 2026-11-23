# Central CI issue ledger

The ledger is the authoritative backlog of distinct lint and GitHub Actions findings. It deduplicates observations and links each finding to immutable source reports. It does not create workspace tasks.

## Finding identity and eligibility

- Lint findings use stable fingerprints. The same finding in both lint scopes maps to one ledger entry.
- Actions findings use workflow identity, job, step, category, and normalized diagnostic text.
- A workflow conclusion alone does not create a finding. The report must contain an independently classified issue.
- Only complete post-run Actions reports contribute findings. Pre-finalizer captures do not create issues.
- Routine successful runs and cancellation-only runs are not captured by default. A successful run with an independently failed non-blocking step can create a finding. A cancelled run can contribute an independent failure; cancellation and downstream status propagation do not.
- Skipped, neutral, queued, in-progress, and unavailable states do not create findings by themselves.

Evidence records contain the immutable report path, run URL, observation time, and source-run identity. Occurrence counts use unique source attempts. The same lint fingerprint in both scopes counts once per run.

## Ingestion

The generator reads paths from the lint and Actions indexes. It does not scan history directories or modify source reports. The capture action ingests lint reports; the diagnostics sweep ingests complete Actions reports. Both use the non-cancelling `gh-ac-report-writer` concurrency group.

The ledger uses schema `1.2.0`. GitHub-hosted Actions runs the generator and regression tests. Ingestion is idempotent, uses atomic replacement, and preserves human-managed status, owner, severity, resolution, accepted risk, duplicate links, and `task_refs`. Initial bootstrap marks indexed reports as processed; it does not backfill historical findings.

## Finding lifecycle

Statuses:

`open`, `investigating`, `planned`, `fixing`, `verifying`, `resolved`, `accepted`, `false_positive`, `duplicate`.

New findings start `open`. Severity defaults are:

- Lint hard and advisory-free: `medium`; advisory: `low`; unknown: `informational`.
- Blocking Actions issue with high confidence: `high`; medium confidence: `medium`; low confidence: `low`.
- High-confidence non-blocking Actions issue: `medium`.

Humans may adjust severity when evidence supports the change. An `accepted` finding requires an `accepted_risk` record. A `duplicate` finding requires a different existing `duplicate_of` ID.

A `resolved` finding requires a fix commit, a successful relevant validation run URL, validation timestamp, and resolution timestamp. When new evidence observes a resolved finding, ingestion reopens it and preserves the previous resolution in `resolution_history`.

## Worker handoff

The Worker owns prioritization, task creation, execution, and task closeout.

1. Review findings only when the user asks, a known failure blocks current work, or the current task requires CI evidence. Do not run periodic triage or poll workflows.
2. Inspect the finding's report and exact evidence. Do not create tasks from conclusion-only, cancellation-only, or routine successful outcomes.
3. Group related findings by remediation. Check the board and active tasks to avoid duplicate work or one-task-per-occurrence.
4. Record every covered finding ID and evidence link in the task. Add that task ID to each finding's `task_refs`.
5. Keep finding state separate from task state: use `planned` when the task is Ready, `fixing` during remediation, and `verifying` while hosted validation is pending.
6. Follow the Worker's approval rules. One task may cover several findings. The approved handoff process does not authorize unrelated changes, weaker tests, or automatic remediation.
7. Resolve findings only after recording the fix commit and successful validation. The run URL and UTC timestamp are sufficient; a full successful-run report is unnecessary. New evidence may reopen the finding.

Ledger ingestion never creates tasks or overwrites human-managed fields. The Worker does not copy diagnostic payloads or occurrence history into task records; it links to that evidence.

## Historical backfill

Do not clear `ingestion_state.processed_reports` or import every old report as a new issue. Historical backfill requires a separate approved task. Review identity rules, deduplicate observations, and preserve every evidence reference.

## Canonical schema and tests

- Schema: `ledger-schema.json`.
- Generator: `scripts/ledger.py`.
- Regression tests: `scripts/test_ledger.py`.
- Hosted execution: GitHub Actions. Do not run repository scripts locally.