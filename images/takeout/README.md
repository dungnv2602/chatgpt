# Image Takeout

This is the single intake location for user-uploaded images intended for retention in this repository, whether they belong to a novel, a drawing session, a visual-reference collection, or another project.

## Upload rules

- Upload every image directly into `images/takeout/`; do not create upload subfolders.
- Incoming filenames may be arbitrary. The user does not need to rename them.
- `history/` and `webp/` are system-managed reserved subdirectories. Never place incoming images in either directory.
- Keep one active batch in `HANDOFF.yml`.
- The Action does nothing until `HANDOFF.yml` has `status: ready`.
- When the hand-off is ready, every image in the top level of the intake folder must be listed exactly once.
- Supported inputs are static PNG, JPG, and JPEG. APNG, GIF, WebP, HEIC, AVIF, TIFF, BMP, and other formats are not accepted by this pipeline. Animated images are never flattened.

## Hand-off format

The assistant inspects each image, determines its descriptive title and intended destination from the project context, assigns a stable asset ID when appropriate, and writes the hand-off. The Action does not guess the image's subject, title, ID, project, or destination.

```yaml
version: 1
batch_id: "2026-11-20-001"
status: ready
items:
  - source: "IMG_20261120_091522.png"
    asset_id: "ILL-001"
    title: "Shared Discovery"
    destination_dir: "novel/Novel-02/assets/illustrations/ARC-001/SCN-001"
    # Include only provenance values actually captured:
    expected_sha256: "0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef"
    output_id: "A001-O01"
    prompt_id: "P001"
    native_generation_id: "platform-generation-id-if-exposed"
    native_output_id: "platform-output-id-if-exposed"
    approval_status: "Not recorded"
    mapping_evidence: "Direct generation-return association recorded at generation time"
```


For drawing-session outputs, when the generation-time original SHA-256 was captured, include it as `expected_sha256` in the item. The processor calculates SHA-256 of the uploaded original and compares it before conversion. A mismatch is retained as a review flag: the image can still be archived, but mapping confidence is reduced to `Probable` and it is never marked `Verified` by that hash. Optional internal `output_id`, `prompt_id`, and exposed native IDs are recorded separately. Supply them only from generation-time records; never infer them from filenames.

The conversion report distinguishes `generation_sha256` (the expected hash recorded at generation) from `source_sha256` (the hash calculated from the upload), and includes `hash_match`. The WebP's own hash is independent because conversion changes bytes. The session processor also reconciles `drawings/YYYY-MM-DD/manifest.csv`: it
records new outputs, inventories legacy WebPs, and pairs a same-stem master
from `images/original/` when present. It records the actual master SHA-256 and
leaves publication verification Pending until the remote blobs are checked. A
legacy WebP with no original remains Not verifiable; an original master with
no same-stem WebP blocks the batch rather than being silently omitted.

For each item:

- `source` is the exact uploaded filename at the top level of this folder.
- `asset_id` is optional for general image assets. Novel illustrations use their stable `ILL-NNN` ID.
- `title` is a concise descriptive title based on the inspected image and its intended role.
- `destination_dir` is a repository-relative directory under `images/`, `novel/`, or `drawings/YYYY-MM-DD/images`. Do not use `images/takeout/`, `images/takeout/webp/`, `images/webp/`, or `images/scripts/`.
- For drawing-session destinations, `attempt` is mandatory. The Action rejects drawing-session uploads without an explicit attempt number so they cannot be omitted from the session manifest and prompt records.

The processor turns the title into a lowercase, hyphen-separated filename slug, removes common diacritics, and prefixes the asset ID when supplied. For the example above, it creates:

- Original master: `novel/Novel-02/assets/illustrations/ARC-001/SCN-001/original/ILL-001-shared-discovery.png`
- WebP delivery file: `novel/Novel-02/assets/illustrations/ARC-001/SCN-001/ILL-001-shared-discovery.webp`

The original is moved byte-for-byte into the destination's `original/` subfolder. The WebP remains in the destination root and is the only format linked from attempt records and the daily README. Existing files are never overwritten.

Before relocation, each WebP is written to persistent staging under `images/takeout/webp/[batch-id]/attempt-NNN/`. Its name is the exact incoming filename with `.webp` appended, so `IMG_001.png` becomes `IMG_001.png.webp` and `IMG_001.jpg` becomes `IMG_001.jpg.webp`. This retains the original extension in staging and avoids collisions between different source formats with the same basename.

## Processing and success conditions

The existing workflow, `.github/workflows/convert-images-to-webp.yml`, runs on pushes to the takeout files or hand-off and can also be started manually on branch `gpt`.

