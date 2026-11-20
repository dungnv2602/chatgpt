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
    # For generated drawings, include the generation-time hash and IDs:
    expected_sha256: "0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef"
    output_id: "A001-O01"
    prompt_id: "P001"
```


For drawing-session outputs, when the generation-time original SHA-256 was captured, include it as `expected_sha256` in the item. The processor calculates SHA-256 of the uploaded original and rejects a mismatch before conversion/relocation, retaining the upload and hand-off for review. Optional `output_id` and `prompt_id` fields are recorded in the conversion report for traceability. These IDs must be supplied from generation-time records; never infer them from filenames.

The conversion report distinguishes `generation_sha256` (the expected hash recorded at generation) from `source_sha256` (the hash calculated from the upload), and includes `hash_match`. The WebP's own hash is independent because conversion changes bytes. Generation-hash matching is not yet a session-level `manifest.csv` reconciler; that remains a separate enhancement.

For each item:

- `source` is the exact uploaded filename at the top level of this folder.
- `asset_id` is optional for general image assets. Novel illustrations use their stable `ILL-NNN` ID.
- `title` is a concise descriptive title based on the inspected image and its intended role.
- `destination_dir` is a repository-relative directory under `images/` or `novel/`. Do not use `images/takeout/`, `images/takeout/webp/`, `images/webp/`, or `images/scripts/`.

The processor turns the title into a lowercase, hyphen-separated filename slug, removes common diacritics, and prefixes the asset ID when supplied. For the example above, it creates:

- Master: `novel/Novel-02/assets/illustrations/ARC-001/SCN-001/ILL-001-shared-discovery.png`
- WebP: `novel/Novel-02/assets/illustrations/ARC-001/SCN-001/ILL-001-shared-discovery.webp`

The original is moved byte-for-byte to its master path. The WebP is a separate delivery derivative beside it. Existing files are never overwritten.

Before relocation, each WebP is written to persistent staging under `images/takeout/webp/[batch-id]/attempt-NNN/`. Its name is the exact incoming filename with `.webp` appended, so `IMG_001.png` becomes `IMG_001.png.webp` and `IMG_001.jpg` becomes `IMG_001.jpg.webp`. This retains the original extension in staging and avoids collisions between different source formats with the same basename.

## Processing and success conditions

The existing workflow, `.github/workflows/convert-images-to-webp.yml`, runs on pushes to the takeout files or hand-off and can also be started manually on branch `gpt`.

It validates the entire batch, converts all images into the persistent attempt-specific staging folder `images/takeout/webp/[batch-id]/attempt-NNN/`, verifies the staged WebPs, and only then relocates the original masters and WebP derivatives to their permanent destinations. The CSV records each staging path as well as the final path. The processor checks source/master SHA-256 equality, WebP signatures and file lengths, destination collisions, and exact manifest coverage.

If validation or conversion fails, original uploads remain in the intake, the hand-off remains ready, and every successfully converted WebP remains in that failed attempt's staging folder for inspection. A retry uses a fresh numbered attempt and does not overwrite earlier staging. On success, staged WebPs are moved to their final destinations and the now-empty successful staging attempt directory is removed.

A batch is successful only after every master and WebP is verified, the original hand-off and reports are archived, and the active hand-off is reset to empty. The workflow commits the completed operation together. A failed attempt does not clear the hand-off; correcting it and retrying the same batch ID creates another numbered attempt.

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
