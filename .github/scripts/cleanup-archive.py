#!/usr/bin/env python3
"""Delete the complete task archive in a 14-day batch cycle."""

from __future__ import annotations

import argparse
import json
import shutil
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ARCHIVE_DIR = ROOT / "archive" / "tasks"
STATE_FILE = ROOT / ".github" / "archive-retention-state.json"
RETENTION_INTERVAL = timedelta(days=14)


def utc_now() -> datetime:
    return datetime.now(timezone.utc).replace(microsecond=0)


def load_last_cleanup() -> datetime:
    state = json.loads(STATE_FILE.read_text(encoding="utf-8"))
    value = state.get("last_cleanup_at")
    if not isinstance(value, str):
        raise ValueError("State file must contain a string last_cleanup_at value.")
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if parsed.tzinfo is None:
        raise ValueError("last_cleanup_at must include a UTC offset.")
    return parsed.astimezone(timezone.utc)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--force",
        action="store_true",
        help="Purge the archive immediately, regardless of the 14-day interval.",
    )
    args = parser.parse_args()

    now = utc_now()
    last_cleanup = load_last_cleanup()
    elapsed = now - last_cleanup

    if not args.force and elapsed < RETENTION_INTERVAL:
        due_at = last_cleanup + RETENTION_INTERVAL
        print(f"Cleanup not due. Next eligible time: {due_at.isoformat()}.")
        return 0

    if not ARCHIVE_DIR.is_dir():
        raise FileNotFoundError(f"Archive directory does not exist: {ARCHIVE_DIR}")

    deleted = 0
    for item in ARCHIVE_DIR.iterdir():
        if item.name == ".gitkeep":
            continue
        if item.is_symlink() or item.is_file():
            item.unlink()
        elif item.is_dir():
            shutil.rmtree(item)
        else:
            item.unlink()
        deleted += 1

    STATE_FILE.write_text(
        json.dumps({"last_cleanup_at": now.isoformat().replace("+00:00", "Z")}, indent=2)
        + "\n",
        encoding="utf-8",
    )
    print(f"Batch cleanup completed. Removed {deleted} archive item(s).")
    print(f"Next cleanup becomes eligible at {(now + RETENTION_INTERVAL).isoformat()}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
