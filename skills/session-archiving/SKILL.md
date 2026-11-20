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
**Status:** Active / Paused / Closed (new sessions begin Active)

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
- **Source scene/version (novel illustration):** exact scene/chapter or supplied passage the user wants followed/adapted

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

### Session status and transitions

- Create every new drawing-session brief with status `Active`.
- Keep at most one drawing session `Active` in the current workflow context.
  When a new distinct session begins while another session is still open, mark
  the previous `Active` session `Paused` and the new session `Active`.
- When resuming a `Paused` session, mark it `Active` and mark any other
  currently `Active` session `Paused`.
- `Paused` means temporarily inactive, not closed. Never change a session to
  `Closed` without the user's closeout cue.
- While the session being discussed is `Active` or `Paused`, include the
  closeout reminder at the end of each response that continues or discusses
  that drawing session. The reminder is not a scheduled or background
  notification; it appears in the conversation response.

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
- **Pre-generation acceptance criteria:** normally three to five observable requirements derived from the active brief, with critical/non-critical status and the visible evidence expected. These must be recorded before generation/editing, not reconstructed after seeing the output.
- **Per-output assessment:** for every image returned, score each criterion Pass / Partial / Fail / Not assessable and cite the visible evidence. Keep outputs separate when one call returns multiple images.
- Operation type: **fresh generation** or **edit of a reference image**.
- Source image/reference, when applicable. Distinguish inspiration references from the exact edit source, and record the actual asset/attachment identifier only when it was supplied to the tool.
- The exact **authored prompt** prepared for the attempt.
- Whether the tool exposed the actual submitted/compiled prompt. If not, say the archived text is the authored direction and do not claim it is the verbatim internal payload.
- The specific detail being tested or changed.

### Acceptance-criteria and prompt-difference format

Before the tool call, include this compact ledger in the attempt record:

```markdown
## Acceptance criteria — before generation/editing
| # | Observable requirement | Critical? | Expected visible evidence |
|---|---|---|---|
| 1 | ... | Yes/No | ... |

## Prompt difference
- **Baseline:** [exact successful prompt path/attempt, or none / first attempt]
- **Preserved:** [what is carried forward]
- **Changed:** [what is different and the user's instruction authorizing it]
- **Excluded:** [what is deliberately not carried forward and why]

## Per-output assessment — after generation/editing
| Output | Criterion | Result: Pass/Partial/Fail/Not assessable | Visible evidence |
|---|---|---|---|
| Image 1 | ... | ... | ... |
```

Keep acceptance criteria concise and testable. Do not use abstract criteria such as
"beautiful" or "perfect" without translating the user's intent into observable
features. Emotional criteria may be assessed through visible expression, gesture,
posture, and staging, while acknowledging when the evidence is interpretive.

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

### Prompt-first image-editing records

For a user-requested change to an existing image, default to **prompt-first
reconstruction**: locate the successful authored prompt that produced the target,
use it as the text baseline, make only the requested change, and generate a new
image from the revised prompt. Do not describe this as a direct edit of the
source image.

Each such attempt must record:
- The successful baseline prompt path/attempt and why it qualifies.
- The requested delta, preserved details, changed details, and exclusions.
- Whether the source image was attached. Prompt-first reconstruction does not
  require source-image attachment; an attached image is optional visual
  comparison/reference, not the editing mechanism.
- Operation type as **fresh generation/reconstruction**, unless a direct edit
  was actually performed and source linkage verified.
- The output's comparison against the successful baseline and requested change.

If the successful baseline prompt cannot be recovered, disclose the missing
source and do not fabricate prompt text. Direct source-image editing is a
secondary method, used only when explicitly requested or when reconstruction is
materially inadequate and the exact source image can be attached through a
supported mechanism. Verify source linkage before calling it a confirmed edit.

