#!/usr/bin/env python3
"""Regression tests for the exact takeout processor used by the GitHub Action."""
import csv
import hashlib
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from verify_published_manifest import github_blob_url, verify_manifest_row, verify_session_links

PROCESSOR = Path(__file__).with_name("process_takeout.py")

FAKE_CWEBP = r'''#!/usr/bin/env python3
import pathlib
import sys

args = sys.argv[1:]
if args == ["-version"]:
    print("fake-cwebp 1.0")
    raise SystemExit(0)
if "-o" not in args:
    print("missing output argument", file=sys.stderr)
    raise SystemExit(2)
output = pathlib.Path(args[args.index("-o") + 1])
payload = b"simulated-webp-payload"
output.write_bytes(
    b"RIFF" + (len(payload) + 4).to_bytes(4, "little") + b"WEBP" + payload
)
'''

class TakeoutProcessorTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.inbox = self.root / "images" / "takeout"
        self.inbox.mkdir(parents=True)
        self.bin_dir = self.root / "bin"
        self.bin_dir.mkdir()
        encoder = self.bin_dir / "cwebp"
        encoder.write_text(FAKE_CWEBP, encoding="utf-8")
        encoder.chmod(0o755)

    def tearDown(self):
        self.temp.cleanup()

    def run_processor(self):
        env = os.environ.copy()
        env["PATH"] = str(self.bin_dir) + os.pathsep + env.get("PATH", "")
        return subprocess.run(
            [
                sys.executable,
                str(PROCESSOR),
                "--repo-root",
                str(self.root),
                "--run-id",
                "unit-test",
            ],
            env=env,
            text=True,
            capture_output=True,
            check=False,
        )

    def manifest(self, item, batch="batch-test"):
        self.manifest_many([item], batch)

    def manifest_many(self, items, batch="batch-test"):
        rows = [
            "version: 1",
            f'batch_id: "{batch}"',
            "status: ready",
            "items:",
        ]
        for index, item in enumerate(items):
            asset_id = item.get("asset_id", "ILL-%03d" % (index + 1))
            rows.extend([
                f'  - source: "{item["source"]}"',
                f'    asset_id: "{asset_id}"',
                f'    title: "{item.get("title", "Shared Discovery")}"',
                (
                    "    destination_dir: "
                    f'"{item.get("destination_dir", "novels/Novel-02/assets/illustrations/ARC-001/SCN-001")}"'
                ),
            ])
            if "attempt" in item:
                rows.append(f'    attempt: "{item["attempt"]}"')
            for key in (
                "expected_sha256", "output_id", "prompt_id", "native_generation_id",
                "native_output_id", "approval_status", "mapping_evidence",
            ):
                if key in item:
                    rows.append(f'    {key}: "{item[key]}"')
        (self.inbox / "HANDOFF.yml").write_text("\n".join(rows) + "\n", encoding="utf-8")

    def test_success_moves_byte_identical_master_creates_webp_and_archives_reports(self):
        original = b"uploaded-original-bytes"
        (self.inbox / "IMG_001.PNG").write_bytes(original)
        self.manifest({"source": "IMG_001.PNG"})

        result = self.run_processor()
        self.assertEqual(result.returncode, 0, result.stderr)

        destination = (
            self.root
            / "novels/Novel-02/assets/illustrations/ARC-001/SCN-001"
        )
        master = destination / "original/ILL-001-shared-discovery.PNG"
        webp = destination / "ILL-001-shared-discovery.webp"
        self.assertEqual(master.read_bytes(), original)
        self.assertTrue(webp.read_bytes().startswith(b"RIFF"))
        self.assertFalse((self.inbox / "IMG_001.PNG").exists())
        self.assertEqual(
            (self.inbox / "HANDOFF.yml").read_text(encoding="utf-8"),
            "version: 1\nstatus: empty\nitems: []\n",
        )

        history = self.inbox / "history/batch-test/attempt-001"
        for name in ("HANDOFF.yml", "conversion-report.csv", "verification-report.md"):
            self.assertTrue((history / name).is_file(), name)
        with (history / "conversion-report.csv").open(encoding="utf-8") as handle:
            row = next(csv.DictReader(handle))
        self.assertEqual(row["status"], "RELOCATED_AND_VERIFIED")
        self.assertEqual(row["master_sha256"], row["source_sha256"])
        self.assertTrue(row["webp_sha256"])
        self.assertEqual(
            row["staging_webp_path"],
            "images/takeout/webp/batch-test/attempt-001/IMG_001.PNG.webp",
        )
        self.assertFalse((self.inbox / "webp/batch-test/attempt-001").exists())


    def test_attempt_output_upload_updates_attempt_record_and_readme(self):
        session = self.root / "drawings/2026-11-19"
        session.mkdir(parents=True)
        attempt_record = session / "attempt-01.md"
        attempt_record.write_text(
            "# Attempt 01 — Partial unapproved portrait\n\n"
            "- **Outcome:** Generated, but the requested visual target was only partially met.\n"
            "- **User approval:** Not approved; user review pending.\n",
            encoding="utf-8",
        )
        readme = session / "README.md"
        readme.write_text(
            "# Drawing session\n\n"
            "| Attempt / prompt | Session / brief | Series / baseline lineage | Execution outcome | User approval / output evidence | Image |\n"
            "|---|---|---|---|---|---|\n"
            "| [01 — Partial unapproved portrait](attempt-01.md) | Session | Standalone | Generated; partial result | User review pending | Waiting for image upload |\n",
            encoding="utf-8",
        )
        (self.inbox / "portrait.png").write_bytes(b"portrait-original")
        (self.inbox / "portrait-alt.png").write_bytes(b"portrait-alternative-original")
        self.manifest_many(
            [
                {
                    "source": "portrait.png",
                    "asset_id": "",
                    "title": "Partial Portrait",
                    "destination_dir": "drawings/2026-11-19/images",
                    "attempt": "1",
                },
                {
                    "source": "portrait-alt.png",
                    "asset_id": "",
                    "title": "Partial Portrait Alternative",
                    "destination_dir": "drawings/2026-11-19/images",
                    "attempt": "1",
                },
            ],
            batch="batch-session-link",
        )

        result = self.run_processor()
        self.assertEqual(result.returncode, 0, result.stderr)

        image_dir = session / "images"
        master = image_dir / "original/partial-portrait.png"
        webp = image_dir / "partial-portrait.webp"
        alt_master = image_dir / "original/partial-portrait-alternative.png"
        alt_webp = image_dir / "partial-portrait-alternative.webp"
        self.assertEqual(master.read_bytes(), b"portrait-original")
        self.assertEqual(alt_master.read_bytes(), b"portrait-alternative-original")
        self.assertTrue(webp.is_file())
        self.assertTrue(alt_webp.is_file())
        attempt_text = attempt_record.read_text(encoding="utf-8")
        readme_text = readme.read_text(encoding="utf-8")
        self.assertIn("[partial-portrait.webp](images/partial-portrait.webp)", attempt_text)
        self.assertIn("[partial-portrait-alternative.webp](images/partial-portrait-alternative.webp)", attempt_text)
        self.assertIn("[partial-portrait.webp](images/partial-portrait.webp)", readme_text)
        self.assertIn("[partial-portrait-alternative.webp](images/partial-portrait-alternative.webp)", readme_text)
        self.assertNotIn("partial-portrait.png", attempt_text)
        self.assertNotIn("partial-portrait-alternative.png", attempt_text)
        self.assertNotIn("partial-portrait.png", readme_text)
        self.assertNotIn("partial-portrait-alternative.png", readme_text)
        self.assertNotIn("Waiting for image upload", readme_text)

        manifest_path = session / "manifest.csv"
        self.assertTrue(manifest_path.is_file())
        with manifest_path.open(encoding="utf-8", newline="") as handle:
            manifest_rows = list(csv.DictReader(handle))
        self.assertEqual(len(manifest_rows), 2)
        self.assertEqual({row["attempt"] for row in manifest_rows}, {"01"})
        self.assertEqual({row["approval_status"] for row in manifest_rows}, {"Not recorded"})
        self.assertEqual({row["verification_status"] for row in manifest_rows}, {"Pending"})
        self.assertEqual({row["mapping_status"] for row in manifest_rows}, {"Corroborated"})
        self.assertIn(
            "## Image inventory — 2 WebP delivery files + 2 original masters (4 files total)",
            readme_text,
        )
        self.assertTrue(all(row["sha256"] for row in manifest_rows))
        self.assertTrue(all(row["webp_sha256"] for row in manifest_rows))
        self.assertTrue(all(row["github_url"].endswith(".webp") for row in manifest_rows))
        self.assertTrue(all("/original/" in row["original_path"] for row in manifest_rows))
        self.assertIn("User review pending", readme_text)
        self.assertIn("Generated; partial result", readme_text)

        with (self.inbox / "history/batch-session-link/attempt-001/conversion-report.csv").open(encoding="utf-8") as handle:
            rows = list(csv.DictReader(handle))
        self.assertEqual(len(rows), 2)
        self.assertEqual({row["attempt"] for row in rows}, {"01"})

    def test_unlisted_image_fails_without_moving_sources_or_clearing_handoff(self):
        (self.inbox / "listed.jpg").write_bytes(b"listed-image")
        (self.inbox / "extra.png").write_bytes(b"unlisted-image")
        self.manifest({"source": "listed.jpg"}, batch="batch-unlisted")
        original_handoff = (self.inbox / "HANDOFF.yml").read_bytes()

        result = self.run_processor()
        self.assertNotEqual(result.returncode, 0)
        self.assertTrue((self.inbox / "listed.jpg").exists())
        self.assertTrue((self.inbox / "extra.png").exists())
        self.assertEqual((self.inbox / "HANDOFF.yml").read_bytes(), original_handoff)
        report = (
            self.inbox
            / "history/batch-unlisted/attempt-001/verification-report.md"
        ).read_text(encoding="utf-8")
        self.assertIn("not listed", report)

    def test_bulk_staging_preserves_each_original_filename(self):
        (self.inbox / "camera.png").write_bytes(b"png-original")
        (self.inbox / "camera.jpg").write_bytes(b"jpeg-original")
        self.manifest_many(
            [
                {
                    "source": "camera.png",
                    "asset_id": "ILL-001",
                    "title": "Morning Window",
                },
                {
                    "source": "camera.jpg",
                    "asset_id": "ILL-002",
                    "title": "Evening Window",
                },
            ],
            batch="batch-bulk",
        )

        result = self.run_processor()
        self.assertEqual(result.returncode, 0, result.stderr)
        destination = (
            self.root
            / "novels/Novel-02/assets/illustrations/ARC-001/SCN-001"
        )
        self.assertTrue((destination / "ILL-001-morning-window.webp").is_file())
        self.assertTrue((destination / "ILL-002-evening-window.webp").is_file())
        history = self.inbox / "history/batch-bulk/attempt-001"
        with (history / "conversion-report.csv").open(encoding="utf-8") as handle:
            rows = list(csv.DictReader(handle))
        self.assertEqual(
            {row["staging_webp_path"] for row in rows},
            {
                "images/takeout/webp/batch-bulk/attempt-001/camera.png.webp",
                "images/takeout/webp/batch-bulk/attempt-001/camera.jpg.webp",
            },
        )
        self.assertFalse((self.inbox / "webp/batch-bulk/attempt-001").exists())

    def test_failed_batch_retains_successful_staging_and_retry_uses_next_attempt(self):
        encoder = self.bin_dir / "cwebp"
        encoder.write_text(
            FAKE_CWEBP.replace(
                'if "-o" not in args:',
                'if any(arg.endswith("broken.jpg") for arg in args):\n'
                '    print("simulated encoder failure", file=sys.stderr)\n'
                '    raise SystemExit(9)\n'
                'if "-o" not in args:',
            ),
            encoding="utf-8",
        )
        encoder.chmod(0o755)
        (self.inbox / "good.png").write_bytes(b"good-image")
        (self.inbox / "broken.jpg").write_bytes(b"broken-image")
        self.manifest_many(
            [
                {"source": "good.png", "asset_id": "ILL-001", "title": "Good Image"},
                {"source": "broken.jpg", "asset_id": "ILL-002", "title": "Broken Image"},
            ],
            batch="batch-retry",
        )
        original_handoff = (self.inbox / "HANDOFF.yml").read_bytes()

        failed = self.run_processor()
        self.assertNotEqual(failed.returncode, 0)
        staged = self.inbox / "webp/batch-retry/attempt-001/good.png.webp"
        self.assertTrue(staged.is_file())
        self.assertTrue((self.inbox / "good.png").is_file())
        self.assertTrue((self.inbox / "broken.jpg").is_file())
        self.assertEqual((self.inbox / "HANDOFF.yml").read_bytes(), original_handoff)
        self.assertFalse((self.root / "novels/Novel-02/assets/illustrations/ARC-001/SCN-001/ILL-001-good-image.webp").exists())

        # Correct the batch, retaining the failed attempt as an inspectable record.
        (self.inbox / "broken.jpg").unlink()
        self.manifest(
            {"source": "good.png", "asset_id": "ILL-001", "title": "Good Image"},
            batch="batch-retry",
        )
        retried = self.run_processor()
        self.assertEqual(retried.returncode, 0, retried.stderr)
        self.assertTrue(staged.is_file(), "failed attempt staging must remain archived")
        self.assertFalse((self.inbox / "webp/batch-retry/attempt-002").exists())
        self.assertTrue((self.inbox / "history/batch-retry/attempt-001/verification-report.md").is_file())
        self.assertTrue((self.inbox / "history/batch-retry/attempt-002/verification-report.md").is_file())
        self.assertEqual(
            (self.inbox / "HANDOFF.yml").read_text(encoding="utf-8"),
            "version: 1\nstatus: empty\nitems: []\n",
        )

    def test_existing_webp_staging_tree_is_reserved_not_scanned_as_intake(self):
        leftover = self.inbox / "webp/older-batch/attempt-001/inspection-note.txt"
        leftover.parent.mkdir(parents=True)
        leftover.write_text("prior staging content", encoding="utf-8")
        (self.inbox / "fresh.png").write_bytes(b"fresh-upload")
        self.manifest({"source": "fresh.png"}, batch="batch-with-old-staging")

        result = self.run_processor()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(leftover.read_text(encoding="utf-8"), "prior staging content")
        self.assertFalse((self.inbox / "webp/batch-with-old-staging/attempt-001").exists())

    def test_destination_collision_fails_without_overwrite(self):
        (self.inbox / "photo.jpg").write_bytes(b"original-upload")
        directory = self.root / "images/references"
        directory.mkdir(parents=True)
        existing = directory / "original" / "shared-discovery.jpg"
        existing.parent.mkdir(parents=True)
        existing.write_bytes(b"keep-this-file")
        self.manifest(
            {
                "source": "photo.jpg",
                "asset_id": "",
                "destination_dir": "images/references",
            },
            batch="batch-collision",
        )

        result = self.run_processor()
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(existing.read_bytes(), b"keep-this-file")
        self.assertTrue((self.inbox / "photo.jpg").exists())
        self.assertEqual(
            (self.inbox / "HANDOFF.yml").read_text(encoding="utf-8").splitlines()[2],
            "status: ready",
        )

    def test_animated_png_fails_and_stays_in_takeout(self):
        signature = b"\x89PNG\r\n\x1a\n"
        apng = (
            signature
            + (8).to_bytes(4, "big")
            + b"acTL"
            + (b"\0" * 8)
            + (0).to_bytes(4, "big")
            + b"IEND"
            + (b"\0" * 4)
        )
        (self.inbox / "animation.png").write_bytes(apng)
        self.manifest({"source": "animation.png"}, batch="batch-apng")

        result = self.run_processor()
        self.assertNotEqual(result.returncode, 0)
        self.assertTrue((self.inbox / "animation.png").exists())
        report = (
            self.inbox
            / "history/batch-apng/attempt-001/verification-report.md"
        ).read_text(encoding="utf-8")
        self.assertIn("animated PNG", report)

    def test_empty_handoff_is_noop_and_leaves_uploads_untouched(self):
        (self.inbox / "not-yet-routed.png").write_bytes(b"waiting")
        (self.inbox / "HANDOFF.yml").write_text(
            "version: 1\nstatus: empty\nitems: []\n", encoding="utf-8"
        )

        result = self.run_processor()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue((self.inbox / "not-yet-routed.png").exists())
        self.assertFalse((self.inbox / "history").exists())


    def test_invalid_unhashable_handoff_status_is_reported_safely(self):
        (self.inbox / "waiting.png").write_bytes(b"waiting-original")
        (self.inbox / "HANDOFF.yml").write_text(
            "version: 1\nstatus: []\nitems: []\n", encoding="utf-8"
        )
        result = self.run_processor()
        self.assertNotEqual(result.returncode, 0)
        self.assertTrue((self.inbox / "waiting.png").is_file())
        report = (
            self.inbox
            / "history/invalid-run-unit-test/attempt-001/verification-report.md"
        ).read_text(encoding="utf-8")
        self.assertIn("status must be 'draft', 'empty', or 'ready'", report)

    def test_not_ready_handoff_is_noop(self):
        (self.inbox / "waiting.png").write_bytes(b"waiting")
        (self.inbox / "HANDOFF.yml").write_text(
            "version: 1\nstatus: draft\nitems: []\n", encoding="utf-8"
        )

        result = self.run_processor()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue((self.inbox / "waiting.png").exists())
        self.assertFalse((self.inbox / "history").exists())



    def test_attempt_06_and_11_uploads_retain_pngs_and_link_only_webps(self):
        session = self.root / "drawings/2026-11-19"
        session.mkdir(parents=True)
        (session / "attempt-06.md").write_text("# Attempt 06\n", encoding="utf-8")
        (session / "attempt-11.md").write_text("# Attempt 11\n", encoding="utf-8")
        readme = session / "README.md"
        readme.write_text(
            "# Drawing session\n\n"
            "| Attempt / prompt | Session / brief | Series / baseline lineage | Execution outcome | User approval / output evidence | Image |\n"
            "|---|---|---|---|---|---|\n"
            "| [06 — Portrait](attempt-06.md) | Session | Baseline | Generated | Not recorded | — |\n"
            "| [11 — Portrait](attempt-11.md) | Session | Baseline | Generated | Not recorded | — |\n"
            "\n## Image inventory — all 0 files\n",
            encoding="utf-8",
        )
        (self.inbox / "upload-six.png").write_bytes(b"attempt-six-original")
        (self.inbox / "upload-eleven.png").write_bytes(b"attempt-eleven-original")
        self.manifest_many(
            [
                {
                    "source": "upload-six.png",
                    "asset_id": "",
                    "title": "Attempt 06 Additional Image",
                    "destination_dir": "drawings/2026-11-19/images",
                    "attempt": "06",
                },
                {
                    "source": "upload-eleven.png",
                    "asset_id": "",
                    "title": "Attempt 11 Additional Image",
                    "destination_dir": "drawings/2026-11-19/images",
                    "attempt": "11",
                },
            ],
            batch="batch-attempt-six-eleven",
        )

        result = self.run_processor()
        self.assertEqual(result.returncode, 0, result.stderr)
        image_dir = session / "images"
        for slug, original in (
            ("attempt-06-additional-image", b"attempt-six-original"),
            ("attempt-11-additional-image", b"attempt-eleven-original"),
        ):
            self.assertEqual((image_dir / "original" / f"{slug}.png").read_bytes(), original)
            self.assertTrue((image_dir / f"{slug}.webp").is_file())

        attempt_six = (session / "attempt-06.md").read_text(encoding="utf-8")
        attempt_eleven = (session / "attempt-11.md").read_text(encoding="utf-8")
        self.assertIn("[attempt-06-additional-image.webp](images/attempt-06-additional-image.webp)", attempt_six)
        self.assertIn("[attempt-11-additional-image.webp](images/attempt-11-additional-image.webp)", attempt_eleven)
        self.assertNotIn(".png", attempt_six)
        self.assertNotIn(".png", attempt_eleven)
        readme_text = readme.read_text(encoding="utf-8")
        self.assertIn("[attempt-06-additional-image.webp](images/attempt-06-additional-image.webp)", readme_text)
        self.assertIn("[attempt-11-additional-image.webp](images/attempt-11-additional-image.webp)", readme_text)
        self.assertIn("## Image inventory — 2 WebP delivery files + 2 original masters (4 files total)", readme_text)
        self.assertNotIn("attempt-06-additional-image.png", readme_text)
        self.assertNotIn("attempt-11-additional-image.png", readme_text)

        with (session / "manifest.csv").open(encoding="utf-8", newline="") as handle:
            rows = list(csv.DictReader(handle))
        self.assertEqual(len(rows), 2)
        self.assertEqual({row["attempt"] for row in rows}, {"06", "11"})
        self.assertEqual({row["verification_status"] for row in rows}, {"Pending"})


    def test_drawing_session_upload_without_attempt_metadata_is_rejected(self):
        session = self.root / "drawings/2026-11-19"
        session.mkdir(parents=True)
        (session / "README.md").write_text(
            "# Drawing session\n\n"
            "| Attempt / prompt | Session / brief | Series / baseline lineage | Execution outcome | User approval / output evidence | Image |\n"
            "|---|---|---|---|---|---|\n",
            encoding="utf-8",
        )
        (self.inbox / "missing-attempt.png").write_bytes(b"missing-attempt")
        self.manifest_many(
            [{
                "source": "missing-attempt.png",
                "title": "Missing Attempt",
                "destination_dir": "drawings/2026-11-19/images",
            }],
            batch="batch-missing-attempt",
        )
        result = self.run_processor()
        self.assertNotEqual(result.returncode, 0)
        self.assertTrue((self.inbox / "missing-attempt.png").is_file())
        report = (
            self.inbox
            / "history/batch-missing-attempt/attempt-001/verification-report.md"
        ).read_text(encoding="utf-8")
        self.assertIn("require explicit attempt metadata", report)




    def test_missing_existing_webp_link_blocks_upload_and_rolls_back(self):
        session = self.root / "drawings/2026-11-19"
        session.mkdir(parents=True)
        (session / "attempt-01.md").write_text(
            "# Attempt 01\n\n## Repository images\n\n"
            "- [missing.webp](images/missing.webp)\n",
            encoding="utf-8",
        )
        readme = session / "README.md"
        readme.write_text(
            "# Drawing session\n\n"
            "| Attempt / prompt | Session / brief | Series / baseline lineage | Execution outcome | User approval / output evidence | Image |\n"
            "|---|---|---|---|---|---|\n"
            "| [01 — Existing](attempt-01.md) | Session | Existing | Generated | Not recorded | [missing.webp](images/missing.webp) |\n\n"
            "## Image inventory — all 1 files\n\n"
            "- [missing.webp](images/missing.webp)\n",
            encoding="utf-8",
        )
        (self.inbox / "new.png").write_bytes(b"new-upload-original")
        self.manifest_many(
            [{
                "source": "new.png",
                "title": "New Output",
                "destination_dir": "drawings/2026-11-19/images",
                "attempt": "1",
            }],
            batch="batch-stale-webp-link",
        )
        handoff_before = (self.inbox / "HANDOFF.yml").read_bytes()
        readme_before = readme.read_bytes()

        result = self.run_processor()
        self.assertNotEqual(result.returncode, 0)
        self.assertTrue((self.inbox / "new.png").is_file())
        self.assertFalse((session / "images/original/new-output.png").exists())
        self.assertEqual((self.inbox / "HANDOFF.yml").read_bytes(), handoff_before)
        self.assertEqual(readme.read_bytes(), readme_before)
        report = (
            self.inbox
            / "history/batch-stale-webp-link/attempt-001/verification-report.md"
        ).read_text(encoding="utf-8")
        self.assertIn("missing or unsafe WebP asset", report)

    def test_png_links_in_drawing_records_are_rejected(self):
        session = self.root / "drawings/2026-11-19"
        session.mkdir(parents=True)
        (session / "attempt-01.md").write_text(
            "# Attempt 01\n\n## Repository images\n\n"
            "- [original.png](images/original.png)\n",
            encoding="utf-8",
        )
        readme = session / "README.md"
        readme.write_text(
            "# Drawing session\n\n"
            "| Attempt / prompt | Session / brief | Series / baseline lineage | Execution outcome | User approval / output evidence | Image |\n"
            "|---|---|---|---|---|---|\n"
            "| [01 — Existing](attempt-01.md) | Session | Existing | Generated | Not recorded | [original.png](images/original.png) |\n",
            encoding="utf-8",
        )
        (session / "images").mkdir()
        (session / "images/original.png").write_bytes(b"png-link-should-not-be-used")
        (self.inbox / "new.png").write_bytes(b"new-upload-original")
        self.manifest_many(
            [{
                "source": "new.png",
                "title": "New Output",
                "destination_dir": "drawings/2026-11-19/images",
                "attempt": "1",
            }],
            batch="batch-png-link",
        )
        result = self.run_processor()
        self.assertNotEqual(result.returncode, 0)
        self.assertTrue((self.inbox / "new.png").is_file())
        report = (
            self.inbox
            / "history/batch-png-link/attempt-001/verification-report.md"
        ).read_text(encoding="utf-8")
        self.assertIn("link only top-level WebP", report)

    def test_existing_manifest_duplicate_output_id_blocks_new_upload(self):
        session = self.root / "drawings/2026-11-19"
        session.mkdir(parents=True)
        (session / "attempt-01.md").write_text("# Attempt 01\n", encoding="utf-8")
        (session / "README.md").write_text(
            "# Drawing session\n\n"
            "| Attempt / prompt | Session / brief | Series / baseline lineage | Execution outcome | User approval / output evidence | Image |\n"
            "|---|---|---|---|---|---|\n"
            "| [01 — New](attempt-01.md) | Session | Existing | Generated | Not recorded | — |\n",
            encoding="utf-8",
        )
        (session / "manifest.csv").write_text(
            "session_date,image_id,filename,prompt_id,approval_status,github_url,sha256,verification_status,attempt,output_id,webp_path\n"
            "2026-11-19,prior-image,prior.png,,Not recorded,https://example.invalid/prior,old-sha,Not verifiable,01,A001-O01,drawings/2026-11-19/images/prior.webp\n",
            encoding="utf-8",
        )
        (self.inbox / "new.png").write_bytes(b"new-generated-original")
        self.manifest_many(
            [{
                "source": "new.png",
                "title": "New Output",
                "destination_dir": "drawings/2026-11-19/images",
                "attempt": "1",
                "output_id": "A001-O01",
            }],
            batch="batch-existing-output-id",
        )
        result = self.run_processor()
        self.assertNotEqual(result.returncode, 0)
        self.assertTrue((self.inbox / "new.png").is_file())
        self.assertFalse((session / "images/original/new-output.png").exists())
        report = (
            self.inbox
            / "history/batch-existing-output-id/attempt-001/verification-report.md"
        ).read_text(encoding="utf-8")
        self.assertIn("Duplicate output_id", report)

    def test_identical_original_bytes_from_two_outputs_get_distinct_internal_image_ids(self):
        session = self.root / "drawings/2026-11-19"
        session.mkdir(parents=True)
        (session / "attempt-01.md").write_text("# Attempt 01\n", encoding="utf-8")
        readme = session / "README.md"
        readme.write_text(
            "# Drawing session\n\n"
            "| Attempt / prompt | Session / brief | Series / baseline lineage | Execution outcome | User approval / output evidence | Image |\n"
            "|---|---|---|---|---|---|\n"
            "| [01 — Two outputs](attempt-01.md) | Session | Existing | Two outputs | Not recorded | — |\n",
            encoding="utf-8",
        )
        identical = b"same-original-image-bytes"
        (self.inbox / "output-one.png").write_bytes(identical)
        (self.inbox / "output-two.png").write_bytes(identical)
        self.manifest_many(
            [
                {
                    "source": "output-one.png",
                    "title": "Output One",
                    "destination_dir": "drawings/2026-11-19/images",
                    "attempt": "1",
                },
                {
                    "source": "output-two.png",
                    "title": "Output Two",
                    "destination_dir": "drawings/2026-11-19/images",
                    "attempt": "1",
                },
            ],
            batch="batch-identical-outputs",
        )
        result = self.run_processor()
        self.assertEqual(result.returncode, 0, result.stderr)
        with (session / "manifest.csv").open(encoding="utf-8", newline="") as handle:
            rows = list(csv.DictReader(handle))
        self.assertEqual(len(rows), 2)
        self.assertEqual(len({row["image_id"] for row in rows}), 2)
        self.assertEqual(len({row["sha256"] for row in rows}), 1)
        self.assertEqual({row["attempt"] for row in rows}, {"01"})
        self.assertTrue(all(row["image_id"].startswith("A01-O-") for row in rows))

    def test_duplicate_output_id_fails_before_relocation(self):
        (self.inbox / "first.png").write_bytes(b"first-original")
        (self.inbox / "second.png").write_bytes(b"second-original")
        self.manifest_many(
            [
                {"source": "first.png", "output_id": "A001-O01", "title": "First"},
                {"source": "second.png", "output_id": "A001-O01", "title": "Second"},
            ],
            batch="batch-duplicate-output-id",
        )
        handoff_before = (self.inbox / "HANDOFF.yml").read_bytes()
        result = self.run_processor()
        self.assertNotEqual(result.returncode, 0)
        self.assertTrue((self.inbox / "first.png").is_file())
        self.assertTrue((self.inbox / "second.png").is_file())
        self.assertEqual((self.inbox / "HANDOFF.yml").read_bytes(), handoff_before)
        report = (
            self.inbox
            / "history/batch-duplicate-output-id/attempt-001/verification-report.md"
        ).read_text(encoding="utf-8")
        self.assertIn("Duplicate output_id", report)

    def test_invalid_handoff_metadata_fields_fail_before_relocation(self):
        invalid_fields = [
            ("asset_id", "ill_001", "Invalid asset_id"),
            ("expected_sha256", "not-a-sha256", "expected_sha256"),
            ("output_id", "bad id", "output_id"),
            ("prompt_id", "bad id", "prompt_id"),
            ("native_generation_id", "x" * 257, "native_generation_id"),
            ("native_output_id", "x" * 257, "native_output_id"),
            ("approval_status", "Unknown", "approval_status"),
            ("mapping_evidence", "x" * 1001, "mapping_evidence"),
        ]
        for index, (field, value, expected_error) in enumerate(invalid_fields, start=1):
            with self.subTest(field=field):
                filename = f"invalid-{index}.png"
                batch = f"invalid-field-{index}"
                source = self.inbox / filename
                source.write_bytes(f"source-{index}".encode("utf-8"))
                item = {"source": filename, field: value}
                self.manifest(item, batch=batch)
                handoff_before = (self.inbox / "HANDOFF.yml").read_bytes()

                result = self.run_processor()

                self.assertNotEqual(result.returncode, 0, result.stdout)
                self.assertTrue(source.is_file(), field)
                self.assertEqual((self.inbox / "HANDOFF.yml").read_bytes(), handoff_before)
                report = (
                    self.inbox
                    / "history"
                    / batch
                    / "attempt-001"
                    / "verification-report.md"
                ).read_text(encoding="utf-8")
                self.assertIn(expected_error, report)
                source.unlink()

    def test_non_mapping_handoff_is_rejected_not_silently_ignored(self):
        (self.inbox / "waiting.png").write_bytes(b"waiting-original")
        (self.inbox / "HANDOFF.yml").write_text("- malformed\\n- top-level\\n", encoding="utf-8")
        result = self.run_processor()
        self.assertNotEqual(result.returncode, 0)
        self.assertTrue((self.inbox / "waiting.png").is_file())
        report = (
            self.inbox
            / "history/invalid-run-unit-test/attempt-001/verification-report.md"
        ).read_text(encoding="utf-8")
        self.assertIn("top level", report)

    def test_session_manifest_backfills_legacy_webps_conservatively(self):
        session = self.root / "drawings/2026-11-19"
        image_dir = session / "images"
        image_dir.mkdir(parents=True)
        attempt_record = session / "attempt-01.md"
        attempt_record.write_text("# Attempt 01\n", encoding="utf-8")
        readme = session / "README.md"
        readme.write_text(
            "# Drawing session\n\n"
            "| Attempt / prompt | Session / brief | Series / baseline lineage | Execution outcome | User approval / output evidence | Image |\n"
            "|---|---|---|---|---|---|\n"
            "| [01 — Legacy](attempt-01.md) | Session | Existing | Generated | Not recorded | [legacy.webp](images/legacy.webp) |\n\n"
            "## Image inventory — all 1 files\n",
            encoding="utf-8",
        )
        payload = b"legacy-webp-payload"
        legacy_webp = b"RIFF" + (len(payload) + 4).to_bytes(4, "little") + b"WEBP" + payload
        (image_dir / "legacy.webp").write_bytes(legacy_webp)

        (self.inbox / "new.png").write_bytes(b"new-generated-original")
        self.manifest_many(
            [{
                "source": "new.png",
                "asset_id": "",
                "title": "New Output",
                "destination_dir": "drawings/2026-11-19/images",
                "attempt": "1",
            }],
            batch="batch-legacy-manifest",
        )
        result = self.run_processor()
        self.assertEqual(result.returncode, 0, result.stderr)

        with (session / "manifest.csv").open(encoding="utf-8", newline="") as handle:
            rows = list(csv.DictReader(handle))
        self.assertEqual(len(rows), 2)
        inventory = readme.read_text(encoding="utf-8")
        self.assertIn("## Image inventory — 2 WebP delivery files + 1 original master (3 files total)", inventory)
        self.assertIn("[new-output.webp](images/new-output.webp)", inventory)
        self.assertIn("[legacy.webp](images/legacy.webp)", inventory)
        legacy = next(row for row in rows if row["webp_path"].endswith("/legacy.webp"))
        new = next(row for row in rows if row["webp_path"].endswith("/new-output.webp"))
        self.assertEqual(legacy["mapping_status"], "Corroborated")
        self.assertEqual(legacy["attempt"], "01")
        self.assertIn("[legacy.webp](images/legacy.webp)", attempt_record.read_text(encoding="utf-8"))
        self.assertEqual(legacy["sha256"], "")
        self.assertEqual(legacy["verification_status"], "Not verifiable")
        self.assertEqual(legacy["original_bytes_available"], "No")
        self.assertTrue(legacy["webp_sha256"])
        self.assertEqual(new["verification_status"], "Pending")
        self.assertIn("Awaiting GitHub post-push", new["verification_error"])
        self.assertEqual(new["mapping_status"], "Corroborated")
        self.assertTrue(new["sha256"])
        self.assertTrue((image_dir / "original/new-output.png").is_file())


    def test_session_manifest_uses_a_matching_legacy_original_master_when_present(self):
        session = self.root / "drawings/2026-11-19"
        image_dir = session / "images"
        original_dir = image_dir / "original"
        original_dir.mkdir(parents=True)
        attempt_record = session / "attempt-01.md"
        attempt_record.write_text("# Attempt 01\n", encoding="utf-8")
        readme = session / "README.md"
        readme.write_text(
            "# Drawing session\n\n"
            "| Attempt / prompt | Session / brief | Series / baseline lineage | Execution outcome | User approval / output evidence | Image |\n"
            "|---|---|---|---|---|---|\n"
            "| [01 — Legacy](attempt-01.md) | Session | Existing | Generated | Not recorded | [legacy.webp](images/legacy.webp) |\n\n"
            "## Image inventory — all 1 files\n",
            encoding="utf-8",
        )
        legacy_original = b"legacy-original-master-bytes"
        (original_dir / "legacy.png").write_bytes(legacy_original)
        payload = b"legacy-webp-payload"
        (image_dir / "legacy.webp").write_bytes(
            b"RIFF" + (len(payload) + 4).to_bytes(4, "little") + b"WEBP" + payload
        )

        (self.inbox / "new.png").write_bytes(b"new-generated-original")
        self.manifest_many(
            [{
                "source": "new.png",
                "title": "New Output",
                "destination_dir": "drawings/2026-11-19/images",
                "attempt": "1",
            }],
            batch="batch-legacy-original-manifest",
        )
        result = self.run_processor()
        self.assertEqual(result.returncode, 0, result.stderr)

        with (session / "manifest.csv").open(encoding="utf-8", newline="") as handle:
            rows = list(csv.DictReader(handle))
        legacy = next(row for row in rows if row["webp_path"].endswith("/legacy.webp"))
        expected_master = "drawings/2026-11-19/images/original/legacy.png"
        self.assertEqual(legacy["original_path"], expected_master)
        self.assertEqual(legacy["filename"], expected_master)
        self.assertEqual(legacy["sha256"], hashlib.sha256(legacy_original).hexdigest())
        self.assertEqual(legacy["original_sha256"], hashlib.sha256(legacy_original).hexdigest())
        self.assertEqual(legacy["original_bytes_available"], "Yes")
        self.assertEqual(legacy["verification_status"], "Pending")
        self.assertEqual(legacy["mapping_status"], "Corroborated")

    def test_orphan_legacy_original_master_blocks_processing_and_rolls_back_new_upload(self):
        session = self.root / "drawings/2026-11-19"
        image_dir = session / "images"
        original_dir = image_dir / "original"
        original_dir.mkdir(parents=True)
        (original_dir / "orphan.png").write_bytes(b"orphan-original")
        (session / "attempt-01.md").write_text("# Attempt 01\n", encoding="utf-8")
        readme = session / "README.md"
        readme.write_text(
            "# Drawing session\n\n"
            "| Attempt / prompt | Session / brief | Series / baseline lineage | Execution outcome | User approval / output evidence | Image |\n"
            "|---|---|---|---|---|---|\n"
            "| [01 — New](attempt-01.md) | Session | Existing | Generated | Not recorded | — |\n",
            encoding="utf-8",
        )
        (self.inbox / "new.png").write_bytes(b"new-generated-original")
        self.manifest_many(
            [{
                "source": "new.png",
                "title": "New Output",
                "destination_dir": "drawings/2026-11-19/images",
                "attempt": "1",
            }],
            batch="batch-orphan-master",
        )
        handoff_before = (self.inbox / "HANDOFF.yml").read_bytes()
        readme_before = readme.read_bytes()

        result = self.run_processor()
        self.assertNotEqual(result.returncode, 0)
        self.assertTrue((self.inbox / "new.png").is_file())
        self.assertTrue((original_dir / "orphan.png").is_file())
        self.assertFalse((image_dir / "new-output.webp").exists())
        self.assertEqual((self.inbox / "HANDOFF.yml").read_bytes(), handoff_before)
        self.assertEqual(readme.read_bytes(), readme_before)
        report = (
            self.inbox
            / "history/batch-orphan-master/attempt-001/verification-report.md"
        ).read_text(encoding="utf-8")
        self.assertIn("Original master has no same-stem WebP", report)

    def test_session_manifest_preserves_existing_rows_and_adds_new_columns(self):
        session = self.root / "drawings/2026-11-19"
        session.mkdir(parents=True)
        (session / "attempt-01.md").write_text("# Attempt 01\n", encoding="utf-8")
        (session / "README.md").write_text(
            "# Drawing session\n\n"
            "| Attempt / prompt | Session / brief | Series / baseline lineage | Execution outcome | User approval / output evidence | Image |\n"
            "|---|---|---|---|---|---|\n"
            "| [01 — Existing](attempt-01.md) | Session | Existing | Generated | Not recorded | — |\n",
            encoding="utf-8",
        )
        (session / "manifest.csv").write_text(
            "session_date,image_id,filename,prompt_id,approval_status,github_url,sha256,verification_status,custom_note\n"
            "2026-11-19,prior-id,prior.webp,,Not recorded,https://example.invalid/prior,,Not verifiable,preserve-me\n",
            encoding="utf-8",
        )
        (self.inbox / "fresh.png").write_bytes(b"fresh-original")
        self.manifest_many(
            [{
                "source": "fresh.png",
                "asset_id": "",
                "title": "Fresh Output",
                "destination_dir": "drawings/2026-11-19/images",
                "attempt": "1",
            }],
            batch="batch-manifest-migration",
        )
        result = self.run_processor()
        self.assertEqual(result.returncode, 0, result.stderr)

        with (session / "manifest.csv").open(encoding="utf-8", newline="") as handle:
            reader = csv.DictReader(handle)
            rows = list(reader)
            self.assertIn("custom_note", reader.fieldnames)
            self.assertIn("native_generation_id", reader.fieldnames)
        prior = next(row for row in rows if row["image_id"] == "prior-id")
        self.assertEqual(prior["custom_note"], "preserve-me")
        self.assertEqual(len(rows), 2)

    def test_generation_hash_matches_uploaded_original_and_is_reported(self):
        original = b"generation-original-byte-sequence"
        import hashlib
        expected = hashlib.sha256(original).hexdigest()
        (self.inbox / "unchanged.png").write_bytes(original)
        self.manifest({"source": "unchanged.png", "expected_sha256": expected, "output_id": "A001-O01", "prompt_id": "P001"}, batch="batch-hash-match")
        result = self.run_processor()
        self.assertEqual(result.returncode, 0, result.stderr)
        with (self.inbox / "history/batch-hash-match/attempt-001/conversion-report.csv").open(encoding="utf-8") as handle:
            row = next(csv.DictReader(handle))
        self.assertEqual(row["generation_sha256"], expected)
        self.assertEqual(row["source_sha256"], expected)
        self.assertEqual(row["hash_match"], "MATCH")
        self.assertEqual(row["output_id"], "A001-O01")
        self.assertEqual(row["prompt_id"], "P001")

    def test_generation_hash_mismatch_is_a_review_flag_not_a_batch_rejection(self):
        original = b"different-original-bytes"
        (self.inbox / "mismatch.png").write_bytes(original)
        wrong = "0" * 64
        session = self.root / "drawings/2026-11-19"
        session.mkdir(parents=True)
        (session / "attempt-01.md").write_text("# Attempt 01\n", encoding="utf-8")
        (session / "README.md").write_text(
            "# Drawing session\n\n"
            "| Attempt / prompt | Session / brief | Series / baseline lineage | Execution outcome | User approval / output evidence | Image |\n"
            "|---|---|---|---|---|---|\n"
            "| [01 — Mismatch](attempt-01.md) | Session | Existing | Generated | Not recorded | — |\n",
            encoding="utf-8",
        )
        self.manifest(
            {
                "source": "mismatch.png",
                "asset_id": "",
                "title": "Mismatch Review",
                "destination_dir": "drawings/2026-11-19/images",
                "attempt": "1",
                "expected_sha256": wrong,
            },
            batch="batch-hash-mismatch",
        )
        result = self.run_processor()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertFalse((self.inbox / "mismatch.png").exists())
        master = session / "images/original/mismatch-review.png"
        self.assertEqual(master.read_bytes(), original)
        report = (self.inbox / "history/batch-hash-mismatch/attempt-001/verification-report.md").read_text(encoding="utf-8")
        self.assertIn("retained and flagged for mapping review, not automatically rejected", report)
        with (session / "manifest.csv").open(encoding="utf-8", newline="") as handle:
            row = next(csv.DictReader(handle))
        self.assertEqual(row["hash_match"], "MISMATCH")
        self.assertEqual(row["mapping_status"], "Probable")
        self.assertEqual(row["verification_status"], "Pending")
        with (self.inbox / "history/batch-hash-mismatch/attempt-001/conversion-report.csv").open(encoding="utf-8") as handle:
            report_row = next(csv.DictReader(handle))
        self.assertEqual(report_row["hash_match"], "MISMATCH")
        self.assertEqual(report_row["mapping_status"], "Probable")


