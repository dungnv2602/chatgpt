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

Before creating a record, inspect active task records and the board. Reuse a parent only when the objective is genuinely the same. A substantive follow-up still receives its own child record. Never place unrelated requests under one parent to reduce task count.

## Persistent skills-refactoring parent exception

The user designated a persistent parent for future skills refactoring. Its record is `workspace/tasks/20261127-173000/task.md` (Refactor Skills). Use this parent only for requests that genuinely concern repository-skill refactoring. Create a distinct child subtask from `.agent/skills/the-worker/assets/SUBTASK_TEMPLATE.md` for each qualifying request. Do not create a replacement parent for a new deliverable or future phase. Keep the subtask index and board reconciled. Close and delete completed child records after normal closeout. **Never mark this parent Done or Cancelled or delete its task folder** unless the user explicitly instructs you to do so. This narrow exception does not permit unrelated work under this parent.

## Task hierarchy and CI attribution

A user task is the genuine parent. Its follow-up requests and CI remediation are child subtasks. The Ledger must never create a synthetic parent for a file, rule, workflow, job, or CI finding.

Every task-specific implementation commit must include one exact commit trailer:

```text
Task-ID: <active-task-or-subtask-id>
```

The CI report must preserve this source task ID. If it names a subtask, resolve its Parent Task ID. Create CI remediation children only when the source ID resolves to an existing, active, genuine user parent. If it does not resolve, retain the finding in the Ledger as unassigned. Never infer attribution from the current board pointer, changed file, workflow name, branch, or timing.

The CI Ledger owns finding identity, evidence, grouping, and child creation. It may update only the attributed parent’s finding summary, its child records, and its subtask index. It must not create parent tasks, change parent status/priority/current execution, or edit the task board.

CI remediation children are P0, Approved, and Ready under the standing authorization. Use Proposed only when that remediation requires a specific unresolved decision. Routine implementation does not need a new ADR merely because it changes code. Keep a genuine decision gate narrow to the dependent work.

## Status, approval, and scheduling

Approval records authority for a scope. It does not depend on status or priority. Record its source and scope. Never infer approval from status. **Approval is not execution authorization and never triggers execution.** The sole execution cue is the explicit standalone word `execute`, matched case-insensitively (for example, `Execute` or `EXECUTE`). Other words, instructions, approval, `Next`, `proceed`, quoted or discussed cue mentions, and implied intent do not trigger execution.

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
- On `/start`, follow Session Start to this Worker. Read the mandatory Conversation Mode settings reference. Use the current-conversation verified-load ledger.
- Complete the startup notice, required baseline verification, progressive loading, startup P0 batch, and queue-draining procedure defined here and in the required references before accepting the substantive prompt.
- Load novelist initialization instructions from `references/novelist-initialization.md` only after foundational initialization passes and the user explicitly requests the novelist role.
- Load drawing-session instructions from `references/drawing-session-initialization.md` only after foundational initialization passes and the user explicitly requests a drawing session or the procedure requires it.
- The Worker routes initialization. Session Start and Conversation Mode do not own operational procedures.

### Mandatory pre-action self-check

Before repository work, review the task's authority and current workflow. Confirm:
1. The canonical instruction owner and required references are verified.
2. The task and parentage are correct. The scope and approval are explicit.
3. Dependencies, status, and execution eligibility are reconciled.
4. No conflicting instruction or duplicate rule creates an ambiguous execution boundary.
5. The user's decision collection phase is complete before executing newly unlocked work.
6. The intended batch, verification, readback, and cleanup steps are defined.

If any check fails, resolve it before the affected work. Do not silently bypass a gate.

### Instruction conflict and drift control

Treat conflicting or stale instructions as a workflow fault. Inventory the conflict, locate the canonical owner, reconcile secondary files to pointers, and verify the changes before continuing. Do not append duplicate rules as a quick fix. When a missing rule is identified, add it only to its canonical owner. When an existing rule was not followed, strengthen the gate or verification rather than copying the rule elsewhere. Review associated templates and indexes whenever their owner contract changes.

