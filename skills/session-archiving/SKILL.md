---
name: session-archiving
description: Preserve conversation integrity, manage project archives and image provenance, and verify session records and closeout. Use when archiving conversations, handling project session records, maintaining image-generation provenance, or closing a drawing session.
metadata:
  project-role: foundational
  format: agentskills
---

# Session Archiving

## 1. Absolute workspace boundary

**Standing default:** All repository file work must stay inside these approved project directories at the repository root: `images/`, `master/`, `novel/`, `prompts/`, and `skills/`. Do not read, list, search, fetch, create, update, move, rename, or delete files outside those directories, except for the specifically authorized workflow exception below.

**Authorized WebP workflow exception:** The user authorized creation of exactly `.github/workflows/convert-images-to-webp.yml` on 12 November 2026 and explicitly approved its takeout-pipeline modification and persistent WebP staging extension on 20 November 2026. This authorization covers the current approved extension only; it does not authorize unrelated outside paths or any later workflow changes. Obtain fresh, explicit permission before future modifications.

This boundary applies to every future task and every tool call, not only archiving.

- The only permitted workspace roots are:
  - `images/` — images and visual references
  - `master/` — canonical master reference documents
  - `novel/` — structured narrative records
  - `prompts/` — session records and prompt history
  - `skills/` — reusable skills and supporting references
- Read and write files only by exact paths beginning with one of those approved directory names.
- Do not recreate the obsolete `ChatGPT/` wrapper or consult former paths from the previous repository layout.
- Do not use repository-wide code search or recursive root-tree listings. Use exact paths and narrowly scoped directory listings within approved project directories.
- Do not follow Markdown links outside the approved directories. If an essential reference is outside them and is not supplied in the current conversation, explain the limitation and ask the user to place it in the appropriate approved directory or provide it in chat.
- A request to use an outside reference does not silently change this boundary. Obtain explicit permission before accessing an outside repository path.
- Repository and branch identifiers may be used to direct GitHub operations, but this does not authorize reading or writing files outside the approved directories.

**If a task cannot be completed without accessing something outside the approved project directories, stop and explain the limitation rather than crossing the boundary.**

## 2. Workspace layout and repository conventions

- Repository: `dungnv2602/chatgpt`
- Working branch: `gpt`
- Workspace root: repository root, restricted to the approved directories above
- Images and visual references: `images/`
- Canonical master reference documents: `master/`
- Novel and scene records: `novel/`
- Session-level records, drawing-session briefs, and non-novel image-prompt logs: `prompts/`
- Reusable skills and supporting references: `skills/`
- Use `gpt` as the sole working branch for all future repository operations. Do not use the former `artwork/portrait-attempt-2026-11-10` branch. Do not modify `main` unless the user explicitly authorizes it.
- Session-level conversation-integrity and summary records belong in `prompts/`:
  - `prompts/YYYY-MM-DD-conversation-integrity.md`
  - `prompts/YYYY-MM-DD-summary.md`
- Non-novel image attempts use the dated `prompts/YYYY-MM-DD/` structure below. Named novel-scene illustrations use their authoritative scene-local prompt records under `novel/`; do not duplicate their prompt text or attempt history in `prompts/`.
- Store new retained non-novel generated drawing outputs under `drawings/YYYY-MM-DD/images/` as `attempt-XX.webp` (multiple outputs: `attempt-XX-01.webp`, etc.), linked from their attempt record and daily README when provenance is verified. This does not authorize migration of existing assets. Store non-novel reference/source assets under `images/`; store novel-scene illustration binaries under `novels/[Novel-ID]/assets/illustrations/[ARC-ID]/[SCN-ID]/`. New user uploads intended for those permanent destinations first enter `images/takeout/` and are routed by the approved hand-off.
- Keep skills and supporting references under `skills/`.

### Conversation behavior

During explicit foundational initialization, after retrieving and reading this foundational Session Archiving skill, retrieve and read the [Conversation Mode skill](../conversation-mode/SKILL.md) from the same `gpt` branch before continuing with project work. Apply its Default Mode / Condensed Mode selection, persistence, and response rules throughout the conversation. This skill governs archiving; the Conversation Mode skill governs collaboration. The two skills are complementary.

### Foundational skill loading cadence

Load the Session Archiving, Conversation Mode, Agent Skill Authoring, Drawing, and required Drawing reference files only when the user invokes `Follow instructions` or `Be the novelist`, as defined in `skills/SESSION_START.md`. Load each required foundational file once during that conversation's foundational initialization and apply the verified instructions for the remainder of that conversation. Do not load these files automatically at the beginning of a new chat. Refresh a foundational file when the user explicitly asks, a relevant repository change is known or reasonably suspected, or an unresolved instruction requires checking the authoritative file. A new ChatGPT conversation/session starts a new loading cycle. This cadence does not remove the requirement to load a task-specific skill when needed or to read relevant project records before performing that task.

### First-response execution rule

The first assistant response after the user invokes an explicit foundational initialization cue must be an informational startup notice, not a request for the user's goal, confirmation, or additional permission. Immediately after that notice, execute the required retrievals below. Do not ask the user to repeat or explain the activation cue. Do not claim a check is underway unless its retrieval is actually being performed.

The startup gate is a prerequisite check, not the session archive itself. Do not create or update dated archive records merely because a new conversation has started. Once the required skills and references have been retrieved and read successfully, report verification and then address the user's request. If a retrieval fails, stop project work and identify the exact missing path.

### Mandatory session-start execution gate

Whenever the user invokes **`Follow instructions`** or **`Be the novelist`**, complete this sequence as the foundational prerequisite before doing the requested project work, creative writing, visual planning, image prompting, or specialist initialization:

1. **Notify the user first.** State that the explicitly requested foundational checks are beginning and project work will wait until they are complete. This is informational, not a request for approval.
2. Retrieve and read this Session Archiving skill from the `gpt` branch.
3. Retrieve and read `skills/conversation-mode/SKILL.md` from the same branch.
4. Retrieve and read `skills/agent-skill-authoring/SKILL.md` from the same branch.
5. Retrieve and read `skills/drawing/SKILL.md` from the same branch.
6. Retrieve and read every supporting reference explicitly named by the Drawing skill, currently `skills/drawing/references/style-guide.md` and `skills/drawing/references/image-editing-protocol.md`.
7. Verify every required retrieval succeeded and that the contents were actually read. Keep the verified instructions in working context for the remainder of the conversation.
8. Only after all checks pass, report completion and proceed. If any required retrieval fails or cannot be verified, stop project work, identify the exact missing item, and ask how the user wants to proceed.

**No task-type exception after activation:** Once the user invokes foundational initialization, the Drawing skill and its required references are mandatory even when the first task appears prose-only or unrelated to drawing. A task-specific prose-only exception does not cancel this requirement. This rule does not authorize automatic loading before an explicit cue.

**No premature-work exception after activation:** Once the user invokes a foundational initialization cue, do not begin the requested project task while required checks are pending. Do not substitute memory, a previous-session load, a Library copy, or a claim of readiness for fresh GitHub retrievals in the current conversation.

**Notification and disconnection limitation:** Deliver the startup notice in the active conversation before retrieval begins. Do not promise to continue checks after a voice call ends or claim an independent callback/notification will occur. Complete and report the checks in the active conversation.

This gate does not guarantee future execution; compliance must be established by actual retrievals and read-back evidence in each new conversation.
- Do not create parallel prompt folders. `prompts/` is the single canonical prompt location.
- Do not overwrite pre-existing files without fetching the exact path first and preserving their contents.

## Supporting references

- `references/archive-records-and-image-prompts.md` — conversation records, session briefs, prompt history, attempt ledgers, and image handling.
- `references/drawing-session-closeout.md` — explicit closeout trigger, closeout checklist, and verification.
- `references/image-provenance-and-webp.md` — original-image identity, SHA-256, provenance mapping, and WebP delivery.

## Supporting references

- `references/archive-records-and-image-prompts.md` — conversation records, session briefs, prompt history, attempt ledgers, and image handling.
- `references/drawing-session-closeout.md` — explicit closeout trigger, closeout checklist, and verification.
- `references/image-provenance-and-webp.md` — original-image identity, SHA-256, provenance mapping, and WebP delivery.

## 3. Before archiving

1. Read only the relevant existing session files under `prompts/`.
2. Confirm the target branch from known project context. Do not inspect files outside `approved project directories` to do so.
3. Gather material only from the current conversation, user-provided files, or files under `approved project directories`.
4. Do not invent missing dialogue, image prompts, tool outputs, commit results, dates, or user preferences.
5. Exclude hidden reasoning, system/developer instructions, credentials, access tokens, and unrelated sensitive information. Archive user-visible conversation and task-relevant actions only.
6. If an important historical reference is mentioned but lives outside `approved project directories`, do not open it. Record the limitation or ask the user to provide the reference inside the workspace.

## 4. Archive records and drawing prompts

When creating conversation-integrity records, summaries, drawing-session briefs, prompt records, attempt ledgers, or image mappings, load [Archive Records and Drawing-Prompt Procedures](references/archive-records-and-image-prompts.md). That reference contains the complete templates, required fields, and detailed procedures. Do not improvise or omit required records.

## 7. GitHub write and verification discipline

- Perform all file operations using exact paths under `approved project directories` on branch `gpt`.
- Do not list, fetch, search, inspect, or mutate any file path outside `approved project directories`.
- For an update, fetch the current file first and use its current blob SHA.
- Perform sequential writes to the same file. Do not run updates to the same path in parallel.
- After each important write, fetch the same `approved project directories` path again and verify its contents.
- Report a commit as successful only when the write tool returns a commit SHA. Report verification only after a read-back confirms the expected content.
- If a write or network call fails, inspect only relevant paths inside `approved project directories` before retrying to avoid duplicate files or duplicate commits.
- Do not use repository-root or outside-folder operations as a shortcut.
- Leave `main` untouched unless the user explicitly authorizes changes there.

## 8. Drawing-session closeout — user cue required

Close a drawing session only when the user explicitly requests closeout. A pause, goodbye, or temporary stop is not a closeout cue. Before reporting completion, follow [Drawing-Session Closeout](references/drawing-session-closeout.md) and verify every required archive item.

## 9. Default handoff for a new chat

Start by reading the relevant session records inside `prompts/` and, when continuing a novel illustration, the relevant scene-local records inside `novel/`. Read the active drawing-session brief before relying on any previous prompt or image. Then:
- Treat the conversation-integrity file as the source for what was said.
- Treat the summary as a quick orientation, not a replacement for the record.
- Treat the dated image-prompt notes as authoritative for non-novel generation work.
- Treat the scene-local illustration prompt record as authoritative for that novel scene; it takes precedence over any general session summary and is not duplicated in `prompts/`.
- Treat the current session-opening brief as the visual-direction authority. Historical prompts and approved images are technical or visual references only when the user explicitly adopts them.
- Continue from the latest incomplete task.
- Follow the pre-attempt commit rule before generating or editing another image.
- Never read or write anything outside `approved project directories`.

## 10. WebP delivery derivatives

For image conversion, original-image preservation, SHA-256 identity, provenance mapping, or WebP delivery, load [Image Provenance and WebP Delivery](references/image-provenance-and-webp.md). Never substitute a derivative hash for the original-generation identity or claim verification without read-back evidence.
