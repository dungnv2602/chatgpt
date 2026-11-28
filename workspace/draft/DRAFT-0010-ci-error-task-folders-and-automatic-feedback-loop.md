---
record_type: decision-draft
template_version: "1.2"
id: "DRAFT-0010"
revision: 7
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

# CI Error Task Folders and Automatic Feedback Loop

## Proposal Summary

Adopt a universal, event-driven post-commit validation lifecycle. The Worker may inspect its changes before committing, but after a commit GitHub Actions is the sole authority for implementation-validation outcomes. The Worker must not run tests/scripts, independently decide whether a commit passed, or override the aggregate result recorded by automation. The Worker may inspect the linked GitHub Actions run **for diagnosis only after the status index reports a failure or infrastructure/capture failure**. That diagnostic inspection does not constitute validation and cannot change the recorded outcome.

A committed task enters **Committed / Awaiting CI**. The Worker immediately moves to another unblocked task instead of waiting for CI. GitHub Actions runs the required validation set; automation records the aggregate terminal result and a direct run URL in a minimal run-status index under `workspace/`, then creates a deduplicated CI-result review task. CI does not generate separate diagnostic reports, finding documents, or error-evidence files. The review task nudges the Worker to read the index. For success, the Worker reconciles the task from the index without opening logs. For failure or infrastructure/capture failure, the Worker opens the linked run to diagnose the cause and creates only the necessary remediation/infrastructure task folders.

A task becomes **Done** only after the required automated checks have succeeded for its exact commit, the aggregate result has been reconciled from the index, and no outstanding subtasks remain. The Worker does not independently validate the implementation. If a required check fails, the Worker diagnoses the linked Actions run and creates remediation subtasks; if validation infrastructure or capture fails, the task remains not Done until that issue is resolved.

This proposal also retains the approved folder-based CI error lifecycle: delete a completed error subtask folder; delete an ordinary parent task folder only when it is Done and has no outstanding subtasks. Retire the confirmed `.takeout/reports/` tree only after all producers and consumers have migrated to the replacement.

This revision consolidates the user's approvals from 2026-11-28, including approval of the lean CI-output model and the failure-only diagnostic boundary: the Worker may inspect the linked Actions run only after the status index records a check failure or infrastructure/capture failure, and solely to diagnose it. It remains a Draft; implementation requires promotion through Decision Governance and an accepted superseding ADR.

## Context and Problem Statement

Current repository contracts define CI diagnostics as report artifacts under `.takeout/reports/`, with a unified index and Ledger. The Ledger owns finding identity, report intake, recurrence, attribution, and child publication. Subtasks are flat Markdown records under a parent's subtasks directory. Current Worker guidance also requires post-commit commit/readback evidence for task completion, while hosted CI results are treated as separate metadata and are not a universal completion gate.

The user has approved a different model with these principles:

- Each distinct actionable CI error diagnosed from the failed GitHub Actions run becomes its own self-contained subtask folder under a genuine, correctly identified active parent task. CI does not generate a separate finding/report document; the Worker creates the remediation task after reading the run.
- The Worker may inspect its changes before committing. After committing, the Worker does not validate its own implementation. GitHub Actions alone executes and validates the required checks.
- The task status explicitly distinguishes work still in progress from a committed task awaiting automated validation.
- A terminal validation result and direct Actions run URL are recorded in a small run-status-only index under `workspace/`. Automation creates a lightweight CI-result review task. The Worker reads the index first and opens the linked run only when diagnosis is needed.
- The Worker does not wait for CI. Immediately after committing, it takes the next unblocked task and continues until no unblocked task remains. It then follows the existing blocked-task procedure and brings blocked tasks to the user for input.
- A review task arriving while the Worker is executing another task does not interrupt that work. It joins the ordinary task queue and is selected when the Worker next selects work.
- A successful required validation result for the exact commit, reconciled through the index, is necessary but not sufficient for Done: outstanding subtasks must also be resolved.
- If an error arrives while its correct parent is active, create the error subtask there; no fallback placeholder is needed. If that parent is Done/deleted or otherwise unavailable, route the error to one permanent fallback parent.
- Completed error subtask folders are deleted. Ordinary parent task folders are deleted when Done. The permanent fallback parent remains available even when empty.
- The user confirmed on 2026-11-28 that the intended report-system retirement target is the existing `.takeout/reports/` directory (not `.take/reports`). Retire that exact directory and its contents only after the replacement workflow is operational and all consumers have migrated.

The existing accepted ADRs and Worker references contain conflicting rules, especially the requirement to verify commit/readback after committing and the absence of a universal CI completion gate. This proposal must supersede those conflicts coherently; it must not be implemented as an informal addendum that leaves contradictory canonical instructions in place.

## Goals and Non-Goals

### Goals

