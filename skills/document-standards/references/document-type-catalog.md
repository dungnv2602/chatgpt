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
| Novel open-discussion register | Template required | `novels/templates/open-discussion-v1.1.md` | One active register per novel. |
| Character profile | Template required when created | `novels/templates/character-profile-v1.1.md` | Optional record. Do not create when the novel summary is sufficient. |
| Development outline | Template required when created | `novels/templates/development-outline-v1.1.md` | Optional focused planning record. |
| Story arc | Template required when created | `novels/templates/arc-v1.1.md` | Current Version 1.1 template exists. |
| Scene | Template required when created | `novels/templates/scene-v1.1.md` | Current Version 1.1 template exists. Scene prose remains creative content. |
| Illustration note | Template required | `novels/templates/illustration-note-v1.1.md` | One record per retained or reviewed novel illustration. |
| Illustration prompt record | Template required before generation | `novels/templates/illustration-prompt-v1.1.md` | Preserve chronological attempts and exact authored prompts. |
| Non-novel drawing attempt | Template required | `skills/drawing/assets/attempt-template.md` | Template version 1.0. Keep the compact six-section record structure. |
| Drawing pattern entry | Template required | `skills/drawing/references/patterns/PATTERN-TEMPLATES.md` | Template version 1.0. Separate copy-ready formats cover successful and failure patterns, evidence, and confidence rules. |
| Drawing session brief | Template required | `skills/session-archiving/assets/session-brief-template.md` | Copy-ready template now exists. |
| Daily drawing index | Template required | `skills/drawing/assets/daily-index-template.md` | Copy-ready index template now exists. The workflow still enforces the single-table contract. |
| Conversation integrity record | Template required | `skills/session-archiving/assets/conversation-integrity-template.md` | Copy-ready template now exists with gap and editorial-summary fields. |
| Session summary | Template required | `skills/session-archiving/assets/session-summary-template.md` | Copy-ready handoff template now exists. |
| Workspace task record | Template required | `workspace/TASK_TEMPLATE.md` | Template version 1.0. The Worker owns task fields and closeout. |
| Task board | Embedded contract | `skills/the-worker/SKILL.md` and `workspace/task_board.md` | One live index. No separate copy template is needed now. |
| Condensed Mode discussion register | Embedded contract | `skills/conversation-mode/SKILL.md` and `workspace/discussion.md` | Fixed headings, ordering, and entry rules. |
| Image takeout hand-off | Schema required | `skills/session-archiving/scripts/process_takeout.py` and `images/takeout/README.md` | The processor parses and validates version, status, batch ID, items, sources, paths, attempt values, IDs, hashes, approval values, and mapping evidence. The README documents the fields. Do not duplicate its rules in an unused schema file. |
| Drawing-session manifest | Generator-owned | `skills/session-archiving/scripts/process_takeout.py` (`MANIFEST_FIELDS`) and `skills/session-archiving/scripts/verify_published_manifest.py` | The processor defines required columns, preserves existing columns, and adds missing fields. The publisher checks required verification columns and published values. |
| Conversion report CSV | Generator-owned | `skills/session-archiving/scripts/process_takeout.py` (`FIELDS`) | The processor defines the output columns and writes one report row per input image. |
| Publication verification report | Generator-owned | `skills/session-archiving/scripts/process_takeout.py` (`write_reports`) and `skills/session-archiving/scripts/verify_published_manifest.py` | The report generator writes fixed sections for checks and errors. The verifier updates manifest statuses and errors. |
| Agent Skill definition | Template required | `skills/agent-skill-authoring/assets/SKILL_TEMPLATE.md` | Copy-ready `SKILL.md` template now exists. |
| Skill index and activation files | Embedded contract | `skills/README.md`, `skills/SESSION_START.md`, `skills/INITIALIZATION_POLICY.md` | Each has a distinct ownership role. Do not force one generic index template. |
| Master image, pose, and prompt catalogues | Lightweight pattern | `master/Images.md`, `master/Poses.md`, `master/Prompts.md` | These are living reference collections, not repeated individual records. Review consistency before defining a shared pattern. |
| Technical skill references | Lightweight pattern | Owning skill and repository writing policy | Use type-specific headings. No universal section layout is appropriate. |
| Creative prose and approved creative prompts | Exempt | Owning creative workflow | Preserve creative form. Apply only required metadata and provenance rules. |

## Existing versioned templates

The novel workspace has Version 1.1 templates for eight document types. It retains Version 1.0 templates for historical compatibility.

Do not mass-migrate untouched legacy novel records. Use the current template for new records and material revisions.

## Priority gaps

1. Review whether existing processor validation and tests cover all documented hand-off fields and failure modes.
2. Review the three master catalogues for shared lightweight structure.
3. Check remaining project-specific record types against this catalog before declaring inventory complete.
4. Complete the repository inventory before marking the catalog complete.

## Catalog maintenance

When a recurring document type is added or changed:

1. Identify its owning skill or workflow.
2. Define its canonical template, schema, or embedded contract.
3. Add or update one catalog row.
4. Link the template from its owner index.
5. Define structural validation and migration rules.
6. Read back all changed paths.
