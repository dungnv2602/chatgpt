---
record_type: decision-draft
template_version: "1.2"
id: "DRAFT-0010"
revision: 1
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

Replace the central CI report/Ledger remediation lifecycle with self-contained, folder-based CI error subtasks. Each distinct actionable CI error becomes its own child task folder containing its task record and all material needed to resolve it. The Worker commits a fix and lets the configured CI workflow generate any next error subtasks. No separate manual fix-verification step is performed. Completed child folders are deleted; when no new error subtasks are generated and no work remains, delete the entire parent CI task folder.

This proposal changes accepted rules in ADR-0003, ADR-0004, and ADR-0007 where they conflict with the approved model. It does not authorize implementation until the user approves this exact Draft revision and a superseding ADR is accepted.

## Context and Problem Statement

Current repository contracts define CI diagnostics as report artifacts under .takeout/reports/, with a unified index and Ledger. The Ledger owns finding identity, report intake, recurrence, attribution, and child publication. Subtasks are flat Markdown records under a parent's subtasks directory. CI completion uses commit/readback evidence.

The user has approved a different operating model:
- Each CI error generates an independent subtask folder.
- Each folder contains its task record and all evidence/instructions needed to resolve its error.
- The Worker commits the fix and relies on automatic CI capture to generate subsequent error subtasks.
- No manual fix verification is performed. If the configured CI capture generates no new error subtasks after the fix cycle, the workflow treats the remediation loop as complete.
- Delete the complete child folder when that error task is finished. Delete the parent CI task folder when no child work remains.

The exact path named for retirement was .take/reports. Repository search found no such path. Current active contracts point to .takeout/reports/. This Draft does not assume those paths are interchangeable; the user must confirm the intended target before destructive retirement.

## Goals and Non-Goals

### Goals

- One self-contained child task folder per distinct actionable CI error.
- Each child contains the diagnostic payload, source commit and Task-ID attribution, affected paths, relevant evidence, and instructions required to resolve it.
- Reuse an active child only when the same error identity recurs while that child exists; keep distinct errors separate.
- Use automatic CI-generated child creation as the feedback and completion signal.
- Remove manual fix-verification as a separate Worker step.
- Delete completed child folders and delete the parent CI task folder after the loop reaches quiescence.
- Retire the central report/Ledger system and obsolete references after coordinated migration.

### Non-Goals

- Do not manually inspect, poll, dispatch, rerun, or wait for hosted CI results.
- Do not create synthetic parent tasks for files, jobs, workflows, or errors.
- Do not retain a second central findings database or report archive.
- Do not claim that no generated subtasks proves the absence of every possible defect; it means the configured CI capture produced no actionable error tasks for that cycle.
- Do not delete .takeout/reports/ until the user confirms this is the intended path and replacement capture is ready.

## Decision Drivers

| Criterion | Why it matters | Relative importance |
|---|---|---|
| Error isolation | Each error must be independently actionable and removable. | High |
| Self-containment | A child must not depend on a central Ledger or sibling folder. | High |
| Feedback-loop reliability | Missing capture must not be confused with a clean CI cycle. | High |
| Low operational overhead | Avoid manual verification and central state reconciliation. | High |
| Cleanup semantics | Completed work should leave no stale task folders or report artifacts. | High |
| Attribution and deduplication | Errors attach to the triggering genuine parent without duplicate active work. | High |
| Migration safety | Existing workflows and accepted ADRs must be replaced coherently. | High |

## Assessment Basis and Evidence Limits

- **Scope of comparison:** Current report/Ledger workflow; folder-based CI child workflow without a central Ledger; hybrid report index plus folder-based children.
- **Assessment method:** Static inspection of current Worker, task/subtask templates, document catalog, Workflow Map, workspace README, and accepted ADRs on branch gpt on 2026-11-28.
- **Evidence boundary:** Repository documents establish current written contracts, not runtime behavior. No local tests or hosted CI results were inspected.
- **Key assumptions:** CI can reliably create task folders from actionable errors and trigger after every relevant fix commit.
- **Unresolved evidence gaps:** Exact report directory to retire; current workflow's ability to write self-contained child folders without the Ledger; trigger/capture failure behavior; duplicate detection without persistent central identity state.

