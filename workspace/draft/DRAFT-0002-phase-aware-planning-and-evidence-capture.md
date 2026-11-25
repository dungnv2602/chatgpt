---
record_type: decision-draft
template_version: "1.1"
id: "DRAFT-0002"
revision: 3
status: "in-review"
created: "2026-11-24"
updated: "2026-11-25"
proposed_by: "Assistant"
decision_makers:
  - "User"
consulted: []
informed: []
related_drafts: []
related_adrs:
  - "ADR-0001"
---

# Introduce Phase-Aware Planning and Evidence Capture for Complex Worker Tasks

## Proposal Summary

Adopt the useful planning and evidence-capture mechanisms from Planning with Files selectively. Do not install or copy its complete system.

Option 3 is recommended because it adds explicit phases, verifiable phase exits, and one current Next Step inside the existing task record. The current Progress Log remains the only chronological activity log. A separate findings note is created only when research evidence is too extensive or complex to remain clear in the task record.

Keep the task record as the sole authority for task scope, approval, status, phase state, current action, progress, verification, and handoff. Treat a findings note as supporting evidence only. Separate planning depth (Lightweight, Phased, Research-led) from execution mode (Serial by default; Parallel only when explicitly authorized).

Update The Worker, add one focused Worker reference, and revise the task template to Version 1.4. Coordinate the CI Ledger renderer and regression tests with the template change. Do not create a new skill, add runtime hooks, or change foundational initialization. Preserve existing approval and task-selection rules.

ADR-0001 governs the Draft-to-ADR process only. It does not decide or authorize this proposal. Review and promote this exact DRAFT-0002 revision through that process before implementation.

## Context and Problem Statement

Planning with Files presents a persistent three-file model:

- `task_plan.md` stores the goal, phases, decisions, errors, and next step.
- `findings.md` stores research and evidence.
- `progress.md` stores the chronological work log and validation results.

Its current skill also defines plan selection, session recovery, phase validation, task isolation, worker ownership, error handling, context-injection hooks, and optional completion gates.

The external source was re-checked against GitHub on 2026-11-25. Its current `master` head remains `aaa38bc62053f5f7c1bfbcb60f0405f7cf0ee228`, committed 2026-11-23 11:57:02 UTC. The latest release is v3.29.1, published 2026-11-23 09:26:21 UTC. The head commit changes README sponsor material; the planning mechanisms reviewed for this Draft are unchanged from the prior source snapshot. The canonical skill at that revision has blob SHA `e95f7dc8c5864a89ca51e2d40de45b2de82c0622`.

The current system is more than three Markdown files. It includes task-specific `.planning/<id>` directories, explicit `PLAN_ID` and `PWF_PLAN_ROOT` selectors, an active-plan pointer for sequential switching, a plan resolver, phase-format checking, plan attestation, and host-specific lifecycle integrations. The canonical skill uses prompt/tool hooks for plan context and offers opt-in autonomous and gated modes. Integration behavior differs by host; it is not one portable hook contract.

### Existing repository capabilities

The repository already implements several parts of this model:

1. Each task has one authoritative record under `workspace/tasks/`.
2. The record stores the original request, scope, approval, requirements, decisions, progress, current state, remaining work, next actions, verification, and handoff.
3. The Worker maintains one current execution task by default.
4. The task board indexes task status and ownership. It is not a second progress log.
5. The discussion register gives each session a short, committed Current Step brief.
6. The Worker reads the selected task and verifies the actual GitHub repository state during recovery.
7. The archive process preserves task history and records exact retention entries.
8. The CI Ledger already owns structured report findings and their evidence links.

These capabilities overlap with the external plan and progress files. Creating three new files for every task would duplicate existing authority.

### Remaining gaps

The task format does not define a standard phase plan. Its Next Actions section can contain several actions without identifying one current next action.

The Progress Log records meaningful activity, but the template does not define phase exit criteria. A long task can therefore have a clear work history without a precise phase boundary.

Research findings appear in progress entries and general References. The template does not provide one standard place for source snapshots, evidence classification, confidence, and limitations.

Recovery depends on the Worker comparing the task's Current State with the actual repository. A phase marker and one next action would make that comparison more direct.

The repository does not need another task-status system. It needs a clearer execution plan inside the system it already uses.

## Goals and Non-Goals

### Goals

- Keep one authoritative task record for each task.
- Give complex tasks a phase-based execution plan.
- Define a single immediate next action.
- Give every phase an observable exit condition.
- Preserve research evidence when it is too extensive for the task record.
- Distinguish observed facts, user instructions, external claims, inferences, and hypotheses.
- Recover safely from interruption, context loss, and failed operations.
- Prevent concurrent workers from overwriting shared task state.
- Preserve current approval, task selection, archive, and CI Ledger ownership.
- Work through the existing GitHub-only repository interface.

### Non-Goals

- Install the external Planning with Files skill or plugin.
- Copy its scripts, hooks, commands, or host adapters.
- Add a local project checkout or local execution requirement.
- Create a separate plan and progress file for every task.
- Add automatic session-history or transcript recovery.
- Add unattended execution, scheduled loops, or a Stop hook.
- Change the task board into a progress dashboard.
- Replace the CI Ledger with a general findings database.
- Change the approval rules or make a phase checklist an authorization mechanism.
- Amend or expand the accepted governance and repository-analysis decision in ADR-0001.

## Decision Drivers

- **Single source of truth:** Task state, approval, and progress must not conflict across duplicate records.
- **Remote-only operation:** The process must use the GitHub repository as its project workspace.
- **Recoverability:** A new session must locate the current task, phase, evidence, and next action.
- **Evidence quality:** Important research claims must retain their source and uncertainty.
- **Low overhead:** Simple tasks must not require several planning documents.
- **Safe collaboration:** Shared task state needs one owner and explicit write boundaries.
- **Approval integrity:** A plan must never expand the user's approved scope.
- **Compatibility:** The Ledger must still generate valid Proposed task records from the canonical template.
- **Auditability:** Task closeout must preserve the useful evidence and verification record.


## Assessment Basis and Evidence Limits

The options are assessed against this repository's actual operating model, not against a hypothetical local coding-agent checkout. The decision criteria are:

- **Runtime fit:** Can the option operate through the existing ChatGPT and GitHub connector workflow without assuming a local project filesystem, shell, or unsupported lifecycle hook?
- **Authority integrity:** Does it preserve one authoritative record for task scope, approval, status, and progress?
- **Phase and evidence quality:** Does it make complex work easier to resume and research claims easier to audit?
- **Collaboration and isolation:** Can independent work stay separate without shared-state races or ambiguous task selection?
- **Safety and approval:** Does it keep external content untrusted and prevent planning or validation artifacts from acting as approval?
- **Proportionality and maintenance:** Is the recurring benefit worth its template, documentation, renderer, validation, and operator cost?

The matrix below uses qualitative ratings. **Strong** means the option naturally satisfies the criterion in this repository. **Moderate** means it can satisfy the criterion with additional manual controls or constraints. **Partial** means only a limited part of the criterion is supported. **Weak** means the core mechanism is unavailable or conflicts with the repository's existing authority model. Cost ratings describe expected adoption and maintenance burden, not measured labor.

### External evidence boundary

Planning with Files' own evaluation report is useful evidence about its design goals, but it does not establish that its measured results will transfer to this repository:

- Test 5, dated 2026-07-06, evaluates version 3.4.0 with Claude Code. Its internal benchmark contains 77 graded cells across seven methods. All 77 runs passed the supplied task tests, so it reports correctness parity for those tasks, not a correctness advantage for Planning with Files.
- In the forced O6 recovery subset, it reports a mean of 5.0 stage-two turns for Planning with Files and 8.3–13.3 for the other six methods. The same report says that the current automatic file-only recovery path had not been re-run under that protocol. The 5.0-turn result must not be presented as a measured result for the current default recovery path.
- Its unforced triggering comparison covers only two small tasks. Planning with Files engaged in 5 of 8 runs (2/3 and 3/5); the report does not establish reliable spontaneous activation for arbitrary tasks.
- The evaluation author identifies important untested areas: cross-IDE behavior, multi-day work, long-horizon drift and mid-task distractors, underspecified-task brainstorming, and an independent task corpus. The raw benchmark workspace is not part of the public repository.
- Earlier skill-compliance and blind-comparison results used version 2.21.0 and small author-run samples. They measure adherence to a prescribed file pattern more directly than task correctness or performance in this environment.

The current v3.29.1 release is newer than the v3.4.0 competitive benchmark. The public report is historical evidence, not validation of every current mechanism. The external guide also reports token and time overhead for its own host and tests. Those figures must not be projected onto ChatGPT/GitHub operations without a local pilot.

Security claims also require precise interpretation. The external SHA-256 attestation detects a change to the plan while the saved digest remains trusted. It is not a keyed signature, proof of user approval, or protection when the same writer can replace both the plan and the digest. Its own security policy continues to treat plan contents as untrusted data. A structural phase checker similarly verifies format or status markers; it cannot prove that an exit criterion is substantively satisfied.

## Considered Options

### Option 1 — Keep the current Worker workflow unchanged

- **Description:** Retain the current Version 1.3 task record, Progress Log, task board, discussion register, recovery sequence, and handoff rules. Continue recording planning and research in the existing task sections without adding a formal phase model or a new evidence-record type.
- **Good:**
  - It has the lowest implementation and maintenance cost. No task-template, Worker, catalog, archive, renderer, or test changes are required.
  - It preserves the current single task record as the source for scope, approval, status, progress, verification, and handoff.
  - It is already compatible with the GitHub-only repository workflow and current task history. No migration or compatibility layer is needed.
  - It avoids process overhead for short lookups, one-file edits, and single-stage verification work.
- **Neutral:**
  - Research can still be captured in Progress Log entries and References. The current system does not prohibit detailed evidence; it leaves the structure to the task author.
  - A careful Worker can manually identify phases and a next action in prose. The limitation is the lack of a consistent field and review rule, not an absolute inability to plan.
- **Bad:**
  - The task template does not define phase states or measurable phase exit criteria. A long task can have a detailed activity history but no explicit answer to which phase is active and what evidence closes it.
  - The current Next Actions section may list multiple future actions without identifying one authoritative immediate action. The Progress Log's historical Next field can also be mistaken for a current pointer.
  - Long research results can become scattered across Progress Log entries and References. A later session must reconstruct why evidence matters and which claims remain uncertain.
  - Recovery quality depends heavily on the Worker writing sufficiently explicit Current State, Remaining Work, and Next Actions sections. There is no common phase structure to expose an omission.
- **Fit and when it is preferable:** This is the best option for lightweight, short-lived, single-stage tasks. It is also reasonable if complex multi-session work is rare and observed recovery problems do not justify additional structure. It is not the best response to the specific phase and research gaps documented in this Draft.
- **Cost and residual risk:** Very low adoption cost and very low new operational risk. The existing ambiguity around phases, the current action, and evidence traceability remains.

### Option 2 — Adopt Planning with Files' three-file model directly

- **Description:** Adopt the external system substantially as designed: create a task-specific directory with task_plan.md, findings.md, and progress.md; use named plan directories and selectors; install its scripts; and configure compatible host lifecycle hooks for context injection, attestation, and optional completion gating. This is more than copying three templates. The current external release couples them to a resolver, state markers, host adapters, and runtime behavior.
- **Good:**
  - The separation is clear: task_plan.md owns phases and the immediate Next Step, findings.md owns research and decisions, and progress.md owns chronological activity.
  - Named plan directories, explicit selectors, and a resolver can isolate unrelated tasks. A pinned PLAN_ID is a binding rather than a hint, and an invalid explicit selector fails closed instead of silently switching to another plan.
  - The one-plan-owner rule and separate worker ledgers give a concrete collaboration model. They reduce the chance that multiple workers overwrite shared planning state.
  - On compatible hosts, lifecycle hooks can re-surface selected plan context automatically. Phase markers and scripts make some structural errors easier to detect than prose-only instructions.
  - The project has evolved beyond its initial templates. It documents host-specific behavior, attestation, recovery boundaries, and guardrails for autonomous or gated operation. A direct adopter could benefit from that integrated system rather than designing each mechanism separately.
