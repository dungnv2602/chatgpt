---
name: maya-and-me-session-archiving
description: Archive Maya_and_Me conversations and image-generation work strictly inside the ChatGPT workspace, using a three-file session record, chronological prompt history, pre-attempt commits, and verified GitHub writes.
created: 2026-11-18T13:18
updated: 2026-11-18T13:18
---

# Maya & Me Session Archiving

## 1. Absolute workspace boundary

**Standing default:** All repository file work must stay inside the explicitly approved project directories at the repository root: `images/`, `master/`, `novel/`, `prompts/`, and `skills/`. Do not read, list, search, fetch, create, update, move, rename, or delete files outside those directories, except for the specifically authorized workflow exception below.

**One-time authorized WebP workflow exception (12 November 2026):** The user explicitly authorized creation of exactly `.github/workflows/convert-images-to-webp.yml` outside the approved project directories for this specific task. This is a one-time exception for that exact file only. It does not authorize changes to other paths outside repository root, nor future edits to the workflow file. Obtain fresh, explicit permission before any later change to that outside-workspace file.

This is a strict standing instruction from the user. It applies to every future task and every tool call, not only archiving.

- The only permitted workspace roots are:
  - `images/`
  - `prompts/`
  - `skills/`
- Read and write files only by exact paths beginning with one of the approved directory names above.
- Do not browse or search the repository root, parent directories, `Archive/`, or any other path outside `ChatGPT/`.
- Do not use repository-wide code search, recursive root-tree listings, or directory listings outside `ChatGPT/`.
- The root-level `images/`, `master/`, `novel/`, `prompts/`, and `skills/` directories are the current canonical locations. Do not recreate the obsolete `ChatGPT/` wrapper.
- Do not follow Markdown links that resolve outside `ChatGPT/`. If an essential reference is not inside an approved project directory or supplied directly in the current conversation, explain that it is unavailable under the current boundary and ask the user to place it in the appropriate approved directory or provide it in chat.
- A user's request to use an outside reference does not itself silently change this boundary. Obtain an explicit instruction that changes the boundary before accessing an outside repository path.
- Repository and branch identifiers may be used to direct GitHub operations, but this does not authorize reading or writing repository files outside `ChatGPT/`.

**If a task cannot be completed without accessing something outside `ChatGPT/`, stop and explain the limitation rather than crossing the boundary.**

## 2. Workspace layout and repository conventions

- Repository: `dungnv2602/chatgpt`
- Working branch: `gpt`
- Workspace root: repository root (approved directories only)
- Images and visual references: `ChatGPT/images/`
- Session records and individual image prompts: `ChatGPT/prompts/`
- Reusable skills: `ChatGPT/skills/`
- Use `chatgpt` as the sole working branch for all future repository operations. Do not read or write through the former `artwork/portrait-attempt-2026-11-10` branch; do not modify `main` unless the user explicitly authorizes it.
- New session records belong in `ChatGPT/prompts/`:
  - `ChatGPT/prompts/YYYY-MM-DD-conversation-integrity.md`
  - `ChatGPT/prompts/YYYY-MM-DD-summary.md`
  - `ChatGPT/prompts/YYYY-MM-DD-image-prompts.md`
- Store all new visual assets explicitly destined for the repository under `ChatGPT/images/`. Do not use an outside image directory.
- Keep this skill and any future skills under `ChatGPT/skills/`.

### Conversation behavior

After loading this foundational session-archiving skill at the start of a Maya_and_Me conversation, retrieve and read the [Conversation Mode skill](../conversation-mode/SKILL.md) from the same `chatgpt` branch before continuing with project work. Apply its Default Mode / Condensed Mode selection, persistence, and response rules throughout the conversation. This skill governs conversation archiving; the Conversation Mode skill governs how the assistant collaborates with the user. The two skills are complementary and neither replaces the other.

### Foundational skill loading cadence

Load the Session Archiving skill and the Conversation Mode skill once at the beginning of each new Maya_and_Me ChatGPT conversation/session. Track that both have been loaded and continue applying their instructions for the remainder of that session; do not fetch or reread them merely because the user changes tasks, roles, topics, or moves between voice and text. Reuse the already-loaded instructions. Refresh a foundational skill only when the user explicitly asks, a relevant repository change is known or reasonably suspected, or an unresolved instruction requires checking the authoritative file. A new ChatGPT conversation/session starts a new loading cycle. This cadence does not remove the requirement to load a task-specific skill when a new task requires one, nor to read relevant project records before performing that task.

