---
record_type: decision-draft
template_version: "1.2"
id: "DRAFT-0006"
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
related_adrs: []
resulting_adr: null
promotion_cleanup_pending: false
cleanup_reason: null
---

# Make Session Start and Conversation Mode lean

## Proposal Summary

Adopt a single-source workflow architecture. The Worker owns initialization, operating procedures, task coordination, records, and execution. Session Start contains only the cue guard and a pointer to the Worker. Conversation Mode contains only conversation presentation settings.

Keep detailed domain procedures in their existing Worker-owned references and specialist skills. Make the initialization policy, skill index, document catalog, and task board point to their owners instead of repeating operational rules.

This Draft asks the user to approve this architecture for implementation. It does not authorize implementation before an accepted ADR exists.

## Context and Problem Statement

The current files split operational ownership across several places.

- .agent/SESSION_START.md defines the /start cue, a long initialization sequence, the startup CI P0 batch, queue draining, blocker handling, material cleanup, domain-skill loading, a verified-load ledger, and detailed Drawing and Novelist role initialization.
- .agent/skills/the-worker/SKILL.md already owns task capture, scheduling, queue execution, blocker handling, immediate temporary-material cleanup, closeout, document governance, decision governance, and Worker-owned domain procedures.
- .agent/skills/the-worker/references/conversation-mode.md defines Default and Condensed presentation modes. It also repeats material cleanup, blocker coordination, approvals, repository restrictions, discussion-register maintenance, and delivery rules that The Worker already owns.
- .agent/INITIALIZATION_POLICY.md repeats initialization, CI P0 startup, skill-loading, and operating rules.
- .agent/skills/README.md repeats skill activation tiers and points to Session Start for a verified-load ledger.
- The document-type catalog attributes the discussion-register contract to Conversation Mode.
- The task board's quiescence wording does not state the latest rule to collect all user decisions before executing newly unlocked work.

The conflicting instructions have already caused a concrete workflow gap. Session Start step 8 says to ask about only the first user-resolvable blocker and resume the queue after that answer. Its step 10 and the Worker require the Worker to collect all user-resolvable blocker decisions before executing work unlocked by those decisions. These instructions cannot both govern the same batch.

The recent rules for immediate temporary-material cleanup and collect-all-decisions-before-batch-execution are correct and already present in the Worker. Their copies in Session Start and Conversation Mode add no authority. The startup instructions and current ownership map must agree with the Worker.

## Goals and Non-Goals

### Goals

- Keep Session Start limited to the explicit /start cue guard and a pointer to The Worker.
- Keep Conversation Mode limited to conversation presentation settings.
- Make The Worker the sole owner of foundational initialization, task execution, collaboration, discussion-register maintenance, approvals, user-input coordination, and closeout.
- Keep detailed CI, decision-governance, archive, media, and document procedures in existing Worker-owned references.
- Keep drawing and novelist execution details in their specialist skills. The Worker owns cue routing and prerequisite order, not creative procedures.
- Preserve conditional initialization, progressive loading, the mandatory startup P0 batch, the decision-collection gate, immediate temporary-material cleanup, remote-only repository work, and hosted-CI review restrictions.
- Remove contradictory or duplicated live rules from the initialization policy, skill index, document catalog, and task-board contract.

### Non-Goals

- Do not change the /start cue or begin loading skills automatically.
- Do not remove the mandatory startup CI P0 batch or change its authorization.
- Do not change hosted CI review restrictions or introduce local tests, scripts, or lint.
- Do not rewrite Drawing or Romantic Storyteller creative procedures as part of this architecture decision.
- Do not create a new standalone initialization skill or duplicate Worker reference.
- Do not change task hierarchy, approval semantics, accepted ADRs, or user authority.
- Do not mass-migrate historical task, discussion, or archive records.

## Decision Drivers

