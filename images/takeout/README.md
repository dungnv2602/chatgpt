# Image Takeout

Use this directory as the single intake location for images that need repository retention.

Images may belong to a novel, a drawing session, a visual-reference collection, or another project.

## Upload rules

- Upload each image directly to `images/takeout/`.
- Do not create upload subfolders.
- Incoming filenames may use any name. The user does not need to rename them.
- Do not place uploads in `history/` or `webp/`. The Action manages these reserved directories.
- Keep one active batch in `HANDOFF.yml`.
- The Action processes a batch only when `HANDOFF.yml` has `status: ready`.
- List every top-level image in the ready hand-off exactly once.
- The pipeline accepts static PNG, JPG, and JPEG files.
- The pipeline rejects APNG, GIF, WebP, HEIC, AVIF, TIFF, BMP, and other formats. It does not flatten animated images.

## Hand-off format

The assistant inspects each image. It then determines the title and destination from the project context.

The assistant assigns a stable asset ID when needed. It writes these values to the hand-off.

The Action does not infer the image's subject, title, ID, project, or destination.

```yaml
version: 1
batch_id: "2026-11-20-001"
status: ready
items:
  - source: "IMG_20261120_091522.png"
    asset_id: "ILL-001"
    title: "Shared Discovery"
    destination_dir: "novels/Novel-02/assets/illustrations/ARC-001/SCN-001"
    # Include only provenance values actually captured:
    expected_sha256: "0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef"
    output_id: "A001-O01"
    prompt_id: "P001"
    native_generation_id: "platform-generation-id-if-exposed"
    native_output_id: "platform-output-id-if-exposed"
    approval_status: "Not recorded"
    mapping_evidence: "Direct generation-return association recorded at generation time"
```

For a drawing-session output, include `expected_sha256` when the generation-time original hash exists.

The processor hashes the uploaded original before conversion. It compares that hash with the expected value.

A mismatch does not reject the image. The processor retains the image and marks its mapping status as `Probable`. It does not mark the mapping as `Verified` from that hash.

Record internal `output_id`, `prompt_id`, and exposed native IDs separately. Use values from generation-time records. Do not infer them from filenames.

The conversion report keeps these hash fields separate:

- `generation_sha256` is the expected hash from generation time.
- `source_sha256` is the hash of the uploaded original.
- `hash_match` records the comparison result.

The WebP hash is separate because conversion changes the bytes.

For drawing-session uploads, the processor also updates `drawings/YYYY-MM-DD/manifest.csv`. It records new outputs and inventories legacy WebP files. It pairs a legacy WebP with a same-stem master in `images/original/` when one exists.

The processor records the actual master hash. Publication remains Pending until the workflow checks the remote Git blobs.

A legacy WebP without an original remains Not verifiable. An original without a same-stem WebP blocks the batch.

## Hand-off fields

Each item uses these fields:

- `source` is the exact uploaded filename in this directory's top level.
- `asset_id` is optional for general image assets. Novel illustrations use a stable `ILL-NNN` ID.
- `title` is a short description based on the inspected image and its intended role.
- `destination_dir` is a repository-relative directory under `images/`, `novels/`, or `drawings/YYYY-MM-DD/images`.
- `attempt` is mandatory for drawing-session destinations.

Do not use `images/takeout/`, `images/takeout/webp/`, `images/webp/`, or the reserved legacy path `images/scripts/` as a destination.

The Action rejects drawing-session uploads without an explicit attempt number. This rule prevents omissions from the session manifest and prompt records.

## Output filenames

The processor creates a lowercase, hyphen-separated slug from the title. It removes common diacritics. It prefixes the asset ID when the hand-off supplies one.

The example item creates these files:

- Original master: `novels/Novel-02/assets/illustrations/ARC-001/SCN-001/original/ILL-001-shared-discovery.png`
- WebP delivery file: `novels/Novel-02/assets/illustrations/ARC-001/SCN-001/ILL-001-shared-discovery.webp`

The processor moves the original bytes to the destination's `original/` folder. It stores the WebP file in the destination root.

Attempt records and daily READMEs link only to the WebP file. The original master remains unchanged. The processor never overwrites an existing file.

## WebP staging

Before relocation, the processor writes each WebP file to persistent staging:

```text
images/takeout/webp/[batch-id]/attempt-NNN/
```

The staged filename preserves the exact incoming filename. It appends `.webp`.

For example:

- `IMG_001.png` becomes `IMG_001.png.webp`.
- `IMG_001.jpg` becomes `IMG_001.jpg.webp`.

This naming rule preserves the source extension. It also prevents collisions between formats that share a basename.

## Processing and success conditions

The [WebP workflow](../../.github/workflows/convert-images-to-webp.yml) runs when intake files or the hand-off change. You can also start it manually on branch `gpt`.

The workflow validates the complete batch. It converts every image into the attempt-specific staging folder. It verifies each staged WebP before it relocates any original.

