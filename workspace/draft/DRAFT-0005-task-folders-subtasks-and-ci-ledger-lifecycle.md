---
record_type: decision-draft
template_version: "1.2"
id: "DRAFT-0005"
revision: 1
status: "in-review"
created: "2026-11-27"
updated: "2026-11-27"
proposed_by: "Assistant"
decision_makers:
  - "User"
consulted: []
informed: []
related_drafts:
  - "DRAFT-0003"
related_adrs:
  - "ADR-0003"
resulting_adr: null
promotion_cleanup_pending: false
cleanup_reason: null
---

# Task Folders, Subtasks, and Reliable CI Ledger Lifecycle

## Proposal Summary

Adopt one folder per task. Each task folder contains an authoritative `task.md` and a `subtasks/` directory. Each independently completable work unit is a subtask record. A CI remediation is a typed subtask, not a separate top-level task note.

Use commit-based completion for CI remediation: a CI subtask becomes Done when the fix is committed to the intended branch, the commit is verified, and the commit SHA and remediation summary are recorded. Hosted CI validation is separate metadata. A pending or failed hosted validation does not undo completion of the remediation subtask. A parent task becomes Done only after every required subtask is Done.

Harden the Ledger so it preserves finding identity across recurrence, does not silently report incomplete ingestion as success, and publishes tasks without violating Worker selection and governance rules. Keep historical single-file task archives immutable and support them alongside the new folder archive format.

The user has approved the high-level direction in conversation: task folders, child subtasks, and commit-based CI-subtask completion. This exact Draft revision remains in review until the user approves it under the repository's decision process.

## Context and Problem Statement

The current task and CI Ledger contracts do not implement the requested model consistently.

Repository facts at branch `gpt`, commit `44ff7e7b956209266951a290fd10080418bb2eec`:

- `workspace/tasks/` contains flat Markdown task records. `workspace/TASK_TEMPLATE.md` is version 1.3.
- `.takeout/reports/triage/scripts/ledger.py` creates flat task notes, scans only `workspace/tasks/*.md`, and writes flat-file paths into the board.
- The generator's task acceptance criteria require a successful hosted validation result before resolving a finding.
- `validate_semantics()` rejects a resolved finding unless it contains a successful validation URL and timestamp.
- `retire_completed_task_findings()` removes terminal findings from the active Ledger after task archival. A later recurrence can therefore lose its original finding identity and remediation links.
- Report-processing exceptions are returned as warnings. The command can exit successfully while indexed reports remain unprocessed.
- Incomplete Actions captures can pass through the ingestion loop and be marked processed even though the capture policy says they remain eligible for retry.
- The task-board writer promotes each generated P0 task to Current Execution. The last generated task can displace an older eligible task, contrary to Worker priority-and-age selection.
- The active task archive procedure and Ledger archive reader assume one archived Markdown file per task.
- The task generator, CI Ledger skill, Worker, GitHub Actions skill, workspace README, task template, schema, tests, and Document Type Catalog do not share one folder/subtask lifecycle contract.

There are two decision conflicts:

1. Accepted ADR-0003 explicitly excludes changes to task generation and Ledger task linkage from its approved report-artifact scope. This proposal requires a new accepted decision that authorizes the narrow task/Ledger changes.
2. DRAFT-0003 proposes task folders but treats independently managed subtasks as separate tasks with separate Task IDs and folders. The user's new direction instead requires subtasks inside every task folder and treats CI remediation as one subtask type. This Draft proposes a narrow revision to that task boundary; it does not approve DRAFT-0003's broader Area/Project architecture.

Without a single lifecycle contract, the Worker, generator, Ledger schema, board, and archive workflow can disagree about whether work is complete. That makes the CI P0 workflow unreliable.

## Goals and Non-Goals

### Goals

