# Image Provenance and WebP Delivery

## 10. WebP delivery derivatives

Original PNG/JPEG files are permanent masters. WebP files are separate
delivery derivatives, never replacements. New retained uploads use the shared
flat intake at `images/takeout/` and the structured `HANDOFF.yml`.

- Incoming filenames may be arbitrary. Inspect each image and prepare a hand-off
  item with the exact source filename, descriptive title, optional stable ID,
  and destination directory. The Action does not infer visual content or
  project membership. For drawing-session destinations, `attempt: NN` is
  mandatory and is the explicit prompt-to-output association used for automatic
  Markdown cross-linking. Non-drawing assets may omit it.
- The existing workflow on branch `gpt` calls
  `skills/session-archiving/scripts/process_takeout.py`. It supports static PNG, JPG, and JPEG.
  APNG and other unsupported formats fail the batch. Animated content is never
  silently flattened.
- PNG uses exact lossless encoding
  (`-lossless -q 100 -m 6 -exact`). JPEG uses high-quality lossy encoding
  (`-preset picture -q 92 -m 6 -sharp_yuv`). ICC profiles are copied. EXIF/XMP
  metadata remain in the unchanged original and are not copied to WebP.
- The original is moved byte-for-byte into the destination's `original/`
  subfolder, using the hand-off-derived name. The WebP derivative remains in
  the destination root. Novel illustration assets use
  `novels/[Novel-ID]/assets/illustrations/[ARC-ID]/[SCN-ID]/`. Other retained
  assets use their declared directory under `images/`. Attempt notes and the
  daily README link only the WebP delivery file. The original master is not
  linked there.
- The processor validates the complete batch, converts every image into
  persistent staging at `images/takeout/webp/[batch-id]/attempt-NNN/`, and
  only then relocates any original. Each staged filename appends `.webp` to
  the exact incoming filename. It rejects unlisted uploads, missing sources,
  destination collisions, symlinks, and invalid paths. It verifies
  source/master SHA-256 equality, WebP signatures, and final WebP hashes.
- When `attempt: NN` is present for a destination under
  `drawings/YYYY-MM-DD/images`, the processor verifies the corresponding
  attempt record and six-column daily README, then writes the verified WebP
  link into both for every generated image, including partial, off-target,
  superseded, and unapproved results. Approval is not a linking condition.
  Multiple uploads may point to the same attempt. The GitHub Action commits
  these Markdown changes together with the image masters, derivatives,
  session `manifest.csv`, and takeout reports. Items without `attempt` are
  processed as ordinary assets and do not enter a drawing session manifest or
  prompt records.
- Every successful or failed attempt is preserved under
  `images/takeout/history/[batch-id]/attempt-NNN/` with the hand-off snapshot,
  `conversion-report.csv`, and `verification-report.md`. The CSV records
  source, staging, and final paths, sizes, size difference, encoder
  profile/version, SHA-256 values, result, and errors. Both `history/` and
  `webp/` are reserved and excluded from intake.
- On failure, original uploads and the ready hand-off remain available and
  successfully converted WebPs remain in that failed attempt's staging
  folder. Retries use a new attempt directory. On success, staged WebPs move
  to final destinations and the now-empty successful staging directory is
  removed. The active hand-off is reset to empty only after every original and
  WebP has been relocated and verified and both reports have been archived.
  After the first push, a separate verifier reads original and WebP blobs from
  `origin/gpt`, validates the direct WebP URL, and upgrades only eligible
  `Pending` manifest rows. Legacy entries without their original master stay
  `Not verifiable`. The Action re-reads the published manifest after the
  verification commit. Never claim a successful Action run without observing
  its result and reading back the published assets, links, and reports.


## Generation provenance and output mapping workflow (approved 2026-11-20)

Capture provenance at generation time for every drawing session. Do not rely on retrospective reconstruction.

- **Before generation:** assign internal session, attempt, and prompt IDs. Reserve output IDs such as `A001-O01`, `A001-O02`. These are archive identifiers, not native platform identifiers. Preserve exact authored prompt and generation/edit operation.
- **Immediately after generation:** capture every returned image in returned order and associate each directly with its attempt/output record. Record the actual output count. Remove unused reserved slots. Do not create phantom outputs. Do not map by filename, visual similarity, chronology alone, or memory when direct association exists.
- **Native IDs:** record platform Generation ID and image/output ID only when exposed. Keep them separate from internal IDs. If unavailable/not exposed, state that. Never invent IDs.
- **Original bytes:** preserve original image bytes when accessible. If not, record the limitation. Screenshots, thumbnails, and recompressed copies are not substitutes for original bytes.
- **Mapping evidence:** direct generation-return association or reliable source metadata can support Verified. Chronology and visual comparison may corroborate but cannot alone establish Verified. Mapping statuses are Verified, Corroborated, Probable, Unmapped, or Conflicting. Explain uncertainty and never silently promote a status.
- **Integrity:** calculate SHA-256 from actual original bytes. Hashes prove byte identity only, not prompt linkage, generation identity, content, or approval. Store original and derivative hashes separately.
- **Manifest:** one row per output. Preserve existing required fields and add internal attempt/output IDs, native Generation ID, native image/output ID, mapping evidence/status, and original-byte availability. Never fabricate IDs, links, hashes, or verification results.
- **Archive:** retain every output regardless of approval and preserve sequence and prompt association. Use established asset-intake procedures. Verify exact paths, blob identity, direct links, and hashes before marking verified.
- **Latency:** generation must not wait for GitHub, hashing, or archival. Capture/associate outputs immediately, then perform remaining archive work. If capture or archive is incomplete, leave explicit pending/incomplete status.
- **Closeout:** reconcile generation records, attempt notes, README, manifest, and repository assets. Read back changes and report unresolved gaps. Do not mark complete while mandatory checks remain unresolved.

