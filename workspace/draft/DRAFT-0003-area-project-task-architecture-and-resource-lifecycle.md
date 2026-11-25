---
record_type: decision-draft
template_version: "1.2"
id: "DRAFT-0003"
revision: 1
status: "in-review"
created: "2026-11-25"
updated: "2026-11-25"
proposed_by: "Assistant"
decision_makers:
  - "User"
consulted: []
informed: []
related_drafts:
  - "DRAFT-0002"
related_adrs:
  - "ADR-0001"
  - "ADR-0002"
resulting_adr: null
promotion_cleanup_pending: false
cleanup_reason: null
---

# Establish Clear Area, Project, and Task Boundaries in the Workspace

## Proposal Summary

Define three separate scopes for repository work:

- An **area** is a durable domain of interest. It owns shared knowledge that applies across its projects.
- A **project** is a bounded outcome that coordinates multiple related tasks. It owns project scope, milestones, dependencies, and project-specific resources.
- A **task** is one approved, actionable outcome. It owns its execution plan, progress, evidence links, verification, and handoff.

Keep the Workspace as the work-management hub. Keep one global task board, one global Draft index, one global ADR system, and the current discussion register. Do not create a second board, conversation transcript, or project-local copy of an ADR.

Option 4 is recommended: use project folders for project coordination, isolate each task in its own folder, and allow both project tasks and standalone tasks. Keep project planning distinct from task execution planning. Use the task-record ownership model proposed by DRAFT-0002. A task folder is a container, not a project.

Treat this Draft as a companion to DRAFT-0002. DRAFT-0002 covers phase-aware execution and research evidence within a task. This Draft covers scope hierarchy, project lifecycle, task isolation, shared resources, and cross-scope navigation. Reconcile the two Drafts before promotion. Do not implement either proposal until the user has approved the exact revisions and the resulting ADRs have reached accepted status.

## Context and Problem Statement

The current repository has a task-management workspace, a global task board, a shared discussion register, global Draft and ADR workflows, and domain directories such as `novels/`. The current task model stores each task as one Markdown record under `workspace/tasks/`.

The repository does not yet define a general project object. It also does not define a reusable boundary between an area, a project, a task, and the resources each scope owns.

The hand-off in `master/Handoff.md` proposes a broader structure. It places projects under Workspace, puts tasks inside project folders, separates plans and progress records, and moves reusable knowledge from projects into area resources. It also proposes project-local boards, project-local Draft and ADR folders, full conversation logging, and a 90-day archive for entire project folders.

The hand-off identifies a valid need. Work that spans several related tasks needs a project-level coordination layer. However, some proposed structures duplicate current records or conflict with accepted repository contracts.

### Existing repository capabilities

The current repository already provides:

1. One global task board that identifies current execution and indexes active and historical tasks.
2. One task record that preserves the request, scope, approval, requirements, decisions, progress, state, verification, and handoff.
3. A three-section discussion register for Current Step, Open Discussions, and the three most recent verified reports.
4. A global Draft lifecycle and one global ADR sequence.
5. One task archive and one report archive with exact-file, 90-day retention.
6. Permanent ADR storage outside the 90-day retention process.
7. Area-like directories. For example, `novels/` contains multiple novel projects and has its own workflow and document hierarchy.
8. Domain-specific project indexes. In the novel area, `novel.md` owns narrative foundation and continuity while child records own detailed arcs, scenes, and illustrations.

These systems should remain authoritative unless a new design replaces them with a clear migration and recovery model.

### Main gaps and conflicts

- A multi-task outcome has no standard Project record, project status, or project-level coordination plan.
- A task may be mistaken for a project when it needs several phases, research evidence, or more than one session.
- A project can duplicate task status, progress, and next actions if it has its own board and progress log.
- Separate task plans and progress files can duplicate the current task record unless each file has a strict ownership boundary.
- A project archive based on a whole folder does not match the current exact-file retention index or cleanup workflow.
- Project-local Draft and ADR folders would compete with the global decision process.
- Word-for-word chat logging conflicts with the Worker rule against conversation transcripts. It would also duplicate task requests, decisions, and progress.
- Repeated `misc` folders do not define who owns an item, how long it remains, or when the Worker must classify it.
- Project and task IDs that encode their current folder path can become misleading when work moves between projects or areas.

## Goals and Non-Goals

### Goals

- Define an Area, Project, Task, Plan, Resource, Decision Draft, ADR, Discussion, and Archive.
- Make the difference between one complex task and a multi-task project explicit.
- Isolate each task's files without creating multiple authorities for task status or progress.
- Give projects a record for outcomes, milestones, dependencies, and project-specific resources.
- Keep one global task index and one global decision system.
- Define how task evidence can become project or area knowledge.
- Recover work from repository records after context loss, including the associated project plan and accepted ADRs.
- Keep the repository's current remote-only GitHub operating model.
- Preserve current archive immutability, exact-file retention, task approval, and ADR approval rules.
- Make the design incremental. Do not mass-migrate existing tasks or project records.

### Non-Goals

- Reorganize every root directory into an area.
- Replace domain-specific project structures such as the novel hierarchy.
- Treat every multi-step task as a project.
- Require every task to have a separate plan, progress file, or findings file.
- Create a second mutable task board for each project.
- Create project-local ADRs or a second Draft approval workflow.
- Store full conversation transcripts.
- Move whole project folders into the current 90-day archive.
- Add automatic reminders, live context hooks, or runtime plan injection.
- Add a generic `misc` directory at every scope.
- Change DRAFT-0002's phase and evidence rules without an explicit reconciliation of both Drafts.

## Definitions and Scope Boundaries

| Concept | Definition | Owns | Does not own |
|---|---|---|---|
| Area | A durable domain of interest that can contain several projects | Area-wide resources, domain standards, project navigation | A live task queue or project execution log |
| Project | A bounded outcome that needs coordination across multiple related tasks | Project charter, success criteria, milestones, task dependencies, project-only resources, closure summary | Detailed task progress or an independent task-status system |
| Task | One actionable outcome with its own approval and acceptance criteria | Task scope, status, approvals, execution plan, progress, evidence links, verification, handoff | A permanent knowledge base or project-wide task board |
| Project plan | A coordination plan across project milestones and task dependencies | Milestones, task relationships, dependency order, project exit criteria | Step-by-step execution details for each task |
| Task execution plan | A plan to complete one task | Task phases, phase exit criteria, one immediate Next Step | A separate project or independent task status |
| Task findings | Evidence collected to support one task | Source inventory, observations, confidence, limitations, unresolved questions | Task approval, task status, or project policy |
| Project resource | Reusable information that has value within one project | Project-specific reference or finding | A duplicate of an area resource or a task activity log |
| Area resource | Curated knowledge that can support multiple projects in one area | The canonical shared area reference | A copy of every task finding |
| Decision Draft | A proposal for one repository decision | Proposal and user review state | Project content drafts or task execution authority |
| ADR | A user-approved repository decision | One accepted decision and its confirmation lifecycle | A project-local decision copy |
| Discussion | A current unresolved question or decision thread | Concise context, required user input, and links | A transcript of every chat turn |
| Archive | A retention or permanent-history location with an explicit policy | Exact archived records and their lifecycle | A general holding area for every old folder |