- Make a task a folder with one authoritative `task.md` and a `subtasks/` directory.
- Give every task folder a subtask index, including tasks that currently have no child work.
- Define parent completion as completion of every required subtask.
- Define CI remediation as a typed subtask with commit-based Done semantics.
- Track hosted validation separately from remediation completion.
- Preserve finding identity, resolution history, and prior task links when findings recur.
- Make ingestion errors visible as a failed operation rather than a successful partial run.
- Leave incomplete Actions captures unprocessed so the capture workflow can retry them.
- Fail closed on missing indexed complete reports and unsafe report-index identifiers.
- Preserve Worker task selection rules and Current Execution ownership.
- Support folder task archives while reading legacy single-file archives.
- Add regression coverage for the above contracts and update all owning documentation.

### Non-Goals

- Change report capture classification, error eligibility, lint baselines, report retention, or the shared report-writer architecture.
- Poll, dispatch, rerun, or inspect hosted CI results automatically.
- Treat hosted CI success as proof that the remediation commit is complete.
- Reopen a completed remediation subtask merely because hosted validation later fails. A recurrence is a new observation linked to the prior remediation.
- Rewrite historical task archives or old task records that are outside the approved active-record migration.
- Change project/area architecture, create project-local boards, or create project-local Draft/ADR systems.
- Change accepted ADR-0003's report-artifact decision beyond authorizing the separately approved task/Ledger lifecycle work.
- Weaken tests, report eligibility, validation, or security checks.

## Decision Drivers

| Criterion | Why it matters | Relative importance |
|---|---|---|
| Lifecycle clarity | Parent, subtask, finding, and hosted validation must have distinct meanings | High |
| Recurrence traceability | New observations must retain links to previous remediation | High |
| Ingestion integrity | Partial failure must not appear as complete success | High |
| Worker compatibility | Task selection, approval, progress, and archive ownership must remain consistent | High |
| Evidence durability | Commits, reports, and task history must remain auditable | High |
| Migration safety | Existing task IDs and historical archives must remain usable | High |
| Operational cost | The structure must not add unnecessary scans or duplicate state | Medium |
| Recovery | A new session must locate parent and child work from the board and task folder | High |

## Assessment Basis and Evidence Limits

- **Scope of comparison:** Current flat task notes; task folders with validation-gated CI subtasks; task folders with commit-complete CI subtasks and separate hosted validation.
- **Assessment method:** Static review of the current branch files, generator, schema, regression tests, task board, Worker lifecycle, CI Ledger skill, GitHub Actions skill, and related decision records.
- **Evidence boundary:** Code and policy statements above are repository facts at the stated commit. The requested folder model and commit-based completion rule are user instructions. The predicted reduction in lifecycle ambiguity is an architectural inference, not a runtime measurement.
- **Key assumptions:** Branch `gpt` remains the source of truth; GitHub-hosted workflows remain the permitted test environment; the user's deferred hosted-results-review boundary remains in force.
- **Unresolved evidence gaps:** No hosted regression run has validated the proposed changes. No production recurrence has been replayed against a prototype. Archive cleanup compatibility for nested task files must be verified by the existing hosted archive tests before rollout.
- **Confidence:** High for the identified source-code and policy mismatches because the owning files were read. Moderate for migration behavior until the new generator and archive paths pass hosted regression tests.

## Considered Options

### Option 1 — Keep flat task notes and model subtasks as linked notes

