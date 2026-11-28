---
record_type: decision-draft
template_version: "1.2"
id: "DRAFT-0010"
revision: 8
status: "draft"
created: "2026-11-28"
updated: "2026-11-28"
proposed_by: "Assistant"
decision_makers:
  - "User"
consulted: []
informed: []
related_drafts: []
related_adrs:
  - "ADR-0003"
  - "ADR-0004"
  - "ADR-0007"
resulting_adr: null
promotion_cleanup_pending: false
cleanup_reason: null
---

# CI Validation, Error Tasks, and Automatic Feedback Loop

## 1. Decision summary

Adopt one commit-specific, event-driven validation lifecycle for every task. Before committing, the Worker may inspect and correct its changes. After committing, GitHub Actions is the sole authority for implementation validation: the Worker does not run tests, scripts, lint, or other post-commit correctness checks and does not override CI outcomes.

Each task declares its required validation contract. Established workflows remain preferred when they fully cover that contract. Uncovered requirements use one generic reusable verifier, called by a dispatcher. The generic verifier supports registered adapters and repository-owned scripts under a structured, protected contract; it is not an unrestricted command runner.

For each terminal aggregate validation attempt, automation publishes one minimal status record and creates one review task. The Worker reads the index first. It opens Actions logs only after a recorded check, infrastructure, coverage, or capture failure, and solely to diagnose it. CI creates no finding reports or diagnostic evidence files. The Worker creates self-contained error subtask folders from the diagnosis.

A task becomes **Done** only when the complete required check set succeeds for its exact current commit, the result is reconciled, and no required subtasks remain. A committed task enters **Committed / Awaiting CI** and the Worker immediately continues with other unblocked work.

This remains a Draft. The user has approved the component decisions recorded below, including the generic verifier's use of both adapters and repository-owned scripts. The consolidated architecture and remaining calls are presented for final decision; implementation is not authorized by this Draft.

## 2. Goals and boundaries

### Goals

