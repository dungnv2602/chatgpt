---
record_type: decision-record
template_version: "1.1"
id: "ADR-0008"
status: "promotion-pending"
decision_date: "2026-11-28"
decision_makers:
  - "User"
proposed_by: "Assistant"
consulted: []
informed: []
source_draft: "DRAFT-0010"
source_draft_revision: 9
approved_scope: "DRAFT-0010 revision 9: universal exact-commit GitHub Actions post-commit validation; one coordinator invoking established reusable workflows and a generic verifier; protected structured contracts; complete aggregate outcomes; isolated, atomic, idempotent status/review publication and recovery; non-blocking Worker queue; folder-based grouped remediation; 14-day post-reconciliation index retention with unresolved-record protection and a verified checkpoint; and retirement of .takeout/reports only after complete migration and operational proof."
related_adrs:
  - "ADR-0003"
  - "ADR-0004"
  - "ADR-0007"
supersedes:
  - "ADR-0003"
  - "ADR-0004"
  - "ADR-0007"
superseded_by: null
implementation_status: "not-started"
implementation_tasks: []
review_triggers:
  - "A required check is missing, skipped, cancelled, or evaluated against a different source SHA or policy revision."
  - "The coordinator, publisher, or recovery sweep loses or duplicates a terminal attempt."
  - "A publisher commit recursively starts source validation."
  - "The index grows beyond recent and genuinely unresolved attempts, or a checkpoint suppresses an unaccounted event."
  - "A CI failure is misattributed, creates duplicate remediation, or fails to reach the permanent fallback."
  - "Migration removes required validation coverage or retires .takeout/reports before all producers and consumers have moved."
---

# CI Validation, Error Tasks, and Automatic Feedback Loop

## Context and Problem Statement

The repository currently has independent push-triggered validation workflows and separate workflow-run diagnostic capture. The current capture path writes report artifacts under `.takeout/reports/`, ingests a CI Ledger, and publishes task records. The current workflows do not provide the single, exact-commit aggregate lifecycle required by this decision.

Repository evidence at branch `gpt`, commit `94f8bf2ec2c923f40df135b872eaa4a5327750b5`:

- `.github/workflows/ste-lint-changed.yml`, `ste-lint-full-docs.yml`, and `validate-document-standards.yml` use independent push triggers and workflow-specific concurrency/cancellation behavior.
- `.github/workflows/gh-actions-capture.yml` listens for completed workflow runs, runs reporting and Ledger ingestion, and publishes `.takeout/reports/`, task folders, and the task board.
- `.github/workflows/gh-actions-diagnostics.yml` also handles workflow-run events and push-based backfill, and publishes report/Ledger output.
- ADR-0003 defines the report artifact layout and evidence retention under `.takeout/reports/`. ADR-0007 makes that report index the latest lint-report locator.
- ADR-0004 defines task folders and subtasks, but its current completion model treats committed CI remediation and hosted validation as separate states. This decision changes post-commit validation into a universal completion gate while retaining the unaffected task-folder, parent/child, governance, and direct-deletion safeguards.

The current design couples validation reporting, finding identity, task publication, and report storage. It also leaves aggregate validation across independently triggered workflows to separate event processing. The approved design replaces that reporting architecture with one coordinator, a compact operational status index, and Worker-authored remediation folders.

This ADR records the user's approval of DRAFT-0010 revision 9 on 2026-11-28. It does not authorize weakening existing validation scope or deleting the old report system before its replacement is operational.

## Decision Drivers

- **Correctness and completion integrity — High:** A task must pass every required check for its exact current commit and protected policy revision.
- **Coverage integrity — High:** Missing, skipped, partial, cancelled, or unreported required checks must never count as success.
- **Reliable aggregation — High:** One coordinator must produce one complete outcome without races between independently completing workflows.
- **Security — High:** Task-authored contracts and scripts must not gain unrestricted commands, secrets, or publisher permissions.
- **Low-noise remediation — High:** One review task per terminal attempt and one child per distinct actionable root cause; no per-log-line or per-job task flood.
- **Recovery and idempotency — High:** Missed triggers, duplicate deliveries, concurrent publishers, and partial failures must be recoverable without infinite loops.
- **Bounded operational state — High:** Keep only recent and unresolved attempt records; do not recreate a permanent findings Ledger or diagnostic archive.
- **Non-blocking execution — High:** The Worker continues with other unblocked tasks while CI runs.
- **Migration safety — High:** Preserve every required check and baseline until the replacement has demonstrated equivalent or stronger coverage.