- Make GitHub Actions the sole authority for post-commit implementation validation across all task types, including tasks requiring scripts; permit Worker log inspection only for diagnosis after a recorded failure.
- Allow pre-commit inspection, but prohibit Worker-led post-commit verification of implementation correctness.
- Introduce **Committed / Awaiting CI** as a distinct task status.
- Require automated validation coverage for every task's declared validation requirements; do not treat absent coverage or absent results as success.
- Reuse established workflows where they provide full coverage; otherwise delegate declared verification contracts to one generic reusable workflow through a thin dispatcher, without cloning orchestration for every task type.
- Record commit-specific aggregate validation status in a minimal index under `workspace/`.
- Create one CI-result review task for every terminal validation event/attempt so the Worker is nudged to reconcile the index.
- Keep review tasks administrative and index-driven; do not copy diagnostic payloads into them.
- Let the Worker continue immediately with other unblocked tasks while committed tasks await CI.
- Process incoming review tasks through the ordinary queue without interrupting the task currently in progress.
- Require successful required checks for the exact commit, completed result reconciliation, and no outstanding subtasks before an ordinary task is Done.
- Have the Worker create one self-contained folder per distinct actionable CI error diagnosed from a failed run, with stable identity and active-child deduplication.
- Route errors to the correct active parent; otherwise use a permanent fallback parent for orphaned/late errors.
- Delete completed child folders and Done ordinary parent folders, but never automatically delete the fallback parent.
- Retire the central report/Ledger remediation system and obsolete references after coordinated migration.

### Non-Goals

- The Worker must not run local scripts, tests, or lint as a substitute for required CI validation.
- The Worker must not inspect, poll, dispatch, rerun, or wait for hosted workflow results to determine or override validation status. After the index records a failed or infrastructure/capture-failed outcome, the Worker may open the linked run and inspect logs solely to diagnose the failure.
- The Worker must not read back committed source files or diffs as a post-commit correctness check. Recording the SHA returned by the commit operation and updating task metadata are administrative actions, not validation.
- The Worker must not use a missing CI result, missing review task, empty error-subtask list, skipped check, or incomplete capture as proof of success.
- Do not create synthetic parent tasks for files, jobs, workflows, or individual errors.
- Do not generate CI-authored diagnostic reports, finding documents, or evidence artifacts. Do not retain a central findings database, diagnostic archive, or report index. The only retained index is the strictly bounded run-status index under `workspace/`; diagnostic context needed for remediation is captured by the Worker in the relevant task folder.
- Do not claim that successful configured checks prove the absence of defects outside their declared coverage.
- Do not delete `.takeout/reports/` until the replacement capture/status workflow is operational and all consumers have migrated.
- Do not delete the permanent fallback parent when it has no children.

## Decision Drivers

| Criterion | Why it matters | Relative importance |
|---|---|---|
| Validation authority | Avoid contradictory manual and automated verification paths. | Critical |
| Exact-commit integrity | A result must validate only the commit it actually checked. | Critical |
| Event-driven handoff | Completed CI results must create actionable Worker queue work. | High |
| Queue throughput | CI waiting must not leave the Worker idle. | High |
| Capture reliability | Missing or failed capture must never look like a clean pass. | Critical |
| Error isolation | Each error must be independently actionable and removable. | High |
| Parent attribution | Active parent ownership and late-error routing must be deterministic. | High |
| Cleanup semantics | Completed work should leave no stale folders, except permanent infrastructure. | High |
| Migration safety | Existing workflows and accepted ADRs must be replaced coherently. | High |

## Assessment Basis and Evidence Limits

- **Scope of comparison:** Current report/Ledger workflow; folder-based CI child workflow without a central Ledger; hybrid run-status index plus folder-based children and event-driven review tasks.
- **Assessment method:** Static inspection of current Worker, GitHub Actions references, task/subtask templates, document catalog, Workflow Map, workspace README, and accepted ADRs on branch `gpt` on 2026-11-28.
- **Evidence boundary:** Repository documents establish current written contracts, not runtime behavior. No local tests or hosted CI results were inspected for this Draft update.
- **Key assumptions:** GitHub Actions can execute the declared required validation set for every task type, aggregate terminal results for an exact commit, write the run-status index, and create review/error task folders with appropriate permissions.
- **Unresolved implementation questions:** Exact workflow orchestration, aggregate required-check definition, event identity and idempotency mechanism, permissions, task queue discovery/ordering, and how the existing board represents the new status and system-generated review tasks. The proposed generic verifier also needs a contract schema, adapter interface, dispatcher/coverage-selection rule, trusted ownership boundary, and policy for tasks requiring secrets or elevated permissions. These must be resolved during implementation design without weakening the approved lifecycle.
- **Script-task requirement:** A task requiring script execution must declare that script as part of its validation contract and have a GitHub Actions workflow execute it. If coverage is absent, the task cannot become Done; workflow coverage must be added before successful validation can be claimed.

### Proposed generic reusable verification workflow

For a task whose declared verification requirements are not covered by an established GitHub Actions workflow, use a generic reusable verification workflow as the default fallback. This is a proposed addition for discussion in revision 7; it is not yet a separately approved policy decision.

**Operating model**

- Keep established, task-specific workflows as the preferred verification path whenever they already cover the task's declared requirements. Do not route a task through the generic verifier merely to duplicate checks already owned by an established workflow.
- Provide one repository-owned reusable workflow, invoked through GitHub Actions `workflow_call`, that can execute different task verification contracts without requiring a new workflow definition for every task type.
- Provide a thin dispatcher/caller workflow that detects or receives a committed task with no established workflow coverage and invokes the reusable verifier. A reusable workflow cannot trigger itself; it must be called by another workflow. The dispatcher is orchestration, not a second validation authority.
- The task declares a machine-readable verification contract, stored in the repository and associated with the task/commit. The contract identifies the required checks, their order or dependencies where relevant, execution environment, working directory, timeout, and expected success conditions. The dispatcher passes the contract locator, source Task-ID, exact commit SHA, and validation-attempt identity to the reusable workflow.
- The reusable workflow checks out and verifies the exact commit SHA under test, resolves the contract from that commit, executes every required check, and returns a terminal result to the same aggregate validation coordinator used by established workflows. Its result is subject to the same index publication, review-task creation, and exact-commit completion gate.
- Support both reusable built-in verification adapters (for common test, lint, build, schema, and policy checks) and repository-owned task scripts for novel checks. A new task type should normally require only a new contract or adapter/script, not a new copy of the orchestration workflow.
- A task may declare multiple independent checks. The verifier must preserve each check's result and allow the aggregate coordinator to determine the final outcome; a partial pass must never be reported as aggregate success.
- If a task's contract is missing, malformed, unsupported, incomplete, or cannot be executed, report a non-success infrastructure/coverage outcome. Do not silently skip the unsupported requirement or treat the absence of a check as success.