Provenance chain: **Session → Attempt → Prompt → Generation event (native ID if exposed) → Output (internal ID. Native output ID if exposed) → original bytes → SHA-256 → archive asset/link**. Internal IDs are archive identifiers, never claims about platform metadata.

## Mandatory image archive manifest and SHA-256 verification (2026-11-20)

For every drawing session, record **every generated image output**—approved, rejected, pending, partial, off-target, failed, or superseded—without treating approval as a condition for archival or linking. Preserve the generation sequence and exact prompt association. The daily README must link every image directly to its exact GitHub asset after the path/blob is verified. Keep approval status separate from outcome and storage/link verification.

Maintain a session-level `manifest.csv`, with one row per generated output and these required columns:
```csv
session_date,image_id,filename,prompt_id,approval_status,github_url,sha256,verification_status
```
Use explicit approval values (Approved, Rejected, Pending, Not recorded) and verification values (Pending, Verified, Failed, Not verifiable). Never invent IDs, prompt associations, URLs, checksums, or verification results. Reconcile the manifest against the chronological attempt records and README. Do not omit outputs when a tool returns multiple images for one attempt.

Calculate SHA-256 from the actual original image bytes when accessible. Do not use a screenshot, thumbnail, or transformed derivative as a substitute for the original's checksum. If the original bytes are unavailable, leave the checksum unavailable/pending. SHA-256 establishes byte identity only. It does not independently prove the image's content, approval, prompt association, or provenance. A renamed or moved byte-identical file retains its checksum, but re-encoding, resizing, editing, or format conversion generally changes it. Record original and derivative checksums separately.

When a user provides a downloaded image's SHA-256, compare it to the archive's recorded checksum. Mark it Verified only when values match. A mismatch is not byte-identical and must not be marked verified. Verify direct GitHub image URLs by checking the exact repository path/blob. Do not mark link or checksum verification complete without an actual check. After updating archival records, read back the README and manifest and verify they agree with attempt records and repository assets. Report unresolved gaps explicitly.


## Original-image SHA-256 identity and WebP derivatives (approved 2026-11-20)

**Original SHA-256 is mandatory when actual original bytes are accessible at generation time.** Calculate it immediately from the exact generated file bytes and record it against session, attempt, prompt, and output ID. Never hash a screenshot, preview, thumbnail, or transformed substitute. If the original bytes are inaccessible, explicitly record the hash as unavailable. Do not fabricate one.

At ingestion, the GitHub Action must calculate SHA-256 from the uploaded original **before** conversion and compare it to the generation-time hash. Matching hashes establish byte-for-byte identity and can verify the uploaded original's mapping to its recorded output. Mismatches must be flagged for review and must not be silently mapped by filename or visual guess. If original bytes differ, metadata inspection and content comparison may be used as fallback evidence, but their evidence and confidence must be recorded separately and conservatively.

WebP conversion changes bytes. Therefore, the original hash is the identity key and the WebP is a derivative linked to the same output ID. The WebP hash is optional and only for derivative-integrity checking. Never expect or require original and WebP hashes to match.

The Action is intended to automate: original SHA-256 calculation and comparison. Output-to-attempt/prompt mapping validation. Conversion. Renaming and relocation. Direct image links in attempt records and README. Manifest update/reconciliation. And verification reporting. Preserve incoming original filenames, but never treat them as mapping evidence. This policy supersedes earlier wording that made hashing unavailable, optional, or mandatory on transformed derivatives. It does not claim the Action has been implemented until its code is actually updated and verified.


## GitHub Action implementation status (2026-11-20)
The takeout processor retains original PNG/JPEG masters in each destination's
`original/` subfolder and places WebP delivery files in the destination root.
Attempt records and daily README rows link only the WebP. Drawing-session
`manifest.csv` updates preserve existing rows and columns, append one record
per new output, and inventory legacy WebPs. A same-stem original in the
destination's `original/` subfolder is paired by deterministic filename stem
its actual SHA-256 is recorded and publication stays Pending until the pushed
Git blob is verified. A WebP without a retained original remains Not verifiable.
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