## Considered Options

### Coordinator architecture

#### Option 1 — One coordinator invoking reusable workflows and the generic verifier (chosen)

One coordinator runs for each source commit. It resolves the protected policy and exact-commit task contract, invokes established checks through reusable `workflow_call` entry points, invokes the generic verifier for uncovered requirements, and aggregates all required results in a final job.

- **Repository fit:** The existing validation workflows are separate push-triggered workflows. They must expose reusable entry points and stop creating duplicate task-validation cycles. The current Actions platform supports reusable workflows.
- **Good:** One coordinator owns the expected check set and terminal result. It can distinguish failed checks from missing/skipped checks and avoids inferring completion from separate workflow events.
- **Neutral:** Existing workflow internals can be reused, but their triggers and interfaces need coordinated refactoring.
- **Bad:** Migration touches established workflows and must preserve their triggers for unrelated uses where required.
- **Dependencies and burden:** Requires reusable workflow interfaces, protected policy, a contract schema, and a final aggregation job. Ongoing orchestration is centralized.
- **Risks and safeguards:** A coordinator defect could affect all task validation. Preserve established checks, use a finalizer that runs after failures, and demonstrate every terminal outcome and recovery path before retiring the old pipeline.
- **Evidence and confidence:** Current workflow source confirms independent push triggers and separate workflow-run reporting. Platform capability for reusable workflows is part of the approved design. No prototype or runtime validation was performed during Draft review.
- **Unknowns:** Exact contract schema, reusable-workflow interfaces, timeout values, and recovery cadence remain engineering details.

#### Option 2 — Independent push workflows plus a separate workflow-run aggregator

Keep established workflows as independent push-triggered runs. A separate aggregator consumes their workflow-run events, compares results against an expected-check manifest, and uses a missing-check timeout and recovery sweep.

- **Repository fit:** This is closer to the current independent-trigger model and requires less restructuring of existing workflow entry points.
- **Good:** Existing validation workflows can retain their primary triggers and most of their current shape.
- **Neutral:** The aggregator must correlate events by exact SHA and distinguish a genuinely missing workflow from one that has not started or completed.
- **Bad:** Event arrival order, cancelled/superseded runs, missing events, and expected-check timeouts create more coordination states. Recovery must reconstruct whether the full check set is terminal.
- **Dependencies and burden:** Requires an expected-check manifest, workflow-run correlation, timeout policy, and recovery logic in addition to every independent workflow.
- **Risks and safeguards:** Late or missing events can cause false incomplete outcomes or premature finalization. Exact-SHA correlation, grace periods, durable watermarks, and idempotency reduce but do not remove this coordination complexity.
- **Evidence and confidence:** The repository already uses workflow-run events for diagnostic capture. That proves event-driven capture exists, not that it provides complete aggregate validation. No aggregator prototype was tested.
- **Unknowns:** Actual event-delivery and timeout behavior under repository load has not been measured.

#### Option 3 — No change to the current independent validation and report-capture model

Keep the existing push-triggered checks and report/Ledger pipeline without introducing a single aggregate completion authority.

- **Good:** Avoids immediate workflow and report-system migration.
- **Neutral:** Existing checks continue to run under their current triggers.
- **Bad:** Does not establish one complete exact-SHA aggregate result or the approved completion gate. It retains the report/Ledger coupling and does not meet the approved architecture.
- **Repository fit and evidence:** This is the current repository model, as shown by the workflow sources listed above.
- **Decision:** Not viable for the approved goals.

### Run-status retention