class PublishedManifestVerificationTests(unittest.TestCase):
    def setUp(self):
        self.repository = "dungnv2602/chatgpt"
        self.branch = "gpt"
        self.webp_payload = b"verified-webp-payload"
        self.webp_bytes = (
            b"RIFF" + (len(self.webp_payload) + 4).to_bytes(4, "little")
            + b"WEBP" + self.webp_payload
        )
        self.original_bytes = b"unchanged-original-master"
        self.webp_path = "drawings/2026-11-19/images/result.webp"
        self.original_path = "drawings/2026-11-19/images/original/result.png"
        self.row = {
            "image_id": "A01-O01",
            "attempt": "01",
            "github_url": github_blob_url(self.webp_path, self.repository, self.branch),
            "webp_path": self.webp_path,
            "webp_sha256": hashlib.sha256(self.webp_bytes).hexdigest(),
            "original_path": self.original_path,
            "sha256": hashlib.sha256(self.original_bytes).hexdigest(),
            "original_sha256": hashlib.sha256(self.original_bytes).hexdigest(),
            "generation_sha256": "",
        }
        self.blobs = {
            self.webp_path: self.webp_bytes,
            self.original_path: self.original_bytes,
            "drawings/2026-11-19/README.md": (
                "# Drawing session\n\n"
                "| Attempt / prompt | Session / brief | Series / baseline lineage | Execution outcome | User approval / output evidence | Image |\n"
                "|---|---|---|---|---|---|\n"
                "| [01 - Output](attempt-01.md) | Session | Existing | Generated | Not recorded | [result.webp](images/result.webp) |\n"
                "\n## Image inventory — 1 WebP delivery files + 1 original master (2 files total)\n\n"
                "- [result.webp](images/result.webp)\n"
            ).encode("utf-8"),
            "drawings/2026-11-19/attempt-01.md": (
                "# Attempt 01\n\n## Repository images\n\n"
                "- [result.webp](images/result.webp)\n"
            ).encode("utf-8"),
        }


    def test_generation_hash_mismatch_does_not_fail_published_storage_verification(self):
        row = dict(self.row)
        row["generation_sha256"] = "0" * 64
        status, error = verify_manifest_row(
            row, lambda path: self.blobs.get(path),
            github_blob_url(self.webp_path, self.repository, self.branch),
        )
        self.assertEqual(status, "Verified")
        self.assertEqual(error, "")

    def test_published_daily_readme_and_attempt_links_are_verified(self):
        error = verify_session_links(self.row, lambda path: self.blobs.get(path))
        self.assertEqual(error, "")

    def test_missing_published_attempt_link_fails_verification(self):
        self.blobs["drawings/2026-11-19/attempt-01.md"] = (
            b"# Attempt 01\n\n## Repository images\n\n- [other.webp](images/other.webp)\n"
        )
        error = verify_session_links(self.row, lambda path: self.blobs.get(path))
        self.assertIn("attempt record does not link", error)

    def test_missing_published_inventory_link_fails_verification(self):
        self.blobs["drawings/2026-11-19/README.md"] = (
            "# Drawing session\n\n"
            "| Attempt / prompt | Session / brief | Series / baseline lineage | Execution outcome | User approval / output evidence | Image |\n"
            "|---|---|---|---|---|---|\n"
            "| [01 - Output](attempt-01.md) | Session | Existing | Generated | Not recorded | [result.webp](images/result.webp) |\n"
            "\n## Image inventory — 0 WebP delivery files + 1 original master (1 file total)\n"
        ).encode("utf-8")
        error = verify_session_links(self.row, lambda path: self.blobs.get(path))
        self.assertIn("inventory does not link", error)

    def test_missing_published_inventory_section_fails_verification(self):
        self.blobs["drawings/2026-11-19/README.md"] = (
            "# Drawing session\n"
        ).encode("utf-8")
        error = verify_session_links(self.row, lambda path: self.blobs.get(path))
        self.assertIn("has no image inventory section", error)

    def test_published_original_and_webp_are_verified(self):
        status, error = verify_manifest_row(
            self.row, lambda path: self.blobs.get(path),
            github_blob_url(self.webp_path, self.repository, self.branch),
        )
        self.assertEqual(status, "Verified")
        self.assertEqual(error, "")

    def test_legacy_webp_is_checked_but_original_mapping_remains_not_verifiable(self):
        row = dict(self.row)
        row["original_path"] = ""
        row["sha256"] = ""
        status, error = verify_manifest_row(
            row, lambda path: self.blobs.get(path),
            github_blob_url(self.webp_path, self.repository, self.branch),
        )
        self.assertEqual(status, "Not verifiable")
        self.assertIn("original master", error)

    def test_published_original_hash_mismatch_fails(self):
        self.blobs[self.original_path] = b"changed-original-master"
        status, error = verify_manifest_row(
            self.row, lambda path: self.blobs.get(path),
            github_blob_url(self.webp_path, self.repository, self.branch),
        )
        self.assertEqual(status, "Failed")
        self.assertIn("original master SHA-256", error)

    def test_published_webp_hash_mismatch_fails(self):
        self.blobs[self.webp_path] = b"changed"
        status, error = verify_manifest_row(
            self.row, lambda path: self.blobs.get(path),
            github_blob_url(self.webp_path, self.repository, self.branch),
        )
        self.assertEqual(status, "Failed")
        self.assertIn("valid RIFF/WEBP", error)

    def test_github_url_must_match_exact_published_path(self):
        row = dict(self.row)
        row["github_url"] = "https://github.com/dungnv2602/chatgpt/blob/gpt/wrong.webp"
        status, error = verify_manifest_row(
            row, lambda path: self.blobs.get(path),
            github_blob_url(self.webp_path, self.repository, self.branch),
        )
        self.assertEqual(status, "Failed")
        self.assertIn("expected published WebP path", error)


if __name__ == "__main__":
    unittest.main(verbosity=2)
