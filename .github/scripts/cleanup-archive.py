#!/usr/bin/env python3
"""Delete only indexed task records that have completed 90 days of retention."""

from __future__ import annotations

import json
import os
import subprocess
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path, PurePosixPath
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
INDEX_FILE = ROOT / ".github" / "archive-retention-index.json"
INDEX_RELATIVE = ".github/archive-retention-index.json"
RETENTION_PERIOD = timedelta(days=90)


def utc_now() -> datetime:
    return datetime.now(timezone.utc).replace(microsecond=0)


def parse_utc_timestamp(value: Any) -> datetime:
    if not isinstance(value, str):
        raise ValueError("archived_at must be a UTC timestamp string.")
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if parsed.tzinfo is None or parsed.utcoffset() != timedelta(0):
        raise ValueError("archived_at must include a UTC offset.")
    return parsed.astimezone(timezone.utc)


def validate_record(record: Any) -> tuple[str, datetime]:
    if not isinstance(record, dict) or set(record) != {"path", "archived_at"}:
        raise ValueError("Each index record must contain only path and archived_at.")
    path = record["path"]
    if not isinstance(path, str) or "\\" in path:
        raise ValueError("Archive path must be a safe POSIX repository path.")
    pure_path = PurePosixPath(path)
    parts = pure_path.parts
    if str(pure_path) != path:
        raise ValueError(f"Archive path is not canonical: {path!r}")
    if (
        len(parts) != 3
        or parts[:2] != ("archive", "tasks")
        or parts[2] in {"", ".", "..", ".gitkeep"}
        or not parts[2].endswith(".md")
    ):
        raise ValueError(f"Invalid indexed archive path: {path!r}")
    return path, parse_utc_timestamp(record["archived_at"])


def load_index(index_path: Path) -> dict[str, Any]:
    data = json.loads(index_path.read_text(encoding="utf-8"))
    if not isinstance(data, dict) or data.get("schema_version") != 1:
        raise ValueError("Retention index must use schema_version 1.")
    if data.get("unindexed_records") != "preserve":
        raise ValueError("Unindexed legacy records must remain protected.")
    records = data.get("records")
    if not isinstance(records, list):
        raise ValueError("Retention index records must be a list.")

    seen: set[str] = set()
    for record in records:
        path, _ = validate_record(record)
        if path in seen:
            raise ValueError(f"Duplicate indexed archive path: {path}")
        seen.add(path)
    return data


def write_index(index_path: Path, data: dict[str, Any]) -> None:
    temporary = index_path.with_name(index_path.name + ".tmp")
    temporary.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    temporary.replace(index_path)


def clean_due_records(
    index_path: Path,
    repository_root: Path,
    now: datetime,
) -> tuple[list[str], bool]:
    """Delete due indexed paths only. Never enumerate the archive directory."""
    if now.tzinfo is None:
        raise ValueError("now must be timezone-aware.")
    now = now.astimezone(timezone.utc)
    data = load_index(index_path)

    due: list[str] = []
    retained: list[dict[str, str]] = []
    for record in data["records"]:
        path, archived_at = validate_record(record)
        if now >= archived_at + RETENTION_PERIOD:
            due.append(path)
        else:
            retained.append(record)

    if not due:
        return [], False

    archive_root = repository_root / "archive"
    archive_dir = archive_root / "tasks"
    if archive_root.is_symlink() or archive_dir.is_symlink():
        raise ValueError("Refusing to follow a symlink in the archive path.")

    targets: list[tuple[str, Path]] = []
    for path in due:
        target = repository_root / PurePosixPath(path)
        if target.is_symlink():
            raise ValueError(f"Refusing to delete a symlink: {path}")
        if target.exists() and not target.is_file():
            raise ValueError(f"Indexed archive path is not a regular file: {path}")
        targets.append((path, target))

    deleted: list[str] = []
    for path, target in targets:
        if target.exists():
            target.unlink()
            deleted.append(path)

    data["records"] = retained
    write_index(index_path, data)
    return deleted, True


def require_scheduled_event(event_name: str | None) -> None:
    if event_name != "schedule":
        raise RuntimeError(
            "Archive retention can run only from the scheduled GitHub Actions event."
        )


def main() -> int:
    try:
        require_scheduled_event(os.environ.get("GITHUB_EVENT_NAME"))
        deleted, index_changed = clean_due_records(INDEX_FILE, ROOT, utc_now())

        if index_changed:
            stage_paths = [INDEX_RELATIVE, *deleted]
            subprocess.run(
                ["git", "add", "--", *stage_paths],
                cwd=ROOT,
                check=True,
            )

        output_path = os.environ.get("GITHUB_OUTPUT")
        if not output_path:
            raise RuntimeError("GITHUB_OUTPUT is not available in the scheduled workflow.")
        with open(output_path, "a", encoding="utf-8") as output:
            output.write("deleted_paths<<EOF\n")
            output.write("\n".join(deleted))
            output.write("\nEOF\n")

        if index_changed:
            print(f"Retention index updated. Deleted {len(deleted)} indexed file(s).")
        else:
            print("No indexed records have reached 90 days. The archive was not accessed.")
        return 0
    except Exception as error:
        print(f"::error::{error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
