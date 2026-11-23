# Drawing Archive, WebP Delivery, and Provenance Verification

## 8. WebP delivery copies and master-image preservation

The original PNG/JPEG is the permanent master. WebP is a separate delivery
derivative, never a replacement. All newly uploaded assets intended for
repository retention pass through the single intake at `images/takeout/`.

- Incoming filenames may be arbitrary. Inspect the image. Prepare the structured
  `HANDOFF.yml` with the exact source filename, descriptive title, optional
  stable ID, and destination directory.
- For a non-novel drawing attempt, include its number as `attempt: NN`. Use
  `drawings/YYYY-MM-DD/images` as the destination for that session.
- The existing workflow runs on branch `gpt` and calls
  `skills/session-archiving/scripts/process_takeout.py`. It accepts static PNG, JPG, and JPEG.
  APNG and other unsupported formats fail the batch. Animation is never
  flattened silently.
- PNGs use exact lossless WebP encoding
  (`-lossless -q 100 -m 6 -exact`). JPEGs use high-quality lossy encoding
  (`-preset picture -q 92 -m 6 -sharp_yuv`). ICC profiles are copied.
  EXIF/XMP metadata are not copied to WebP, but remain in the original master.
- The original upload is moved byte-for-byte into the destination's
  `original/` subfolder under its hand-off-derived name. The same-stem WebP
  remains in the destination root. Attempt notes and the daily README link
  only the WebP delivery file. Novel illustrations use
  `novels/[Novel-ID]/assets/illustrations/[ARC-ID]/[SCN-ID]/`. Retained
  non-novel assets use their declared destination under `images/`.
- When an item targets `drawings/YYYY-MM-DD/images`, an explicit `attempt: NN`
  is mandatory. The processor checks the matching `attempt-NN.md` and
  six-column daily README, then automatically adds the verified WebP link to
  both records for every uploaded generated output. Approval and success
  classification are irrelevant to link creation. Multiple images may identify the same attempt. Their links
  are grouped in that row.
  Items without `attempt` metadata are processed as ordinary assets and do not
  change a prompt record or daily README. The GitHub Action commits these
  Markdown changes together with the processed assets.
- The Action converts the entire batch into persistent staging at
  `images/takeout/webp/[batch-id]/attempt-NNN/` before moving any original.
  Staged filenames append `.webp` to each exact incoming filename. It verifies
  destination collisions, exact hand-off coverage, original/master SHA-256
  equality, WebP signatures, and final WebP hashes. It does not overwrite
  existing assets.
- For drawing sessions, the processor maintains `manifest.csv` one row per
  output, preserving existing rows/columns and inventorying legacy WebPs.
  Legacy WebPs are paired with same-stem masters in `images/original/` when
  present. Their original SHA-256 is recorded and publication remains
  `Pending` until the pushed master and WebP blobs are verified. WebPs without
  originals remain `Not verifiable`. Orphan originals without matching WebPs
  block the batch.
- Internal fallback image IDs include a per-upload filename discriminator so
  separate outputs with identical bytes are still represented by separate
  manifest rows. These are archive IDs, not native platform IDs.
- Every attempt is archived under
  `images/takeout/history/[batch-id]/attempt-NNN/` with the original hand-off,
  `conversion-report.csv`, and `verification-report.md`. The CSV records
  staging and final paths, sizes, size difference, encoder profile/version,
  hashes, status, and errors. Both `history/` and `webp/` are excluded from
  intake detection.
- The active hand-off is cleared only after every image is converted,
  relocated, and verified locally and the reports are written. On failure, the
  ready hand-off and source images remain available for correction, and
  successful WebPs from that attempt remain in staging. A retry uses a fresh
  attempt directory. Successful processing removes its empty staging
  directory. The Action then reads back the original and WebP Git blobs,
  canonical WebP URL, daily README inventory/table links, and attempt-note
  WebP link. It publishes manifest verification statuses after these checks.
- Never change a master or WebP after conversion as part of this pipeline.
  Separate image edits require the normal prompt-archive and explicit editing
  workflow.


## Mandatory takeout hand-off closeout

The assistant owns the hand-off. The user should not have to create or repair
`images/takeout/HANDOFF.yml` after a generation workflow.

For each generation event:
1. Immediately capture the returned image count, sequence, internal output IDs, exposed native IDs, exact authored prompt, and attempt number.
   Capture the generation-time original SHA-256 when the original bytes are accessible.
2. Record each output in its attempt record before asking for review. Keep
   approval separate from archival eligibility.
3. When the user uploads generated originals to `images/takeout/`, inspect
   each image and match it to the generation-time output record. Use direct
   generation-return association, native metadata, or a documented corroborating
   source. Prompt text helps establish the intended title and scene, but does
   not by itself prove which uploaded file is which output.