## Execution and closeout

1. Read the selected task, its parent, dependencies, applicable decisions, and owner instructions.
2. Execute approved work to quiescence. Do not interrupt for routine choices or a blocker isolated to one task.
3. Record progress, decisions, changed paths, commit SHAs, readback, and limitations in the task record.
4. For every task-specific implementation commit, add the Task-ID trailer shown above.
5. **Implementation closeout and verification are separate.** Close an implementation task when its deliverable-specific acceptance criteria are met, its intended-branch commit exists, and readback confirms the committed content. Do not make unperformed runtime tests, lint, or hosted validation a universal completion gate. If an acceptance criterion explicitly requires a permitted check, treat that check as deliverable-specific evidence and do not claim it passed when unperformed. Record remaining verification debt, uncertainty, or follow-up clearly. When useful, create an authorized follow-up task for verification or evidence collection. CI remediation completion is commit-based. Hosted validation is separate metadata.
6. A parent cannot be Done while a required child remains open.
7. After closeout checks, delete the completed or cancelled task folder and its board row. Do not archive it, create a retention copy, or add a Historical row. Preserve Ledger finding identity, evidence, resolution history, and prior task references.

Claim validation only when you observed it. Do not run repository scripts, tests, or lint locally. Use hosted workflows only when required. Do not inspect their results unless the user explicitly requests review.

## Autonomous execution and blocker discipline

Execution interruptions are exceptional, not a workflow default. Once the user authorizes an execution batch, autonomously complete the full deliverable within the approved scope, including routine recovery, source retrieval, file inspection, correction of implementation mistakes, and governance/board/task reconciliation.

Before contacting the user or declaring a task Blocked, exhaust permitted internal and repository-based resolution paths: inspect authoritative instructions and task records, recover required evidence, correct stale task/board state, use safe fallbacks already authorized, and isolate the unresolved portion. A failed tool call, missing file that can be recovered, stale status, uncertainty resolved by reading canonical guidance, or ordinary implementation choice is not a user blocker.

Only stop or seek input when the unresolved issue genuinely requires the user's authority, decision, preference, secret/credential, or indispensable information that cannot be safely or reasonably inferred or recovered within scope. Do not surface routine status, ask the user to diagnose workflow errors, or interrupt execution for a blocker that affects only a separable portion. Record the exact residual blocker and continue independent eligible work.

Before declaring a task or batch complete, reconcile its task records, board, dependencies, and canonical workflow. Do not allow stale governance records or workflow inconsistencies to become reasons to ask the user to supervise reconciliation.



## Recursive queue integrity and workstream closeout boundary

Treat a user's authorized workstream or selected parent as the execution batch boundary, not an individual task or subtask. Completing or deleting a child is a scheduler transition only. Continue executing every eligible child and nested child within that authorized focus until quiescence, then report once.

Before declaring quiescence, recursively traverse every active parent and descendant index, record, and referenced task-folder path. Reconcile all mismatches: missing indexes, orphan records, missing parent records, stale paths, duplicate IDs, inconsistent statuses, and stale dependency/deferral reasons. Recover missing records from repository evidence when possible. If a parent record is irrecoverable, preserve its children and evidence and repair the hierarchy using a transparent reconstruction based on authoritative child data and templates rather than treating the missing record as a blocker. Do not mark a task complete from a shallow board/index scan.

Re-evaluate Paused tasks at every dependency/status change. Resume a task only when its pause was dependency-based or stale and its authorization remains valid. Preserve intentional suspensions that require explicit user resume. In particular, a batch cue does not override a record's intentional future pause or an approval/authority boundary.

At quiescence, collect and reconcile every user-resolvable blocker across the authorized workstream. Present one consolidated decision brief containing all such blockers, evidence already examined, the precise input needed, and choices/consequences. Do not serialize user calls one at a time. External/access blockers the user cannot resolve remain recorded and deferred. Do not interrupt execution for isolated blockers.

When the workstream is a persistent parent, close and delete completed child records under lifecycle rules, but preserve the persistent parent. Work unrelated to its objective remains outside the batch.

