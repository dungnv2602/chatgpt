---
name: the-worker
description: Manage repository sessions, task operations, document governance, CI, and decision records. Use for /start, repository work, task management, CI remediation, or governance tasks.
metadata:
  project-role: foundational
  format: agentskills
---

# The Worker

## Purpose

The Worker is the sole operational entry point for repository work. It owns session continuity, task operations, document governance, GitHub Actions, CI Ledger, and decision governance.

## Activation

Load The Worker during `/start`. Use it as the sole skill for cross-cutting repository operations. Load its domain references only when the current task activates them.

## Authority and scope

The Worker owns request capture, task hierarchy, selection, execution, continuity, and closeout. The task board is its published schedule, not a second scheduler.

Use repository `dungnv2602/chatgpt`, branch `gpt`, as the sole project source of truth. Use remote GitHub operations only. Do not use local shell, Python, container, or local Git for repository work. Do not inspect, poll, dispatch, rerun, or wait for hosted CI results.

Initialize only on the cue in `.agent/SESSION_START.md`. That file owns session initialization.

### Branch-first file reads and SHA provenance

- Read files from the intended branch by default. Do not select a commit SHA for ordinary file reads.
- A commit-specific read is permitted only when the SHA is explicitly supplied or obtained from a documented GitHub operation in the current workflow.
- Before using a SHA, identify and record its source. Never reuse an unexplained SHA from previous context, conversation history, or a stale lookup.
- If a commit-specific read returns `NOT_FOUND`, verify the exact path against the intended branch before concluding the file is missing.


## Material recovery and immediate cleanup

Recover task-required source material autonomously when it is accessible and within the approved task scope. Do not ask for permission solely to retrieve material needed to complete the task. Use the authoritative source and avoid unnecessary copies.

Treat downloaded, extracted, duplicated, or staged recovery artifacts as temporary. Delete each temporary artifact immediately after its last required use, and clean up all remaining temporary recovery artifacts at task closeout. Verify cleanup when possible and record the outcome. Do not retain temporary copies for convenience or future tasks.

This rule does not authorize deleting canonical repository files, source records, user-owned originals, retained evidence, or files whose preservation is required by an applicable workflow, policy, or explicit instruction. Keep required evidence and canonical materials in place. If an artifact is canonical or its ownership/retention is uncertain, do not delete it; resolve the uncertainty within existing governance or ask only if an essential authority boundary remains.

## Prompt capture — mandatory

Before answering or acting on a request with an identifiable outcome, find or create its task record. Capture questions, research, advice, writing, creative work, and project changes before delivering the result.

- **New objective:** create a parent task folder from `.agent/skills/the-worker/assets/TASK_TEMPLATE.md`.
- **Follow-up, correction, extension, or next step of an existing objective:** create a separate child record under that genuine parent from `.agent/skills/the-worker/assets/SUBTASK_TEMPLATE.md`. Do not overwrite an earlier prompt or silently enlarge its record.
- **Several related requirements in one prompt:** preserve the full prompt once in the parent and split its independently completable deliverables into child records. Unrelated objectives receive separate parents.

- **Clarification, decision, or approval that changes scope, priority, or authorization without adding a deliverable:** append its exact wording and UTC timestamp to Subsequent Instructions. Create a child when it adds work.
- **Greeting, reaction, or acknowledgement with no request or decision:** do not create a task.
- **Unclear parentage:** do not guess. Preserve the request in the discussion register and ask one concise question at quiescence.

Preserve every request with an identifiable outcome verbatim in its own parent task or follow-up subtask under Original Request/Original Prompt. Preserve non-deliverable clarifications, constraints, decisions, and approvals verbatim under Subsequent Instructions. Link the record from its parent index and keep the task board current. A request is not tracked solely because it appears in chat, a parent summary, or the discussion register.

Before creating a record, inspect active task records and the board. Before assigning a child ID, read the full parent task record and its subtask index. Include all Progress and closeout history. Treat every ID ever used in that parent as consumed, even after deletion. Choose the next unused sequential number. An empty index does not prove that an ID is available. Reuse a parent only when the objective is genuinely the same. A substantive follow-up still receives its own child record. Never place unrelated requests under one parent to reduce task count.

Every task and subtask record must retain the JSON `Validation Contract` block from its current template. Set `contract_revision` and `checks`. Use `[]` when no task-specific checks are required. Each implementation commit must carry one exact `Task-ID` trailer that resolves to one record in that commit's tree. The coordinator binds the contract to that commit's exact SHA. Missing or ambiguous attribution or contract data fails closed. Use only registered typed adapters and repository-relative entrypoints. Never add shell strings, credentials, environment overrides, or permission settings. Read `references/task-validation-interfaces.md` for the complete interface.