- **Description and operating model:** Keep one Markdown file per task under `workspace/tasks/`. Add child-note links and a CI-specific note format. Keep the current board and flat archive path. Implement commit-based CI completion and Ledger recurrence retention without changing the task path topology.
- **Repository and environment fit:** Strongest fit with the current generator, task board, task parser, and archive reader. It avoids a path migration.
- **Good — strengths:** Smallest structural change; existing task links remain valid; the current archive index continues to reference exact files; the Worker can continue reading one task note.
- **Neutral — trade-offs:** Child notes can carry independent acceptance criteria, but parent-child discovery depends on consistent links and manual folder-like naming conventions.
- **Bad — weaknesses:** A task is still a note, not the requested folder. Child records are not physically contained by the parent. Evidence, child work, and parent metadata can become scattered. The task-folder requirement remains unmet.
- **Implementation and migration cost:** Lower than folder migration. Generator and board logic still need lifecycle, recurrence, error-surfacing, and validation changes. No active task path migration is required.
- **Dependencies and operational burden:** Requires Worker discipline to keep parent and child note links synchronized. Existing archive workflow remains.
- **Risks and safeguards:** Broken or stale child links can hide incomplete work. Add schema-like subtask references and tests, but the physical containment gap remains.
- **Evidence and confidence:** Current repository files demonstrate that flat notes are the existing design. Confidence is high for compatibility, but no prototype has tested the linked-note subtask model.
- **Limitations and unknowns:** This option does not satisfy the user's explicit task-folder requirement. It is retained as the no-change/lowest-migration comparator, not recommended.

### Option 2 — Task folders with hosted-validation-gated CI subtasks

- **Description and operating model:** Store each task in `workspace/tasks/<task-id>/task.md` with child records under `subtasks/`. A CI remediation subtask remains open until a hosted workflow reports success. The parent remains open until every required subtask, including hosted validation, is complete.
- **Repository and environment fit:** The folder model fits the requested containment boundary. The validation gate conflicts with the user's selected Option 1 completion rule and the deferred-results-review workflow.
- **Good — strengths:** A Done CI subtask would imply both committed remediation and successful hosted validation. The parent completion state would be conservative and simple to interpret.
- **Neutral — trade-offs:** The Worker must separate source remediation from hosted validation operationally, even though both are combined into one subtask status.
- **Bad — weaknesses:** A committed fix cannot be marked complete while hosted validation is pending. Independent work can be unnecessarily blocked. The Worker may have to inspect or wait for hosted results before continuing, which conflicts with the user's explicit boundary. A failed or unavailable hosted run can keep a technically completed remediation open.
- **Implementation and migration cost:** Requires the folder generator, board, task parser, archive migration, schema, tests, and Worker documentation. It also preserves the existing validation-gated resolution logic.
- **Dependencies and operational burden:** Depends on hosted workflow availability and result review for every CI subtask closeout.
- **Risks and safeguards:** This model risks coupling task completion to an external asynchronous system. A separate validation field could reduce ambiguity, but the subtask would still remain open.
- **Evidence and confidence:** The current code already enforces successful validation for resolved findings. Confidence is high that this option resembles current behavior; no evidence establishes that it meets the user's preferred operating model.
- **Limitations and unknowns:** Hosted validation latency and availability are not measured here. This option is not recommended because it contradicts the user's selected completion rule.

### Option 3 — Task folders with commit-complete CI subtasks and separate validation metadata

- **Description and operating model:** Store each task in `workspace/tasks/<task-id>/task.md`. Every task folder contains `subtasks/README.md` and zero or more child records. CI remediation is a typed child record. Mark it Done only after the fix commit exists on the intended branch, the Worker verifies the commit and reads back the changed files, and the commit SHA plus concise remediation summary are recorded. Hosted validation is separate metadata with states such as pending, passed, or failed. The parent task becomes Done only when every required child subtask is Done.
- **Repository and environment fit:** Matches the user's requested folder/subtask hierarchy and selected commit-based CI completion rule. Requires coordinated updates to the generator, board, schema, Worker, GitHub Actions skill, templates, tests, catalog, and archive handling.
- **Good — strengths:** Parent outcome and child work have distinct acceptance boundaries. The CI subtask can finish when authorized remediation is committed, so independent work can continue without waiting for hosted CI. Validation remains visible and auditable without redefining task completion. The folder is a stable recovery and archive unit.
- **Neutral — trade-offs:** A task can be Done while its hosted validation metadata is pending. Users and workers must read the two fields separately. This is intentional, not a hidden inconsistency.
- **Bad — weaknesses:** A commit may later fail hosted validation. The workflow must create or link a new recurrence/remediation record without rewriting the completed historical subtask. Parent Done means its authorized work is complete, not that every external validation system is green.
- **Implementation and migration cost:** Highest initial cost. Update task and subtask templates; migrate active flat records while preserving IDs and content; update generator discovery, task IDs, board links, archive reader/writer, retention index handling, Ledger schema and tests; preserve legacy archived single-file records.
- **Dependencies and operational burden:** Requires exact branch/commit verification by the Worker, hosted validation metadata capture when reviewed, and one consistent parent-child archive contract. No periodic scan is added.
- **Risks and safeguards:** Main risk is conflating remediation completion with validation. Use explicit field names and policy language. Keep finding identity and resolution history in the Ledger. Never delete terminal findings solely because their task was archived. Link recurrence to the previous task IDs.
- **Evidence and confidence:** The current code confirms the generator and schema are the points enforcing flat paths and validation-gated resolution. The existing `upsert_finding()` already reopens a resolved identity and preserves resolution history, but retirement currently deletes that identity. Confidence is high for the code-level diagnosis; runtime behavior remains unverified until hosted tests run.
- **Limitations and unknowns:** The folder archive path must be checked against scheduled cleanup behavior. Hosted validation is intentionally not part of the remediation Done gate. This option is recommended.

