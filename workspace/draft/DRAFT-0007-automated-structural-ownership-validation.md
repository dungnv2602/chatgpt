---
record_type: decision-draft
template_version: "1.2"
id: "DRAFT-0007"
revision: 1
status: "in-review"
created: "2026-11-28"
updated: "2026-11-28"
proposed_by: "Assistant"
decision_makers:
  - "User"
consulted: []
informed: []
related_drafts: []
related_adrs:
  - "ADR-0005"
resulting_adr: null
promotion_cleanup_pending: false
cleanup_reason: null
---

# Automated Structural Validation for Canonical Ownership and Drift

## Proposal Summary

Add a lightweight repository validator that checks defined structural invariants for the canonical instruction-ownership architecture established by ADR-0005. The validator would detect structural drift and stale references without duplicating operational policy or attempting to decide instruction semantics. Option 2 is recommended: focused structural validation integrated into an existing repository validation workflow, with no implementation until this Draft is approved and an ADR is accepted.

## Context and Problem Statement

ADR-0005 and The Worker establish one canonical operating authority and entry/reference ownership boundaries. The Worker already requires a pre-action self-check, conflict/drift gate, single-owner invariant, and reconciliation of associated templates and indexes. Those controls are procedural. They depend on the worker following them during repository work.

A repeatable structural check could detect a subset of violations independently, especially path/reference integrity and observable structural boundaries. It must not become a second authority or reproduce the Worker as executable policy.

