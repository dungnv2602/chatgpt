# Image Assets and WebP Delivery

This directory contains retained image masters, non-novel visual assets, and the universal user-upload intake. Novel illustration binaries live inside each novel's central asset library under `novel/[Novel-ID]/assets/illustrations/`.

## Universal intake

All user-uploaded images intended for repository retention enter through [`images/takeout/`](takeout/README.md). Incoming filenames may be arbitrary. The assistant inspects the images, decides their descriptive titles and destinations, and writes the structured `HANDOFF.yml`. The Action never guesses image content or project membership.

The intake is flat: place image files directly in `images/takeout/`, not in subfolders. The Action processes only a ready hand-off and only static PNG, JPG, and JPEG. Unsupported formats and APNG are reported as failures rather than silently flattened.

## Naming and destination rules

Each hand-off item specifies:

- the exact incoming filename (`source`);
- an optional stable ID (`asset_id`, e.g. `ILL-001`);
- a descriptive title (`title`);
- a repository-relative `destination_dir` under `images/` or `novel/`.

The processor converts the title into a lowercase, hyphen-separated slug, removes common diacritics, and prefixes the stable ID when supplied. For example, an item with ID `ILL-001` and title `Shared Discovery` becomes:

- Master: `ILL-001-shared-discovery.png`
- WebP derivative: `ILL-001-shared-discovery.webp`

The original is moved byte-for-byte to the master path. The WebP is a separate delivery derivative stored beside it. Existing destination files are never overwritten.

## Existing GitHub Action

The existing [WebP/takeout workflow](../.github/workflows/convert-images-to-webp.yml) uses `cwebp` and the tested conversion profiles below. Its processor is [`images/scripts/process_takeout.py`](scripts/process_takeout.py).

The workflow validates the complete hand-off and converts the complete batch into temporary runner storage before relocating any original. It verifies the original master by SHA-256, verifies WebP container signatures and output hashes, checks for destination collisions, and confirms every image in the intake is listed exactly once.

The workflow commits the completed operation together. A failed conversion or verification leaves the active hand-off ready and restores originals to the intake where rollback succeeds. It archives a diagnostic attempt and does not claim success.

## Conversion profiles

| Source | Profile | Fidelity |
|---|---|---|
| PNG | `-lossless -q 100 -m 6 -exact` | Lossless encoding, including RGB values in fully transparent pixels |
| JPEG | `-preset picture -q 92 -m 6 -sharp_yuv` | High-quality lossy encoding; not pixel-identical |

Both profiles request ICC profile copying. EXIF and XMP are not copied into WebP; they remain in the unchanged original master.

## Reports and processing history

Every attempt, successful or failed, is retained under:

```text
images/takeout/history/[batch-id]/attempt-NNN/
  HANDOFF.yml
  conversion-report.csv
  verification-report.md
```

The CSV records source and destination paths, title and ID, format, encoder profile and version, original and WebP sizes, size difference, SHA-256 values, status, and errors. A negative size reduction means the WebP is larger than the original; the derivative is still retained for inspection.

The verification report records the checks, outcome, warnings, and errors. The history tree is excluded from intake detection and is never processed as new uploaded content.

See [the takeout instructions](takeout/README.md) for the complete hand-off schema and operating procedure.