| Criterion | Why it matters | Relative importance |
|---|---|---|
| One operational authority | Conflicting instructions already caused the wrong execution sequence. | High |
| Cue-controlled loading | The user requires initialization only after the explicit cue. | High |
| Preservation of behavior | Refactoring must not silently remove startup, cleanup, approval, or safety constraints. | High |
| Progressive disclosure | Detailed domain procedures should load only when the task activates them. | High |
| Low duplication | Future edits should have one authoritative rule location. | High |
| Clear ownership | Conversation settings, initialization cues, Worker operations, and specialist procedures have distinct owners. | High |
| Verifiable maintenance | Changed files and references must be easy to inspect and read back. | Medium |

## Assessment Basis and Evidence Limits

- **Scope of comparison:** Current distributed architecture, one-file Worker centralization, and a single-source Worker architecture with focused references and specialist ownership.
- **Assessment method:** Qualitative review of the current files and their cross-references on branch gpt.
- **Repository snapshot:** Branch head 1e522633bf86f8b3ac4dd3345d9bbab218062fff before this Draft and its task records were created.
- **Evidence boundary:** The review establishes current file contents and conflicts. It does not establish client-side skill-loader behavior or hosted CI results.
- **Key assumptions:** The Worker can remain the foundational operating authority. Existing Worker-owned references and specialist skills can keep detailed procedures without another activation layer.
- **Unresolved evidence gaps:** No local validator, tests, lint, or hosted CI results were reviewed. These are outside the allowed workflow unless the user separately authorizes CI review.

## Considered Options

### Option 1 — Keep the current distributed instructions

- **Description and operating model:** Keep Session Start as a long startup and role-initialization manual. Keep Conversation Mode as both presentation settings and collaboration policy. Keep Worker, Initialization Policy, Skills README, document catalog, and task board as parallel sources for overlapping rules.
- **Repository and environment fit:** This matches the current files and needs no migration. The existing startup flow can continue to load the Worker and Conversation Mode.
- **Good — strengths:** The startup sequence is visible in one file. Conversation Mode carries the discussion-register contract and user-interruption rules near its mode settings. Existing links need few changes.
- **Neutral — trade-offs:** Users and maintainers must consult several files to understand initialization and execution. The Worker must still reconcile those files.
- **Bad — weaknesses:** It preserves duplicated ownership and the explicit conflict between Session Start steps 8 and 10. Similar conflicts can recur when one copy changes without the others. Conversation Mode remains more than a settings file, and Session Start remains more than a cue pointer.
- **Implementation and migration cost:** No migration cost. Ongoing maintenance requires repeated edits and cross-file consistency reviews.
- **Dependencies and operational burden:** The assistant must remember which duplicate copy is current and compare multiple procedures during execution.
- **Risks and safeguards:** Contradictory instructions can cause premature execution, missed blockers, unnecessary loading, or incorrect startup behavior. A consistency checklist could catch some drift, but it would not remove duplicate authority.
- **Evidence and confidence:** The retrieved Session Start, Worker, Conversation Mode, Initialization Policy, and task board contain the overlapping rules described above. Confidence is high for the duplication and step 8/10 conflict.
- **Limitations and unknowns:** Keeping the files unchanged does not establish whether a conflict will recur. It does not satisfy the user's requested separation.

### Option 2 — Put every procedure in the Worker skill body