The CSV records each staging path and final path.

The processor checks:

- Source and master SHA-256 equality.
- WebP signatures and file lengths.
- Destination collisions.
- Exact hand-off coverage.
- Attempt metadata for each drawing-session upload.

If validation or conversion fails, the original uploads remain in the intake. The hand-off remains ready.

Every WebP that the processor converted successfully remains in the failed attempt's staging folder. A retry uses a new numbered attempt. It does not overwrite earlier staging.

On success, the processor moves staged WebP files to their final destinations. It then removes the empty staging directory.

## Published drawing-session verification

For drawing outputs, the session manifest starts with publication status `Pending`.

After the Action pushes the assets and Markdown changes, a second step reads the exact blobs from `origin/gpt`.

That step checks:

- Original master SHA-256.
- WebP SHA-256.
- Canonical WebP URL.
- Daily README image-inventory link.
- Attempt-table link.
- Attempt-note WebP link.

The verifier updates the manifest after these checks.

The final check-only pass confirms that the published manifest matches the Git branch.

The workflow records failed publication checks as `Failed` before the final check fails.

Legacy assets without retained originals remain `Not verifiable`. The workflow still checks their WebP URL and derivative hash.

A batch succeeds only after local verification of every master and WebP. The processor must also archive the original hand-off and reports. It clears the active hand-off last.

A failed attempt does not clear the hand-off. Correct the hand-off and retry the same batch ID. The retry creates another numbered attempt.

## History and reports

The processor retains each attempt under:

```text
images/takeout/history/
└── [batch-id]/
    └── attempt-001/
        ├── HANDOFF.yml
        ├── conversion-report.csv
        └── verification-report.md
```

The CSV records source, staging, and final paths. It also records the title, ID, source format, encoder profile, encoder version, original and WebP byte counts, size difference, SHA-256 values, verification status, and errors.

A negative size reduction means the WebP is larger than the original. This is a valid result.

The Markdown report records the batch outcome, checks, warnings, and errors. The workflow retains failed attempts for review.

The `history/` and `webp/` directories are reserved. The intake detector does not process them as new uploads.

The active hand-off starts in this state:

```yaml
version: 1
status: empty
items: []
```

## Conversion profiles

| Source | Encoder profile | Result |
|---|---|---|
| PNG | `-lossless -q 100 -m 6 -exact` | Lossless. Preserves RGB values in fully transparent pixels. |
| JPEG | `-preset picture -q 92 -m 6 -sharp_yuv` | High-quality lossy output. It is not pixel-identical. |

Both profiles copy ICC profiles.

The WebP file does not retain EXIF or XMP metadata. The original master retains that metadata.

## Drawing-session manifest

For each upload with an explicit `attempt` and a destination under `drawings/YYYY-MM-DD/images`, the processor updates that session's `manifest.csv`.

It adds one row per output. It preserves existing rows and columns. It adds missing required columns. It also inventories top-level WebP files that lack manifest rows.

The required columns are:

```csv
session_date,image_id,filename,prompt_id,approval_status,github_url,sha256,verification_status
```

Additional columns keep these values separate:

- Internal output ID.
- Native Generation ID and native output ID.
- Attempt number.
- Mapping evidence and mapping status.
- Original and WebP paths and hashes.
- Generation-time hash and hash-match result.
- Original-byte availability and verification error.

The processor applies these rules:

- New uploads record the uploaded-original SHA-256 in `sha256` and `original_sha256`. WebP bytes use `webp_sha256`.
- A generation-time hash match can set mapping status to `Verified`.
- An explicit attempt without a generation-time hash keeps mapping status `Corroborated`. The processor does not infer mapping from filenames.
- New rows start with `verification_status: Pending`.
- Only the post-push verifier can change that status to `Verified`. It must read the exact original and WebP blobs from `origin/gpt` and check the WebP URL.
- The processor pairs existing WebP files with same-stem files in the `original/` folder when available.
- It calculates the retained master's SHA-256. The row remains `Pending` until the workflow reads back the master and WebP blobs.
- WebP files without masters remain `Not verifiable`. The processor does not invent an original checksum.
- An original master without a matching WebP blocks processing.
- Internal fallback image IDs include a per-upload filename discriminator. Separate outputs with identical bytes therefore receive separate manifest rows.
- These internal IDs are archive identifiers. They are not native platform IDs.
- Approval remains separate from mapping and verification. Missing approval, prompt IDs, native IDs, or generation hashes remain blank or `Not recorded`.

The README and attempt records link only to WebP delivery files. The unchanged original master remains in the destination's `original/` folder and in the session manifest.

## Documentation standard

This file defines an operational hand-off. Apply Strict mode from the repository [ASD-STE100 policy](../../skills/asd-ste100/references/repository-writing-policy.md) when you revise it. Preserve every field, status, path, conversion rule, and verification requirement.
