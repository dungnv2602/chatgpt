# ADR-0008 Task Validation Interfaces

The Worker owns the task-validation policy and contract interfaces. GitHub Actions consumes these files. It does not own them.

## Source-of-truth files

- `.agent/skills/the-worker/assets/task-validation/task-validation-policy.json` defines the mandatory validation set, coordinator binding, terminal outcomes, and protection requirements.
- `.agent/skills/the-worker/assets/task-validation/task-validation-contract.schema.json` defines additive task-specific checks pinned to one 40-character source commit SHA.
- `.agent/skills/the-worker/assets/task-validation/task-validation-adapters.json` is the closed registry of supported typed verifier adapters.
- `.agent/skills/the-worker/scripts/build_task_validation_contract.py` resolves the source commit's Task-ID trailer and builds its exact-SHA contract.
- `.agent/skills/the-worker/scripts/task_validation.py` validates and executes registered task checks without shell strings.
- `.agent/skills/the-worker/scripts/aggregate_task_validation.py` classifies the complete exact-SHA check set.
- `.agent/skills/the-worker/scripts/publish_task_validation.py` atomically publishes one status record and review folder per eligible terminal attempt.
- `.agent/skills/the-worker/scripts/recover_task_validation.py` performs paginated Actions-run recovery, artifact recovery, checkpoint advancement, and three-day pruning.
- `.agent/skills/the-worker/assets/task-validation/task-validation-status-index.schema.json` defines the compact status index and checkpoint.
- `.agent/skills/the-worker/assets/task-validation/task-validation-lifecycle.schema.json` defines the per-task Validation Lifecycle block. The task templates include this block; legacy records without it are not backfilled.
- `.agent/skills/the-worker/assets/task-validation/task-validation-review-template.md` defines generated per-attempt review records.

The policy file's Git blob SHA is the immutable policy revision for a coordinator attempt. The numeric `policy_revision` is a human-managed schema revision and is not a substitute for binding the blob SHA.

## Ownership and execution boundary

The Worker skill owns operational policy, machine-readable contracts, schemas, and adapter registries. Store those files in the owning skill's `assets/` directory. Store their explanatory procedures in `references/` and their executable tools in `scripts/`.

Store GitHub Actions workflow definitions in `.github/workflows/`. A workflow's consumption of a policy file does not transfer ownership of that policy to `.github/`. Do not place Worker-owned contracts in a workflow directory or a neighboring GitHub configuration path.

## Mandatory validation coverage

The manifest preserves the three existing required validation families and adds the generic verifier:

| Policy ID | Existing workflow | Coordinator job ID | Coverage |
|---|---|---|---|
| `ste-lint-changed` | `ste-lint-changed.yml` | `lint_changed` | Changed-document lint, report tooling tests, and incremental/full-audit fallback |
| `ste-lint-full-docs` | `ste-lint-full-docs.yml` | `lint_full` | Full technical-document audit and report tooling tests |
| `validate-document-standards` | `validate-document-standards.yml` | `document_standards` | Document catalog, structural ownership, and existing Ledger regression tests |
| `generic-verifier` | `task-validation-verifier.yml` | `generic_verifier` | Exact-SHA task contract validation, closed adapter enforcement, and additive task-specific checks |

The policy records each coordinator job ID and its result collection mode. Ordinary checks use the job result. The generic verifier uses its structured outcome and must return the exact source SHA, policy blob SHA, and result digest.

The protected policy names the coordinator job IDs used by the aggregate workflow. The three existing reusable workflows now accept the exact source SHA and skip legacy publication in coordinator mode. Their direct-push report pipeline remains intact until the privileged publisher and report migration are ready. No hosted validation result is claimed.

## Reusable workflow-call interface

The three existing validation workflows expose `workflow_call` with `coordinator_call` and required `source_sha` inputs. Coordinator calls check out the exact supplied SHA. They skip legacy report publication and diagnostics jobs. Their direct push triggers retain the existing report pipeline and validation behavior. The coordinator grants only `contents: read`, so a called job cannot obtain a write-capable token even where its direct-push mode retains a write permission declaration.