Evidence basis: current branch `gpt), repository readback on 2026-11-28 of The Worker, ADR-0005, Session Start, Conversation Mode, document-type catalog, task templates, and board contract. No validator prototype, tests, or hosted CI inspection were performed.

## Goals and Non-Goals

### Goals
- Enforce a limited, explicit set of observable ownership invariants.
- Detect invalid entry-file structure, required owner/reference absence, stale links, and designated duplicate structural markers where reliably detectable.
- Produce actionable diagnostics with file and rule identifiers.
- Keep rule definitions and operating policy owned by The Worker/ADR, not copied into validator prose.
- Use repository-side validation with maintainable, bounded scope.

### Non-Goals
- Interpret semantic meaning or decide whether every instruction is correctly placed.
- Replace the Worker's mandatory self-check or conflict-resolution process.
- Automatically edit or reconcile files.
- Validate arbitrary Markdown prose for semantic duplication.
- Inspect hosted CI results as part of this proposal.

## Decision Drivers

| Criterion | Why it matters | Importance |
|---|---|---|
| Canonical ownership | Avoid introducing a parallel policy authority. | High |
| Detection value | Detect practical, observable drift early. | High |
| False positives | Avoid treating harmless text as policy violations. | High |
| Maintainability | Keep checks small and tied to stable structures. | High |
| Integration fit | Use existing repository workflow and validation conventions. | Medium |
| Coverage and limits | Keep detection limits explicit and preserve manual review. | High |
| Rollback | Changes should be easy to remove or disable. | Medium |

## Assessment Basis and Evidence Limits

- **Scope:** Three options: manual-only controls, focused structural validation, or comprehensive semantic policy engine.
- **Method:** Qualitative analysis of current repository structure and existing ADR-0005 ownership contract. No prototypes, measurements, or tests.
- **Evidence boundary:** Repository readback establishes the current ownership model and designated files. It does not establish the effectiveness of any proposed validator, the available workflow integration point, or a measured false-positive rate.
- **Assumptions:** Structural invariants can be specified in testable form; the repository has an appropriate validation entry point or can accommodate one after implementation research.
- **Unknowns:** Actual integration location, runtime constraints, maintainers' desired diagnostic format, and detection accuracy remain untested. These should be investigated during implementation under the accepted ADR.

## Considered Options

### Option 1 — Keep procedural controls only

- **Description and operating model:** Continue relying on The Worker self-check, drift gate, and remote readback. No validator is added.
- **Repository/environment fit:** Fits the current architecture and avoids added tooling.
- **Good — strengths:** No new runtime, workflow, maintenance, or rule configuration. The Worker retains full context to evaluate semantic conflicts and exceptions.
- **Neutral — trade-offs:** Detection remains tied to the operating process and task-specific readback; no independent automated structural signal.
- **Bad — weaknesses:** A missed check or inconsistent manual readback can leave observable structural drift undetected.
- **Implementation and migration cost:** None beyond current procedures.
- **Dependencies and operational burden:** Depends on continued adherence to Worker gates and verification.
- **Risks and safeguards:** Risk of missed structural regressions; existing mandatory self-check and readback remain safeguards.
- **Evidence and confidence:** Repository fact: current controls are procedural. Confidence high in that observation; effectiveness is not measured.
- **Limitations and unknowns:** Frequency and impact of missed drift are unknown. No incident rate or benchmark supports quantification.

### Option 2 — Lightweight structural validator (recommended)

- **Description and operating model:** Add a small validator for explicit structural invariants, such as required files/pointers, restricted entry-file boundaries, expected reference paths, and link/path integrity. Rules should be encoded as focused checks, not copied operating instructions. Diagnostics should identify the failed check and path. It would run in an existing validation workflow or a minimal appropriate integration identified during implementation.
- **Repository/environment fit:** The architecture has designated owner files, pointer-only entry contracts, and references. These are observable structures suitable for bounded checks, subject to implementation research.
- **Good — strengths:** Independent, repeatable detection of a defined subset of drift; actionable diagnostics; avoids semantic policy duplication by testing structure rather than rephrasing rules.
- **Neutral — trade-offs:** Only detects explicitly modeled conditions; manual Worker review remains necessary.
- **Bad — weaknesses:** Fragile pattern checks may false-positive or miss changes; path and link checks cannot establish policy correctness.
- **Implementation and migration cost:** Moderate but bounded; identify integration point, encode rules, add test fixtures for expected pass/fail cases, document coverage and limitations.
- **Dependencies and operational burden:** Requires a supported runtime, workflow integration, ownership of validator code and fixtures, and maintenance as canonical paths/contracts change.
- **Risks and safeguards:** False positives, false negatives, and rule drift. Safeguard with stable structural checks, fixture tests, version-controlled diagnostics, and an explicit rule-to-owner mapping; avoid duplicated policy text.
- **Evidence and confidence:** Repository facts show structural contracts and named files. Confidence moderate in feasibility, but no prototype or workflow integration has been examined.
- **Limitations and unknowns:** No performance, false-positive, or coverage data. This proposal does not guarantee detection of semantic duplication or conflicting instructions.

### Option 3 — Comprehensive semantic policy engine

- **Description and operating model:** Develop a broad configurable rule engine attempting to classify instruction text, infer ownership, identify semantic duplication/conflict, and evaluate policy relationships.
- **Repository/environment fit:** Could cover broader text patterns, but would operate on natural-language documents and the current architecture does not establish a reliable semantic schema for all rules.
- **Good — strengths:** Potentially wider automated coverage if rules and classification become reliable and maintainable.
- **Neutral — trade-offs:** More configuration, interpretation, and review; still requires human decisions for ambiguous meaning.
- **Bad — weaknesses:** Greater complexity, risk of false positives and false negatives, possible policy duplication, and difficulty proving semantic completeness.
- **Implementation and migration cost:** High and not established; likely requires rule language, classifier or parser strategy, broad fixtures, maintenance and integration work. No estimates are supported.
- **Dependencies and operational burden:** Potentially extra runtime/dependencies and sustained rule-engine maintenance. Exact requirements are unknown.
- **Risks and safeguards:** Overconfidence in automated interpretation, authority duplication, and costly upkeep. Would need strict rule ownership, explainable diagnostics, and human review.
- **Evidence and confidence:** Hypothesis that broader semantic checks could add coverage. No repository prototype or independent evidence supports achievable accuracy.
- **Limitations and unknowns:** Feasibility, accuracy, cost, and reliability are unknown.

## Comparative Assessment

| Criterion | Option 1: Manual | Option 2: Structural | Option 3: Semantic engine |
|---|---|---|---|
| Canonical ownership | Strong (no new system) | Strong if checks map to owner contracts | Weak/Moderate risk of parallel authority |
| Detection value | Limited to process | Moderate, for modeled invariants | Potentially broad, unproven |
| False-positive risk | Low automated noise | Manageable with fixtures and narrow rules | Unknown, potentially higher |
| Maintainability | Minimal additional burden | Bounded and focused | High/unknown |
| Integration fit | Existing process | Likely, subject to workflow research | Not established |
| Coverage transparency | Manual judgment | Explicit scope and limits | Harder to establish |
| Rollback | Not applicable | Straightforward if isolated | More complex |

### Overall comparison

Option 1 is least costly but adds no independent detection. Option 3 may offer broader analysis, but its complexity and accuracy are unestablished and could create a second policy authority. Option 2 best balances independent structural checks with bounded scope and canonical ownership. Option 1 remains reasonable if implementation research shows there are too few stable invariants to justify automation. Option 3 would only become preferable with demonstrated accuracy and a clear, non-duplicative rule ownership model.

## Proposed Recommendation

Recommend Option 2, a lightweight structural validator. Limit it to deterministic checks of designated file boundaries, expected pointers/paths, and structural reference integrity. The validator should report findings rather than repair files, and its check definitions should be mapped to canonical owners. The Worker remains authoritative for interpretation, task orchestration, conflict resolution, and remediation.

The recommendation depends on implementation research finding a suitable integration point and testable invariants. If that is not confirmed, reconsider the scope rather than expanding into semantic analysis.

## Consequences and Trade-Offs

- **Positive:** Adds an independent, repeatable check for selected structural drift.
- **Negative:** Adds code, fixtures, integration, and maintenance.
- **Neutral:** Does not replace Worker review or change canonical policy.
- **Conditional:** Benefit depends on reliable checks and workflow execution.

## Risks and Safeguards

| Risk | Likelihood / Impact | Evidence / rationale | Safeguard | Residual risk |
|---|---|---|---|---|
| Structural check falsely flags a valid change | Unknown / Medium | No prototype or fixtures yet | Narrow checks and pass/fail fixtures; diagnostics explain each check | Some noise may persist |
| Validator misses semantic drift | High / Medium | Structural-only scope | Preserve Worker conflict gate and review | Manual detection remains required |
| Validator becomes second policy owner | Medium / High | Rules can duplicate prose | Map checks to canonical owner; test structures, not restate instructions | Contract changes may require reconciliation |
| Integration is unsuitable | Unknown / Medium | Integration point not yet investigated | Research existing validation entry point before coding | Scope may be reduced or withdrawn |
| Checks become stale | Medium / Medium | Paths/contracts can change | Associated-template/owner review and reference integrity checks | Maintenance remains necessary |

## Repository Impact

| Area | Proposed change | Owner / exact files | Approval dependency |
|---|---|---|---|
| Validator | Add focused structural checks and diagnostics | Proposed location to be determined after workflow/source review | Draft and accepted ADR |
| Tests | Add validator fixture tests | Proposed alongside validator | Draft and accepted ADR |
| Workflow | Integrate at an appropriate repository validation point | Existing workflow to be identified | Draft and accepted ADR |
| Canonical ownership | Keep validator rule mapping linked to The Worker/ADR-0005 | The Worker and relevant owner references, only if needed | Draft and accepted ADR |
| Documentation | Brief validation scope/limitations | Validator or owning reference | Draft and accepted ADR |

## Proposed Implementation Outline

1. Inspect current validation workflow and repository runtime constraints.
2. Select stable structural invariants directly traceable to canonical owners.
3. Implement focused checks and fixture tests; diagnostics include path and check identifier.
4. Integrate into the appropriate validation workflow without inspecting hosted results.
5. Reconcile any affected templates/indexes only where the contract changes.
6. Verify via repository readback and permitted checks; preserve explicit limits.
7. Confirmation criteria: validator exists, tests cover checks and invalid cases, integration invokes it, diagnostics are actionable, checks map to canonical owners, and no operating policy is duplicated.

## Questions for the User

- Approve or reject Option 2 and the scope described above. Implementation is not authorized until the resulting ADR is accepted.

## Revision History

- Revision 1 (2026-11-28): Initial proposal, evidence-qualified comparison, recommended Option 2.