- **Neutral:**
  - This option is not inherently better or worse for every agent. Its advantages depend on a host that exposes the required file, shell, environment, and lifecycle capabilities. The external README documents multiple integrations, but the hook capability and enforcement level differ by host.
  - The benchmark is evidence that structured plans can improve measured re-orientation in some tested host scenarios. It is not proof that this exact repository would gain the same number of turns or improve task correctness.
  - The external pattern can be appropriate for projects whose local filesystem is already the canonical task workspace and where the task record does not separately govern status and approval.
- **Bad:**
  - A second plan file would duplicate the objective, scope, requirements, decisions, current state, and next actions already owned by the repository task record. A separate progress.md would duplicate the existing Progress Log. A separate findings.md would introduce a second evidence location unless its authority and link rules were carefully constrained.
  - A separate plan selector or active-plan pointer would compete with the Worker's current execution pointer and task board. The repository would need new rules for reconciling the task board, task record, active plan, and archive state.
  - The current project workspace is GitHub, accessed through repository tools. This session does not expose the local filesystem, Bash/PowerShell execution, or the prompt/tool/Stop lifecycle hooks required by the external implementation. GitHub Actions can validate committed files, but it cannot inject a plan into each ChatGPT turn or control the end of the live conversation.
  - The external README says planning files are gitignored by default. That is reasonable for local working memory, but it conflicts with this repository's requirement that project state and durable evidence live in GitHub unless an explicit synchronization and archive policy is added.
  - A hook that re-injects externally sourced plan content creates a prompt-injection boundary. Delimiters reduce ambiguity but do not make the content trusted. The external attestation is not a user approval mechanism and does not protect against a writer that can replace both the plan and the digest.
  - The added plan directories, scripts, host adapters, tests, state files, and lifecycle integrations would substantially increase the maintenance and recovery surface. Host-specific differences would require their own support and verification.
- **Evaluation evidence and limits:** The external Test 5 reports 77/77 passing task test suites across all seven tested methods. In the forced recovery subset it reports 5.0 mean stage-two turns for Planning with Files, but it explicitly says the current file-only recovery behavior was not re-run under that protocol. The test used Claude Code and v3.4.0, not the current v3.29.1 release or ChatGPT. It did not evaluate multi-day work, other IDEs, long-horizon drift, or an external task corpus. These findings support investigation of durable plans; they do not justify copying the architecture here or promising the same recovery gain.
- **Fit and when it is preferable:** This would be the strongest option if the repository moved to a compatible local coding-agent host and intentionally made per-task plan files, rather than the current task record, the primary execution authority. It is a poor direct fit for the present GitHub-only ChatGPT workflow.
- **Cost and residual risk:** Very high adoption and maintenance cost. Without a deliberate authority migration and supported host runtime, duplicate state and partially functioning hooks would create more risk than value.

### Option 3 — Integrate planning into the task record and add optional research notes

- **Description:** Extend the existing task record with a structured Execution Plan. Use named phases and exit criteria only for work that needs them. Keep exactly one current Next Step in that plan and retain the existing Progress Log as the only chronological activity history. Create a task findings note only when evidence volume or complexity warrants a separate record.
- **Good:**
  - It directly addresses the documented gaps without creating a second source of task authority. The task record continues to own scope, approval, task status, phase status, current action, progress, verification, and handoff.
  - The existing recovery process already selects and reads the task record from GitHub. Adding a phase and one Next Step to that record makes the active work state available at the same recovery point, without depending on local hooks.
  - Lightweight tasks remain lightweight. They record a planning level and one immediate action but do not acquire artificial phases or an empty findings note.
  - Research-led work gains a repeatable way to retain exact source locators, source versions, evidence classifications, confidence rationale, limitations, contradictions, and unresolved questions. The task record links and summarizes the note but remains authoritative.
  - A single owner can keep the task record, board, discussion register, and final handoff consistent. Independent parallel work can use separate task records and explicitly assigned output paths rather than concurrent edits to one shared plan.
  - The design uses existing Document Standards, GitHub-hosted validation, task archival, and CI Ledger ownership. It does not assume a new local runtime.
- **Neutral:**
  - The system remains primarily procedural. The Worker must read and update the plan at defined checkpoints. There is no automatic per-turn injection, and a phase marker is not proof that work is complete.
  - The task template becomes longer, but the detailed phase structure is conditional. New task records use Version 1.4 while existing Version 1.2 and 1.3 records remain readable.
  - The optional findings note creates another artifact for some tasks. It therefore needs a clear creation trigger, a link from the task record, and an exact archive/retention procedure.
  - The CI Ledger renderer must remain compatible with the updated task template. This is coordination work, not a reason to duplicate the task plan.
- **Bad:**
  - The Worker, task template, focused reference, and Ledger renderer/tests must change together. If one owner is missed, manually created and Ledger-generated tasks may have different structures.
  - Phase updates and evidence capture require disciplined checkpointing. A stale plan can mislead a new session until repository state and the latest Progress Log are reconciled.
  - Human-assessed exit criteria can be marked complete incorrectly. A structural test can catch missing fields but cannot prove semantic completion.
  - Research notes can grow into an unmaintained parallel knowledge base if the creation threshold is too low or if their status and authority are not explicitly limited.
- **Fit and when it is preferable:** Strongest fit for the current repository. It improves planning and evidence quality while preserving the task's existing authority and the GitHub-only operating model. It is preferable when complex multi-stage or research-led tasks occur often enough to justify a modest template and maintenance cost.
- **Cost and residual risk:** Moderate one-time implementation cost across the Worker, template, catalog, archive guide, and Ledger renderer/tests. Ongoing cost is low for lightweight tasks and moderate for phased or research-led tasks. The residual risks are procedural drift and incorrect semantic assessment; the pilot and evidence rules are intended to expose these before general adoption.

### Option 4 — Build a repository-specific hook and script framework

- **Description:** Build custom plan initialization, phase parsing, validation, task isolation, context injection, integrity checks, and completion hooks. This option has two materially different forms:
  1. **Repository/CI validation:** GitHub Actions or repository scripts validate that committed task records contain the required fields, phase markers, links, and permitted status values.
  2. **Live runtime integration:** Host-specific hooks read and inject task context on prompts/tool calls, attest planning state, and optionally influence when a run may stop.