### When to create a Project

Create a project when one outcome requires coordination across multiple independently trackable tasks, shared milestones, dependencies, or resources that must remain available across sessions.

A project is not required only because:

- A task has several phases.
- A task needs a research note.
- A task spans more than one conversation.
- A task changes several related files.
- A task has a detailed execution plan.

Those conditions may require a Phased or Research-led task under DRAFT-0002. They do not by themselves establish a project.

A project may start with a small task set. It must still have a distinct shared outcome and project-level coordination need. Do not create empty project folders or speculative projects.

### When to create an independent Task

Create a separate task when the work has an independently verifiable outcome, owner, dependency, approval boundary, or deliverable. A project can coordinate several such tasks.

Use phases within one task when the stages contribute to one outcome and do not need independent task status or ownership.

Do not use several plan files as a substitute for task decomposition. If work can be assigned, reviewed, blocked, and completed independently, create a child task with its own stable Task ID.

### Relationship with DRAFT-0002 and the newer task requirements

Keep the planning and evidence rules in DRAFT-0002 as the task-level design basis:

- The task record remains the authority for task scope, approval, status, phase state, the immediate Next Step, progress, verification, and handoff.
- The task Execution Plan and chronological Progress Log remain in `TASK.md`. This Draft does not add a separate task `PLAN.md` or `PROGRESS.md`.
- A research evidence file remains optional. This Draft proposes placing it beside `TASK.md` as `FINDINGS.md`, inside the task's own folder, instead of using the shared `workspace/task-notes/` location proposed in DRAFT-0002 revision 3.
- A task folder is the isolation boundary. Its Task ID is the selector. Independently managed subtasks receive separate Task IDs and folders. This Draft does not add a separate `PLAN_ID` or a shared active-plan pointer.

This is a material path refinement to DRAFT-0002, not an additional findings system. Do not implement both the shared `workspace/task-notes/` family and task-local `FINDINGS.md` files. Before ADR promotion, reconcile the exact approved DRAFT-0002 revision and update its implementation paths, template, and catalog requirements to match the selected architecture.

The current repository records a state discrepancy: `workspace/discussion.md` says the user approved Option 3 with additional requirements, while DRAFT-0002 revision 3 and its index still show `in-review`, and the linked task record still says Blocked pending review. Do not resolve this by guessing or silently changing approval metadata. Confirm the exact approved revision and added scope, then update the Draft, index, task, and board consistently before promotion.

## Decision Drivers

| Criterion | Why it matters | Relative importance |
|---|---|---|
| Clear ownership | Each record needs one purpose and one source of truth | High |
| Task/project distinction | A complex task must not create an unnecessary project | High |
| Recovery | A new session must find the correct project, task, plan, and accepted decisions | High |
| Low duplication | Boards, plans, progress logs, and resources must not repeat each other | High |
| Task isolation | Independent tasks must not overwrite another task's state | High |
| Knowledge reuse | Validated information should remain available at the correct scope | High |
| Approval integrity | Drafts, plans, and project records must not authorize unapproved work | High |
| Archive compatibility | New structures must fit the current exact-file retention policy or define a safe replacement | High |
| Operating-environment fit | The design must work through GitHub repository operations | High |
| Migration and maintenance cost | The structure must justify its permanent complexity | Medium |
| Navigation | The user and Worker must locate current and historical work quickly | Medium |

## Assessment Basis and Evidence Limits

- **Scope of comparison:** The current flat task model, the complete hierarchy in `master/Handoff.md`, a centralized task-folder model, and a hybrid project/task model.
- **Repository snapshot:** Repository `dungnv2602/chatgpt`, branch `gpt`, commit `36e7613f974119c3075784d6cece2e29df407b15` before this Draft was created.
- **Assessment method:** Qualitative review of the current Worker, workspace, Draft and ADR contracts, task template, archive policy, Document Type Catalog, and the existing novel-area hierarchy.
- **Evidence boundary:** Repository paths and their contents are observed repository facts at the stated commit. The hand-off in `master/Handoff.md` is a user-supplied design proposal. The recommended model is an architectural inference, not a tested implementation.
- **Key assumption:** The GitHub repository remains the sole project workspace. The current global task board, global Draft/ADR lifecycle, and exact-file archive retention remain in force unless a later accepted decision changes them.
- **Unresolved evidence gaps:** No prototype or three-project pilot has tested the proposed hierarchy. The maintenance cost of nested task paths and project indexes is not measured. The best migration path for active tasks remains to be validated against the actual task inventory at implementation time.
- **Confidence:** High for the identified conflicts with current repository contracts because the relevant owner files were read. Moderate for the recommended directory topology because its operational benefit has not yet been tested with live projects.

## Considered Options

### Option 1 — Keep the current flat task model

- **Description and operating model:** Keep task records as files in `workspace/tasks/`. Use the global task board and discussion register. Do not add a first-class Project record or a defined Area resource lifecycle. Use existing domain directories for their current content.
- **Repository and environment fit:** Strong. This is the current implementation and matches The Worker, Document Standards, task archival, and GitHub-only operations.
- **Good — strengths:**
  - The model has one global task board and one task record per task.
  - It has the lowest migration cost. Existing paths, task links, and templates remain valid.
  - It already supports lightweight and complex tasks through the current record and the proposed DRAFT-0002 planning levels.
  - It avoids new project status, project templates, and nested path rules.
- **Neutral — trade-offs:**
  - A task can link to related tasks and domain documents. A careful Worker can coordinate a small project manually.
  - Existing areas can continue to maintain domain-specific indexes without a generic area schema.
  - A task record can become long when the work has a large evidence set or several phases. DRAFT-0002 addresses part of that issue.
- **Bad — weaknesses:**
  - Several related tasks have no single canonical record for their shared outcome, project milestones, dependencies, and closure state.
  - Project-level resources and reusable findings have no standard promotion path.
  - The Worker must reconstruct project relationships from task links and conversation context.
  - Independent project work can appear as unrelated tasks on the global board.
- **Implementation and migration cost:** None for the current structure. Future coordination improvements would remain manual. No new templates, path rules, or archive changes are required.
- **Dependencies and operational burden:** No new tools or permissions. The Worker must maintain cross-task links manually.
- **Risks and safeguards:** The main risk is fragmented project context. Mitigate it with clear Related Tasks links and a concise task handoff. This does not replace a project charter when several tasks share a long-lived outcome.
- **Evidence and confidence:** The task board, task template, Worker, and workspace README demonstrate the current model. Confidence is high for the current-state description.
- **Limitations and unknowns:** This option has not been measured against a larger multi-task project. It may be sufficient when projects are rare or contain only a few loosely related tasks.

