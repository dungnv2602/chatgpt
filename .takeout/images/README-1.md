# Image Assets and WebP Delivery

This directory supports shared image intake and retained image masters. WebP files are separate delivery derivatives.

## Destinations

- General retained assets: the declared destination under `images/`.
- Non-novel drawing outputs: `drawings/YYYY-MM-DD/images/`.
- Novel illustrations: `novels/[Novel-ID]/assets/illustrations/[ARC-ID]/[SCN-ID]/`.

The Worker preserves each original byte-for-byte in the destination's `original/` folder. It stores the WebP derivative in the destination root. Do not overwrite an existing asset.

## Shared intake

Send every new upload that requires repository retention to the flat `images/takeout/` intake. Do not create upload subfolders or place uploads in the reserved `history/` and `webp/` directories.

The normal Action accepts static PNG, JPG, and JPEG files. It rejects unsupported formats and does not flatten animated images. Every mapped hand-off item must reference a dated conversation-integrity record with an exact source-mapping row. Drawing outputs must also match the attempt's recorded Generation ID or Output ID. Keep the platform source_asset_id separate from the repository asset_id used for filename prefixes. Incomplete provenance stays in intake and must not trigger relocation. An item marked `images/unclassified` is converted by the same normal Action, but its original remains in intake and its WebP remains under `takeout/webp/unclassified/`. The processor does not classify it, invent provenance, relocate it, or edit project indexes.

## Workflow ownership

The Worker owns image inspection, provenance, processing, original preservation, and publication verification. The Action uses:

- Processor: [`process_takeout.py`](../../.agent/skills/the-worker/scripts/process_takeout.py).
- Workflow: [`convert-images-to-webp.yml`](../../.github/workflows/convert-images-to-webp.yml).
- Canonical hand-off and operating procedure: [Image Takeout](README-2.md).

Use Image Takeout for the `HANDOFF.yml` schema, conversion profiles, staging and retry behavior, reports, manifest updates, and published-blob checks. Do not duplicate those procedures here.

Drawing attempt records and daily indexes link to verified WebP delivery files. Original masters remain preserved separately. See the [Drawing archive and delivery rules](../../.agent/skills/drawing/references/archive-and-delivery.md) for session-specific records.

## Documentation standard

Apply the repository [ASD-STE100 writing policy](../../.agent/skills/asd-ste100/references/repository-writing-policy.md) when you revise this README.
