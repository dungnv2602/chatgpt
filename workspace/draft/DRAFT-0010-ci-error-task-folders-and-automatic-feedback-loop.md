---
record_type: decision-draft
template_version: "1.2"
id: "DRAFT-0010"
revision: 3
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

The user confirmed on 2026-11-28 that the intended retirement target is the existing .takeout/reports/ directory (not .take/reports). Retire that exact directory and its contents after the replacement folder-based CI capture workflow is ready and all consumers have been migrated.

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
- Do not delete .takeout/reports/ until the replacement capture workflow is ready and all consumers have been migrated. The user has confirmed this is the intended directory.

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
- **Unresolved evidence gaps:** Current workflow's ability to write self-contained child folders without the Ledger; trigger/capture failure behavior; duplicate detection without persistent central identity state.

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

### Option 3 — Keep a thin CI run-status index inside workspace/ and move remediation into self-contained folders

- **Description and operating model:** Retain only a compact CI run-status index under workspace/. For each relevant commit, record the commit SHA, run identifier, workflow identity, completion time, and terminal outcome (success, failure, or infrastructure/capture failure). A successful status means the configured CI checks completed successfully for that exact commit. All actionable errors and their evidence remain exclusively in individual self-contained CI subtask folders. The index may link to active error folders but must not store findings, diagnostic payloads, evidence, recurrence identity, or remediation state.
- **Repository and environment fit:** Fits the requested folder-based remediation model while preserving a narrow, auditable signal that the configured validation cycle actually ran. The index is workspace-owned metadata, not a report artifact under .takeout/reports/.
- **Good — strengths:** Confirms whether the post-commit CI cycle completed; distinguishes a successful clean cycle from a failed run or failed capture; retains commit-specific validation status without retaining a findings Ledger.
- **Neutral — trade-offs:** A small central metadata file remains and requires a defined schema, writer, and reader. This is not a full retirement of all CI metadata, but it does retire the report/finding system and its .takeout/reports/ location.
- **Bad — weaknesses:** A green status is only as meaningful as the checks configured in that workflow; it does not prove the absence of defects outside their coverage. A status index can become a Ledger if its scope is not constrained.
- **Implementation and migration cost:** High; requires a new minimal status writer/consumer, folder-based error capture, and coordinated removal of report/Ledger consumers.
- **Dependencies and operational burden:** CI must publish an unambiguous terminal state for each relevant commit. The status writer must distinguish success, actionable test/check failure, and infrastructure/capture failure. Consumers must not infer success from a missing record.
- **Risks and safeguards:** Freeze the allowed fields and reject findings/evidence payloads in the index. Require a matching commit SHA and terminal state. Treat missing, pending, cancelled, or capture-failed status as not validated, never as success. Keep error identity and all remediation material in child folders only.
- **Evidence and confidence:** The need for a completion signal follows from the user's approved no-manual-verification loop; the exact index schema and workflow feasibility remain design work. No runtime behavior has been verified.
- **Limitations and unknowns:** Exact workflow events, status APIs, write permissions, and whether all relevant checks report a reliable terminal state remain to be inspected during implementation.

## Comparative Assessment

| Criterion | Option 1: Existing Ledger | Option 2: Folder loop | Option 3: Thin run index |
|---|---|---|---|
| One folder per error | Weak | Strong | Strong |
| Self-contained remediation | Partial | Strong | Strong |
| No manual fix verification | Weak | Strong | Strong |
| Central state overhead | High | Low | Low–moderate, tightly bounded |
| Distinguishes clean cycle from failed capture | Strong | Requires safeguards | Strong, with explicit terminal states |
| Complete report-system retirement | No | Yes | Yes; retains only run-status metadata under workspace/ |
| Migration cost | Low | High | High |

### Overall comparison

Option 1 is easiest to retain but fails the approved lifecycle. Option 2 fully removes central state, but its clean-cycle signal depends entirely on reliable capture behavior. Option 3 preserves the folder-based remediation model while retaining only the minimum commit-specific run outcome needed to know whether automated validation actually completed. The decisive boundary is that the index records run status only: no findings, logs, evidence, deduplication state, or remediation history. With that boundary, Option 3 retires .takeout/reports/ and the central findings Ledger while retaining a useful validation signal.

## Proposed Recommendation

Adopt Option 3. Keep a minimal CI run-status index inside workspace/ and make CI create self-contained per-error task folders. The index records only commit-specific run identity and terminal outcome, allowing the workflow to distinguish successful validation from failed checks or failed capture. All actionable errors and all remediation evidence live only in their own child folders. Do not retain a central findings Ledger or report archive, and do not retain any index under .takeout/reports/.

The user confirmed .takeout/reports/ as the intended retirement target. Migrate every consumer, make folder-based capture and run-status recording operational, and then delete that directory. The Worker does not manually verify fixes; the subsequent automated run is the validation signal.

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

1. Approve this Draft revision and the workspace-local run-status index scope; the exact report-tree retirement path is confirmed.
2. Promote the Draft to a superseding ADR for ADR-0003, ADR-0004, and ADR-0007 where rules conflict.
3. Update canonical task/subtask folder contracts and document catalog before creating subtask folders.
4. Update CI capture to create one self-contained child folder per distinct actionable error under the genuine parent identified by the source commit Task-ID trailer.
5. Replace the old report index with a strictly bounded run-status index under workspace/. Remove Ledger and report-index dependencies from remediation. Ensure missing or failed capture is never treated as a successful clean cycle.
6. Update Worker and Workflow Map to commit fixes and rely on automatic CI-created children; do not perform separate manual fix verification.
7. Migrate existing active tasks/records only as required; do not backfill historical reports.
8. Remove obsolete report producers, consumers, schemas, scripts, indexes, and the confirmed report tree after replacement is operational.
9. Execute two workstreams: (a) folder-based CI generation and feedback loop; (b) report-system retirement and reference cleanup.
10. At quiescence, delete completed child folders and then the entire parent CI task folder. No archive copies.

## User Clarification

- **2026-11-28:** User confirmed that the intended retirement target is .takeout/reports/.
- **2026-11-28:** User selected Option 3: retain the successful-run status concept, move the index inside workspace/, and use it to identify whether committed changes passed the configured automated CI checks. The index must remain run-status-only; findings and evidence belong in self-contained error folders.

## Review and Approval

- **Revision presented:** 3
- **User decision:** Option 3 selected and approved as the preferred architecture direction; exact report target confirmed as .takeout/reports/. This revision incorporates the selected run-status-only index model and is awaiting approval as a complete consolidated Draft.
- **Approved scope:** Desired operating model and report retirement target confirmed; implementation still requires a superseding accepted ADR.
- **Decision date:** 2026-11-28
- **Resulting ADR:** Not created

## Discussion and Revision History

| Date | Revision | Change | User feedback / decision |
|---|---|---|---|
| 2026-11-28 | 1 | Prepared the superseding CI folder/feedback-loop proposal and documented the repository path discrepancy. | User approved the operating model; clarified the intended directory. |
| 2026-11-28 | 2 | Confirmed .takeout/reports/ as the exact retirement target and removed the unresolved-path question. | User confirmed the path. |
| 2026-11-28 | 3 | Selected Option 3; narrowed the retained index to commit-specific CI run status only and relocated it under workspace/. Clarified that success means configured checks completed successfully for the exact commit, while missing/failed capture is not success. | User approved Option 3 and requested feedback on the approach; awaiting approval of the consolidated revision. |

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