## Considered Options

### Option 1 — Keep the report/Ledger workflow and flat child records

- **Description and operating model:** Retain unified reports and Ledger as the source of truth. The Ledger groups findings and creates flat child Markdown records under parent tasks. Worker uses commit/readback completion.
- **Repository and environment fit:** Matches ADR-0003, ADR-0004, ADR-0007, current Worker references, and existing generator paths.
- **Good — strengths:** Lowest migration cost; preserves existing identity, recurrence, evidence, and index machinery.
- **Neutral — trade-offs:** Existing report infrastructure remains central and requires ongoing maintenance.
- **Bad — weaknesses:** Does not satisfy folder-per-error, self-contained subtask folders, or the no-manual-verification rule.
- **Implementation and migration cost:** Lowest; mostly maintain current implementation.
- **Dependencies and operational burden:** Requires report indexes, Ledger, schemas, shared eligibility logic, and report capture.
- **Risks and safeguards:** Central state can flood, drift, or become inconsistent with task folders. Existing idempotency and attribution safeguards mitigate some risk but do not meet the requested lifecycle.
- **Evidence and confidence:** Current ADRs and Worker/template paths explicitly describe this model; high confidence about documented contracts.
- **Limitations and unknowns:** Runtime behavior has not been tested in this review.

### Option 2 — One self-contained folder per CI error with automatic feedback loop

- **Description and operating model:** CI creates one child folder for each distinct actionable error under the triggering genuine parent task. Each folder contains task.md, exact diagnostics, relevant logs/evidence, source commit and Task-ID attribution, affected paths, and references needed to fix the error. The Worker fixes and commits; CI runs automatically and creates further error folders if needed. No manual fix verification is performed. A completed child folder is deleted. When no new error folders are generated and no child work remains, the parent CI task folder is deleted.
- **Repository and environment fit:** Matches the approved model but requires changes to Worker, CI capture workflows, task/subtask folder templates, catalog, board reconciliation, and existing report/Ledger producers.
- **Good — strengths:** Each error is isolated and self-contained; cleanup is simple; no central findings database; automatic CI becomes the feedback mechanism.
- **Neutral — trade-offs:** Historical diagnostics are intentionally discarded with completed folders. A later recurrence is a new error task.
- **Bad — weaknesses:** Without a central identity store, duplicate detection across deleted/completed work is limited. If CI capture fails silently or does not run, absence of child folders could be mistaken for success.
- **Implementation and migration cost:** Highest; coordinated changes are needed across workflows, scripts, templates, indexes, skills, ADRs, and active task records.
- **Dependencies and operational burden:** CI must be able to create folders and update task indexes. Worker must keep board and parent/child indexes synchronized. Capture failures need a visible failure path.
- **Risks and safeguards:** Distinguish a completed CI cycle with no actionable errors from a missing or failed capture; reuse a matching child only while it remains active; include all needed context; delete only after the fix commit has triggered the next capture cycle.
- **Evidence and confidence:** User approval establishes the desired lifecycle. Current repository contracts establish the migration surface. Feasibility is an inference until workflow code is reviewed and changed.
- **Limitations and unknowns:** Capture mechanism and path write permissions have not been inspected as part of this Draft. No prototype or runtime replay has been performed.

### Option 3 — Retain a thin CI run index but move remediation into self-contained folders

- **Description and operating model:** Keep a minimal run/capture status index to distinguish completed CI cycles from missing/failed capture, but place every actionable error and its working evidence in a separate child folder. Do not keep a central findings Ledger.
- **Repository and environment fit:** Transitional compromise; still depends on central CI metadata and does not fully retire the report system.
- **Good — strengths:** Provides an explicit signal that a CI cycle completed, reducing the risk that no children means no capture.
- **Neutral — trade-offs:** Some central metadata remains, but it is not a findings database.
- **Bad — weaknesses:** Retains infrastructure the user wants retired and adds a second completion signal.
- **Implementation and migration cost:** High; requires redesign but less than removing all capture metadata.
- **Dependencies and operational burden:** Requires a minimal run-status producer and consumer, plus child-folder generation and cleanup.
- **Risks and safeguards:** The index may regrow into a Ledger. Strictly limit it to cycle success/failure; do not store findings, evidence, or task lifecycle.
- **Evidence and confidence:** The existing unified index demonstrates a current place for capture metadata; the minimal alternative is an architectural inference.
- **Limitations and unknowns:** User has not approved retaining any report index.