- Deliver generated images in the conversation.
- Store new retained non-novel/day drawing outputs in `drawings/YYYY-MM-DD/images/` using `attempt-XX.webp` (multiple outputs: `attempt-XX-01.webp`, etc.); link exact verified assets from the attempt note and daily README. Existing image assets are not migrated. Non-novel reference/source images remain under `images/`; novel-scene illustration binaries remain in the novel's central `assets/illustrations/[ARC-ID]/[SCN-ID]/` library. New uploads for permanent reference/novel destinations enter through `images/takeout/` and its hand-off.
- Never claim a fresh generation was an edit of the original.
- Never claim a reference image was supplied unless the tool call actually included that reference.
- Preserve source-image identity and distinguish an edit from a newly generated composition.
- Use a repository reference image from `images/` or a novel's central `assets/illustrations/[ARC-ID]/[SCN-ID]/` library, or from an image the user supplies directly in the current conversation.
- If an image edit fails, state that the image was not modified; do not imply the source image changed.

### Daily attempt ledger

Do not create a separate cross-session success catalogue. For each
non-novel drawing date, maintain `drawings/YYYY-MM-DD/README.md` as the
navigation ledger for that date's attempts. It must contain one contiguous
Markdown table with exactly six fields:

1. **Attempt / prompt:** attempt number or stable ID, concise descriptive title,
   and direct link to the complete attempt record.
2. **Session / brief:** session ID or name and direct link to the opening brief.
   State explicitly when no separate brief was created.
3. **Series / baseline lineage:** verified primary series ID/name and theme,
   plus the parent attempt or successful baseline when known. Use
   `legacy/unassigned` or `not established` when membership is uncertain.
4. **Execution outcome:** what actually happened and whether the result met
   the defining acceptance criteria. Distinguish generated, edited with
   verified source linkage, rejected, blocked, pending, superseded, and
   unconfirmed outcomes. A prompt approved for generation is not a successful
   image result.
5. **User approval / output evidence:** separate the user's explicit approval
   from the assistant's visual assessment. State whether the image was delivered
   only in conversation, no output was returned, storage is unverified, or
   approval was not recorded.
6. **Image:** link every generated image output once its exact repository asset
   is uploaded and verified, regardless of user approval or prompt compliance.
   Include partial, off-target, superseded, and unapproved outputs. Approval is
   recorded separately in field 5. If an image was generated but is not yet
   uploaded, write `Waiting for image upload`. Use `—` only when no image was
   returned or generated.

Include every attempt, not only successful ones, and keep the rows in
chronological order. The table is a compact navigation/status summary. Each
linked attempt record remains authoritative for the exact prompt, source and
operation metadata, acceptance criteria, visual assessment, user approval,
output identity, and provenance. Never infer missing lineage, approval, or
storage details. When a field is unknown, say so explicitly.

After each attempt is finalized, update its attempt record first, then update
the matching daily README row from the verified record. Keep exactly one row
per attempt. When a user approves an image, record that approval in both the
attempt record and the table's approval/output field without disguising a
different execution outcome. When an approved image is renamed or moved,
update the exact asset link in the attempt record and daily README.

For a named novel scene, maintain the complete chronological prompt and output
history in the scene-local illustration records. Do not create a duplicate
daily prompt history or cross-session success catalogue for that scene. The
scene record remains authoritative for prompt lineage, outcomes, approval,
and image links.

Determine the latest successful text baseline by reviewing finalized attempt
records within the active series or exact artwork thread. The daily README
helps locate those records but does not establish success, series membership,
or visual authority.
 
### Session-local image asset handling and provenance

When the user asks to retain generated or uploaded images, or when the active
session workflow requires keeping a source asset:

1. Give each retained image a clear, descriptive filename based on its visible
   content. Preserve the original bytes; do not overwrite a full-resolution
   original with a thumbnail.