### Option 2 — Adopt the hand-off hierarchy literally

- **Description and operating model:** Create an area root, a project folder under Workspace, and task folders inside each project. Require separate `TASK.md`, `PLAN.md`, and `PROGRESS.md` files for tasks and separate project `PLAN.md`, `PROGRESS.md`, and `TASK_BOARD.md` files. Add project-local Draft, ADR, resource, miscellaneous, and archive folders. Archive a completed project folder for 90 days. Store word-for-word conversations in the discussion register.
- **Repository and environment fit:** Weak without substantial changes. Several parts conflict with existing Worker, governance, discussion, and archive contracts.
- **Good — strengths:**
  - The hierarchy gives a visible location for each area, project, and task.
  - Separate task files can make task-specific planning and progress easier to inspect.
  - A project-local task tree groups related work physically.
  - Project resources can remain with their project until a promotion decision.
  - A project-level plan can coordinate milestones across tasks.
- **Neutral — trade-offs:**
  - This model can work in a repository designed from the start around nested projects and separate task artifacts.
  - A full conversation archive can preserve source dialogue, but it creates a different record type and retention obligation. The current repository has explicitly chosen not to create transcripts.
  - A project-local board may help navigation in a very large project, but it must still reconcile with the global task board.
- **Bad — weaknesses:**
  - Separate task and project progress files can duplicate task records, the global task board, and the discussion register unless each record has strict ownership.
  - A project `TASK_BOARD.md` creates a second mutable task index. Status changes can leave it inconsistent with the global board.
  - Project-local ADRs conflict with the global ADR sequence and the rule that only accepted global ADRs govern implementation tasks.
  - Project-local Drafts conflict with the global Draft index and source-Draft promotion rules. The repository explicitly does not use `archive/draft/`.
  - A full word-for-word transcript conflicts with the Worker rule against conversation transcripts. It also duplicates task prompts, decisions, and progress.
  - A whole-project 90-day archive is not supported by the current retention index. The current workflow retains exact files under `archive/tasks/` and `archive/reports/`. It does not archive or delete whole project folders.
  - Repeated `misc` and `archive/resources` folders create holding areas without a single owner or promotion rule.
  - A project can become a container for every record type rather than a bounded outcome. This increases overhead and makes project creation too easy.
- **Implementation and migration cost:** Very high. It requires new templates, path coverage, Worker recovery rules, board reconciliation, project lifecycle rules, Draft/ADR changes, archive workflow changes, retention schema changes, and migration of existing links. The conversation archive also requires a separate privacy and retention design.
- **Dependencies and operational burden:** It requires changes to the task renderer, task closeout, archive retention, and the global decision workflow. It creates several indexes that the Worker must keep synchronized.
- **Risks and safeguards:** The main risks are conflicting sources of truth, incomplete archives, and accidental loss of project records. Safeguards would require explicit ownership maps, transaction-style updates, and new validation. Even with these controls, the design keeps more mutable files than necessary.
- **Evidence and confidence:** The conflicts are directly supported by `skills/the-worker/SKILL.md`, `skills/the-worker/references/conversation-mode.md`, `skills/decision-governance/SKILL.md`, `workspace/draft/README.md`, `workspace/adr/README.md`, and `archive/README.md`. Confidence is high for the identified conflicts.
- **Limitations and unknowns:** No prototype exists. The benefit of separate progress files and local boards is not established. The design assumes a need for project-local archives that the current workflows do not provide.

### Option 3 — Centralize all task folders and link them to projects

- **Description and operating model:** Create `workspace/projects/[project-id]/PROJECT.md` and an optional project coordination plan. Keep every task folder in one central `workspace/tasks/[task-id]/` directory, whether the task is standalone or belongs to a project. Add a Project ID field to each task and a Project column to the global task board. Each project record links to its tasks by ID.
- **Repository and environment fit:** Strong. It retains one task directory, one board, and the existing global task lifecycle. It needs fewer path rules than nested project task folders.
- **Good — strengths:**
  - Every task has one predictable location, so recovery and archive handling are simpler.
  - Project membership is an explicit task field rather than an inferred path.
  - The global board can show all tasks and their project IDs without a second board.
  - Project plans can coordinate tasks without copying their progress logs.
  - A task can move between projects by changing its Project ID without moving its files.
- **Neutral — trade-offs:**
  - Project folders contain links rather than the task records themselves. This separates project control from task storage.
  - The Worker must use the Project ID to find related tasks. The global board can provide that relationship.
  - The path is consistent for standalone and project tasks, but a project folder does not physically contain its tasks.
- **Bad — weaknesses:**
  - A task directory can contain many task folders without physical grouping by project.
  - Project files and task files are separate. A person browsing only the project directory must follow links to reach task records.
  - The global task board needs a Project ID column and accurate links. A missing value can leave a task unassigned even when it belongs to a project.
  - Project-specific files and task-specific evidence may be split across separate root paths.
- **Implementation and migration cost:** Moderate. Add project records and templates, a project index, task-folder paths, a board Project ID column, and catalog rules. The task closeout process needs a new folder archive path, but the global task structure remains simple.
- **Dependencies and operational burden:** The Worker maintains Project IDs and links. The project plan and global task board must remain aligned. No project-local board is required.
- **Risks and safeguards:** The main risk is loss of clear project grouping. Use a project index and exact Task IDs. Keep the global board authoritative for task status.
- **Evidence and confidence:** The current task board already indexes tasks and is explicitly not a progress log. The novel area also demonstrates linked records under a parent project. Confidence is moderate because this option is not implemented.
- **Limitations and unknowns:** The amount of project browsing and task movement is not measured. This option may be preferable when tasks frequently change project association or when a single central task directory is a strong operational priority.

### Option 4 — Use project folders with nested task folders and one global task board

- **Description and operating model:** Store project coordination records in `workspace/projects/[project-id]/`. Store project tasks in `workspace/projects/[project-id]/tasks/[task-id]/TASK.md`. Store standalone tasks in `workspace/tasks/[task-id]/TASK.md`. The global task board lists all tasks and their exact record paths. Each task folder is the isolation boundary. Use the existing task record as the authority for task status, approvals, acceptance criteria, execution plan, Progress Log, verification, and handoff. Create a `FINDINGS.md` only when the task meets the evidence threshold in DRAFT-0002.
  
  A project has one `PROJECT.md` charter and may have one `PLAN.md` to coordinate milestones, tasks, and dependencies. It does not have a separate progress log or task board. The Project record contains a concise current summary and links to the global board and task records.
