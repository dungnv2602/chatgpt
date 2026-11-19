## 1. Absolute workspace boundary

**Standing default:** All repository file work must stay inside these approved project directories at the repository root: `images/`, `master/`, `novel/`, `prompts/`, and `skills/`. Do not read, list, search, fetch, create, update, move, rename, or delete files outside those directories, except for the specifically authorized workflow exception below.

**One-time authorized WebP workflow exception (12 November 2026):** The user explicitly authorized creation of exactly `.github/workflows/convert-images-to-webp.yml` outside the approved project directories for that specific task only. This exception does not authorize changes to other outside paths or future edits to that workflow. Obtain fresh, explicit permission before any later change to it.

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
- Store new visual assets explicitly destined for the repository under `images/`.
- Keep skills and supporting references under `skills/`.

### Conversation behavior

After loading this foundational Session Archiving skill at the start of a Maya & Me conversation, retrieve and read the [Conversation Mode skill](../conversation-mode/SKILL.md) from the same `gpt` branch before continuing with project work. Apply its Default Mode / Condensed Mode selection, persistence, and response rules throughout the conversation. This skill governs archiving; the Conversation Mode skill governs collaboration. The two skills are complementary.

### Foundational skill loading cadence

Load the Session Archiving skill and Conversation Mode skill once at the beginning of each new Maya & Me ChatGPT conversation/session. Track that both have been loaded and continue applying them for the remainder of that session. Refresh a foundational skill when the user explicitly asks, a relevant repository change is known or reasonably suspected, or an unresolved instruction requires checking the authoritative file. A new ChatGPT conversation/session starts a new loading cycle. This cadence does not remove the requirement to load a task-specific skill when needed or to read relevant project records before performing that task.

### First-response execution rule

The first assistant response in a new Maya & Me conversation must be an informational startup notice, not a request for the user's goal, confirmation, or permission. Immediately after that notice, execute the required retrievals below. Do not ask the user to repeat, explain, or activate the project workflow. Do not claim a check is underway unless its retrieval is actually being performed.

The startup gate is a prerequisite check, not the session archive itself. Do not create or update dated archive records merely because a new conversation has started. Once the required skills and references have been retrieved and read successfully, report verification and then address the user's request. If a retrieval fails, stop project work and identify the exact missing path.

### Mandatory session-start execution gate

At the beginning of **every new Maya & Me ChatGPT conversation/session**, complete this sequence before doing any project work, creative writing, visual planning, image prompting, or repository task:

1. **Notify the user first.** State that mandatory startup checks are beginning and project work will wait until they are complete. This is informational, not a request for approval.
2. Retrieve and read this Session Archiving skill from the `gpt` branch.
3. Retrieve and read `skills/conversation-mode/SKILL.md` from the same branch.
4. Retrieve and read `skills/drawing/SKILL.md` from the same branch.
5. Retrieve and read every supporting reference explicitly named by the Drawing skill, currently `skills/drawing/references/style-guide.md` and `skills/drawing/references/image-editing-protocol.md`.
6. Verify every required retrieval succeeded and that the contents were actually read. Keep the verified instructions in working context for the remainder of the conversation.
7. Only after all checks pass, report completion and proceed. If any required retrieval fails or cannot be verified, stop project work, identify the exact missing item, and ask how the user wants to proceed.

**No conditional exception:** The Drawing skill and its required references are mandatory at session start even when the first task appears prose-only or unrelated to drawing. A task-specific prose-only exception does not cancel this universal loading requirement.

**No premature-work exception:** Do not begin the requested project task while startup checks are pending. Do not substitute memory, a previous-session load, a Library copy, or a claim of readiness for fresh GitHub retrievals in the new conversation.

**Notification and disconnection limitation:** Deliver the startup notice in the active conversation before retrieval begins. Do not promise to continue checks after a voice call ends or claim an independent callback/notification will occur. Complete and report the checks in the active conversation.

