#!/usr/bin/env python3
"""Verify published drawing assets and GitHub links against a pushed Git ref."""
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import os
import re
import subprocess
import sys
from pathlib import Path
from typing import Callable
from urllib.parse import quote, unquote


BlobReader = Callable[[str], bytes | None]


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def valid_webp_bytes(data: bytes) -> bool:
    return (
        len(data) >= 12
        and data[:4] == b"RIFF"
        and data[8:12] == b"WEBP"
        and int.from_bytes(data[4:8], "little") + 8 == len(data)
    )


def github_blob_url(relative_path: str, repository: str, branch: str,
                    server_url: str = "https://github.com") -> str:
    return (
        f"{server_url.rstrip('/')}/{repository}/blob/{branch}/"
        f"{quote(relative_path, safe='/')}"
    )


def verify_manifest_row(row: dict[str, str], blob_reader: BlobReader,
                        expected_url: str) -> tuple[str, str]:
    """Verify remote URL, WebP bytes, and original bytes when retained."""
    webp_path = (row.get("webp_path") or "").strip()
    if not webp_path:
        return "Failed", "webp_path is missing."
    if (row.get("github_url") or "").strip() != expected_url:
        return "Failed", "github_url does not point to the expected published WebP path."

    webp_bytes = blob_reader(webp_path)
    if webp_bytes is None:
        return "Failed", f"Published WebP is missing from the target Git ref: {webp_path}"
    if not valid_webp_bytes(webp_bytes):
        return "Failed", f"Published WebP is not a valid RIFF/WEBP file: {webp_path}"
    expected_webp_sha = (row.get("webp_sha256") or "").strip().lower()
    if not expected_webp_sha or sha256_bytes(webp_bytes) != expected_webp_sha:
        return "Failed", f"Published WebP SHA-256 does not match the manifest: {webp_path}"

    original_path = (row.get("original_path") or "").strip()
    expected_original_sha = (row.get("sha256") or "").strip().lower()
    if not original_path or not expected_original_sha:
        return (
            "Not verifiable",
            "The WebP path and derivative hash are verified, but the original master or its SHA-256 is unavailable.",
        )

    original_bytes = blob_reader(original_path)
    if original_bytes is None:
        return "Failed", f"Published original master is missing from the target Git ref: {original_path}"
    actual_original_sha = sha256_bytes(original_bytes)
    if actual_original_sha != expected_original_sha:
        return "Failed", f"Published original master SHA-256 does not match the manifest: {original_path}"

    recorded_master_sha = (row.get("original_sha256") or "").strip().lower()
    if recorded_master_sha and actual_original_sha != recorded_master_sha:
        return "Failed", f"original_sha256 does not match the published master: {original_path}"

    # A generation-hash mismatch is a provenance review flag, not a storage
    # failure. The published original is verified against the uploaded-source
    # hash above; mapping confidence is kept separately in mapping_status.

    return "Verified", ""




def verify_session_links(row: dict[str, str], blob_reader: BlobReader) -> str:
    """Verify remote daily README inventory/table and attempt-note links."""
    webp_path = (row.get("webp_path") or "").strip()
    parts = Path(webp_path).parts
    if len(parts) != 4 or parts[0] != "drawings" or parts[2] != "images":
        return f"Drawing WebP path is not in a dated session images folder: {webp_path}"
    session_date = parts[1]
    relative_link = f"images/{parts[3]}"

    readme_path = f"drawings/{session_date}/README.md"
    readme_bytes = blob_reader(readme_path)
    if readme_bytes is None:
        return f"Published daily README is missing: {readme_path}"
    try:
        readme = readme_bytes.decode("utf-8")
    except UnicodeDecodeError:
        return f"Published daily README is not UTF-8: {readme_path}"

    link_pattern = re.compile(r"\[[^\]]+\]\((images/[^)]+\.webp)\)")
    inventory_pattern = re.compile(
        r"(?ms)^## Image inventory — (?:all \d+(?: WebP delivery)? files|"
        r"\d+ WebP delivery files \+ \d+ original masters? \(\d+ files? total\))[ \t]*\n"
        r".*?(?=^## |\Z)"
    )
    inventory = inventory_pattern.search(readme)
    if not inventory:
        return f"Published daily README has no image inventory section: {readme_path}"
    inventory_links = {unquote(link) for link in link_pattern.findall(inventory.group(0))}
    if relative_link not in inventory_links:
        return f"Published daily README inventory does not link {relative_link}."

    attempt = (row.get("attempt") or "").strip()
    if not attempt:
        return ""

    if not attempt.isdigit() or not 1 <= int(attempt) <= 999:
        return f"Manifest has an invalid attempt value for {webp_path}: {attempt!r}"
    attempt_number = str(int(attempt)).zfill(2)
    attempt_path = f"drawings/{session_date}/attempt-{attempt_number}.md"
    attempt_bytes = blob_reader(attempt_path)
    if attempt_bytes is None:
        return f"Published attempt record is missing: {attempt_path}"
    try:
        attempt_text = attempt_bytes.decode("utf-8")
    except UnicodeDecodeError:
        return f"Published attempt record is not UTF-8: {attempt_path}"

    repository_section = re.search(
        r"(?ms)^## Repository images[ \t]*\n.*?(?=^## |\Z)",
        attempt_text,
    )
    if not repository_section:
        return f"Published attempt record has no Repository images section: {attempt_path}"
    attempt_links = {unquote(link) for link in link_pattern.findall(repository_section.group(0))}
    if relative_link not in attempt_links:
        return f"Published attempt record does not link {relative_link}: {attempt_path}"

    lines = readme.splitlines()
    header_rows = [
        index for index, line in enumerate(lines)
        if line.strip().startswith("|")
        and "Attempt / prompt" in line
        and "Image" in line
    ]
    if len(header_rows) != 1:
        return f"Published daily README must have exactly one attempt table: {readme_path}"
    header_index = header_rows[0]
    row_pattern = re.compile(rf"\]\(attempt-{re.escape(attempt_number)}\.md\)")
    matching_rows = [
        index for index in range(header_index + 2, len(lines))
        if row_pattern.search(lines[index])
    ]
    if len(matching_rows) != 1:
        return (
            f"Published daily README has {len(matching_rows)} rows for attempt "
            f"{attempt_number}: {readme_path}"
        )
    cells = [cell.strip() for cell in lines[matching_rows[0]].strip().strip("|").split("|")]
    if len(cells) != 6:
        return f"Published daily README attempt row is malformed: {readme_path}"
    table_links = {unquote(link) for link in link_pattern.findall(cells[5])}
    if relative_link not in table_links:
        return f"Published daily README attempt row does not link {relative_link}: {readme_path}"
    return ""