### First-response execution rule

The first assistant response in a new Maya_and_Me conversation must be an informational startup notice, not a request for the user's goal, confirmation, or permission. Immediately after that notice, execute the five required retrievals in the gate below. Do not ask the user to repeat, explain, or activate the project workflow. Do not claim that a check is underway unless the corresponding retrieval is actually being performed.

The startup gate is a prerequisite check, not the session archive itself. Do not create or update dated archive records merely because a new conversation has started. Once the required skills and references have been retrieved and read successfully, report that verification and then address the user's actual request. If a retrieval fails, stop project work and identify the exact missing path.

### Mandatory session-start execution gate

At the beginning of **every new Maya_and_Me ChatGPT conversation/session**, complete this sequence before doing any project work, creative writing, visual planning, image prompting, or repository task:

1. **Notify the user first.** State that the mandatory startup checks are beginning and that project work will wait until they are complete. This is an informational notice, not a request for approval.
2. Retrieve and read this Session Archiving skill from the `gpt` branch.
3. Retrieve and read `ChatGPT/skills/conversation-mode/SKILL.md` from the same branch.
4. Retrieve and read `ChatGPT/skills/drawing/SKILL.md` from the same branch.
5. Retrieve and read every supporting reference explicitly named by the Drawing skill, currently `ChatGPT/skills/drawing/references/style-guide.md` and `ChatGPT/skills/drawing/references/image-editing-protocol.md`.
6. Verify that every required retrieval succeeded and that the contents were actually read. Keep the verified instructions in working context for the remainder of the conversation.
7. Only after all checks pass, report completion and proceed to the user's request. If any required retrieval fails or cannot be verified, stop project work, identify the exact missing item, and ask how the user wants to proceed.

**No conditional exception:** The Drawing skill and its required references are mandatory at session start even when the first task appears to be prose-only or unrelated to drawing. The Romantic Storyteller skill's prose-only exception concerns whether Drawing is needed for that particular task; it does not cancel Drawing's universal session-start loading requirement.

**No premature-work exception:** Do not begin the requested project task while startup checks are pending. Do not substitute a promise, memory, previous-session load, Library copy, or a claim of readiness for fresh GitHub retrievals in the new conversation.

**Notification and disconnection limitation:** The startup notice must be delivered in the active conversation before retrieval begins. Do not tell the user that checks will continue after a voice call ends or that an independent callback/notification will occur. Complete and report the checks in the active conversation; the user may disconnect or start the work after the completion report.

This gate makes the existing session-start obligations explicit and operational. It does not guarantee that a future model will execute them; compliance must be established by the actual retrievals and read-back evidence in each new conversation.
- Do not create parallel prompt folders. `ChatGPT/prompts/` is the single canonical prompt location.
- Do not overwrite pre-existing workspace files without fetching the exact `ChatGPT/` path first and preserving their contents.

## 3. Before archiving

1. Read only the relevant existing session files under `ChatGPT/prompts/`.
2. Confirm the target branch from known project context. Do not inspect files outside `ChatGPT/` to do so.
3. Gather material only from the current conversation, user-provided files, or files under `ChatGPT/`.
4. Do not invent missing dialogue, image prompts, tool outputs, commit results, dates, or user preferences.
5. Exclude hidden reasoning, system/developer instructions, credentials, access tokens, and unrelated sensitive information. Archive user-visible conversation and task-relevant actions only.
6. If an important historical reference is mentioned but lives outside `ChatGPT/`, do not open it. Record the limitation or ask the user to provide the reference inside the workspace.

## 4. File 1: Conversation integrity

The conversation-integrity file is a chronological record, not a polished retelling.