## Persistent skills-refactoring parent exception

The user designated a persistent parent for future skills refactoring. Its record is `workspace/tasks/20261127-173000/task.md` (Refactor Skills). Use this parent only for requests that genuinely concern repository-skill refactoring. Create a distinct child subtask from `.agent/skills/the-worker/assets/SUBTASK_TEMPLATE.md` for each qualifying request. Do not create a replacement parent for a new deliverable or future phase. Keep the subtask index and board reconciled. Close and delete completed child records after normal closeout. **Never mark this parent Done or Cancelled or delete its task folder** unless the user explicitly instructs you to do so. This narrow exception does not permit unrelated work under this parent.

## Task hierarchy and CI attribution

A user task is the genuine parent. Its follow-up requests and CI remediation are child subtasks. Never infer parentage from the current execution pointer, changed files, workflow names, branch, or timing.

Every task-specific implementation commit must include one exact commit trailer:

~~~text
Task-ID: <active-task-or-subtask-id>
~~~

The task-validation publisher preserves the source Task-ID from the exact source commit. If it names a subtask, resolve that child's Parent Task ID. A valid, active, user-originated parent takes precedence. If the marker is missing, malformed, ambiguous, unsupported, or resolves to a missing, inactive, deleted, or non-user parent, use only the permanent fallback parent configured by worker_lifecycle.fallback_parent_id in the Worker-owned task-validation policy. Its current record is workspace/tasks/20261128-193800/task.md. Verify the policy ID and the fallback record's matching ID, Origin: Assistant, Status: In Progress, Current execution: No, and subtasks index. If any check fails, fail closed; never infer a substitute or create another fallback. The fallback parent is permanent, never Current Execution, never Done/Cancelled, and never deleted.

### Task-validation review queue

The Worker is non-blocking while validation runs. After committing a task-specific change, continue with the next eligible task; do not poll, wait for, dispatch, rerun, or inspect hosted CI. The publisher and recovery workflow own result capture. When assigned to reconcile the review queue, read workspace/task-validation/status-index.json first.

After each task-specific source commit, update the task record's Validation Lifecycle JSON block with state `awaiting_ci`, the exact source SHA, and that commit's policy blob SHA. This is a metadata-only commit and must not trigger source validation. Do not put lifecycle data in the compact status index. The recovery sweep compares awaiting task records with indexed attempts and dispatcher runs. It starts a missing exact-SHA dispatch only when source and current policy activation and default-branch workflow availability are verified. Otherwise it leaves the task awaiting CI and reports the unmet gate. Cancelled and superseded attempts do not change task lifecycle state.

- Success: do not inspect logs or create feedback children. Reconcile the attempt after checking whether its exact source SHA is still the task's current commit; when current, set lifecycle state `passed`, record run/attempt/outcome/reconciliation time, mark the index record reconciled, and remove its review folder. A stale result must not overwrite the current task lifecycle. Only mark the task Done when the complete required check set succeeds for that exact current SHA and policy revision and no required subtasks remain.
- Cancelled or superseded: no logs, review folders, feedback children, or task-state changes. These attempts are not feedback work.
- check_failure, coverage_failure, infrastructure_failure, or capture_failure: set lifecycle state `review_required` only when the result SHA is current. Inspect Actions logs only for the recorded actionable failure and only when hosted inspection is authorized. Diagnose root causes, not individual log lines. After recording/reusing remediation children, set lifecycle state `reviewed` when current, mark the index record reconciled, and remove its review folder.
- Group related failed checks/jobs/steps by diagnosed root cause and genuine parent. Create or reuse one active P0, Approved child per distinct root cause. Do not create one child per check, job, assertion, log line, or duplicate attempt. Derive a stable `rc-<16 lowercase hex>` group ID from the normalized root-cause signature plus parent ID, store it in the child's `Root-cause group` field, and reuse only an active child with the same parent and group ID. Do not use the legacy Ledger group for new task-validation remediation.
- Resolve the source Task-ID to its active genuine parent; otherwise route to the single permanent fallback parent. Never use the current board pointer as a substitute.
- After review, mark the attempt's recovery.reconciled_at timestamp and remove its review folder. Keep the compact status record for three days after reconciliation. Unresolved records never expire and must stop checkpoint advancement.
- The status index stores only the ADR-0008 compact attempt fields. Never add findings, root-cause signatures, logs, diagnostics, evidence, remediation state, or task history to it.

The legacy CI Ledger owns only pre-migration report findings until every legacy producer and consumer has migrated. Do not create a second findings archive for task-validation attempts. The Worker owns task-validation diagnosis, grouping, attribution, child creation, and task lifecycle. The Ledger does not schedule.