- **Good:**
  - Repository/CI validation could catch missing or malformed structure consistently. It may be a useful narrow safeguard after a stable template and repeated failure pattern exist.
  - A supported agent runtime could automate plan selection, context re-surfacing, and some integrity checks. That could reduce reliance on the model remembering every procedural instruction.
  - A repository-specific implementation could be designed around the task record as the authority rather than copying the external file layout.
- **Neutral:**
  - GitHub Actions can react to repository events and validate committed documents. It cannot observe an uncommitted task state between ChatGPT tool calls, re-inject a plan into the current model turn, or enforce a live conversation stop condition.
  - Static checks are useful for syntax and cross-file consistency, but semantic exit criteria still require evidence review.
  - A later local agent runtime might expose hooks, but that would be a separate deployment target requiring its own design and verification.
- **Bad:**
  - The current ChatGPT/GitHub connector workflow does not expose the required local lifecycle hook interface. A live hook implementation would be inactive or would force an unapproved move to another host.
  - A custom framework creates scripts, test suites, permissions, runtime compatibility, error handling, documentation, and security boundaries that the repository must maintain.
  - A validator can create false confidence. Passing phase-format checks cannot establish that the objective was met, that evidence supports the result, or that the user approved the change.
  - Runtime context injection can repeatedly surface untrusted content. Hashing or delimiter framing does not convert external instructions into trusted instructions or replace repository approval controls.
  - A Stop gate can prolong an unproductive run or turn a soft procedural expectation into a runtime failure unless it has explicit caps, stall detection, host capability handling, and safe fallback behavior.
- **Fit and when it is preferable:** The CI-validation subset may become viable if the Option 3 pilot reveals repeated structural errors that a hosted check can reliably prevent. The live-hook subset is not viable in the current operating environment. Neither should be added pre-emptively.
- **Cost and residual risk:** High to very high, depending on whether the implementation is a narrow hosted validator or a full lifecycle system. A hosted validator would still leave semantic verification and live recovery manual. A runtime framework would add ongoing platform and security maintenance.


## Comparative Assessment

| Criterion | Option 1: Current workflow | Option 2: Direct three-file system | Option 3: Task-integrated plan | Option 4: Custom automation |
|---|---|---|---|---|
| Fit with current ChatGPT/GitHub workflow | **Strong** | **Weak** — assumes local files and host hooks | **Strong** | **Partial** — hosted checks only |
| Single task-authority integrity | **Strong** | **Weak** unless the task model is redesigned | **Strong** | **Moderate** if automation validates, but does not own, task state |
| Phase structure and exit criteria | **Weak** — prose only | **Strong** on supported hosts | **Strong** with explicit Worker checkpoints | **Partial** — can validate structure, not completion |
| Research evidence capture | **Moderate** — task prose and links | **Strong** — dedicated findings file | **Strong when triggered** — optional evidence note | **Partial** — metadata checks do not synthesize evidence |
| Recovery after context loss | **Moderate** — manual repository recovery | **Strong on compatible hosts**; current file-only benchmark not measured | **Moderate to strong** — same task record, manual re-read | **Partial** — CI cannot re-inject live context |
| Independent task isolation | **Moderate** — distinct task records | **Strong** — named plan directories and selectors | **Moderate to strong** — separate task records and output ownership | **Partial** — depends on design |
| Approval and trust-boundary fit | **Strong** — existing controls | **Moderate** — attestation is not approval and injected content remains untrusted | **Strong** — plan and evidence remain subordinate to user/task authority | **Moderate** — automation can be mistaken for semantic or user approval |
| Adoption and ongoing cost | **Low** | **Very high** | **Moderate** | **High to very high** |

**Overall assessment:** Option 1 has the lowest cost but does not close the identified process gaps. Option 2 has the most complete automation on compatible hosts but conflicts with this repository's current authority and runtime model. Option 3 gives the best balance of fit, control, and targeted improvement. Option 4 may later provide narrow structural checks but is not a substitute for a task plan or evidence review.

This is a qualitative architecture-fit comparison. It is not a weighted numerical score, a performance benchmark, or a guarantee that Option 3 will reduce recovery time. The three-task pilot is the proposed way to test whether its additional structure provides enough value here.


## Proposed Recommendation

Adopt **Option 3 — Integrate planning into the task record and add optional research notes**, using a staged rollout and the controls below.

This is a repository-fit decision, not a claim that Option 3 would outperform Planning with Files in a compatible local coding-agent host. Option 2 contains stronger built-in runtime mechanisms when its hooks and local filesystem are available. Those mechanisms are not available in the current ChatGPT/GitHub workflow, and direct adoption would split authority already held by the task record. Option 1 is cheaper, but it leaves the specific phase, single-action, and research-traceability gaps unresolved. Option 4 is premature until there is a supported runtime and evidence that static procedural controls are failing.

### Record ownership model

| Record | Authority | Purpose |
|---|---|---|
| Task record | The Worker | Scope, user approval, planning level, execution mode, phases, current state, one Next Step, progress, verification, and handoff |
| Findings note | The Worker, when required | Supporting research evidence and technical discoveries for one task; never task status or approval |
| Task board | The Worker | Task index and current execution pointer; not a second progress log |
| Discussion register | The Worker | Current-step navigation, open user decisions, and recent verified success reports |
| CI Ledger | Ledger processor | CI finding identity, recurrence, status, and evidence references |
| Draft and ADR | Decision governance | Proposals and accepted repository decisions |

The task record remains authoritative. A findings note supplements it. A findings note cannot approve scope, change task status, or override a user decision.

### 1. Select the planning level and execution mode

Use planning in proportion to task complexity.

| Planning level | Use when | Required structure |
|---|---|---|
| Lightweight | One narrow lookup, small edit, or single verification activity | Existing task sections, planning level, and one Next Step; no phase list or findings note |
| Phased | Work has multiple dependent stages, coordinated deliverables, multiple related files or workflows, work likely to span sessions, material risk, or an external approval gate | Execution Plan with named phases, objectives, exit criteria, phase status, and one Next Step |
| Research-led | Evidence from several sources or substantial comparative analysis is needed to support a decision or implementation | Phased plan plus a findings note only when evidence cannot remain concise and auditable in the task record |

