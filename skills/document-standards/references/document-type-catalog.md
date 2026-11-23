# Document Type Catalog

**Catalog version:** 1.0  
**Inventory status:** Initial inventory. Full file-by-file coverage is not complete.  
**Source branch:** `gpt`

This catalog maps recurring document types to their canonical formats. It distinguishes standalone templates from embedded contracts and generated formats.

Do not create a second template when an owning workflow already defines the required format.

## Classification

| Class | Meaning |
|---|---|
| Template required | Copy a canonical template when creating the record. |
| Schema required | Follow a defined field schema and validate its values. |
| Embedded contract | Follow the format defined by one canonical live file or owning skill. |
| Generator-owned | The generating script and its tests define the output format. |
| Lightweight pattern | Use a small consistent structure for a one-off or low-risk note. |
| Exempt | Do not force a template where creative freedom or an external format controls the content. |

## Initial inventory

| Document type | Class | Current canonical format | Inventory finding / next action |
|---|---|---|---|
| Novel foundation | Template required | `novels/templates/novel-v1.1.md` | Current Version 1.1 template exists. |
| Novel open-discussion register | Template required | `novels/templates/open-discussion-v1.1.md` | One active register per novel. The Novel-02 example uses an approved-decision register and topic-grouped questions; its relationship roadmap embeds proposal content, with no separate deferred or resolved sections. |
| Character profile | Template required when created | `novels/templates/character-profile-v1.1.md` | Optional record. No current example was found in the inspected project records `novels/Novel-01/novel.md` and `novels/Novel-02/novel.md`. Do not create when the novel summary is sufficient. |
| Development outline | Template required when created | `novels/templates/development-outline-v1.1.md` | Optional focused planning record. `novels/Novel-02/planning/relationship-progression.md` is a current Version 1.1, topic-specific outline whose section layout differs from the generic template; preserve it and use the template for new records or material revisions. |
| Story arc | Template required when created | `novels/templates/arc-v1.1.md` | Current Version 1.1 template exists. |
| Scene | Template required when created | `novels/templates/scene-v1.1.md` | Current Version 1.1 template exists. Scene prose remains creative content. |
| Illustration note | Template required | `novels/templates/illustration-note-v1.1.md` | One record per retained or reviewed novel illustration. Three Version 1.0 examples exist: `novels/Novel-01/Arc-01/Scene-002/illustrations/illustration-01.md`, `novels/Novel-01/Arc-01/Scene-002/illustrations/illustration-02.md`, and `novels/Novel-01/Arc-01/Scene-002/illustrations/illustration-03.md`. Preserve them as legacy records. |
| Illustration prompt record | Template required before generation | `novels/templates/illustration-prompt-v1.1.md` | Preserve chronological attempts and exact authored prompts. No standalone prompt record was found among the three Scene-002 illustration notes listed in the Illustration Note row. Repository handoff is conditional on an accepted output being uploaded. |
| Non-novel drawing attempt | Template required | `skills/drawing/assets/attempt-template.md` | Template version 1.1. Separates record, generation, and user-decision states. Includes required lineage, criteria, provenance, and per-output evidence. |
| Drawing pattern entry | Template required | `skills/drawing/references/patterns/PATTERN-TEMPLATES.md` | Template version 1.0. Separate copy-ready formats cover successful and failure patterns, evidence, and confidence rules. Current examples are in `skills/drawing/references/patterns/successful-patterns.md` and `skills/drawing/references/patterns/failure-patterns.md`. |
| Drawing session brief | Template required | `skills/session-archiving/assets/session-brief-template.md` | Template version 1.0. Status values are Active, Paused, and Closed. New sessions start Active. |
| Daily drawing index | Template required | `skills/drawing/assets/daily-index-template.md` | Template version 1.1. Defines the exact six-field table for attempt, session, lineage, execution, approval/evidence, and image. |
| Conversation integrity record | Template required | `skills/session-archiving/assets/conversation-integrity-template.md` | Copy-ready template now exists with gap and editorial-summary fields. The historical record `drawings/history/2026-11-12-conversation-integrity.md` predates the template and remains unchanged. |
| Session summary | Template required | `skills/session-archiving/assets/session-summary-template.md` | Copy-ready handoff template now exists. The historical record `drawings/history/2026-11-12-summary.md` predates the template and remains unchanged. |
| Workspace task record | Template required | `workspace/TASK_TEMPLATE.md` | Template version 1.1. The Worker owns task fields and closeout. The active record remains In Progress / Archived: No until the archive copy passes full read-back. |
| Task board | Embedded contract | `skills/the-worker/SKILL.md` and `workspace/task_board.md` | One live index. No separate copy template is needed now. |
| Condensed Mode discussion register | Embedded contract | `skills/conversation-mode/SKILL.md` and `workspace/discussion.md` | Fixed headings, ordering, and entry rules. |
| Image takeout hand-off | Schema required | `skills/session-archiving/scripts/process_takeout.py` and `images/takeout/README.md` | The processor validates the YAML contract. `skills/session-archiving/scripts/test_process_takeout_unittest.py` covers readiness, exact intake coverage, missing attempt metadata, malformed top-level data, duplicate output IDs, rollback, and hashes. |
| Drawing-session manifest | Generator-owned | `skills/session-archiving/scripts/process_takeout.py` (`MANIFEST_FIELDS`) and `skills/session-archiving/scripts/verify_published_manifest.py` | The processor defines columns, preserves existing columns, and adds missing fields. The publisher checks verification columns and published values. `skills/session-archiving/scripts/test_process_takeout_unittest.py` covers legacy rows, missing columns, duplicate IDs, hashes, and publication links. |
| Conversion report CSV | Generator-owned | `skills/session-archiving/scripts/process_takeout.py` (`FIELDS`) | The processor defines the output columns and writes one report row per input image. `skills/session-archiving/scripts/test_process_takeout_unittest.py` checks report creation and source, staging, and final paths. |
| Publication verification report | Generator-owned | `skills/session-archiving/scripts/process_takeout.py` (`write_reports`) and `skills/session-archiving/scripts/verify_published_manifest.py` | The report generator writes fixed sections for checks and errors. `skills/session-archiving/scripts/test_process_takeout_unittest.py` covers published asset, URL, README, and attempt-link outcomes. |
| Agent Skill definition | Template required | `skills/agent-skill-authoring/assets/SKILL_TEMPLATE.md` | Copy-ready `SKILL.md` template now exists. |
| Skill index and activation files | Embedded contract | `skills/README.md`, `skills/SESSION_START.md`, `skills/INITIALIZATION_POLICY.md` | Each has a distinct ownership role. Do not force one generic index template. |
| Master image, pose, and prompt catalogues | Lightweight pattern | `master/Images.md`, `master/Poses.md`, `master/Prompts.md` | These are living reference collections, not repeated individual records. Review consistency before defining a shared pattern. |
| Technical skill references | Lightweight pattern | `skills/asd-ste100/SKILL.md` and `skills/asd-ste100/references/repository-writing-policy.md`, plus the owning skill | Use type-specific headings. No universal section layout is appropriate. |
| Creative prose and approved creative prompts | Exempt | `novels/WORKFLOW.md` and `skills/drawing/SKILL.md` | Preserve creative form. Apply only required metadata and provenance rules. |