The coordinator is defined as a reusable workflow in `.github/workflows/task-validation.yml`. It binds the source SHA and policy blob SHA, resolves the task contract from the source commit's Task-ID trailer, calls the three established validation workflows and the generic verifier, aggregates their results, and calls the isolated publisher as a separate job. The dispatcher is `.github/workflows/task-validation-dispatch.yml`; its push trigger is gated by explicit policy activation and verified protection, and it suppresses duplicate first-attempt dispatches for an already-published source SHA. The generic verifier is `.github/workflows/task-validation-verifier.yml`. Activation remains staged until publisher/recovery and report migration are ready. The three legacy push workflows remain active meanwhile, so no duplicate validation cycle is started.

## Per-task validation lifecycle

The task and subtask templates define a `Validation Lifecycle` JSON block governed by `.agent/skills/the-worker/assets/task-validation/task-validation-lifecycle.schema.json`. It is task-local metadata, not a second run index.

| State | Meaning | Allowed transition |
|---|---|---|
| `not_committed` | No task-specific implementation commit is awaiting validation. | `awaiting_ci` after a source commit with the exact Task-ID trailer. |
| `awaiting_ci` | The task's current source SHA and policy blob SHA are recorded; no terminal attempt has been reconciled. | `review_required` for an actionable terminal failure; `passed` for a complete exact-SHA success. |
| `review_required` | A current-SHA actionable failure needs Worker diagnosis and grouped remediation. | `reviewed` after all actionable root causes are diagnosed and linked to remediation children. |
| `reviewed` | The failure attempt is reconciled and its review folder removed; remediation children remain ordinary queued work. | `passed` only after a qualifying successful result for the exact current SHA and policy revision. |
| `passed` | The exact current SHA has a reconciled complete success. | `awaiting_ci` after a newer implementation commit. |

After a task implementation commit, the Worker updates only that task's lifecycle block in a metadata-only commit. The source SHA remains the implementation commit, not the metadata commit. The dispatcher excludes `workspace/tasks/**`, so lifecycle updates cannot create validation recursion. Do not change the ordinary task Status to a special CI status; `awaiting_ci` and related values belong only to the lifecycle block.

The Worker matches status-index attempts by all three values: exact `source_task_id`, `source_sha`, and `policy_revision`. A mismatch is stale or unattributable and cannot mutate the task. A later success does not erase earlier actionable failure work for the same source SHA. Cancelled and superseded attempts never mutate the lifecycle. The Worker, not the publisher or recovery workflow, owns task Status, remediation children, and final Done transitions.

## Status index and review queue

- The single compact status index is `workspace/task-validation/status-index.json`. Its schema is Worker-owned under `assets/task-validation/`.
- The `closed_through` tuple is the monotonic recovery checkpoint. Advance it only after every earlier attempt is accounted for and reconciled.
- The publisher uses `(coordinator_run_id, attempt)` as its idempotency key. It checks the source commit's policy blob SHA, then writes the status record and the review folder in one metadata-only commit. Concurrent push conflicts are retried with a bounded retry count.
- Review records live at `workspace/task-validation/reviews/<run-id>-<attempt>/review.md`. Cancelled and superseded attempts have status records but no review folder or feedback task.
- The index contains only source Task-ID when valid, source SHA, run ID/attempt, check-set identity, policy revision, completion time, outcome, Actions URL, and recovery metadata. Do not add findings, logs, diagnostics, evidence, remediation state, or task history.
- The task's Validation Lifecycle block stores only its latest source SHA, policy blob SHA, coordinator run/attempt, outcome, and reconciliation state. It is not an attempt history or findings store. Cancelled and superseded attempts do not mutate it.
- Worker attribution and lifecycle use the policy's `worker_lifecycle.fallback_parent_id`; the current permanent fallback parent is `workspace/tasks/20261128-193800/task.md`. This ID is not written into the status index when source attribution is absent.
- The coordinator uploads a compact aggregate artifact for recovery. The publisher workflow is `.github/workflows/task-validation-publisher.yml`; it checks out trusted branch `gpt`, executes only the Worker-owned publisher script, receives no secrets, and has contents-write permission only in its isolated publish job. It never checks out or executes task source code.
- The recovery workflow is `.github/workflows/task-validation-recovery.yml`. It runs from gpt push events, can be called after publication, and defines a 15-minute schedule. It uses paginated Actions-run metadata, aggregate artifacts, and Worker-owned task lifecycle blocks; it does not inspect logs or validate source code. When a committed task is awaiting CI but has no indexed or active attempt, recovery may request a workflow-dispatch for that exact SHA only after both source/current coordinator policies are enabled, protection is verified, and dispatcher availability on the default branch is verified. Its only write permissions are actions:write for that gated dispatch and contents:write for checkpoint/retention. Reconciled records expire three days after reconciliation; unresolved records never expire.
- The Worker writes `awaiting_ci` plus the exact source SHA and policy blob SHA into the task's Validation Lifecycle block after the source commit. Recovery compares those records with the compact index and dispatcher runs. If an attempt is missing, recovery can request an exact-SHA `workflow_dispatch` only after the source and current policies confirm coordinator activation, verified protection, and verified default-branch workflow availability.
- The repository default branch is currently `main`, while the project branch is `gpt`. GitHub requires a workflow-dispatch and scheduled workflow definition to exist on the default branch. The recovery dispatch and scheduled sweep gates are therefore external prerequisites and remain disabled until the dispatcher/recovery definitions are available there. Do not change the default branch or write to `main` without explicit user authorization.