## Comparative Assessment

| Criterion | Option 1: Flat notes | Option 2: Folder + validation gate | Option 3: Folder + commit gate |
|---|---|---|---|
| Task-folder requirement | Weak — not met | Strong — met | Strong — met |
| Parent/subtask containment | Partial — links only | Strong — physical child records | Strong — physical child records |
| Commit-based CI completion | Can be implemented | No — validation blocks Done | Yes — explicit |
| Hosted validation visibility | Separate field possible | Coupled to subtask status | Separate metadata |
| Recurrence traceability | Can be fixed | Can be fixed | Strong — retain finding identity and prior task refs |
| Migration complexity | Lower | High | High |
| Fit with user direction | Partial | Weak | Strong |

### Overall comparison

Option 1 minimizes migration but fails the task-folder requirement. Option 2 meets the folder requirement but preserves the validation gate the user rejected. Option 3 has the largest initial migration cost, but it is the only option that satisfies both the requested physical task hierarchy and the selected CI completion semantics. It also creates a clear place to fix recurrence and ingestion-integrity defects without confusing hosted validation with remediation completion.

## Proposed Recommendation

Approve Option 3.

The decisive rule is that a CI remediation subtask is Done when its authorized fix is committed to the intended branch, verified, and recorded. Hosted validation is a separate state. The parent task closes only after all required subtasks are Done. A later recurrence is represented by a new observation and a new remediation task/subtask linked to the prior finding and task references; it does not retroactively invalidate the earlier remediation record.

The Ledger must retain terminal findings as identity/history records. It may bound evidence rows, but it must not discard finding identity when a task is archived. The generator must fail visibly on malformed indexed evidence rather than silently reporting partial ingestion as success.

## Consequences and Trade-Offs

- **Positive:** Task and subtask records are physically grouped. Parent completion is unambiguous. CI remediation can finish without waiting for hosted validation. Recurrence remains traceable.
- **Negative:** Active task records must move to folders. Board and archive paths change. The schema and regression suite require coordinated updates.
- **Neutral:** Historical archives remain single files. The reader supports both old and new archive forms.
- **Conditional:** A Done remediation can have validation status Pending or Failed. This is acceptable only while the UI and documentation label validation separately and do not imply that hosted CI passed.

## Risks and Safeguards

