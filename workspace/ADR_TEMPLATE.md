---
record_type: decision-record
template_version: "1.1"
id: "ADR-0001"
status: "accepted"
decision_date: "YYYY-MM-DD"
decision_makers:
  - "User"
proposed_by: "Assistant"
consulted: []
informed: []
source_draft: "DRAFT-0001"
source_draft_revision: 1
approved_scope: "Exact scope approved by the user"
related_adrs: []
supersedes: []
superseded_by: null
implementation_status: "not-started"
implementation_tasks: []
review_triggers: []
---

<!-- Promotion transaction: create a provisional ADR with status promotion-pending. Do not list it as accepted or use it to govern a task. Change it to accepted only after the completeness checklist and provisional read-back pass. Read back the accepted record before deleting the source Draft. -->

# {Short title that describes the accepted decision}

## Context and Problem Statement

{Describe the problem, current state, scope, and why the decision is required. Preserve material rationale from the approved source Draft.}

## Decision Drivers

- {Constraint, user goal, quality attribute, risk, or operating requirement}

## Considered Options

- {Option 1}
- {Option 2}
- {Current approach or no-change option, when viable}

## Decision Outcome

Chosen option: "{Option}", because {explain how it best meets the decision drivers}.

### Consequences

- **Good:** {Positive effect}
- **Neutral:** {Material effect without a clear advantage}
- **Bad:** {Negative effect or accepted cost}

### Confirmation

Define how the repository will prove that this decision is implemented and remains effective.

- [ ] {Observable acceptance or fitness criterion}
- [ ] {Relevant test, review, workflow result, or operational evidence}

## Pros and Cons of the Options

### {Option 1}

- **Good:** {Benefit}
- **Neutral:** {Trade-off}
- **Bad:** {Cost or limitation}

### {Option 2}

- **Good:** {Benefit}
- **Neutral:** {Trade-off}
- **Bad:** {Cost or limitation}

## Implementation Scope

- **In scope:** {Approved implementation boundary}
- **Out of scope:** {Explicit exclusions}
- **Tasks:** {Links to implementation tasks. Each task must link back to this ADR.}
- **Dependencies:** {Accepted ADRs, prerequisites, or external dependencies}
- **Migration / rollback:** {Required transition and recovery approach, or Not applicable}

## More Information

- **Source Draft:** {Draft ID, exact revision, and provenance. Do not link to a source file that successful promotion deletes.}
- **Approved scope:** {Exact scope approved by the user.}
- **Related ADRs:** {Links and relationship}
- **Evidence:** {Repository paths, commits, tests, research, or external sources}
- **Review trigger:** {Condition that requires this decision to be reviewed}

## Decision Lifecycle History

| Date | Status / implementation change | Evidence and reason |
|---|---|---|
| YYYY-MM-DD | Accepted | User approved {Draft ID, exact revision, and scope}. |