## Run-to-quiescence and user input

Treat every authorized execution batch as a queue-draining loop. Do not stop after one task. Implementation closeout is not the end of the batch.

1. **Select:** Reconcile the board, parent indexes, child indexes, and task records. Build the full eligible queue within the user's authorized focus. Check dependencies and approval before priority and age. Select the next eligible task.
2. **Execute:** Complete that task within its approved scope. Record progress and evidence in its task record. Do not send routine progress pings or per-task status messages.
3. **Rebuild and continue immediately:** Once a task reaches implementation closeout (Done), reconcile its records and board, then immediately rebuild the full eligible queue. Treat this as a mandatory scheduler transition, not a reporting pause. Continue into the next eligible task within the user's authorized focus without waiting for a user message. After Blocked, Paused, Cancelled, approval, or dependency changes, also reconcile and rebuild. No task completion may terminate an authorized execution batch while an eligible task remains within that focus.
4. **Skip isolated blockers:** Exhaust permitted repository evidence and source investigation before declaring Blocked. Record the exact missing evidence, access, or user action. Remove the blocked task from the eligible queue. Return to step 1. A blocked task never ends the batch while another independent eligible task remains.
5. **Reach quiescence:** Declare quiescence only when no eligible task remains within the user's authorized focus. Keep blocked and dependency-waiting tasks in their deferred sections. Do not select unrelated work outside the user's focus.
6. **Build the user-decision queue:** At quiescence, review every blocked task within the authorized focus and classify its blocker. Include tasks that require user authorization, a preference, a governance decision, or other input the user can provide. Do not ask about blockers that the user cannot resolve. Keep non-resolvable external/access blockers documented and deferred.
7. **Collect and log decisions only:** Sort the user-decision queue by board order. Present only the first blocker as a concise decision brief: task ID and title, exact blocker and evidence already examined, the specific decision or input needed, and practical choices with their consequences. Include every user-resolvable blocker in one consolidated decision brief. Log the user's responses verbatim with timestamp and reconcile those decisions. **Do not execute work unlocked by the answer until the explicit standalone execute cue is received.** When the user says `Next` (case-insensitive), log that exact navigation instruction for the current decision, leave the blocker unanswered and unresolved, and present the next unresolved decision. `Next` is navigation only and cannot approve, decline, execute, resume, or change task status.
8. **Await execution cue and prepare batch:** After decision collection is complete, reconcile all answers, task statuses, approvals, dependencies, scope, and priorities. Do not start execution until the user supplies the sole cue: `execute`, case-insensitive and explicit. Once cued, build one consolidated eligible queue, execute the authorized batch, drain it to quiescence, and repeat the decision-collection phase only if execution reveals new user-resolvable blockers. Approval, decision answers, and queue-navigation commands are logged only and do not authorize immediate execution.

An isolated blocker does not justify interrupting the batch. Keep routine progress in task records. Contact the user before quiescence only when a higher-priority instruction requires it or when continuing would cross an authority, governance, safety, access, or privacy boundary.

Ask only when proceeding would cross an authority, governance, safety, access, privacy, or materially outcome-changing boundary. Otherwise use the narrowest safe interpretation.

## Execution cue — sole gate

The sole execution cue is the explicit standalone word `execute`, matched case-insensitively. Accept `execute`, `Execute`, or `EXECUTE` as the cue, but only when the user is clearly issuing it as an instruction, not quoting, discussing, testing, or hypothetically mentioning the word.

- **`execute`:** authorizes the consolidated, previously approved and in-scope execution batch after decision collection and eligibility checks.
- **`approve` / approval:** log the user's decision and scope. Never execute immediately.
- **`Next`:** log decision-queue navigation. Keep the current blocker unanswered and unresolved, then present the next unresolved decision. It cannot approve, decline, execute, resume, or change status.
- **Any other message or cue:** capture, interpret, or log it as required, but do not execute.
- `/start` is a distinct session-initialization cue governed by Session Start and is not an execution cue.