- Preserve exact user and assistant wording wherever it is available and relevant.
- Keep repetitions, corrections, informal phrasing, and meaningful wording intact. Do not silently polish the transcript.
- Record tool activity as a clearly labeled **tool event**, not as dialogue.
- If a tool prompt or compiled input is not exposed, do not reconstruct it and call it verbatim.
- If part of the conversation is unavailable, add an **Editorial summary of unavailable material**. State that it is a summary, not a quote, and identify its basis when possible.
- Mark transcription uncertainty and omissions.
- Never claim the file is a complete verbatim transcript if it is curated, partial, or assembled from retained context.
- Keep interpretations and archival notes separate from the dialogue itself.
- Keep links within `ChatGPT/`. Do not add links to external repository paths.

Recommended structure:

```markdown
# Conversation Integrity — YYYY-MM-DD

**Project:** ...
**Branch:** ...
**Companion files:** [Summary](YYYY-MM-DD-summary.md) · [Image prompts](YYYY-MM-DD-image-prompts.md)

## Integrity policy
...

## Chronological record
...

## Gaps and editorial summaries
...

## Integrity and completeness notes
...
```

## 5. File 2: Session summary

The summary is a practical handoff for a future chat.

Include:
- The session's purpose.
- Important preferences and constraints.
- Decisions made and corrections supplied by the user.
- What was completed and what remains incomplete.
- Verified paths within `ChatGPT/` and the branch information when useful.
- The next concrete task, in priority order.

Separate confirmed facts from hypotheses. Do not repeat unsupported explanations as facts. Link only to files under `ChatGPT/`.

## 6. File 3: Image prompts

This is the operational history of image generation and editing.

### Mandatory pre-attempt rule

**Commit the authored prompt inside `ChatGPT/prompts/` before every image-generation or image-edit attempt.** This applies whether the next attempt is expected to succeed, is exploratory, or is a revision. Never generate first and archive later.

Before drafting the next prompt:
1. Read this session's image-prompt file under `ChatGPT/prompts/`.
2. Review the most relevant successful and unsuccessful prior attempts from within `ChatGPT/`.
3. Select a known base prompt when one exists.
4. Change as little as practical so the next attempt tests a clear hypothesis.
5. Append the new attempt with a sequential number and a pending outcome.
6. Commit the updated file on the working branch.
7. Verify the committed content by fetching the exact `ChatGPT/prompts/...` path.
8. Only then invoke image generation or editing.

### Required fields for each attempt

Record:
- Sequential attempt number and a short descriptive title.
- Status before the call: pending.
- Operation type: **fresh generation** or **edit of a reference image**.
- Source image/reference, when applicable. Use a path under `ChatGPT/images/` or an image supplied in the current conversation.
- The exact **authored prompt** prepared for the attempt.
- Whether the tool exposed the actual submitted/compiled prompt. If not, say the archived text is the authored direction and do not claim it is the verbatim internal payload.
- The specific detail being tested or changed.

### Record the result immediately afterward

Update the same entry with the actual outcome:
- **Generated successfully and followed the requested details.**
- **Generated, but missed a requested detail.** Name the mismatch.
- **Rejected; no image returned.**
- **Failed for a technical reason.**
- **Unconfirmed.**

Do not mark an image attempt successful merely because an image was returned. Inspect whether it followed the user's key instructions. Record what worked, what failed, and one useful next-step lesson.

### Image handling

- Deliver generated images in the conversation.
- Store repository image assets only under `ChatGPT/images/`, and only when the user has requested repository storage or the established workflow requires it.
- Never claim a fresh generation was an edit of the original.
- Never claim a reference image was supplied unless the tool call actually included that reference.
- Preserve source-image identity and distinguish an edit from a newly generated composition.
- Use a reference image only from `ChatGPT/images/` or from an image the user supplies directly in the current conversation.
- If an image edit fails, state that the image was not modified; do not imply the source image changed.

### Separate successful-prompt index

Maintain one separate file at `ChatGPT/prompts/successful-image-prompts-index.md`. This is a curated index, not a replacement for the complete chronological image log.

1. Include only prompt attempts whose recorded outcome is a successful match or a successful generation that followed its defining creative direction. Do not include rejected attempts, failed generations, generated-but-missed-target results, or partial matches.
2. For each included attempt, link directly to the original attempt heading in the chronological image log.
3. Link directly to each known associated image file under `ChatGPT/images/`. Include more than one image when a single successful prompt produced multiple approved results.
4. Preserve caveats when a particular detail was not verified, or when the successful output fulfilled a revised prompt but was later superseded by a clarified brief.
5. Update the successful-only index when an attempt's result is finalized or when an image is renamed. Keep failed and partial attempts in the chronological history only.
6. Link the successful-only index from the chronological image log and from the session summary. Read back the index and all changed files after writing.