| Risk | Likelihood / Impact | Evidence / rationale | Safeguard | Residual risk |
|---|---|---|---|---|
| Parent marked Done while a required subtask remains open | Medium / High | Parent and child statuses are currently not modeled | Worker closeout checks every required child record before parent archival | Missing child registration can still hide work |
| CI remediation marked Done without a real commit | Medium / High | Ledger schema can validate SHA shape but cannot prove branch membership | Worker verifies the commit exists on the intended branch and records readback evidence | Remote history may later be rewritten only under separate authorized action |
| Hosted validation mistaken for task completion | Medium / High | Current schema requires validation for resolution | Separate validation metadata and explicit policy language | Readers may still conflate the fields |
| Recurrence loses its prior identity | High / High | Current retirement deletes terminal findings | Retain terminal finding identity and resolution history; append new task refs on recurrence | Ledger size grows; evidence remains bounded |
| Partial ingestion appears successful | Medium / High | Current parser records errors as warnings and exits normally | Return structured errors and exit non-zero after publishing safe partial progress | A failed report may require a later natural sweep |
| Incomplete capture is consumed | Medium / High | Current loop can mark ineligible captures processed | Do not mark non-final/incomplete Actions captures processed | Incomplete entries may be reconsidered on each sweep |
| Unsafe or missing indexed report path | Medium / High | Lint run IDs are used in paths without strict numeric validation; missing files may be skipped | Validate IDs, reject traversal, and fail on missing indexed complete reports | Index producers remain a trust boundary |
| Wrong task becomes Current Execution | Medium / Medium | Every generated P0 task overwrites the pointer | Let Worker selection preserve valid current task or choose by status and age | Concurrent publisher races remain controlled by shared writer |
| New archive paths break retention | Medium / High | Existing archive reader assumes exact flat task files | Index each archived file, read `task.md` as parent, and retain legacy-file support | Hosted cleanup regression remains required |
| Migration loses task history | Low / High | Moving records can break relative links | Preserve IDs/content, update relative paths, migrate only active records in approved scope, and read back every path | External links may remain outside repository search scope |

## Repository Impact

| Area | Proposed change | Owner / exact files | Approval dependency |
|---|---|---|---|
| Task template | Define folder parent record and subtask index | `workspace/TASK_TEMPLATE.md`, new `workspace/SUBTASK_TEMPLATE.md` | This Draft and accepted ADR |
| Active task records | Move active flat notes into ID folders; preserve IDs and content | `workspace/tasks/<id>/task.md` and `subtasks/` | This Draft and accepted ADR |
| Task board | Link to exact `tasks/<id>/task.md` paths; preserve Worker selection | `workspace/task_board.md` | This Draft and accepted ADR |
| Worker | Define parent/subtask lifecycle, CI completion, and folder archive closeout | `.agent/skills/the-worker/SKILL.md` | This Draft and accepted ADR |
| CI Ledger skill | Define parent task refs, CI subtask semantics, recurrence retention, and no retirement deletion | `.agent/skills/ci-ledger/SKILL.md` | This Draft and accepted ADR |
| GitHub Actions skill | Align technical remediation and validation boundary | `.agent/skills/github-actions/SKILL.md` | This Draft and accepted ADR |
| Generator | Create folders/subtasks; discover folder tasks; preserve board selection; harden ingestion | `.takeout/reports/triage/scripts/ledger.py` | This Draft and accepted ADR |
| Schema | Make hosted validation optional metadata for commit-resolved findings | `.takeout/reports/triage/ledger-schema.json` | This Draft and accepted ADR |
| Tests | Cover folder generation, commit-only resolution, recurrence, ingestion errors, incomplete captures, and legacy archive compatibility | `.takeout/reports/triage/scripts/test_ledger.py` | This Draft and accepted ADR |
| Archive | Archive complete task folders and retain exact-file index entries; read legacy flat archives | `.agent/skills/the-worker/SKILL.md`, `.github/archive-retention-index.json`, archive cleanup tests | This Draft and accepted ADR |
| Catalog and navigation | Register task/subtask paths and update workspace/triage guides | `.agent/skills/document-standards/references/document-type-catalog.md`, `workspace/README.md`, `.takeout/reports/triage/README.md` | This Draft and accepted ADR |
| Decision records | Clarify the task-model relationship with DRAFT-0003 and ADR-0003 | `workspace/draft/README.md`, `workspace/adr/README.md`, related record links | This Draft and accepted ADR |