- **Repository and environment fit:** Strong, with a defined migration cost. It follows the hierarchy in the hand-off while retaining global task and decision authority. It also preserves DRAFT-0002's task-level record ownership.
- **Good — strengths:**
  - Each task has a stable folder that can contain its authoritative record and optional evidence without sharing a working directory with another task.
  - Project tasks are physically grouped under their project. Standalone tasks remain under the Workspace task root.
  - One global task board still indexes all task statuses, dependencies, project IDs, and exact record paths.
  - The project plan coordinates task outcomes and dependencies. It does not repeat each task's actions or detailed progress.
  - Task execution planning remains inside the authoritative task record, as proposed by DRAFT-0002. A task folder does not automatically require separate `PLAN.md` or `PROGRESS.md` files.
  - Independent subtasks receive their own Task IDs and folders. The Task ID is the explicit selector for the task. The Project ID selects the project. A global active-plan pointer is not needed.
  - Task findings remain with their task. Validated reusable knowledge can be curated into a project or area resource without treating every finding as permanent.
  - The global Draft and ADR systems remain intact.
- **Neutral — trade-offs:**
  - The Worker must read the exact task path from the global board. It must not search project folders to guess the current task.
  - The Document Type Catalog needs separate path rules for standalone and project task records.
  - Project tasks and standalone tasks have different active paths, but use the same task template and status lifecycle.
  - A project may have a project plan and each complex task may have its own execution plan. These plans operate at different levels and must use different fields and decision boundaries.
- **Bad — weaknesses:**
  - Nested paths add a second task location. A board row with an incorrect path can prevent recovery.
  - Moving a task into or out of a project requires a controlled path move, updated board link, and updates to links from its project plan.
  - The Worker and task renderer must support both path families.
  - A project can still become unnecessary overhead if the creation criteria are not enforced.
  - Keeping the Progress Log inside `TASK.md` may make a very long record harder to read. Splitting it into `PROGRESS.md` may help later, but it would require an explicit ownership and migration rule.
- **Implementation and migration cost:** Moderate to high. Add project and project-plan templates, task-folder path rules, a Project ID column, Worker recovery and closeout changes, task renderer and regression tests, and archive path support. Do not mass-migrate existing tasks. Move an active task to a folder only when it is materially revised or when the user approves a migration. Use a three-case pilot before general rollout.
- **Dependencies and operational burden:** The Worker owns the global board, task records, project records, and discussion register. The Document Standards catalog must cover both task path families. The CI Ledger renderer must create task records at the canonical standalone path unless an approved project context assigns a project path. Project task creation must record the exact destination path.
- **Risks and safeguards:** The main risks are incorrect path links, duplicated progress, stale project summaries, and incomplete archive transactions. Keep task status in the task record and global board. Keep the Project plan at milestone level. Read back all moved paths and archive each task file as an exact file.
- **Evidence and confidence:** The current Worker, task board, task template, Document Type Catalog, and archive rules establish the existing contracts. `master/Handoff.md` establishes the user's intended hierarchy. The current novel workflow demonstrates the value of parent project indexes and specialized child records. Confidence is moderate because the proposed path layout has not been piloted.
- **Limitations and unknowns:** The design has not been tested with several active projects or many nested tasks. The cost of updating all board and cross-file links must be measured during the pilot. A future decision may still split task progress into a separate file if record size or recovery tests show a clear benefit.

## Comparative Assessment

The matrix uses qualitative fit ratings. **Strong** means the option fits the criterion without a material conflict. **Moderate** means it needs additional controls or manual work. **Partial** means it supports only part of the criterion. **Weak** means it conflicts with the existing architecture or cannot meet the criterion without a redesign. Cost refers to expected implementation and maintenance burden, not measured labor.

| Criterion | Option 1: Current | Option 2: Literal hand-off | Option 3: Central task folders | Option 4: Project-nested tasks |
|---|---|---|---|---|
| Clear Area / Project / Task boundaries | **Weak** — no generic Project object | **Strong** — explicit hierarchy | **Strong** — separate project records and task metadata | **Strong** — separate project and task folders |
| Task/project distinction | **Partial** — relies on related-task links | **Moderate** — project may become a task container | **Strong** — project coordinates linked tasks | **Strong** — project coordinates nested task folders |
| Single source of task status | **Strong** — current task record | **Weak** — project and task boards can conflict | **Strong** — task record and one board | **Strong** — task record and one board |
| Task isolation | **Partial** — one file per task | **Strong** — separate task folder | **Strong** — separate central task folder | **Strong** — separate task folder under project |
| Project coordination | **Weak** — manual cross-links | **Strong** — separate project plan and board | **Strong** — project plan plus global task board | **Strong** — project plan plus nested task folders |
| Recovery path | **Moderate** — flat task selection | **Weak to Moderate** — several indexes and records | **Strong** — global board selects task, Project ID selects parent | **Strong** — global board selects exact nested task path |
| Research evidence | **Moderate** — task references | **Strong** — separate evidence records, but risk of duplication | **Strong** — optional task findings linked to task | **Strong** — optional task findings inside task folder |
| Resource promotion | **Partial** — no general lifecycle | **Moderate** — project and area folders, unclear transfer rules | **Strong** — task evidence to project/area resources | **Strong** — scoped resources and explicit promotion |
| Draft / ADR governance | **Strong** — global process | **Weak** — proposes local decision folders | **Strong** — global decision process | **Strong** — global decision process |
| Archive compatibility | **Strong** — current policy | **Weak** — whole-project archive is unsupported | **Strong** — exact-file task archives | **Moderate to Strong** — exact-file archives preserve nested task IDs |
| Migration and maintenance cost | **Low** | **Very High** | **Moderate** | **Moderate to High** |
| Fit with existing novel-area structure | **Moderate** | **Moderate** — requires further mapping | **Strong** — project record can link domain content | **Strong** — project coordination can link domain content |

### Overall comparison

Option 1 is adequate for small and loosely related work. It does not provide a general project lifecycle or durable project-level coordination.

Option 2 follows the hand-off most closely. It also introduces the most conflicts. It creates several mutable indexes, duplicates task progress, moves global decisions into project folders, requires a new archive system, and conflicts with the no-transcript rule. Its physical hierarchy is useful, but it needs a smaller ownership model.

Option 3 has the simplest task-path rule. It is preferable when project membership changes often or when the user values one central task directory over physical project grouping.

Option 4 gives the clearest physical project boundary while retaining one global board. It is preferable when task files and project resources should remain grouped by project. Its additional path and recovery complexity is manageable if the board stores exact task paths and the Worker never guesses or scans for the active task.

## Proposed Recommendation

Adopt **Option 4 — Project folders with nested task folders and one global task board**, subject to the scope and safeguards below.

This option preserves the useful parts of the hand-off without copying its full structure. It gives a multi-task project a real home. It also gives every task an isolated folder. It does not create a project merely because a task has a plan.

Option 3 is the strongest alternative. It has fewer path families and makes task moves simpler. Choose Option 3 instead if pilot evidence shows that nested project task paths add more maintenance than the physical grouping saves.

### 1. Define the area layer

An area is a long-lived domain, such as `novels/`. It may contain several projects and a shared `resources/` directory.