def git_blob_reader(git_ref: str) -> BlobReader:
    def read(relative_path: str) -> bytes | None:
        if not relative_path or relative_path.startswith("/") or ".." in Path(relative_path).parts:
            return None
        result = subprocess.run(
            ["git", "cat-file", "blob", f"{git_ref}:{relative_path}"],
            capture_output=True,
            check=False,
        )
        return result.stdout if result.returncode == 0 else None
    return read


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--git-ref", default="origin/gpt")
    parser.add_argument("--repository", default=os.environ.get("GITHUB_REPOSITORY", "dungnv2602/chatgpt"))
    parser.add_argument("--branch", default=os.environ.get("GITHUB_REF_NAME", "gpt"))
    parser.add_argument("--server-url", default=os.environ.get("GITHUB_SERVER_URL", "https://github.com"))
    parser.add_argument("--check-only", action="store_true")
    args = parser.parse_args()

    root = Path(args.repo_root).resolve()
    manifests = sorted((root / "drawings").glob("*/manifest.csv"))
    if not manifests:
        print("No drawing session manifests found.")
        return 0

    blob_reader = git_blob_reader(args.git_ref)
    failures: list[str] = []
    checked = 0
    for manifest_path in manifests:
        if manifest_path.is_symlink() or not manifest_path.is_file():
            failures.append(f"Manifest is not a regular file: {manifest_path}")
            continue
        relative_manifest = manifest_path.relative_to(root).as_posix()
        if args.check_only:
            published_manifest = blob_reader(relative_manifest)
            if published_manifest is None or published_manifest != manifest_path.read_bytes():
                failures.append(f"Published manifest does not match the checked-out file: {relative_manifest}")
                continue

        try:
            with manifest_path.open("r", newline="", encoding="utf-8") as handle:
                reader = csv.DictReader(handle)
                fieldnames = list(reader.fieldnames or [])
                rows = [dict(row) for row in reader]
        except (OSError, UnicodeError, csv.Error) as exc:
            failures.append(f"Cannot read {relative_manifest}: {exc}")
            continue
        if not {"github_url", "webp_path", "verification_status"}.issubset(fieldnames):
            failures.append(f"Manifest is missing required verification columns: {relative_manifest}")
            continue
        if "verification_error" not in fieldnames:
            fieldnames.append("verification_error")

        changed = False
        for row in rows:
            webp_path = (row.get("webp_path") or "").strip()
            expected_url = github_blob_url(
                webp_path, args.repository, args.branch, args.server_url
            ) if webp_path else ""
            status, error = verify_manifest_row(row, blob_reader, expected_url)
            if status != "Failed":
                link_error = verify_session_links(row, blob_reader)
                if link_error:
                    status, error = "Failed", link_error
            current = (row.get("verification_status") or "").strip()
            if args.check_only:
                if current in {"Pending", "Failed"}:
                    failures.append(
                        f"{relative_manifest}: {row.get('image_id', '(no image_id)')} has status {current}."
                    )
                elif current != status:
                    failures.append(
                        f"{relative_manifest}: {row.get('image_id', '(no image_id)')} "
                        f"claims {current}, but published verification returns {status}."
                    )
            else:
                if current != status or (row.get("verification_error") or "") != error:
                    row["verification_status"] = status
                    row["verification_error"] = error
                    changed = True
            checked += 1

        if not args.check_only and changed:
            buffer = io.StringIO(newline="")
            writer = csv.DictWriter(
                buffer, fieldnames=fieldnames, extrasaction="ignore", lineterminator="\n"
            )
            writer.writeheader()
            writer.writerows(rows)
            manifest_path.write_text(buffer.getvalue(), encoding="utf-8")

    if args.check_only:
        if failures:
            for failure in failures:
                print(f"ERROR: {failure}", file=sys.stderr)
            return 1
        print(f"Published verification passed for {checked} manifest row(s).")
        return 0

    print(f"Checked {checked} manifest row(s); verification statuses updated where needed.")
    # Publish Failed statuses before the workflow's final --check-only pass.
    # The latter deliberately returns non-zero after the diagnostics are on-branch.
    for failure in failures:
        print(f"ERROR: {failure}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