#### Option 1 — Retain reconciled records for 14 days, then compact behind a verified checkpoint (chosen)

Keep each attempt record for 14 days after successful reconciliation. Never prune unresolved or partially reconciled attempts. After expiry, remove the individual record and rely on one small monotonic checkpoint that advances only after every earlier attempt is accounted for and reconciled.

- **Good:** Recent attempt details remain available for diagnosis and traceability, while old completed records do not accumulate indefinitely. The checkpoint preserves duplicate/delayed-event suppression after compaction.
- **Neutral:** Recovery correctness depends on checkpoint discipline. The 14-day period is a policy window, not proof that every possible external event delay is impossible.
- **Bad:** The system must implement safe compaction and prove that no unresolved gap exists before advancing the checkpoint.
- **Dependencies and burden:** Requires reconciliation state, ordered/paginated recovery, and a durable closed-through watermark.
- **Risks and safeguards:** An incorrectly advanced checkpoint could suppress an unaccounted event. Advance only after a complete sweep confirms no gaps or outstanding attempts. Never expire unresolved records.
- **Evidence and confidence:** The 14-day period is the user's explicit decision. The bounded-index and checkpoint behavior is a design safeguard; no production measurement exists yet.

#### Option 2 — Retain every attempt record indefinitely

- **Good:** Preserves the simplest complete per-attempt history and duplicate-event lookup.
- **Neutral:** Requires little compaction logic.
- **Bad:** The index grows continuously, contrary to the user's requirement to keep operational state lean.
- **Decision:** Rejected because indefinite growth is not acceptable.

#### Option 3 — Delete each attempt immediately after reconciliation

- **Good:** Minimizes the live index.
- **Neutral:** Requires a durable checkpoint to distinguish already reconciled events from missing events.
- **Bad:** Removes recent attempt detail immediately and makes delayed-event investigation less convenient.
- **Decision:** Rejected in favor of a bounded 14-day diagnostic window.

## Comparative Assessment

| Decision driver | Single coordinator | Independent workflow aggregator | No change |
|---|---|---|---|
| Complete exact-SHA aggregation | Strong: one owner and finalizer | Moderate: depends on event correlation and timeout/recovery | Weak: no single aggregate authority |
| Workflow migration | Moderate cost: reusable entry points | Lower initial refactor, higher aggregator complexity | Lowest immediate cost |
| Missing/late event handling | Explicit coordinator and recovery | Requires expected manifest, grace period, and recovery | Not adequately addressed |
| Long-term operational burden | Centralized orchestration | Distributed workflow and aggregator coordination | Retains existing report/Ledger coupling |

| Retention driver | 14-day plus checkpoint | Indefinite | Immediate pruning |
|---|---|---|---|
| Index growth | Bounded recent/unresolved records | Unbounded | Minimal |
| Recent traceability | Strong for 14 days | Strong indefinitely | Weak |
| Duplicate suppression after pruning | Checkpoint-based | Per-record history | Checkpoint-based |
| Recovery complexity | Higher than indefinite; guarded by sweep | Lower | Higher and loses recent detail |

The single coordinator is preferred because the repository needs one authoritative expected-check set and terminal outcome. The independent aggregator remains technically viable but adds event-correlation and timeout states. For retention, 14 days balances recent traceability with bounded growth. Indefinite retention conflicts with the user's explicit concern about index growth. Immediate pruning removes useful recent context.

## Decision Outcome

**Chosen coordinator:** Option 1 — one coordinator per source commit invoking established reusable workflows and the generic verifier.

**Chosen retention:** Option 1 — retain reconciled per-attempt records for 14 days, then compact/prune behind a verified monotonic checkpoint. Never prune an unreconciled attempt.

### Normative decision