- Keep each area's README as its index and operating contract.
- Add an area `resources/` directory only when a real cross-project resource exists.
- Put domain-specific content in its canonical area path.
- Keep shared resources in one canonical location. Link to them from projects. Do not copy the same reference into several project folders.
- Do not reinterpret every repository root directory as an area. Directories such as `skills/`, `images/`, `drawings/`, `workspace/`, and `archive/` have system or workflow roles. Keep their existing ownership.
- Treat `resources/` as a permanent knowledge collection, not an archive or a trash folder.

An area resource must include its purpose, source provenance, evidence status, owner or maintaining workflow, and review requirement when relevant. An external claim does not become an approved fact merely because it is stored under `resources/`.

### 2. Define the project layer

Create a project when several related tasks contribute to one bounded outcome.

Use this initial path:

`workspace/projects/[AREA-PROJECT-ID]/`

Each project contains:

- `PROJECT.md` — project charter and navigation record.
- `PLAN.md` — optional project coordination plan, required only when several tasks have meaningful milestones or dependencies.
- `tasks/` — task folders for project work.
- `resources/` — optional project-specific resources that have continuing value within the project.

The Project record owns:

- Project ID and area.
- Outcome, scope, and non-goals.
- Success and closure criteria.
- Project status and dates.
- Project-level dependencies and constraints.
- Links to its primary domain artifacts.
- Links to global decisions and its project plan.
- A concise current-state summary and closure summary.

Do not repeat detailed task progress in `PROJECT.md`. Do not create a separate project `PROGRESS.md` in the first release. The Project record summarizes task outcomes and links to task records.

The project plan owns milestones, task relationships, dependency order, and project exit criteria. It does not own task-level execution steps, task status, or task progress. Update the global task board for task status changes. Update the project plan when milestones, dependencies, or project scope change.

Do not create a project-local `TASK_BOARD.md`. The global board remains the only task-status index.

### 3. Keep project tasks and standalone tasks separate by path

Use these paths:

| Task type | Canonical path |
|---|---|
| Standalone task | `workspace/tasks/[task-id]/TASK.md` |
| Project task | `workspace/projects/[project-id]/tasks/[task-id]/TASK.md` |

Every task uses the same canonical task template and global status lifecycle.

The task record owns its scope, user approval, objective, acceptance criteria, task status, execution plan, progress, verification, and handoff. It links to its Project ID when it belongs to a project.

Keep the task-level Execution Plan and Progress Log in the task record as proposed by DRAFT-0002. A task folder does not require separate `PLAN.md` or `PROGRESS.md` files in the first release. This avoids splitting the task's status, next action, and chronological history across several records.

Create a task `FINDINGS.md` only when the evidence threshold in DRAFT-0002 applies. Its content is supporting evidence, not task status or approval.

A task folder is an isolation boundary. It is not a new project. One task still has one bounded outcome and one authoritative task record.

### 4. Use explicit selectors, not a shared active-plan pointer

Use the Project ID to select a project and the Task ID to select one task.

- The global task board stores each task's exact record path.
- A project record identifies its Project ID and its area.
- A task record identifies its Project ID or states that it is standalone.
- The Worker opens the exact task path from the board. It does not scan folders or select the newest file.
- A project task's path identifies its task folder. A standalone task's path identifies its task folder.
- Do not create a global `ACTIVE_PLAN` pointer.
- Do not create a second `PLAN_ID` for a task that already has a stable Task ID and one execution plan.

Independently managed subtasks receive separate Task IDs and task folders. The Task ID is the selector for each independent plan. Use phases inside one task only when the phases lead to one shared outcome.

If a project genuinely needs several parallel workstreams, represent each workstream as a child task with its own owner, dependencies, deliverable, and acceptance criteria. Keep one orchestrator responsible for project state and shared indexes. Parallel execution still requires explicit user authorization.

### 5. Define project and task identifiers

- Keep task IDs globally unique and stable. Continue using the current UTC timestamp format.
- Use an area prefix in a Project ID when one area clearly owns the project. Example: `NOVEL-001`.
- Use a cross-area prefix only when the project genuinely spans multiple areas.
- Do not encode a Task ID with its current Project ID. A task may move between projects without changing its identity.
- Never reuse an ID.
- A path change must preserve the Task ID and update the global board and all affected links.

### 6. Define resource ownership and promotion

Use the narrowest canonical scope that supports the resource.

| Resource scope | Canonical location | Use |
|---|---|---|
| Task evidence | Task `FINDINGS.md`, when required | Evidence for one task |
| Project resource | `workspace/projects/[project-id]/resources/` | Material useful to the project but not to other projects |
| Area resource | `[area]/resources/` | Validated material useful across projects in one area |
| Repository-wide reference or policy | Existing canonical `master/` or `skills/` location | Material that applies across areas or governs repository operation |

Use this promotion sequence:

1. Capture task-specific evidence in the task record or findings file.
2. At task closeout, decide whether the finding has continuing value.
3. Keep project-only material in the project resource area when it has a clear owner and future use.
4. Prepare an area resource only when the material is relevant to more than one project or supports the area as a whole.
5. Prepare a repository-wide reference or skill only when the material has cross-area value and fits that owner's contract.
6. Preserve source provenance and link the originating task. Do not silently turn an inference into policy.
7. Do not copy a complete task findings file into a permanent resource. Curate the reusable result and preserve its source links.

A decision that changes repository policy or architecture still requires a global Decision Draft and accepted ADR. Resource placement does not bypass approval.

### 7. Keep Drafts and ADRs global

- Keep decision Drafts in `workspace/draft/`.
- Keep accepted ADRs in the single flat `workspace/adr/` sequence.
- Keep both indexes global.
- Add Area ID or Project ID metadata to a Draft or ADR only when it helps navigation.
- A project record may link to a global Draft or ADR. It must not copy it into a project folder.
- A content draft, such as a novel chapter, belongs in its domain project. Call it a working draft or content draft to distinguish it from a Decision Draft.
- Do not create project-local `draft/` or `resource/adr/` authorities.
- Do not create `archive/draft/`. Follow the existing verified Draft-to-ADR promotion and cleanup rules.

### 8. Keep the discussion register; do not create a transcript

Keep `workspace/discussion.md` and its three sections:

1. Current Step — one short brief with links to active tasks.
2. Open Discussions — current questions, user decisions, approvals, and blockers.
3. Reports — the three most recent verified successful outcomes.

Do not record every user and assistant message word for word.

Preserve the user's original task prompt and relevant later instructions verbatim in the task record. Record decisions, approvals, and material clarifications. Keep the discussion register concise and link each open decision to its Draft or task.

The Worker may open a discussion when it identifies a decision that needs user input. An assistant-generated proposal remains Proposed until the user approves it. Do not create a full transcript to compensate for limited chat context. Recover from the task, project, and decision records.

### 9. Use one intake and classification path

Do not create separate `misc/` folders at Workspace, Project, and Area levels.

- Put an unresolved decision in Open Discussions.
- Create a task when the item has an actionable outcome.
- Create a Project only when several related tasks need coordination.
- Put a durable resource in its canonical project or area resource location after review.
- Keep an item unclassified only while its owner, scope, or destination is genuinely unknown.

