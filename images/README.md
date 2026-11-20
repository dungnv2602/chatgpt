# Image Assets and WebP Delivery

This directory stores retained image masters, non-novel visual assets, and user-upload intake.

Novel illustration files belong in each novel's asset library under `novels/[Novel-ID]/assets/illustrations/`.

## Universal intake

Place every uploaded image that needs repository retention in [images/takeout/](takeout/README.md).

Incoming filenames may use any name. The assistant inspects each image. It prepares a title and destination, then records them in `HANDOFF.yml`.

The Action does not infer image content or project membership.

Place image files directly in `images/takeout/`. Do not create upload subfolders.

The Action reserves two intake subdirectories:

- `history/` stores processing reports.
- `webp/` stores staged WebP files.

Do not place uploads in either directory.

The Action processes only a ready hand-off. It accepts static PNG, JPG, and JPEG files. It reports unsupported formats and APNG as failures. It does not flatten animated images.

## Naming and destination rules

Each hand-off item specifies:

- The exact incoming filename in `source`.
- An optional stable ID in `asset_id`, such as `ILL-001`.
- A descriptive title in `title`.
- A repository-relative destination in `destination_dir`.

Use `images/`, `novels/`, or `drawings/YYYY-MM-DD/images/` as the destination root.

The processor creates a lowercase filename slug from the title. It replaces spaces with hyphens and removes common diacritics. It prefixes the stable ID when the hand-off supplies one.

For example, the title `Shared Discovery` with ID `ILL-001` creates:

- Master: `ILL-001-shared-discovery.png`
- WebP derivative: `ILL-001-shared-discovery.webp`

The processor moves the original bytes to the master path. It stores the WebP derivative beside the master. It never overwrites an existing destination file.

## GitHub Action

The [WebP/takeout workflow](../.github/workflows/convert-images-to-webp.yml) runs the approved conversion process. It uses `cwebp` and the profiles below.

The processor is [`skills/session-archiving/scripts/process_takeout.py`](../skills/session-archiving/scripts/process_takeout.py).

The workflow checks the complete hand-off before it moves any original. It converts the full batch into persistent staging under `images/takeout/webp/[batch-id]/attempt-NNN/`.

Each staged filename preserves the incoming filename. It appends `.webp`. For example, `camera.png` becomes `camera.png.webp`.

The workflow checks every staged WebP before it moves an original. It then moves each verified WebP to its final destination.

The processor checks the original master with SHA-256. It also checks WebP signatures, output hashes, destination collisions, and hand-off coverage.

The workflow commits the completed batch as one operation.

If conversion or verification fails, the workflow keeps the hand-off ready. It restores original files to the intake when rollback succeeds. It retains successful staged WebP files in the matching attempt folder.

A retry uses a new attempt directory. A successful batch moves staged files to their final destinations. It removes the empty staging directory. The workflow archives a diagnostic report for each attempt.

## Conversion profiles

| Source | Encoder profile | Result |
|---|---|---|
| PNG | `-lossless -q 100 -m 6 -exact` | Lossless. Preserves RGB values in fully transparent pixels. |
| JPEG | `-preset picture -q 92 -m 6 -sharp_yuv` | High-quality lossy output. It is not pixel-identical. |

Both profiles copy ICC profiles.

The WebP files do not retain EXIF or XMP metadata. The unchanged original masters retain that metadata.

## Reports and processing history

The processor stores every attempt under:

```text
images/takeout/history/[batch-id]/attempt-NNN/
  HANDOFF.yml
  conversion-report.csv
  verification-report.md
```

The CSV records source, staging, and destination paths. It also records the title, ID, format, encoder profile, encoder version, byte counts, size difference, SHA-256 values, status, and errors.

A negative size reduction means that the WebP file is larger than the original. The workflow still retains that derivative.

The Markdown report records the batch outcome, checks, warnings, and errors.

The `history/` archive and `webp/` staging directory are reserved. The intake detector does not treat either directory as a source of new uploads.

See [Image Takeout](takeout/README.md) for the hand-off schema and operating procedure.

## Documentation standard

This README is technical documentation. Apply the repository [ASD-STE100 writing policy](../skills/asd-ste100/references/repository-writing-policy.md) when you revise it.