4. Write every mapped upload to `HANDOFF.yml` with its exact top-level source filename, descriptive title, explicit attempt, and destination.
   Include the internal output ID, exposed native IDs, approval status, mapping evidence, and `expected_sha256` when the generation-time original hash exists.
   Do not fabricate unavailable fields. Do not leave placeholder entries.
5. Reconcile the hand-off against the actual intake directory. Every supported
   top-level image must appear exactly once. No unlisted images, duplicate
   source names, unresolved placeholders, missing attempt values, or invalid
   destinations are allowed.
6. Keep `status: draft` while any image, mapping, or required metadata is
   unresolved. Set `status: ready` only after the exact-coverage and metadata
   checks pass. Then run the workflow. A green CI result with a draft hand-off
   is a no-op, not a successful conversion.
7. If a generation output has not yet been uploaded, keep it recorded as
   awaiting upload in the attempt record. Do not invent an intake filename or
   add a speculative hand-off item. Resume the hand-off as soon as the upload
   appears.
8. After processing, check the archived report, original master, WebP
   derivative, manifest row, attempt link, and daily README link. Read back
   every changed repository record before reporting completion.

This closeout is mandatory for every image-generation workflow that retains
outputs in the repository. It applies to approved, pending, rejected,
superseded, partial, and off-target outputs. It does not authorize changing a
closed drawing session's creative brief or approval state.

## Mandatory generated-image archive verification (2026-11-20)

For every drawing session, archive **every generated image output**. This includes approved, rejected, pending, partial, off-target, failed, and superseded outputs.

Record each output separately. Link it from the session README after you check its exact repository asset. Preserve generation order and prompt-to-output association. Record approval in a separate field. Approval does not control archival or linking eligibility.


## Generation provenance and output mapping workflow (approved 2026-11-20)

Capture provenance at generation time. Do not rely on retrospective image-to-attempt guesses. This rule applies to every drawing session and every output status. It includes approved, rejected, pending, partial, off-target, failed, and superseded outputs.

### Before generation
1. Assign internal session, attempt, and prompt IDs before invoking image generation (for example, session `2026-11-20`, attempt `A001`, prompt `P001`). These are archive IDs, not platform Generation IDs.
2. Reserve output IDs such as `A001-O01`, `A001-O02`. Reconcile reserved slots against actual outputs. Do not assume the number returned.
3. Preserve the exact authored prompt and operation type. Follow the existing pre-generation prompt commit and read-back requirement.

### Immediately after generation
4. Capture every returned image in its returned sequence. Associate each image directly with its attempt and output record. Do not map by filename, visual similarity, chronology alone, or memory when direct association is available.
5. Record the platform Generation ID and native image or output ID only when the system exposes them. Keep native IDs separate from internal archive IDs. If an ID is not exposed, mark it unavailable. Never invent IDs.
6. Preserve original bytes when accessible. If they cannot be retrieved, record the limitation. Do not substitute a screenshot, thumbnail, or recompressed preview as the original.
7. Record the actual output count and sequence. Remove unused reserved slots. Do not create phantom outputs. If the association cannot be established reliably, mark it Unmapped or Unverified.

### Mapping evidence and identity
8. Use internal output IDs (e.g. `A001-O01`) as stable archive identifiers when native IDs are not exposed. They must not be represented as native platform IDs.
9. Keep internal session, attempt, prompt, and output IDs separate from native Generation IDs and native image or output IDs. Record approval, outcome, mapping evidence and status, original-byte availability, archive path, SHA-256, and verification status separately.
10. Direct generation-return association or reliable original metadata can support Verified mapping. Chronology and visual comparison may provide corroboration. They cannot establish Verified mapping by themselves. Filename numbering is never proof.
11. Mapping statuses: `Verified`, `Corroborated`, `Probable`, `Unmapped`, or `Conflicting`. Explain uncertain or retrospective evidence. Never silently upgrade status.
12. Calculate SHA-256 only from original image bytes when they are accessible. A hash proves byte identity only. It does not prove the generation event, prompt association, visual content, or approval. Record original and derivative hashes separately.

### Archive and check
13. Archive every output regardless of approval. Preserve sequence, prompt association, direct links, and statuses. Use the established asset-intake procedure.
14. Extend the session `manifest.csv` with one row per output. Include internal attempt and output IDs, native Generation ID, native image or output ID, mapping evidence and status, and original-byte availability. Preserve existing required columns. Leave unavailable native IDs empty or mark them unavailable.
15. Reconcile generation records, attempt notes, README, manifest, and actual assets. Compare each path, link, and hash with its recorded value. Read back all edited records.
16. Do not delay drawing for GitHub, hashing, or archive work. Generate the image and capture its output association immediately. Then complete metadata, hashing, archival, and verification.

If capture or archival is incomplete, use a pending or incomplete status. Do not claim complete closeout.

