# Image Reference and Editing Protocol

## 1. Identify the reference's role

Determine whether the image is an identity reference, composition reference,
style reference, or exact edit source. The user must assign that role within
the active drawing session. A reference from an earlier session is not active
by default, even if it was previously approved or stored. A reference can serve
several roles, but establish priorities.

- **Identity:** preserve faces, hair, glasses, and stable visual features.
- **Composition:** preserve subject placement, body geometry, camera view, and
  spatial relationships.
- **Style:** transfer brushwork, palette, line, or print texture without
  importing unrelated subject matter.
- **Edit source:** modify that exact image and keep all non-target properties.

Do not confuse "use this as inspiration" with "edit this exact image."

## 2. Attach the actual image

- Use the currently uploaded image when the user says "this image", "the one I
  uploaded", or equivalent, and retain the role assigned in the current session
  brief.
- Do not silently substitute an older generated image or repository asset.
- The active session-opening brief controls visual direction. It overrides
  conflicting features in historical prompts and images.
- Use the image tool's supported reference attachment mechanism. A filename or
  image ID written in prose is not an attachment.
- If a reference ID or asset pointer is required, use the exact pointer exposed
  by the current conversation or tool result.
- Never invent an image ID or claim that a reference was attached when it was not.

## 3. Write a constrained edit prompt

Lead with the operation: "Edit the exact supplied image", "This is a style-only
transformation", or "Change only [property]". Then define locked properties.

For composition-sensitive images, lock subjects, faces, body positions, pose
direction, contact points, hand ownership and order, clothing, colors, objects,
lighting, camera angle, and crop only as specified by the active session brief
or explicit edit request. Do not import old-session locks. Keep the requested
change singular.

## 4. Verify the operation

Inspect both the rendered result and returned metadata when available.

- If parent/source linkage is confirmed and the requested change is visible,
  record a confirmed edit.
- If metadata says no edit or no parent, do not claim source continuity even if
  the new image resembles it.
- If metadata is unavailable, state that source linkage is unconfirmed.
- A good-looking output is not automatically a successful edit.

Classify outcomes precisely: confirmed edit, partial edit, fresh generation,
fresh generation with missed target, rejected, or technical failure.

## 5. Stop repeating failed context-only calls

If several attempts revert to the same wrong pose or discard the source image:
1. Stop repeating near-identical prompts.
2. Check whether the image was actually attached to the tool call.
3. Reduce the requested change to one operation.
4. Prefer a localized edit or explicitly source-linked style transfer when supported.
5. If the tool cannot retain the source, tell the user and preserve the best
   partial image instead of claiming success.

## 6. Prompt-before-generation archive

Follow `skills/session-archiving/SKILL.md` for every attempt:
- create or retrieve the current session-opening brief and verify its exact path;
- for non-novel work, commit the authored prompt in its dated `prompts/YYYY-MM-DD/` attempt note; for a named novel scene, commit it in the authoritative scene-local illustration prompt record under `novel/`;
- treat the session brief as the visual authority; use the most recent successful prompt in the explicitly active series only as a compatible text baseline, never as an authority over the current brief;
- later failed, rejected, partial, or missed-target prompts are diagnostic evidence only, never the baseline;
- record the session ID/brief path, series ID/theme when explicitly active, selected baseline provenance, operation type, and the actual source reference attached;
- verify the pre-attempt commit;
- after the call, record the actual result, image ID, user assessment, and mismatch;
- do not store image binaries in Git unless requested and technically completed.
