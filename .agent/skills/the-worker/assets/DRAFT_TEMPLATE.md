---
record_type: decision-draft
template_version: "1.2"
id: "DRAFT-0001"
revision: 1
status: "in-review"
created: "YYYY-MM-DD"
updated: "YYYY-MM-DD"
proposed_by: "Assistant"
decision_makers:
  - "User"
consulted: []
informed: []
related_drafts: []
related_adrs: []
resulting_adr: null
promotion_cleanup_pending: false
cleanup_reason: null
---

# {Short title that describes the proposed decision}

## Proposal Summary

{State the decision requested and the recommended direction in a few sentences. Identify the exact choice the user is being asked to make.}

## Context and Problem Statement

{Describe the current state, the problem, why it matters, and the scope of the decision. Link exact repository evidence. Distinguish observed conditions from interpretation.}

## Goals and Non-Goals

### Goals

- {Required result}

### Non-Goals

- {Explicitly excluded work}

## Decision Drivers

{List the criteria that materially determine whether an option is suitable. Make them specific enough to compare options consistently. Include user requirements, repository constraints, quality attributes, risk, operating environment, cost, and lifecycle needs as relevant.}

| Criterion | Why it matters | Relative importance |
|---|---|---|
| {Criterion} | {Decision relevance} | {High / Medium / Low, with rationale} |

## Assessment Basis and Evidence Limits

{Explain how the options were identified and assessed. State the repository branch/commit or external source snapshot when relevant. Identify assumptions, evidence gaps, evaluation method, and any limits on comparability.}

- **Scope of comparison:** {Options and variants included; explain any excluded alternatives.}
- **Assessment method:** {Qualitative comparison, measured test, cost model, prototype, or other method.}
- **Evidence boundary:** {What the available evidence can and cannot establish.}
- **Key assumptions:** {Assumptions that could change the result.}
- **Unresolved evidence gaps:** {Missing tests, unavailable measurements, or unknowns.}

## Considered Options

Assess every materially viable option, including the current approach or no-change option when it is viable. Include materially different variants of an option when their trade-offs differ (for example, templates-only versus full automation). Do not omit an option merely because it is not recommended.

Use the same assessment dimensions for every option. Repeat the Option structure below for all options; add or remove option sections as needed. If only one option is genuinely viable, explain why alternatives are infeasible and state why a comparative matrix is not applicable.

For each option, provide specific, decision-relevant detail. Do not use generic claims such as "easy", "flexible", "scalable", or "more secure" without explaining the mechanism and consequence. Mark unsupported details as unknown rather than inventing them.

### Option 1 — {Name}

- **Description and operating model:** {What it is, how it works, and any materially distinct variants.}
- **Repository and environment fit:** {Compatibility with actual architecture, tools, workflows, policies, and constraints.}
- **Good — strengths:** {Concrete benefits and the mechanism producing each benefit.}
- **Neutral — trade-offs:** {Material effects with no clear net advantage, conditional benefits, and compromises.}
- **Bad — weaknesses:** {Concrete limitations, failure modes, and disadvantages.}
- **Implementation and migration cost:** {Files/systems affected, complexity, effort drivers, migration, and rollback needs. Do not invent numeric estimates.}
- **Dependencies and operational burden:** {Required tools, permissions, integrations, skills, ownership, support, and ongoing maintenance.}
- **Risks and safeguards:** {Important risks, likelihood/impact where supportable, mitigations, and residual exposure.}
- **Evidence and confidence:** {Repository facts, external claims, tests, benchmarks, prototypes, or observed behavior that support this assessment. Explain confidence and why.}
- **Limitations and unknowns:** {What has not been tested, what evidence does not prove, source/host/version constraints, and unresolved questions.}

### Option 2 — {Name}

- **Description and operating model:** {What it is, how it works, and any materially distinct variants.}
- **Repository and environment fit:** {Compatibility with actual architecture, tools, workflows, policies, and constraints.}
- **Good — strengths:** {Concrete benefits and the mechanism producing each benefit.}
- **Neutral — trade-offs:** {Material effects with no clear net advantage, conditional benefits, and compromises.}
- **Bad — weaknesses:** {Concrete limitations, failure modes, and disadvantages.}
- **Implementation and migration cost:** {Files/systems affected, complexity, effort drivers, migration, and rollback needs. Do not invent numeric estimates.}
- **Dependencies and operational burden:** {Required tools, permissions, integrations, skills, ownership, support, and ongoing maintenance.}
- **Risks and safeguards:** {Important risks, likelihood/impact where supportable, mitigations, and residual exposure.}
- **Evidence and confidence:** {Repository facts, external claims, tests, benchmarks, prototypes, or observed behavior that support this assessment. Explain confidence and why.}
- **Limitations and unknowns:** {What has not been tested, what evidence does not prove, source/host/version constraints, and unresolved questions.}

