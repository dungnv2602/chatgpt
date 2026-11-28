---
record_type: decision-draft
template_version: "1.2"
id: "DRAFT-0009"
revision: 1
status: "in-review"
created: "2026-11-28"
updated: "2026-11-28"
proposed_by: "Assistant"
decision_makers:
  - "User"
consulted: []
informed: []
related_drafts:
  - "DRAFT-0002"
  - "DRAFT-0003"
related_adrs:
  - "ADR-0001"
  - "ADR-0002"
  - "ADR-0004"
  - "ADR-0005"
  - "ADR-0006"
  - "ADR-0007"
resulting_adr: null
promotion_cleanup_pending: false
cleanup_reason: null
---

# Project, Task, and Knowledge Lifecycle — Unified Workspace Architecture

## Proposal Summary

Establish an explicit project layer without creating parallel authorities for task status, task execution, decisions, discussion, or evidence. Retain the global Workspace as the work-management hub and the global task board, Draft/ADR system, discussion register, CI Ledger, and task-folder lifecycle.

Adopt a project record and project resource boundary for multi-task outcomes. Use one global task board for both standalone and project-associated tasks. Tasks remain independently approved and executable records in their existing folders; their execution planning and progress stay in their task record, subject to a separately approved reconciliation of DRAFT-0002. Projects coordinate outcomes, milestones, dependencies, and resources, not individual task activity. Area resources are durable knowledge across projects. Project resources are project-specific knowledge and can be promoted to an area resource when proven reusable.

Do not adopt word-for-word conversation transcripts, project-local task boards, project-local Drafts/ADRs, duplicate task plan/progress files, whole-project archive retention, or a root-level holding area with no owner. This proposal is a synthesis and refinement of DRAFT-0002 revision 4, DRAFT-0003 revision 1, `master/Handoff.md`, and the current repository architecture. It is a proposal only; no architecture is implemented by this Draft.

## Context and Problem Statement

The current repository already has durable governance and execution boundaries: The Worker owns workflow; tasks are folders with child subtasks; the global board is the scheduler view; the discussion register is concise; accepted ADRs are permanent decision records; the CI Ledger owns diagnostics; completed task folders are directly deleted at closeout under ADR-0004; and repository access is GitHub-only.

DRAFT-0002 proposes phase-aware task planning and optional research evidence. DRAFT-0003 proposes an Area/Project/Task hierarchy, project coordination, and resource lifecycle. The hand-off adds workspace conversation logging, project/task plan-progress files, local boards, project-local decision stores, and retention archives. These proposals contain useful ideas but need reconciliation against current accepted policy and against one another.

### Current constraints and evidence

- Task folders and nested subtasks are current accepted structure (ADR-0004); task records own scope, status, approvals, progress, evidence, and closeout.
- The Worker is the operating authority; entry files and templates have reconciled boundaries (ADR-0005).
- Canonical ownership and drift checks exist (ADR-0006), but structural validation does not replace semantic review.
- The unified report index is the sole latest lint locator (ADR-0007).
- ADR-0002 retires source Drafts after completeness-checked promotion; the ADR must stand on its own.
- DRAFT-0002 revision 4 remains in review. Its planning levels, execution-plan changes, findings note and pilot are not approved as a package.
- DRAFT-0003 revision 1 remains in review and has not established project folders or project-resource lifecycle.
- `master/Handoff.md` is available as a user vision snapshot dated 2026-11-25. It proposes a working-session chat transcript, miscellaneous holding area, standalone tasks and project folders, project-local plan/progress/board, task plan/progress files, project resources and draft/ADR/archive hierarchy, and 90-day project-folder retention. Those concepts are assessed below; the transcript and duplicated governance parts are rejected in this proposal.

## Goals