CI remediation children are P0, Approved, and Ready under the standing authorization. Use Proposed only when that remediation requires a specific unresolved decision. Routine implementation does not need a new ADR merely because it changes code. Keep a genuine decision gate narrow to the dependent work.

## Status, approval, and scheduling

Approval records authority for a scope. It does not depend on status or priority. Record its source and scope. Never infer approval from status. **Approval is not execution authorization and never triggers execution by itself.** The universal execution directive is `execute`, matched case-insensitively when clear directive intent is present; its semantics and persistence are defined in the canonical Execution cue and authorization lifecycle section. Quoted, discussed, hypothetical or negated mentions are not directives.

Use these statuses: Proposed, Ready, In Progress, Blocked, Paused, Done, and Cancelled. Ready requires satisfied dependencies and any real decision gate. Use Blocked for a genuine external or user-resolvable blocker. Use Paused for intentional suspension.

The Worker is the sole scheduler. Verify eligibility and dependencies first, then priority and age. Keep dependency-waiting work out of the eligible queue. Detect cycles. do not repeatedly retry an impossible dependency chain. Correct an edge only when the error is clear and authorized. Ask for essential input only at quiescence.

The board publishes:
- one Current Execution pointer, or none.
- the ordered eligible queue.
- the next task.
- deferred tasks and their reasons.

Do not duplicate the queue in task records, README files, or skill references. The Ledger does not schedule.

## Canonical instruction ownership and drift prevention

The Worker is the sole operational authority. Session Start is only the cue guard and pointer. Conversation Mode defines presentation settings only. Initialization policy, skills indexes, catalogs, boards, templates, and discussion registers must not independently redefine operating procedures. Follow the owner and its references. Reconcile duplicate wording into pointers.

### Initialization orchestration

- The only foundational initialization cue is `/start`. Treat quoted, discussed, or hypothetical uses as non-cues.
- Do not load repository instructions, skills, or references at conversation start unless an explicit cue or task-specific activation condition requires them.
- On `/start`, follow Session Start to this Worker. Read `.agent/WORKFLOW_MAP.md` for an overview before loading task-related skills or references. Read the mandatory Conversation Mode settings reference. Use the current-conversation verified-load ledger.
- Complete the startup notice, required repository/task-state verification, progressive loading, startup P0 batch drawn only from eligible tasks in the workspace, and queue-draining procedure defined here and in the required references before accepting the substantive prompt. Session initialization is not a CI task: do not inspect `.takeout/reports/`, CI report indexes or history, or the CI Ledger; do not collect a CI baseline or reconcile Ledger state during startup. An explicit user instruction may supersede a particular startup gate for a scoped task; record the exact override in its task record, bypass only the named gate and scope, and do not imply skipped verification passed.
- Load novelist initialization instructions from `references/novelist-initialization.md` only after foundational initialization passes and the user explicitly requests the novelist role.
- Load drawing-session instructions from `references/drawing-session-initialization.md` only after foundational initialization passes and the user explicitly requests a drawing session or the procedure requires it.
- The Worker routes initialization. Session Start and Conversation Mode do not own operational procedures.

### Mandatory pre-action self-check

Before repository work, review the task's authority and current workflow. Confirm:
1. The canonical instruction owner and required references are verified.
2. The task and parentage are correct. The scope and approval are explicit.
3. Dependencies, status, and execution eligibility are reconciled.
4. No conflicting instruction or duplicate rule creates an ambiguous execution boundary.
5. Each planned file has one registered canonical owner and an allowed path. A consumer path is not treated as its owner.
6. The child ID is unused in the full parent history. Deleted child IDs remain consumed.
7. Any required decision collection is reconciled in the written cue order before dependent work begins; approval alone never triggers execution.
8. Applicable execution mechanisms, scope, recovery, verification, readback, and cleanup are defined; batch boundaries are scheduling details, not cue semantics.

If any check fails, resolve it before the affected work. Do not silently bypass a gate.

### Instruction conflict and drift control

Treat conflicting or stale instructions as a workflow fault. Inventory the conflict, locate the canonical owner, reconcile secondary files to pointers, and verify the changes before continuing. Do not append duplicate rules as a quick fix. When a missing rule is identified, add it only to its canonical owner. When an existing rule was not followed, strengthen the gate or verification rather than copying the rule elsewhere. Review associated templates and indexes whenever their owner contract changes.

## Execution, recovery, queue draining and closeout

Treat the user's authorized workstream or reconciled scope as the execution boundary. Batch is a scheduling mechanism only. Execute eligible work recursively to quiescence within scope, then report once.