## Recovery scheduling constraint

The repository's current default branch is `main`, while this project is maintained exclusively on `gpt`. GitHub scheduled workflows run only from the default branch, so a schedule defined only on `gpt` is not operational until the default branch changes or an external scheduler invokes the recovery workflow. The recovery workflow can still run opportunistically from `gpt` push events and after publication. Do not claim scheduled recovery is operational before that external prerequisite is met. See [GitHub's schedule event documentation](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows).

## Task contract source and binding

Every parent task and subtask declares a JSON object in the `Validation Contract` section of its canonical task record. The section contains `contract_revision` and an additive `checks` array. Use an empty array when the task requires no checks beyond repository policy.

The coordinator reads the source commit's exact `Task-ID` trailer. It resolves that ID to one task record in the same source commit tree. The Worker-owned builder rejects missing or ambiguous attribution, missing contract blocks, invalid JSON, and unsupported contract fields. It then injects the exact source SHA into the contract. The contract is therefore bound to the implementation commit without requiring a self-referential SHA in the task record.

The policy job also records the policy file's Git blob SHA. The generic verifier checks the source SHA and policy blob SHA against its exact checkout. It receives a read-only token, no secrets, and no persisted checkout credentials. Its typed adapters execute with `shell=False` and a restricted environment.

The coordinator aggregates every mandatory check. The generic verifier runs all task-added checks as its nested check set. Their full definitions and contract revision contribute to the aggregate check-set identity. Every mandatory result must match the source SHA, policy blob SHA, check-set identity, coordinator run ID, and attempt. Missing, duplicate, skipped, pending, partial, or mismatched results cannot produce success.

## Task contract constraints

A task contract:

- must identify the exact source commit SHA;
- may add checks but cannot remove, rename, or override policy-mandated checks;
- may select only adapter identifiers registered in `task-validation-adapters.json`;
- carries a repository-relative entrypoint and an argument array, never a shell command string;
- cannot define environment overrides, credentials, permissions, or arbitrary executables.
- may declare at most 16 checks, with no check exceeding 15 minutes or 25 aggregate minutes.

The schema and registry are interfaces for the generic verifier. They do not themselves execute or validate a contract. The verifier must independently enforce adapter registration, path containment, argument constraints, resource limits, and fail-closed rejection.

## Protection prerequisite

A file in the repository is not self-protecting. GitHub branch protection or a ruleset must require review for changes to the policy, contract/status schemas, adapter registry, review template, Worker authority, task-contract templates, verifier, aggregate, publisher and recovery scripts/tests, dispatcher, coordinator/reusable workflows, and legacy report/diagnostic producer workflows while migration remains staged. The policy records these required paths as an external prerequisite. Effective protection has not been established or verified. Do not enable the coordinator until the repository's effective ruleset has been verified.

## Security boundary