A single intake or inbox directory may be proposed later if the volume of unclassified items justifies it. Do not create it in the first release. The Worker must not promise a reminder unless the user requests one and an available reminder mechanism is configured.

### 10. Define project lifecycle and closeout

Use these Project statuses:

| Status | Meaning |
|---|---|
| Proposed | A project concept awaits a user decision or required scope |
| Active | The project has an approved outcome and active work |
| Blocked | A dependency prevents progress |
| Paused | Work is intentionally inactive |
| Completed | Project success and closeout criteria pass |
| Cancelled | The project will not continue |
| Superseded | Another project or decision replaces it |

Project creation requires a clear outcome, area or cross-area scope, initial task set or defined first task, and project success criteria.

A project can close only when:

1. Every required child task is Done or explicitly Cancelled.
2. All project dependencies and external decisions are resolved or recorded as accepted residuals.
3. Project resources are classified as project-only, area-wide, repository-wide, or temporary.
4. Area-wide and repository-wide knowledge has a canonical destination and provenance.
5. The Project record contains a concise outcome and closure summary.
6. The project plan records its final milestone state.
7. The global task board reflects every task's actual state.

Do not move the entire project folder to the 90-day archive. Mark it Completed or Cancelled and retain the Project record as a durable closure index. Archive task records and findings as individual files under the existing task retention policy. Keep durable area resources in the area. This avoids deleting project context while a resource or archived task still references it.

### 11. Preserve the current archive model

Keep the current archive classes:

- Task and findings records use the 90-day exact-file retention process.
- CI report files use the same exact-file retention process.
- Accepted ADRs remain permanent in `archive/adr/`.
- Draft promotion follows the global governance process. Do not add a Draft archive.
- Project records and approved area resources are not temporary task archives.

For task-folder storage, archive exact files under a Task ID directory, for example:

`archive/tasks/[task-id]/TASK.md`

If a task has a findings file, archive it as a separate exact file under the same Task ID directory. Add one retention-index entry for each archived file. Preserve the Task ID and record content. Do not add a folder entry or ask the cleanup workflow to delete a whole directory.

Before implementation, update the Worker archive transaction, retention-index contract, and relevant hosted cleanup tests to support this layout. If the current index schema or workflow cannot safely handle exact nested files, keep the existing archive layout until the new contract passes validation. Do not weaken the current retention controls.

### 12. Recover work after context loss

Use the exact global task-board path as the entry point.

1. Read `workspace/discussion.md`.
2. Read `workspace/README.md` and `workspace/task_board.md`.
3. Identify the current task and its exact path.
4. Read the complete task record.
5. If the task has a Project ID, read that project's `PROJECT.md` and `PLAN.md`, if present.
6. Read every associated accepted ADR that governs the task. Do not rely only on an ADR ID or a previous conversation summary.
7. Read the task's findings file and other exact linked dependencies when relevant.
8. Check the current branch and committed repository state through GitHub.
9. Compare actual state with the task and project records.
10. Resume from the task's one current Next Step. Reconcile any conflict before continuing.

Do not guess the project from a filename, choose the newest plan, or use an unverified active pointer. If the board, task, project, and ADR disagree, stop and reconcile against the latest user instruction and actual repository state.

### 13. Keep indexes and plans at the correct level

| Record | What it owns | What it must not repeat |
|---|---|---|
| Global task board | Task ID, title, priority, status, origin, update date, Project ID, accepted ADRs, exact task path | Detailed progress and project milestones |
| Project record | Project scope, status, area, outcome, closure summary, links | Task progress history and task status tables |
| Project plan | Milestones, task relationships, dependencies, project exit criteria | Task execution steps and Progress Logs |
| Task record | Task scope, approval, status, acceptance criteria, task plan, progress, verification, handoff | Project-wide milestone tracking |
| Findings file | Evidence and source provenance for one task | Task status, task plan, or issue backlog |
| Area README | Area scope, project navigation, shared resource index | Full project records and task histories |
| Discussion register | Current work, user decisions, and verified recent reports | Transcript or detailed task history |
| Global ADR index | Accepted decisions and lifecycle | Project-specific copies of decision records |

## Consequences and Trade-Offs

- **Positive:** A multi-task outcome gains a project record and coordination plan without turning every complex task into a project.
- **Positive:** Each task has a dedicated folder. Project tasks remain physically grouped, and standalone tasks retain a predictable Workspace path.
- **Positive:** One global board remains the task-status authority. One global Draft and ADR system remains the decision authority.
- **Positive:** Area and project resources have distinct promotion rules. Task evidence does not become permanent policy by default.
- **Positive:** The Worker can recover the current task from an exact board path, then read its project and accepted ADR dependencies.
- **Neutral:** The Worker must maintain two task path families. The global board must store the exact path.
- **Neutral:** A project plan and a task execution plan both exist, but they serve different scopes. The Worker must not copy task actions into the project plan.
- **Neutral:** Project folders remain after project completion. This preserves the project closure record without creating a new project archive lifecycle.
- **Negative:** The nested layout requires Worker, task renderer, catalog, task board, and archive updates. It also requires regression tests for both task path families.
- **Negative:** If the project does not have several independently trackable tasks, a project record adds unnecessary overhead.
- **Negative:** A long task record may eventually benefit from a separate Progress Log. The first release does not adopt that split because it would require another authority and migration rule.
- **Negative:** Area resource promotion requires judgment. A weak or unverified finding can still be misclassified unless the Worker records evidence and provenance.

## Risks and Safeguards

| Risk | Likelihood / Impact | Evidence / rationale | Safeguard | Residual risk |
|---|---|---|---|---|
| A complex task becomes an unnecessary project | Medium / Medium | A multi-phase task can still have one deliverable | Require several independently trackable tasks and one shared outcome before Project creation | The threshold requires judgment |
| Task and Project plans duplicate actions | Medium / High | Both plans can contain next steps if ownership is vague | Project plan owns milestones/dependencies. Task plan owns execution phases and the immediate task action | Authors may still copy task detail into project summaries |
| Project task status diverges from the global board | Medium / High | A local board would create two status sources | Do not create project task boards. Use the global board only | Project summaries can still become stale |
| Nested task paths break recovery | Medium / High | A wrong board path prevents the Worker from finding the task | Store exact paths, use Task ID selectors, and read back board and task links | A missed link update can still block recovery |
| Task progress is split across files | Medium / Medium | TASK, PLAN, and PROGRESS files can repeat status and Next Step | Keep the task plan and Progress Log in the authoritative task record for the first release | Very long task files may become harder to scan |
| Project resources duplicate area resources | Medium / Medium | Similar references can be copied into several scopes | One canonical location, promotion rules, source links, no duplicate copies | Scope changes may still require a controlled move or new curation |
| A transient finding is treated as permanent knowledge | Medium / High | File location can imply authority | Require evidence classification, provenance, confidence, and review before promotion | Human review can still be wrong |
| Project closure deletes useful context | Low / High | Whole-folder archive or deletion can remove linked information | Keep the Project closure record and durable resources. Archive task files individually | Project records may accumulate over time |
| New task archive paths break retention | Medium / High | Existing rules use exact files and known path families | Update index contract and hosted cleanup tests before path migration. Never archive folders as one index item | Migration may reveal untested cleanup assumptions |
| Local Draft/ADR copies diverge from global decisions | Medium / High | Two decision authorities can accept different content | Keep one global Draft/ADR system | Project links may become stale and need checks |
| Transcript logging captures redundant or sensitive content | Medium / High | Full dialogue repeats records and extends retention | Keep concise discussion summaries and verbatim task instructions only | A summary may omit context that was not recorded as a decision |
| Project creation becomes a default for all work | Medium / Medium | A project folder can look like the normal task container | Require project entry criteria and keep standalone tasks valid | Users may still over-classify work |
| Parallel subtasks overwrite shared state | Medium / High | Shared project plans and global indexes are mutable | Separate task IDs and output paths. One orchestrator owns shared records. Require explicit parallel approval | Serialized reconciliation remains necessary |

