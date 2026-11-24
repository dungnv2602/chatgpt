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

The processor moves each provenance-mapped original byte-for-byte into the destination's `original/` folder. It stores the WebP derivative in the destination root. Novel assets use `novels/[Novel-ID]/assets/illustrations/[ARC-ID]/[SCN-ID]/`. Other assets use their declared destination. The original retains its metadata. The WebP does not replace the master. An item whose exact destination is `images/unclassified` is converted to WebP but remains in intake; its derivative stays under `images/takeout/webp/unclassified/`. The processor preserves that item in a residual Draft hand-off after a successful batch.

## Unclassified image handling

Use the normal Ready takeout workflow for both provenance-mapped and unclassified images. This keeps validation, conversion, reporting, and publication in one path without weakening the provenance gate.

1. Keep the original image at the top level of `images/takeout/`.
2. Review retained provenance. Match the exact source Asset ID, Generation ID or Output ID, conversation record, attempt record, and hand-off mapping. Do not classify by appearance, filename, chronology, or resemblance.
3. If the exact association is not established, keep the item unclassified with `destination_dir: "images/unclassified"`. Do not invent its source, attempt, prompt, asset ID, destination, or project membership.
4. The normal processor converts static PNG, JPG, and JPEG sources using the standard source-specific profile. It rejects animated PNG and malformed or extension-mismatched sources.
5. It writes the derivative to `images/takeout/webp/unclassified/attempt-NNN/`. Append `.webp` to the complete source filename. It chooses the next unused attempt directory and refuses to overwrite prior derivatives.
6. Verify the WebP RIFF container and declared length. Hash the source before and after conversion. Require an unchanged source hash. Record the derivative SHA-256 in the conversion report.
7. Keep the original in intake and the derivative in the unclassified staging directory. Keep the item in the residual Draft hand-off. Do not relocate either file or edit a manifest, attempt record, daily index, or other project index.

If any mapped or unclassified conversion fails, the Ready hand-off remains active and no mapped original is relocated. Successfully converted WebPs remain in their attempt directories for inspection. A retry uses a new attempt directory. The user performs any later relocation. Do not update an index unless the user explicitly requests it and supplies or confirms exact mapping details.

The normal workflow does not classify images. It validates the submitted hand-off and the exact source paths. It does not invent titles, asset IDs, prompt IDs, native IDs, attempts, conversation records, approvals, or destinations.

Attempt records and daily drawing indexes link only to verified WebP delivery files. Approval does not control whether a generated output is retained or linked.

## Processing and publication

The [takeout processor](../scripts/process_takeout.py) and [GitHub Action](../../../.github/workflows/convert-images-to-webp.yml) own conversion and repository changes.

The processor validates the complete batch before relocating originals. It rejects missing or unlisted sources, unsafe paths, symlinks, and destination collisions. It stages and verifies each WebP before final placement.

On failure, the original uploads and ready hand-off remain available. Successful staged WebPs remain in the failed attempt folder. Each retry uses a new attempt directory and preserves earlier evidence.

On success, the processor moves verified mapped WebPs to their destination roots. It retains verified unclassified derivatives under the unclassified staging path and keeps their originals in intake. It archives the complete hand-off and reports. It then removes only mapped entries from the active hand-off. Unclassified entries remain in a residual Draft hand-off; the processor clears the active hand-off only when no deferred items remain.

After the first push, the publication verifier reads the exact original and WebP blobs from `origin/gpt`. It checks their hashes, the canonical WebP URL, the manifest, and the required Markdown links. Eligible manifest rows remain `Pending` until these checks pass. The final check-only pass verifies the published manifest against the branch.

Do not report publication as successful until the Action result is observed and the exact published assets, links, reports, and manifest have been read back. Legacy WebP files without retained originals remain `Not verifiable`.

## Drawing-session hand-off

The [Drawing archive rules](../../drawing/references/archive-and-delivery.md) own the drawing-session manifest and attempt-link contract. Record one manifest row for every returned output, including rejected, partial, pending, off-target, failed, superseded, and unapproved results. Keep approval separate from mapping and publication status.

Reconcile the session brief, attempt records, daily README, manifest, and repository assets before closeout. The [drawing-session closeout procedure](drawing-session-closeout.md) defines the user's required closeout cue and final checks.

## Documentation standard

This file defines shared technical and operational requirements. Apply Strict mode from the repository [ASD-STE100 policy](../../asd-ste100/references/repository-writing-policy.md) when you revise it.