- Validation and verifier jobs must receive no secrets and no write-capable token.
- Task-supplied values are untrusted data, not executable instructions.
- The publisher must be a separate, narrowly permissioned workflow/job and must not execute task code.
- The coordinator must bind source SHA, policy blob SHA, check-set identity, run ID, and attempt before aggregation.
- No source-validation or legacy diagnostic push trigger may be created by metadata-only publication commits. The dispatcher, changed-document lint, document-standards workflow, and legacy diagnostics workflow explicitly exclude `workspace/task-validation/**`; the full-document audit is scoped to the STE-100 ruleset. The recovery workflow's push filter excludes the status index and review folders.

## Legacy report migration inventory

The legacy report tree is still live and must remain intact. This inventory separates the task-validation replacement from report producers and consumers that still require migration.

| Legacy producer / consumer | Current responsibility | Migration state |
|---|---|---|
| `.github/workflows/ste-lint-changed.yml` | Changed-document lint, baseline lookup in `.takeout/reports/index.json`, and legacy lint-report publication. | Reusable exact-SHA entry point exists and skips legacy publication in coordinator mode. Direct-push reporting remains active while coordinator activation is staged. |
| `.github/workflows/ste-lint-full-docs.yml` | Full-document lint, legacy baseline lookup, and lint-report publication. | Reusable exact-SHA entry point exists and skips legacy publication in coordinator mode. Direct-push reporting remains active while coordinator activation is staged. |
| `.github/workflows/validate-document-standards.yml` | Catalog/ownership/verifier tests and legacy Ledger regression tests. | Reusable exact-SHA entry point exists. Its Ledger regression test uses `.agent/skills/the-worker/scripts/test_ledger.py`; the obsolete report-family script path has been removed from the trigger/test configuration. |
| `.github/workflows/gh-actions-capture.yml` and `.takeout/reports/gh_ac_reports/actions/capture/action.yml` | Workflow-run capture, legacy report generation, Ledger ingestion, and report/task publication. | Still a legacy producer for non-coordinator workflow-run diagnostics. Retain coverage for unrelated workflow runs until their replacement is proven. |
| `.github/workflows/gh-actions-diagnostics.yml` | Workflow-run capture and push/manual backfill through `actions-report.py` and `ledger.py`. | Still a legacy producer and recovery path. Push backfill is policy-gated after coordinator activation; workflow-run capture remains for non-task workflows. |
| `.agent/skills/the-worker/scripts/actions-report.py`, `ledger.py`, `eligibility.py`, their schemas/templates and regression tests | Legacy report capture, classification, Ledger ingestion, and report storage. | Code is Worker-owned, but outputs and consumers still target `.takeout/reports/`. Retain until all report families and consumers have migrated. |
| `.takeout/reports/index.json`, `ledger.json`, `history/`, README, composite action | Legacy report indexes, evidence, Ledger state, and navigation. | Retained as compatibility state; no task-validation attempts or new parallel findings archive may be added. |
| `workspace/README.md`, `.agent/skills/the-worker/references/ci-ledger.md`, document catalog, ADR-0003/0007 references, and workflow path filters | Navigation, operational instructions, schemas, regression coverage, and historical report locators. | Navigation and ownership now distinguish task-validation from the legacy Ledger. Remove obsolete paths and superseded locator references only in the gated retirement phase. |

The three validation workflows already expose reusable exact-SHA entry points. Their direct-push legacy mode must not be disabled until the coordinator is enabled, protected, and demonstrated operational. The diagnostic capture workflow must continue covering unrelated non-task workflow runs until an equivalent replacement exists. Do not claim the report tree is migrated or retire it in this stage.

## Implementation state

The exact-SHA coordinator, generic verifier, aggregate artifact, gated dispatcher, isolated publisher, and run-metadata recovery sweep are implemented as repository files. Publisher and recovery regression tests are registered in document-standards CI but have not been executed by the Worker. No hosted run or publication is claimed. Recovery's committed-task-awaiting-CI reconciliation depends on Worker lifecycle metadata in subtask `20261128-230000-04`. The repository default branch is main, so the scheduled sweep cannot operate from gpt yet. Effective branch protection and publisher write access remain external prerequisites. Worker feedback lifecycle and report-tree retirement remain incomplete. `.takeout/reports/` and all existing report producers/consumers remain intact pending migration and Confirmation.