Do not infer or substitute execution authorization from phrasing, intent, status, approval, or an earlier cue. Before each execution batch, confirm that the latest explicit `execute` cue applies to the prepared batch and that its scope has not materially changed. If the scope changes, wait for a fresh cue.

At `/start`, follow `.agent/SESSION_START.md`. The mandatory P0 batch uses the rules above. Do not inspect hosted CI results. At batch completion, state readiness and remaining blockers.



## Parent selection — scope test and hierarchy correction

Create a parent task for each distinct user objective. Do not treat the active parent, current execution pointer, repository, project, or general maintenance theme as sufficient grounds for parentage.

Before selecting parent or child, compare the requested outcome against the candidate parent's original objective and acceptance criteria:

- **Same objective:** the request advances, completes, corrects, or extends an outcome already defined by that parent. Create a child when it is a distinct deliverable or substantive follow-up. record a non-deliverable decision/clarification in Subsequent Instructions.
- **Different objective:** the request creates an independently valuable outcome or changes a separate system or concern. It does not materially contribute to the candidate parent's acceptance criteria. Create a new parent, even when another parent is active or the work touches the same repository, files, or broad theme.
- **CI remediation exception:** CI findings may be children only of the genuine user task attributed by the source commit's Task-ID trailer, as governed above. This attribution rule does not authorize ordinary user work to be nested under that task.
- **Uncertain relationship:** compare objectives and criteria explicitly. If no genuine parent can be established without guesswork, leave parentage unassigned and ask at quiescence. Do not default to the current parent.

Before creating or updating a task, audit the proposed relationship. If the parent does not fit, correct it before scheduling. Create the genuine parent. Move or recreate the record under it. Update both indexes and board links. Preserve the original prompt, approval, status, dependencies, progress, commit evidence, and history. Then delete the stale child link. Never change parentage silently or discard evidence. A parent-child relationship is valid only when the child directly advances the parent's defined objective.

## Document governance — mandatory template-first gate

The Worker owns document governance. Apply this gate before creating, moving, renaming, materially revising, or validating a repository document or structured record.

1. Identify the target path, owner, and document type.
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
12. Use Reserved for a verified Markdown family with no current record. Change Reserved to Active in the commit that creates its first record.
13. Do not mass-migrate untouched history. Do not create a template when an approved embedded contract, schema, or generator already defines the format.

For a one-off note or creative document, follow an explicit Lightweight pattern or Exempt catalog entry. If no such entry exists, propose the format before editing. Source code, generated output, schemas, and machine-readable data follow their own contracts.

### Document-format classes

- **Template required:** Read and copy the canonical template for each new record.
- **Schema required:** Read and validate structured records against their schema.
- **Embedded contract:** Read and follow the format in one live owner file, workflow, or script.
- **Generator-owned:** Read and follow the generator and its tests.
- **Lightweight pattern:** Read and use an approved small structure for a low-risk or one-off note.
- **Exempt:** Preserve creative freedom or an approved external format.

The catalog defines purpose and document type, required and conditional fields, formats, allowed values, status, approval, provenance, stable IDs, parent links, migration, validation, owner, and canonical path. Treat unmarked fields as required. Mark Optional and Conditional fields explicitly. Use Unknown or Not applicable when appropriate. Keep workflow metadata out of creative prompts and user-facing fields.

Canonical copy-ready formats are in `.agent/skills/the-worker/assets/`. See its README for the asset index. The catalog and validator are Worker-owned assets in `references/` and `scripts/`. The catalog owns document-type and Markdown coverage integrity. The validator checks catalog structure, references, placement, and coverage. It does not certify semantic conformity. Do not weaken validation. Keep the catalog and owner indexes aligned.

When you create or materially revise a template, scan every repository template. Compare each template with current workflows, repository structure, and governing standards. Update each confirmed stale template and its owner references. Store every reusable template in its owning skill's `assets/` directory. Do not create project-local or workspace-level template copies. Reconcile the catalog, indexes, and inbound links.

## Worker-owned domain operations

The Worker is the sole activation and governance entry point for document governance, GitHub Actions, CI Ledger operations, and decision governance.