{Repeat the complete Option structure for every additional viable option.}

## Comparative Assessment

Compare the viable options against the same decision drivers. The matrix is a concise synthesis, not a replacement for the detailed option assessments.

| Criterion | Option 1 | Option 2 | Option 3 | Option 4 |
|---|---|---|---|---|
| {Decision driver} | {Assessment and evidence pointer} | {Assessment and evidence pointer} | {Assessment and evidence pointer} | {Assessment and evidence pointer} |

{Use consistent qualitative terms such as Strong / Moderate / Partial / Weak, with a short explanation or evidence pointer. Use quantitative scores only when a defensible measurement method and comparable data exist. Mark Not applicable with a reason. Add columns for further options. If only one viable option exists, explain why this comparison is not applicable.}

### Overall comparison

{Explain the decisive differences, trade-offs, and conditions under which a non-recommended option could be preferable. Do not calculate an unsupported aggregate score or imply false precision.}

## Proposed Recommendation

{State the recommended option and why it best meets the decision drivers. Explicitly compare it with the strongest alternative(s), explain the decisive trade-offs, identify assumptions on which the recommendation depends, and state what evidence could change the recommendation. This is a proposal, not an accepted decision.}

## Consequences and Trade-Offs

- **Positive:** {Expected benefits and who receives them.}
- **Negative:** {Expected costs, constraints, and obligations.}
- **Neutral:** {Material effects without a clear direction.}
- **Conditional:** {Benefits or costs that depend on assumptions, scale, or future capabilities.}

## Risks and Safeguards

| Risk | Likelihood / Impact | Evidence / rationale | Safeguard | Residual risk |
|---|---|---|---|---|
| {Risk} | {Assessment or Unknown} | {Why this rating is justified} | {Control} | {Remaining exposure} |

## Repository Impact

| Area | Proposed change | Owner / exact files | Approval dependency |
|---|---|---|---|
| {Workflow, skill, template, script, data, or archive} | {Change} | {Exact paths} | {This Draft or another decision} |

## Proposed Implementation Outline

{Identify the likely ADR, implementation tasks, dependencies, migration sequence, validation, rollback, and confirmation criteria. Do not create implementation tasks as authorization to implement this proposal.}

## Questions for the User

1. {Specific decision or unresolved trade-off. Ask only questions that require user judgment.}

## Review and Approval

- **Revision presented:** {Revision or commit}
- **User decision:** Pending / Approved / Changes requested / Rejected / Withdrawn
- **Approved scope:** {Exact scope, or Not approved}
- **Decision date:** {Date or Pending}
- **Resulting ADR:** {ADR ID and link, or Not created}

## Discussion and Revision History

| Date | Revision | Change | User feedback / decision |
|---|---|---|---|
| YYYY-MM-DD | 1 | Initial proposal | Pending |

## References and Evidence Register

| ID | Source / exact locator | Version, date, or commit | Evidence type | Supports which option / claim | Limitations |
|---|---|---|---|---|---|
| E1 | {URL, repository path, commit, page, section, or test result} | {Version/date/SHA} | {Repository fact / External claim / Test / Benchmark / Inference / Hypothesis} | {Specific claim} | {Scope, host, sample, freshness, or other caveat} |

{Preserve exact source URLs and repository locators. For benchmarks, report the evaluated version, host, task/sample size, protocol, measured outcome, and untested scenarios when available. Do not transfer results across hosts or versions without justification. Separate source claims from your own inference.}

<!--
Draft lifecycle:
- Allowed statuses: draft, in-review, changes-requested, approved-for-adr, rejected, withdrawn, superseded.
- Do not use promoted as a Draft status.
- On successful promotion, delete this source file after the accepted ADR passes the completeness and read-back checks.
- If deletion fails after acceptance, keep this file temporarily. Set resulting_adr, promotion_cleanup_pending, and cleanup_reason. Add it to Promotion Cleanup Pending, not Current Drafts.
- Do not create an `.archive/draft/` folder or a Promoted Drafts index.
-->