1. GitHub Actions is the sole authority for implementation validation after a source commit. The Worker may inspect and correct changes before commit. After commit, the Worker does not run tests, scripts, lint, or other correctness checks and does not override CI outcomes.
2. Every task declares a machine-readable validation contract pinned to the exact source SHA or immutable contract revision. Protected repository policy defines mandatory checks. Task metadata may add checks but cannot weaken mandatory policy.
3. Established workflows remain preferred when they fully cover declared requirements. A thin dispatcher invokes established checks and one generic reusable verifier for uncovered requirements. The generic verifier supports registered adapters and repository-owned scripts.
4. The generic verifier accepts structured, typed arguments only. It rejects unrestricted shell strings, unsafe paths, unsupported adapters, excessive resource requests, and invalid contracts. It runs at the exact source SHA without secrets or write-capable tokens.
5. The privileged publisher runs separately with narrowly scoped write permission and does not execute untrusted task code.
6. One coordinator runs per source commit. It invokes required established checks through reusable `workflow_call` entry points and the generic verifier. Its final aggregation job runs even when validation jobs fail. Independent push workflows must not create duplicate task-validation cycles.
7. The aggregate binds every required result to the same repository, exact source SHA, check-set identity, protected policy revision, coordinator run ID, and attempt. A rerun is a distinct attempt. Missing, skipped, partial, pending, cancelled, or incomplete checks are never success.
8. Terminal outcomes are `success`, `check_failure`, `coverage_failure`, `infrastructure_failure`, `capture_failure`, `cancelled`, or `superseded`. A stale result never changes the current task state. A later successful rerun does not erase earlier failure work.
9. For each terminal attempt, publish one compact status record and one review-task folder atomically. Use run ID plus attempt as the idempotency key. Duplicate delivery creates no duplicate work. Do not cancel distinct pending finalizers or lose concurrent writes.
10. A scheduled recovery sweep compares coordinator run metadata and committed tasks awaiting CI with the index. It uses a durable watermark, safe pagination, bounded retries, and idempotent publication. It does not inspect logs or validate source code.
11. Status-index and review-task commits are metadata-only and excluded from source-validation triggers. Do not rely solely on bot identity to prevent recursive workflows. Do not automatically rerun failed checks.
12. The Worker sets committed tasks to **Committed / Awaiting CI** and immediately continues with other unblocked work. Review tasks join the ordinary queue and do not interrupt active work.
13. The Worker reads the index first. It opens Actions logs only after a recorded check, coverage, infrastructure, or capture failure, solely to diagnose actionable root causes. It does not inspect successful or obsolete logs.
14. The Worker creates one self-contained child folder per distinct actionable root cause, grouping related failing jobs/steps. Reuse an active matching child. Do not create one child per log line, assertion, job, or duplicate event.
15. Attach a child to the correctly identified active parent. If that parent is Done, deleted, or unavailable, use one permanent fallback parent. Never infer parentage or recreate a deleted parent.
16. Delete completed child folders and Done ordinary parent folders under the approved lifecycle. Never automatically delete the permanent fallback parent.
17. A task becomes **Done** only when the complete required check set succeeds for its exact current commit and policy revision, the result is reconciled, and no required subtasks remain.
18. Keep one compact run-status index under `workspace/`. Store only source Task-ID when valid, exact SHA, coordinator run ID/attempt, check-set identity, policy revision, completion timestamp, outcome, Actions URL, and recovery metadata. Do not store findings, signatures, logs, diagnostics, evidence, remediation state, or task history.
19. Retain individual attempt records for 14 days after successful reconciliation. Never prune unresolved or partially reconciled attempts, regardless of age. After expiry, remove individual records and advance a small monotonic closed-through checkpoint only after the recovery sweep proves that all earlier attempts are accounted for. Duplicate/delayed events at or below the verified checkpoint are no-ops.
20. Retire the complete `.takeout/reports/` tree only after every producer, consumer, schema, script, test, navigation entry, and document has migrated; the replacement is operational; existing validation coverage and baselines are preserved; and GitHub Actions has demonstrated success, failure, missing-event, duplicate-event, and publication-recovery behavior.
21. Do not preserve a parallel findings Ledger, diagnostic archive, or permanent attempt archive. Preserve unrelated lint/test/workflow coverage.

### Consequences

