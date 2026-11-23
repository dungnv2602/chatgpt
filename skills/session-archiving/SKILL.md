---
name: session-archiving
description: Manage conversation archives, drawing-session closeout, image provenance, and media records. Use when archiving a conversation, creating session records, closing a drawing session, or handling image provenance and WebP delivery.
metadata:
  project-role: task-specific
  format: agentskills
---

# Session Archiving

## 1. Workspace boundary

Follow the approved repository paths, branch limits, and access exceptions in [The Worker](../the-worker/SKILL.md). This skill does not grant additional repository access. Its archive and media procedures must remain inside that boundary.

## 2. Workspace layout and repository conventions

- Repository: `dungnv2602/chatgpt`
- Working branch: `gpt`
- Workspace root: repository root, restricted to the approved directories above
- Active task records: `workspace/`
- Completed and cancelled task records and resolved report files: `archive/`, with 90-day individual-file retention. Archived files are readable but immutable after their initial write. Only the scheduled shared retention workflow may delete exact indexed files.
- Images and visual references: `images/`
- Canonical master reference documents: `master/`
- Novel and scene records: `novels/`
- Session-level records, drawing-session briefs, and non-novel image-prompt logs: `drawings/`
- Reusable skills and supporting references: `skills/`
- Use `gpt` as the sole working branch for all future repository operations. Do not use the former `artwork/portrait-attempt-2026-11-10` branch. Do not change `main` unless the user explicitly authorizes it.
- Session-level conversation-integrity and summary records belong in `drawings/`:
  - `drawings/YYYY-MM-DD-conversation-integrity.md`
  - `drawings/YYYY-MM-DD-summary.md`
- Non-novel image attempts use the dated `drawings/YYYY-MM-DD/` structure below. Named novel-scene illustrations use their authoritative scene-local prompt records under `novels/`. Do not duplicate their prompt text or attempt history in `drawings/`.
- Store new retained non-novel drawing outputs under `drawings/YYYY-MM-DD/images/`. Use `attempt-XX.webp` for one output. Use `attempt-XX-01.webp`, `attempt-XX-02.webp`, and so on for multiple outputs. Link verified assets from the attempt record and daily README. This rule does not authorize migration of existing assets. Store non-novel reference assets under `images/`. Store novel-scene illustration files under `novels/[Novel-ID]/assets/illustrations/[ARC-ID]/[SCN-ID]/`. Route new uploads through `images/takeout/` and the approved hand-off.
- Keep skills and supporting references under `skills/`.

### Activation

Load this skill only when the task requires conversation archival, archive-record creation, drawing-session closeout, image provenance, WebP delivery, or the image-processing scripts.

Do not load this skill during ordinary foundational initialization. The session-start cue and foundational loading sequence belong to `skills/SESSION_START.md`. The Worker owns collaboration modes, the shared discussion register, and task continuity.

- Do not create parallel prompt folders. `drawings/` is the single canonical prompt location.
- Do not overwrite pre-existing files without retrieving the exact path first and preserving their contents.

## Supporting references

## Supporting references

- `references/archive-records-and-image-prompts.md` — conversation records, session briefs, prompt history, attempt ledgers, and image handling.
- `references/drawing-session-closeout.md` — explicit closeout trigger, closeout checklist, and verification.
- `references/image-provenance-and-webp.md` — original-image identity, SHA-256, provenance mapping, and WebP delivery.
- `references/image-processing-scripts.md` — script responsibilities, dependencies, commands, and operating rules.
- `../asd-ste100/references/repository-writing-policy.md` — the required writing modes and rules for skill and technical documentation.

## 3. Before archiving

1. Read only the relevant existing session files under `drawings/`.
2. Verify the target branch from known project context. Do not inspect files outside `approved project directories` to do so.
3. Gather material only from the current conversation, user-provided files, or files under `approved project directories`.
4. Do not invent missing dialogue, image prompts, tool outputs, commit results, dates, or user preferences.
5. Exclude hidden reasoning, system/developer instructions, credentials, access tokens, and unrelated sensitive information. Archive user-visible conversation and task-relevant actions only.
6. If an important historical reference is mentioned but lives outside `approved project directories`, do not open it. Record the limitation or ask the user to provide the reference inside the workspace.