2. Keep new retained non-novel/day drawing outputs under the dated prompt
   folder's `images/` subdirectory, using `attempt-XX.webp` or numbered
   multiple-output suffixes, and link them from the attempt note and daily README
   when provenance is verified. Do not migrate existing image assets. Keep
   non-novel reference/source images under `images/` and novel-scene illustration
   binaries under `novels/[Novel-ID]/assets/illustrations/[ARC-ID]/[SCN-ID]/`
   when a supported repository binary-upload route is available. New uploads
   intended for permanent reference/novel destinations first enter
   `images/takeout/` and are routed through its hand-off. Verify the exact
   final path and blob identity before claiming repository storage.
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
3. **Preserve the original image exactly.** The default is rename-only:
   do not convert, recompress, resize, crop, rotate, filter, retouch, strip
   metadata, or create derivatives. The user has explicitly authorized a
   repository intake exception: images placed in `images/takeout/` and listed
   in a ready `HANDOFF.yml` may be moved/renamed to their declared master path
   and converted to a separate WebP by the existing GitHub Action. Original
   bytes, format, resolution, metadata, and visual content must remain
   unchanged. Do not perform the conversion or relocation manually.
4. Record the exact path, stable file/Library ID, source generation ID when
   known, original name, dimensions, byte size, checksum where available, and
   session-specific role in the session brief or attempt record.
5. For every generated non-novel drawing output retained in the repository,
   include its attempt number in the `HANDOFF.yml` item as `attempt: NN` and
   set the destination to `drawings/YYYY-MM-DD/images`. Do this whether the
   user approved the result, rejected it, or has not reviewed it; user approval
   does not control image linking. After conversion and relocation succeed,
   the takeout processor automatically adds the verified WebP link to the
   attempt record and matching README Image cell. Do not add a global
   reference-index link. Items without attempt metadata do not modify prompt
   records or daily ledgers.
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

When an image is already stored in its permanent `images/` or `novel/` location under an opaque filename, rename the existing Git tree path while reusing its exact blob SHA. Remove the old path in the same tree update and verify the new path, absence of the old path, identical blob SHA, and identical byte size.

For new user uploads intended for repository retention, use the universal flat intake `images/takeout/`. Inspect the actual image and prepare `images/takeout/HANDOFF.yml` with its exact incoming filename, descriptive title, optional stable asset ID, and destination directory. For a session output associated with a non-novel drawing attempt, also include `attempt: NN` in that item and target exactly `drawings/YYYY-MM-DD/images`. Do not manually rename or relocate the incoming file. The existing Action derives the permanent master filename from the optional ID and normalized title slug and preserves the original bytes. It stages each WebP under `images/takeout/webp/[batch-id]/attempt-NNN/`, appending `.webp` to the exact incoming filename, then verifies and moves the derivative beside the master. Novel illustration binaries belong in `novels/[Novel-ID]/assets/illustrations/[ARC-ID]/[SCN-ID]/`; retained non-novel assets use a destination under `images/`.

Every attempt is archived under `images/takeout/history/[batch-id]/attempt-NNN/` with the original hand-off, `conversion-report.csv`, and `verification-report.md`. The CSV records both staging and final WebP paths. On failure, original uploads and the ready hand-off remain in the intake and successfully converted WebPs remain in the failed attempt's staging folder; a retry uses a fresh attempt number. On success, staged WebPs move to their permanent destinations and the empty successful staging attempt folder is removed. The Action does not clear the active hand-off unless the entire batch passes verification. Read back the archived reports and final asset paths before claiming success.

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

### Active-session closeout reminder

While a drawing session is Active or Paused, append a brief, unobtrusive
reminder at the end of each response that continues or discusses that session,
stating that it remains open and the user can say `end session` for formal
closeout. This is a reminder only: it must not interrupt drawing, require a
reply, or pressure the user to close. Once the user invokes `end session`,
suppress the reminder during closeout. If closeout cannot be completed and the
session remains open, resume reminders in later responses that continue or
discuss that session. Stop reminding once the session is Closed. The reminder
does not itself trigger closeout.

Until the cue is received:
- Keep the drawing session marked `Active` or `Paused`; never mark it
  `Closed` merely because work has stopped temporarily.
- Preserve its current brief, prompt lineage, attempt outcomes, unresolved
  criteria, and next step.
- A new drawing session may begin with a new brief, but this does not close the
  preceding session. Mark the preceding `Active` session `Paused` and the new
  session `Active`.
- When a paused session is resumed, make it `Active` and pause any other
  currently `Active` session.