## Comparative Assessment

| Criterion | Option 1: Existing Ledger | Option 2: Folder loop | Option 3: Thin run index |
|---|---|---|---|
| One folder per error | Weak | Strong | Strong |
| Self-contained remediation | Partial | Strong | Strong |
| No manual fix verification | Weak | Strong | Strong |
| Central state overhead | High | Low | Moderate |
| Distinguishes clean cycle from failed capture | Strong | Requires safeguards | Strong |
| Complete report-system retirement | No | Yes | Partial |
| Migration cost | Low | High | High |

### Overall comparison

Option 1 is easiest to retain but fails the approved lifecycle. Option 3 improves isolation but retains central capture state contrary to the requested retirement. Option 2 best matches the approved direction, provided CI can distinguish a completed no-error cycle from a missing or failed capture. This is a capture-integrity condition, not manual fix verification.

## Proposed Recommendation

Adopt Option 2. Make CI create self-contained per-error task folders and use subsequent automatic CI task generation as the remediation feedback loop. Do not manually inspect or verify fixes. Keep only the minimal workflow behavior required to guarantee that a CI cycle actually triggers and task creation is not silently skipped; do not retain a central findings Ledger or report archive.

Confirm whether the intended retirement target is .take/reports (not found) or .takeout/reports/ (the active repository path). If .takeout/reports/ is intended, migrate every consumer before deleting it.

## Consequences and Trade-Offs

- **Positive:** Self-contained error work; one folder is the unit of execution and deletion; no central findings Ledger; automatic feedback loop.
- **Negative:** Completed CI evidence and recurrence history are deleted with the child folder. Future recurrence is treated as a new error.
- **Neutral:** Parent tasks remain genuine user tasks; CI error folders remain children, not synthetic parents.
- **Conditional:** Reliability depends on CI triggering and task-folder generation being trustworthy.

## Risks and Safeguards

| Risk | Likelihood / Impact | Evidence / rationale | Safeguard | Residual risk |
|---|---|---|---|---|
| CI does not run after a commit | Unknown / High | Trigger behavior not yet inspected | Require the configured trigger path for every in-scope fix commit | Workflow misconfiguration can still suppress a run |
| Capture fails but creates no child | Unknown / High | Capture behavior not yet inspected | Distinguish capture failure from a successful cycle with zero actionable errors | A failed capture may need a visible blocker |
| Duplicate errors create flooding | Medium / Medium | Same error can recur across cycles | Stable signature and reuse only while matching child remains active | Deleted history limits long-term correlation |
| Child lacks needed evidence | Medium / High | Self-containment is a new contract | Include exact diagnostic payload, source commit, attribution, affected paths, and instructions | Some external logs may expire |
| Premature deletion loses active work | Low / High | Folder deletion is destructive | Delete only after child resolution and the next CI capture opportunity | No retained archive by design |
| Old consumers reference retired paths | High / High | Current docs and ADRs reference .takeout/reports/ | Inventory and migrate all consumers before deleting the actual path | External references may remain |

## Repository Impact

| Area | Proposed change | Owner / exact files | Approval dependency |
|---|---|---|---|
| Decision records | Supersede conflicting report/Ledger and flat-child rules | ADR-0003, ADR-0004, ADR-0007; new ADR | This Draft |
| Worker lifecycle | Define folder-per-error generation, automatic CI feedback, deletion, no manual fix verification | .agent/skills/the-worker/SKILL.md and CI references | Accepted ADR |
| Task/subtask formats | Define subtask folder with task.md, evidence, and index integration | SUBTASK_TEMPLATE.md, TASK_TEMPLATE.md, document catalog | Accepted ADR |
| CI producer | Generate child folders from actionable errors; remove central Ledger/report writers | .github/workflows/, .agent/skills/the-worker/scripts/ | Accepted ADR |
| Navigation | Remove obsolete report links and map CI flow to task folders | .agent/WORKFLOW_MAP.md, workspace/README.md, task board | Accepted ADR |
| Data retirement | Delete confirmed obsolete report tree after migration | User-confirmed exact path; current candidate .takeout/reports/ | User path confirmation and accepted ADR |