Serial execution is the default. **Parallel is an execution mode, not a planning level.** Parallel execution requires explicit user authorization, separate work ownership, defined output paths, dependencies, and acceptance criteria. One orchestrator remains responsible for shared task state and indexes.

Use a phased plan when one or more of these conditions apply:

- The task has several distinct outcomes or dependencies.
- It requires research across multiple sources or comparison of competing specifications.
- It is likely to span several sessions.
- It changes a workflow, policy, architecture, or multiple related files.
- It contains a material risk, irreversible action, or external approval gate.
- Authorized parallel work requires separate assignments.

A prediction of five or more meaningful tool operations may prompt a complexity review. It is not a hard threshold. Do not create phases merely to satisfy a call count or to make a lightweight task look structured.

### 2. Add an Execution Plan to the task record

Update workspace/TASK_TEMPLATE.md from Version 1.3 to Version 1.4. Add an Execution Plan section immediately after Decisions.

Every new task records:

- Planning level: Lightweight, Phased, or Research-led.
- Execution mode: Serial by default, or Parallel with the approving user instruction and named owners.
- Intended completion condition.
- Current phase, or Not applicable for a Lightweight task.
- Exactly one immediate Next Step.
- Named phases in execution order when the task requires a phase plan.

Each phase records:

- One objective.
- Concrete actions or deliverables.
- Observable exit criteria.
- A status of pending, in_progress, or complete.

Use two to seven phases. Prefer three to seven when the work has enough distinct stages. Do not force artificial phases onto a Lightweight task.

Keep no more than one phase in_progress unless the user explicitly authorizes parallel execution. If an external condition prevents progress, set the task to the existing Blocked or Paused status. Do not mark the active phase complete merely because work is blocked.

A phase becomes complete only after its exit criteria pass. Link the evidence in the Progress Log or the findings note. Phase status is not task status.

Keep exactly one authoritative Next Step in the Execution Plan. It must identify the immediate executable action, not a broad goal such as "continue research". Update it whenever the active phase or immediate action changes.

Rename the existing Next Actions section to Following Actions. Keep it optional and use it only for ordered actions that follow the immediate Next Step. Do not repeat the Next Step or present a Following Actions item as current. Remaining Work records unresolved requirements and blockers, not another action pointer. The Progress Log's Next field describes what followed a historical entry; it does not override the current Next Step.

The task board remains an index and does not gain phase columns. Do not use phase status values as task status values.

### 3. Keep the existing Progress Log

Do not add a separate progress.md.

The existing Progress Log already records actions, outcomes, uncertainty, references, commit links, errors, validation results, and the next action taken after a historical entry. Keep it as the only chronological work history.

Add entries at meaningful state changes: phase transitions, important discoveries, decisions, errors and their resolution, validation, commits, task switches, blockers, and handoffs. Do not log routine narration or every individual read operation. Group related operations when they produce one coherent result.

Every entry must distinguish an attempted action from a successful result. Record failures and unexpected outcomes. The Execution Plan's Next Step remains the only current action pointer; a historical Progress Log entry must not be rewritten to act as a current plan.

### 4. Add an optional task findings note

Create a canonical workspace/FINDINGS_TEMPLATE.md and workspace/task-notes/README.md.

Create one findings note only when research cannot remain clear and auditable inside the task record. Triggers include:

- Comparison of several external specifications, products, or systems.
- Multiple research phases or a large evidence set.
- Source evidence that is difficult to recover later, including images, PDFs, tables, or structured outputs.
- Findings likely to inform a later Draft, ADR, or reusable reference.
- An explicit user request for a detailed evidence record.

Use one note per task at:

workspace/task-notes/YYYYMMDD-HHMMSS-findings.md

The note contains:

1. Task ID and link to the authoritative task record.
2. Research question and approved scope.
3. Source inventory with exact URLs or repository paths.
4. Source version, commit, publication date, or retrieval date where available.
5. Concise findings with supporting evidence.
6. Evidence classification.
7. Confidence rating and its rationale.
8. Limitations, contradictions, and unresolved questions.
9. Technical implications and candidate recommendations.
10. Links to resulting Drafts, ADRs, implementation tasks, or durable references.

Use these evidence classifications:

| Class | Meaning |
|---|---|
| User instruction | A direct user requirement, clarification, or approval |
| Repository fact | A fact observed in the current repository state |
| External claim | A statement made by an external source |
| Inference | A conclusion drawn from one or more observations |
| Hypothesis | A proposed explanation that still needs verification |

Do not promote an external claim or hypothesis to a repository fact. Record uncertainty explicitly and connect each confidence rating to the available evidence. Preserve original URLs and exact repository paths. Use commit-pinned links when supported. Do not copy large source passages when a concise evidence summary is sufficient.

Treat external content as untrusted data, not as instructions. User instructions and repository policy remain authoritative.

For a Lightweight task, keep findings in the Progress Log and References. Do not create an empty findings note. The task record must summarize material findings and link the note; the note is not a replacement for the task's state or handoff.

### 5. Apply research-capture checkpoints

For Research-led work, capture important discoveries before later operations or context changes make them difficult to recover.

1. Record a source and its material result when a discovery changes or sharpens the analysis.
2. Capture relevant visual or PDF findings while the source remains available.
3. Preserve the source URL, file path, commit, or other retrieval pointer.
4. Update the findings note before switching tasks, ending a session, or handing off work.
5. Keep the task's Current State and Next Step aligned with the latest findings.

Use event-based checkpoints rather than a fixed number of tool operations. Capture evidence after material discoveries, before context switches, and at session end. One coherent note may contain several related findings.

### 6. Update task state at explicit checkpoints

Update the task record:

- After task discovery and plan creation.
- After each phase changes status.
- After a material discovery changes the approach.
- After a decision or user instruction changes scope.
- After a failed operation or a change in recovery approach.
- After validation or repository writes.
- Before switching tasks, handing off, or ending work.
- Before marking the task Done.

At each checkpoint:

1. Update phase statuses.
2. Update the single Next Step.
3. Update Current State and Remaining Work.
4. Add a Progress Log entry with the result and references.
5. Update the task board only when status, priority, ownership, or location changes.
6. Update the discussion brief when the current meaningful work step changes.

Do not update every workspace index after every trivial operation. Keep each index within its existing purpose.

### 7. Recover from the repository state

Extend the Worker's existing recovery sequence:

1. Read workspace/discussion.md.
2. Read workspace/README.md and workspace/task_board.md.
3. Identify the task selected in Current Execution.
4. Read the complete task record.
5. Read its linked findings note, if one exists.
6. Check the current branch and relevant committed files through GitHub.
7. Compare the repository state with the task's Current State and latest Progress Log entry.
8. Resolve discrepancies before continuing.
9. Resume from the exact Next Step in the active phase.

Never select another task when the Current Execution pointer, task record, or dependency state is ambiguous. Reconcile the records or ask the user.

Use these recovery questions:

| Question | Source |
|---|---|
| Where is the work now? | Task status and current phase |
| What is the next action? | Execution Plan Next Step |
| What outcome must the task meet? | Objective and acceptance criteria |
| What did the Worker learn? | Findings note or task evidence |
| What work took place? | Progress Log and committed repository state |

Do not use conversation memory as a substitute for repository verification. Do not add automatic access to local session stores or transcripts.

### 8. Handle failures without repeating them

Record a failed operation in the Progress Log. Each failure entry includes the operation and observed error, attempt number, diagnostic finding, changed approach for the next attempt, and outcome or remaining blocker.

Never repeat the same failed operation with the same inputs without a new reason. Diagnose the failure before retrying.

Use three materially different attempts as a normal upper bound for one failure class. After that, stop and report the blocker. Ask the user for direction unless a clearly safe alternative remains. Stop earlier when another attempt risks data loss, broad scope change, security exposure, or an irreversible result. Do not exhaust a retry count when the safe action is to pause.

Do not hide an unresolved failure. Keep it in Open Discussions when it needs user attention.

### 9. Assign one owner to shared task state

Keep the Worker's existing one-current-task default.

The Worker or designated orchestrator owns the authoritative task record, its phase plan and Next Step, the task board, the discussion register, and the final handoff.

A delegated worker may own a clearly scoped output or evidence file. It must report its result to the orchestrator. It must not independently rewrite shared planning sections or task indexes.

For independent parallel work, create separate task records when outcomes and write scopes are distinct. Give each assignment an explicit owner, exact paths, dependencies, and acceptance criteria. Keep one orchestrator responsible for the parent outcome and shared indexes.

Do not use a shared mutable plan as a substitute for write ownership. If two workers need to update the same task state, serialize those updates through its owner. Do not introduce a shared active-plan pointer or automatic newest-plan selection; the task ID and task board already provide stable identity.

### 10. Separate planning from authority and completion

A plan describes how to execute approved work. It does not authorize more work.

- The original user request and later user instructions define the approved scope.
- Task approval authorizes only the task scope.
- A Draft remains a proposal until the user approves its exact revision.
- An ADR records an accepted repository decision.
- An implementation task must follow the accepted decision rules.
- Phase completion means that phase exit criteria passed.
- Task completion still requires the task acceptance criteria and current archive closeout rules.

A phase validator, checklist, or task status cannot prove semantic correctness by itself. Record the actual verification method, result, and limitation. Do not add an automatic Stop gate or unattended completion loop. The Worker must report a blocker or partial result honestly.

### 11. Preserve task evidence at closeout

Keep a findings note beside the active task while the task remains open.

When the task closes:

1. Include the relevant findings summary and source links in the final task record.
2. Move the exact findings note to archive/tasks/YYYYMMDD-HHMMSS-findings.md with the task archive.
3. Register the task record and findings note as separate entries with their exact archive paths. Use the same UTC archive timestamp for both files in the existing retention index.
4. Read back both archived files before deleting either active copy. If either archive write or read-back fails, keep both active records and reconcile the partial archive state.
5. Keep both archive records under the existing task retention policy.

Do not add findings notes to the report archive or create a separate findings retention process.

If a finding has continuing project value, propose a durable skill reference, ADR, or other canonical document before task closeout. Do not turn a task note into permanent policy without approval.

### 12. Keep existing workspace indexes focused

The task board remains an index. Do not add phase counts or duplicate progress details.

The discussion register keeps its existing sections and report limit. Current Step links the active task. Open Discussions links any Draft awaiting review. Reports contains only completed and verified outcomes.

The CI Ledger remains the source of truth for CI finding lifecycle and evidence references. A findings note may cite Ledger records. It must not create duplicate CI finding identities or become another active issue backlog.


## Consequences and Trade-Offs

- **Positive:** Complex tasks gain explicit phases, measurable exit conditions, and one immediate action inside the existing authoritative task record.
- **Positive:** A new session can recover phase, current action, blockers, and linked evidence through the same GitHub task record the Worker already reads.
- **Positive:** Research-heavy tasks preserve source versions, classifications, confidence, and limitations without requiring every task to create extra files.
- **Positive:** The task board, discussion register, and CI Ledger keep their existing responsibilities. No local filesystem or runtime hook is required.
- **Neutral:** The task template and Worker instructions become longer. Detailed phases remain conditional; lightweight tasks retain a small structure.
- **Neutral:** Phase management remains procedural. The Worker must update the plan at defined checkpoints, and no automatic per-turn injection is provided.
- **Neutral:** A findings note creates an additional file for selected tasks. It must be linked, archived, and retained with its task.
- **Negative:** The implementation spans the Worker, focused reference, task template, optional findings template and index, archive guide, catalog, and CI Ledger renderer/tests. These changes require coordinated review and hosted validation.
- **Negative:** Phased tasks require checkpoint updates. If the Worker does not reconcile the plan with repository state, the Execution Plan can become stale.
- **Negative:** Findings notes can become a duplicate knowledge base if the creation threshold is too low or their subordinate status is unclear.
- **Negative:** A human must evaluate semantic exit criteria. A structural check cannot prove that the objective was met or that the evidence is sufficient.