- **Good:** Exact-commit completion becomes deterministic. Missing coverage cannot be mistaken for success. One coordinator removes cross-workflow aggregation races. Remediation is grouped and attributable. Index growth is bounded without discarding unresolved work.
- **Neutral:** Established workflows need reusable entry points. The publisher, recovery sweep, and checkpoint add operational components. Recent reconciled attempt history is available for 14 days rather than indefinitely.
- **Bad:** The migration is broad and must preserve current validation coverage. A coordinator, contract, publisher, or checkpoint defect can block task completion until recovery. The permanent fallback parent requires ongoing queue hygiene.

### Confirmation

- [ ] Every task-validation source commit starts exactly one coordinator and binds to its exact SHA and protected policy revision.
- [ ] Established required workflows are callable through reusable entry points. The generic verifier runs only uncovered requirements and supports approved adapters and repository-owned scripts.
- [ ] Protected policy enforces mandatory checks. Task metadata cannot weaken the required check set or introduce unrestricted shell execution.
- [ ] Verification jobs have no secrets or write-capable token. The isolated publisher has only designated write access and executes no untrusted code.
- [ ] Aggregate success requires every required check to pass. Missing, skipped, partial, pending, cancelled, or mismatched results are non-success.
- [ ] Every terminal attempt produces exactly one status record and one review task. Duplicate deliveries and concurrent publication cannot lose or duplicate attempts.
- [ ] Recovery detects missing coordinator triggers and publication gaps, advances its watermark only after complete reconciliation, and uses bounded retries.
- [ ] Metadata-only publisher commits cannot recursively trigger source validation.
- [ ] Worker queue handling is non-blocking and review tasks do not interrupt active work.
- [ ] Worker reads the index first and opens logs only for diagnosis after recorded failure. It never independently validates or overrides CI.
- [ ] Root-cause grouping, active-child reuse, parent attribution, fallback routing, and direct folder deletion meet the approved lifecycle.
- [ ] The index contains only allowed operational metadata. Reconciled records expire after 14 days. Unresolved records never expire. Checkpoint advancement and duplicate suppression are covered by regression tests and recovery demonstrations.
- [ ] Existing required lint, test, build, schema, and workflow coverage and baselines are preserved.
- [ ] GitHub Actions demonstrates success, check failure, missing/skipped check, cancellation/supersession, duplicate delivery, concurrent publication, missed trigger, publisher failure, stale result, and recursion prevention.
- [ ] All `.takeout/reports/` producers and consumers have migrated. The replacement is operational before the complete directory and obsolete Ledger/report paths are retired.
- [ ] No parallel findings archive, diagnostic archive, or permanent per-attempt archive remains.

## Pros and Cons of the Options

### One coordinator invoking reusable workflows

- **Good:** One expected-check set and finalizer produce a complete aggregate result for the exact commit.
- **Neutral:** Requires existing workflows to expose reusable entry points and coordinated migration.
- **Bad:** Central orchestration becomes a critical component and needs explicit recovery and regression coverage.

### Independent workflows plus workflow-run aggregation

- **Good:** Preserves more of the existing workflow structure.
- **Neutral:** Requires a manifest, event correlation, missing-check grace period, and recovery.
- **Bad:** Late, missing, cancelled, and superseded events create more states and race conditions.

### No change

- **Good:** Avoids immediate migration.
- **Neutral:** Current independent checks continue to run.
- **Bad:** Does not deliver one complete aggregate authority or the approved exact-commit completion gate.

### 14-day retention plus checkpoint

- **Good:** Bounded index growth with a recent operational trace and safe duplicate suppression after compaction.
- **Neutral:** Requires checkpoint correctness and recovery verification.
- **Bad:** Removes per-attempt detail after 14 days, and checkpoint errors can suppress delayed events if safeguards fail.

### Indefinite per-attempt retention

- **Good:** Full per-attempt traceability without compaction.
- **Neutral:** Simpler duplicate lookup.
- **Bad:** Index growth is unbounded.

### Immediate pruning after reconciliation