**Safety and integrity boundaries**

- Do not accept arbitrary shell command strings from task metadata as executable input. Use structured contract fields and named adapters; where a repository-owned script is needed, reference a validated repository-relative path and pass arguments as discrete values rather than interpolating an unrestricted command string.
- Validate contract schema, script paths, working directories, and input types. Reject path traversal and references outside the checked-out repository unless a separately approved adapter explicitly supports them.
- Execute against the exact commit being validated, not the branch's moving HEAD or the dispatcher's latest checkout.
- Use least-privilege permissions, no secrets by default, pinned third-party actions, bounded execution time/resources, and explicit handling of fork/untrusted contribution contexts. Any elevated permission or secret requirement must use an explicitly approved workflow path rather than being inferred from a task contract.
- Treat the verification contract and scripts as code under review. A task must not be able to weaken its own required checks merely by editing its contract; required-check policy and permitted adapters need trusted ownership or protected governance.
- The generic verifier must not redefine required-check policy, write diagnostic reports, or independently declare the task Done. It supplies check outcomes to the existing aggregate coordinator and run-status index only.

**Coverage selection and fallback**

- Before dispatch, determine whether an established workflow fully covers the task's declared verification contract. Partial coverage is not full coverage; uncovered requirements must be delegated to the generic verifier or explicitly classified as unsupported/non-success.
- Avoid running the same required check twice unless duplication is intentionally declared as a separate requirement.
- The aggregate required-check identity must record which established workflows and/or generic contract checks formed the validation set for that exact commit and attempt.
- If no safe generic adapter or permitted script can satisfy a requirement, fail closed and create an infrastructure/coverage remediation task. Do not manufacture a green result.

**Design boundary**

The generic workflow is an execution mechanism, not an unrestricted arbitrary-command runner. Its versatility comes from a stable contract schema, reusable adapters, and repository-owned verification scripts. New verification needs can be added without cloning workflow orchestration, while permissions, exact-commit integrity, and aggregate-result authority remain centralized.

## Considered Options

### Option 1 — Keep the report/Ledger workflow and flat child records

- **Description and operating model:** Retain unified reports and Ledger as the source of truth. The Ledger groups findings and creates flat child Markdown records under parent tasks. Current completion relies on commit/readback evidence; hosted validation is separate metadata.
- **Repository and environment fit:** Matches ADR-0003, ADR-0004, ADR-0007, current Worker references, and existing generator paths.
- **Good — strengths:** Lowest migration cost; preserves existing identity, recurrence, evidence, and index machinery.
- **Neutral — trade-offs:** Existing report infrastructure remains central and requires ongoing maintenance.
- **Bad — weaknesses:** Does not satisfy folder-per-error, universal CI validation, event-driven review, or the no-post-commit-verification rule.
- **Implementation and migration cost:** Lowest; mostly maintain current implementation.
- **Dependencies and operational burden:** Requires report indexes, Ledger, schemas, shared eligibility logic, and report capture.
- **Risks and safeguards:** Central state can flood, drift, or become inconsistent with task folders. Existing idempotency and attribution safeguards mitigate some risk but do not meet the requested lifecycle.
- **Evidence and confidence:** Current ADRs and Worker references explicitly describe this model; high confidence about documented contracts.
- **Limitations and unknowns:** Runtime behavior has not been tested in this review.

### Option 2 — One self-contained folder per CI error with automatic feedback loop and no central run index

- **Description and operating model:** CI creates one child folder for each distinct actionable error under the triggering genuine parent task. Each folder contains task.md, exact diagnostics, relevant logs/evidence, source commit and Task-ID attribution, affected paths, and references needed to fix the error. The Worker fixes and commits; CI runs automatically and creates further error folders if needed. No manual post-commit verification is performed. A completed child folder is deleted. When no new error folders are generated and no child work remains, the parent CI task folder is deleted.
- **Repository and environment fit:** Matches the folder-based remediation direction but cannot, by itself, reliably distinguish a successful clean validation cycle from a missing, skipped, or failed capture.
- **Good — strengths:** Each error is isolated and self-contained; cleanup is simple; no central findings database.
- **Neutral — trade-offs:** Historical diagnostics are intentionally discarded with completed folders. A later recurrence is a new error task.
- **Bad — weaknesses:** Absence of error folders alone is not sufficient evidence that required checks completed successfully. It also lacks an explicit event handoff to prompt the Worker to reconcile a terminal result.
- **Implementation and migration cost:** High; coordinated changes are needed across workflows, Worker, templates, board, and existing report/Ledger producers.
- **Dependencies and operational burden:** CI must create folders and update task indexes. Capture failures need a visible failure path.
- **Risks and safeguards:** Distinguish a completed CI cycle with no actionable errors from a missing or failed capture; reuse a matching child only while that child remains active; include all needed context; do not infer success from silence.
- **Evidence and confidence:** User approval establishes the desired folder lifecycle. Feasibility remains to be implemented and operationally demonstrated.
- **Limitations and unknowns:** No durable commit-specific terminal status or event-driven review task is defined in this option.

