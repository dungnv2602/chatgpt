#!/usr/bin/env python3
"""Delete only exact indexed archive files after 90 days of individual retention."""
from __future__ import annotations
import json, os, subprocess, sys
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
        raise ValueError("archived_at_utc must be a UTC timestamp string.")
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if parsed.tzinfo is None or parsed.utcoffset() != timedelta(0):
        raise ValueError("archived_at_utc must include a UTC offset.")
    return parsed.astimezone(timezone.utc)

def validate_record(record: Any) -> tuple[str, datetime]:
    if not isinstance(record, dict) or set(record) != {"path", "archived_at_utc"}:
        raise ValueError("Each index record must contain only path and archived_at_utc.")
    path = record["path"]
    if not isinstance(path, str) or "\\" in path:
        raise ValueError("Archive path must be a safe POSIX repository path.")
    pure = PurePosixPath(path)
    parts = pure.parts
    if str(pure) != path or len(parts) < 3 or parts[0] != ".archive" or parts[1] not in {"task", "reports"}:
        raise ValueError(f"Invalid indexed archive path: {path!r}")
    if any(part in {"", ".", ".."} for part in parts[2:]) or parts[-1] == ".gitkeep" or path.endswith("/") or not pure.suffix:
        raise ValueError(f"Indexed path must identify an individual file: {path!r}")
    return path, parse_utc_timestamp(record["archived_at_utc"])

def load_index(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict) or data.get("schema_version") != 1 or data.get("unindexed_records") != "preserve":
        raise ValueError("Retention index must use schema_version 1 and preserve unindexed records.")
    records = data.get("records")
    if not isinstance(records, list):
        raise ValueError("Retention index records must be a list.")
    seen = set()
    for record in records:
        item, _ = validate_record(record)
        if item in seen:
            raise ValueError(f"Duplicate indexed archive path: {item}")
        seen.add(item)
    return data

def clean_due_records(index_path: Path, repository_root: Path, now: datetime) -> tuple[list[str], bool]:
    """Delete due exact paths. Treat each indexed task folder as one archive unit."""
    if now.tzinfo is None:
        raise ValueError("now must be timezone-aware.")
    now = now.astimezone(timezone.utc)
    data = load_index(index_path)
    due, retained = [], []
    task_folders: dict[str, list[tuple[dict[str, Any], datetime]]] = {}
    individual_records = []
    for record in data["records"]:
        path, archived_at = validate_record(record)
        parts = PurePosixPath(path).parts
        if parts[1] == "task" and len(parts) >= 4:
            folder = PurePosixPath(*parts[:3]).as_posix()
            task_folders.setdefault(folder, []).append((record, archived_at))
        else:
            individual_records.append((record, path, archived_at))

    # A folder archive is one immutable snapshot. Require its parent and child
    # index, and one timestamp, before any part of the folder can expire.
    for folder, entries in task_folders.items():
        paths = {record["path"] for record, _stamp in entries}
        required = {folder + "/task.md", folder + "/subtasks/README.md"}
        if not required.issubset(paths):
            missing = sorted(required - paths)
            raise ValueError(
                "Task-folder archive index is incomplete for " + folder
                + ": missing " + ", ".join(missing)
            )
        timestamps = {stamp for _record, stamp in entries}
        if len(timestamps) != 1:
            raise ValueError(
                "Task-folder archive entries must share one archived_at_utc timestamp: "
                + folder
            )
        archived_at = next(iter(timestamps))
        if now >= archived_at + RETENTION_PERIOD:
            due.extend(record["path"] for record, _stamp in entries)
        else:
            retained.extend(record for record, _stamp in entries)

    # Legacy flat task archives and report files retain their individual policy.
    for record, path, archived_at in individual_records:
        if now >= archived_at + RETENTION_PERIOD:
            due.append(path)
        else:
            retained.append(record)

    if not due:
        return [], False
    archive_root = repository_root / ".archive"
    for family in ("task", "reports"):
        family_dir = archive_root / family
        if archive_root.is_symlink() or family_dir.is_symlink():
            raise ValueError(f"Refusing to follow symlink in {family_dir}.")
    targets = []
    for path in due:
        target = repository_root / PurePosixPath(path)
        cursor = repository_root
        for component in PurePosixPath(path).parts:
            cursor = cursor / component
            if cursor.is_symlink():
                raise ValueError(f"Refusing to follow a symlink in indexed path: {path}")
        if target.exists() and not target.is_file():
            raise ValueError(f"Indexed archive path is not a regular file: {path}")
        targets.append((path, target))
    deleted = []
    for path, target in targets:
        if target.exists():
            target.unlink()
            deleted.append(path)
    data["records"] = retained
    temporary = index_path.with_name(index_path.name + ".tmp")
    temporary.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    temporary.replace(index_path)
    return deleted, True

def require_scheduled_event(event_name: str | None, actions_context: str | None) -> None:
    if event_name != "schedule" or actions_context != "true":
        raise RuntimeError("Archive retention can run only from a scheduled GitHub Actions run.")

def main() -> int:
    try:
        require_scheduled_event(os.environ.get("GITHUB_EVENT_NAME"), os.environ.get("GITHUB_ACTIONS"))
        test_script = ROOT / ".github" / "scripts" / "test_cleanup_archive.py"
        subprocess.run([sys.executable, str(test_script)], cwd=ROOT, check=True)
        deleted, changed = clean_due_records(INDEX_FILE, ROOT, utc_now())
        if changed:
            subprocess.run(["git", "add", "--", INDEX_RELATIVE, *deleted], cwd=ROOT, check=True)
        output_path = os.environ.get("GITHUB_OUTPUT")
        if not output_path:
            raise RuntimeError("GITHUB_OUTPUT is not available in the scheduled workflow.")
        with open(output_path, "a", encoding="utf-8") as output:
            output.write("deleted_paths<<EOF\n" + "\n".join(deleted) + "\nEOF\n")
        print(f"Retention index updated. Deleted {len(deleted)} indexed file(s)." if changed else "No indexed files have reached 90 days. Archive directories were not accessed.")
        return 0
    except Exception as error:
        print(f"::error::{error}", file=sys.stderr)
        return 1

if __name__ == "__main__":
    raise SystemExit(main())
