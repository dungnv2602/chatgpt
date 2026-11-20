# Archive Records and Drawing-Prompt Procedures

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
**Companion files:** Summary file: `drawings/YYYY-MM-DD-summary.md` · Image-prompt history: non-novel dated prompt record. For novel scenes, link the scene-local prompt record instead.

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

Every distinct drawing session starts with a user-defined visual direction.
This opening brief is the sole creative authority for that session. It applies to day-drawing and novel-illustration sessions. No repository-wide image index, historical prompt, previous portrait, character sheet, stored image, or old project convention dictates the new session. Use one only when the user explicitly adopts it.

- For non-novels/day drawing, archive the brief as
  `drawings/YYYY-MM-DD/session-[NN]-brief.md`.
- For a named novel scene, archive it as
  `novels/[Novel-ID]/[Arc-ID]/[Scene-ID]/illustrations/session-[YYYY-MM-DD]-[NN]-brief.md`.
- Create and commit the brief before the first image prompt for that session.
  Read it back and verify it.
- Preserve the user's opening direction faithfully. Record specified, locked,
  variable, excluded, and open details. Mark unspecified features as open.
  Never invent constraints.
- Append later explicit user corrections or refinements as dated amendments
  in the same brief. Preserve the original opening brief. Do not silently
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
wording in the first section. The structured fields summarize it and must not
invent detail.

```markdown
# Drawing Session Brief

**Session ID:** ...
**Session type:** Day drawing / Novel illustration
**Project or novel scene:** ...
**Created:** YYYY-MM-DD
**Status:** Active / Paused / Closed (new sessions start Active)

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
user's request is compact. This is a record of the user's direction, not a
questionnaire that must be completed before work.

### Session status and transitions

- Create every new drawing-session brief with status `Active`.
- Keep at most one drawing session `Active` in the current workflow context.
  When a new distinct session starts while another session is still open, mark
  the previous `Active` session `Paused` and the new session `Active`.
- When resuming a `Paused` session, mark it `Active` and mark any other
  currently `Active` session `Paused`.
- `Paused` means temporarily inactive, not closed. Never change a session to
  `Closed` without the user's closeout cue.
- While the session being discussed is `Active` or `Paused`, include the
  closeout reminder at the end of each response that continues or discusses
  that drawing session. The reminder is not a scheduled or background
  notification. It appears in the conversation response.

For a novel illustration, the user selects one narrative-fidelity mode in the
opening brief:
- **Text-faithful:** Depict the stated events, relationships, chronology, and
  scene facts closely. Do not invent or contradict manuscript facts. Creative
  choices are limited to details the source and brief leave open.
- **Interpretive:** Preserve established story facts, character intentions, and the scene's emotional meaning. The assistant may choose visual staging, gestures, framing, and other unspecified details.
- **Adaptive:** Deliberately reinterpret or depart from literal staging while
  preserving the story elements the user identifies as non-negotiable. State
  the permitted adaptation scope in the brief.

Do not choose a fidelity mode on the user's behalf when the distinction would
materially change the illustration. Ask one focused question if the brief and
context do not resolve it. Day-drawing sessions may mark this field
`Not applicable` unless the user wants a source-faithfulness constraint.

### Daily folder and one-note-per-attempt format for non-novel drawing work

For non-novel drawing work, organize image prompts by date. Each calendar day is a folder under `drawings/`. Each image-generation or image-edit attempt is its own Markdown note.

**Exception for novel scenes:** The scene-local prompt record under `novels/[Novel-ID]/[Arc-ID]/[Scene-ID]/illustrations/` is authoritative. Keep that attempt there. Do not duplicate it in the daily `drawings/` folder.

```text
drawings/
  YYYY-MM-DD/
    README.md              # daily index and status overview
    session-01-brief.md    # authoritative direction for this drawing session
    attempt-01.md          # one complete attempt record
    attempt-02.md
    ...
