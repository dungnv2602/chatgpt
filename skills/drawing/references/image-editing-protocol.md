# Image Reference and Editing Protocol

## 1. Prompt-first editing: locate the successful baseline

When the user requests an edit to an existing image, the primary source of
continuity is the **successful authored prompt that produced the target image**,
not the image binary itself. Default to controlled prompt reconstruction:

- Locate the exact successful prompt in the authoritative attempt record.
- Verify that it produced the target image or that the user approved that
  specific attempt as successful for the intended purpose.
- Recover the complete authored prompt. If it is unavailable, disclose the gap
  do not invent, reconstruct from memory, or substitute an unrelated prompt.
- Use the successful prompt as the baseline for rebuilding the image. Preserve
  its established visual content and details unless the user requests a change.
- Revise only the requested element, keeping unrequested elements unchanged.
- Generate a fresh reconstruction from the revised prompt and assess it against
  the baseline and the requested change.

The source image may be used as a secondary visual reference when helpful and
when the user assigns that role. It is not the default editing mechanism.

## 2. Optional image-reference roles

If an image is deliberately included, establish its role and priority:

- **Identity:** preserve faces, hair, glasses, and stable visual features.
- **Composition:** preserve subject placement, body geometry, camera view, and
  spatial relationships.
- **Style:** transfer brushwork, palette, line, or print texture without
  importing unrelated subject matter.
- **Visual comparison:** use the image to compare the reconstruction with the
  approved result.
- **Direct edit source (secondary workflow):** modify that exact image only when
  the user explicitly requests direct editing or reconstruction is inadequate,
  and when the actual source can be attached through the supported mechanism.

Do not confuse "use this as inspiration" with "edit this exact image." Prompt-first
reconstruction does not require an image attachment.

## 3. Revise the proven prompt, not the image

Lead with the single requested change. Use the verified successful authored prompt
as the baseline, then revise it minimally.

- **Preserve:** every unrequested visual element, including identity/face,
  hairstyle, wardrobe, pose, body geometry, composition, camera, lighting,
  background, environment, mood, and rendering style, as applicable to the
  baseline.
- **Change:** only the element the user requested.
- **Exclude:** unwanted additions, text, boxes, artifacts, or other details
  specifically identified by the user or present only in unsuccessful attempts.
- Do not add decorative improvements, substitute clothing, alter faces, or change
  scenes to solve an unrelated issue.
- Avoid wholesale rewording of a successful prompt. Unnecessary prompt drift can
  change more than the requested target.

For a style-only change, revise only the rendering treatment and preserve all
scene and subject details.

## 4. Optional direct-edit verification

Direct editing is a secondary method, not the default. Use it only when the user
explicitly requests a direct image edit or when prompt reconstruction is
materially inadequate and the actual image source is accessible through the
supported mechanism.

- Attach the exact image source. A filename or image ID in text is not enough.
- Inspect the returned operation and parent/source metadata.
- If source linkage is confirmed and the requested change is visible, classify
  it as a confirmed edit.
- If metadata shows no source or parent, do not claim source continuity even if
  the output resembles the original.
- If metadata is unavailable, state that source linkage is unconfirmed.
- A successful-looking output is not automatically a confirmed edit.

## 5. Recovery when prompt reconstruction misses

If the revised prompt reconstruction repeatedly misses the requested detail:

1. Stop repeating near-identical prompt revisions.
2. Recheck the exact successful baseline and inspect assistant-added drift.
3. Reduce the revision to the requested change only.
4. If prompt reconstruction is materially inadequate, consider a direct edit as
   a secondary approach only when the user explicitly requests it or its
   limitations have been explained and the exact source can be attached.
5. If neither method is reliable, explain the limitation and preserve the
   best successful baseline rather than mislabeling the result.

# 6. Prompt-before-generation archive

Follow `skills/session-archiving/SKILL.md` for every attempt:
- create or retrieve the current session-opening brief and verify its exact path
- for non-novel work, commit the authored prompt in its dated `prompts/YYYY-MM-DD/` attempt note. For a named novel scene, commit it in the authoritative scene-local illustration prompt record under `novels/[Novel-ID]/[Arc-Folder]/[Scene-Folder]/illustrations/`
- treat the session brief as the visual authority. Use the most recent successful prompt in the explicitly active series only as a compatible text baseline, never as an authority over the current brief
- later failed, rejected, partial, or missed-target prompts are diagnostic evidence only, never the baseline
- record the session ID/brief path, series ID/theme when explicitly active, selected baseline provenance, operation type, and the actual source reference attached
- derive normally three to five observable acceptance criteria from the brief and mark critical criteria
- record the prompt difference: baseline, preserved details, changed details, and excluded/not-carried-forward details
- verify the pre-attempt commit
- after the call, record the actual result, image ID, user assessment, and mismatch
- do not store image binaries in Git unless requested and technically completed.