Do not silently promote a merely generated image to a success. Use the outcome classification and visual inspection recorded in the chronological log.

### User-approved visual references and binary provenance

When the user asks to retain generated or uploaded images as reusable references:

1. Give each approved image a stable, descriptive filename. Preserve the original image bytes whenever possible; do not overwrite a full-resolution original with a thumbnail.
2. Keep image binaries under `ChatGPT/images/` when a supported repository binary-upload route is available. After upload, verify the exact path and blob identity before claiming repository storage.
3. If the current GitHub connection cannot transfer binary files, preserve the original image in the persistent Files Library using a descriptive name, and create `ChatGPT/images/reference-index.md` as a tracked pointer. Record the exact Library path, stable file ID, source generation ID, original artifact name, dimensions, byte count, and SHA-256 checksum when available.
4. State clearly whether an asset is stored in GitHub, the persistent Files Library, or only the conversation. A Markdown index in GitHub does not mean that the image binary is in Git.
5. Link user-accessible Library assets through the supported file-navigation UI in the final response. Do not invent a URL for a Library item.
6. In the image-prompt log, link each successful attempt to the relevant reference-index entry. In the conversation-integrity file, record the user's approval and the exact storage actions as tool events.
7. Update the drawing skill when the user-approved images establish a reusable visual direction. Distinguish visual inspiration references from verified edit sources.

### Mandatory uploaded-image rename and cross-link procedure

For each image the user uploads as part of the Maya & Me image workflow:

1. Inspect the image itself and identify its role and distinguishing visible content. Do not rely on the incoming filename as the descriptive name.
2. Unless the user explicitly marks it temporary or says not to retain it, rename the uploaded image using an accurate, descriptive, stable filename. Use the exact surfaced file ID or Library file ID from Files metadata; never guess an identifier.
3. **Rename only. Do not convert, recompress, resize, crop, rotate, filter, retouch, strip metadata, or create derivatives unless the user explicitly authorizes that exact change.** Preserve the original format, extension, resolution, metadata, and byte content exactly.
4. Perform task-related file creation and editing only inside the assigned `ChatGPT/` workspace. Do not create temporary files, conversion intermediates, derivatives, or working copies outside `ChatGPT/images/`, `ChatGPT/prompts/`, or `ChatGPT/skills/` without explicit user permission for a specific location.
5. Keep image binaries under `ChatGPT/images/` when a supported repository binary-upload route is available. After upload, verify the exact path and blob identity before claiming repository storage.
6. If the current GitHub connection cannot transfer binary files, preserve the exact user-uploaded original in the persistent Files Library only when it can be filed within the assigned `ChatGPT/images/` path. Create `ChatGPT/images/reference-index.md` as a tracked pointer. Record the exact path, stable file ID, source generation ID, original artifact name, dimensions, byte count, and SHA-256 checksum when available. Do not create a fallback folder elsewhere.
7. State clearly whether an asset is stored in GitHub, the persistent Files Library, or only the conversation. A Markdown index in GitHub does not mean that the image binary is in Git.
8. Link user-accessible Library assets through the supported file-navigation UI in the final response. Do not invent a URL for a Library item.
9. In the image-prompt log, link each successful attempt to the relevant reference-index entry. In the conversation-integrity file, record the user's approval and the exact storage actions as tool events.
10. Update the drawing skill when the user-approved images establish a reusable visual direction. Distinguish visual inspiration references from verified edit sources.

Do not finish a drawing-session archive while an uploaded keeper image remains under an opaque temporary filename or while its successful prompt and conversation event lack direct links.

### When an opaque image cannot be visually inspected

If an image is present in `ChatGPT/images/` but its binary cannot be surfaced through the available image reader, do not invent a subject description. If its existing name contains a reliable timestamp, it may be renamed to a neutral, timestamp-based filename that preserves the original extension (for example, `archive-photo-YYYY-MM-DD-HHMMSSZ.jpg`). Record that the pixels were not inspected and that the name is temporal rather than content-descriptive. If no reliable timestamp or other identifying metadata exists, leave the file unchanged until its visual content can be provided. In either case, preserve the exact Git blob SHA and byte size.