### Protect the user's solitude — interruption and reporting gate

The user's explicit preference is to be left undisturbed while authorized repository work proceeds. Treat interruption minimization as a mandatory execution constraint, not a conversational courtesy.

- **No progress pings:** Do not send interim updates, status narration, check-ins, confirmation requests, or “still working” messages during an authorized batch. Do not use partial/progress responses to announce tool work. Communicate only at the batch's quiescence, except for an exceptional issue that is urgent, safety-critical, or requires stopping to avoid an irreversible action outside authority.
- **Do not surface isolated blockers:** Recover, investigate, correct, defer, or isolate routine/recoverable issues within repository scope. Continue independent eligible work. A failed call, uncertainty, stale note, missing nonessential evidence, or routine choice is not grounds to interrupt.
- **Aggregate intervention:** Only interrupt at quiescence when a substantial set of concrete blockers or decisions is genuinely user-resolvable and prevents further authorized progress, or when a single exceptional issue requires immediate intervention. Exhaust available repository evidence and recovery first. Consolidate all such issues into one concise report, specify precisely what decision/input is needed, and avoid asking about issues the user cannot resolve.
- **Quiet autonomous completion:** Continue the authorized batch recursively to quiescence, including implementation, tracking, readback, closeout, queue rebuilding, and independent work beyond skipped blockers. Do not stop merely because one task is blocked or because a commit was made.
- **Final communication:** At quiescence, report completed outcomes, material limitations, and only the aggregated actionable blockers. If no intervention is required, keep the report brief. Do not manufacture a question, request renewed permission for already-authorized scope, or imply that the user must supervise routine execution.
- **Authority remains bounded:** This interruption rule does not grant new scope, bypass approval/decision gates, permit restricted validation, or authorize irreversible actions. If a genuine authority boundary cannot be resolved safely, isolate it and continue unrelated work; report it only when intervention is necessary.


### Mandatory operation-level worklist

A task-level queue or status snapshot is not sufficient to drive execution or prove quiescence. For every authorized execution directive, maintain a concrete, reconciled worklist of independently completable operations for the authorized scope. Persist the worklist in the active task/subtask Progress or Handoff record when repository work is underway; for non-repository actions, maintain it in the conversation's execution context and reconcile it before every scheduler transition.

Each worklist item must identify:
- the task/acceptance criterion or outcome it advances;
- a bounded operation (not a vague task-level label);
- state: eligible, executing, completed, blocked, deferred, or cancelled;
- prerequisites and whether those prerequisites are local to this operation;
- blocker or recovery condition, if any;
- next action or reassessment trigger;
- evidence/commit/readback when completed.

**Decomposition is mandatory:** Before accepting a blocked task as blocked, enumerate its remaining acceptance criteria and split them into operations. Split further whenever an operation can proceed without the blocked prerequisite. A blocked parent or child must never hide eligible work within its own scope. A blocker applies only to the operations that require it.

**Scheduler transition protocol:** After every operation outcome (completed, blocked, failed, interrupted, deferred, or prerequisite change), reconcile the worklist and immediately choose the next eligible operation. Rebuild eligibility based on current evidence rather than preserving a stale queue. Do not stop at assessment, reconciliation, readback, tracking, commit, or reporting while operations remain eligible. Completion of a task/child is itself a scheduler transition; continue to the next eligible item without a new cue.

**Recovery:** Failed or interrupted operations first reconcile actual effects, source state, authorization, and duplicate risk. Resume or retry only remaining work; do not repeat completed effects. Routine recovery, task decomposition, record updates, commits, readback, and queue reselection remain covered by active authorization. Revisit a blocked item only when its stated trigger changes, unless source investigation reveals a safe recovery path.

**Quiescence evidence:** The final stop-proof must reconcile (a) every in-scope task and acceptance criterion, (b) its decomposed operations and states, (c) all dependencies and blockers, (d) recovery/continuation options, and (e) that no eligible or directly necessary operation remains. A blocked task is not proof of quiescence if its residual work has not been decomposed. A status scan or closeout report alone is insufficient. Only genuine scope exhaustion or a boundary that prevents all remaining work may stop the batch.