It validates the entire batch, converts all images into the persistent attempt-specific staging folder `images/takeout/webp/[batch-id]/attempt-NNN/`, verifies the staged WebPs, and only then relocates the original masters and WebP derivatives to their permanent destinations. The CSV records each staging path as well as the final path. The processor checks source/master SHA-256 equality, WebP signatures and file lengths, destination collisions, exact hand-off coverage, and attempt metadata for every drawing-session upload.

If validation or conversion fails, original uploads remain in the intake, the hand-off remains ready, and every successfully converted WebP remains in that failed attempt's staging folder for inspection. A retry uses a fresh numbered attempt and does not overwrite earlier staging. On success, staged WebPs are moved to their final destinations and the now-empty successful staging attempt directory is removed.

For drawing outputs, the session manifest initially records publication as
`Pending`. After the Action pushes the assets and Markdown changes, a second
step reads the exact blobs back from `origin/gpt`, verifies the original
master SHA-256, WebP SHA-256, canonical WebP URL, daily README image-inventory
link, attempt-table link, and attempt-note WebP link, then commits the updated
manifest status. The final check-only pass confirms the published manifest
itself matches the GitHub branch. Failed publication checks are recorded as
`Failed` on-branch before the final verification step fails the Action. Legacy assets without retained originals
remain `Not verifiable`; their WebP URL and derivative hash are still checked.

A batch is successful only after every master and WebP is verified locally,
the original hand-off and reports are archived, and the active hand-off is
reset to empty. A failed attempt does not clear the hand-off; correcting it
and retrying the same batch ID creates another numbered attempt.

## History and reports

Each attempt is retained under:

```text
images/takeout/history/
└── [batch-id]/
    └── attempt-001/
        ├── HANDOFF.yml
        ├── conversion-report.csv
        └── verification-report.md
```

The CSV records source, staging, and final paths, title and ID, source format, encoder profile and version, original/WebP byte counts, size difference, SHA-256 values, verification status, and errors. A negative size reduction is valid: it means the WebP is larger than the original.

The Markdown verification report records the batch outcome, checks, and warnings/errors. Failed attempts are retained for inspection. Both `history/` and `webp/` are reserved and excluded from intake detection; neither is reprocessed as uploaded content.

The active hand-off starts empty:

```yaml
version: 1
status: empty
items: []
```

## Conversion profiles

| Source | Encoder profile | Fidelity |
|---|---|---|
| PNG | `-lossless -q 100 -m 6 -exact` | Lossless; preserves RGB values in fully transparent pixels |
| JPEG | `-preset picture -q 92 -m 6 -sharp_yuv` | High-quality lossy; not pixel-identical |

Both profiles request ICC profile copying. EXIF/XMP metadata are not copied to WebP; they remain in the unchanged original master.


## Drawing-session manifest

For every upload that includes an explicit \`attempt\` and targets
\`drawings/YYYY-MM-DD/images\`, the processor updates that session's
\`manifest.csv\` with one row per output. It preserves existing rows and columns,
adds missing required columns, and inventories pre-existing top-level WebP
assets that do not yet have a manifest row.

The required columns remain:

\`\`\`csv
session_date,image_id,filename,prompt_id,approval_status,github_url,sha256,verification_status
\`\`\`

Additional columns keep the internal output ID, native Generation/output IDs,
attempt, mapping evidence/status, original and WebP paths and hashes,
generation-time hash, hash-match result, original-byte availability, and
verification error separate.

- New uploads record the actual uploaded-original SHA-256 in \`sha256\` and
  \`original_sha256\`; WebP bytes have their own \`webp_sha256\`.
- A generation-time hash match can set mapping status to \`Verified\`. When the
  hand-off explicitly assigns an attempt but no generation-time hash is
  available, mapping remains \`Corroborated\`; the processor does not infer a
  mapping from filenames.
- The processor writes \`verification_status: Pending\`. Only the post-push
  verifier may change it to \`Verified\`, after reading the exact original and
  WebP blobs from \`origin/gpt\` and checking the GitHub WebP URL.
- Pre-existing WebP assets are paired with same-stem files in the `original/`
  subfolder when available. The retained master SHA-256 is calculated and the
  row remains `Pending` until the exact master and WebP blobs are read back.
  WebPs without masters remain `Not verifiable`, with no fabricated original
  checksum. Orphan masters without matching WebPs block processing.
- Internal fallback image IDs include a per-upload filename discriminator so
  separate outputs with identical image bytes still receive separate manifest
  rows. These IDs are archive identifiers, not native platform IDs.
- Approval stays separate from mapping and verification. Missing approval,
  prompt IDs, native IDs, or generation hashes remain `Not recorded` or blank.

The README and attempt records intentionally link only the WebP delivery file;
the unchanged original master is retained under the destination's \`original/\`
subfolder and recorded in the session manifest.
