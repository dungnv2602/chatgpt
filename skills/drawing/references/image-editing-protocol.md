# Image Source and Editing Protocol

This reference governs the choice between fresh generation and direct image editing.

## 1. Select the operation

| User intent | Operation | Required source |
|---|---|---|
| Create a new scene, composition, or variation | Fresh generation | Active brief; successful prompt when continuing a series |
| Change one particular existing image | Direct image edit | The exact source image, available to the image tool |
| Re-create an unavailable image as a new output | Fresh generation | Active brief and any recoverable successful prompt |

Do not substitute one operation for another. A fresh generation is not an edit.

## 2. Fresh generation

1. Read the active session brief.
2. For a continuation, locate the latest successful prompt in the same series or artwork thread.
3. Use its authored text as the baseline. Preserve unaffected details and wording.
4. Apply only changes authorized by the latest user instruction.
5. Record the baseline, prompt difference, acceptance criteria, and authored prompt before generation.

Do not use a failed or rejected prompt as the default baseline. Do not restore historical details that conflict with the active brief.

## 3. Direct image edit

Use a direct edit only when the user wants a particular image changed and the exact source is available.

1. Attach the actual source image through the supported image tool.
2. Describe the requested change. Preserve all other requested or locked properties.
3. Record the source image, operation type, authored edit instructions, and acceptance criteria before the call.
4. Inspect the result for the requested change and unintended differences.
5. Record whether source linkage is confirmed, supported by the tool call, or unavailable.

A filename, repository path, generation ID, or written prompt does not attach an image. Do not claim a source edit when the source was not supplied to the tool.

## 4. Source unavailable

If the user requests a direct edit but the source is not available, explain that the edit cannot be performed from the current materials. Do not silently switch to fresh generation. Ask whether the user wants a new reconstruction only when that choice is not already clear.

A successful prompt can guide a new image. It cannot stand in for the source image or prove that the new result is an edit.

## 5. Prompt and record integrity

- Commit the attempt record before the image operation.
- Keep prompt text limited to the visual instructions needed for that operation.
- Keep file paths, attempt labels, prompt IDs, and provenance metadata in the attempt record.
- Do not invent native IDs or claim access to a hidden compiled prompt.
- Record the actual operation, source availability, output, deviations, and verification afterward.

Use the canonical Drawing attempt template for every attempt. The Worker owns session records, prompt history, image retention, WebP delivery, and drawing-session closeout.

## Documentation standard

Apply Strict mode from the repository ASD-STE100 policy.