### Renaming image files already tracked in GitHub

When an uploaded image is already present in `ChatGPT/images/` under an opaque or temporary filename, do not create another copy. Rename the existing Git tree path while reusing its exact blob SHA. Remove the old path in the same tree update, commit on `chatgpt`, and verify the new path, absence of the old path, identical blob SHA, and identical byte size. This is the preferred zero-byte-change rename. Never re-encode or re-upload the image merely to change its filename. If a safe same-blob rename cannot be performed, stop and explain the limitation rather than silently creating a derivative or claiming the rename is complete.

## 7. GitHub write and verification discipline

- Perform all file operations using exact paths under `ChatGPT/` on branch `gpt`.
- Do not list, fetch, search, inspect, or mutate any file path outside `ChatGPT/`.
- For an update, fetch the current file first and use its current blob SHA.
- Perform sequential writes to the same file. Do not run updates to the same path in parallel.
- After each important write, fetch the same `ChatGPT/` path again and verify its contents.
- Report a commit as successful only when the write tool returns a commit SHA. Report verification only after a read-back confirms the expected content.
- If a write or network call fails, inspect only relevant paths inside `ChatGPT/` before retrying to avoid duplicate files or duplicate commits.
- Do not use repository-root or outside-folder operations as a shortcut.
- Leave `main` untouched unless the user explicitly authorizes changes there.

## 8. Finishing a session

1. Verify the relevant dated records under `ChatGPT/prompts/` exist and contain the intended material.
2. Verify every image attempt made in the session has a recorded outcome.
3. Ensure the next task in the summary matches the latest prompt-history state.
4. Provide direct links to records under `ChatGPT/`.
5. State any known gaps honestly. Do not promise background notification or work after the conversation ends unless a supported automation has actually been created.

## 9. Default handoff for a new chat

Start by reading the relevant records inside `ChatGPT/prompts/` only. Then:
- Treat the conversation-integrity file as the source for what was said.
- Treat the summary as a quick orientation, not a replacement for the record.
- Treat the image-prompt file as the authoritative chronological record for generation work.
- Continue from the latest incomplete task.
- Follow the pre-attempt commit rule before generating or editing another image.
- Never read or write anything outside `ChatGPT/`.

 
## 10. WebP delivery derivatives

The user approved keeping original PNG/JPEG master images alongside WebP delivery copies so they can inspect the results visually.

- Source masters remain untouched. Never delete, overwrite, rename, resize, recompress, or edit a source image as part of WebP generation.
- The generated-only directory is `ChatGPT/images/webp/`. Mirror the source's relative path and append `.webp` to its full filename (for example, `portrait.png` becomes `webp/portrait.png.webp`). Do not manually store master images or unrelated assets in this directory.
- Record each conversion in `ChatGPT/images/webp/conversion-report.csv`, including source/output paths, byte counts, percentage size change, profile, ICC metadata handling, encoder version, and outcome. A negative saving is valid: keep the WebP and report that it is larger. Never discard a conversion based only on file size.
- PNGs use exact lossless WebP encoding (`-lossless -q 100 -m 6 -exact`). The exact option preserves RGB values in fully transparent pixels. JPEGs use high-quality lossy WebP (`-preset picture -q 92 -m 6 -sharp_yuv`). Copy ICC profiles with `-metadata icc`; EXIF and XMP are not copied by this profile.
- Animated PNG (APNG) files are skipped because `cwebp` does not encode animated PNG input. Record the skip in the CSV rather than silently creating a static substitute.
- The workflow runs only on `chatgpt`; it may write generated files only below `ChatGPT/images/webp/`. It must not change the source files.
- The workflow definition is at `.github/workflows/convert-images-to-webp.yml`. The user's one-time authorization covers its initial creation only. Any future modification requires new explicit permission because it is outside the assigned workspace.
- After installation, verify the workflow YAML, generated folder instructions, skill updates, and session records by reading back their exact paths. Do not claim a successful GitHub Actions run unless a run is observed as completed successfully.