### Option 3 — Workspace run-status index, event-driven review tasks, and folder-based remediation

- **Description and operating model:** Retain only a compact CI run-status index under `workspace/`. For each validation attempt, record the exact commit SHA, validation-cycle/run identity, required workflow/check-set identity, completion time, aggregate terminal outcome (success, check failure, or infrastructure/capture failure), and direct GitHub Actions run URL. The index is run-status-only: it must not store findings, diagnostic payloads, logs, evidence, deduplication signatures, or remediation state.

  GitHub Actions executes the required checks for the exact commit. When the complete required check set reaches a terminal aggregate outcome, automation writes the index record and creates one lightweight CI-result review task for that validation event/attempt. The review task contains references (source Task-ID, commit SHA, validation/run identity, index location, run URL, and instructions), not copied diagnostics. The Worker executes the review task by reading the index first. For success, it reconciles task state from the index. For failure or infrastructure/capture failure, it may open the linked run and inspect logs solely to diagnose the cause, then creates the necessary remediation/infrastructure task folders. It must not rerun checks or independently decide whether validation succeeded.

  A validation event means the aggregate result for the declared required check set for one exact commit and one validation attempt—not an individual job finishing while other required jobs remain pending. Duplicate event deliveries must not create duplicate review tasks. A rerun is a distinct attempt and must have a distinct identity. A later successful rerun does not silently erase a prior failed event or delete already-created remediation work.

  CI does not generate separate diagnostic reports, finding documents, or error-evidence files. The Worker captures only the actionable diagnosis and necessary evidence in the remediation task folder. A successful aggregate result means the declared required checks completed successfully for that exact commit; it does not prove absence of defects outside their coverage. Missing, pending, cancelled, skipped, incomplete, or infrastructure/capture-failed outcomes are not success.

- **Task lifecycle:** After the Worker commits, the task enters **Committed / Awaiting CI** and the Worker immediately selects another unblocked task. It continues processing unblocked work without waiting for CI. When no unblocked task remains, it follows the existing blocked-task procedure and brings blocked tasks to the user for input. A CI-result review task created while the Worker is busy joins the ordinary queue and does not interrupt the current task.

  The Worker marks a task **Done** only after the review task reconciles a successful aggregate result for the exact commit and no outstanding subtasks remain. If actionable checks fail, automation creates error subtasks and the original task returns to active remediation. If validation infrastructure or capture fails, the task remains not Done and is blocked or routed to an explicit infrastructure task; it must not be treated as a clean pass.

- **Error routing:** If the correct original parent is still active and can own the error, create the error subtask under that parent. Do not create a fallback task in this case. If the original parent is Done/deleted or otherwise unavailable, create the subtask under one permanent fallback parent for orphaned/late CI errors. Preserve the originating Task-ID, exact commit SHA, and validation/run identity in the error subtask. The fallback parent is permanent infrastructure and is never deleted just because it has no children.

- **Repository and environment fit:** Fits the folder-based remediation model while retaining a narrow, auditable signal that the configured validation cycle actually ran and a queue event that prompts reconciliation. The index is workspace-owned metadata, not a report artifact under `.takeout/reports/`.
- **Good — strengths:** Universal CI-only post-commit validation; explicit task state; commit-specific aggregate result; event-driven review; non-blocking queue throughput; direct diagnostic source in Actions; no CI-generated finding documents or central findings Ledger; clear late-error destination.
- **Neutral — trade-offs:** A small central metadata file and system-generated review tasks remain. The Worker performs diagnosis only on failed runs and records actionable findings in task folders.
- **Bad — weaknesses:** A green result is only as meaningful as the declared required checks. A missing workflow, omitted script, incorrectly optional check, or failed event delivery could undermine the model if not detected.
- **Implementation and migration cost:** Highest; requires coordinated changes to workflow orchestration, status writer, event/task generator, Worker policy, templates, queue, board, ADRs, and existing report/Ledger consumers.
- **Dependencies and operational burden:** GitHub Actions must run every required check and aggregate results for each exact commit/attempt. Automation must write status and the run URL before or atomically with review-task publication, deduplicate event deliveries, and preserve the queue handoff. Worker reads the index for status and opens the linked run only for failure diagnosis.
- **Risks and safeguards:** Require declared validation coverage, exact SHA binding, aggregate required-check completion, idempotent event identity, visible infrastructure failure, and no inference of success from absent records. Do not generate CI diagnostic artifacts; let the Worker capture concise actionable diagnosis and evidence in child folders.
- **Evidence and confidence:** The user approved this operating model on 2026-11-28. The exact index schema, workflow implementation, permissions, and queue integration remain implementation work; no runtime behavior has been verified.
- **Limitations and unknowns:** Exact workflow triggers, check aggregation, event delivery/recovery, write permissions, and queue-discovery behavior remain to be designed and implemented.

## Comparative Assessment