## Validation coverage limits

The processor validates the hand-off when it processes a ready batch. Its regression suite covers important success and failure paths. Field-level cases now check invalid asset IDs, generation hashes, internal IDs, native IDs, approval values, and mapping evidence. A drawing-session upload test also checks that provenance metadata reaches the generated manifest. Existing tests cover manifest backfill, custom-column preservation, published hashes, URLs, and attempt links.

The suite does not test every invalid value or every interaction between fields. Do not claim exhaustive schema coverage. The processor and its tests remain the schema authority. Do not create a second hand-off or manifest schema.

The processor and its tests remain the authority for the current YAML and CSV formats. A separate schema file is not required unless another consumer needs it or the processor adopts it.

## Existing versioned templates

The novel workspace has Version 1.1 templates for eight document types. It retains Version 1.0 templates for historical compatibility.

Do not mass-migrate untouched legacy novel records. Use the current template for new records and material revisions.

## Representative records reviewed

| Document type | Representative record or inspected scope | Finding | Handling |
|---|---|---|---|
| Novel open-discussion register | `novels/Novel-02/open-discussion.md` | The Version 1.1 register has an approved-decision table, topic-grouped questions, and a current-status summary. Its relationship roadmap embeds proposal content rather than duplicating it in a separate proposal section; no separate deferred or resolved sections are present. | Preserve the active record. The canonical template now allows embedded proposals and marks separate proposal, deferred, and resolved sections as conditional. |
| Development outline | `novels/Novel-02/planning/relationship-progression.md` | Current Version 1.1 focused outline. It separates the approved broad direction from proposed dramatic beats and open questions, but its section layout is specific to this relationship progression. | Preserve the active record. Use the canonical template for new outlines and material revisions. |
| Drawing pattern entries | `skills/drawing/references/patterns/successful-patterns.md`; `skills/drawing/references/patterns/failure-patterns.md` | Current examples use separate success and failure structures. They distinguish observed results, hypotheses, evidence, confidence, and limitations. | Keep the indexes. Use the matching copy-ready pattern in `PATTERN-TEMPLATES.md`. |
| Character profile | Inspected `novels/Novel-01/novel.md` and `novels/Novel-02/novel.md` | No current character-profile record was found. | Keep this type optional. Do not create a profile only to populate the catalog. |
| Novel illustration prompt record | `novels/Novel-01/Arc-01/Scene-002/scene.md`; the three illustration notes are listed in the Illustration Note row above | The inspected scene has no standalone prompt-record link or file in its illustration set. | Use the canonical prompt-record template before future novel illustration generation. |