## Repository Impact

| Area | Proposed change | Owner / exact files | Approval dependency |
|---|---|---|---|
| Worker task and project recovery | Define Area, Project, Task boundaries, creation triggers, exact selectors, resource promotion, and recovery sequence | `skills/the-worker/SKILL.md` and a focused Worker reference | This Draft |
| Task record storage | Use one folder per task with `TASK.md`; support standalone and project-nested locations | `workspace/TASK_TEMPLATE.md`, Worker path rules | This Draft and DRAFT-0002 reconciliation |
| Project record format | Add the project charter and navigation template | New `workspace/PROJECT_TEMPLATE.md` | This Draft |
| Project coordination plan | Add a project-plan template only if the final design requires a separate file | New `workspace/PROJECT_PLAN_TEMPLATE.md` or embedded contract | This Draft |
| Project index | Define project navigation, status, and active/closed lifecycle | New `workspace/projects/README.md` | This Draft |
| Task board | Add Project ID and preserve exact task record paths | `workspace/task_board.md` and Worker owner instructions | This Draft |
| Workspace navigation | Link project indexes and templates | `workspace/README.md` | This Draft |
| Area resource ownership | Define shared-resource location and promotion rules | Area README files such as `novels/README.md`, plus owner-specific references | This Draft |
| Task findings | Place optional evidence with the task folder and link it from TASK.md | DRAFT-0002 findings template and Worker procedure | DRAFT-0002 and this Draft |
| Document Type Catalog | Register Project records and both task-record path families | `skills/document-standards/references/document-type-catalog.md` | This Draft |
| CI Ledger renderer | Create task folders at the canonical standalone path and preserve the current template | `reports/triage/scripts/ledger.py` | This Draft |
| CI Ledger tests and guide | Test the generated path and new task format | `reports/triage/scripts/test_ledger.py`, `reports/triage/README.md` | This Draft |
| Archive closeout | Archive exact task files under Task ID paths and keep per-file retention | `skills/the-worker/SKILL.md`, focused archive reference if needed, `archive/README.md`, and retention-index contract | This Draft |
| Archive cleanup | Confirm exact nested task paths are supported. Do not add whole-folder deletion | authorized archive cleanup files and hosted regression tests | This Draft |
| Draft and ADR governance | Keep both systems global. Add optional area/project metadata and links only | `skills/decision-governance/SKILL.md`, Draft/ADR indexes and templates if needed | No change unless metadata is required |
| Discussion register | Keep the current three-section contract and prohibit transcripts | `skills/the-worker/references/conversation-mode.md` | No structural change |
| Novel area | Preserve the existing Novel → Arc → Scene → Illustration hierarchy. Link project coordination rather than duplicating story canon | `novels/README.md`, `novels/WORKFLOW.md`, and existing novel records | This Draft only if a concrete change is required |
| Foundational initialization | Keep current conditional initialization | `skills/SESSION_START.md`, `skills/INITIALIZATION_POLICY.md` | No change proposed |

### Compatibility and migration

- Do not mass-migrate existing task records or area projects.
- Keep existing flat task records readable. Move an existing task to a folder only when the task is materially revised or when the user approves a migration.
- Preserve Task IDs, original prompts, approval state, progress, evidence, and links during any move.
- Keep existing domain project structures. Do not create a duplicate project record when a domain-specific authoritative project index already owns the same purpose.
- The existing `novels/Novel-01/novel.md` and `novels/Novel-02/novel.md` remain the narrative and continuity authorities. A new Workspace Project record, if needed, must own only cross-task coordination and link to those domain files.
- Keep existing accepted ADRs and global Draft records in their current canonical locations.
- Keep archived task records immutable. Do not rewrite old archives to fit the new folder layout.
- Update Document Standards path coverage in the same commit that activates each new document family.
- Do not change archive cleanup until the exact-file index and hosted regression tests confirm the nested archive paths.

## Proposed Implementation Outline

After the user approves this exact Draft and the implementation ADR reaches accepted status:

1. Reconcile DRAFT-0002 with this Draft. Confirm that its approved task-level planning, evidence, and folder requirements do not conflict with the project/task architecture.
2. Create one implementation ADR for the combined, explicitly scoped decisions. Preserve the separate Draft IDs and revisions as decision provenance.
3. Create an implementation task with the accepted ADR in Governing ADR(s).
4. Define the project and task path contracts before moving existing records.
5. Create the project template and optional project-plan template. Register their path families in the Document Type Catalog.
6. Update the task template and Worker instructions for task folders, exact paths, Project IDs, project coordination, and recovery.
7. Update the global task board with Project ID and exact task paths. Do not create a project-local task board.
8. Update the CI Ledger renderer and tests. Keep Ledger-generated tasks standalone unless a verified project assignment explicitly sets a Project ID.
9. Update task closeout and the archive contract for exact files under Task ID directories. Verify the retention index and hosted cleanup tests before use.
10. Pilot a standalone lightweight task, a multi-phase standalone task, and a project with at least two independent tasks. Do not create dummy tasks to fill a pilot category.
11. Check fresh-session recovery from the global board, task record, project record, and associated accepted ADRs.
12. Review the pilot evidence. Keep the proposal open if the pilot reveals path errors, duplicate state, unclear project criteria, or incomplete archive handling.
13. Migrate existing tasks only when they are materially revised or when the user separately approves a migration.
14. Do not add transcripts, local Draft/ADR folders, project task boards, full-project 90-day archives, or automatic plan hooks as implementation shortcuts.

## Pilot and Acceptance Criteria

Run this pilot only after the implementation ADR, coordinated repository changes, and hosted validation pass. Use naturally occurring work. Do not create dummy tasks.

| Pilot case | Required characteristics | Expected structure |
|---|---|---|
| Standalone lightweight task | One narrow result with no shared project outcome | `workspace/tasks/[task-id]/TASK.md` |
| Standalone phased task | One result with multiple execution phases | One task folder, one TASK.md, and the DRAFT-0002 execution plan |
| Multi-task project | One shared outcome with at least two independently verifiable tasks | One Project folder and separate task folders under its `tasks/` directory |