This gate does not guarantee future execution; compliance must be established by actual retrievals and read-back evidence in each new conversation.
- Do not create parallel prompt folders. `prompts/` is the single canonical prompt location.
- Do not overwrite pre-existing files without fetching the exact path first and preserving their contents.

## 3. Before archiving

1. Read only the relevant existing session files under `prompts/`.
2. Confirm the target branch from known project context. Do not inspect files outside `approved project directories` to do so.
3. Gather material only from the current conversation, user-provided files, or files under `approved project directories`.
4. Do not invent missing dialogue, image prompts, tool outputs, commit results, dates, or user preferences.
5. Exclude hidden reasoning, system/developer instructions, credentials, access tokens, and unrelated sensitive information. Archive user-visible conversation and task-relevant actions only.
6. If an important historical reference is mentioned but lives outside `approved project directories`, do not open it. Record the limitation or ask the user to provide the reference inside the workspace.

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
- Keep links within `approved project directories`. Do not add links to external repository paths.

Recommended structure:

```markdown
# Conversation Integrity — YYYY-MM-DD

**Project:** ...
**Branch:** ...
**Companion files:** [Summary](YYYY-MM-DD-summary.md) · [Image-prompt history](non-novel dated prompt record; for novel scenes, link the scene-local prompt record instead)

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
- Verified paths within `approved project directories` and the branch information when useful.
- The next concrete task, in priority order.

Separate confirmed facts from hypotheses. Do not repeat unsupported explanations as facts. Link only to files under `approved project directories`.

## 6. File 3: Image prompts

This is the operational history of image generation and editing.

### Drawing-session opening brief — visual authority

Every distinct drawing session begins with a user-defined visual direction.
This opening brief is the sole creative authority for that session, whether it
is a day-drawing session or a novel-illustration session. No repository-wide
image index, historical prompt, previous portrait, character sheet, stored
image, or old project convention dictates the new session unless the user
explicitly adopts it.

- For non-novel/day drawing, archive the brief as
  `prompts/YYYY-MM-DD/session-[NN]-brief.md`.
- For a named novel scene, archive it as
  `novel/[Novel-ID]/[Arc-ID]/[Scene-ID]/illustrations/session-[YYYY-MM-DD]-[NN]-brief.md`.
- Create and commit the brief before the first image prompt for that session.
  Read it back and verify it.
- Preserve the user's opening direction faithfully. Record specified, locked,
  variable, excluded, and open details. Mark unspecified features as open;
  never invent constraints.
- Append later explicit user corrections or refinements as dated amendments
  in the same brief. Preserve the original opening brief; do not silently
  rewrite its history. The latest explicit user instruction controls the
  property it changes.
- Every attempt note must link to its session brief and identify its session ID.
- A new drawing session gets a new brief even when it belongs to the same day,
  character, novel, or series. Earlier images and prompts are historical
  references only unless explicitly selected by the user in the new session.
- In a novel session, scene and manuscript records provide narrative facts
  only to the extent the user asks the illustration to follow or adapt them.
  The session brief governs visual interpretation and design.
- Do not create, maintain, or recreate `images/reference-index.md` or any
  replacement repository-wide visual authority index. Session-specific image
  provenance belongs in the session brief and relevant attempt record.

### Session brief structure

Use this structure for each session brief. Preserve the user's actual opening
wording in the first section; the structured fields summarize it and must not
invent detail.

```markdown
# Drawing Session Brief

**Session ID:** ...
**Session type:** Day drawing / Novel illustration
**Project or novel scene:** ...
**Created:** YYYY-MM-DD
**Status:** Active / Paused / Closed