## Proposed Implementation Outline

After the user approves this exact Draft revision and its implementation ADR reaches accepted status:

1. Reconcile the task-folder/subtask decision with DRAFT-0003. Keep DRAFT-0003's broader Area/Project proposal separate; do not silently approve it.
2. Create an accepted ADR that records this narrow task and CI Ledger lifecycle decision and its relationship to ADR-0003.
3. Create an implementation task governed by the accepted ADR.
4. Add canonical task and subtask templates and catalog path coverage.
5. Migrate the active flat task records to ID folders, preserving task IDs, original requests, status, approval, progress, and evidence. Keep historical archives immutable.
6. Update the Ledger generator to create parent folders and CI remediation subtasks, bind `task_refs` to parent Task IDs, and update board links.
7. Update archive reading and closeout for `.archive/task/<id>/task.md` and child records while retaining legacy single-file archive support.
8. Change resolution semantics to require a verified fix commit and timestamp, with hosted validation optional and separately represented.
9. Retain terminal findings and resolution history. On recurrence, reopen the same finding identity and append a new parent task reference while preserving prior links.
10. Make ingestion errors explicit and non-zero; leave incomplete captures unprocessed; validate indexed identifiers and complete report paths.
11. Preserve the Worker’s Current Execution selection rules rather than selecting the last generated task.
12. Add regression tests for every listed invariant and run them only through the authorized hosted workflow.
13. Read back every changed file, task folder, board link, schema, and archive record. Do not inspect hosted validation results until the user explicitly triggers results review.

## Confirmation Criteria

The implementation ADR should require observable confirmation that:

1. Every active task is a folder containing `task.md` and `subtasks/`.
2. Every task has a subtask index. Each child has its own ID, type, status, acceptance criteria, evidence, and completion record.
3. The CI Ledger generates a parent task folder and a CI remediation subtask, not a flat note.
4. `task_refs` identify stable parent Task IDs. Parent task Done is blocked while any required subtask is not Done.
5. A CI remediation subtask can become Done with a verified commit SHA and remediation summary while hosted validation remains Pending.
6. The Ledger accepts a commit-based resolution without requiring hosted validation. If validation metadata exists, the schema validates its shape and state.
7. A later observation reopens the same resolved finding, preserves the previous resolution in `resolution_history`, and creates a new task/subtask when the previous task is no longer active.
8. Archiving a task does not delete the finding identity or prior task references from the Ledger.
9. Malformed indexed reports produce a visible ingestion error and non-zero command result; safe partial changes remain publishable and the failed report remains retryable.
10. Incomplete or pre-finalizer Actions captures are not marked processed by the Ledger.
11. Missing indexed complete reports and unsafe run identifiers fail closed.
12. Creating a new P0 task does not displace a valid current task selected by Worker priority/age rules.
13. New folder archives and legacy single-file archives are both read correctly by the Ledger and retention workflow.
14. The hosted Ledger regression suite and Document Type Catalog validation pass after the changes. No result is claimed until observed.
15. The active task board, task folders, discussion register, and archive retention index agree after migration and closeout.

## Questions for the User

1. Do you approve Option 3 and this exact scope for task folders, subtasks, commit-based CI remediation completion, recurrence retention, and ingestion-integrity repairs?
2. Do you approve migrating all active flat task notes into folders while leaving historical archives immutable?
3. Do you approve the rule that archived terminal findings remain in the Ledger as identity/history records so later recurrence can link to prior remediation?

## Review and Approval

- **Revision presented:** 1
- **User decision:** Pending exact Draft approval
- **Approved scope:** High-level direction approved in conversation; this exact revision and its additional Ledger-integrity repairs await approval
- **Decision date:** Pending
- **Resulting ADR:** Not created

## Discussion and Revision History

