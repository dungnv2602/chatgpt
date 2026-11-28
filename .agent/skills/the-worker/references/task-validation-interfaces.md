# ADR-0008 Task Validation Interfaces

The Worker owns the task-validation policy and contract interfaces. GitHub Actions consumes these files. It does not own them.

## Source-of-truth files

- `.agent/skills/the-worker/assets/task-validation/task-validation-policy.json` defines the mandatory validation set, coordinator binding, terminal outcomes, and protection requirements.
- `.agent/skills/the-worker/assets/task-validation/task-validation-contract.schema.json` defines additive task-specific checks pinned to one 40-character source commit SHA.
- `.agent/skills/the-worker/assets/task-validation/task-validation-adapters.json` is the closed registry of supported typed verifier adapters.

The policy file's Git blob SHA is the immutable policy revision for a coordinator attempt. The numeric `policy_revision` is a human-managed schema revision and is not a substitute for binding the blob SHA.

## Ownership and execution boundary

The Worker skill owns operational policy, machine-readable contracts, schemas, and adapter registries. Store those files in the owning skill's `assets/` directory. Store their explanatory procedures in `references/` and their executable tools in `scripts/`.

Store GitHub Actions workflow definitions in `.github/workflows/`. A workflow's consumption of a policy file does not transfer ownership of that policy to `.github/`. Do not place Worker-owned contracts in a workflow directory or a neighboring GitHub configuration path.

## Mandatory validation coverage

The initial manifest preserves the three existing required validation families:

| Policy ID | Existing workflow | Existing job ID | Coverage |
|---|---|---|---|
| `ste-lint-changed` | `ste-lint-changed.yml` | `ste-lint` | Changed-document lint, report tooling tests, and incremental/full-audit fallback |
| `ste-lint-full-docs` | `ste-lint-full-docs.yml` | `ste-lint` | Full technical-document audit and report tooling tests |
| `validate-document-standards` | `validate-document-standards.yml` | `validate-document-standards` | Document catalog, structural ownership, and existing Ledger regression tests |

This is an initial mapping, not a claim that the workflows have already been migrated or that the job identifiers are confirmed as stable aggregate check names. The downstream workflow migration must preserve the existing scripts, test cases, path coverage, and baseline behavior, then establish stable names for aggregation.

## Reusable workflow-call interface

The three existing validation workflows now expose `workflow_call` and accept the optional boolean input `coordinator_call`. The full-document workflow uses this input to bypass its direct-push supersession cancellation logic when invoked by the coordinator.

**Do not wire the coordinator to these entry points yet.** At this stage, the legacy workflows still contain report publication and write-capable jobs, and some paths check out the branch name rather than the immutable caller SHA. Subtask `20261128-230000-02` must first make the reusable entry points exact-SHA and validation-only, separate publication into the privileged publisher, and preserve existing validation semantics. Until then, invoking them from the coordinator would not satisfy ADR-0008's security boundary.

## Task contract constraints

A task contract:

- must identify the exact source commit SHA;
- may add checks but cannot remove, rename, or override policy-mandated checks;
- may select only adapter identifiers registered in `task-validation-adapters.json`;
- carries a repository-relative entrypoint and an argument array, never a shell command string;
- cannot define environment overrides, credentials, permissions, or arbitrary executables.

The schema and registry are interfaces for the generic verifier. They do not themselves execute or validate a contract. The verifier must independently enforce adapter registration, path containment, argument constraints, resource limits, and fail-closed rejection.

## Protection prerequisite

A file in the repository is not self-protecting. GitHub branch protection or a ruleset must require review for changes to the policy, schema, adapter registry, and coordinator workflow. The policy records this as an external prerequisite; protection has not been established by these commits. Do not treat the policy as protected until the repository's effective ruleset has been verified.

## Security boundary

- Validation and verifier jobs must receive no secrets and no write-capable token.
- Task-supplied values are untrusted data, not executable instructions.
- The publisher must be a separate, narrowly permissioned workflow/job and must not execute task code.
- The coordinator must bind source SHA, policy blob SHA, check-set identity, run ID, and attempt before aggregation.
- No source-validation trigger may be created by metadata-only publication commits.

## Implementation state

This is the interface foundation only. No coordinator, verifier, publisher, exact-SHA aggregate, runtime protection, or operational confirmation is claimed here. `.takeout/reports/` and all existing report producers/consumers remain intact pending the later migration and confirmation gates.
