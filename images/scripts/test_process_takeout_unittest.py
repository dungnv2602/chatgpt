#!/usr/bin/env python3
"""Regression tests for the exact takeout processor used by the GitHub Action."""
import csv
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

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
            asset_id = item.get("asset_id") or ("ILL-%03d" % (index + 1))
            rows.extend([
                f'  - source: "{item["source"]}"',
                f'    asset_id: "{asset_id}"',
                f'    title: "{item.get("title", "Shared Discovery")}"',
                (
                    "    destination_dir: "
                    f'"{item.get("destination_dir", "novel/Novel-02/assets/illustrations/ARC-001/SCN-001")}"'
                ),
            ])
        (self.inbox / "HANDOFF.yml").write_text("\n".join(rows) + "\n", encoding="utf-8")

    def test_success_moves_byte_identical_master_creates_webp_and_archives_reports(self):
        original = b"uploaded-original-bytes"
        (self.inbox / "IMG_001.PNG").write_bytes(original)
        self.manifest({"source": "IMG_001.PNG"})

        result = self.run_processor()
        self.assertEqual(result.returncode, 0, result.stderr)

        destination = (
            self.root
            / "novel/Novel-02/assets/illustrations/ARC-001/SCN-001"
        )
        master = destination / "ILL-001-shared-discovery.PNG"
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
            / "novel/Novel-02/assets/illustrations/ARC-001/SCN-001"
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
        self.assertFalse((self.root / "novel/Novel-02/assets/illustrations/ARC-001/SCN-001/ILL-001-good-image.webp").exists())

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
        existing = directory / "shared-discovery.jpg"
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

    def test_not_ready_handoff_is_noop(self):
        (self.inbox / "waiting.png").write_bytes(b"waiting")
        (self.inbox / "HANDOFF.yml").write_text(
            "version: 1\nstatus: draft\nitems: []\n", encoding="utf-8"
        )

        result = self.run_processor()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue((self.inbox / "waiting.png").exists())
        self.assertFalse((self.inbox / "history").exists())


if __name__ == "__main__":
    unittest.main(verbosity=2)