1. **Reconcile and select:** Read the board, parent/child indexes and records. Recursively check orphan records, missing indexes, stale paths, duplicate IDs, status/dependency mismatches, and pauses. Recover records from repository evidence and templates when possible. Then construct or reconcile the operation-level worklist. Do not declare quiescence from a shallow scan.
2. **Check eligibility:** Confirm scope, approval, dependencies, decisions and authorization before priority and age. Detect dependency cycles. Resume only stale/dependency-based pauses when authority remains valid. Preserve intentional pauses.
3. **Execute and decompose:** Execute the next eligible bounded operation. Decompose residual task acceptance criteria around blockers; recover source material, make routine decisions and correct errors within scope. Do not interrupt for isolated blockers or routine updates.
4. **Record evidence:** Capture decisions, progress, paths, commits, readback, checks and limitations in task records/worklist. Every task-specific implementation commit must carry the exact `Task-ID: <task-id>` trailer.
5. **Close implementation:** Mark a task Done when its acceptance criteria are met and its intended-branch commit is read back. Runtime checks are not universal gates. Do not claim checks that were not performed. Record verification debt separately. A parent cannot be Done while required children remain open.
6. **Rebuild and continue:** After every operation or status/dependency transition, reconcile the worklist and immediately select the next eligible operation within the authorized focus. A completed child or task is a scheduler transition, never a reporting pause.
7. **Skip blockers locally:** Exhaust repository recovery and source investigation first. Isolate the operation, record its precise cause and reassessment trigger, and continue independent/remaining work. A failed tool call or recoverable uncertainty is not a blocker.
8. **Reach quiescence:** Stop only after the operation-level stop-proof gate confirms no eligible or directly necessary recoverable operation remains within scope. Reconcile user-resolvable blockers and present one consolidated decision brief. Do not ask about external blockers the user cannot resolve.
9. **Collect decisions and process cues:** Log decisions and reconcile cues in their written order. `Next` is navigation only. An execution directive applies universally to the eligible work within its reconciled scope; do not require another cue for routine continuation or already-authorized work. A genuinely new scope or authority boundary requires the appropriate authorization.
10. **Close records:** Read back each deliverable and tracking record. Delete completed/cancelled child folders and board rows under the normal lifecycle. Preserve the persistent skills-refactoring parent when its exception applies. Do not archive or create retention copies. Preserve Ledger identity and history.
11. **Cleanup:** Remove temporary recovery artifacts immediately after last use and verify cleanup when possible.

Do not run local repository scripts, tests or lint. Do not inspect hosted CI results unless explicitly authorized. Commit/readback evidence does not prove runtime behavior.
## Workflow map maintenance and display cue

- `.agent/WORKFLOW_MAP.md` is the canonical workflow overview. It routes to authoritative owners and references and does not replace them.
- The `/map` cue displays the current map only. It does not initialize, load additional skills, reconcile startup, or execute.
- Whenever a workflow, cue, activation prerequisite, ownership boundary, or operational route changes, update the map in the same governed change cycle. Read back the map and changed owner documents before commit.
- At `/start`, Session Start requires the Workflow Map to be read first for overview, before loading The Worker or any related skills/references. Then load The Worker.

## Execution cue and authorization lifecycle

The explicit `execute` directive is **universal**: it authorizes execution of eligible, previously approved and in-scope work and applicable actions. The cue is not defined or limited by batch execution. Batch is one scheduling mechanism; the execution mechanism depends on context. A clear directive may initiate implementation, continue or resume work, perform necessary preparation/reconciliation and proceed, drain eligible queues, or carry out other authorized actions. Interpret the complete message and directive intent rather than requiring a standalone token or isolated message.

Recognize explicit workflow cues in their written order, within the complete message. Distinguish actual directive use from quoted, discussed, tested, hypothetical, or negated mentions. Parse surrounding instructions, constraints and scope. Do not manufacture retroactive authorization: an action must be authorized at the point it occurs.

- **`execute`:** universal execution directive. After reconciling scope, approval, dependencies, and gates, execute applicable eligible work and continue through preparation, reconciliation, implementation, recovery, transitions and queue selection until genuine quiescence or a real boundary.
- **`approve` / approval:** record the decision and scope; approval alone does not initiate execution. When cues are ordered together (e.g., Approve then Execute), reconcile approval first, then evaluate Execute against the newly eligible state. Do not require separate messages.
- **`Next`:** decision-queue navigation only. Keep the current blocker unanswered and unresolved; present the next unresolved decision. It cannot approve or execute.
- **Other instructions:** capture, interpret and record as governed; do not treat non-execution instructions or implied intent as execution authorization unless they clearly include an execution directive.
- **`/start`:** distinct session initialization governed by Session Start; not an execution cue.

### Authorization persistence

An issued execution authorization remains active for its applicable scope through routine preparation, decomposition, reconciliation, implementation choices, tracking updates, commits, readback, recovery, safe retries, task transitions and queue reselection. These procedural milestones do not consume, reset or interrupt authorization. Redundant cues do not narrow, restart or interrupt the active authorization. Reconcile actual effects before retrying; prevent duplicate work or records where practical.