## User's opening brief
> [Preserve the user's opening direction accurately.]

## Active visual direction
- Subject and theme:
- Scene or story moment:
- Mode / medium:
- Character identity and appearance:
- Wardrobe:
- Pose and spatial relationships:
- Camera / framing:
- Environment:
- Lighting and palette:
- Mood / emotional intention:
- **Narrative fidelity (novel illustration only):** Text-faithful / Interpretive / Adaptive / Not applicable

## Locked features
- ...

## Permitted variation
- ...

## Explicit exclusions
- ...

## References assigned to this session
- Asset:
- User-assigned role:
- Actual attachment/source status:

## Amendments
- [Date/time] — [User's exact correction or concise faithful record]
```

Write `Not specified / open` for fields the user has not defined. Do not fill
gaps from a former session, a global image catalogue, a successful prompt, or
the assistant's aesthetic assumptions. A session brief may be compact when the
user's request is compact; this is a record of the user's direction, not a
questionnaire that must be completed before work.

For a novel illustration, the user selects one narrative-fidelity mode in the
opening brief:
- **Text-faithful:** Depict the stated events, relationships, chronology, and
  scene facts closely. Do not invent or contradict manuscript facts. Creative
  choices are limited to details the source and brief leave open.
- **Interpretive:** Preserve established story facts, character intentions, and
  the scene's emotional meaning, while allowing the assistant to choose visual
  staging, gestures, framing, and other unspecified details.
- **Adaptive:** Deliberately reinterpret or depart from literal staging while
  preserving the story elements the user identifies as non-negotiable. State
  the permitted adaptation scope in the brief.

Do not choose a fidelity mode on the user's behalf when the distinction would
materially change the illustration. Ask one focused question if the brief and
context do not resolve it. Day-drawing sessions may mark this field
`Not applicable` unless the user wants a source-faithfulness constraint.

### Daily folder and one-note-per-attempt format for non-novel drawing work

For non-novel drawing work, organize image prompts by date. Each calendar day is a folder under `prompts/`, and each image-generation or image-edit attempt is its own Markdown note. **Exception:** for an illustration belonging to a named novel scene, the scene-local prompt record under `novel/[Novel-ID]/[Arc-ID]/[Scene-ID]/illustrations/` is authoritative. Keep that novel attempt there and do not duplicate it in the daily `prompts/` folder.

```text
prompts/
  YYYY-MM-DD/
    README.md              # daily index and status overview
    session-01-brief.md    # authoritative direction for this drawing session
    attempt-01.md          # one complete attempt record
    attempt-02.md
    ...
```

- Use zero-padded sequential filenames (`attempt-01.md`, `attempt-02.md`, ...), with one attempt per file. Never append a second attempt to an existing attempt note.
- `README.md` is the daily index: list attempts in order, link each note and its session brief, and show its current outcome/status. Update it whenever an attempt is added or its outcome changes.
- **README table format is mandatory:** use exactly one continuous Markdown table for the entire day's attempt index, with a single header row and consistent columns (at minimum `Attempt`, `Prompt note`, `Session brief`, `Primary series / membership`, and `Status / outcome`). Every attempt, including the latest one, must be a row inside that same table. Use a stable series ID/name; write `standalone/unassigned` when no series is established. Do not place a second table below it, split the index into separate tables, or leave attempt rows outside the table. Keep rows in ascending attempt-number order.
- **Keep table rows physically contiguous:** never insert a blank line between the header, separator, or any attempt row. A blank line terminates a Markdown table in many renderers and can make the newest attempt appear as a separate block. When appending an attempt, add its row immediately after the previous row with no empty line. When revising a status, edit the existing row in place; do not move it outside the table or create a second table.
- **Validate before committing:** read back the complete daily `README.md` and verify that it contains exactly one attempt-index table, one header row, one separator row, and every numbered attempt exactly once in ascending order. Confirm there are no blank lines inside the table and that the final attempt row is part of the same contiguous table. Do not mark the index update complete until this read-back check passes.
- **Status accuracy:** distinguish `not approved / not generated`, `approved / pending generation`, `generated successfully`, `generated with mismatch`, `rejected / no image returned`, and `technical failure`. If an attempt has multiple runs, preserve the sequence in the status cell (for example, an earlier image returned but a later retry was rejected); do not overwrite history with only the latest or earlier outcome. A user declining approval must never be represented as pending approval.
- Each attempt note contains all required fields below, the exact authored prompt, and its final outcome when known. Keep the full record self-contained.
- Session-level conversation-integrity and summary records remain at `prompts/YYYY-MM-DD-conversation-integrity.md` and `prompts/YYYY-MM-DD-summary.md` unless the user changes that convention.
- Existing legacy `YYYY-MM-DD-image-prompts.md` files remain historical records. Do not delete or rewrite them during adoption unless the user explicitly requests migration. For a day already in progress, create the daily folder and separate notes for its attempts; preserve the legacy file as-is.

### Mandatory pre-attempt rule

**Commit the session brief and authored prompt in their authoritative locations before the first image-generation or image-edit attempt.** For non-novel work, use the session brief and attempt notes under `prompts/YYYY-MM-DD/`. For a named novel scene, use the session brief and illustration prompt records under `novel/[Novel-ID]/[Arc-ID]/[Scene-ID]/illustrations/`. This applies whether the next attempt is expected to succeed, is exploratory, or is a revision. Never generate first and archive later, and never duplicate a novel-scene prompt in the root `prompts/` history.

Before drafting the next prompt:
1. Read the authoritative session-opening brief first. If it does not exist,
   create it from the user's opening direction, commit it, and read it back
   before drafting the first image prompt. For novel illustrations, place the
   brief in the scene-local illustration folder.
2. Read the authoritative chronological prompt history for the exact artwork
   thread or novel scene. Identify the active primary series only when the
   session brief explicitly continues/adopts it. Inspect later attempts for
   context, then locate the most recent successful prompt in that same series.
3. Use only that most recent successful prompt as the historical text baseline.
   The current session brief outranks it: discard or rewrite every conflicting
   feature. Newer failed, rejected, partial, or missed-target prompts are
   diagnostic evidence only. Extract only explicit user-requested/user-approved
   changes from them and apply those changes to the successful baseline. Never
   use a failed prompt as the base.
4. If no series applies, use the most recent successful prompt for the exact
   artwork/thread. If no relevant success exists, start from the current session
   brief and explicit constraints; do not borrow from an unrelated series. For a
   new subseries, record any inherited parent-series seed and branch point.
5. Change as little as practical so the next attempt tests a clear hypothesis.
6. Append a new attempt with a sequential number, required series metadata,
   baseline provenance, and a pending outcome.
7. Commit the updated file on the working branch.
8. Verify the committed content by fetching the exact prompt-record path.
9. Only then invoke image generation or editing.

### Required fields for each attempt

Record:
- Sequential attempt number and a short descriptive title.
- Status before the call: pending.
- **Drawing session ID and session-brief path.** Mandatory for every attempt.
- **Opening direction authority:** link the active session brief and confirm it controls visual direction. Do not treat any prior index, prompt, or image as a replacement.
- **Primary series ID/name and theme spine.** Record a series only when the current session brief explicitly continues/adopts it. Otherwise record `standalone/unassigned`; do not guess. Record secondary series only for a deliberate crossover.
- **Membership role:** series seed, continuation, subseries, branch, crossover, standalone, or provisional. For a branch, record the parent series and branch point.
- **Continuity anchors and permitted variation** relevant to this attempt, taken from the current session brief; state which user-locked details must remain unchanged. Do not import locks from an older session.
- **Prompt baseline provenance:** exact path/attempt or scene-local record of the most recent successful prompt in the primary series (or exact artwork thread if not a series), its recorded outcome, and why it qualifies. If the next operation requires a full-scene prompt but the newest success is only a localized edit/style-only prompt, also record the most recent successful full-generation prompt from that same series as the operation-compatible text skeleton and explain the choice. If there is no such baseline, say so explicitly. For a new branch, record the inherited seed and its source.
- **Latest-attempt diagnostic reference:** link the newest later attempt inspected when it differs from the selected successful baseline, and state what was or was not carried forward from it.
- **Acceptance criteria:** normally three to five observable requirements derived from the active brief for this image; mark critical criteria and define the visible evidence for each. Record `Not applicable` only when no meaningful visual criterion can be derived.
- **Prompt difference:** record (a) baseline prompt or `none / first attempt`, (b) details preserved, (c) details changed, and (d) details deliberately excluded/not carried forward. Identify the user instruction supporting each change.
- Operation type: **fresh generation** or **edit of a reference image**.
- Source image/reference, when applicable. Distinguish inspiration references from the exact edit source, and record the actual asset/attachment identifier only when it was supplied to the tool.
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

Do not mark an image attempt successful merely because an image was returned. Inspect whether it followed the user's key instructions and the active session brief. Record what worked, what failed, and one useful next-step lesson.

When one tool call returns multiple images, record each output separately within that attempt: its image/generation identifier or stored path, whether it meets the defining requirements of the active session brief, and whether the user approved it as a keeper. Preserve mixed outcomes; one successful output does not make every image in the batch successful. The prompt/result pair may qualify as a successful prompt baseline when at least one output is explicitly judged successful for the intended purpose and the prompt-to-output link is reliable; use only individually approved output(s) as visual references, and only in future sessions when the user explicitly selects them.

Keep two judgements distinct:
- **Prompt/result success:** the prompt is linked to an output that meets the defining requirements, or the user explicitly accepts that attempt's result as successful for the intended purpose. This may qualify the exact prompt as a future series baseline.
- **User-approved visual keeper:** the user approves an image as a visual asset. This approval does not automatically validate an uncertain or separately unsuccessful originating prompt. When the exact prompt link is known and the user accepts the attempt/result as successful, record both the user-approved output and its prompt-baseline eligibility without erasing earlier assessment history.

A failed, rejected, partial, or missed-target prompt is never the default text baseline. If a later successful prompt does not exist, return to the most recent successful prompt in the same series/artwork thread and apply only user-requested changes from later attempts.

### Image handling

- Deliver generated images in the conversation.
- Store repository image assets only under `images/`, and only when the user has requested repository storage or the established workflow requires it.
- Never claim a fresh generation was an edit of the original.
- Never claim a reference image was supplied unless the tool call actually included that reference.
- Preserve source-image identity and distinguish an edit from a newly generated composition.
- Use a reference image only from `images/` or from an image the user supplies directly in the current conversation.
- If an image edit fails, state that the image was not modified; do not imply the source image changed.

### Separate successful-prompt index

Maintain one separate file at `prompts/successful-image-prompts-index.md`. This is a curated index, not a replacement for the complete chronological image log.

1. Include only prompt attempts whose recorded outcome is a successful match or a successful generation that followed its defining creative direction. Do not include rejected attempts, failed generations, generated-but-missed-target results, or partial matches as prompt successes.
2. For each included attempt, record its primary series ID/name and theme spine, plus any verified branch/subseries relationship. If historical membership cannot be established reliably, label it `legacy/unassigned` rather than guessing.
3. Link directly to the original attempt heading or scene-local prompt record and each known associated image file under `images/`. Include more than one image when a single successful prompt produced multiple approved results.
4. Preserve caveats when a particular detail was not verified, when the successful output fulfilled a revised brief, or when a user-approved visual keeper is not itself proof of prompt success.
5. Keep the success index as a discovery aid. Determine which prompt is most recent from the chronological source records within the active series; never infer recency from the order of index entries.
6. Update the successful-only index when an attempt's result is finalized or when an image is renamed. Keep failed and partial attempts in the chronological history only, unless the user separately approves an image as a visual keeper; then list it in the user-approved-output section without disguising the prompt's actual outcome.
7. Link the successful-only index from the chronological non-novel image log and from the session summary. For a novel-scene prompt, link the scene-local record without copying its prompt text into the root log. Read back the index and all changed files after writing.

Do not silently promote a merely generated image to a success. Use the outcome classification and visual inspection recorded in the chronological log. A user-approved image whose originating prompt is known may qualify as a successful prompt/result pair when the user's approval clearly accepts that attempt as successful; preserve the user's attribution. If the prompt mapping or scope of approval is uncertain, keep it as an approved visual asset only and continue using the latest verified successful prompt as the text baseline.

### Session-local image asset handling and provenance

When the user asks to retain generated or uploaded images, or when the active
session workflow requires keeping a source asset:

1. Give each retained image a clear, descriptive filename based on its visible
   content. Preserve the original bytes; do not overwrite a full-resolution
   original with a thumbnail.
2. Keep image binaries under `images/` when a supported repository binary-upload
   route is available. Verify the exact path and blob identity before claiming
   repository storage.
3. If the binary cannot be transferred to GitHub, retain it in the persistent
   Files Library only when the user has requested retention and that storage is
   available. Record its exact Library path, stable file ID, source generation
   ID, original artifact name, dimensions, byte count, and checksum where
   available in the current session brief or attempt record—not in a global
   visual reference index.
4. State clearly whether an asset is stored in GitHub, the persistent Files
   Library, or only the current conversation. A Markdown note does not mean
   that the image binary is in Git.
5. Link the asset directly from the session brief or relevant attempt record
   using a verified repository path or supported file-navigation reference.
   Never invent a URL.
6. Preserve the asset's role within that session: inspiration, identity,
   composition, style, exact edit source, or approved keeper. A retained image
   is not automatically a reference for future drawing sessions.
7. Never create or maintain `images/reference-index.md` or any replacement
   global index intended to dictate visual identity, wardrobe, style, or
   composition. The session-opening brief is the only visual-direction
   authority for its session.

### Session-specific uploaded-image naming and cross-link procedure

For an image the user supplies within a drawing session:

1. Inspect the image itself and identify its role as stated by the user or
   assigned in the session brief. Do not rely on its incoming filename.
2. If the user asks to retain it for later use, give it an accurate, descriptive,
   stable filename. Use consistent numbered suffixes for a set. If it is only
   for the current session, do not silently promote it to a future-session asset.
3. **Rename only. Do not convert, recompress, resize, crop, rotate, filter,
   retouch, strip metadata, or create derivatives unless explicitly authorized.**
   Preserve original format, extension, resolution, metadata, and bytes.
4. Record the exact path, stable file/Library ID, source generation ID when
   known, original name, dimensions, byte size, checksum where available, and
   session-specific role in the session brief or attempt record.
5. When the image is associated with a successful output, link it directly in
   the relevant attempt record and successful-prompt index if appropriate.
   Do not add a global reference-index link.
6. In conversation-integrity records, record the user's instruction/approval
   and exact storage or rename actions as tool events. Preserve historical
   facts, but do not treat them as current visual direction.
7. Verify the renamed asset through Files metadata and read back every updated
   GitHub Markdown file. Never claim a Library URL or GitHub storage unless
   verified.

Do not finish a session archive while a requested keeper image remains under an
opaque temporary filename or while its session brief and successful prompt
record lack direct links.

### When an opaque image cannot be visually inspected

If an image is present in `images/` but its binary cannot be surfaced through the available image reader, do not invent a subject description. If its existing name contains a reliable timestamp, it may be renamed to a neutral, timestamp-based filename that preserves the original extension (for example, `archive-photo-YYYY-MM-DD-HHMMSSZ.jpg`). Record that the pixels were not inspected and that the name is temporal rather than content-descriptive. If no reliable timestamp or other identifying metadata exists, leave the file unchanged until its visual content can be provided. In either case, preserve the exact Git blob SHA and byte size.

### Renaming image files already tracked in GitHub

When an uploaded image is already present in `images/` under an opaque or temporary filename, do not create another copy. Rename the existing Git tree path while reusing its exact blob SHA. Remove the old path in the same tree update, commit on `gpt`, and verify the new path, absence of the old path, identical blob SHA, and identical byte size. This is the preferred zero-byte-change rename. Never re-encode or re-upload the image merely to change its filename. If a safe same-blob rename cannot be performed, stop and explain the limitation rather than silently creating a derivative or claiming the rename is complete.

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

**The only closeout trigger is the user's direct cue: `end session`.**
Recognize it only as a standalone instruction, case-insensitive and allowing
surrounding punctuation. A quoted mention or discussion of the phrase does not
invoke it. Do not infer closeout from a pause, goodbye, a topic change, an
apparently final image, the start of another session, or the end of a chat.

Until the cue is received:
- Keep the drawing session marked `Active` or `Paused`; never mark it
  `Closed` merely because work has stopped temporarily.
- Preserve its current brief, prompt lineage, attempt outcomes, unresolved
  criteria, and next step.
- A new drawing session may begin with a new brief, but this does not close the
  preceding session. Mark the preceding session `Paused` if appropriate.

When the user sends `end session`, close the active drawing session without
asking for a second confirmation:

1. Stop further image generation/editing for that session.
2. Verify the opening brief and every amendment, and confirm all attempts are
   recorded in their authoritative locations.
3. Verify every generated output separately, including its acceptance-criteria
   assessment, outcome, image/source identifier, and user approval status.
4. Ensure every attempt contains its prompt baseline provenance and prompt
   difference record: preserved, changed, and excluded details.
5. Identify the final approved image(s), their exact originating prompts, and
   any storage location that is actually verified. Do not label an unapproved
   or uncertain output as final.
6. Record unresolved requirements, failed attempts, missing source links,
   technical gaps, and any work intentionally left incomplete. Do not erase
   failures or silently mark them successful.
7. Update the session brief status to `Closed`; prepare or update the relevant
   session summary/handoff with completed work, approved outputs, unresolved
   items, and the next possible task.
8. Read back all changed records and verify their links and status. If archival
   verification fails, report the exact gap and do not claim a fully verified
   closeout.

A closeout may be recorded as `Closed — unresolved items remain` when the user
ends the session before every visual requirement is satisfied. Closing a
session records its state; it does not imply that every image succeeded.

## 9. Finishing a session

1. Verify the relevant session records under `prompts/` exist. For non-novel drawing work, verify the dated attempt notes and README; for a named novel scene, verify its scene-local prompt records under `novel/` instead of creating duplicate attempt notes in `prompts/`.
2. Verify every image attempt made in the session has a recorded outcome in its authoritative location.
3. Ensure the next task in the summary matches the latest prompt-history state.
4. Provide direct links to records under `approved project directories`.
5. State any known gaps honestly. Do not promise background notification or work after the conversation ends unless a supported automation has actually been created.

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

The user approved keeping original PNG/JPEG master images alongside WebP delivery copies so they can inspect the results visually.

- Source masters remain untouched. Never delete, overwrite, rename, resize, recompress, or edit a source image as part of WebP generation.
- The generated-only directory is `images/webp/`. Mirror the source's relative path and append `.webp` to its full filename (for example, `portrait.png` becomes `webp/portrait.png.webp`). Do not manually store master images or unrelated assets in this directory.
- Record each conversion in `images/webp/conversion-report.csv`, including source/output paths, byte counts, percentage size change, profile, ICC metadata handling, encoder version, and outcome. A negative saving is valid: keep the WebP and report that it is larger. Never discard a conversion based only on file size.
- PNGs use exact lossless WebP encoding (`-lossless -q 100 -m 6 -exact`). The exact option preserves RGB values in fully transparent pixels. JPEGs use high-quality lossy WebP (`-preset picture -q 92 -m 6 -sharp_yuv`). Copy ICC profiles with `-metadata icc`; EXIF and XMP are not copied by this profile.
- Animated PNG (APNG) files are skipped because `cwebp` does not encode animated PNG input. Record the skip in the CSV rather than silently creating a static substitute.
- The workflow runs only on `gpt`; it may write generated files only below `images/webp/`. It must not change the source files.
- The workflow definition is at `.github/workflows/convert-images-to-webp.yml`. The user's one-time authorization covers its initial creation only. Any future modification requires new explicit permission because it is outside the assigned workspace.
- After installation, verify the workflow YAML, generated folder instructions, skill updates, and session records by reading back their exact paths. Do not claim a successful GitHub Actions run unless a run is observed as completed successfully.