- Distinguish a project (multi-task shared outcome) from one complex task.
- Provide a durable, concise project charter, milestones, dependencies, completion criteria, and project resources.
- Preserve the global scheduler and task approval/execution boundaries.
- Keep project coordination from duplicating task-level progress or the global board.
- Define promotion of useful project knowledge to area-wide resources.
- Keep decision governance global and ADRs self-contained.
- Improve recovery and navigation with stable links and explicit owners.
- Introduce structure incrementally, with a pilot and rollback.

## Non-Goals

- Reorganize all existing areas or domain-specific systems.
- Implement this architecture or migrate existing work before user approval and an accepted ADR.
- Require a project for every multi-phase task, research task, or multi-session task.
- Create project-local task boards, task progress/plan files, Draft/ADR repositories, transcripts, or archive-retention copies.
- Change task approval, task ID, child-task, CI Ledger, task deletion, Draft promotion, or hosted CI review rules.
- Approve DRAFT-0002's planning proposal or treat its pending content as accepted.

## Definitions and boundaries

| Record | Owns | Does not own |
|---|---|---|
| Area | Domain navigation and canonical reusable resources shared across projects | Task scheduling or project execution |
| Project | Shared outcome, charter, success criteria, milestones, dependency map, project status, project-specific resource index, closure summary | Detailed task progress, approvals, global board state |
| Task | One independently verifiable result, approval, status, execution plan, progress, evidence, verification, handoff | Project-wide milestone status or durable knowledge repository |
| Subtask | Bounded child outcome under a task, with its own record and acceptance criteria | Independent project charter |
| Project resource | Reusable knowledge scoped to one project, with source/evidence and owner | Duplicate task logs or area-wide canonical knowledge |
| Area resource | Curated durable knowledge reusable across projects in an area | Raw unfiltered task evidence |
| Draft / ADR | One global proposal / permanent accepted decision | Project content drafting or execution tracking |
| Discussion | Concise unresolved conversation context, question, or decision request with links | Word-for-word transcript |
| Task board | Global scheduler and current task index | Project-specific status duplication |
| Archive/retirement | The existing lifecycle rules of each record type | A generic trash folder |

### Project creation trigger

Create a project only when one outcome needs at least two independently trackable tasks plus coordination through shared milestones, dependencies, or resources. One complex task remains a task even if it is phased, research-led, spans sessions, or touches many files.

Project identifiers should be stable and opaque enough not to encode a mutable path or area name. Project association is a field/link on task records, not a separate task identity or board. A project may be started with a small task set but must have a specific shared outcome and meaningful coordination need.

## Proposed topology

```
workspace/
  task_board.md                 # global scheduler
  discussion.md                 # concise current/open/report contract
  projects/
    <project-id>/
      project.md                # charter, milestones, dependencies, state, links
      resources/
        README.md               # project-scope evidence/reference index
        <curated-resource>.md
  tasks/
    <task-id>/
      task.md
      subtasks/
        README.md
        <subtask-records>
  draft/                        # global proposals
  adr/                          # global accepted decisions
  analysis/                      # repository-state reviews
```

This is a target shape, not an authorization to create folders or migrate records. Existing area directories (such as domain-specific roots) retain their own established contracts. An area-resource location must be designed in a separate implementation plan after inventory: do not assume a generic root `resources/` path or force every area to use identical domain structure. If a generic resource registry is adopted, it must be explicitly indexed and catalogued.

### Project record

The project record should be concise and template-driven, containing:

- Metadata: stable ID, title, status, creation/update dates, owner, associated area(s), approved scope if applicable.
- Original outcome/request and project success criteria.
- Milestones and dependency relationships, with completion evidence or task links.
- Task references (stable task IDs only), not a second mutable board. The global board remains authoritative for task status.
- Current project state, risks, blocked conditions, and next coordination action.
- Project-resource index, promotion candidates, and closure summary.
- Verification and closeout record.

Project status describes the shared outcome, not an aggregation of every task state copied from the board. At recovery, project status must be reconciled with linked tasks and repository evidence.

### Task association and execution planning