Routine execution work, corrective actions, evidence and tracking needed to fulfill the approved objective are within scope. Independently valuable objectives or genuine scope, safety, privacy, policy, permission or other authority boundaries are not automatically included. If a boundary requires additional approval or authorization, isolate that work, record the exact boundary and continue independent work. Do not use a boundary as a reason to stop unrelated authorized work.

### Execution invariant and recovery

### Blocker-locality invariant — mandatory scheduler enforcement

A blocker, restriction, failure, unavailable evidence, or authority gate is local to the operation it actually prevents. It is **not** a terminal signal for the universal execution directive, authorization lifecycle, task, batch, or workstream.

When an operation cannot proceed:
1. Identify the exact blocked operation and the narrowest applicable restriction or missing prerequisite. Do not broaden its scope by implication.
2. Isolate and record/defer that operation without consuming, suspending, resetting, or revoking authorization for unaffected work.
3. Immediately re-evaluate the authorized scope and scheduler queue. Select and execute the next eligible independent operation; include directly necessary recoverable preparation, reconciliation, retries, and transitions.
4. Revisit the blocked operation only when its prerequisite changes or an authorized recovery path becomes available. Avoid repeated futile retries or polling.
5. Do not report, ask for input, or transfer control merely because a blocker was encountered. Aggregate intervention at quiescence unless the boundary is urgent or all remaining progress is genuinely prevented.

**Stop-proof gate:** Before ending an active execution authorization, reconcile all remaining in-scope operations, their eligibility, dependencies, recoverability, and blocker scope. A stop is valid only when scope is exhausted, no eligible or directly necessary recoverable operation remains, or a genuine boundary prevents all remaining progress. A restriction on one operation cannot satisfy this stop condition while independent authorized work remains. A report is closeout, never a scheduler transition or substitute for execution.

Before and during execution, reconcile the cue and its ordered operations, scope, authorization, eligible work, dependencies, actual changes and outstanding operations. A readback, status reconciliation, preparation, acknowledgment or report alone is not fulfillment when eligible work remains. Resume after interrupted or partially completed operations by reconciling evidence first; retry safely when recoverable, and isolate only genuinely unrecoverable blockers. Never infer quiescence from a shallow scan or a procedural checkpoint.

Continue queue selection and execution until no eligible work or directly necessary recoverable operation remains within the active scope, the scope is exhausted, or a genuine boundary cannot be resolved. Stop at quiescence or a mandatory safety/authorization boundary, not merely because a task, commit, readback or reassessment finished. Collect and present unresolved user-resolvable blockers only at quiescence, one at a time as governed by decision collection. Do not ask the user to supervise routine execution.

At `/start`, follow `.agent/SESSION_START.md`. Do not inspect hosted CI results.
## Parent selection — scope test and hierarchy correction

Create a parent task for each distinct user objective. Do not treat the active parent, current execution pointer, repository, project, or general maintenance theme as sufficient grounds for parentage.

Before selecting parent or child, compare the requested outcome against the candidate parent's original objective and acceptance criteria:

- **Same objective:** the request advances, completes, corrects, or extends an outcome already defined by that parent. Create a child when it is a distinct deliverable or substantive follow-up. record a non-deliverable decision/clarification in Subsequent Instructions.
- **Different objective:** the request creates an independently valuable outcome or changes a separate system or concern. It does not materially contribute to the candidate parent's acceptance criteria. Create a new parent, even when another parent is active or the work touches the same repository, files, or broad theme.
- **CI remediation exception:** CI findings may be children only of the genuine user task attributed by the source commit's Task-ID trailer, as governed above. This attribution rule does not authorize ordinary user work to be nested under that task.
- **Uncertain relationship:** compare objectives and criteria explicitly. If no genuine parent can be established without guesswork, leave parentage unassigned and ask at quiescence. Do not default to the current parent.

Before creating or updating a task, audit the proposed relationship. If the parent does not fit, correct it before scheduling. Create the genuine parent. Move or recreate the record under it. Update both indexes and board links. Preserve the original prompt, approval, status, dependencies, progress, commit evidence, and history. Then delete the stale child link. Never change parentage silently or discard evidence. A parent-child relationship is valid only when the child directly advances the parent's defined objective.

## Document governance — mandatory template-first gate

The Worker owns document governance. Apply this gate before creating, moving, renaming, materially revising, or validating any repository artifact, including non-Markdown files.

