# Drawing Archive, WebP Delivery, and Provenance Verification

## 8. WebP delivery copies and master-image preservation

The original PNG/JPEG is the permanent master. WebP is a separate delivery
derivative, never a replacement. All newly uploaded assets intended for
repository retention pass through the single intake at `images/takeout/`.

- The incoming filename may be arbitrary. Inspect the actual image and prepare
  the structured `HANDOFF.yml` with source filename, descriptive title,
  optional stable ID, and exact destination directory. For an image belonging
  to a non-novel drawing attempt, also include that attempt number in the item
  as `attempt: NN` and target `drawings/YYYY-MM-DD/images` for its session.
- The existing workflow runs on branch `gpt` and calls
  `images/scripts/process_takeout.py`. It accepts static PNG, JPG, and JPEG.
  APNG and other unsupported formats fail the batch; animation is never
  flattened silently.
- PNGs use exact lossless WebP encoding
  (`-lossless -q 100 -m 6 -exact`); JPEGs use high-quality lossy encoding
  (`-preset picture -q 92 -m 6 -sharp_yuv`). ICC profiles are copied.
  EXIF/XMP metadata are not copied to WebP, but remain in the original master.
- The original upload is moved byte-for-byte into the destination's
  `original/` subfolder under its hand-off-derived name. The same-stem WebP
  remains in the destination root. Attempt notes and the daily README link
  only the WebP delivery file. Novel illustrations use
  `novel/[Novel-ID]/assets/illustrations/[ARC-ID]/[SCN-ID]/`; retained
  non-novel assets use their declared destination under `images/`.
- When an item targets `drawings/YYYY-MM-DD/images`, an explicit `attempt: NN`
  is mandatory. The processor validates the matching `attempt-NN.md` and
  six-column daily README, then automatically adds the verified WebP link to
  both records for every uploaded generated output; approval and success
  classification are irrelevant to link creation. Multiple images may identify the same attempt; their links
  are grouped in that row.
  Items without `attempt` metadata are processed as ordinary assets and do not
  alter a prompt record or daily README. The GitHub Action commits these
  Markdown changes together with the processed assets.
- The Action converts the entire batch into persistent staging at
  `images/takeout/webp/[batch-id]/attempt-NNN/` before moving any original.
  Staged filenames append `.webp` to each exact incoming filename. It checks
  destination collisions, exact hand-off coverage, original/master SHA-256
  equality, WebP signatures, and final WebP hashes. It does not overwrite
  existing assets.
- For drawing sessions, the processor maintains `manifest.csv` one row per
  output, preserving existing rows/columns and inventorying legacy WebPs.
  Legacy WebPs are paired with same-stem masters in `images/original/` when
  present; their original SHA-256 is recorded and publication remains
  `Pending` until the pushed master and WebP blobs are verified. WebPs without
  originals remain `Not verifiable`; orphan originals without matching WebPs
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
  attempt directory; successful processing removes its empty staging
  directory. The Action then reads back the original and WebP Git blobs,
  canonical WebP URL, daily README inventory/table links, and attempt-note
  WebP link before publishing manifest verification statuses.
- Never alter a master or WebP after conversion as part of this pipeline.
  Separate image edits require the normal prompt-archive and explicit editing
  workflow.


## Mandatory generated-image archive verification (2026-11-20)

For every drawing session, archive **every generated image output**, regardless of approval, rejection, prompt compliance, or whether it is superseded. Each output must be individually recorded and directly linked from the session README once its exact repository asset exists and is verified. Preserve generation order and prompt-to-output association. Approval is a separate field and never determines archival or linking eligibility.


## Generation provenance and output mapping workflow (approved 2026-11-20)

Use capture-at-generation-time to avoid retrospective image-to-attempt guesses. This is mandatory for every drawing session and applies to approved, rejected, pending, partial, off-target, failed, and superseded outputs.

### Before generation
1. Assign internal session, attempt, and prompt IDs before invoking image generation (for example, session `2026-11-20`, attempt `A001`, prompt `P001`). These are archive IDs, not platform Generation IDs.
2. Reserve output IDs such as `A001-O01`, `A001-O02`. Reconcile reserved slots against actual outputs; do not assume the number returned.
3. Preserve the exact authored prompt and operation type. Follow the existing pre-generation prompt commit and read-back requirement.

### Immediately after generation
4. Capture every returned image in its returned sequence and associate it directly with its attempt/output record. Do not map by filename, visual similarity, chronology alone, or memory when direct association is available.
5. Record platform Generation ID and native image/output ID only when exposed by the generation system. Keep native IDs separate from internal archive IDs. If unavailable, explicitly mark them unavailable/not exposed; never invent IDs.
6. Preserve original bytes when accessible. If they cannot be retrieved, record the limitation; do not substitute a screenshot, thumbnail, or recompressed preview as the original.
7. Record the actual output count and sequence. Remove unused reserved slots; do not create phantom outputs. If the association cannot be established reliably, mark it Unmapped or Unverified.

### Mapping evidence and identity
8. Use internal output IDs (e.g. `A001-O01`) as stable archive identifiers when native IDs are not exposed. They must not be represented as native platform IDs.
9. Keep internal session/attempt/prompt/output IDs, native Generation ID, native image/output ID, approval, outcome, mapping evidence/status, original-byte availability, archive path, SHA-256, and verification status separate.
10. Direct generation-return association or reliable original metadata can support Verified mapping. Chronology and visual comparison may corroborate but cannot alone make a mapping Verified. Filename numbering is never proof.
11. Mapping statuses: `Verified`, `Corroborated`, `Probable`, `Unmapped`, or `Conflicting`. Explain uncertain or retrospective evidence; never silently upgrade status.
12. Calculate SHA-256 only from original image bytes when accessible. A hash proves byte identity, not generation event, prompt association, visual content, or approval. Record original and derivative hashes separately.