- **Description and operating model:** Move all operational instructions from Session Start and Conversation Mode into the Worker SKILL.md. Keep Session Start as a cue pointer and Conversation Mode as settings only. Move specialist-role procedures into the Worker as well.
- **Repository and environment fit:** The Worker already owns most cross-cutting operations. This option would make one file the home for general operations and detailed specialist procedures.
- **Good — strengths:** It gives the repository one obvious operational file. It removes the current Session Start and Conversation Mode overlap. It makes the startup sequence directly visible in the Worker.
- **Neutral — trade-offs:** The Worker becomes longer. The agent must load specialized details even when the task does not need them, unless the Worker also adds progressive references.
- **Bad — weaknesses:** Drawing, novelist, CI diagnostics, decision governance, and archive procedures would sit beside general scheduling and task rules. This mixes different domains and weakens progressive disclosure. It would duplicate specialist instructions that already have appropriate owners.
- **Implementation and migration cost:** Large Worker revision. Specialist content would need careful migration and link reconciliation. Existing Worker references and skill-specific procedures would become redundant or need another restructuring.
- **Dependencies and operational burden:** Every specialist workflow depends on the Worker body carrying its detailed procedure. The Worker becomes a broad manual that is harder to maintain.
- **Risks and safeguards:** Centralization can remove file-level duplication but create an oversized skill and repeat content owned by specialist skills. Keeping specialist procedures in existing domain skills would mitigate this risk, but then the design becomes Option 3.
- **Evidence and confidence:** The Worker already has extensive task and governance procedures. Drawing and Romantic Storyteller have specialist workflows. Confidence is high that wholesale transfer would create unnecessary duplication and loading.
- **Limitations and unknowns:** No measurement was made of loading latency or context cost. The concern is structural and follows the existing progressive-loading design.

### Option 3 — Make the Worker the sole operating authority and retain focused owners

- **Description and operating model:** The Worker owns all cross-cutting operating rules and initialization orchestration. Session Start contains only the cue guard and Worker pointer. Conversation Mode contains only Default and Condensed presentation settings. Existing Worker-owned references retain detailed CI, decision-governance, document, archive, and media procedures. Drawing and Romantic Storyteller retain specialist procedures. The Worker defines when each is loaded and in what order.
- **Repository and environment fit:** This matches the existing foundational skill design. The Worker is already the sole scheduler and operational entry point. Existing focused references and specialist skills already provide progressive disclosure.
- **Good — strengths:** It creates one authority for initialization, task coordination, user interruptions, approvals, the discussion register, recovery cleanup, and execution. The two entry files become small and stable. Detailed procedures stay with their existing owners. The existing all-calls-before-batch rule and cleanup rule remain in one operating authority.
- **Neutral — trade-offs:** The Worker must contain concise routing instructions and direct links to detailed procedures. Maintainers must update the Worker when a cue or dependency changes.
- **Bad — weaknesses:** The Worker remains a substantial skill. If its links or activation rules become stale, a specialist workflow may fail to load. The architecture still needs a clear boundary between general rules and specialist procedures.
- **Implementation and migration cost:** Moderate cross-file rewrite and readback. Reuse current Worker references and specialist skills. Update current ownership references in the Initialization Policy, Skills README, document catalog, and task-board contract. No new skill or reference is required.
- **Dependencies and operational burden:** The Worker needs a concise cue-to-skill map and a per-conversation verified-load ledger. Detailed procedures remain in current domain owners.
- **Risks and safeguards:** A missed dependency can prevent required loading. Maintain one cue map in the Worker, use a current-session verification ledger there, and check every changed link and owner reference after the commit.
- **Evidence and confidence:** The repository already has the Worker, focused Worker references, specialist skills, and a progressive-loading policy. The current duplication and direct conflict are visible in the reviewed files. Confidence is high that this option best meets the requested ownership boundaries.
- **Limitations and unknowns:** Remote readback can verify committed text and links by inspection. It does not prove client-specific automatic skill discovery or hosted validation.

## Comparative Assessment

| Criterion | Option 1 — Keep distributed | Option 2 — All in Worker body | Option 3 — Worker authority with focused owners |
|---|---|---|---|
| One operational authority | Weak — duplicate owners remain | Strong — one file | Strong — Worker owns policy and routes to owners |
| Lean Session Start | Weak — retains long procedure | Strong | Strong |
| Lean Conversation Mode | Weak — retains coordination rules | Strong | Strong |
| Progressive disclosure | Moderate — mixed loading | Weak — specialist content is centralized | Strong — existing focused references and skills remain |
| Behavior preservation | Moderate — conflict remains | Moderate — transfer risks omissions | Strong — explicit migration and reconciliation |
| Maintenance burden | Weak — multiple copies | Moderate — large central file | Strong — one policy owner, detailed content in appropriate owners |
| Risk of contradictory rules | Weak — observed conflict remains | Moderate — one file but specialist duplication risk | Strong — cross-cutting rules have one owner |