| Criterion | Option 1: Existing Ledger | Option 2: Folder loop only | Option 3: Run index + event review |
|---|---|---|---|
| One folder per error | Weak | Strong | Strong |
| Self-contained remediation | Partial | Strong | Strong |
| Universal CI-only post-commit validation | Weak | Partial | Strong |
| Explicit Committed / Awaiting CI status | Weak | Partial | Strong |
| Distinguishes clean cycle from failed capture | Strong via reports, but current lifecycle differs | Weak without another signal | Strong, with explicit aggregate terminal states |
| Event-driven Worker nudge | Weak | Partial | Strong |
| Worker can continue other tasks while CI runs | Not consistently defined | Possible | Explicit |
| Late/orphaned error destination | Not aligned to approved lifecycle | Needs definition | Permanent fallback parent |
| Central state overhead | High | Low | Low–moderate, strictly bounded |
| Complete report-system retirement | No | Yes | Yes; retains only run-status metadata under workspace/ |
| Migration cost | Low | High | Highest |

### Overall comparison

Option 1 preserves existing machinery but conflicts with the approved universal validation and task-folder lifecycle. Option 2 removes central state but cannot safely use absence of generated subtasks as proof that required validation succeeded. Option 3 preserves folder-based remediation while retaining the minimum commit-specific run outcome and event-driven handoff needed for a reliable lifecycle. The index records run status only; the review task provides the nudge; the Worker reads the index rather than validating code or inspecting workflow diagnostics. Option 3 is the recommended architecture.

## Proposed Recommendation

Adopt Option 3.

### A. Universal post-commit validation and diagnosis boundary

- Before commit, the Worker owns implementation and may inspect its changes, review diffs, and make corrections.
- After commit, GitHub Actions is the sole authority for implementation-validation outcomes. The Worker must not run tests/scripts/lint, independently decide whether a commit passed, or override the aggregate status recorded in the workspace index.
- The Worker may retain the commit SHA returned by the commit operation and update task metadata as administrative bookkeeping. Such bookkeeping is not validation.
- The Worker must not inspect successful workflow logs or independently re-evaluate passing checks. When the index records a failed or infrastructure/capture-failed result, the Worker may open the linked Actions run and inspect logs **solely to diagnose the cause and prepare remediation**. This diagnostic inspection cannot change the recorded validation outcome.
- Every task declares its validation requirements. Tasks requiring scripts must have those scripts executed by required GitHub Actions checks. Missing coverage or a missing result means not validated, never Done.
- Do not weaken, skip, or silently omit required checks to obtain a green result.

### B. Task status and completion

Use these lifecycle meanings:

| Status | Meaning |
|---|---|
| **In Progress** | Implementation or remediation work is still required. |
| **Committed / Awaiting CI** | Implementation has been committed; required automated validation and result reconciliation are outstanding. No Worker post-commit verification is performed. |
| **Blocked** | Progress requires an external decision, missing dependency, or validation/capture infrastructure recovery; follow existing blocked-task escalation. |
| **Done** | Required aggregate checks succeeded for the exact commit, the result was reconciled, and no outstanding subtasks remain. The ordinary task folder is then deleted. |

A task is not Done merely because it was committed, a workflow started, one workflow/job passed, the status index is empty, or no error subtask appeared. Missing, pending, cancelled, skipped, incomplete, or infrastructure/capture-failed results cannot establish success.

If a check failure generates actionable subtasks, the original task returns to active remediation. If validation infrastructure or capture fails, the task remains not Done and must be made visibly blocked or assigned explicit infrastructure remediation. A later successful rerun may validate the same exact commit only when the complete required check set succeeds; it does not silently erase previous failure events or outstanding remediation folders.

### C. Event-driven validation and review handoff

1. The Worker commits and records the returned commit SHA as task metadata; task status becomes Committed / Awaiting CI.
2. GitHub Actions executes the task's declared required check set for that exact commit.
3. Automation aggregates all required workflow/check outcomes for that commit and validation attempt. Do not publish a successful terminal result while any required check remains pending or absent.
4. On every terminal aggregate validation event/attempt—including success, check failure, and infrastructure/capture failure—automation writes the run-status-only index record and creates one corresponding CI-result review task.
5. Duplicate event deliveries are idempotent. A distinct rerun/attempt has a distinct event identity and review task.
6. The review task is a system-generated administrative task. It contains the source Task-ID, exact commit SHA, validation/run identity, index location, and reconciliation instructions. It does not contain copied logs, findings, or diagnostic payloads.
7. When the Worker executes the review task, it reads the workspace index first and matches the exact commit and attempt. For success, it reconciles task state without opening logs. For failure or infrastructure/capture failure, it opens the linked run solely to diagnose the cause, creates the necessary remediation/infrastructure task folders, and updates task lifecycle. It does not rerun validation or independently decide whether validation succeeded.
8. Complete and delete the review task folder after reconciliation. If the result is missing, incomplete, or cannot be matched, do not mark the source task Done; route the issue through the existing blocked/infrastructure process.

A validation event is the aggregate result of the full required check set for one exact commit and one attempt, not an individual job completion while other required jobs remain pending.

### D. Non-blocking Worker task queue

- Immediately after a task enters Committed / Awaiting CI, the Worker selects and executes another unblocked task.
- Continue this behavior until no unblocked tasks remain.
- At that point, follow the existing blocked-task procedure and bring blocked tasks to the user for input.
- A CI-result review task arriving while another task is in progress does not interrupt that work. It joins the ordinary queue and is eligible for selection at the next task-selection point.
- Review tasks are normal unblocked system-generated tasks, not a separate queue that can be forgotten.
- CI waiting must never be treated as a reason for the Worker to idle while other unblocked tasks exist.

### E. Error folders, routing, and permanent fallback