- Standalone tasks remain valid. Project tasks carry a project link and stable project ID.
- Tasks and subtasks retain their existing folder/task record authority and approval gate.
- The task record remains the sole task execution record. No separate task PLAN.md or PROGRESS.md.
- DRAFT-0002's phase model, optional findings file, template revision, and pilot remain pending. If the user later approves DRAFT-0002, its plan/evidence design must be reconciled with this project architecture before implementation; do not create competing evidence paths.
- Project-level milestones and task phases are distinct: project milestones represent outcomes across tasks; phases represent steps toward one task result.

## Knowledge and resource lifecycle

1. Raw evidence remains attached to or linked from the task that gathered it. Task evidence does not become permanent area knowledge automatically.
2. At task closeout, identify any reusable result. Promote only if its usefulness and evidence warrant a curated resource; otherwise leave the task reference during active work and follow the task lifecycle at closure.
3. Project-specific material is curated under the project resource index. It must be linked, sourced, dated, and labeled with limitations where relevant.
4. Material useful beyond the project is proposed for area resources. Promotion requires a stable owner/location and explicit readback; avoid duplicate copies by linking or transferring ownership.
5. Resources that are obsolete, speculative, or superseded should be removed or replaced according to their owner contract, not collected in an unowned miscellaneous folder.
6. Decision records are global and follow Draft-to-ADR governance. A project resource may link to an ADR but cannot contain a second decision copy.

## Discussion, temporary material, and reports

Keep the existing discussion register's concise contract. Capture the unresolved issue, context, one useful question/decision, and task/Draft/project links. Do not transcript every turn or automatically clear previous conversation text on Draft revisions. The repository's task, Draft, ADR, and report records preserve decisions and evidence; verbatim dialogue is redundant and creates privacy, maintenance, and synchronization costs.

A miscellaneous holding area is not proposed. Unclassified material must have a named task or project owner and an explicit next action or decision request. Temporary material must not be silently retained without owner, lifecycle, or purpose.

The current three-report discussion contract remains unless a separate approved change replaces it. The unified CI report index and Ledger remain authoritative for diagnostics.

## Considered options

### Option 1 — No project layer

Keep all work as independent tasks and rely on links, the global board, and discussion register.

- Fit: fully compatible with current state.
- Strengths: minimal overhead; no new records or paths; no migration.
- Trade-offs: cross-task outcomes, milestones, dependencies, and reusable project knowledge must be reconstructed.
- Weaknesses: project relationships can fragment and remain implicit.
- Cost/maintenance: lowest.
- Risks: coordination gaps; mitigate with explicit related-task links, but this is insufficient for larger outcomes.
- Evidence/confidence: current board/task model confirms compatibility; no measured project-scale comparison.

### Option 2 — Adopt the hand-off hierarchy literally

Use project folders with separate plans, progress logs, project task boards, task PLAN/PROGRESS/TASK files, project-local Draft/ADR stores, transcript logging, miscellaneous folders, and 90-day project archive.

- Fit: weak, as it conflicts with global board and governance, direct task deletion, transcript avoidance, and single-record authority.
- Strengths: visible physical containment, local plan and navigation, and retention of completed project material.
- Trade-offs: could suit a repository designed around local project workspaces and redundant indexes.
- Weaknesses: duplicates task progress/status and board, splits decisions, requires archive migration, and transcript synchronization creates a substantial ongoing burden.
- Cost: high structural and lifecycle changes across templates, Worker, catalog, board, archive and decision governance.
- Risks: stale duplicated state and contradictory decision records; safeguards would still require a single owner and reconciliation.
- Evidence/confidence: hand-off is a user vision document; these conflicts are observed against current accepted repository contracts.

### Option 3 — Project layer, global task board, task-owned execution and curated resources (recommended)

Add a concise project charter and project resources, while task records remain the execution authority and all task scheduling remains global.