These procedures are Worker-owned references, not separate Agent Skills. Do not activate them as standalone skills.

Load the relevant reference only when the task requires it:

- `references/ci-ledger.md` for the startup P0 batch, report intake, finding attribution, grouping, lifecycle, or Ledger integrity.
- `references/github-actions.md` for workflow design, diagnostics, technical remediation, or validation procedures. Load it with the CI Ledger reference for the startup P0 batch.
- `references/decision-governance.md` for Drafts, ADRs, repository analysis, implementation linkage, or Confirmation.

The Worker owns document governance in this file and its canonical document-type catalog. The Worker does not activate a separate document-governance skill.

Keep these decision controls in force:

- Decision approval and task execution approval are separate.
- Do not implement a proposal before the user approves its exact Draft revision and scope and its ADR reaches accepted status.
- Every new implementation task must link one or more accepted ADRs. Grandfather existing tasks.
- Keep accepted ADR context, options, and outcomes immutable. Use a new Draft and ADR when a decision changes.
- P0 priority does not bypass decision governance.

## Diagnostic investigation before blockers

When a task depends on CI-generated or workflow diagnostic evidence, exhaust the evidence already published in the repository before declaring the task Blocked.

1. **Read the complete indexed report.** Read the report JSON as well as its Markdown summary and index. Follow the published report path. Do not search report history or inspect hosted CI unless separately authorized by the applicable policy.
2. **Read diagnostic payloads, not just summaries.** Examine failed check names, status and exit codes, captured stdout/stderr, tracebacks, failing assertions, diagnostic locations, per-file records, normalized findings, and relevant metadata. Inspect the exact payload fields that apply. Do not treat a summary that omits details as proof the details are unavailable.
3. **Trace the diagnosis in repository source.** Follow diagnostic locations and output into the affected workflow, script, generator, tests, configuration, or report producer. Read relevant source and tests. Use repository evidence to establish the cause and scope before you correct the issue.
4. **Separate committed diagnostics from hosted CI access.** A diagnostic report or log committed to the repository is repository evidence. Reading it is not hosted CI result inspection. The restriction against hosted CI inspection does not prohibit reading already-published repository files. Do not fetch, poll, dispatch, rerun, or inspect hosted CI unless explicitly authorized.
5. **Investigate reporting gaps as defects.** If a report, capture, or summary omits information needed to diagnose a failure, investigate the reporting/capture mechanism and correct the defect or create a task for it. Do not automatically block the original remediation solely because the summary is insufficient. Continue with independent source investigation where possible.
6. **Blocker discipline.** Declare Blocked only after you exhaust repository evidence and source investigation within the permitted scope. State which evidence or access you lack. List the paths and diagnostic fields you examined. Explain why you cannot continue repository-side investigation. State what specific external or user input you need. Uncertainty alone is not a blocker.
7. **Read back and record.** Read back the exact relevant repository sources and task records after changes. Record examined report paths, concrete diagnostic details, source locations, commit SHAs, and limitations. Do not claim validation that was not performed.

This procedure applies before task selection, status changes, blocker declarations, and remediation closeout. It does not authorize local execution, hosted CI review, or any other restricted action.



## CI and Actions operational ownership

The Worker owns both CI Ledger and GitHub Actions operations. Its references define policy and procedures. The report producer, composite action, workflow, report schema, report template, Ledger schema, shared eligibility module, report indexes, and immutable evidence remain in their report-family paths because existing workflows and scripts consume those paths. Treat those paths as Worker-governed implementation assets, not independent operational owners. Consolidation must preserve path contracts until a coordinated migration updates every consumer.


## Canonical CI implementation

- Scripts and regression tests: `.agent/skills/the-worker/scripts/`.
- Schemas and templates: `.agent/skills/the-worker/assets/`.
- Capture action: `.github/workflows/gh-actions-capture.yml`.
- Report indexes, history, and Ledger state remain in `.takeout/reports/` as data outputs.

Do not maintain duplicate implementations in report-family script directories. The capture workflow calls the Worker scripts.
