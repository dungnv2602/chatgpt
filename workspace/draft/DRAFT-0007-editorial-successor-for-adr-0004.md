---
record_type: decision-draft
template_version: "1.2"
id: "DRAFT-0007"
revision: 1
status: "in-review"
created: "2026-11-27"
updated: "2026-11-27"
proposed_by: "Assistant"
decision_makers:
  - "User"
consulted: []
informed: []
related_drafts: []
related_adrs:
  - "ADR-0004"
  - "ADR-0003"
resulting_adr: null
promotion_cleanup_pending: false
cleanup_reason: null
---

# Editorial Successor for ADR-0004

## Proposal Summary

This Draft proposes a successor record for ADR-0004. The successor would correct editorial lint findings only. It would preserve Option 3, its approved scope, lifecycle rules, and Confirmation criteria. ADR-0004 would remain unchanged. The user must approve this exact Draft before any successor ADR or source edit.

## Context and Problem Statement

ADR-0004 is an accepted decision record. Decision Governance protects its decision content from direct edits. The current CI Ledger records 34 distinct findings against its prose.

- 8 long-sentence findings.
- 19 passive-voice findings.
- 1 semicolon finding.
- 5 synonym-rotation findings.
- 1 present-perfect finding.

The findings group under five P0 tasks. The tasks remain Proposed because no accepted ADR authorizes the requested wording changes.

- [Long-sentence task 20261127-013151-30](../tasks/20261127-013151-30/task.md)
- [Passive-voice task 20261127-013151-31](../tasks/20261127-013151-31/task.md)
- [Semicolon task 20261127-013151-32](../tasks/20261127-013151-32/task.md)
- [Synonym-rotation task 20261127-013151-33](../tasks/20261127-013151-33/task.md)
- [Present-perfect task 20261127-013151-34](../tasks/20261127-013151-34/task.md)

The accepted decision selects Option 3. It uses task folders with nested subtasks. CI remediation completion depends on a verified commit. Hosted validation remains separate metadata. The decision also covers recurrence history, ingestion integrity, Worker selection, decision governance, task migration, and legacy archive compatibility. This Draft does not propose a different task or Ledger lifecycle.

## Goals and Non-Goals

### Goals

- Resolve the identified editorial findings without changing the accepted decision.
- Preserve every lifecycle rule, requirement, constraint, risk, safeguard, and Confirmation criterion.
- Preserve implementation status and the link to task 20261126-232913.
- Preserve the pending state of Confirmation criterion 15.
- Preserve the verified state of Confirmation criterion 16.
- Keep ADR-0004 immutable and retain its complete history.
- Create a clear successor link if the user approves the proposal.

### Non-Goals

- Change task folder structure or subtask semantics.
- Change commit-based completion or hosted-validation metadata.
- Change Ledger identity, recurrence, ingestion, retention, or archive behavior.
- Change Worker selection or accepted-ADR governance.
- Claim that hosted regression or Document Type Catalog validation passed.
- Implement any change before the user approves this Draft and its successor ADR.

## Decision Drivers

| Criterion | Why it matters | Relative importance |
|---|---|---|
| Decision integrity | The successor must preserve the accepted outcome and scope. | High |
| Governance compliance | The process must not rewrite an accepted record. | High |
| CI remediation | The proposal must address all 34 recorded findings. | High |
| Confirmation integrity | Existing verified and pending states must remain accurate. | High |
| Traceability | Readers must locate both the predecessor and successor. | High |
| Implementation cost | The change should avoid unrelated source or workflow work. | Medium |
| Reviewability | The user must approve an exact revision and scope. | High |

## Assessment Basis and Evidence Limits

- **Scope of comparison:** Three viable record-management options. Direct edits to ADR-0004 are excluded because current governance prohibits them.
- **Assessment method:** Repository review of ADR-0004, its linked tasks, the CI Ledger, and captured lint reports.
- **Evidence boundary:** The Ledger records 34 distinct finding IDs across five remediation tasks. It does not establish that every suggested wording change is semantically safe.
- **Key assumptions:** The user wants the prose findings resolved while preserving the accepted decision.
- **Unresolved evidence gaps:** No wording patch exists. No successor ADR exists. Hosted validation for a future patch remains unknown.

## Considered Options

### Option 1 — Keep ADR-0004 unchanged and accept the lint debt

- **Description and operating model:** Keep the accepted file unchanged. The user may accept the findings as risk and close their tasks without prose remediation.
- **Repository and environment fit:** This follows the current immutability rule. It leaves the current CI findings in the accepted file.
- **Good — strengths:** It preserves the original record and requires no migration.
- **Neutral — trade-offs:** The task board and Ledger would need explicit accepted-risk records.
- **Bad — weaknesses:** The 34 editorial findings remain in the source. This does not meet the current P0 remediation objective.
- **Implementation and migration cost:** No source change is required. The Worker would record accepted risk and closeout evidence.
- **Dependencies and operational burden:** The user must accept the risk. The Worker must preserve each finding identity and its decision.
- **Risks and safeguards:** Future readers may mistake accepted lint debt for clean prose. Record the reason and exact finding IDs.
- **Evidence and confidence:** The current ADR and five task records establish the findings. Confidence is high for the recorded Ledger state.
- **Limitations and unknowns:** This option does not test whether editorial corrections preserve meaning.

