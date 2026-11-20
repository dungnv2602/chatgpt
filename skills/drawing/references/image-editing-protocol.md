# Image Reference and Editing Protocol

## 1. Prompt-first editing: locate the successful baseline

For an image edit, use the **successful authored prompt that produced the target image** as the primary continuity source. Do not use the image binary as the primary source.

Use controlled prompt reconstruction by default:

- Locate the exact successful prompt in the authoritative attempt record.
- Check that it produced the target image. Alternatively, check that the user approved that specific attempt for its intended purpose.
- Recover the complete authored prompt. If it is unavailable, disclose the gap. Do not invent it, reconstruct it from memory, or substitute an unrelated prompt.
- Use the successful prompt as the baseline for rebuilding the image. Preserve its established visual content unless the user requests a change.
- Revise only the requested element. Keep all unrequested elements unchanged.
- Generate a fresh reconstruction from the revised prompt. Assess it against the baseline and the requested change.

The source image may serve as a secondary visual reference. Use it only when helpful and when the user assigns that role. It is not the default editing method.

## 2. Optional image-reference roles

When the user includes an image, establish its role and priority:

- **Identity:** preserve faces, hair, glasses, and stable visual features.
- **Composition:** preserve subject placement, body geometry, camera view, and spatial relationships.
- **Style:** transfer brushwork, palette, line, or print texture. Do not import unrelated subject matter.
- **Visual comparison:** compare the reconstruction with the approved result.
- **Direct edit source (secondary workflow):** Modify that exact image only when the user explicitly requests direct editing. You may also do so when reconstruction is inadequate and the user has approved this method. The actual source must be attachable through the supported mechanism.

Do not treat "use this as inspiration" as "edit this exact image." No attachment is needed for prompt-first reconstruction.

## 3. Revise the proven prompt, not the image

Start with the single requested change. Use the verified successful authored prompt as the baseline. Make only the necessary revision.

- **Preserve:** every unrequested visual element. This includes identity and face, hairstyle, wardrobe, pose, and body geometry. It also includes composition, camera, lighting, background, environment, mood, and rendering style when the baseline specifies them.
- **Change:** only the element the user requested.
- **Exclude:** unwanted additions, text, boxes, artifacts, or other details that the user identified or that appear only in unsuccessful attempts.
- Do not add decorative improvements. Do not substitute clothing, alter faces, or change scenes to solve an unrelated issue.
- Avoid wholesale rewording of a successful prompt. Unnecessary prompt changes can affect more than the requested target.

For a style-only change, revise only the rendering treatment. Preserve all scene and subject details.

## 4. Optional direct-edit verification

Direct editing is a secondary method, not the default. Use it only when the user explicitly requests a direct image edit. Use it when reconstruction is materially inadequate and the actual image source is accessible through the supported mechanism.

- Attach the exact image source. A filename or image ID in text is not enough.
- Inspect the returned operation and parent/source metadata.
- If the metadata confirms source linkage and the requested change is visible, classify the result as a confirmed edit.
- If the metadata shows no source or parent, do not claim source continuity. This rule applies even when the output resembles the original.
- If metadata is unavailable, state that source linkage is unconfirmed.
- A result that looks successful is not automatically a confirmed edit.

## 5. Recovery when prompt reconstruction misses

If prompt reconstruction repeatedly misses the requested detail:

1. Stop repeating near-identical prompt revisions.
2. Recheck the exact successful baseline. Look for assistant-added changes.
3. Reduce the revision to the requested change only.
4. Consider direct editing only when the user explicitly requests it. You may also consider it after explaining its limits, if the exact source can be attached.
5. If neither method is reliable, explain the limit. Preserve the best successful baseline instead of mislabeling the result.

## 6. Prompt-before-generation archive

Follow `skills/session-archiving/SKILL.md` for every attempt:

1. Create or retrieve the current session-opening brief. Verify its exact path.
2. For non-novel work, commit the authored prompt in its dated `drawings/YYYY-MM-DD/` attempt note. For a named novel scene, commit it in the authoritative scene-local illustration prompt record under `novels/[Novel-ID]/[Arc-Folder]/[Scene-Folder]/illustrations/`.
3. Treat the session brief as the visual authority. Use the most recent successful prompt in the explicitly active series only as a compatible text baseline. Do not treat it as authority over the current brief.
4. Treat later failed, rejected, partial, or missed-target prompts as diagnostic evidence only. Do not use them as the baseline.
5. Record the session ID or brief path. Record the series ID or theme when it is explicitly active. Record the selected baseline source, operation type, and attached source reference.
6. Derive three to five observable acceptance criteria from the brief. Mark critical criteria.
7. Record the prompt difference. State the baseline, preserved details, changed details, and excluded or omitted details.
8. Verify the pre-attempt commit.
9. After the call, record the actual result, image ID, user assessment, and mismatch.
10. Do not store image binaries in Git unless the user requests storage and the operation completes.

## Technical documentation standard

This file defines operational instructions for image references and edits. Apply Strict mode from the repository [ASD-STE100 policy](../../asd-ste100/references/repository-writing-policy.md) when you revise it. Preserve source-verification, prompt-baseline, and user-authority requirements.
