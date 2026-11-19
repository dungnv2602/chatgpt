# Image Takeout

This is the single intake location for user-uploaded images intended for retention in this repository, whether they belong to a novel, a drawing session, a visual-reference collection, or another project.

## Upload rules

- Upload every image directly into `images/takeout/`; do not create subfolders.
- Incoming filenames may be arbitrary. The user does not need to rename them.
- Keep one active batch in `HANDOFF.yml`.
- The Action does nothing until `HANDOFF.yml` has `status: ready`.
- When the hand-off is ready, every image in the folder must be listed exactly once.
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
```

For each item:

- `source` is the exact uploaded filename at the top level of this folder.
- `asset_id` is optional for general image assets. Novel illustrations use their stable `ILL-NNN` ID.
- `title` is a concise descriptive title based on the inspected image and its intended role.
- `destination_dir` is a repository-relative directory under `images/` or `novel/`. Do not use `images/takeout/`, `images/webp/`, or `images/scripts/`.

The processor turns the title into a lowercase, hyphen-separated filename slug, removes common diacritics, and prefixes the asset ID when supplied. For the example above, it creates:

- Master: `novel/Novel-02/assets/illustrations/ARC-001/SCN-001/ILL-001-shared-discovery.png`
- WebP: `novel/Novel-02/assets/illustrations/ARC-001/SCN-001/ILL-001-shared-discovery.webp`

The original is moved byte-for-byte to its master path. The WebP is a separate delivery derivative beside it. Existing files are never overwritten.

## Processing and success conditions

The existing workflow, `.github/workflows/convert-images-to-webp.yml`, runs on pushes to the takeout files or hand-off and can also be started manually on branch `gpt`.

It validates the entire batch, converts all images into temporary runner storage, and only then relocates originals and publishes WebP derivatives. It checks source/master SHA-256 equality, WebP signatures and file lengths, destination collisions, and exact manifest coverage. If validation or conversion fails, sources remain in the intake and the hand-off remains ready. The workflow records a diagnostic attempt.

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

The CSV records source and destination paths, title and ID, source format, encoder profile and version, original/WebP byte counts, size difference, SHA-256 values, verification status, and errors. A negative size reduction is valid: it means the WebP is larger than the original.

The Markdown verification report records the batch outcome, checks, and warnings/errors. Failed attempts are retained for inspection. The history directory is excluded from intake detection and is never reprocessed as uploaded content.

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