- Fit: compatible in principle with ADR-0004 task folders, ADR-0005 Worker authority, ADR-0002 source-Draft cleanup, and the GitHub-only workflow. Requires approved implementation.
- Strengths: project milestones and dependencies gain an owner; task state is not duplicated; project knowledge is bounded and can be promoted.
- Trade-offs: requires project record/template/index, project-link support in tasks and board navigation, recovery procedures, and resource promotion rules.
- Weaknesses: coordination record may drift unless checkpoints reconcile project state against task links and evidence. The resource promotion process requires judgment.
- Cost: moderate new structural surface; exact migration and validator cost remain unmeasured.
- Dependencies: templates, Worker procedure, catalog/path coverage, project navigation, board task association if necessary, resource lifecycle, pilot.
- Risks: orphan projects, over-creation, stale milestone status, resource duplication. Safeguards: creation trigger, concise project record, no duplicate board, project checkpoint, closeout/promotion gate, pilot.
- Evidence/confidence: current repository structure and pending drafts support the design basis; benefits remain an inference until piloted.

### Option 4 — Project folders with task-local plan/progress artifacts but no local board or ADR

Add projects but split each task into TASK, PLAN, PROGRESS and optional findings documents, with global decision records.

- Fit: partly compatible but task authority conflicts with current task record and pending DRAFT-0002 model.
- Strengths: execution artifacts may be easier to inspect separately in local-file environments.
- Trade-offs: could work if task records were redesigned as metadata-only pointers.
- Weaknesses: currently duplicates task record authority and increases recovery/link overhead. No supported runtime hooks in the current environment.
- Cost: high template and migration cost; no current evidence the split benefits this GitHub-only workflow.
- Risks: conflicting state and partial updates; would require transactional safeguards and migration.
- Evidence/confidence: conceptual comparison only; not prototyped.

## Comparative assessment

| Criterion | Option 1 | Option 2 | Option 3 | Option 4 |
|---|---|---|---|---|
| Single task authority | Strong | Weak | Strong | Weak/conditional |
| Multi-task coordination | Partial | Strong but duplicated | Strong | Strong |
| Global decision governance | Strong | Weak | Strong | Strong |
| Resource reuse | Partial | Strong but fragmented | Strong with promotion | Partial |
| Recovery/navigation | Partial | Strong but redundant | Strong if checkpointed | Moderate |
| Fit with accepted contracts | Strong | Weak | Strong in principle | Partial |
| Maintenance cost | Low | High | Moderate | High |
| Evidence basis | Existing | Vision document | Repository synthesis, unpiloted | Unpiloted |

## Recommendation

Adopt Option 3 in principle. It introduces the missing project coordination layer while preserving the accepted global governance and task authority. The main conditions are: project creation is selective; project status is not a duplicate task board; task execution stays in the task record; resources are curated and promoted deliberately; no transcripts or local decision stores; and the pilot demonstrates recovery and useful coordination before rollout.

Option 1 is preferable for work that does not meet the project trigger. Option 2 would only be preferable if the repository deliberately migrated to a project-local workspace and multiple authorities with a fully supported reconciliation system, which is not the current environment.

## Implementation scope after approval

- Project record and project resource-index templates.
- Workspace project navigation and directory contract.
- Project/task linking conventions and global-board integration only where required.
- Worker project-creation, recovery, coordination checkpoint, resource promotion and closeout procedures.
- Document catalog and structural validator/path coverage.
- Reconciliation with DRAFT-0002 revision and associated task-template changes.
- Migration plan for existing active tasks, project relationships and area resource paths; no bulk migration unless separately approved.
- Pilot and rollback procedure.

## Pilot and acceptance

Pilot with three real outcomes (not synthetic tasks), including one multi-task project with dependencies. Evaluate:

1. Recovery from repository alone identifies project outcome, status, milestone, linked tasks, current dependency and next coordination action.
2. Global board remains the only task-status authority and shows no duplicated project-local status.
3. Each task retains its own approval, acceptance, progress and closeout.
4. Project milestones can be checked against task evidence without duplicating task progress.
5. Project resources are source-linked, owner-defined, and no duplicate area/project copies are created.
6. A task can be associated or disassociated without ID/path instability.
7. Standalone tasks remain lightweight and do not acquire a project by default.
8. Project closure yields a concise closure summary and knowledge-promotion disposition; it does not create a whole-folder archive or violate existing task lifecycle.
9. Project creation and maintenance overhead is reasonable; record qualitative observations, not invented numeric metrics.

