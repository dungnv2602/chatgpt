# Image Processing Scripts

The Worker owns the image-intake and publication-verification tools. The scripts sit in `.agent/skills/the-worker/scripts/`. They support archival, integrity, rollback, and publication checks.

## Files

- `.agent/skills/the-worker/scripts/process_takeout.py` — checks one `images/takeout/` hand-off. It checks destination safety and source identity. It converts PNG and JPEG files to WebP. It stages the full batch before relocation. It updates drawing-session records and manifests. It writes success or failure reports and handles rollback.
- `.agent/skills/the-worker/scripts/verify_published_manifest.py` — reads the pushed Git ref. It checks published master and WebP blobs, checksums, canonical WebP URLs, and drawing-session links. It then updates or checks manifest status.
- `.agent/skills/the-worker/scripts/test_process_takeout_unittest.py` — tests the processor and publication verifier. It imports the verifier from this directory. It runs the processor by its sibling path. Keep all three files together.

## Dependencies

- Python 3.
- PyYAML for the takeout processor.
- `cwebp` from the WebP package for image conversion. The regression suite uses a fake encoder. It does not modify real image assets.

## Run from the repository root

Compile both production scripts:

```bash
python3 -m py_compile \
    .agent/skills/the-worker/scripts/process_takeout.py \
    .agent/skills/the-worker/scripts/verify_published_manifest.py
```

Run the regression suite:

```bash
python3 -m unittest discover \
  -s .agent/skills/the-worker/scripts \
  -p 'test_process_takeout_unittest.py' \
  -v
```

Process a ready takeout hand-off:

```bash
python3 .agent/skills/the-worker/scripts/process_takeout.py \
  --repo-root . \
  --run-id "$GITHUB_RUN_ID"
```

Check published assets after the first push:

```bash
python3 .agent/skills/the-worker/scripts/verify_published_manifest.py \
  --repo-root . \
  --git-ref origin/gpt \
  --branch gpt
```

Run the final read-only check:

```bash
python3 .agent/skills/the-worker/scripts/verify_published_manifest.py \
  --repo-root . \
  --git-ref origin/gpt \
  --branch gpt \
  --check-only
```

## Operating rules

1. Treat `images/takeout/HANDOFF.yml` as the explicit batch contract. The scripts do not infer image content, project membership, prompt association, or native generation IDs.
2. Keep original PNG and JPEG masters byte-identical. Store WebP derivatives separately.
3. Use `area/novel/` for novel-scene assets. The processor accepts reconstructed project roots.
4. Store drawing-session outputs under `area/drawing/YYYY-MM-DD/images/`. Include an explicit attempt number. The processor uses it to reconcile the attempt record, README, and manifest.
5. Do not report a batch or publication as verified because a script ran. Require successful process output, published Git read-back, and the final `--check-only` result.
6. Update the GitHub workflow's script paths and test-discovery directory when these files move. The workflow calls the scripts. This reference documents their responsibilities and supported commands.

## Documentation standard

This file is technical documentation. Apply Strict mode from the repository [ASD-STE100 policy](../../asd-ste100/references/repository-writing-policy.md) when you revise it. Preserve command names, paths, behavior, and verification requirements.
