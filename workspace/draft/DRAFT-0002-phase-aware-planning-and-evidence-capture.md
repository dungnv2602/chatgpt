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

The recommended implementation is deliberately narrower than the external system:

1. **Keep one task authority.** The task record remains the only authority for task scope, approval, status, phase state, current action, progress, verification, and handoff. Do not add a separate task_plan.md or progress.md.
2. **Add proportional planning.** Use three planning levels: Lightweight, Phased, and Research-led. Lightweight tasks have no phase list. Phased tasks have named phases and measurable exit criteria. Research-led tasks use the phased structure and add a findings note only when its evidence needs a separate record.
3. **Separate planning depth from concurrency.** Serial execution remains the default. Parallel execution is a separate mode, not a fourth complexity level. It requires explicit user authorization, separate work ownership, defined output paths, and one orchestrator for shared task state.
4. **Keep one current action.** Add one authoritative Next Step to the Execution Plan. Make Following Actions optional and subordinate. Do not let Remaining Work or historical Progress Log entries present a competing current action.
5. **Keep the Progress Log.** It remains the only chronological activity history. Record material discoveries, phase transitions, errors, decisions, validation, commits, blockers, and handoffs without logging every routine read.
6. **Create findings notes selectively.** Record research in the task record when it remains concise. Use a findings note when source evidence is extensive, comparative, multimodal, or likely to inform a later Draft/ADR. Findings notes supplement the task; they do not set status, approve scope, or override task decisions.
7. **Preserve repository compatibility.** Update The Worker and one focused reference, Task Template 1.3 to 1.4, Document Type Catalog coverage, archive documentation, and the CI Ledger renderer/tests as one coordinated implementation scope. Keep existing Version 1.2 and 1.3 task records readable; do not mass-migrate them.
8. **Validate by use, not by benchmark transfer.** After implementation and hosted validation, run the three-task pilot below. Do not claim a recovery improvement until this repository's own pilot evidence supports it.

Do not add runtime hooks, automatic context injection, a Stop gate, or a new standalone skill in this decision. Reassess those capabilities only through a separate Draft if a supported runtime becomes available and measured failures justify the additional system.

## Consequences and Trade-Offs

- **Positive:** Complex tasks gain explicit phases, exit criteria, and one immediate next action.
- **Positive:** A new session can recover the current phase without reconstructing it from a long activity log.
- **Positive:** Research-heavy tasks retain evidence with source context, confidence, and limitations.
- **Positive:** The existing task record remains authoritative for status, approval, and progress.
- **Positive:** Simple tasks avoid extra planning files.
- **Neutral:** The Worker must update task phases and evidence at defined checkpoints.
- **Neutral:** The task template becomes longer. Its phased sections remain optional for lightweight tasks.
- **Negative:** The Ledger renderer and its tests need coordinated updates when the task template changes.
- **Negative:** Optional findings notes add a second active file and an archive-retention entry for some tasks.
- **Negative:** A human must assess phase status and completion. This environment has no automatic hook for that purpose.

## Risks and Safeguards

| Risk | Likelihood / Impact | Safeguard | Residual risk |
|---|---|---|---|
| Task template duplicates the Progress Log | Medium / Medium | Keep chronology only in the task Progress Log. | A worker may still repeat details in multiple sections. |
| Phases become artificial overhead | Medium / Medium | Use planning levels and skip phases for lightweight tasks. | Complexity classification requires judgment. |
| A worker marks a phase complete without evidence | Medium / High | Define observable exit criteria and record verification. | Semantic review can still miss a gap. |
| External content becomes an instruction source | Medium / High | Treat findings and source material as untrusted data. | Model-level prompt injection cannot be eliminated by Markdown framing. |
| A findings note conflicts with the task record | Low / High | Task record owns status and approval. Findings notes are evidence only. | A stale note can still mislead until reconciled. |
| Concurrent workers overwrite shared state | Medium / High | One owner controls the task record, board, and discussion register. | Remote write conflicts still require reconciliation. |
| Ledger task generation breaks after template edits | Medium / High | Update renderer and tests in the same implementation task. | Hosted validation may reveal untested formatting assumptions. |
| Task evidence is lost at closeout | Medium / Medium | Archive any findings note with the task and index its exact path. | Retention removes both after the existing 90-day period. |
| The design expands into an unsupported hook system | Medium / Medium | Do not add hooks, scripts, or completion gates in the initial scope. | Future runtime changes may justify a separate Draft. |

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
