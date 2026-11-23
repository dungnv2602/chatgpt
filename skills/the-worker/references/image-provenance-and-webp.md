# Image Provenance and WebP Delivery

The Worker owns shared image intake, original-byte preservation, WebP processing, publication, and provenance checks.

Use the [Image Takeout procedure](../../../images/takeout/README.md) for the exact hand-off schema, supported formats, conversion profiles, staging, retries, reports, and processor behavior. Use the [Drawing archive rules](../../drawing/references/archive-and-delivery.md) for drawing-session output records, manifest fields, and delivery links. This reference defines the shared Worker requirements without duplicating those detailed contracts.

## Generation and source evidence

- Capture every returned image immediately, in return order. Record the actual output count and associate each output with its attempt and prompt. Remove unused reserved IDs.
- Keep internal session, attempt, prompt, and output IDs separate from native platform IDs. Record native IDs only when the tool exposes them. Never invent IDs.
- Use direct generation-return association or reliable source metadata for output mapping. Do not infer mapping from filenames, chronology, memory, or visual similarity. Record uncertainty instead.
- Preserve the exact authored prompt and operation type. Do not claim to know an internal compiled prompt when the tool does not expose it.
- Preserve original image bytes when accessible. Calculate the original SHA-256 at generation time. Never hash a screenshot, thumbnail, recompressed copy, or transformed derivative as a substitute.
- If original bytes are unavailable, record that limit and leave the hash unavailable. A hash proves byte identity only. It does not prove content, prompt association, generation identity, or approval.
- Keep original and WebP hashes separate. Conversion changes the bytes. A generation-hash mismatch is retained for review and does not establish a verified mapping.
- Keep user approval, prompt/result success, mapping confidence, and publication verification as separate states.
- Do not delay image generation for GitHub, hashing, or archival work. Capture the output association first and record any later archive work as pending.

## Intake and original preservation

1. Inspect each uploaded image that requires repository retention.
2. Create one hand-off item with its exact top-level source filename, descriptive title, optional repository asset_id, and repository destination. Record source_asset_id separately when the generation record exposes a platform Asset ID.
3. Include `attempt: NN` for a destination under `drawings/YYYY-MM-DD/images/`. Other assets may omit it.
4. List every top-level upload exactly once in the ready hand-off. The Action does not infer image content, title, ID, or project membership.
5. Keep uploads directly in `images/takeout/`. Do not place them in the reserved `history/` or `webp/` directories.

Add a mandatory `conversation_record` path to every ready hand-off item. The file must be a dated conversation-integrity record and must contain the exact source filename in its `Image source mapping` table. For drawing outputs, use `drawings/history/YYYY-MM-DD-conversation-integrity.md`; include the attempt and a native Generation ID or recorded internal Output ID. The processor cross-checks that identity against the referenced attempt note. If an Asset ID is supplied, it must also match. A Partial or Curated record must identify unavailable material and label editorial summaries; do not invent a transcript to pass validation.

The processor moves each original byte-for-byte into the destination's `original/` folder. It stores the WebP derivative in the destination root. Novel assets use `novels/[Novel-ID]/assets/illustrations/[ARC-ID]/[SCN-ID]/`. Other assets use their declared destination. The original retains its metadata. The WebP does not replace the master.

## Unclassified image conversion-only path

Use this path when the image cannot be classified or mapped from retained evidence, but the user requests a WebP derivative. This path converts media only. It does not resolve provenance or authorize relocation.

1. Keep the source image in the top level of `images/takeout/`. Do not rename, move, or overwrite it.
2. Record the exact source filename in the conversion-only workflow's explicit allowlist. Do not use a wildcard or infer a file from chronology.
3. Convert only supported static formats. Use the same PNG or JPEG encoder profile defined below.
4. Write the derivative to `images/takeout/webp/[batch-id]/attempt-NNN/`. Append `.webp` to the complete source filename.
5. Reject an existing target. Use a new attempt directory for each retry.
6. Verify the WebP RIFF container and declared length. Hash the source before and after conversion. Require an unchanged source hash. Record the derivative SHA-256.
7. Commit only the verified derivatives and the conversion workflow changes. Do not stage source PNGs or unrelated project files.

The conversion-only workflow must not call `process_takeout.py`. It must not move or delete source files. It must not write `HANDOFF.yml`, conversion manifests, drawing manifests, attempt records, daily indexes, or destination files. It must not invent a title, asset ID, prompt ID, attempt, conversation record, approval, or destination. The image remains unclassified after conversion.

The user performs any later relocation. Do not move the source or derivative into a final destination. Do not edit an index or manifest unless the user explicitly requests the edit. When requested, use only exact relocation and mapping details that the user supplied or that repository evidence verifies. Keep missing values unknown.

After a later mapping is established, the ordinary provenance-gated processor remains mandatory for any assistant-managed relocation. A staged derivative from the conversion-only path does not bypass the conversation-record, source-identity, destination, or publication checks.

The current dedicated workflow, `.github/workflows/convert-unclassified-takeout.yml`, uses an exact seven-file allowlist for the 2026-11-20-001 intake. For a later batch, update the allowlist to the exact approved filenames and use a new batch/attempt path. Do not broaden it to all intake files.


Attempt records and daily drawing indexes link only to verified WebP delivery files. Approval does not control whether a generated output is retained or linked.

## Processing and publication

The [takeout processor](../scripts/process_takeout.py) and [GitHub Action](../../../.github/workflows/convert-images-to-webp.yml) own conversion and repository changes.

The processor validates the complete batch before relocating originals. It rejects missing or unlisted sources, unsafe paths, symlinks, and destination collisions. It stages and verifies each WebP before final placement.

On failure, the original uploads and ready hand-off remain available. Successful staged WebPs remain in the failed attempt folder. Each retry uses a new attempt directory and preserves earlier evidence.

On success, the processor moves verified WebPs to their destination roots, archives the hand-off and reports, and clears the active hand-off last.

After the first push, the publication verifier reads the exact original and WebP blobs from `origin/gpt`. It checks their hashes, the canonical WebP URL, the manifest, and the required Markdown links. Eligible manifest rows remain `Pending` until these checks pass. The final check-only pass verifies the published manifest against the branch.

Do not report publication as successful until the Action result is observed and the exact published assets, links, reports, and manifest have been read back. Legacy WebP files without retained originals remain `Not verifiable`.

## Drawing-session hand-off

The [Drawing archive rules](../../drawing/references/archive-and-delivery.md) own the drawing-session manifest and attempt-link contract. Record one manifest row for every returned output, including rejected, partial, pending, off-target, failed, superseded, and unapproved results. Keep approval separate from mapping and publication status.

Reconcile the session brief, attempt records, daily README, manifest, and repository assets before closeout. The [drawing-session closeout procedure](drawing-session-closeout.md) defines the user's required closeout cue and final checks.

## Documentation standard

This file defines shared technical and operational requirements. Apply Strict mode from the repository [ASD-STE100 policy](../../asd-ste100/references/repository-writing-policy.md) when you revise it.