1. Identify the target path, canonical owner, document type, and allowed location. Do not infer ownership from a consumer path.
2. Read the current entry in `references/document-type-catalog.md`.
3. Read the format source that matches the catalog class:
   - **Template required:** Read the complete canonical template.
   - **Schema required:** Read the schema and relevant validator or tests.
   - **Embedded contract:** Read the owner file that defines the format.
   - **Generator-owned:** Read the generator, schema, and relevant tests.
   - **Lightweight pattern:** Read the documented pattern and owner instructions.
   - **Exempt:** Preserve the approved form. Do not add a template requirement.
4. If the catalog entry is missing or unclear, stop before editing the target. Propose the required format to the user.
5. If a required template or format contract does not exist, do not modify the target. Propose a suitable format and explain its purpose, intended use, fields, ownership, and validation.
6. Wait for the user's explicit approval of the proposed format. Do not create the template or edit the target before approval.
7. After approval, create the canonical template or contract. Update the catalog, owner index, and workflow. Read back and commit this format setup first.
8. Before editing the target, explicitly assess the canonical format for freshness against the current document, repository state, workflow, standards, and source evidence. Decide whether the template/contract itself needs correction or extension. If it does, update the canonical format first within approved scope, reconcile its catalog and owner pointers, commit/read back that format change, and only then revise the target using the updated format. If it does not, record or act on that assessment without unnecessary template churn.
9. Read the complete current canonical template or format source after any update and before modifying the target. Create or revise the target from that current format.
10. Preserve required fields, provenance, chronology, approved content, and facts. Include conditional sections only when applicable. Delete unused placeholders. Do not invent approvals or values.
11. Update indexes and links. Check the target against its format and writing or data standard. Read back every changed path and commit.
12. Use Reserved for a verified Markdown or non-Markdown family with no current record. Change Reserved to Active in the commit that creates its first record.
13. Do not mass-migrate untouched history. Do not create a template when an approved embedded contract, schema, or generator already defines the format.

For a one-off note or creative document, follow an explicit Lightweight pattern or Exempt catalog entry. If no such entry exists, propose the format before editing. Source code, generated output, schemas, and machine-readable data follow their own contracts.

The non-Markdown coverage table registers governed files under `.agent/skills/` and `.github/`. Each file must match exactly one family and its placement rule. A Worker-owned policy, schema, registry, or configuration belongs in the Worker skill's `assets/`. Explanatory guidance belongs in `references/`. Executable tools belong in `scripts/`. GitHub Actions workflow definitions belong in `.github/workflows/`. They consume Worker-owned contracts without owning them. Fail closed when the catalog has no matching family or the canonical location is unclear.

### Document-format classes

- **Template required:** Read and copy the canonical template for each new record.
- **Schema required:** Read and validate structured records against their schema.
- **Embedded contract:** Read and follow the format in one live owner file, workflow, or script.
- **Generator-owned:** Read and follow the generator and its tests.
- **Lightweight pattern:** Read and use an approved small structure for a low-risk or one-off note.
- **Exempt:** Preserve creative freedom or an approved external format.

The catalog defines purpose and document type, required and conditional fields, formats, allowed values, status, approval, provenance, stable IDs, parent links, migration, validation, owner, and canonical path. Treat unmarked fields as required. Mark Optional and Conditional fields explicitly. Use Unknown or Not applicable when appropriate. Keep workflow metadata out of creative prompts and user-facing fields.

Canonical copy-ready formats are in `.agent/skills/the-worker/assets/`. See its README for the asset index. The catalog and validator are Worker-owned assets in `references/` and `scripts/`. The catalog owns document-type, Markdown, and governed non-Markdown coverage integrity. The validator checks catalog structure, references, placement, and coverage. It does not certify semantic conformity. Do not weaken validation. Keep the catalog and owner indexes aligned.

When you create or materially revise a template, scan every repository template. Compare each template with current workflows, repository structure, and governing standards. Update each confirmed stale template and its owner references. Store every reusable template in its owning skill's `assets/` directory. Do not create project-local or workspace-level template copies. Reconcile the catalog, indexes, and inbound links.

## Worker-owned domain operations

The Worker is the sole activation and governance entry point for document governance, GitHub Actions, CI Ledger operations, and decision governance.

These procedures are Worker-owned references, not separate Agent Skills. Do not activate them as standalone skills.

Load the relevant reference only when the task requires it:

- `references/ci-ledger.md` only for an assigned, selected CI task in the workspace that requires report intake, finding attribution, grouping, lifecycle, or Ledger integrity.
- `references/github-actions.md` only for an assigned, selected CI task in the workspace that requires workflow design, diagnostics, technical remediation, or validation procedures. Load it with the CI Ledger reference only when that task needs both.
- `references/decision-governance.md` for Drafts, ADRs, repository analysis, implementation linkage, or Confirmation.
- `references/task-validation-interfaces.md` for ADR-0008 policy, contract schema, adapter registry, or coordinator interface work.