### Option 2 — Add a separate editorial note

- **Description and operating model:** Create a companion note with proposed wording corrections. Leave ADR-0004 unchanged.
- **Repository and environment fit:** The workspace supports Markdown records and linked evidence. The note would not replace the accepted ADR.
- **Good — strengths:** The note can explain every proposed correction without changing the predecessor.
- **Neutral — trade-offs:** Readers must consult two files to understand the editorial history.
- **Bad — weaknesses:** The linter still scans ADR-0004. The original findings remain unresolved.
- **Implementation and migration cost:** Create one note and add navigation links. Do not change the accepted ADR.
- **Dependencies and operational burden:** The Worker must maintain the note and keep its links accurate.
- **Risks and safeguards:** Readers may treat the note as authoritative decision text. Label it as non-authoritative.
- **Evidence and confidence:** The repository already uses linked Draft and ADR records. Confidence is high for the navigation model.
- **Limitations and unknowns:** This option does not remediate findings in the accepted ADR.

### Option 3 — Create a superseding editorial successor

- **Description and operating model:** Prepare a new ADR that supersedes ADR-0004. Copy its complete decision and correct only approved editorial wording.
- **Repository and environment fit:** The ADR workflow supports permanent IDs, supersession links, and lifecycle history. The old file can remain immutable.
- **Good — strengths:** The successor can contain corrected prose while preserving the original decision and audit trail.
- **Neutral — trade-offs:** The repository gains one more ADR record and needs index updates.
- **Bad — weaknesses:** A careless rewrite could change requirements or rationale. The review must compare decision-bearing content line by line.
- **Implementation and migration cost:** After approval, create the successor ADR and update lifecycle metadata and links. Do not change implementation files.
- **Dependencies and operational burden:** The user must approve this Draft. The successor must pass the ADR completeness and read-back gates.
- **Risks and safeguards:** Semantic drift could change the accepted decision. Preserve all requirements and compare the successor with ADR-0004.
- **Evidence and confidence:** ADR-0004, its tasks, and Ledger records provide the source material. Confidence is high for scope and finding counts.
- **Limitations and unknowns:** Exact replacement wording remains subject to review. No patch or hosted validation exists.

## Comparative Assessment

| Criterion | Option 1: Keep unchanged | Option 2: Editorial note | Option 3: Successor ADR |
|---|---|---|---|
| Decision integrity | Strong. No source edit. | Strong. No source edit. | Strong if the review preserves meaning. |
| Governance compliance | Strong. | Strong. | Strong after Draft approval and ADR promotion. |
| CI remediation | Weak. Findings remain. | Weak. Findings remain. | Strong. The successor can remove the findings. |
| Confirmation integrity | Strong. No state change. | Strong. No state change. | Strong if every state remains unchanged. |
| Traceability | Strong. One record remains. | Moderate. Readers need two records. | Strong. The predecessor links to its successor. |
| Implementation cost | Low. | Low. | Moderate. Requires a new ADR and index updates. |
| Reviewability | Strong. No wording decision. | Moderate. The note is separate. | Strong. The user approves an exact successor scope. |

### Overall comparison

Option 1 best preserves simplicity but leaves the P0 findings unresolved. Option 2 records proposed wording but does not change the lint target. Option 3 requires more review and migration. It is the only option that can remediate the source while preserving the original file.

## Proposed Recommendation

Choose Option 3. Prepare a superseding ADR with editorial corrections only.

The successor must preserve Option 3 and the exact approved scope in ADR-0004. It must preserve every lifecycle rule, requirement, rationale, consequence, risk, safeguard, and Confirmation criterion. It must also preserve implementation status and task 20261126-232913.

The successor must preserve the current Confirmation state. Criteria 1–14 remain verified. Criterion 15 remains pending until hosted Ledger regression and Document Type Catalog results receive authorized review. Criterion 16 remains verified.

The Worker must keep ADR-0004 unchanged until the user approves this Draft and the successor reaches accepted status. The Worker must then mark the predecessor as superseded through lifecycle metadata. The predecessor file must remain available and immutable.

## Consequences and Trade-Offs

- **Positive:** The successor can provide lint-compliant prose and preserve the original decision history.
- **Negative:** The repository must maintain predecessor and successor links.
- **Neutral:** The task folder and CI Ledger design remain unchanged.
- **Conditional:** The P0 tasks can proceed only after the user approves this Draft and the successor ADR becomes accepted.

## Risks and Safeguards