- Each distinct actionable CI error diagnosed by the Worker from a failed Actions run is one self-contained subtask folder under a genuine parent.
- If the correct originating parent is still active and can own the error, create the subtask there. Do not create a placeholder/fallback task for errors that have a valid active parent.
- If the original parent is Done and deleted, or otherwise unavailable, create the error under a single permanent fallback parent for orphaned/late CI errors.
- Preserve the originating Task-ID, exact commit SHA, validation/run identity, concise Worker-authored diagnosis, relevant log excerpts or durable references, affected paths, and remediation instructions in the error subtask. CI does not create a separate finding document.
- Reuse a matching error subtask only while it remains active; distinct errors remain separate.
- Delete a completed error subtask folder and all its contents. Delete an ordinary parent folder when it is Done and has no outstanding subtasks.
- The fallback parent is permanent workflow infrastructure. Never delete it merely because it has no outstanding children. Its completed child folders are still deleted normally.
- A later error associated with a previously Done/deleted task is new work routed to the fallback parent; do not recreate or silently reopen the deleted original task.

### F. Run-status index boundary

Keep the index under `workspace/`. Its allowed content is limited to run/validation metadata, including:

- exact commit SHA;
- validation-cycle and run/attempt identity;
- required workflow/check-set identity;
- completion timestamp;
- aggregate terminal outcome (success, check failure, infrastructure failure, or capture failure).

The index must not contain findings, error signatures, logs, diagnostic payloads, evidence, remediation state, or historical finding records. It may contain the direct Actions run URL as a locator. A successful record means only that the declared required checks completed successfully for that exact commit.

### G. Report-system retirement

The user confirmed `.takeout/reports/` as the exact retirement target. Migrate every producer, consumer, schema, script, navigation link, and documentation reference to the folder-based error tasks and workspace run-status index. Make replacement capture and status publication operational before deleting `.takeout/reports/`. Do not preserve a parallel findings archive or hidden Ledger.

## Consequences and Trade-Offs

- **Positive:** One validation authority after commit; no Worker post-commit verification; explicit Awaiting CI state; event-driven review; parallel task throughput; exact-commit validation; self-contained error work; deterministic late-error routing; no central findings Ledger.
- **Negative:** The system depends on GitHub Actions coverage, aggregate result publication, and reliable event/task creation. Completed diagnostics and recurrence history are deleted with their task folders.
- **Neutral:** Review tasks and the run-status index are retained as operational metadata, not as findings storage. CI produces no separate diagnostic documents; the Worker consults the run only when diagnosis is necessary.
- **Conditional:** A successful configured check set is meaningful only when the task's required validation contract is complete and all required checks actually run.

## Risks and Safeguards

| Risk | Likelihood / Impact | Evidence / rationale | Safeguard | Residual risk |
|---|---|---|---|---|
| Required workflow does not run after a commit | Unknown / Critical | Trigger behavior not yet inspected | Declare required checks per task type; detect absent required results; never infer success | Workflow configuration can still be wrong |
| Script task has no CI execution coverage | Unknown / Critical | Current coverage has not been inventoried | Add required Actions coverage for each declared script before task can be Done | New script types may be omitted |
| One workflow passes while another required check is pending | Medium / High | Multi-workflow aggregation needed | Create terminal event only for aggregate required-check set | Aggregator defects |
| Event delivery is duplicated or lost | Unknown / High | Event/task writer not implemented | Stable event identity, idempotent creation, recoverable outbox/reconciliation | Platform outages |
| Review task is created before index is durable | Medium / High | Writer ordering not yet implemented | Publish index record before review task, or use atomic/recoverable publication | Partial writes |
| Old run is mistaken for current commit validation | Medium / Critical | Multiple commits/reruns possible | Exact SHA and attempt identity matching; never apply a result to another SHA | Incorrect task metadata |
| A rerun hides a prior failure | Medium / High | Multiple attempts possible | Keep attempt identities distinct; never silently erase existing remediation folders | Flaky-check handling needs policy |
| Capture fails but no child is created | Unknown / Critical | Capture behavior not yet inspected | Explicit infrastructure/capture terminal state and review task | Capture failure can delay remediation |
| Late error has no valid parent | High / Medium | Original folders are intentionally deleted | Permanent fallback parent; preserve origin references | Fallback queue may accumulate work |
| Duplicate errors create flooding | Medium / Medium | Same error can recur across cycles | Stable signature and reuse only while matching child remains active | No long-term identity history after deletion |
| Actions logs expire before remediation | Medium / High | Direct run inspection replaces CI-generated evidence copies | Record run URL and capture the relevant concise log excerpts/diagnosis in the Worker-created remediation task | Some artifacts may expire before review |
| Premature deletion loses active work | Low / Critical | Folder deletion is destructive | Delete ordinary parent only after successful validation and no outstanding subtasks; delete child only when resolved | No retained archive by design |
| Worker idles while CI runs | Medium / High | CI duration can be long | Mandatory next-unblocked-task scheduling rule | Queue discovery latency |
| Review task is forgotten or starved | Medium / High | Review task is asynchronous | Review task enters ordinary queue and is eligible at every next task-selection point | Sustained higher-priority work may delay it |
| Old consumers reference retired paths | High / High | Current docs and ADRs reference `.takeout/reports/` | Inventory and migrate all consumers before deleting the actual path | External references may remain |
| Fallback parent is accidentally deleted | Low / High | Ordinary parents are deleted at Done | Mark fallback as permanent infrastructure excluded from empty-parent cleanup | Manual deletion remains possible |