The Worker owns document governance in this file and its canonical document-type catalog. The Worker does not activate a separate document-governance skill.

Keep these decision controls in force:

- Decision approval and task execution approval are separate.
- Do not implement a proposal before the user approves its exact Draft revision and scope and its ADR reaches accepted status.
- Every new implementation task must link one or more accepted ADRs. Grandfather existing tasks.
- Keep accepted ADR context, options, and outcomes immutable. Use a new Draft and ADR when a decision changes.
- P0 priority does not bypass decision governance.

## Diagnostic investigation before blockers

For an assigned CI task in `workspace/tasks/` that depends on CI-generated or workflow diagnostic evidence, exhaust the evidence already published in the repository before declaring the task Blocked. This diagnostic procedure does not authorize CI investigation for ordinary tasks or during initialization.

1. **Read the complete indexed report.** Read the report JSON as well as its Markdown summary and index. Follow the published report path. Do not search report history or inspect hosted CI unless separately authorized by the applicable policy.
2. **Read diagnostic payloads, not just summaries.** Examine failed check names, status and exit codes, captured stdout/stderr, tracebacks, failing assertions, diagnostic locations, per-file records, normalized findings, and relevant metadata. Inspect the exact payload fields that apply. Do not treat a summary that omits details as proof the details are unavailable.
3. **Trace the diagnosis in repository source.** Follow diagnostic locations and output into the affected workflow, script, generator, tests, configuration, or report producer. Read relevant source and tests. Use repository evidence to establish the cause and scope before you correct the issue.
4. **Separate committed diagnostics from hosted CI access.** A diagnostic report or log committed to the repository is repository evidence. Reading it is not hosted CI result inspection. The restriction against hosted CI inspection does not prohibit reading already-published repository files. Do not fetch, poll, dispatch, rerun, or inspect hosted CI unless explicitly authorized.
5. **Investigate reporting gaps as defects.** If a report, capture, or summary omits information needed to diagnose a failure, investigate the reporting/capture mechanism and correct the defect or create a task for it. Do not automatically block the original remediation solely because the summary is insufficient. Continue with independent source investigation where possible.
6. **Blocker discipline.** Declare Blocked only after you exhaust repository evidence and source investigation within the permitted scope. State which evidence or access you lack. List the paths and diagnostic fields you examined. Explain why you cannot continue repository-side investigation. State what specific external or user input you need. Uncertainty alone is not a blocker.
7. **Read back and record.** Read back the exact relevant repository sources and task records after changes. Record examined report paths, concrete diagnostic details, source locations, commit SHAs, and limitations. Do not claim validation that was not performed.

This procedure applies before task selection, status changes, blocker declarations, and remediation closeout. It does not authorize local execution, hosted CI review, or any other restricted action.



## CI and Actions operational ownership

The Worker owns GitHub Actions operations, the task-validation review queue, and the remaining legacy CI Ledger until its migration gates pass. CI work is task-scoped and workspace-bound: handle it only for an assigned task under workspace/tasks/ and within the user's authorized scope. A startup P0 batch does not authorize CI baseline collection, status-index/report-history reads, Ledger reconciliation, hosted inspection, or remediation. Load CI references only for the selected CI task that requires them.

The task-validation status index under workspace/task-validation/ is the canonical compact status record for ADR-0008 coordinator attempts. It is not a findings archive. The legacy .takeout/reports/ family remains intact for pre-migration lint and non-task-validation workflow producers/consumers until every consumer is migrated and Confirmation permits retirement. Do not scan it during startup or unrelated work. Do not add task-validation findings or logs to either index.

## Canonical CI implementation

- Worker-owned scripts and regression tests: .agent/skills/the-worker/scripts/.
- Worker-owned schemas, policies and templates: .agent/skills/the-worker/assets/.
- Workflow execution and reusable capture entry points: .github/workflows/.
- ADR-0008 status index, checkpoint and review queue: workspace/task-validation/.
- Legacy report outputs, history, and Ledger state pending staged migration: .takeout/reports/.
- Legacy lint report generator, schema, template, and tests under Worker ownership: .agent/skills/the-worker/scripts/generate_lint_report.py, test_generate_lint_report.py, and .agent/skills/the-worker/assets/lint-report-schema.json, lint-report-template.md. Coordinator mode retains regression coverage but skips legacy index lookup and report publication.

Do not maintain duplicate implementations in report-family script directories. Workflows consume Worker-owned scripts and assets; they do not own the policy, schemas, or task lifecycle.