Failure pauses rollout and triggers revision of the Draft/implementation rather than bypassing acceptance.

## Risks and safeguards

| Risk | Safeguard | Residual |
|---|---|---|
| Projects created for tasks that are merely complex | Multi-task coordination trigger | Judgment can vary |
| Project status diverges from tasks | Checkpoint reconciliation; milestone evidence links | Staleness between checkpoints |
| Project resources become an uncurated dump | Resource-index and promotion gate | Curation requires judgment |
| Duplicate area/project resources | Explicit promotion and canonical ownership | Migration may require link updates |
| Task/project status duplicated | Project status is outcome-level only; global board task state remains authoritative | Project state still needs reconciliation |
| Existing draft proposals conflict | Reconcile DRAFT-0002 before implementation; DRAFT-0003 superseded by this proposal if approved | Scope reconciliation may need revisions |
| Unsupported automation assumed | GitHub-only/manual operation unless separately approved | More manual recovery |
| Deleted task evidence is needed later | Promote durable findings before task closeout; retain accepted ADR and reports per their contracts | Some raw evidence is not retained |

## Implementation sequence

1. User approves exact DRAFT-0009 revision and scope.
2. Reconcile DRAFT-0002's exact pending revision/decision and DRAFT-0003's status; do not treat either as already approved.
3. Create an accepted ADR from DRAFT-0009 with sufficient rationale and constraints, readback-check, then delete source Draft under ADR-0002 lifecycle.
4. Create implementation task linked to accepted ADR.
5. Define canonical project template and resource index; reconcile task/project association and board without creating another board.
6. Update Worker recovery and checkpoint contract, catalog, templates and structural validator as required.
7. Readback paths and links; commit-based evidence; do not inspect hosted CI under current operating contract.
8. Pilot and assess; pause rollout on failure. Migrate only approved existing records.
9. Roll back project record/template/navigation additions if pilot fails, preserving task records and accepted ADR.

## Review questions

1. Do you approve Option 3 as the direction, with the multi-task project trigger and global board/task authority preserved?
2. Do you agree that project resources are curated project-scope knowledge, with promotion to area resources governed by a future canonical area-resource path rather than an automatic copy?
3. Should the project pilot and resource lifecycle be approved as part of the implementation scope, while DRAFT-0002's pending planning/evidence changes remain separately reconciled and not implicitly approved?

## Review and Approval

- **Revision presented:** 1
- **User decision:** Pending
- **Approved scope:** Not approved
- **Decision date:** Pending
- **Resulting ADR:** Not created

## Discussion and Revision History

| Date | Revision | Change | User feedback / decision |
|---|---|---|---|
| 2026-11-28 | 1 | Reconciled DRAFT-0002, DRAFT-0003 and `master/Handoff.md` against current accepted task, governance, Worker and CI report contracts. Expanded the options, boundaries, resource lifecycle, risks, pilot and implementation sequence. | Pending user review |

## References

- `workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md`, revision 4 (pending).
- `workspace/draft/DRAFT-0003-area-project-task-architecture-and-resource-lifecycle.md`, revision 1 (pending).
- `master/Handoff.md`, user vision snapshot (2026-11-25).
- `workspace/adr/0002-retire-source-drafts-after-verified-adr-promotion.md`.
- `workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md`.
- `workspace/adr/0005-lean-session-start-and-conversation-mode.md`.
- `workspace/adr/0006-automated-structural-validation-for-canonical-ownership-and-drift.md`.
- `workspace/adr/0007-unified-index-as-latest-lint-report-locator.md`.
- `.agent/skills/the-worker/SKILL.md`.
- `workspace/task_board.md`, `workspace/discussion.md`, `workspace/README.md`.