| Risk | Likelihood / Impact | Evidence / rationale | Safeguard | Residual risk |
|---|---|---|---|---|
| Wording changes alter decision meaning | Medium / High | Editorial rewrites can change scope or obligations. | Compare every decision-bearing section against ADR-0004. | Low after independent read-back. |
| Successor omits a lifecycle rule | Medium / High | ADR-0004 contains detailed normative rules. | Use a completeness checklist and exact source comparison. | Low after checklist review. |
| Confirmation status changes without evidence | Medium / High | Criterion 15 remains pending. | Preserve every checkbox and its evidence. | Low. |
| Readers follow the predecessor | Medium / Medium | Both records remain in the repository. | Add reciprocal supersession links and index entries. | Low. |
| The proposal expands implementation scope | Low / High | The P0 tasks target prose only. | Restrict the successor to editorial corrections. | Low. |

## Repository Impact

| Area | Proposed change | Owner / exact files | Approval dependency |
|---|---|---|---|
| Decision record | Create a superseding ADR with editorial corrections only. | New file under `workspace/adr/` | This Draft and ADR acceptance |
| Predecessor metadata | Set status to superseded and link the successor. | `workspace/adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md` | Successor acceptance |
| ADR index | List the successor and preserve the predecessor link. | `workspace/adr/README.md` | Successor acceptance |
| P0 task links | Link the accepted successor ADR to the five remediation tasks. | Tasks 20261127-013151-30 through -34 | Successor acceptance |
| CI Ledger | Preserve finding IDs and evidence. Record resolution only after verified remediation. | `.takeout/reports/triage/ledger.json` | Fix commit and required validation |

## Proposed Implementation Outline

1. Obtain approval for this exact Draft revision and scope.
2. Assign the next unused ADR ID during promotion.
3. Create the successor from the complete ADR-0004 content.
4. Apply only the approved editorial corrections.
5. Compare every decision-bearing section and Confirmation criterion.
6. Read back the provisional ADR and verify all links.
7. Accept the successor only after the completeness gate passes.
8. Mark ADR-0004 as superseded through lifecycle metadata. Keep its file unchanged.
9. Update the ADR index and all five P0 task links.
10. Remediate the five task groups. Record commits and validation separately.
11. Do not claim hosted validation while criterion 15 remains pending.

Do not change task scripts, workflows, Ledger schemas, task templates, or implementation scope under this proposal.

## Questions for the User

1. Do you approve Option 3 and the creation of a superseding ADR with editorial corrections only?

## Review and Approval

- **Revision presented:** DRAFT-0007 revision 1
- **User decision:** Pending
- **Approved scope:** Not approved
- **Decision date:** Pending
- **Resulting ADR:** Not created

## Discussion and Revision History

| Date | Revision | Change | User feedback / decision |
|---|---|---|---|
| 2026-11-27 | 1 | Initial proposal based on the five ADR-0004 P0 task groups. | Pending |

## References and Evidence Register

| ID | Source / exact locator | Version, date, or commit | Evidence type | Supports which option / claim | Limitations |
|---|---|---|---|---|---|
| E1 | [Accepted ADR-0004](../adr/0004-task-folders-subtasks-and-reliable-ci-ledger-lifecycle.md) | Branch gpt, current file | Repository fact | Accepted outcome, scope, lifecycle rules, and Confirmation state | Does not authorize direct edits. |
| E2 | [Long-sentence task](../tasks/20261127-013151-30/task.md) | Current task record | Repository fact | 8 long-sentence findings | Lint flags require human review. |
| E3 | [Passive-voice task](../tasks/20261127-013151-31/task.md) | Current task record | Repository fact | 19 passive-voice findings | Lint flags require human review. |
| E4 | [Semicolon task](../tasks/20261127-013151-32/task.md) | Current task record | Repository fact | 1 semicolon finding | Lint flags require human review. |
| E5 | [Synonym-rotation task](../tasks/20261127-013151-33/task.md) | Current task record | Repository fact | 5 synonym-rotation findings | Lint flags require human review. |
| E6 | [Present-perfect task](../tasks/20261127-013151-34/task.md) | Current task record | Repository fact | 1 present-perfect finding | Lint flags require human review. |
| E7 | [STE Lint Changed run 45910973837](https://github.com/dungnv2602/chatgpt/actions/runs/45910973837) | 2026-11-26 | Hosted diagnostic | Initial finding evidence | Does not establish a future patch result. |
| E8 | [STE Lint Changed run 45911174533](https://github.com/dungnv2602/chatgpt/actions/runs/45911174533) | 2026-11-26 | Hosted diagnostic | Recurring finding evidence | Does not establish a future patch result. |
| E9 | [STE Lint Changed run 45911611855](https://github.com/dungnv2602/chatgpt/actions/runs/45911611855) | 2026-11-26 | Hosted diagnostic | Recurring finding evidence | Does not establish a future patch result. |
| E10 | [Decision Governance](../../.agent/skills/decision-governance/SKILL.md) | Branch gpt, current file | Repository policy | Draft approval and ADR immutability | Governs the process, not editorial correctness. |
