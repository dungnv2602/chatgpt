# ADR-0008 Task Validation Interfaces

The Worker owns the task-validation policy and contract interfaces. GitHub Actions consumes these files. It does not own them.

## Source-of-truth files

- `.agent/skills/the-worker/assets/task-validation/task-validation-policy.json` defines the mandatory validation set, coordinator binding, terminal outcomes, and protection requirements.
- `.agent/skills/the-worker/assets/task-validation/task-validation-contract.schema.json` defines additive task-specific checks pinned to one 40-character source commit SHA.
- `.agent/skills/the-worker/assets/task-validation/task-validation-adapters.json` is the closed registry of supported typed verifier adapters.
- `.agent/skills/the-worker/scripts/build_task_validation_contract.py` resolves the source commit's Task-ID trailer and builds its exact-SHA contract.
- `.agent/skills/the-worker/scripts/task_validation.py` validates and executes registered task checks without shell strings.
- `.agent/skills/the-worker/scripts/aggregate_task_validation.py` classifies the complete exact-SHA check set.

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

The protected policy names the coordinator job IDs used by the aggregate workflow. The three existing reusable workflows now accept the exact source SHA and skip legacy publication in coordinator mode. Their direct-push report pipeline remains intact until the privileged publisher and report migration are ready. No hosted validation result is claimed.

## Reusable workflow-call interface

The three existing validation workflows expose `workflow_call` with `coordinator_call` and required `source_sha` inputs. Coordinator calls check out the exact supplied SHA. They skip legacy report publication and diagnostics jobs. Their direct push triggers retain the existing report pipeline and validation behavior. The coordinator grants only `contents: read`, so a called job cannot obtain a write-capable token even where its direct-push mode retains a write permission declaration.

The coordinator is defined as a reusable workflow in `.github/workflows/task-validation.yml`. It binds the source SHA and policy blob SHA, resolves the task contract from the source commit's Task-ID trailer, calls the three established validation workflows and the generic verifier, then aggregates their results. The generic verifier is `.github/workflows/task-validation-verifier.yml`. The coordinator has no push trigger yet. Its activation is staged until the privileged publisher and report migration are ready. This preserves the legacy push-report pipeline and prevents duplicate validation cycles. The publisher and recovery lifecycle remain separate downstream work. Do not claim publication or operational recovery until that work is complete.

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

The schema and registry are interfaces for the generic verifier. They do not themselves execute or validate a contract. The verifier must independently enforce adapter registration, path containment, argument constraints, resource limits, and fail-closed rejection.

## Protection prerequisite

A file in the repository is not self-protecting. GitHub branch protection or a ruleset must require review for changes to the policy, schema, adapter registry, Worker authority, task-contract templates, verifier and aggregate scripts/tests, and coordinator/reusable workflows. The policy records these required paths as an external prerequisite. Effective protection has not been established or verified. Do not enable the coordinator until the repository's effective ruleset has been verified.

## Security boundary

- Validation and verifier jobs must receive no secrets and no write-capable token.
- Task-supplied values are untrusted data, not executable instructions.
- The publisher must be a separate, narrowly permissioned workflow/job and must not execute task code.
- The coordinator must bind source SHA, policy blob SHA, check-set identity, run ID, and attempt before aggregation.
- No source-validation trigger may be created by metadata-only publication commits.

## Implementation state

The coordinator, generic verifier, and exact-SHA aggregate are implemented as repository files. Their runtime behavior has not been demonstrated. GitHub branch protection remains an external prerequisite and is unverified. The publisher, recovery sweep, durable checkpoint, Worker feedback lifecycle, and report-tree retirement remain incomplete. `.takeout/reports/` and all existing report producers/consumers remain intact pending the later migration and confirmation gates.