The pilot passes only when:

1. The Worker can distinguish a complex task from a project using the documented entry criteria.
2. Each task has one Task ID, one authoritative TASK.md, one status, and one acceptance boundary.
3. The project has one shared outcome, project-level exit criteria, and a coordination plan that does not duplicate task execution details.
4. The global task board links every standalone and project task to its exact path and records the correct Project ID.
5. A fresh Worker session can recover each task from the repository alone. For project work, it can also recover the Project record and all governing accepted ADRs.
6. Each task folder isolates its own record and optional findings. One task cannot overwrite another task's plan or progress record.
7. The project does not need a separate mutable task board or detailed progress log.
8. Task findings preserve exact source locators, evidence classifications, confidence rationale, and limitations. The task record remains the authority for scope and status.
9. A task archive transaction preserves the task record and findings as separate exact files with valid 90-day entries. The cleanup process does not delete an entire project folder.
10. Global Draft and ADR indexes remain the only decision authorities.
11. Existing task records remain readable. No historical or active task is mass-migrated.
12. No full transcript, project-local ADR, project-local decision Draft, or redundant `misc` directory is created.

If any criterion fails, pause general migration. Revise the Worker instructions, templates, board, or archive contract. Repeat the affected pilot case before rollout.

## Questions for the User

1. Do you approve Option 4 and the proposed Area, Project, Task, Resource, and Archive boundaries?
2. Do you agree that project tasks should live under their Project folder while standalone tasks remain under `workspace/tasks/`, with the global task board indexing both?
3. Do you accept the first-release file boundary: TASK.md retains the task execution plan and Progress Log; an optional FINDINGS.md sits beside it in the task folder; and no separate task PLAN.md or PROGRESS.md is created?
4. Do you agree that independent subtasks should be separate tasks with Task IDs, rather than named plan directories with a separate PLAN_ID selector?
5. Do you approve the rule that a completed project remains as a closed Project record and that its task records use existing per-file retention, rather than archiving the whole project folder for 90 days?

## Review and Approval

- **Revision presented:** 1
- **User decision:** Pending
- **Approved scope:** Not approved
- **Decision date:** Pending
- **Resulting ADR:** Not created

## Discussion and Revision History

| Date | Revision | Change | User feedback / decision |
|---|---|---|---|
| 2026-11-25 | 1 | Initial companion proposal. Defined Area, Project, and Task boundaries; compared four hierarchy models; reconciled task folders, project plans, resource promotion, global decisions, discussion records, and archive retention with current repository contracts. | Awaiting user review. |

## References and Evidence Register

| ID | Source / exact locator | Version, date, or commit | Evidence type | Supports which option / claim | Limitations |
|---|---|---|---|---|---|
| E1 | `master/Handoff.md` | Read from `gpt`; blob SHA `95e72f6e85cb3f57aca0f393605fc938f1f0cd69` | User instruction / proposal | User's proposed area, project, task, plan, progress, resource, and archive hierarchy | A proposal, not an accepted repository contract |
| E2 | `skills/the-worker/SKILL.md` | Read from `gpt` | Repository fact | Task ownership, current task, progress, approval, remote-only operations, workspace boundary, task archive | Describes the current system, not the proposed Project model |
| E3 | `skills/the-worker/references/conversation-mode.md` | Read from `gpt` | Repository fact | Three-section discussion register, no transcript, Current Step and Open Discussion rules | No project lifecycle today |
| E4 | `workspace/README.md` and `workspace/task_board.md` | Read from `gpt` | Repository fact | Workspace responsibilities, current task index, recovery, historical task links | Board currently has no Project ID column |
| E5 | `workspace/TASK_TEMPLATE.md` | Version 1.3 at review time | Repository fact | Existing task record authority and embedded Progress Log | DRAFT-0002 proposes a later task format |
| E6 | `workspace/draft/DRAFT-0002-phase-aware-planning-and-evidence-capture.md` | Revision 3, in-review at snapshot | Repository proposal | Task-level phased planning, one Next Step, optional task findings, single task authority | Current discussion register records later Option 3 approval and additions. Reconcile its state and exact scope before promotion |
| E7 | `workspace/DRAFT_TEMPLATE.md` and `skills/decision-governance/SKILL.md` | Draft template 1.2 | Repository fact | Required option assessment, Draft lifecycle, ADR approval, exact revision review | Process requirements, not the architecture decision itself |
| E8 | `workspace/adr/README.md` and `archive/adr/0001-establish-draft-to-adr-governance-and-repository-analysis.md` | Read from `gpt` | Repository fact | Global ADR numbering, acceptance, permanent archive, task links | ADR-0001 governs process; it does not approve this architecture |
| E9 | `workspace/adr/README.md` and `archive/adr/0002-retire-source-drafts-after-verified-adr-promotion.md` | Read from `gpt` | Repository fact | Source Draft deletion after verified promotion; no Draft archive | Applies to decision Drafts, not project content drafts |
| E10 | `archive/README.md` | Read from `gpt` | Repository fact | 90-day exact-file retention for tasks/reports, permanent ADR archive, no full transcripts | Exact nested task-file paths need hosted validation before use |
| E11 | `novels/README.md` and `novels/WORKFLOW.md` | Version 1.1 at review time | Repository fact | Existing area-like root, multiple domain projects, parent-child record ownership, optional project planning | Novel-specific hierarchy must not be imposed on unrelated areas |
| E12 | `skills/document-standards/references/document-type-catalog.md` | Read from `gpt` | Repository fact | Active Markdown task and Draft path coverage; template-first rules | Catalog path rules must be updated before new task families are created |
| E13 | Branch `gpt` | `36e7613f974119c3075784d6cece2e29df407b15` | Repository snapshot | Fixed source snapshot for this review | This commit contains the Current Step brief immediately before Draft creation |

## Technical and Approval Boundary

This Draft proposes a repository architecture. It does not approve its implementation.

The exact approved Draft revision, the accepted implementation ADR, and a separately approved implementation task remain required before changes to Worker behavior, task paths, project folders, templates, indexes, archive retention, or CI Ledger generation.

DRAFT-0002 remains a related decision. Do not assume that approval of one Draft automatically approves the other. Reconcile their exact content and approval metadata before ADR promotion.

<!--
Draft lifecycle:
- Allowed statuses: draft, in-review, changes-requested, approved-for-adr, rejected, withdrawn, superseded.
- Do not use promoted as a Draft status.
- On successful promotion, delete this source file after the accepted ADR passes the completeness and read-back checks.
- If deletion fails after acceptance, keep this file temporarily. Set resulting_adr, promotion_cleanup_pending, and cleanup_reason. Add it to Promotion Cleanup Pending, not Current Drafts.
- Do not create an archive/draft/ folder or a Promoted Drafts index.
-->