## Proposed Implementation Outline

1. Approve this Draft revision and exact report-tree retirement path.
2. Promote the Draft to a superseding ADR for ADR-0003, ADR-0004, and ADR-0007 where rules conflict.
3. Update canonical task/subtask folder contracts and document catalog before creating subtask folders.
4. Update CI capture to create one self-contained child folder per distinct actionable error under the genuine parent identified by the source commit Task-ID trailer.
5. Remove Ledger and report-index dependencies from remediation. Ensure capture failure is not treated as a clean cycle.
6. Update Worker and Workflow Map to commit fixes and rely on automatic CI-created children; do not perform separate manual fix verification.
7. Migrate existing active tasks/records only as required; do not backfill historical reports.
8. Remove obsolete report producers, consumers, schemas, scripts, indexes, and the confirmed report tree after replacement is operational.
9. Execute two workstreams: (a) folder-based CI generation and feedback loop; (b) report-system retirement and reference cleanup.
10. At quiescence, delete completed child folders and then the entire parent CI task folder. No archive copies.

## Questions for the User

1. The repository contains .takeout/reports/, not .take/reports/. Did you intend the existing .takeout/reports/ directory to be retired?

## Review and Approval

- **Revision presented:** 1
- **User decision:** Pending exact Draft review
- **Approved scope:** Direction approved in conversation; formal approval of this Draft revision and exact path is pending.
- **Decision date:** Pending
- **Resulting ADR:** Not created

## Discussion and Revision History

| Date | Revision | Change | User feedback / decision |
|---|---|---|---|
| 2026-11-28 | 1 | Prepared a superseding CI folder/feedback-loop proposal based on the user's approved direction; recorded repository path discrepancy and required safeguards. | Pending exact Draft review |

## References and Evidence Register

| ID | Source / exact locator | Version, date, or commit | Evidence type | Supports which option / claim | Limitations |
|---|---|---|---|---|---|
| E1 | .agent/skills/the-worker/SKILL.md, Task hierarchy and CI attribution; CI/Actions operational ownership; Canonical CI implementation | Branch gpt, retrieved 2026-11-28 | Repository fact | Current Ledger ownership, attribution and report paths | Written contract, not runtime proof |
| E2 | .agent/skills/the-worker/references/ci-ledger.md | Branch gpt, retrieved 2026-11-28 | Repository fact | Central identity, report intake, and child generation | Written contract, not runtime proof |
| E3 | .agent/skills/the-worker/assets/SUBTASK_TEMPLATE.md v1.6 and TASK_TEMPLATE.md v2.7 | Branch gpt, retrieved 2026-11-28 | Repository fact | Flat subtask record format and parent task folder format | Written contract, not runtime proof |
| E4 | .agent/skills/the-worker/references/document-type-catalog.md v1.27 | Branch gpt, retrieved 2026-11-28 | Repository fact | Catalog classifies subtask records and reports as template/generator-owned | Current path coverage needs migration review |
| E5 | workspace/adr/0003-canonical-github-actions-diagnostic-report-artifact-layout.md, workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md, workspace/adr/0007-unified-index-as-latest-lint-report-locator.md | Branch gpt, retrieved 2026-11-28 | Repository fact | Accepted decisions this proposal would supersede | Decision rationale must be preserved in resulting ADR |
| E6 | .agent/WORKFLOW_MAP.md and workspace/README.md | Branch gpt, retrieved 2026-11-28 | Repository fact | Current CI flow and report navigation | Map and navigation are summaries |
| E7 | User's messages in this conversation approving per-error folders, deletion, and automatic CI feedback loop | 2026-11-28 | User instruction | Proposed Option 2 | Exact report path remains unresolved |