- One post-commit validation authority across all task types.
- Exact-commit and exact-check-set integrity; no missing, skipped, cancelled, partial, or incomplete result can count as success.
- Reuse established workflows and use one generic reusable verifier for uncovered requirements.
- One aggregate result and one review task per validation attempt, with duplicate-delivery protection.
- No CI-authored diagnostic reports, finding documents, evidence files, findings Ledger, or parallel diagnostic archive.
- Self-contained remediation subtask folders, correct parent attribution, bounded recurrence, and deterministic late-error routing.
- Non-blocking Worker scheduling, recoverable publication, no event loss, no workflow feedback loops, and no silent deadlocks.
- Retire \`.takeout/reports/\` only after every producer and consumer has migrated and the replacement is operational.

### Non-goals

- The Worker must not run or independently score post-commit validation.
- The Worker must not inspect successful Actions logs, poll for results, dispatch or rerun validation, or wait for CI.
- CI must not create remediation folders or copy diagnostics into task records. The Worker creates remediation folders after diagnosis.
- A missing result, empty error list, or absence of a generated subtask is never proof of success.
- Do not weaken required checks, baselines, permissions, or protections to obtain a green result.
- Do not preserve a hidden findings database or diagnostic archive after migration.

## 3. Validation contract and execution

### 3.1 Task contract and trusted policy

Every task must identify its validation requirements before its implementation commit. The contract must be machine-readable and pinned to the exact source commit (or reference an immutable contract revision). It identifies required checks, named adapters or repository-relative scripts, typed arguments, working directories, dependencies/order, timeouts, and success conditions.

A protected repository policy defines mandatory checks and permitted adapters. A task contract may add checks but cannot remove, weaken, or redefine mandatory policy. Policy revision and check-set identity are recorded for each attempt. A task with no valid required check set is not eligible to become Done.

Every task-specific implementation commit carries exactly one valid \`Task-ID: <id>\` trailer. The ID must resolve to a genuine task; child IDs resolve through their parent. Missing, malformed, ambiguous, inactive, or deleted attribution is never guessed from paths, branch, workflow, timing, or Current Execution. Unattributable work is routed to the permanent fallback process.

### 3.2 Established workflows and generic fallback

- An established workflow is used when it fully covers declared requirements. Partial coverage is not full coverage.
- A thin dispatcher selects the established checks and invokes one repository-owned generic reusable workflow for uncovered requirements. A partially covered task runs both the established checks and the generic checks for the uncovered portion; do not duplicate the same required check.
- The reusable verifier is invoked through \`workflow_call\`; it cannot trigger itself. New verification needs should normally require a contract, adapter, or repository-owned script—not a cloned orchestration workflow.
- Support both registered adapters (for common test, lint, build, schema, and policy checks) and repository-owned scripts for novel checks.
- All required check results feed one aggregate coordinator. Individual job completion never creates a review task or a terminal aggregate result.

### 3.3 Generic verifier security

- Do not accept free-form shell command strings from task metadata. Use schema-validated fields, allowlisted adapter names, repository-relative script paths, and discrete typed arguments.
- Reject path traversal, invalid working directories, unsupported adapters, malformed arguments, excessive matrix sizes, and unbounded time/resource requests.
- Run verification code at the exact source SHA. Do not check out a moving branch head.
- The verifier receives no secrets and no write-capable token. Use least-privilege read-only access, pinned third-party actions, bounded time/resources, and isolated handling for fork or otherwise untrusted contributions.
- Keep the privileged status publisher in a separate job with narrowly scoped write permission. It must not execute task scripts or untrusted repository code.
- A contract requiring secrets, deployment access, elevated permissions, or an unsupported environment cannot silently use the generic path; it requires a separately reviewed established workflow or remains a non-success coverage/infrastructure outcome.
- Scripts and contracts are code under review. Protected policy, not task-authored metadata, controls the mandatory check set.

## 4. One aggregate validation cycle

### 4.1 Preferred orchestration

Use one coordinator workflow per source commit. It resolves the protected policy and exact-commit task contract, invokes required established checks and the generic verifier as reusable jobs, and aggregates their outcomes in a final job that runs even when validation jobs fail.

Established workflows used by this coordinator must expose callable entry points (or equivalent reusable jobs). Their independent triggers may remain for unrelated purposes, but they must not create duplicate task-validation cycles. The coordinator is the sole authority for the task's aggregate result.

This single-coordinator design avoids races between separate workflow completions and avoids an aggregator guessing whether another required workflow is still pending. If repository constraints prevent this design, a separately approved alternative must provide an explicit expected-check manifest, missing-check timeout, and equivalent recovery guarantees.

### 4.2 Aggregate outcomes

| Outcome | Meaning | Task effect |
|---|---|---|
| \`success\` | Every required check completed successfully for the exact SHA and policy revision. | Eligible for reconciliation to Done if no subtasks remain. |
| \`check_failure\` | At least one required check ran and failed. | Worker diagnoses the linked run and creates remediation children. |
| \`coverage_failure\` | A required check is absent, skipped unexpectedly, unsupported, or not represented in the declared set. | Never success; create coverage/infrastructure remediation. |
| \`infrastructure_failure\` | Runner, dependency, service, or orchestration infrastructure prevented reliable validation. | Never success; route infrastructure remediation. |
| \`capture_failure\` | Aggregate status or review-task publication could not be completed reliably. | Never success; recovery automation must repair publication. |
| \`cancelled\` / \`superseded\` | The attempt was cancelled or made obsolete by a newer source commit. | Never success; reconcile as stale/non-current without diagnosing obsolete logs. |

A skipped, missing, pending, partial, cancelled, or incomplete required check cannot be converted to success. A full required check set must be present for the exact SHA and policy revision. A successful result proves only that the declared checks passed, not that defects outside their coverage do not exist.

### 4.3 Exact commit, attempts, and stale results

- Each validation attempt has a unique identity based on repository, coordinator run ID, and run attempt. A rerun is a distinct attempt.
- The aggregate record identifies the exact source SHA, source Task-ID, check-set identity, protected policy revision, completion time, outcome, and direct Actions run URL.
- Results never transfer to another SHA or check-set revision.
- A result for a commit that is no longer the task's expected commit is stale. Reconcile its review task without changing the newer task state or creating obsolete remediation.
- A later successful rerun does not erase an earlier failed attempt or delete remediation already created from it. Each attempt is reconciled independently; outstanding remediation remains outstanding.
- A rerun must produce a complete required-check result. A partial rerun cannot inherit unreported checks as passing.

## 5. Publication, recovery, and loop prevention

### 5.1 Atomic, idempotent publication

For every terminal aggregate attempt, publish:
1. one minimal run-status index record; and
2. one lightweight CI-result review task folder.

Publish both in one repository commit/transaction so a review task cannot appear before its status record or vice versa. Use the run ID plus attempt as the idempotency key. Duplicate event deliveries must not create duplicate records or tasks. Do not use a concurrency arrangement that silently cancels distinct pending finalizers; handle concurrent writes with safe retry/merge semantics.

The review task contains only source Task-ID, source SHA, run/attempt identity, check-set/policy identity, index locator, Actions URL, outcome, and reconciliation instructions. It contains no copied logs, findings, signatures, or diagnostic payloads.

### 5.2 Recovery sweep

A scheduled automation reconciler repairs missed or incomplete handoffs. It checks coordinator run metadata and committed tasks awaiting validation against the status index. After a bounded trigger/publication grace period, it creates one idempotent coverage/capture-failure record and review task for a source commit whose coordinator run or publication is missing.

The sweep reads workflow/run metadata only; it does not inspect logs or validate source code. It uses a durable watermark stored with the run-status metadata, paginates safely, and advances the watermark only after all earlier events are reconciled. Repeated sweeps are idempotent. Publication retries are bounded; a persistent failure remains visibly non-success and enters infrastructure remediation rather than retrying indefinitely.

### 5.3 Prevent recursive workflows

Status-index and system-generated review-task commits are metadata-only and excluded from source-validation triggers. The publisher writes only its designated status/review paths in a separate commit. Do not rely solely on bot identity or token-specific event suppression to prevent recursion. A publisher commit must never start another validation cycle.

Do not automatically rerun failed validation. A new source commit creates a new validation cycle; any separately authorized rerun is a distinct attempt and receives its own review task.

## 6. Worker lifecycle and task queue

### 6.1 Statuses

| Status | Meaning |
|---|---|
| **In Progress** | Implementation or remediation remains. |
| **Committed / Awaiting CI** | A source commit exists; required validation and result reconciliation are pending. |
| **Blocked** | A user decision, external dependency, or infrastructure recovery prevents progress. |
| **Done** | The complete required check set succeeded for the exact current SHA, the result was reconciled, and no required subtasks remain. |

Commit alone, workflow start, one passing job, an empty index, or no generated error child is not Done. If checks fail, the source task returns to active remediation. If coverage, infrastructure, or capture fails, it remains not Done and is blocked or receives an explicit infrastructure child.

### 6.2 Non-blocking scheduling

- Immediately after committing and recording the returned SHA, set **Committed / Awaiting CI** and select the next unblocked task.
- Continue through unblocked work until none remains. Do not wait for or poll CI.
- Review tasks join the ordinary queue. A review task arriving during active work does not interrupt it; it is eligible at the next task-selection point.
- When no unblocked task remains, follow the existing blocked-task/quiescence procedure. A task awaiting an external CI event is not falsely marked Done or converted into an implementation blocker.
- Review tasks are administrative tasks and are deleted after successful reconciliation. A missing or mismatched result is not silently closed; the recovery/infrastructure path must make it visible.

### 6.3 Review behavior

The Worker always reads the status index first.

- **Success for the current exact SHA:** reconcile task state; do not open logs.
- **Check failure for the current exact SHA:** inspect the linked run solely to diagnose actionable root causes; create or update remediation children.
- **Coverage, infrastructure, or capture failure:** inspect the linked run only when needed to diagnose the failure; create the appropriate infrastructure/coverage child or block the task.
- **Stale, cancelled, or superseded attempt:** reconcile as non-current; do not inspect obsolete logs or change the current task's status.
- **Missing, incomplete, or unmatchable record:** do not mark Done; rely on recovery automation or route a visible infrastructure task.

The Worker never reruns checks, re-scores results, or changes the aggregate outcome.

## 7. Error subtask lifecycle and flood controls

- The Worker—not CI—creates one self-contained subtask folder per distinct actionable root cause, under the genuine active parent identified by the source Task-ID.
- Group multiple failing steps/jobs that share one root cause into one child. Do not create one child per log line, test assertion, rule, or repeated event.
- If a matching child is already active, update that child with the new affected paths and run/attempt references instead of creating another. Keep the matching key/fingerprint in the child folder only; never add error signatures or deduplication state to the run-status index.
- Distinct root causes remain separate children. Once a child is completed and deleted, a later recurrence is new work.
- If the source parent is still active and correctly identified, place the child there. If the parent is Done/deleted or unavailable, use one permanent fallback parent for orphaned/late errors. Never recreate a deleted original parent or infer parentage.
- Preserve in the child only what is needed to resolve it: source Task-ID, source SHA, run/attempt references, concise diagnosis, relevant log excerpts or durable Actions links, affected paths, and remediation/acceptance criteria.
- Delete a completed child folder and all its contents. Delete an ordinary parent folder only when Done and no required children remain. Never automatically delete the permanent fallback parent, even when empty.
- Each terminal aggregate attempt creates one review task, not one per job or finding. Duplicate deliveries are deduplicated. Distinct attempts remain distinct, as previously approved.

## 8. Run-status index

Keep one compact index under \`workspace/\`. It is operational run metadata, not a diagnostic or findings store.

**Allowed fields:** source Task-ID (when valid), exact source SHA, coordinator run ID and attempt, check-set identity, protected policy revision, completion timestamp, aggregate outcome, and direct Actions run URL. A recovery watermark may be stored as run-reconciliation metadata.

**Forbidden:** findings, error signatures, logs, diagnostic payloads, evidence, remediation state, copied report content, or task history.

Keep one record per validation attempt so event delivery remains idempotent and previous outcomes are not silently overwritten. Do not retain a second index, Ledger, or archive.

## 9. Migration and retirement

The exact retirement target is \`.takeout/reports/\`. Do not delete it until:
- all report producers, consumers, schemas, scripts, tests, navigation, and documentation have migrated;
- the coordinator, generic verifier, aggregate publisher, recovery sweep, status index, and review-task creation are operational;
- all required checks retain their current validation scope and baselines; and
- the replacement has demonstrated reliable success, failure, missing-event, duplicate-event, and publication-recovery behavior through GitHub Actions.

Then retire the complete \`.takeout/reports/\` tree and obsolete Ledger/report paths. Do not preserve a parallel findings archive. Preserve unrelated lint/test/workflow coverage even though report storage and report ingestion are removed.

The resulting ADR must reconcile conflicting clauses in ADR-0003, ADR-0004, and ADR-0007. Supersede only the scopes that conflict; preserve unrelated rationale and safeguards where still applicable. Update Worker policy, GitHub Actions guidance, templates, schemas, task board, Workflow Map, workspace README, and all active references in one governed migration. Do not implement policy changes before the superseding ADR is accepted.

## 10. Failure and recovery guarantees

| Failure | Required behavior |
|---|---|
| Source commit does not trigger coordinator | Recovery sweep detects the awaiting task after grace period; publishes one coverage/capture failure and review task. |
| Required workflow/job is missing or skipped | Aggregate is non-success; create coverage remediation. |
| One required check fails | Aggregate check failure; Worker diagnoses the run and creates grouped remediation children. |
| Runner/service fails | Infrastructure failure; never success. |
| Coordinator is cancelled or superseded | Record the terminal attempt; do not apply it to a newer commit. |
| Duplicate terminal event | Idempotent no-op after the first successful publication. |
| Concurrent publishers | Safe retry/merge; no lost attempt or overwritten index entry. |
| Index/review publication partially fails | Atomic publication prevents half-state; recovery sweep repairs the missing handoff. |
| Publisher repeatedly fails | Bounded retry, visible capture failure, infrastructure remediation; no infinite loop. |
| Status commit triggers validation again | Path/trigger exclusion prevents recursive execution. |
| Same error recurs while child is active | Update the existing child; do not flood the queue. |
| Original parent was deleted | Route actionable late error to permanent fallback; never recreate the original parent. |
| Actions logs have expired or are inaccessible | Do not guess; create an infrastructure task with the run locator and missing-evidence limitation. |

## 11. Implementation sequence

1. Finalize the open architecture calls below and promote this Draft through Decision Governance to a superseding ADR.
2. Inventory existing workflows and map every task/contract requirement to its current check coverage. Preserve all existing required validation scope.
3. Define the protected validation policy, contract schema, registered adapters, script interface, and trust boundary.
4. Implement the coordinator, reusable entry points for established workflows, generic verifier, exact-SHA execution, and aggregate classification.
5. Implement the isolated publisher, atomic status-index/review-task publication, idempotency, concurrency-safe writes, and recovery sweep.
6. Implement task status, review-task queue handling, error-child grouping/deduplication, active-parent routing, and permanent fallback.
7. Migrate Worker policy, templates, schemas, catalog, board, Workflow Map, README, and all active references; reconcile ADR conflicts.
8. Demonstrate success, check failure, missing/skipped checks, cancellation/supersession, duplicate delivery, concurrent publication, missed trigger, publisher failure, stale result, and recursive-trigger prevention through GitHub Actions.
9. Only after the replacement is operational, remove every \`.takeout/reports/\` producer/consumer and retire that directory.
10. Close the migration by deleting completed child folders and Done ordinary parent folders under the approved lifecycle; preserve the permanent fallback parent.

## 12. User-approved decisions

The following decisions were explicitly approved during discussion:

- The exact report-retirement target is \`.takeout/reports/\`.
- Retain only a compact run-status index under \`workspace/\`; do not retain findings, diagnostic payloads, logs, evidence, error signatures, remediation state, or a parallel Ledger/archive.
- GitHub Actions is the sole post-commit implementation-validation authority for every task type. The Worker may inspect before commit, but not validate after commit.
- Add **Committed / Awaiting CI**. Done requires successful required checks for the exact commit, result reconciliation, and no outstanding required subtasks.
- Required scripts must execute in GitHub Actions. Missing coverage or missing results are never success.
- Every terminal aggregate validation attempt creates one review task. Duplicate deliveries are idempotent; a rerun is a distinct attempt.
- The Worker reads the index first and inspects logs only after recorded check/infrastructure/capture failure, solely for diagnosis. It never inspects successful logs or overrides aggregate status.
- CI produces no diagnostic/finding/evidence documents. The Worker creates one self-contained child folder per distinct actionable root cause.
- Review tasks join the ordinary queue and do not interrupt active work. The Worker continues with other unblocked tasks while CI is pending.
- Correct active parent receives the error child; otherwise use one permanent fallback parent. Never infer parentage or recreate a deleted original parent.
- Completed error children and Done ordinary parent folders are deleted; the permanent fallback parent is never automatically deleted.
- Revision 7's generic verifier direction is approved: one reusable workflow for uncovered task requirements, supporting both registered adapters and repository-owned scripts, with a thin dispatcher. Revision 8 hardens this with exact-commit, trust, privilege, anti-flood, recovery, and loop-prevention safeguards.

## 13. Remaining user decisions

Only the following architecture choices remain for user direction. Recommendations are included; no implementation is authorized.

1. **Coordinator architecture — recommended: one coordinator invoking reusable jobs.** Existing task-validation workflows would expose \`workflow_call\` entry points and be called by one coordinator, alongside the generic verifier. This gives one reliable aggregate result without waiting for separate workflows or guessing whether a check is missing. Alternative: retain independent push-triggered workflows and add a separate \`workflow_run\` aggregator plus missing-check timeout/recovery. The single-coordinator model is simpler and less prone to race conditions, but requires refactoring established workflows.

2. **Run-status retention — recommended: retain one compact record per attempt.** Keep all attempt metadata in the single index, with no diagnostic content. This preserves idempotency and makes previous outcomes visible without retaining findings or reports. Alternative: prune records after their review tasks are reconciled, reducing index growth but weakening long-term attempt traceability and duplicate-event protection.

No other policy choice is intentionally left open. Contract limits, adapter allowlists, timeouts, recovery cadence, retry bounds, trigger filters, and exact schemas are implementation details to be designed within the approved safeguards and accepted ADR.

## 14. Review and decision state

- **Revision:** 8
- **Status:** Draft; not yet formally accepted as a complete decision record.
- **Approved components:** All decisions in Section 12, including the generic verifier supporting both registered adapters and repository-owned scripts.
- **Awaiting user calls:** Only the two choices in Section 13.
- **Implementation authorization:** Not granted. Approval of design components and this revision does not itself authorize implementation. Implementation requires formal Draft promotion, an accepted superseding ADR, and the user's explicit execution instruction.
- **Resulting ADR:** None.

## 15. Revision history

| Date | Revision | Change | Decision |
|---|---:|---|---|
| 2026-11-28 | 1–4 | Established the folder-based remediation model, universal Actions-only post-commit validation, Awaiting CI state, exact-commit completion gate, event-driven review, non-blocking queue, and permanent fallback. | Individual architecture decisions approved. |
| 2026-11-28 | 5–6 | Reduced CI output to a run-status index and review task; restricted Worker log inspection to failure diagnosis. | Approved. |
| 2026-11-28 | 7 | Added one generic reusable verifier, thin dispatcher, structured contracts, adapters, and repository-owned scripts. | User approved both adapters and repository-owned scripts. |
| 2026-11-28 | 8 | Reassessed and consolidated the lifecycle; added one aggregate coordinator, trusted contract policy, isolated publisher, atomic/idempotent publication, recovery sweep, loop prevention, stale-result handling, error grouping, flood controls, and explicit failure guarantees. Reduced duplicated options, risks, and implementation text. | Presented for the two remaining architecture calls in Section 13. |

## 16. Repository references

- \`.agent/skills/the-worker/SKILL.md\` — current task authority, queue, commit, and closeout rules.
- \`.agent/skills/the-worker/references/github-actions.md\` — current Actions workflow design and remediation boundaries.
- \`.agent/skills/the-worker/references/ci-ledger.md\` — current report ingestion, finding identity, attribution, and child publication.
- \`.agent/skills/the-worker/references/decision-governance.md\` — Draft/ADR promotion and implementation authorization.
- \`workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md\`, \`workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md\`, and \`workspace/adr/0007-unified-index-as-latest-lint-report-locator.md\` — accepted decisions requiring scoped reconciliation.
- \`.agent/WORKFLOW_MAP.md\`, \`workspace/README.md\`, and \`workspace/task_board.md\` — navigation and current task publication.
- User decisions in this conversation, 2026-11-28 — approved lifecycle, index boundary, diagnostic boundary, queue behavior, fallback, and generic verifier direction.