## Repository Impact

| Area | Proposed change | Owner / exact files | Approval dependency |
|---|---|---|---|
| Decision records | Supersede conflicting report/Ledger, flat-child, and post-commit readback rules | ADR-0003, ADR-0004, ADR-0007; new ADR | Accepted consolidated Draft |
| Worker lifecycle | Define pre-commit inspection boundary, no post-commit verification, status transitions, queue draining, review-task handling | `.agent/skills/the-worker/SKILL.md` and CI references | Accepted ADR |
| Task state and templates | Add Committed / Awaiting CI, validation requirements, review-task type, fallback-parent semantics | TASK_TEMPLATE.md, SUBTASK_TEMPLATE.md, task board/queue contracts, catalog | Accepted ADR |
| CI validation | Define required checks by task type/path and aggregate exact-commit results, including script execution | `.github/workflows/` and relevant workflow assets | Accepted ADR |
| Event producer | Write run-status index and create idempotent review tasks for terminal aggregate events | CI automation/workflow scripts | Accepted ADR |
| Error producer | Generate one self-contained error folder per actionable finding and route to active parent or fallback | CI capture scripts and task-folder generator | Accepted ADR |
| Index | Create strictly bounded run-status-only index under `workspace/` | Workspace-owned index/schema and writer/reader | Accepted ADR |
| Permanent fallback | Establish a permanent parent for orphaned/late CI error subtasks | Canonical task hierarchy and task board | Accepted ADR |
| Navigation | Remove obsolete report links and map CI flow to folders, status index, and review queue | `.agent/WORKFLOW_MAP.md`, `workspace/README.md`, task board | Accepted ADR |
| Data retirement | Delete confirmed obsolete report tree after migration | User-confirmed exact path: `.takeout/reports/` | Replacement operational |

## Proposed Implementation Outline

1. Approve this consolidated Draft and promote it to a superseding ADR for ADR-0003, ADR-0004, and ADR-0007 where rules conflict.
2. Define task validation contracts: required workflow/check set for each task type, including scripts and other executable acceptance criteria. Establish a machine-readable contract schema, trusted policy boundary, and named adapter interface.
3. Retain established workflows when they fully cover a task's contract. Design a thin dispatcher and one generic reusable verifier for uncovered contracts; pin execution to the exact commit, enforce least privilege, and fail closed on unsupported or unsafe requirements.
4. Define the task status lifecycle and board representation, including **Committed / Awaiting CI** and **Done** gates.
5. Define the aggregate validation event and status-index schema, exact SHA/attempt identity, event idempotency, and failure/recovery semantics.
6. Implement CI automation that records each terminal aggregate result and direct run URL, then creates one lightweight review task per validation attempt; do not generate separate CI finding/report/evidence documents.
7. Implement Worker review-task instructions: read the workspace index first; reconcile success from the index; for failure/infrastructure failure, inspect the linked run only for diagnosis, create necessary remediation tasks, and never rerun or independently re-score validation.
8. Implement the non-blocking task queue rule: after commit, immediately select the next unblocked task; continue until none remain, then use the existing blocked-task escalation. Review tasks join the ordinary queue and do not interrupt current work.
9. Define and implement self-contained error-subtask folders, active-parent routing, stable active-child deduplication, and the permanent orphan/late-error fallback parent.
10. Update Worker, templates, catalog, board, Workflow Map, workspace README, and all related references; reconcile accepted ADR conflicts.
11. Execute two parent-level workstreams: (a) folder-based CI generation, validation status, event-driven review, and automatic feedback loop; (b) report-system retirement and reference cleanup.
12. Migrate consumers and make replacement capture/status publication operational. Only then delete the confirmed `.takeout/reports/` tree.
13. At quiescence, delete completed error child folders and Done ordinary parent task folders. Never delete the permanent fallback parent. Do not retain archive copies of completed findings.

## User Clarifications and Approved Decisions

All decisions below were approved by the user during discussion on 2026-11-28. This records approval of the individual design decisions; the consolidated Draft revision remains open for continued discussion and has not yet been declared formally accepted as a complete decision record.

- **Report retirement target:** The exact directory is `.takeout/reports/`.
- **Index choice:** Option 3; retain only a run-status index under `workspace/`. Do not retain findings, diagnostics, logs, evidence, deduplication identity, or remediation state in the index.
- **Universal validation:** After commit, GitHub Actions is the sole implementation-validation authority. The Worker may inspect changes before commit but must not independently validate after commit. This applies to all task types, including script tasks.
- **Task status:** Add **Committed / Awaiting CI** to distinguish committed work awaiting automated validation from **In Progress** work that still needs implementation. **Done** requires successful required automated checks for the exact commit, result reconciliation, and no outstanding subtasks.
- **Script validation:** Required scripts must be executed by an appropriate GitHub Actions workflow. Missing coverage or missing results cannot be treated as success.
- **Event-driven review and diagnostic boundary:** Every terminal aggregate validation event/attempt creates a system-generated CI-result review task. The Worker reads the workspace index first. It opens linked Actions logs only when the index records a check failure or infrastructure/capture failure, solely to diagnose the cause and create remediation work. It does not inspect logs after success, and log inspection never validates or overrides the aggregate status.
- **Review-task content:** Store references to the source Task-ID, commit SHA, validation/run identity, index location, direct Actions run URL, and reconciliation instructions; do not duplicate CI diagnostics.
- **Queue behavior:** As soon as a task is committed, the Worker immediately moves to another unblocked task. Continue until no unblocked task remains, then follow the existing blocked-task procedure and bring blocked tasks to the user. Incoming review tasks join the ordinary queue and do not interrupt current work.
- **Active-parent routing:** If an error has a correctly identified active parent, create the error as its subtask; no placeholder is needed.
- **Orphan/late-error routing:** If the original parent is Done/deleted or otherwise unavailable, create the error under one permanent fallback parent. The fallback parent is never deleted merely because it is empty.
- **Folder cleanup:** Completed error child folders are deleted. Ordinary parent folders are deleted when Done and no outstanding subtasks remain. The permanent fallback parent is exempt from automatic deletion.