### Archive and verify
13. Archive every output regardless of approval. Preserve sequence, prompt association, direct links, and statuses; use the established asset-intake procedure.
14. Extend the session `manifest.csv` with one row per output and include internal attempt/output IDs, native Generation ID, native image/output ID, mapping evidence/status, and original-byte availability. Preserve existing required columns. Unavailable native IDs remain empty or explicitly unavailable.
15. Reconcile generation records, attempt notes, README, manifest, and actual assets. Verify paths, links, and hashes only after checking them; read back all edited records.
16. Do not block drawing on GitHub, hashing, or archival latency. Generate, capture outputs and their associations immediately, then complete metadata, hashing, archive, and verification. If capture or archival is incomplete, retain an explicit pending/incomplete status; do not claim complete closeout.

Provenance chain: **Session → Attempt → Prompt → Generation event (native ID if exposed) → Output (internal ID; native output ID if exposed) → original bytes → SHA-256 → archived asset/link**. Every link is evidence-backed; missing native IDs are stated honestly.

Maintain a session-level `manifest.csv` as the machine-readable source for archival tracking. Required columns:
```csv
session_date,image_id,filename,prompt_id,approval_status,github_url,sha256,verification_status
```
Use one row per generated output (not merely one row per prompt when an attempt yields multiple images). Record `approval_status` as Approved, Rejected, Pending, or Not recorded; use `verification_status` values that distinguish Pending, Verified, Failed, and Not verifiable. Do not invent identifiers, URLs, checksums, or statuses. Keep prompt IDs and image IDs stable and unambiguous.


Calculate SHA-256 from the actual original image bytes whenever those bytes are accessible. Do not calculate a checksum from screenshots, thumbnails, or recompressed derivatives and misrepresent it as the original checksum. If the original is unavailable, record SHA-256 as unavailable/pending rather than guessing. A checksum identifies exact file bytes; it does not establish visual content, prompt lineage, approval, or authenticity by itself.

When the user supplies a downloaded image's SHA-256, compare it with the recorded checksum for the candidate archived original. A match verifies byte-identical files; a mismatch means the files are not byte-identical and must not be marked verified. Renaming or moving a file does not change its checksum; re-encoding, editing, resizing, or converting usually does. If a source original and a WebP derivative are both archived, calculate and record their checksums separately and do not compare them as if they were the same byte stream.

README image links must point directly to the correct image asset and be checked against the repository path/blob before they are marked Verified. The manifest must not mark a URL or checksum Verified until the corresponding verification actually occurs. After archive changes, read back the README and manifest and reconcile every generated output against the chronological attempt record. Report any missing asset, link, prompt association, checksum, or verification explicitly.


## Original-image SHA-256 identity and WebP derivatives (approved 2026-11-20)

SHA-256 is mandatory **when the actual original generated image bytes are accessible immediately after generation**. Calculate the hash from those exact original bytes, never from a preview, screenshot, thumbnail, or recompressed copy. Record it against the session, attempt, prompt, and output ID before the user downloads the image. If original bytes are not accessible, state that the generation-time hash is unavailable; do not invent or calculate a hash from a substitute.


When the user later uploads an unchanged original, the GitHub Action calculates SHA-256 from the uploaded original before conversion and compares it with the generation-time hash. A match establishes byte-for-byte identity and may verify the original-to-output mapping. A mismatch is a review flag—not an automatic rejection—because metadata alteration, recompression, or conversion may change bytes. Do not silently fall back to filenames or visual guessing to claim a verified match. Use metadata and image-content comparison only as separately documented fallback evidence, with conservative mapping status.

The WebP is a derivative with different bytes and therefore is **not expected to match the original SHA-256**. The original hash remains the identity key for the output; record the derivative's path and link under the same output ID. A WebP SHA-256 is optional and only for independent derivative integrity checks. Never compare original PNG/JPEG hashes against converted WebP hashes as if equality were expected.

The GitHub Action should automate original-hash calculation and matching, mapping validation, conversion, renaming/relocation, direct README and attempt-record links, manifest reconciliation, and verification reporting. Preserve existing upload filenames unchanged; filenames are not identity evidence. Do not claim implementation is present until the Action itself has been inspected and modified.


## GitHub Action implementation status (2026-11-20)
The takeout processor retains original PNG/JPEG masters in each destination's
`original/` subfolder and places WebP delivery files in the destination root.
Attempt records and daily README rows link only the WebP. Drawing-session
`manifest.csv` updates preserve existing rows and columns, append one record
per new output, and inventory legacy WebPs. A same-stem original in the
destination's `original/` subfolder is paired by deterministic filename stem;
its actual SHA-256 is recorded and publication stays Pending until the pushed
Git blob is verified. A WebP without a retained original remains Not verifiable.
An original master without a same-stem WebP blocks processing rather than
silently disappearing from the manifest. Generation-time hash matches,
explicit attempt associations, native identifiers, approval, and
original/derivative hashes remain separate fields.

The Action does not query image-generation history or autonomously discover
native platform IDs. It consumes the explicit `attempt`, prompt/output IDs,
and generation hash supplied in `HANDOFF.yml`; missing provenance remains
blank and mapping confidence is never upgraded by filename. A supplied
generation-hash mismatch is retained for review, with mapping status
`Probable`, rather than rejecting the uploaded image. The workflow runs
Python compilation and regression tests before processing. The GitHub Actions
run must pass and its published output must be read back before the workflow
is described as fully verified.