### Overall comparison

Option 1 avoids migration but keeps the known conflict. Option 2 removes duplicate entry files but moves specialist details into an unsuitable central file. Option 3 separates activation, operating policy, presentation settings, and specialist execution without creating new operational copies.

Option 2 could be preferable only if the Worker had no focused references or specialist skills. The repository already has those boundaries. Option 3 therefore provides the clearest ownership with less migration than a wholesale rewrite.

## Proposed Recommendation

Choose **Option 3 — Worker authority with focused owners**.

The user has already specified the intended boundaries for Session Start and Conversation Mode. Option 3 applies those boundaries and preserves progressive loading.

The Worker becomes the only operational authority for:

- The /start startup sequence and startup P0 batch.
- The per-conversation verified-load ledger and cue-to-skill routing.
- Task capture, scheduling, queue draining, closeout, and repository discipline.
- Discussion-register ownership and updates.
- User-input coordination, including sequential collection of all user-resolvable blocker decisions before batch execution.
- Approval and execution gates.
- Temporary-material recovery and immediate cleanup.
- Cross-cutting rules and loading of focused Worker references.

The Worker must point to, not reproduce, detailed procedures in existing Worker-owned references and specialist skills. The Drawing skill owns drawing execution. Romantic Storyteller owns novelist and scene execution. The Worker owns activation cues and dependency order.

The implementation should reduce the live files as follows:

1. **.agent/SESSION_START.md:** Keep only the conditional cue guard, the literal /start trigger, and a pointer to .agent/skills/the-worker/SKILL.md. It must not contain startup steps, queue rules, CI policy, cleanup, role procedures, or a loading ledger.
2. **.agent/skills/the-worker/references/conversation-mode.md:** Keep only Default and Condensed mode definitions and the presentation effect. State that mode does not alter operating rules or authority.
3. **.agent/skills/the-worker/SKILL.md:** Own initialization, cue routing, baseline loading, the verified-load ledger, discussion-register contract, startup P0 orchestration, task execution, blocker decisions, approval gates, cleanup, and closeout. Reconcile overlapping rules into one coherent procedure.
4. **Existing Worker references and specialist skills:** Keep detailed procedures in their current appropriate owners. The Worker links and activates them when required. Do not duplicate those procedures in its general workflow.
5. **.agent/INITIALIZATION_POLICY.md:** Keep a concise source-of-truth map and copyable user instruction only. It must not restate procedures.
6. **.agent/skills/README.md:** Keep the skill catalogue and concise activation pointers. Point to the Worker's loading policy. Describe Conversation Mode as settings only.
7. **Document-type catalog:** Correct the ownership of Session Start, Conversation Mode, and the discussion register.
8. **workspace/task_board.md:** Keep only a short pointer to the Worker's scheduler and decision-collection contract. Do not restate the queue algorithm.
9. **workspace/discussion.md and its template:** Keep the register as task/session data. The Worker owns its operational contract. The template defines only record headings and entry shape.

The migration must preserve these controls:

- Do not initialize without the literal /start instruction.
- Do not load unrelated skills. Reuse verified reads within the current conversation.
- Complete the mandatory startup CI P0 batch before accepting the substantive prompt. Send the required notice. Do not inspect hosted CI results.
- Continue independent eligible tasks past isolated blockers.
- At quiescence, present all user-resolvable blockers one at a time. Record each answer without executing the work it unlocks. After all calls are collected, reconcile and execute one batch.
- Delete temporary recovered materials immediately after their final use. Preserve canonical files, user originals, required evidence, and governed-retention materials.
- Keep approval distinct from execution cues.
- Do not run local scripts, tests, or lint. Do not review hosted CI without an explicit user request.