- **Good:** Smallest live index.
- **Neutral:** Depends on a checkpoint for old duplicate suppression.
- **Bad:** Removes recent context immediately and makes delayed-event diagnosis harder.

## Implementation Scope

- **In scope:** Coordinator and reusable workflow interfaces; protected validation policy and task contract schema; registered adapters and repository-owned script interface; generic verifier; exact-SHA aggregate classification; isolated publisher; atomic/idempotent status and review-task publication; recovery sweep and checkpoint; Worker lifecycle and queue rules; grouped remediation folders and permanent fallback; migration of report producers/consumers, schemas, scripts, tests, navigation, documentation, templates, board, and active references; scoped reconciliation of ADR-0003, ADR-0004, and ADR-0007; retirement of `.takeout/reports/` after replacement proof.
- **Out of scope:** Weakening required checks or baselines; unrestricted task-authored shell execution; granting secrets or publisher permissions to verification code; automatic CI reruns; Worker post-commit correctness checks; per-job/per-finding task floods; a parallel findings Ledger or diagnostic archive; deleting `.takeout/reports/` before replacement proof; changes to unrelated lint/test/workflow coverage.
- **Tasks:** Implementation task linkage will be added after this ADR reaches accepted status. The current execution parent is `20261126-142500`.
- **Dependencies:** ADR-0003, ADR-0004, ADR-0007 (scoped supersession); Decision Governance; current task-folder and subtask templates; GitHub Actions and Worker policy.
- **Migration / rollback:** First map every current required check and baseline. Implement the coordinator and publisher alongside existing workflows without removing report producers. Demonstrate all confirmation scenarios. Migrate every consumer and reference. Only then retire the full report tree. Rollback before retirement by restoring the prior workflow triggers and report pipeline from the pre-migration commit. After retirement, rollback must restore the complete prior producers, consumers, schemas, and report data from the recorded migration commit; do not partially restore a parallel archive.

## More Information

- **Source Draft:** DRAFT-0010 revision 9, approved by the user on 2026-11-28. The source is retained until accepted ADR read-back and promotion cleanup pass.
- **Approved scope:** Exact scope stated in DRAFT-0010 revision 9 and its approved architecture decisions. No additional policy choice is introduced by this ADR.
- **Related ADRs and supersession scope:**
  - **ADR-0003:** Supersede its canonical report artifact layout and report-storage requirements under `.takeout/reports/`. Preserve unrelated lint/test/workflow validation coverage. Its report-layout decision no longer governs after the approved migration.
  - **ADR-0004:** Supersede only the clauses that treat CI remediation completion as commit/readback-only with separate optional hosted validation, and clauses requiring the old findings Ledger identity/history/archive lifecycle. Preserve the general task-folder/subtask model, genuine parent attribution, Worker ownership, direct deletion, task governance, and unrelated safeguards.
  - **ADR-0007:** Supersede its `.takeout/reports/index.json` latest-lint-report locator decision when the report tree is retired. Preserve no unrelated requirement from that report locator.
- **Evidence:**
  - User approval of DRAFT-0010 revision 9 and explicit coordinator and 14-day retention decisions, 2026-11-28.
  - Repository branch `gpt`, commit `94f8bf2ec2c923f40df135b872eaa4a5327750b`: current workflow sources listed in Context and Problem Statement.
  - `workspace/draft/DRAFT-0010-ci-error-task-folders-and-automatic-feedback-loop.md`, revision 9.
  - `workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md`, `0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md`, and `0007-unified-index-as-latest-lint-report-locator.md`.
  - No tests, prototypes, or hosted CI runs were executed or inspected during this decision promotion. Confirmation requires later implementation evidence.
- **Review trigger:** Any failed Confirmation criterion, material platform change, repeated publication/recovery failure, validation coverage change, or evidence that 14-day retention/checkpoint behavior loses required operational traceability.

## Decision Lifecycle History

| Date | Status / implementation change | Evidence and reason |
|---|---|---|
| 2026-11-28 | Promotion pending | User approved DRAFT-0010 revision 9 and instructed promotion. Provisional ADR created for completeness review. |