## Review and Approval

- **Revision presented:** 7
- **User decisions:** The revision 4 architecture decisions remain approved. The lean CI-output model introduced in revision 5 is approved: CI retains only the run-status index and lightweight review-task event, with no CI-authored diagnostic/report/evidence documents. The Worker inspects the linked Actions run only after a recorded check failure or infrastructure/capture failure, solely for diagnosis.
- **Consolidated Draft status:** Draft; the individual design decisions recorded here have been approved, including the lean CI-output model and failure-only diagnostic boundary. Revision 7 adds a proposed generic reusable verification workflow; this addition is awaiting user review and approval. The complete consolidated Draft has not yet been formally accepted as a decision record.
- **Implementation authorization:** Not granted by this Draft update. Implementation requires the user's explicit execution instruction after the decision is finalized and the required superseding ADR is accepted.
- **Decision date:** 2026-11-28
- **Resulting ADR:** Not created

## Discussion and Revision History

| Date | Revision | Change | User feedback / decision |
|---|---|---|---|
| 2026-11-28 | 1 | Prepared the superseding CI folder/feedback-loop proposal and documented the repository path discrepancy. | User approved the operating model; clarified the intended directory. |
| 2026-11-28 | 2 | Confirmed `.takeout/reports/` as the exact retirement target and removed the unresolved-path question. | User confirmed the path. |
| 2026-11-28 | 3 | Selected Option 3; narrowed the retained index to commit-specific CI run status only and relocated it under `workspace/`. | User approved the Option 3 architecture direction. |
| 2026-11-28 | 4 | Consolidated universal GitHub Actions-only post-commit validation; Committed / Awaiting CI; exact-commit Done gate; event-driven review tasks; index-only Worker reconciliation; non-blocking queue scheduling; active-parent vs permanent fallback routing; and permanent fallback lifecycle. | User approved each of these decisions and asked to update the Draft for continued discussion. |
| 2026-11-28 | 5 | Proposed lean CI output: retain only the run-status index (including a direct run URL) and lightweight review-task event; stop generating CI-authored finding/report/evidence documents. Worker opens failed Actions runs only for diagnosis and creates remediation task folders; successful outcomes are reconciled from the index without log inspection. | Recommendation presented for user decision. |
| 2026-11-28 | 6 | Recorded approval of the lean CI-output model and failure-only diagnostic boundary: inspect the linked Actions run only after the index records check failure or infrastructure/capture failure, solely to diagnose the cause. Do not inspect logs after success; do not transfer validation authority to the Worker. | User approved. |
| 2026-11-28 | 7 | Proposed a generic reusable verification workflow for tasks without established workflow coverage, invoked by a thin dispatcher and driven by a structured task verification contract. Added exact-commit, least-privilege, contract-validation, and fail-closed boundaries. | User requested assessment and continuation of the Draft; proposal awaiting discussion and approval. |

## References and Evidence Register

| ID | Source / exact locator | Version, date, or commit | Evidence type | Supports which option / claim | Limitations |
|---|---|---|---|---|---|
| E1 | `.agent/skills/the-worker/SKILL.md`, task hierarchy and CI attribution; CI/Actions operational ownership; canonical CI implementation | Branch gpt, retrieved 2026-11-28 | Repository fact | Current Worker lifecycle, attribution, and report paths | Written contract, not runtime proof |
| E2 | `.agent/skills/the-worker/references/ci-ledger.md` | Branch gpt, retrieved 2026-11-28 | Repository fact | Central identity, report intake, and child generation | Written contract, not runtime proof |
| E3 | `.agent/skills/the-worker/assets/SUBTASK_TEMPLATE.md` v1.6 and `TASK_TEMPLATE.md` v2.7 | Branch gpt, retrieved 2026-11-28 | Repository fact | Current flat subtask record format and parent task folder format | Written contract, not runtime proof |
| E4 | `.agent/skills/the-worker/references/document-type-catalog.md` v1.27 | Branch gpt, retrieved 2026-11-28 | Repository fact | Catalog classifies subtask records and reports as template/generator-owned | Current path coverage needs migration review |
| E5 | `workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md`, `workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md`, `workspace/adr/0007-unified-index-as-latest-lint-report-locator.md` | Branch gpt, retrieved 2026-11-28 | Repository fact | Accepted decisions this proposal would supersede | Decision rationale must be preserved in resulting ADR |
| E6 | `.agent/WORKFLOW_MAP.md` and `workspace/README.md` | Branch gpt, retrieved 2026-11-28 | Repository fact | Current CI flow and report navigation | Map and navigation are summaries |
| E7 | User messages in this conversation | 2026-11-28 | User instruction | Approved folder-per-error lifecycle, universal validation delegation, event-driven review, queue behavior, and late-error fallback | Approval of design decisions; implementation remains pending |
