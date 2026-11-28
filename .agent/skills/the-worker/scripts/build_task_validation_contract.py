#!/usr/bin/env python3
"""Build the exact-SHA contract declared by the task named in a commit trailer."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any


TASK_ID_PATTERN = re.compile(r"^[0-9]{8}-[0-9]{6}(?:-[0-9]{2})*$")
TRAILER_PATTERN = re.compile(r"^Task-ID:[ \t]*([0-9]{8}-[0-9]{6}(?:-[0-9]{2})*)[ \t]*$", re.MULTILINE)
CONTRACT_PATTERN = re.compile(r"^## Validation Contract\s*\n\s*```json\s*\n(.*?)\n```\s*$", re.MULTILINE | re.DOTALL)


class TaskContractError(ValueError):
    """Raised when task attribution or its declared contract is invalid."""


def extract_task_id(commit_message: str) -> str:
    matches = TRAILER_PATTERN.findall(commit_message)
    if len(matches) != 1 or not TASK_ID_PATTERN.fullmatch(matches[0]):
        raise TaskContractError("Commit message must contain exactly one valid Task-ID trailer")
    return matches[0]


def find_task_record(root: Path, task_id: str) -> Path:
    matches: list[Path] = []
    tasks_root = root / "workspace" / "tasks"
    for path in tasks_root.glob("*/task.md"):
        if path.is_file() and re.search(rf"^- \*\*ID:\*\* {re.escape(task_id)}$", path.read_text(encoding="utf-8"), re.MULTILINE):
            matches.append(path)
    for path in tasks_root.glob("*/subtasks/*.md"):
        if path.is_file() and re.search(rf"^- \*\*ID:\*\* {re.escape(task_id)}$", path.read_text(encoding="utf-8"), re.MULTILINE):
            matches.append(path)
    if len(matches) != 1:
        raise TaskContractError(f"Task ID must resolve to exactly one active task record: {task_id}")
    return matches[0]


def parse_declared_contract(task_record: Path) -> dict[str, Any]:
    content = task_record.read_text(encoding="utf-8")
    matches = CONTRACT_PATTERN.findall(content)
    if len(matches) != 1:
        raise TaskContractError("Task record must contain exactly one JSON Validation Contract block")
    try:
        value = json.loads(matches[0])
    except json.JSONDecodeError as exc:
        raise TaskContractError(f"Task Validation Contract is not valid JSON: {exc}") from exc
    if not isinstance(value, dict) or set(value) != {"contract_revision", "checks"}:
        raise TaskContractError("Task Validation Contract must contain only contract_revision and checks")
    revision = value.get("contract_revision")
    checks = value.get("checks")
    if not isinstance(revision, str) or not 1 <= len(revision) <= 128:
        raise TaskContractError("contract_revision must be a non-empty string of at most 128 characters")
    if not isinstance(checks, list):
        raise TaskContractError("checks must be a JSON array")
    return value


def build_contract(root: Path, source_sha: str, commit_message: str) -> tuple[dict[str, Any], str]:
    if not re.fullmatch(r"[0-9a-f]{40}", source_sha):
        raise TaskContractError("Source SHA must be 40 lowercase hexadecimal characters")
    task_id = extract_task_id(commit_message)
    record = find_task_record(root, task_id)
    declared = parse_declared_contract(record)
    contract = {
        "schema_version": 1,
        "source_sha": source_sha,
        "contract_revision": declared["contract_revision"],
        "checks": declared["checks"],
    }
    return contract, task_id


def read_commit_message(root: Path, source_sha: str) -> str:
    try:
        result = subprocess.run(
            ["git", "show", "-s", "--format=%B", source_sha],
            cwd=root,
            check=True,
            capture_output=True,
            text=True,
            timeout=10,
        )
    except (OSError, subprocess.SubprocessError) as exc:
        raise TaskContractError(f"Cannot read source commit message: {exc}") from exc
    return result.stdout


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--source-sha", required=True)
    args = parser.parse_args()
    try:
        root = args.root.resolve(strict=True)
        message = read_commit_message(root, args.source_sha)
        contract, task_id = build_contract(root, args.source_sha, message)
        print(json.dumps(contract, ensure_ascii=True, separators=(",", ":")))
        print(f"::notice::Task validation contract resolved for {task_id}", file=sys.stderr)
        return 0
    except (TaskContractError, OSError, UnicodeError) as exc:
        print(json.dumps({"error": str(exc)}), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
