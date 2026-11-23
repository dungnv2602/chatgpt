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
2. Create one hand-off item with its exact top-level source filename, descriptive title, optional stable asset ID, and repository destination.
3. Include `attempt: NN` for a destination under `drawings/YYYY-MM-DD/images/`. Other assets may omit it.
4. List every top-level upload exactly once in the ready hand-off. The Action does not infer image content, title, ID, or project membership.
5. Keep uploads directly in `images/takeout/`. Do not place them in the reserved `history/` or `webp/` directories.

The processor moves each original byte-for-byte into the destination's `original/` folder. It stores the WebP derivative in the destination root. Novel assets use `novels/[Novel-ID]/assets/illustrations/[ARC-ID]/[SCN-ID]/`. Other assets use their declared destination. The original retains its metadata. The WebP does not replace the master.

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