When the user sends `end session`, close the current drawing session under
discussion, whether its status is `Active` or `Paused`, without asking for a
second confirmation. If multiple non-closed sessions could reasonably be the
target, ask one concise question to identify the session before changing any
record; this is target clarification, not a second approval:

1. Stop further image generation/editing for that session.
2. Verify the opening brief and every amendment, and confirm all attempts are
   recorded in their authoritative locations. For non-novel work, verify that
   the daily `README.md` indexes every attempt in its single contiguous table.
   Reconcile the success-only prompt index when an attempt's finalized
   classification or approved-output listing requires an update. For a named
   novel scene, verify the scene-local illustration prompt/attempt records and
   their links instead of creating a duplicate daily log.
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
8. Read back all changed records, including the applicable daily index,
   daily README and attempt records, scene-local records, and session summary/handoff. Verify
   their links and status. If archival verification fails, report the exact
   gap and do not claim a fully verified closeout.

The session brief status remains `Closed` even when unresolved requirements
remain. Record those unresolved items in the closeout summary/handoff; closure
records the session's state and does not imply that every image succeeded.

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

Original PNG/JPEG files are permanent masters. WebP files are separate
delivery derivatives, never replacements. New retained uploads use the shared
flat intake at `images/takeout/` and the structured `HANDOFF.yml`.

- Incoming filenames may be arbitrary. Inspect each image and prepare a hand-off
  item with the exact source filename, descriptive title, optional stable ID,
  and destination directory. The Action does not infer visual content or
  project membership. The optional `attempt: NN` field is the explicit
  prompt-to-output association used for automatic Markdown cross-linking.
- The existing workflow on branch `gpt` calls
  `images/scripts/process_takeout.py`. It supports static PNG, JPG, and JPEG.
  APNG and other unsupported formats fail the batch; animated content is never
  silently flattened.
- PNG uses exact lossless encoding
  (`-lossless -q 100 -m 6 -exact`); JPEG uses high-quality lossy encoding
  (`-preset picture -q 92 -m 6 -sharp_yuv`). ICC profiles are copied. EXIF/XMP
  metadata remain in the unchanged original and are not copied to WebP.
- The original is moved and renamed to the hand-off-derived master path without
  changing its bytes or format. The WebP derivative is stored beside it.
  Novel illustration assets use
  `novels/[Novel-ID]/assets/illustrations/[ARC-ID]/[SCN-ID]/`; other retained
  assets use their declared directory under `images/`.
- The processor validates the complete batch, converts every image into
  persistent staging at `images/takeout/webp/[batch-id]/attempt-NNN/`, and
  only then relocates any original. Each staged filename appends `.webp` to
  the exact incoming filename. It rejects unlisted uploads, missing sources,
  destination collisions, symlinks, and invalid paths. It verifies
  source/master SHA-256 equality, WebP signatures, and final WebP hashes.
- When `attempt: NN` is present for a destination under
  `drawings/YYYY-MM-DD/images`, the processor verifies the corresponding
  attempt record and six-column daily README, then writes the verified WebP
  link into both for every generated image, including partial, off-target,
  superseded, and unapproved results. Approval is not a linking condition.
  Multiple uploads may point to the same attempt. The GitHub Action commits
  these Markdown changes together with the image masters,
  derivatives, and takeout reports. Items without `attempt` are not linked to
  prompt records.
- Every successful or failed attempt is preserved under
  `images/takeout/history/[batch-id]/attempt-NNN/` with the hand-off snapshot,
  `conversion-report.csv`, and `verification-report.md`. The CSV records
  source, staging, and final paths, sizes, size difference, encoder
  profile/version, SHA-256 values, result, and errors. Both `history/` and
  `webp/` are reserved and excluded from intake.
- On failure, original uploads and the ready hand-off remain available and
  successfully converted WebPs remain in that failed attempt's staging
  folder. Retries use a new attempt directory. On success, staged WebPs move
  to final destinations and the now-empty successful staging directory is
  removed. The active hand-off is reset to empty only after every original and
  WebP has been relocated and verified and both reports have been archived.
  Never claim a successful Action run without observing its result and
  reading back the published assets and reports.