## Consequences and Trade-Offs

- **Positive:** The two entry files become small and stable. The Worker becomes the clear authority for the operating sequence. Existing focused references retain progressive disclosure.
- **Negative:** The Worker requires a coordinated update and clear cue routing. Its core procedure remains substantial.
- **Neutral:** The Skills README, Initialization Policy, document catalog, and task board still contain navigation or ownership metadata. They link to the Worker without duplicating its rules.
- **Conditional:** If a future Worker procedure becomes too large for its core skill body, it may move to a focused Worker-owned reference. The Worker remains its sole activation and policy owner.

## Risks and Safeguards

| Risk | Likelihood / Impact | Evidence / rationale | Safeguard | Residual risk |
|---|---|---|---|---|
| A moved rule is omitted | Medium / High | Session Start currently contains many unique startup and specialist-routing steps | Map each behavior to its destination before editing. Read back all migrated rules. | Manual review can miss an obscure dependency |
| Duplicate rules remain in secondary indexes | Medium / Medium | Initialization Policy and Skills README repeat activation rules | Change them to pointer/index content. Audit the catalog and board. | A future edit can introduce new duplication |
| Startup order changes unintentionally | Medium / High | Startup P0 processing precedes substantive prompt handling | Preserve the notice, CI reference loading, P0 batch, decision calls, and readiness gate in the Worker | Client-specific cue behavior remains untested |
| Specialist workflows lose prerequisites | Medium / High | Drawing and novelist initialization have dependency order | Keep detailed domain procedures in specialist skills. Put only cue routing and dependency order in the Worker. | External skill-loader behavior is not established |
| Worker becomes too long | Medium / Medium | The Worker already owns multiple cross-cutting procedures | Reuse focused references and move detailed domain procedures to their existing owners | Future growth may require another bounded reference |
| Board or catalog contradicts the Worker | Medium / Medium | Both publish workflow metadata | Update their short contracts and read back every changed path | Future maintenance can cause drift |

## Repository Impact

| Area | Proposed change | Owner / exact files | Approval dependency |
|---|---|---|---|
| Session cue | Reduce to cue guard and Worker pointer | .agent/SESSION_START.md | This Draft and accepted ADR |
| Conversation settings | Remove operational coordination; retain modes only | .agent/skills/the-worker/references/conversation-mode.md | This Draft and accepted ADR |
| Core operations | Reconcile initialization, loading, register, P0, queue, decisions, approvals, cleanup, and closeout | .agent/skills/the-worker/SKILL.md | This Draft and accepted ADR |
| Initialization map | Remove copied active procedures | .agent/INITIALIZATION_POLICY.md | This Draft and accepted ADR |
| Skills navigation | Remove redundant loading procedure | .agent/skills/README.md | This Draft and accepted ADR |
| Document ownership | Correct catalog descriptions and canonical owners | .agent/skills/the-worker/references/document-type-catalog.md | This Draft and accepted ADR |
| Scheduler publication | Point to the Worker decision-collection rule | workspace/task_board.md | This Draft and accepted ADR |
| Discussion register | Keep record format; move operational ownership to Worker | workspace/discussion.md, .agent/skills/the-worker/assets/DISCUSSION_TEMPLATE.md | This Draft and accepted ADR |
| Specialist routing | Preserve details in existing skill owners | .agent/skills/drawing/SKILL.md, .agent/skills/romantic-storyteller-visual-artist/SKILL.md | This Draft and accepted ADR if changes are needed |

## Proposed Implementation Outline

