# Takeout Processing — 2026-11-20-001

- Batch: 2026-11-20-001
- Attempt: attempt-002
- Status: FAILED
- Items processed: 18
- Generated: 2026-11-24T02:25:05+00:00

## Verification checks
- Inbox is flat and contains only PNG/JPG/JPEG uploads, README.md, HANDOFF.yml, and the reserved history/ and webp/ directories.
- Every uploaded image is listed exactly once; no unlisted or untracked image will be processed.
- Every mapped item has an existing conversation-integrity record with an exact image-source mapping; drawing outputs also match the attempt record asset ID and generation ID.
- 7 unclassified image(s) will be converted to WebP without relocation; their original files will remain unchanged in images/takeout/: file_000000001e9882079286e1de59e27f1b.png, file_000000004b9c82119aa3e8e273bb1f2c.png, file_0000000064d08211910f68838cb1237a.png, file_0000000069f082079011ee0627b3995c.png, file_000000008c6882118eba4e134b3a76c2.png, file_00000000dfa08211a68e0644d6c6f2a1.png, file_00000000e5e482118465d6df866ea0d9.png
- Uploaded originals matching supplied generation-time SHA-256 values were identified.
- Generation-time SHA-256 matching was unavailable for items without expected_sha256.
- Mapped destinations are restricted to approved images/, novels/, or dated drawings/ asset folders; duplicate and existing paths are rejected.
- Batch was not marked successful; sources were restored to takeout and converted WebPs were retained in staging where rollback succeeded.

## Errors and warnings
- Daily README must contain exactly one attempt table with an Image column: drawings/2026-11-21/README.md