Provenance chain: **Session → Attempt → Prompt → Generation event → Output → original bytes → SHA-256 → archived asset/link**. Record native IDs when exposed. Record internal IDs as archive identifiers, not platform metadata. Every link must have evidence. State when native IDs are unavailable.

Maintain a session-level `manifest.csv` as the machine-readable source for archival tracking. Required columns:
```csv
session_date,image_id,filename,prompt_id,approval_status,github_url,sha256,verification_status
```
Use one row per generated output. Do not use one row per prompt when an attempt yields multiple images.

Use these `approval_status` values: Approved, Rejected, Pending, or Not recorded. Use these `verification_status` values: Pending, Verified, Failed, or Not verifiable. Do not invent IDs, URLs, checksums, or statuses. Keep prompt IDs and image IDs stable and unambiguous.


Calculate SHA-256 from the actual original image bytes whenever those bytes are accessible. Do not calculate a checksum from screenshots, thumbnails, or recompressed derivatives and misrepresent it as the original checksum. If the original is unavailable, record SHA-256 as unavailable/pending rather than guessing. A checksum identifies exact file bytes. It does not establish visual content, prompt lineage, approval, or authenticity by itself.

When the user supplies a downloaded image's SHA-256, compare it with the recorded checksum for the candidate original. A match establishes byte identity. A mismatch means the files are not byte-identical. Do not mark the file verified.

Renaming or moving a file does not change its checksum. Re-encoding, editing, resizing, or converting usually changes it. If you archive an original and a WebP derivative, calculate and record their hashes separately. Do not compare them as the same byte stream.

README image links must point directly to the matching image asset. Check each link against the repository path and blob before marking it Verified. Do not mark a URL or checksum Verified in the manifest before you check it.

After archive changes, read back the README and manifest. Reconcile every generated output against the chronological attempt record. Report any missing asset, link, prompt association, checksum, or verification.


## Original-image SHA-256 identity and WebP derivatives (approved 2026-11-20)

SHA-256 is mandatory **when the actual original generated image bytes are accessible immediately after generation**. Calculate the hash from those exact original bytes, never from a preview, screenshot, thumbnail, or recompressed copy. Record it against the session, attempt, prompt, and output ID before the user downloads the image. If original bytes are not accessible, state that the generation-time hash is unavailable. Do not invent or calculate a hash from a substitute.


When the user later uploads an unchanged original, the GitHub Action calculates SHA-256 before conversion. It compares this hash with the generation-time hash. A match establishes byte-for-byte identity. It may also check the original-to-output mapping. A mismatch is a review flag, not an automatic rejection. Metadata alteration, recompression, or conversion may change the bytes. Do not claim a verified match based only on filenames or visual guessing. Use metadata and image-content comparison only as separately documented fallback evidence. Keep the mapping status conservative.

The WebP is a derivative with different bytes and therefore is **not expected to match the original SHA-256**. The original hash remains the identity key for the output. Record the derivative's path and link under the same output ID. A WebP SHA-256 is optional and only for independent derivative integrity checks. Never compare original PNG/JPEG hashes against converted WebP hashes as if equality were expected.

The GitHub Action should automate these tasks:

- Calculate and compare original hashes.
- Check output mapping.
- Convert, rename, and relocate files.
- Add direct links to the README and attempt records.
- Reconcile the manifest and write verification reports.

Preserve incoming upload filenames. Filenames are not identity evidence. Do not claim implementation until you inspect and update the Action.


## GitHub Action implementation status (2026-11-20)
The takeout processor retains original PNG/JPEG masters in each destination's
`original/` subfolder and places WebP delivery files in the destination root.
Attempt records and daily README rows link only the WebP. Drawing-session
`manifest.csv` updates preserve existing rows and columns, append one record
per new output, and inventory legacy WebPs. A same-stem original in the
destination's `original/` subfolder is paired by filename stem. The processor
records its SHA-256. Publication remains Pending until the pushed Git blob is
verified. A WebP without a retained original remains Not verifiable.
An original master without a same-stem WebP blocks processing rather than
silently disappearing from the manifest. Generation-time hash matches,
explicit attempt associations, native identifiers, approval, and
original/derivative hashes remain separate fields.

The Action does not query image-generation history or autonomously discover
native platform IDs. It consumes the explicit `attempt`, prompt/output IDs,
and generation hash supplied in `HANDOFF.yml`. Missing provenance remains
blank and mapping confidence is never upgraded by filename. A supplied
generation-hash mismatch is retained for review, with mapping status
`Probable`, rather than rejecting the uploaded image. The workflow runs
Python compilation and regression tests before processing. The GitHub Actions
run must pass and its published output must be read back before the workflow
is described as fully verified.



## Technical documentation standard

This file defines operational image archive and delivery procedures. Apply Strict mode from the repository [ASD-STE100 policy](../../asd-ste100/references/repository-writing-policy.md) when you revise it. Preserve byte identity, provenance, mapping, and verification requirements.