## Risks and Safeguards

| Risk | Likelihood / Impact | Safeguard | Residual risk |
|---|---|---|---|
| The Execution Plan duplicates the Progress Log or other task sections | Medium / Medium | The plan owns current phase and Next Step; the Progress Log owns chronology; Remaining Work owns unresolved requirements and blockers. | Authors may still repeat information unless reviewed at checkpoints. |
| Phases become artificial overhead | Medium / Medium | Use explicit complexity triggers and keep Lightweight tasks phase-free. Tool-call count is a prompt to assess complexity, not a hard threshold. | Classification still requires judgment. |
| A phase is marked complete without adequate evidence | Medium / High | Give every phase observable exit criteria and link verification in the Progress Log or findings note. Keep semantic review separate from structural validation. | A reviewer can still misinterpret weak evidence. |
| The current Next Step becomes stale or conflicts with Following Actions | Medium / High | Maintain exactly one current Next Step. Make Following Actions optional and subordinate. Reconcile the pointer with Current State and repository state at each checkpoint. | A skipped checkpoint can leave a stale pointer until recovery detects it. |
| A findings note becomes a second source of task authority | Medium / High | The task record owns status, scope, and approval. The findings note records evidence only. | A stale note can still mislead until reconciled. |
| Findings notes are created too often or abandoned | Medium / Medium | Define narrow creation triggers; prohibit empty notes; archive notes with their task; register exact paths under the existing retention policy. | Research value may expire under the existing retention period unless moved to an approved durable reference. |
| Concurrent workers overwrite shared task state | Medium / High | Serial execution is default. Parallel work needs user authorization, separate task IDs or isolated output files, and one orchestrator for shared indexes. | Concurrent writes can still conflict and require serialized reconciliation. |
| Ledger-generated tasks diverge from manually created tasks | Medium / High | Update the Ledger renderer, regression tests, and operator guide in the same implementation task as the task-template revision. | Hosted validation may expose untested formatting assumptions. |
| Archive or retention handling omits a findings note | Medium / Medium | Update the archive contract. Read back both the task archive and findings archive before deleting active copies. Register exact paths and the UTC timestamp. | A failed multi-file closeout still requires manual recovery. |
| External content is treated as trusted instruction | Medium / High | Treat source material and findings as untrusted data. Keep user instructions and repository policy authoritative. Do not add automatic content injection. | Prompt injection cannot be eliminated by Markdown formatting alone. |
| A future validator creates false confidence | Medium / Medium | Describe validation as structural only. Require evidence for semantic phase exits and retain normal task acceptance and user approval. | Structural checks cannot evaluate every meaning-dependent condition. |
| External benchmark figures are treated as repository guarantees | Medium / Medium | Record source versions, host, sample limits, and untested scenarios. Evaluate this design with the repository's three-task pilot. | The pilot is small and cannot prove every long-term benefit. |

## Repository Impact

| Area | Proposed change | Owner / files | Approval dependency |
|---|---|---|---|
| Worker instructions | Add complexity triggers, phase planning, checkpoints, evidence rules, and recovery steps. | `skills/the-worker/SKILL.md` | This Draft |
| Worker reference | Add the detailed task-planning and recovery procedure. | New `skills/the-worker/references/task-planning-and-recovery.md` | This Draft |
| Task template | Move to Version 1.4. Add an Execution Plan, one authoritative Next Step, and optional Following Actions. | `workspace/TASK_TEMPLATE.md` | This Draft |
| Findings template | Add a copy-ready research evidence format. | New `workspace/FINDINGS_TEMPLATE.md` | This Draft |
| Task notes index | Define when and how to create task findings notes. | New `workspace/task-notes/README.md` | This Draft |
| Workspace navigation | Link the optional findings format and note directory. | `workspace/README.md` | This Draft |
| Archive contract | Define closeout for task findings notes under the existing task archive and retention policy. | `archive/README.md` | This Draft |
| Document catalog | Register the new template and optional task-note family. | `skills/document-standards/references/document-type-catalog.md` | This Draft |
| CI Ledger renderer | Update exact template replacements for the new task structure. | `reports/triage/scripts/ledger.py` | This Draft |
| CI Ledger regression tests | Verify generated tasks contain the current template structure and valid phase placeholders. | `reports/triage/scripts/test_ledger.py` | This Draft |
| CI Ledger operator guide | Document any renderer or generated task handoff changes. | `reports/triage/README.md` | This Draft |
| Task board | Keep its current index structure. Do not add a phase column. | `workspace/task_board.md` | No structural change |
| Discussion register | Keep the existing three-section contract. | `workspace/discussion.md` | No structural change |
| Foundational initialization | Keep the current conditional load order. | `skills/SESSION_START.md`, `skills/INITIALIZATION_POLICY.md` | No change proposed |
| Skill index | Do not add a separate skill. | `skills/README.md` | No change proposed |

### Document catalog and path coverage

The current catalog already registers the task record family. The implementation must also register:

- `workspace/FINDINGS_TEMPLATE.md` as an exempt template source.
- `workspace/task-notes/README.md` as the embedded directory contract.
- `workspace/task-notes/*-findings.md` as a reserved task findings family.

Activate the findings-family path rule in the same commit that creates its first findings record. Do not create a dummy note only to activate the rule.

The new Worker reference follows the existing `skills/*/references/*.md` rule. The proposal does not need a separate Agent Skill definition.

### Compatibility and migration

Do not mass-migrate existing task records.

Use Task Template 1.4 for new tasks after implementation. The current canonical template is Version 1.3. The Worker must continue to read existing Version 1.2 and 1.3 task records. Do not mass-migrate them.

When an existing task resumes, add the Execution Plan only when it materially improves recovery. Preserve the original prompt and task ID. For a migrated record, replace the legacy `Next Actions` section with the v1.4 Execution Plan and optional `Following Actions`. The Worker must reconcile the latest Progress Log and repository state before setting the single Next Step.

The task board must keep existing links. The Ledger renderer must continue to generate valid v1.4 task records and preserve compatibility with current v1.2 and v1.3 records.

## Proposed Implementation Outline

After explicit user approval of this Draft revision:

1. Create the implementation ADR under the process established by ADR-0001. The accepted ADR must record this proposal's own decision and scope. ADR-0001 governs the process but does not approve this proposal's substance or implementation.
2. Create a separate implementation task that references the accepted ADR.
3. Update the task template, Worker skill, Worker reference, workspace navigation, archive contract, and Document Type Catalog.
4. Create the findings template and its directory README. Activate the path rule in the same commit that adds the first real findings note.
5. Update the CI Ledger renderer, regression tests, and operator guide in the same task.
6. Read back every changed path and check all links and path-coverage rules.
7. Use the appropriate GitHub-hosted validation workflow. Do not run scripts locally or poll CI.
8. Run the three-task pilot defined below after implementation and hosted validation pass.
9. Review every pilot acceptance criterion before general adoption.
10. Create a follow-up Draft before adding automation, hooks, or a separate skill.

Do not create implementation tasks as authorization to implement this Draft before approval.

## Three-Task Pilot and Acceptance Criteria

Run the pilot only after the accepted ADR, implementation task, coordinated repository changes, and hosted validation are complete. Use one naturally occurring eligible task from each category. Do not create dummy work to fill a pilot category. If a category does not arise, keep the pilot open until a suitable task exists.

| Pilot case | Required task characteristics | Expected planning treatment |
|---|---|---|
| Lightweight | One narrow lookup, small edit, or single verification activity | Lightweight level, no phase list, no findings note, and one Next Step |
| Phased | Several dependent stages or coordinated changes across multiple files | Phased level, named phases, exit criteria, phase status, and one Next Step |
| Research-led | Evidence from several sources or substantial comparative analysis | Research-led level, named phases, one findings note, and one Next Step |

The pilot passes only when all these criteria pass:

1. **Planning selection:** All three tasks use the correct planning level. The lightweight task has no artificial phases or findings note.
2. **Single action pointer:** Each task has exactly one clear, executable Next Step. Following Actions, Remaining Work, and historical Progress Log entries do not contradict it.
3. **Phase evidence:** Every phase in the phased and research-led tasks has a stated objective and measurable exit criteria. Each phase marked `complete` links to evidence in the Progress Log or findings note.
4. **Repository-only recovery:** A fresh Worker session can recover each task from the repository alone and identify its planning level, current phase or its not-applicable state, Next Step, blockers, and relevant evidence. Pass target: 3 of 3 tasks without relying on conversation history.
5. **Research traceability:** The research-led task's findings note records exact source locators, evidence classifications, confidence rationale, limitations, and unresolved questions. Every material external claim links to its source.
6. **Authority and ownership:** No task contains conflicting status authority, duplicate progress histories, or more than one `in_progress` phase unless the user approved parallel work.
7. **Findings-note lifecycle:** The pilot creates a findings note only for the research-led case unless another task meets the documented trigger. The research note archives with its task, both archive entries use the exact paths and UTC timestamp, and both remain under the existing retention policy.

If any criterion fails, pause general adoption. Revise the template, Worker procedure, or Ledger renderer as needed, then repeat the affected pilot case before rollout. Record the pilot results in the implementation task and link the evidence from the resulting ADR confirmation.

### Rollback and adjustment

If the phased plan causes unnecessary overhead, raise the trigger threshold and keep findings notes limited to research-heavy work.

If findings notes prove unnecessary, stop creating new ones. Preserve and close existing notes under the approved archive policy.

If the team later needs host-specific lifecycle automation, evaluate that capability in a separate Draft. Do not add unsupported automation as a hidden extension to this decision.

## Questions for the User

1. Do you approve DRAFT-0002 revision 2 and Option 3, including the v1.4 task template, optional findings notes, Worker reference, and coordinated Ledger updates?
2. Do you approve adapting the external project's concepts rather than installing or copying its complete system?
3. Do you approve the three-task pilot composition and pass criteria in this revision?

## Review and Approval

- **Revision presented:** 2
- **User decision:** Pending
- **Approved scope:** Not approved
- **Decision date:** Pending
- **Resulting ADR:** Not created

## Discussion and Revision History

| Date | Revision | Change | User feedback / decision |
|---|---|---|---|
| 2026-11-24 | 1 | Initial proposal based on Planning with Files and current Worker integration review. | Superseded by revision 2. |
| 2026-11-24 | 2 | Linked the proposal to accepted ADR-0001, targeted Task Template 1.4, established one authoritative Next Step, reconciled Following Actions, revised research checkpoints and findings-note closeout, defined a measurable three-task pilot, and addressed the Draft's recorded lint findings. | User approved preparation of revision 2 only. Decision approval remains pending. |

## References

- External repository: https://github.com/OthmanAdi/planning-with-files
- External branch head: https://github.com/OthmanAdi/planning-with-files/commit/aaa38bc62053f5f7c1bfbcb60f0405f7cf0ee228
- External canonical skill: `skills/planning-with-files/SKILL.md`
- External templates: `templates/task_plan.md`, `templates/findings.md`, `templates/progress.md`
- External workflow: `docs/workflow.md`
- External long-running task guide: `docs/long-running-agent-tasks.md`
- External plan inventory: `skills/planning-with-files/plan-inventory.md`
- External security policy: `SECURITY.md`
- External resolver and validation: `scripts/resolve-plan-dir.sh`, `scripts/check-complete.sh`, `scripts/gate-stop.sh`, and `tests/test_check_complete_resolver.py`
- Current Worker: `skills/the-worker/SKILL.md`
- Worker Conversation Mode: `skills/the-worker/references/conversation-mode.md`
- Current task template: `workspace/TASK_TEMPLATE.md` (Version 1.3 at Draft revision time; proposed target Version 1.4).
- Workspace navigation: `workspace/README.md`
- Task renderer and tests: `reports/triage/scripts/ledger.py` and `reports/triage/scripts/test_ledger.py`
- Document Type Catalog: `skills/document-standards/references/document-type-catalog.md`
- Related accepted decision: [ADR-0001 — Establish Draft-to-ADR Governance and Repository Analysis](../../archive/adr/0001-establish-draft-to-adr-governance-and-repository-analysis.md). ADR-0001 governs the decision process and does not approve this proposal's substance or implementation.
