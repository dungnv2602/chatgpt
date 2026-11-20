# Image Processing Scripts

The Session Archiving skill owns the executable tools for the image takeout and publication-verification workflow. The scripts live beside this skill because they implement its archival, integrity, rollback, and publication responsibilities.

## Files

- `scripts/process_takeout.py` — validates one `images/takeout/` hand-off, checks destination safety and source identity, converts PNG/JPEG to WebP, stages the complete batch before relocation, updates drawing-session records/manifests, and writes success or failure reports with rollback handling.
- `scripts/verify_published_manifest.py` — reads the pushed Git ref and verifies published master/WebP blobs, checksums, canonical WebP URLs, and drawing-session links before updating or checking manifest verification status.
- `scripts/test_process_takeout_unittest.py` — regression suite for the processor and publication verifier. It imports the verifier from the same directory and invokes the processor by its sibling path. Keep all three files together.

## Dependencies

- Python 3.
- PyYAML for the takeout processor.
- `cwebp` from the WebP package for actual image conversion. The regression suite uses a fake encoder and does not need to modify real image assets.

## Run from the repository root

Compile both production scripts:

```bash
python3 -m py_compile \
  skills/session-archiving/scripts/process_takeout.py \
  skills/session-archiving/scripts/verify_published_manifest.py
```

Run the regression suite:

```bash
python3 -m unittest discover \
  -s skills/session-archiving/scripts \
  -p 'test_process_takeout_unittest.py' \
  -v
```

Process a ready takeout hand-off:

```bash
python3 skills/session-archiving/scripts/process_takeout.py \
  --repo-root . \
  --run-id "$GITHUB_RUN_ID"
```

Verify published assets after the first push:

```bash
python3 skills/session-archiving/scripts/verify_published_manifest.py \
  --repo-root . \
  --git-ref origin/gpt \
  --branch gpt
```

Run the final read-only verification:

```bash
python3 skills/session-archiving/scripts/verify_published_manifest.py \
  --repo-root . \
  --git-ref origin/gpt \
  --branch gpt \
  --check-only
```

## Operating rules

1. Treat `images/takeout/HANDOFF.yml` as the explicit batch contract. The scripts do not infer image content, project membership, prompt association, or native generation identifiers.
2. Keep original PNG/JPEG masters byte-identical and separate from WebP derivatives.
3. Use `novels/` (plural) for novel-scene assets. The obsolete `novel/` root is not a valid destination.
4. Keep drawing-session outputs under `drawings/YYYY-MM-DD/images/` with an explicit attempt number so the processor can reconcile the attempt record, README, and manifest.
5. Do not report a batch or publication as verified merely because a script was invoked. Require successful process output, published Git read-back, and the final `--check-only` result.
6. Update the GitHub workflow's script paths and test-discovery directory whenever these files are moved. The workflow is the execution caller. This reference documents the scripts and their supported invocation.