## Legacy examples reviewed

The following records predate the current templates. Preserve them as historical records. Do not migrate them only to match a newer template.

| Document type | Representative records | Finding | Handling |
|---|---|---|---|
| Novel foundation, arc, and scene | `novels/Novel-01/novel.md`, `novels/Novel-01/Arc-01/arc.md`, `novels/Novel-01/Arc-01/Scene-001/scene.md` | These records declare format Version 1.0. The current templates use Version 1.1. | Keep untouched records at Version 1.0. Use Version 1.1 for new records and material revisions. |
| Non-novel drawing attempt | `drawings/2026-11-20/attempt-01.md`, `drawings/2026-11-21/attempt-17.md` | The older notes use earlier field layouts. Attempt 17 combines prompt-archive and generation-pending states in one status value. | Preserve existing notes. Use the Version 1.1 template with separate record, generation, and user-decision states for new records and material revisions. |
| Daily drawing index | `drawings/2026-11-20/README.md`, `drawings/2026-11-21/README.md` | These indexes predate the Version 1.1 six-field template. | Preserve existing indexes. Use the six-field template for new daily indexes and material revisions. |
| Drawing session brief | `drawings/2026-11-21/session-01-brief.md` | This brief predates the canonical template and records a closed session. | Preserve it. New briefs use the canonical status values Active, Paused, and Closed. |
| Novel illustration notes | `novels/Novel-01/Arc-01/Scene-002/illustrations/illustration-01.md`; `novels/Novel-01/Arc-01/Scene-002/illustrations/illustration-02.md`; `novels/Novel-01/Arc-01/Scene-002/illustrations/illustration-03.md` | All three records declare format Version 1.0 and predate the current Version 1.1 template. | Preserve the records. Use Version 1.1 for new notes and material revisions. |
| Session integrity and summary | `drawings/history/2026-11-12-conversation-integrity.md`; `drawings/history/2026-11-12-summary.md` | These historical records predate the standalone templates and use project-specific chronological and handoff structures. | Preserve them. Use the canonical templates for new records. |
| Workspace task record | `workspace/tasks/20261122-233900-enforce-template-first-document-standards.md` | This task record declares Template version 1.0. The current task template is Version 1.1. | Preserve the original task metadata. Use Version 1.1 for new task records. |
| Agent Skill definitions | Existing skill files under `skills/` | Many skills predate the reusable Agent Skill template. | Do not mass-convert existing skills. Use the canonical template for new skills and material rewrites. |

No new session summary or conversation-integrity record was required during this review. Their templates remain available for future sessions.

## Priority gaps

1. Obtain separate user approval before integrating the catalog validator and its tests into GitHub Actions; run both checks on a hosted runner after approval.
2. Review the three master catalogues for shared lightweight structure.
3. Check remaining project-specific record types and complete the repository inventory before marking the catalog complete.

## Catalog maintenance

When a recurring document type is added or changed:

1. Identify its owning skill or workflow.
2. Define its canonical template, schema, or embedded contract.
3. Add or update one catalog row.
4. Link the template from its owner index.
5. Define structural validation and migration rules.
6. Read back all changed paths.
7. Run `skills/document-standards/scripts/validate_catalog.py` and its tests through an authorized GitHub Actions workflow. This validator checks catalog integrity and exact references; it does not validate document content. Do not run it locally.
