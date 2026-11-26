# Drawing Asset Archive and Delivery

The Worker owns shared intake, original-byte preservation, WebP conversion, publication, and provenance. This reference defines Drawing-specific destinations and records.

## Asset destinations

- Retained non-novel drawing outputs: area/drawing/YYYY-MM-DD/images/.
- Novel illustrations: area/novel/[Novel-ID]/assets/illustrations/[ARC-ID]/[SCN-ID]/.
- Other retained image assets: the destination declared in images/takeout/HANDOFF.yml.

Store each retained output separately. Use attempt-XX.webp for one image and numbered suffixes for multiple outputs. Link only exact assets whose path and provenance have been verified. Do not migrate existing assets.

## Shared intake

All new retained uploads enter through the flat images/takeout/ intake. Follow the Worker's [image provenance and WebP procedure](../the-worker/references/image-provenance-and-webp.md) and [Image Takeout guide](../../../../.takeout/images/README-2.md).

For a non-novel drawing output, include the attempt number in the hand-off and set the destination to area/drawing/YYYY-MM-DD/images/. The processor requires this field before it updates the attempt record, daily index, or session manifest. Do not move or convert uploaded files manually.

The processor is  .agent/skills/the-worker/scripts/process_takeout.py. The workflow is .github/workflows/convert-images-to-webp.yml. It preserves the original PNG/JPEG master and creates a separate WebP derivative.

## Generation provenance

Record every returned output, including rejected, partial, pending, and superseded results. Keep each output's generation order, attempt, prompt, approval, mapping evidence, and original-byte availability distinct.

Capture native IDs only when the image tool exposes them. Internal attempt and output IDs are archive identifiers, not platform IDs. Capture the original SHA-256 only from original bytes. A hash match establishes byte identity, not prompt association or approval.

Do not infer an output mapping from a filename or chronology. Use direct generation-return association or reliable native metadata. Otherwise record the mapping as Corroborated, Probable, Unmapped, or Conflicting.

## Drawing-session manifest

The processor maintains manifest.csv with one row per output. Its required columns are:

    session_date,image_id,filename,prompt_id,approval_status,github_url,sha256,verification_status

The manifest also preserves attempt, output, native IDs, mapping evidence, original/WebP paths, and separate hashes. Do not replace existing columns or rows.

The processor inventories legacy WebPs. It pairs a legacy WebP with a same-stem original in the destination's original/ folder when available. A WebP without an original remains Not verifiable. An original without a matching WebP blocks processing.

New rows begin as Pending. The publication verifier reads the exact original and WebP blobs from gpt. It checks their hashes, canonical URL, daily README, and attempt links before it marks the row Verified. Do not mark publication complete before this check.

## Failure and closeout

On failure, preserve the original intake files, ready hand-off, and successful staged WebPs. Retry in a new staging attempt. Do not overwrite prior evidence.

On success, verify the attempt report, original master, WebP, manifest row, attempt link, and daily README link. Read back every changed record before reporting completion.

The Worker defines the drawing-session closeout. Close only when the user says end session.

## Documentation standard

Apply Strict mode from the repository ASD-STE100 policy.