| Date | Revision | Change | User feedback / decision |
|---|---|---|---|
| 2026-11-27 | 1 | Initial proposal. Captured the approved task-folder and commit-based CI-subtask direction, identified Ledger recurrence and ingestion-integrity defects, and defined migration and compatibility boundaries. | User approved the high-level direction; exact Draft revision awaits review. |

## References and Evidence Register

| ID | Source / exact locator | Version, date, or commit | Evidence type | Supports which option / claim | Limitations |
|---|---|---|---|---|---|
| E1 | `.takeout/reports/triage/scripts/ledger.py` | Branch `gpt`, commit `44ff7e7b956209266951a290fd10080418bb2eec` | Repository fact | Flat task generation, parser paths, validation gate, finding retirement, ingestion error handling, and task selection | Static code review; no local execution |
| E2 | `.takeout/reports/triage/ledger-schema.json` | Schema 1.5.0 at commit `44ff7e7b956209266951a290fd10080418bb2eec` | Repository fact | Resolved finding requires successful validation evidence | Schema shape does not prove runtime semantics |
| E3 | `.takeout/reports/triage/scripts/test_ledger.py` | Branch `gpt`, commit `44ff7e7b956209266951a290fd10080418bb2eec` | Repository fact | Current regression expectations include flat files and finding retirement | Tests were not run |
| E4 | `.agent/skills/ci-ledger/SKILL.md` | Branch `gpt`, commit `44ff7e7b956209266951a290fd10080418bb2eec` | Repository fact | Current task, resolution, and retirement policy | Conflicts with other owner policies |
| E5 | `.agent/skills/the-worker/SKILL.md` | Branch `gpt`, commit `44ff7e7b956209266951a290fd10080418bb2eec` | Repository fact | Worker task selection, archive, and batch lifecycle | Must be reconciled with CI-specific subtask rules |
| E6 | `.agent/skills/github-actions/SKILL.md` | Branch `gpt`, commit `44ff7e7b956209266951a290fd10080418bb2eec` | Repository fact | Hosted validation and remediation completion instructions | Current wording conflicts with selected commit-based completion |
| E7 | `workspace/TASK_TEMPLATE.md`, `workspace/task_board.md`, `workspace/README.md` | Branch `gpt`, commit `44ff7e7b956209266951a290fd10080418bb2eec` | Repository fact | Flat task record and board paths | Static review only |
| E8 | `.agent/skills/decision-governance/SKILL.md` | Branch `gpt`, commit `44ff7e7b956209266951a290fd10080418bb2eec` | Repository fact | Draft/ADR approval gate and implementation-task linkage | Governs process, not the technical choice |
| E9 | `workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md` | Revision 1, in-review | Repository fact | Existing proposed task-folder model and its separate-subtask-ID boundary | Not an accepted decision |
| E10 | `workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md` | Accepted ADR-0003 | Repository fact | Explicit exclusion of task generation and Ledger lifecycle changes from its approved scope | A new decision is required for this proposal |
| E11 | User instructions in this conversation | 2026-11-27 | User instruction | Task folders, child subtasks, CI subtask type, and commit-based Done semantics | Does not replace the repository's exact Draft/ADR promotion gate |

## Technical and Approval Boundary

This Draft does not authorize implementation. The user has approved the high-level direction, but this exact Draft revision and resulting ADR remain subject to the repository's decision process. Do not change task generation, Ledger schema, active task paths, archive behavior, or Worker lifecycle until the user approves this revision and the resulting ADR reaches accepted status.

<!--
Draft lifecycle:
- Allowed statuses: draft, in-review, changes-requested, approved-for-adr, rejected, withdrawn, superseded.
- Do not use promoted as a Draft status.
- On successful promotion, delete this source file after the accepted ADR passes the completeness and read-back checks.
- If deletion fails after acceptance, keep this file temporarily. Set resulting_adr, promotion_cleanup_pending, and cleanup_reason. Add it to Promotion Cleanup Pending, not Current Drafts.
- Do not create an .archive/draft/ folder or a Promoted Drafts index.
-->