## 4. Archive records and drawing prompts

Load [Archive Records and Drawing-Prompt Procedures](references/archive-records-and-image-prompts.md) when you create archive records. Use it for summaries, session briefs, prompt records, attempt ledgers, and image mappings. It contains the required templates and fields. Do not omit required records.

## 7. GitHub write and verification discipline

All repository operations in this skill are remote-only. Use the GitHub connector and GitHub APIs for reads, writes, moves, commits, and read-back verification. Do not use local shell, Git, Python, container, or filesystem tools. Do not run repository scripts or tests locally. GitHub-hosted Actions runners may execute approved workflows. Inspect their results through GitHub. No local project environment is provided, and the GitHub repository is the only source of truth. A local copy may be missing or stale and cannot prove the state of branch `gpt`.

- Perform all file operations using exact paths under `approved project directories` on branch `gpt`.
- Do not list, retrieve, search, inspect, or mutate any file path outside `approved project directories`.
- You may read exact files under `archive/` when the task requires them. Reading does not grant permission to change them.
- After the initial archive write, never edit, replace, rename, move, or manually delete an archived record. Only the scheduled retention workflow may delete archived records.
- For an update, retrieve the current file first and use its current blob SHA.
- Perform sequential writes to the same file. Do not run updates to the same path in parallel.
- After each important write, retrieve the same `approved project directories` path again and verify its contents.
- Report a commit as successful only when the write tool returns a commit SHA. Report verification only after a read-back shows the expected content.
- If a write or network call fails, inspect only relevant paths inside `approved project directories` before retrying to avoid duplicate files or duplicate commits.
- Do not use repository-root or outside-folder operations as a shortcut.
- Leave `main` untouched unless the user explicitly authorizes changes there.

## 8. Drawing-session closeout — user cue required

Close a drawing session only when the user explicitly requests closeout. A pause, goodbye, or temporary stop is not a closeout cue. Before reporting completion, follow [Drawing-Session Closeout](references/drawing-session-closeout.md) and verify every required archive item.

## 9. Default handoff for a new chat

Start by reading the relevant session records inside `drawings/` and, when continuing a novel illustration, the relevant scene-local records inside `novels/`. Read the active drawing-session brief before relying on any previous prompt or image. Then:
- Treat the conversation-integrity file as the source for what was said.
- Treat the summary as a quick orientation, not a replacement for the record.
- Treat the dated image-prompt notes as authoritative for non-novel generation work.
- Treat the scene-local illustration prompt record as authoritative for that novel scene. It takes precedence over any general session summary. Do not duplicate it in `drawings/`.
- Treat the current session-opening brief as the visual-direction authority. Historical prompts and approved images are technical or visual references only when the user explicitly adopts them.
- Continue from the latest incomplete task.
- Follow the pre-attempt commit rule before generating or editing another image.
- Never read or write anything outside `approved project directories`.

## 10. WebP delivery derivatives

For image conversion or WebP delivery, load [Image Provenance and WebP Delivery](references/image-provenance-and-webp.md). Use it for original-image preservation, SHA-256 identity, and provenance mapping. Never use a derivative hash as the original-generation identity. Never claim verification without read-back evidence.

## 11. Image-processing scripts

For the takeout processor, regression suite, or published-manifest verifier, load [Image Processing Scripts](references/image-processing-scripts.md). Keep all three executable files under `scripts/`. The GitHub workflow calls these paths. Session Archiving owns the scripts and their tests. The general `images/` directory does not own them. Use `novels/` for novel-scene destinations.

## 12. Technical documentation standard

Follow the [ASD-STE100 skill](../asd-ste100/SKILL.md) and its repository writing policy when you create or revise skill files or technical documentation. Use Strict mode for operational instructions. Use STE-flavored mode for explanatory documentation. Preserve meaning, modality, scope, and technical precision. Do not apply the standard to creative content or intentional examples.