1. Obtain approval of this exact Draft revision and scope.
2. Promote it to the next available ADR after completing the decision-governance completeness and readback gates. The next unused ADR number appears to be ADR-0005.
3. Create a separate implementation child linked to the accepted ADR. Do not use this Draft-preparation child as implementation authorization.
4. Create a behavior-to-destination matrix from the current Session Start and Conversation Mode contents. Include each unique instruction, its current duplicate, and its new owner.
5. Rewrite the Worker as the sole operational policy and initialization owner. Consolidate the startup sequence and ensure the collect-all-decisions-before-batch gate is the only user-decision procedure.
6. Reduce Session Start and Conversation Mode to their specified minimal contracts.
7. Convert Initialization Policy and Skills README into source maps and indexes. Correct the document catalog and task-board cross-references.
8. Check every path link and every moved behavior by remote readback. Check that no live copy of a moved operational rule remains in Session Start or Conversation Mode.
9. Record all changed paths and commit evidence in the implementation task. Do not run local tests, scripts, or lint. Do not inspect hosted CI unless the user explicitly requests it.
10. Confirm the final ownership map and preserved behavior against this Draft and the accepted ADR.

Rollback: Restore the previous file contents from Git history if readback exposes an omitted rule or broken dependency. Do not leave a partial migration that mixes old and new owners.

## Questions for the User

1. Approve DRAFT-0006 Revision 1 and its exact Option 3 scope for ADR promotion and implementation?

## Review and Approval

- **Revision presented:** 1
- **User decision:** Pending
- **Approved scope:** Not approved
- **Decision date:** Pending
- **Resulting ADR:** Not created

## Discussion and Revision History

| Date | Revision | Change | User feedback / decision |
|---|---|---|---|
| 2026-11-28 | 1 | Initial proposal based on the current branch audit | Pending |

## References and Evidence Register

| ID | Source / exact locator | Version, date, or commit | Evidence type | Supports which option / claim | Limitations |
|---|---|---|---|---|---|
| E1 | .agent/SESSION_START.md | Blob 5ad2010aad87d4de92b5b013c5fdc76245b00faf; branch snapshot 1e522633bf86f8b3ac4dd3345d9bbab218062fff | Repository fact | Startup and specialist procedures plus conflicting blocker instructions | Text inspection only |
| E2 | .agent/skills/the-worker/SKILL.md | Blob 9b88f2fcdcc8d5257b7d373cb48dcdcda58331c2; same snapshot | Repository fact | Existing Worker ownership and new batch-decision gate | Text inspection only |
| E3 | .agent/skills/the-worker/references/conversation-mode.md | Blob 3d5c6ebcf59166310d4f9d660041dc4e6fa4463d; same snapshot | Repository fact | Mode settings mixed with operational procedures | Text inspection only |
| E4 | .agent/INITIALIZATION_POLICY.md | Blob 1e678fafcb38621117b9cf62fb58a978ce0392c6; same snapshot | Repository fact | Repeated active initialization policy | Text inspection only |
| E5 | .agent/skills/README.md | Blob 3776d89cdc9d0604aa7286d863e62328c4d5ba0c; same snapshot | Repository fact | Repeated skill-loading hierarchy and stale load-ledger owner | Text inspection only |
| E6 | .agent/skills/the-worker/references/document-type-catalog.md | Blob 738be6392c845f484cf4892902bf120bf7921f00; same snapshot | Repository fact | Current Conversation Mode and discussion-register ownership | Text inspection only |
| E7 | workspace/task_board.md | Blob 3a1767aa90983fed92ef7d61bd35e02a88be6dc3; same snapshot | Repository fact | Scheduler contract does not state latest call-collection gate | Text inspection only |
| E8 | .agent/skills/the-worker/references/decision-governance.md | Blob f390c5f6c2b39c87a22b34c1a36a39ca2dc3e146; same snapshot | Repository policy | Draft approval and accepted ADR gate before implementation | Relevant procedure read |
| E9 | .agent/skills/the-worker/assets/DRAFT_TEMPLATE.md | Blob d3f1ac7b59a13f6da43c1c52d141145c0ce4ccad; same snapshot | Repository template | Required Draft structure and option assessment | Full template read |