```

- Use zero-padded sequential filenames (`attempt-01.md`, `attempt-02.md`, ...), with one attempt per file. Never append a second attempt to an existing attempt note.
- `README.md` is the daily index: list attempts in order, link each note and its session brief, and show its current outcome/status. Update it whenever an attempt is added or its outcome changes.
- **README table format is mandatory:** Use one continuous Markdown table for the day's entire attempt index. Include one header row and consistent columns. The minimum columns are `Attempt`, `Prompt note`, `Session brief`, `Primary series / membership`, and `Status / outcome`.
  Include every attempt exactly once in that table. Use a stable series ID or name. Write `standalone/unassigned` when no series is established. Do not add a second table or place attempt rows outside the table. Keep rows in ascending attempt-number order.
- **Keep table rows physically contiguous:** Do not insert blank lines between the header, separator, or attempt rows. Many renderers treat a blank line as the end of a Markdown table. This can make the newest attempt appear as a separate block.
  When appending an attempt, place its row directly after the previous row. When revising a status, edit the existing row. Do not move it outside the table or create a second table.
- **Verify before committing:** Read back the complete daily `README.md`. Verify that it contains one attempt-index table, one header row, and one separator row. Verify that every numbered attempt appears exactly once in ascending order. Verify that no blank line interrupts the table. Verify that the final attempt row belongs to the same table. Do not mark the index update complete until the table meets all listed conditions.
- **Status accuracy:** distinguish `not approved / not generated`, `approved / pending generation`, `generated successfully`, `generated with mismatch`, `rejected / no image returned`, and `technical failure`. If an attempt has multiple runs, preserve the sequence in the status cell (for example, an earlier image returned but a later retry was rejected). Do not overwrite history with only the latest or earlier outcome. A user declining approval must never be represented as pending approval.
- Each attempt note contains all required fields below, the exact authored prompt, and its final outcome when known. Keep the full record self-contained.
- Session-level conversation-integrity and summary records remain at `drawings/YYYY-MM-DD-conversation-integrity.md` and `drawings/YYYY-MM-DD-summary.md` unless the user changes that convention.
- Existing legacy `YYYY-MM-DD-image-prompts.md` files remain historical records. Do not delete or rewrite them during adoption unless the user explicitly requests migration. For a day already in progress, create the daily folder and separate notes for its attempts. Preserve the legacy file as-is.

### Mandatory pre-attempt rule

**Commit the session brief and authored prompt in their authoritative locations before the first image-generation or image-edit attempt.**

For non-novel work, use the session brief and attempt notes under `drawings/YYYY-MM-DD/`. For a named novel scene, use the session brief and illustration prompt records under `novels/[Novel-ID]/[Arc-ID]/[Scene-ID]/illustrations/`.

This rule applies to successful, exploratory, and revision attempts. Never generate first and archive later. Never duplicate a novel-scene prompt in the root `drawings/` history.

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
   artwork/thread. If no relevant success exists, use the current session
   brief and explicit constraints. Do not borrow from an unrelated series. For a
   new subseries, record any inherited parent-series seed and branch point.
5. Change as little as practical so the next attempt tests a clear hypothesis.
6. Append a new attempt with a sequential number, required series metadata,
   baseline provenance, and a pending outcome.
7. Commit the updated file on the working branch.
8. Verify the committed content by reading the exact prompt-record path.
9. Only then invoke image generation or editing.

### Required fields for each attempt

Record:
- Sequential attempt number and a short descriptive title.
- Status before the call: pending.
- **Drawing session ID and session-brief path.** Mandatory for every attempt.
- **Opening direction authority:** link the active session brief and verify it controls visual direction. Do not treat any prior index, prompt, or image as a replacement.
- **Primary series ID/name and theme spine.** Record a series only when the current session brief explicitly continues/adopts it. Otherwise record `standalone/unassigned`. Do not guess. Record secondary series only for a deliberate crossover.
- **Membership role:** series seed, continuation, subseries, branch, crossover, standalone, or provisional. For a branch, record the parent series and branch point.
- **Continuity anchors and permitted variation** relevant to this attempt, taken from the current session brief. State which user-locked details must remain unchanged. Do not import locks from an older session.
- **Prompt baseline provenance:** Record the exact path and attempt, or the scene-local record, for the most recent successful prompt in the primary series. If the work is not a series, use the exact artwork thread. Record its outcome and why it qualifies.
  If the next operation needs a full-scene prompt, verify the newest success's scope. If it is only a localized edit or style-only prompt, record the newest successful full-generation prompt from that series. Use it as the compatible text skeleton and explain why.
  If no baseline exists, state that fact. For a new branch, record the inherited seed and source.
- **Latest-attempt diagnostic reference:** Link the newest later attempt you inspected when it differs from the selected successful baseline. State what you carried forward and what you did not.
- **Acceptance criteria:** normally three to five observable requirements derived from the active brief for this image. Mark critical criteria and define the visible evidence for each. Record `Not applicable` only when no meaningful visual criterion can be derived.
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
- **Rejected. No image returned.**
- **Failed for a technical reason.**
- **Unconfirmed.**

Do not mark an image attempt successful merely because an image was returned. Inspect whether it followed the user's key instructions and the active session brief. Record what worked, what failed, and one useful next-step lesson.

When one tool call returns multiple images, record each output separately. Include its image or generation ID, or its stored path. State whether it meets the active session brief and whether the user approved it as a keeper. Preserve mixed outcomes. One successful output does not make every image in the batch successful.

The prompt/result pair may qualify as a successful prompt baseline when one output is explicitly judged successful for its intended purpose. The prompt-to-output link must be reliable.

Use only individually approved outputs as visual references. Use them in future sessions only when the user selects them.

Keep two judgements distinct:
- **Prompt/result success:** The prompt links to an output that meets the defining requirements. The user may also explicitly accept the attempt's result as successful for its intended purpose. This can qualify the exact prompt as a future series baseline.
- **User-approved visual keeper:** The user approves the image as a visual asset. This approval does not verify an uncertain or unsuccessful originating prompt.
  When the prompt link is known and the user accepts the attempt as successful, record the output and its baseline eligibility. Preserve earlier assessment history.

A failed, rejected, partial, or missed-target prompt is never the default text baseline. If no later successful prompt exists, return to the most recent success in the same series or artwork thread. Apply only user-requested changes from later attempts.

### Image handling

### Prompt-first image-editing records

For a user-requested change to an existing image, default to **prompt-first
reconstruction**. Locate the successful authored prompt that produced the target.
Use it as the text baseline. Make only the requested change. Generate a new
image from the revised prompt. Do not describe this as a direct edit of the
source image.

Each such attempt must record:
- The successful baseline prompt path/attempt and why it qualifies.
- The requested delta, preserved details, changed details, and exclusions.
- Whether the source image was attached. Prompt-first reconstruction does not
  require source-image attachment. An attached image is optional visual
  comparison/reference, not the editing mechanism.
- Operation type as **fresh generation/reconstruction**, unless a direct edit
  was actually performed and source linkage verified.
- The output's comparison against the successful baseline and requested change.

If the successful baseline prompt cannot be recovered, disclose the missing source. Do not fabricate prompt text. Use direct source-image editing only when explicitly requested. Also use it when reconstruction is materially inadequate and you can attach the exact source image through a supported mechanism. Verify source linkage before calling it a confirmed edit.

- Deliver generated images in the conversation.
- Store new retained non-novels/day drawing outputs in `drawings/YYYY-MM-DD/images/` using `attempt-XX.webp` (multiple outputs: `attempt-XX-01.webp`, etc.). Link exact verified assets from the attempt note and daily README. Existing image assets are not migrated. Non-novel reference/source images remain under `images/`. Novel-scene illustration binaries remain in the novel's central `assets/illustrations/[ARC-ID]/[SCN-ID]/` library. New uploads for permanent reference/novel destinations enter through `images/takeout/` and its hand-off.
- Never claim a fresh generation was an edit of the original.
- Never claim a reference image was supplied unless the tool call actually included that reference.
- Preserve source-image identity and distinguish an edit from a newly generated composition.
- Use a repository reference image from `images/` or a novel's central `assets/illustrations/[ARC-ID]/[SCN-ID]/` library, or from an image the user supplies directly in the current conversation.
- If an image edit fails, state that the image was not modified. Do not imply the source image changed.

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
   returned or generated. Use `Not verified` when the tool outcome is
   unconfirmed and no attempt-specific image can be attributed.

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
   content. Preserve the original bytes. Do not overwrite a full-resolution
   original with a thumbnail.
2. Keep new retained non-novel/day-drawing outputs in the dated prompt folder's `images/` subdirectory. Use `attempt-XX.webp` or numbered suffixes for multiple outputs. Link each output from the attempt note and daily README when provenance is verified. Do not migrate existing image assets. Keep non-novel reference/source images under `images/`. Keep novel-scene illustration binaries under `novels/[Novel-ID]/assets/illustrations/[ARC-ID]/[SCN-ID]/` when a supported repository upload route is available. Route new uploads for permanent reference or novel destinations through `images/takeout/`. Verify the exact final path and blob identity before claiming repository storage.
3. If you cannot transfer the binary to GitHub, retain it in the Files Library only when the user requested retention and that storage is available. Record its exact Library path, stable file ID, source generation ID, original artifact name, dimensions, byte count, and checksum where available. Put these details in the current session brief or attempt record, not in a global visual reference index.
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
3. **Preserve the original image exactly.** The default is rename-only. Do not convert, recompress, resize, crop, rotate, filter, retouch, strip metadata, or create derivatives. The user has explicitly authorized one repository intake exception. Images placed in `images/takeout/` and listed in a ready `HANDOFF.yml` may move to their declared master path. The existing GitHub Action converts them to a separate WebP. Keep the original bytes, format, resolution, metadata, and visual content unchanged. Do not convert or relocate the file manually.
4. Record the exact path, stable file or Library ID, and source generation ID when known. Also record the original name, dimensions, byte size, checksum where available, and session-specific role in the session brief or attempt record.
5. For every generated non-novel drawing output retained in the repository,
   include its attempt number in the `HANDOFF.yml` item as `attempt: NN` and
   set the destination to `drawings/YYYY-MM-DD/images`. Do this whether the
   user approved the result, rejected it, or has not reviewed it. User approval
   does not control image linking. After conversion and relocation succeed,
   the takeout processor automatically adds the verified WebP link to the
   attempt record and matching README Image cell. Do not add a global
   reference-index link. Items without attempt metadata do not change prompt
   records or daily ledgers.
6. In conversation-integrity records, record the user's instruction/approval
   and exact storage or rename actions as tool events. Preserve historical
   facts, but do not treat them as current visual direction.
7. Verify the renamed asset through Files metadata and read back every updated
   GitHub Markdown file. Never claim a Library URL or GitHub storage unless
   verified.

Do not finish a session archive while a requested keeper image has an opaque temporary filename. Also add direct links to its session brief and successful prompt record.

### When an opaque image cannot be visually inspected

If an image is present in `images/` but its binary cannot be viewed, do not invent a subject description. If its name contains a reliable timestamp, you may rename it to a neutral timestamp-based filename. Preserve the original extension (for example, `archive-photo-YYYY-MM-DD-HHMMSSZ.jpg`).

Record that you did not inspect the pixels. State that the filename is based on time, not image content. If no reliable timestamp or identifying metadata exists, leave the file unchanged until its visual content is available. In either case, preserve the exact Git blob SHA and byte size.

### Renaming image files already tracked in GitHub

When an image is already stored in its permanent `images/` or `novels/` location under an opaque filename, rename its Git tree path. Reuse its exact blob SHA.

Delete the old path in the same tree update. Verify the new path and verify that the old path is absent. Verify that the blob SHA and byte size remain identical.

For new uploads that need repository retention, use the universal flat intake `images/takeout/`. Inspect the image. Prepare `images/takeout/HANDOFF.yml` with the exact incoming filename, descriptive title, optional stable asset ID, and destination directory.

For a non-novel drawing attempt, include `attempt: NN` in the hand-off item. Set its destination to `drawings/YYYY-MM-DD/images`. Do not rename or move the uploaded file manually.

The Action derives the master filename from the optional ID and normalized title slug. It preserves the original bytes. It stages each WebP under `images/takeout/webp/[batch-id]/attempt-NNN/`. The staged name appends `.webp` to the exact incoming filename. The Action verifies each derivative and moves it beside the master.

Novel illustration binaries belong in `novels/[Novel-ID]/assets/illustrations/[ARC-ID]/[SCN-ID]/`. Store other retained non-novel assets under `images/`.

Archive every attempt under `images/takeout/history/[batch-id]/attempt-NNN/`. Include the original hand-off, `conversion-report.csv`, and `verification-report.md`. The CSV records staging and final WebP paths.

On failure, keep the original uploads and ready hand-off in the intake. Keep successfully converted WebPs in that attempt's staging folder. Use a new attempt number for each retry.

On success, move staged WebPs to their permanent destinations. Delete the empty staging folder. The Action clears the active hand-off only after the full batch passes verification. Read back the reports and final asset paths before you claim success.



## Technical documentation standard

This reference contains operational archive procedures. Apply Strict mode from the repository [ASD-STE100 policy](../../asd-ste100/references/repository-writing-policy.md) when you revise it. Preserve transcript integrity, prompt provenance, user approval, and archive requirements.
