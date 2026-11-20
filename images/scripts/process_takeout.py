#!/usr/bin/env python3
"""Process one images/takeout hand-off as a verified, rollback-capable batch."""
from __future__ import annotations
import argparse, csv, hashlib, io, os, re, subprocess, sys, unicodedata
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath
from typing import Any
from urllib.parse import quote, unquote
import yaml

SUPPORTED = {".png", ".jpg", ".jpeg"}
KNOWN_IMAGE = SUPPORTED | {".apng", ".gif", ".webp", ".bmp", ".tif", ".tiff", ".heic", ".heif", ".avif"}
HANDOFF = "HANDOFF.yml"
EMPTY_HANDOFF = "version: 1\nstatus: empty\nitems: []\n"
FIELDS = [
    "source_filename", "source_path", "title", "asset_id", "attempt", "destination_dir",
    "image_id", "master_path", "webp_path", "manifest_path", "staging_webp_path",
    "source_format", "conversion_profile", "original_bytes", "webp_bytes",
    "size_change_percent", "source_sha256", "master_sha256", "webp_sha256",
    "generation_sha256", "output_id", "prompt_id", "native_generation_id",
    "native_output_id", "mapping_status", "hash_match", "cwebp_version", "status", "error",
]
MANIFEST_FIELDS = [
    "session_date", "image_id", "filename", "prompt_id", "approval_status",
    "github_url", "sha256", "verification_status", "attempt", "output_id",
    "native_generation_id", "native_output_id", "mapping_status",
    "mapping_evidence", "original_path", "webp_path", "original_sha256",
    "webp_sha256", "generation_sha256", "hash_match", "original_bytes_available",
    "verification_error",
]

class ProcessingError(Exception):
    pass

def digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()

def slugify(title: str) -> str:
    original = title
    value = title.strip().replace("Đ", "D").replace("đ", "d")
    value = unicodedata.normalize("NFKD", value)
    value = "".join(c for c in value if not unicodedata.combining(c))
    value = value.encode("ascii", "ignore").decode("ascii").lower()
    value = re.sub(r"[^a-z0-9]+", "-", value).strip("-")
    if not value:
        raise ProcessingError(f"Title {original!r} cannot produce a safe filename; use Latin letters or numbers.")
    return value

def validate_batch_id(value: Any) -> str:
    if not isinstance(value, str) or not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]{0,79}", value):
        raise ProcessingError("batch_id must be 1–80 safe letters, numbers, dots, underscores or hyphens.")
    return value

def destination_dir(value: Any, root: Path) -> Path:
    if not isinstance(value, str) or not value.strip() or "\\" in value:
        raise ProcessingError("Each item needs a repository-relative destination_dir using forward slashes.")
    p = PurePosixPath(value)
    parts = p.parts
    if p.is_absolute() or not parts or any(x in {".", ".."} for x in parts):
        raise ProcessingError(f"Unsafe destination_dir: {value!r}")
    if parts[0] not in {"images", "novel", "drawings"}:
        raise ProcessingError("Destinations must be inside images/, novel/, or a dated drawing session's images/ folder.")
    if parts[0] == "images" and len(parts) > 1 and parts[1] in {"takeout", "webp", "scripts"}:
        raise ProcessingError(f"Reserved image destination: {value!r}")
    if parts[0] == "drawings":
        if len(parts) != 3 or parts[2] != "images" or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", parts[1]):
            raise ProcessingError("Drawing output destinations must be drawings/YYYY-MM-DD/images.")
        try:
            datetime.strptime(parts[1], "%Y-%m-%d")
        except ValueError as exc:
            raise ProcessingError(f"Invalid drawing-session date in destination: {parts[1]}") from exc
    result = root.joinpath(*parts)
    try:
        result.resolve(strict=False).relative_to(root.resolve())
    except ValueError as exc:
        raise ProcessingError(f"Destination escapes the repository: {value!r}") from exc
    return result

def reject_symlink_components(path: Path, root: Path) -> None:
    current = root
    for part in path.relative_to(root).parts:
        current = current / part
        if current.is_symlink():
            raise ProcessingError(f"Symlink destination component is not allowed: {current.relative_to(root).as_posix()}")

def is_apng(path: Path) -> bool:
    with path.open("rb") as f:
        if f.read(8) != b"\x89PNG\r\n\x1a\n":
            return False
        size = path.stat().st_size
        while True:
            header = f.read(8)
            if len(header) != 8:
                return False
            length, kind = int.from_bytes(header[:4], "big"), header[4:]
            if kind == b"acTL":
                return True
            if kind == b"IEND":
                return False
            if f.tell() + length + 4 > size:
                raise ProcessingError(f"Corrupt PNG chunk length: {path.name}")
            f.seek(length + 4, os.SEEK_CUR)

def valid_webp(path: Path) -> bool:
    if not path.is_file() or path.stat().st_size < 12:
        return False
    with path.open("rb") as f:
        header = f.read(12)
    return header[:4] == b"RIFF" and header[8:12] == b"WEBP" and int.from_bytes(header[4:8], "little") + 8 == path.stat().st_size

def attempt_folder(history: Path, batch: str, staging_root: Path | None = None) -> Path:
    if history.is_symlink() or (history.exists() and not history.is_dir()):
        raise ProcessingError("images/takeout/history must be a normal directory.")
    history.mkdir(parents=True, exist_ok=True)
    batch_root = history / batch
    if batch_root.is_symlink() or (batch_root.exists() and not batch_root.is_dir()):
        raise ProcessingError(f"Batch history path must be a normal directory: {batch}")
    batch_root.mkdir(parents=True, exist_ok=True)

    staging_batch_root = None
    if staging_root is not None:
        if staging_root.is_symlink() or (staging_root.exists() and not staging_root.is_dir()):
            raise ProcessingError("images/takeout/webp must be a normal directory.")
        staging_root.mkdir(parents=True, exist_ok=True)
        staging_batch_root = staging_root / batch
        if staging_batch_root.is_symlink() or (staging_batch_root.exists() and not staging_batch_root.is_dir()):
            raise ProcessingError(f"WebP staging batch path must be a normal directory: {batch}")
        staging_batch_root.mkdir(parents=True, exist_ok=True)

    n = 1
    while True:
        attempt_name = f"attempt-{n:03d}"
        history_attempt = batch_root / attempt_name
        staging_attempt = staging_batch_root / attempt_name if staging_batch_root is not None else None
        if history_attempt.exists() or history_attempt.is_symlink() or (
            staging_attempt is not None and (staging_attempt.exists() or staging_attempt.is_symlink())
        ):
            n += 1
            continue
        return history_attempt

def write_reports(folder: Path, handoff: bytes, rows: list[dict[str, Any]], batch: str,
                  state: str, checks: list[str], errors: list[str], count: int) -> None:
    folder.mkdir(parents=True, exist_ok=True)
    (folder / HANDOFF).write_bytes(handoff)
    with (folder / "conversion-report.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)
    lines = [
        f"# Takeout Processing — {batch}", "",
        f"- Batch: {batch}", f"- Attempt: {folder.name}", f"- Status: {state}",
        f"- Items: {count}", f"- Generated: {datetime.now(timezone.utc).isoformat(timespec='seconds')}",
        "", "## Verification checks",
    ]
    lines.extend(f"- {x}" for x in (checks or ["No verification checks completed."]))
    lines.extend(["", "## Errors and warnings"])
    lines.extend(f"- {x}" for x in (errors or ["None."]))
    (folder / "verification-report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

def failure_rows(items: list[Any], error: str, version: str) -> list[dict[str, Any]]:
    rows = []
    for item in items:
        if not isinstance(item, dict):
            continue
        source = item.get("source", "")
        rows.append({
            "source_filename": source, "source_path": f"images/takeout/{source}" if source else "",
            "title": item.get("title", ""), "asset_id": item.get("asset_id", ""),
            "attempt": item.get("attempt", ""),
            "destination_dir": item.get("destination_dir", ""), "image_id": "",
            "master_path": "", "webp_path": "", "manifest_path": "",
            "source_format": Path(str(source)).suffix.lower().lstrip("."),
            "conversion_profile": "", "original_bytes": "", "webp_bytes": "",
            "size_change_percent": "", "source_sha256": "", "master_sha256": "",
            "webp_sha256": "", "generation_sha256": item.get("expected_sha256", ""),
            "output_id": item.get("output_id", ""), "prompt_id": item.get("prompt_id", ""),
            "native_generation_id": item.get("native_generation_id", ""),
            "native_output_id": item.get("native_output_id", ""),
            "mapping_status": "NOT_ASSESSED", "hash_match": "NOT_CHECKED",
            "cwebp_version": version, "status": "FAILED", "error": error,
        })
    return rows


def split_markdown_table_cells(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]

def prepare_attempt_readme_updates(prepared: list[dict[str, Any]], root: Path) -> dict[Path, str]:
    """Prepare idempotent attempt-record and daily-README links for session outputs."""
    grouped: dict[tuple[str, str], list[str]] = {}
    for item in prepared:
        attempt = item.get("attempt", "")
        if not attempt:
            continue
        relative_directory = item["directory"].relative_to(root).as_posix()
        match = re.fullmatch(r"drawings/(\d{4}-\d{2}-\d{2})/images", relative_directory)
        if not match:
            raise ProcessingError(
                "An item with attempt metadata must target drawings/YYYY-MM-DD/images."
            )
        session_date = match.group(1)
        try:
            datetime.strptime(session_date, "%Y-%m-%d")
        except ValueError as exc:
            raise ProcessingError(f"Invalid drawing-session date in destination: {session_date}") from exc
        grouped.setdefault((session_date, attempt), []).append(f"images/{item['webp'].name}")

    # Backfill confirmed mappings already present in the daily README table
    # into attempt records. Ambiguous and unmapped outputs are left untouched.
    for session_date in {date for date, _attempt in grouped}:
        session_dir = root / "drawings" / session_date
        for relative_link, attempts in linked_attempt_assets(session_dir).items():
            unique_attempts = list(dict.fromkeys(attempts))
            if len(unique_attempts) == 1:
                grouped.setdefault((session_date, unique_attempts[0]), []).append(relative_link)

    updates: dict[Path, str] = {}
    for (session_date, attempt), raw_links in grouped.items():
        links = list(dict.fromkeys(raw_links))
        session_dir = root / "drawings" / session_date
        attempt_path = session_dir / f"attempt-{attempt}.md"
        readme_path = session_dir / "README.md"
        for target_path in (attempt_path, readme_path):
            if target_path.is_symlink() or not target_path.is_file():
                raise ProcessingError(
                    f"Cannot link uploaded output: required session record is missing or unsafe: "
                    f"{target_path.relative_to(root).as_posix()}"
                )

        attempt_content = updates.get(attempt_path)
        if attempt_content is None:
            attempt_content = attempt_path.read_text(encoding="utf-8")
        heading_pattern = re.compile(
            r"(?ms)^## Repository images[ \t]*\n.*?(?=^## |\Z)"
        )
        section_match = heading_pattern.search(attempt_content)
        if section_match:
            section = section_match.group(0).rstrip()
            existing = [
                unquote(link)
                for link in re.findall(r"\[[^\]]+\]\((images/[^)]+)\)", section)
            ]
            additions = [link for link in links if link not in existing]
            if additions:
                section += "\n" + "\n".join(
                    f"- [{Path(link).name}]({quote(link, safe='/')})" for link in additions
                )
                attempt_content = (
                    attempt_content[:section_match.start()]
                    + section
                    + "\n\n"
                    + attempt_content[section_match.end():].lstrip("\n")
                )
        else:
            link_lines = "\n".join(
                f"- [{Path(link).name}]({quote(link, safe='/')})" for link in links
            )
            attempt_content = (
                attempt_content.rstrip()
                + "\n\n## Repository images\n\n"
                + link_lines
                + "\n"
            )
        updates[attempt_path] = attempt_content

        readme_content = updates.get(readme_path)
        if readme_content is None:
            readme_content = readme_path.read_text(encoding="utf-8")
        lines = readme_content.splitlines()
        header_rows = [
            index for index, line in enumerate(lines)
            if line.strip().startswith("|")
            and "Attempt / prompt" in line
            and "Image" in line
        ]
        if len(header_rows) != 1:
            raise ProcessingError(
                f"Daily README must contain exactly one attempt table with an Image column: "
                f"{readme_path.relative_to(root).as_posix()}"
            )
        header_index = header_rows[0]
        headers = split_markdown_table_cells(lines[header_index])
        if len(headers) != 6 or headers[5].lower() != "image":
            raise ProcessingError(
                f"Daily README attempt table must have exactly six columns with Image last: "
                f"{readme_path.relative_to(root).as_posix()}"
            )
        row_pattern = re.compile(rf"\]\(attempt-{re.escape(attempt)}\.md\)")
        matching_rows = [
            index for index in range(header_index + 2, len(lines))
            if row_pattern.search(lines[index])
        ]
        if len(matching_rows) != 1:
            raise ProcessingError(
                f"Expected exactly one README row for attempt {attempt}; found {len(matching_rows)}."
            )
        row_index = matching_rows[0]
        cells = split_markdown_table_cells(lines[row_index])
        if len(cells) != 6:
            raise ProcessingError(
                f"README row for attempt {attempt} does not contain exactly six columns."
            )
        existing_links = [
            unquote(link)
            for link in re.findall(r"\[[^\]]+\]\((images/[^)]+)\)", cells[5])
        ]
        merged_links = list(dict.fromkeys(existing_links + links))
        cells[5] = ", ".join(
            f"[{Path(link).name}]({quote(link, safe='/')})" for link in merged_links
        )
        lines[row_index] = "| " + " | ".join(cells) + " |"
        updates[readme_path] = "\n".join(lines) + ("\n" if readme_content.endswith("\n") else "")

    # Keep the daily README's all-assets inventory synchronized. Attempt rows
    # remain the canonical prompt links; this is the session-wide asset list.
    session_dates = {session_date for session_date, _attempt in grouped}
    inventory_heading = re.compile(
        r"(?m)^## Image inventory — (?:all \d+(?: WebP delivery)? files|\d+ WebP delivery files \+ \d+ original masters? \(\d+ files? total\))[ \t]*$"
    )
    inventory_section = re.compile(
        r"(?ms)^## Image inventory — (?:all \d+(?: WebP delivery)? files|\d+ WebP delivery files \+ \d+ original masters? \(\d+ files? total\))[ \t]*\n.*?(?=^## |\Z)"
    )
    inventory_links = re.compile(r"\[[^\]]+\]\((images/[^)]+\.webp)\)")
    for session_date in session_dates:
        session_dir = root / "drawings" / session_date
        readme_path = session_dir / "README.md"
        readme_content = updates.get(readme_path)
        if readme_content is None:
            readme_content = readme_path.read_text(encoding="utf-8")
        headings = inventory_heading.findall(readme_content)
        if not headings:
            continue
        if len(headings) != 1:
            raise ProcessingError(
                f"Daily README must contain at most one image inventory heading: "
                f"{readme_path.relative_to(root).as_posix()}"
            )
        section_match = inventory_section.search(readme_content)
        if not section_match:
            raise ProcessingError(
                f"Could not isolate daily README image inventory: "
                f"{readme_path.relative_to(root).as_posix()}"
            )
        section = section_match.group(0)
        image_dir = session_dir / "images"
        existing_webps = {
            f"images/{path.name}"
            for path in image_dir.glob("*.webp")
            if path.is_file() and not path.is_symlink()
        } if image_dir.is_dir() else set()
        new_links = {
            link
            for (date, _attempt), links in grouped.items()
            if date == session_date
            for link in links
        }
        all_webps = existing_webps | new_links
        current_heading = section.splitlines()[0]
        original_dir = image_dir / "original"
        if original_dir.is_symlink() or (original_dir.exists() and not original_dir.is_dir()):
            raise ProcessingError(
                f"Original-master directory is unsafe: {original_dir.relative_to(root).as_posix()}"
            )
        original_masters = (
            [
                path for path in original_dir.iterdir()
                if path.is_file() and not path.is_symlink()
                and path.suffix.lower() in SUPPORTED
            ]
            if original_dir.is_dir() else []
        )
        new_original_count = sum(
            1 for item in prepared
            if item["directory"].relative_to(root).as_posix()
            == f"drawings/{session_date}/images"
        )
        original_master_count = len(original_masters) + new_original_count
        total_assets = len(all_webps) + original_master_count
        original_label = "original master" if original_master_count == 1 else "original masters"
        file_label = "file" if total_assets == 1 else "files"
        replacement_heading = (
            f"## Image inventory — {len(all_webps)} WebP delivery files + "
            f"{original_master_count} {original_label} ({total_assets} {file_label} total)"
        )
        section = section.replace(current_heading, replacement_heading, 1)
        existing_inventory_links = {
            unquote(link) for link in inventory_links.findall(section)
        }
        # Inventory every actual delivery WebP, not only the most recent upload.
        # This also repairs omissions in older session inventories.
        additions = sorted(all_webps - existing_inventory_links)
        if additions:
            section = (
                section.rstrip()
                + "\n\n### Newly archived WebP assets\n\n"
                + "\n".join(
                    f"- [{Path(link).name}]({quote(link, safe='/')})" for link in additions
                )
                + "\n"
            )
        readme_content = (
            readme_content[:section_match.start()]
            + section
            + readme_content[section_match.end():]
        )
        updates[readme_path] = readme_content

    return updates


def github_blob_url(relative_path: str) -> str:
    server = os.environ.get("GITHUB_SERVER_URL", "https://github.com").rstrip("/")
    repository = os.environ.get("GITHUB_REPOSITORY", "dungnv2602/chatgpt")
    branch = os.environ.get("GITHUB_REF_NAME", "gpt")
    return f"{server}/{repository}/blob/{branch}/{quote(relative_path, safe='/')}"


def linked_attempt_assets(session_dir: Path) -> dict[str, list[str]]:
    """Read existing attempt-note WebP links as conservative legacy mapping evidence."""
    linked: dict[str, list[str]] = {}
    section_pattern = re.compile(r"(?ms)^## Repository images[ \t]*\n.*?(?=^## |\Z)")
    link_pattern = re.compile(r"\[[^\]]+\]\((images/[^)]+)\)")
    for attempt_path in sorted(session_dir.glob("attempt-*.md")):
        match = re.fullmatch(r"attempt-(\d{2,3})\.md", attempt_path.name)
        if not match or attempt_path.is_symlink() or not attempt_path.is_file():
            continue
        section = section_pattern.search(attempt_path.read_text(encoding="utf-8"))
        if not section:
            continue
        attempt = str(int(match.group(1))).zfill(2)
        for raw_link in link_pattern.findall(section.group(0)):
            link = unquote(raw_link)
            if link.lower().endswith(".webp"):
                linked.setdefault(link, []).append(attempt)

    # Older session archives may have their only confirmed image mapping in
    # the daily README row rather than an attempt-note Repository images block.
    readme_path = session_dir / "README.md"
    if readme_path.is_file() and not readme_path.is_symlink():
        lines = readme_path.read_text(encoding="utf-8").splitlines()
        header_rows = [
            index for index, line in enumerate(lines)
            if line.strip().startswith("|")
            and "Attempt / prompt" in line
            and "Image" in line
        ]
        if len(header_rows) == 1:
            header_index = header_rows[0]
            for line in lines[header_index + 2:]:
                if not line.strip().startswith("|"):
                    continue
                cells = split_markdown_table_cells(line)
                if len(cells) != 6:
                    continue
                attempt_match = re.search(r"\]\(attempt-(\d{2,3})\.md\)", cells[0])
                if not attempt_match:
                    continue
                attempt = str(int(attempt_match.group(1))).zfill(2)
                for raw_link in link_pattern.findall(cells[5]):
                    link = unquote(raw_link)
                    if link.lower().endswith(".webp"):
                        linked.setdefault(link, []).append(attempt)
    return linked


def legacy_manifest_row(session_date: str, session_dir: Path, webp: Path,
                        links: dict[str, list[str]]) -> dict[str, str]:
    relative_webp = f"drawings/{session_date}/{webp.relative_to(session_dir).as_posix()}"
    session_relative_webp = webp.relative_to(session_dir).as_posix()
    webp_sha = digest(webp)
    attempts = list(dict.fromkeys(links.get(session_relative_webp, [])))
    if len(attempts) == 1:
        attempt, mapping_status = attempts[0], "Corroborated"
        mapping_evidence = (
            f"Existing attempt-{attempt}.md Repository images link; "
            "generation-time output association and original hash were not recorded."
        )
    elif len(attempts) > 1:
        attempt, mapping_status = "", "Conflicting"
        mapping_evidence = "Existing attempt-note links associate this WebP with multiple attempts: " + ", ".join(attempts)
    else:
        attempt, mapping_status = "", "Unmapped"
        mapping_evidence = "Legacy WebP asset has no attempt-note link; no mapping was inferred."
    stable_key = hashlib.sha256((relative_webp + "\0" + webp_sha).encode("utf-8")).hexdigest()[:16]
    return {
        "session_date": session_date,
        "image_id": f"LEGACY-{stable_key}",
        "filename": relative_webp,
        "prompt_id": "",
        "approval_status": "Not recorded",
        "github_url": github_blob_url(relative_webp),
        "sha256": "",
        "verification_status": "Not verifiable",
        "verification_error": "Legacy derivative retained without an available original master or generation-time checksum.",
        "attempt": attempt,
        "output_id": "",
        "native_generation_id": "",
        "native_output_id": "",
        "mapping_status": mapping_status,
        "mapping_evidence": mapping_evidence,
        "original_path": "",
        "webp_path": relative_webp,
        "original_sha256": "",
        "webp_sha256": webp_sha,
        "generation_sha256": "",
        "hash_match": "NOT_PROVIDED",
        "original_bytes_available": "No",
    }


def prepare_session_manifest_updates(prepared: list[dict[str, Any]], root: Path) -> dict[Path, str]:
    """Append verified outputs and conservatively backfill legacy WebP assets."""
    grouped: dict[str, list[dict[str, Any]]] = {}
    for item in prepared:
        if not item.get("attempt"):
            continue
        relative_directory = item["directory"].relative_to(root).as_posix()
        match = re.fullmatch(r"drawings/(\d{4}-\d{2}-\d{2})/images", relative_directory)
        if not match:
            raise ProcessingError("Manifest entries require drawings/YYYY-MM-DD/images destinations.")
        session_date = match.group(1)
        grouped.setdefault(session_date, []).append(item)

    updates: dict[Path, str] = {}
    for session_date, session_items in grouped.items():
        session_dir = root / "drawings" / session_date
        manifest_path = session_dir / "manifest.csv"
        if manifest_path.is_symlink() or (manifest_path.exists() and not manifest_path.is_file()):
            raise ProcessingError(f"Session manifest is not a regular file: {manifest_path.relative_to(root).as_posix()}")

        if manifest_path.exists():
            try:
                with manifest_path.open("r", newline="", encoding="utf-8") as handle:
                    reader = csv.DictReader(handle)
                    existing_fields = list(reader.fieldnames or [])
                    rows = [dict(row) for row in reader]
            except (OSError, UnicodeError, csv.Error) as exc:
                raise ProcessingError(f"Cannot read session manifest {manifest_path}: {exc}") from exc
            if not existing_fields:
                raise ProcessingError(f"Session manifest has no CSV header: {manifest_path.relative_to(root).as_posix()}")
        else:
            existing_fields, rows = list(MANIFEST_FIELDS), []

        fieldnames = list(existing_fields)
        for field in MANIFEST_FIELDS:
            if field not in fieldnames:
                fieldnames.append(field)

        seen_ids: dict[str, dict[str, str]] = {}
        seen_webps: dict[str, dict[str, str]] = {}
        for row in rows:
            image_id = (row.get("image_id") or "").strip()
            webp_path = (row.get("webp_path") or "").strip()
            if image_id:
                if image_id in seen_ids:
                    raise ProcessingError(f"Duplicate image_id in session manifest: {image_id}")
                seen_ids[image_id] = row
            if webp_path:
                if webp_path in seen_webps:
                    raise ProcessingError(f"Duplicate webp_path in session manifest: {webp_path}")
                seen_webps[webp_path] = row

        image_dir = session_dir / "images"
        if image_dir.is_symlink() or (image_dir.exists() and not image_dir.is_dir()):
            raise ProcessingError(f"Session images directory is unsafe: {image_dir.relative_to(root).as_posix()}")
        links = linked_attempt_assets(session_dir)
        new_webp_paths = {
            item["webp"].relative_to(root).as_posix()
            for item in session_items
        }

        if image_dir.is_dir():
            for legacy_webp in sorted(image_dir.glob("*.webp")):
                if legacy_webp.is_symlink() or not legacy_webp.is_file():
                    raise ProcessingError(f"Legacy WebP is not a regular file: {legacy_webp.relative_to(root).as_posix()}")
                relative_webp = legacy_webp.relative_to(root).as_posix()
                if relative_webp in new_webp_paths or relative_webp in seen_webps:
                    continue
                if not valid_webp(legacy_webp):
                    raise ProcessingError(f"Legacy WebP failed container validation: {relative_webp}")
                legacy_row = legacy_manifest_row(session_date, session_dir, legacy_webp, links)
                if legacy_row["image_id"] in seen_ids:
                    raise ProcessingError(f"Legacy manifest image_id collision: {legacy_row['image_id']}")
                rows.append(legacy_row)
                seen_ids[legacy_row["image_id"]] = legacy_row
                seen_webps[relative_webp] = legacy_row

        for item in session_items:
            relative_master = item["master"].relative_to(root).as_posix()
            relative_webp = item["webp"].relative_to(root).as_posix()
            image_id = item["output_id"] or f"A{item['attempt']}-O-{item['source_sha'][:12]}"
            if item["hash_match"] == "MATCH":
                mapping_status = "Verified"
                mapping_evidence = "Uploaded original SHA-256 matches the recorded generation-time SHA-256."
            elif item["hash_match"] == "MISMATCH":
                mapping_status = "Probable"
                mapping_evidence = (
                    (item.get("mapping_evidence") + " ") if item.get("mapping_evidence") else ""
                ) + (
                    "Uploaded-original SHA-256 differs from the supplied generation-time hash; "
                    "retained for manual review and not marked Verified."
                )
            else:
                mapping_status = "Corroborated"
                mapping_evidence = item.get("mapping_evidence") or (
                    f"HANDOFF explicitly assigns this upload to attempt {item['attempt']}; "
                    "generation-time SHA-256/native output IDs were unavailable."
                )
            row = {
                "session_date": session_date,
                "image_id": image_id,
                "filename": relative_master,
                "prompt_id": item["prompt_id"],
                "approval_status": item["approval_status"],
                "github_url": github_blob_url(relative_webp),
                "sha256": item["source_sha"],
                "verification_status": "Pending",
                "verification_error": "Awaiting GitHub post-push asset and URL read-back verification.",
                "attempt": item["attempt"],
                "output_id": item["output_id"],
                "native_generation_id": item["native_generation_id"],
                "native_output_id": item["native_output_id"],
                "mapping_status": mapping_status,
                "mapping_evidence": mapping_evidence,
                "original_path": relative_master,
                "webp_path": relative_webp,
                "original_sha256": item["master_sha"],
                "webp_sha256": item["webp_sha"],
                "generation_sha256": item["expected_sha"],
                "hash_match": item["hash_match"],
                "original_bytes_available": "Yes",
            }
            prior_by_id = seen_ids.get(image_id)
            prior_by_webp = seen_webps.get(relative_webp)
            if prior_by_id or prior_by_webp:
                prior = prior_by_id or prior_by_webp
                if (prior.get("webp_path") == relative_webp
                        and prior.get("sha256") == item["source_sha"]):
                    continue
                raise ProcessingError(
                    f"Conflicting session manifest identity for image {image_id} or {relative_webp}."
                )
            rows.append(row)
            seen_ids[image_id] = row
            seen_webps[relative_webp] = row

        buffer = io.StringIO(newline="")
        writer = csv.DictWriter(buffer, fieldnames=fieldnames, extrasaction="ignore", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
        updates[manifest_path] = buffer.getvalue()

    return updates


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--run-id", default="local")
    args = parser.parse_args()
    root = Path(args.repo_root).resolve()
    inbox = root / "images" / "takeout"
    manifest = inbox / HANDOFF
    if inbox.is_symlink():
        print("images/takeout/ must not be a symlink.", file=sys.stderr)
        return 1
    if not manifest.exists():
        print("No HANDOFF.yml; no-op. Uploaded files remain untouched.")
        return 0
    if manifest.is_symlink() or not manifest.is_file():
        print("HANDOFF.yml must be a regular file.", file=sys.stderr)
        return 1
    raw = manifest.read_bytes()
    try:
        data = yaml.safe_load(raw.decode("utf-8"))
    except Exception as exc:
        batch = f"invalid-run-{args.run_id}"
        folder = attempt_folder(inbox / "history", batch)
        msg = f"HANDOFF.yml is not valid UTF-8 YAML: {exc}"
        write_reports(folder, raw, [], batch, "FAILED", [], [msg], 0)
        print(msg, file=sys.stderr)
        return 1
    if not isinstance(data, dict):
        batch = f"invalid-run-{args.run_id}"
        folder = attempt_folder(inbox / "history", batch)
        msg = "HANDOFF.yml must contain a YAML mapping at its top level."
        write_reports(folder, raw, [], batch, "FAILED", [], [msg], 0)
        print(msg, file=sys.stderr)
        return 1
    handoff_status = data.get("status")
    if handoff_status in {"draft", "empty"}:
        print(f"Hand-off status is {handoff_status!r}; no-op. Uploaded files remain untouched.")
        return 0
    if handoff_status != "ready":
        batch = f"invalid-run-{args.run_id}"
        folder = attempt_folder(inbox / "history", batch)
        msg = f"HANDOFF.yml status must be 'draft', 'empty', or 'ready'; got {handoff_status!r}."
        items = data.get("items") if isinstance(data.get("items"), list) else []
        write_reports(folder, raw, failure_rows(items, msg, ""), batch, "FAILED", [], [msg], len(items))
        print(msg, file=sys.stderr)
        return 1
    try:
        batch = validate_batch_id(data.get("batch_id"))
    except ProcessingError as exc:
        batch = f"invalid-run-{args.run_id}"
        folder = attempt_folder(inbox / "history", batch)
        items = data.get("items") if isinstance(data.get("items"), list) else []
        write_reports(folder, raw, failure_rows(items, str(exc), ""), batch, "FAILED", [], [str(exc)], len(items))
        print(str(exc), file=sys.stderr)
        return 1

    folder = attempt_folder(inbox / "history", batch, inbox / "webp")
    raw_items = data.get("items")
    items_report = raw_items if isinstance(raw_items, list) else []
    errors: list[str] = []
    checks: list[str] = []
    prepared: list[dict[str, Any]] = []
    moved: list[tuple[Path, Path]] = []
    staged_moves: list[tuple[Path, Path]] = []
    written_text_updates: list[tuple[Path, bytes | None]] = []
    stage_root = inbox / "webp" / batch / folder.name
    encoder_version = ""

    try:
        if type(data.get("version")) is not int or data.get("version") != 1:
            raise ProcessingError("HANDOFF.yml version must be integer 1.")
        if not isinstance(raw_items, list) or not raw_items:
            raise ProcessingError("A ready hand-off must contain at least one item.")
        if not inbox.is_dir():
            raise ProcessingError("images/takeout/ does not exist.")
        version = subprocess.run(["cwebp", "-version"], capture_output=True, text=True, check=True)
        encoder_version = (version.stdout or version.stderr).strip()

        inbox_images: set[str] = set()
        for child in inbox.iterdir():
            if child.name in {"history", "webp"}:
                if child.is_symlink() or not child.is_dir():
                    raise ProcessingError(f"images/takeout/{child.name} must be a normal directory.")
                continue
            if child.name == HANDOFF:
                continue
            if child.is_symlink() or child.is_dir() or not child.is_file():
                raise ProcessingError(f"Unexpected directory, symlink or non-file in takeout: {child.name}")
            suffix = child.suffix.lower()
            if suffix not in SUPPORTED:
                if suffix in KNOWN_IMAGE:
                    raise ProcessingError(f"Unsupported image format {suffix} for {child.name}; only PNG, JPG and JPEG are accepted. Animated images are never flattened.")
                raise ProcessingError(f"Unexpected non-image file in takeout: {child.name}")
            inbox_images.add(child.name)
        checks.append("Inbox is flat and contains only PNG/JPG/JPEG files, HANDOFF.yml, and the reserved history/ and webp/ directories.")

        sources: set[str] = set()
        ids: set[str] = set()
        output_ids: set[str] = set()
        targets: set[str] = set()
        for number, item in enumerate(raw_items, start=1):
            if not isinstance(item, dict):
                raise ProcessingError(f"items[{number - 1}] must be a mapping.")
            name = item.get("source")
            if not isinstance(name, str) or not name or Path(name).name != name or "/" in name or "\\" in name:
                raise ProcessingError(f"Item {number}: source must be a filename directly inside images/takeout/.")
            if name in sources:
                raise ProcessingError(f"Duplicate source filename: {name}")
            sources.add(name)
            source = inbox / name
            if source.is_symlink() or not source.is_file() or source.stat().st_size == 0:
                raise ProcessingError(f"Source is missing, empty or not a regular file: {name}")
            suffix = source.suffix.lower()
            if suffix not in SUPPORTED:
                raise ProcessingError(f"Unsupported source format: {name}")
            title = item.get("title")
            if not isinstance(title, str) or not title.strip():
                raise ProcessingError(f"Item {number} requires a descriptive title.")
            slug = slugify(title)
            asset_id = item.get("asset_id", "")
            if asset_id is None:
                asset_id = ""
            if asset_id != "":
                if not isinstance(asset_id, str) or not re.fullmatch(r"[A-Z][A-Z0-9-]{0,31}", asset_id):
                    raise ProcessingError(f"Invalid asset_id {asset_id!r}; use uppercase letters, numbers and hyphens, e.g. ILL-001.")
                if asset_id in ids:
                    raise ProcessingError(f"Duplicate asset_id: {asset_id}")
                ids.add(asset_id)
            directory = destination_dir(item.get("destination_dir"), root)
            attempt_value = item.get("attempt")
            attempt_ref = ""
            is_drawing_session_asset = bool(
                re.fullmatch(r"drawings/\d{4}-\d{2}-\d{2}/images", directory.relative_to(root).as_posix())
            )
            if is_drawing_session_asset and (attempt_value is None or attempt_value == ""):
                raise ProcessingError(
                    f"Item {number}: drawing-session images require explicit attempt metadata for manifest and prompt linking."
                )
            if attempt_value is not None and attempt_value != "":
                if isinstance(attempt_value, bool):
                    raise ProcessingError(f"Item {number}: attempt must be a positive integer or digit string.")
                if isinstance(attempt_value, int):
                    attempt_number = attempt_value
                elif isinstance(attempt_value, str) and re.fullmatch(r"\d{1,3}", attempt_value.strip()):
                    attempt_number = int(attempt_value.strip())
                else:
                    raise ProcessingError(f"Item {number}: attempt must be a positive integer or digit string.")
                if not 1 <= attempt_number <= 999:
                    raise ProcessingError(f"Item {number}: attempt must be between 1 and 999.")
                if not re.fullmatch(r"drawings/\d{4}-\d{2}-\d{2}/images", directory.relative_to(root).as_posix()):
                    raise ProcessingError(
                        f"Item {number}: attempt metadata is only valid for a drawings/YYYY-MM-DD/images destination."
                    )
                attempt_ref = f"{attempt_number:02d}"
            reject_symlink_components(directory, root)
            stem = f"{asset_id}-{slug}" if asset_id else slug
            # Normalize the content type for encoder selection but preserve the
            # uploaded extension's exact spelling in the permanent master path.
            original_suffix = source.suffix
            master, webp = directory / "original" / f"{stem}{original_suffix}", directory / f"{stem}.webp"
            for target in (master, webp):
                rel = target.relative_to(root).as_posix()
                if rel in targets:
                    raise ProcessingError(f"Multiple items resolve to the same destination: {rel}")
                targets.add(rel)
                reject_symlink_components(target.parent, root)
                if target.exists() or target.is_symlink():
                    raise ProcessingError(f"Destination already exists; refusing to overwrite: {rel}")
            expected_sha = item.get("expected_sha256", "")
            if expected_sha is None:
                expected_sha = ""
            if expected_sha != "" and (
                not isinstance(expected_sha, str) or not re.fullmatch(r"[a-fA-F0-9]{64}", expected_sha)
            ):
                raise ProcessingError(f"Item {number}: expected_sha256 must be a 64-character hexadecimal SHA-256.")
            output_id = item.get("output_id", "")
            prompt_id = item.get("prompt_id", "")
            native_generation_id = item.get("native_generation_id", "")
            native_output_id = item.get("native_output_id", "")
            output_id = "" if output_id is None else output_id
            prompt_id = "" if prompt_id is None else prompt_id
            native_generation_id = "" if native_generation_id is None else native_generation_id
            native_output_id = "" if native_output_id is None else native_output_id
            for field_name, field_value in (("output_id", output_id), ("prompt_id", prompt_id)):
                if field_value != "" and (
                    not isinstance(field_value, str)
                    or not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]{0,79}", field_value)
                ):
                    raise ProcessingError(f"Item {number}: {field_name} must be a safe identifier.")
            if output_id:
                if output_id in output_ids:
                    raise ProcessingError(f"Duplicate output_id in hand-off: {output_id}")
                output_ids.add(output_id)
            for field_name, field_value in (
                ("native_generation_id", native_generation_id),
                ("native_output_id", native_output_id),
            ):
                if field_value and (
                    not isinstance(field_value, str) or len(field_value) > 256
                    or any(character in field_value for character in "\r\n")
                ):
                    raise ProcessingError(f"Item {number}: {field_name} must be a single-line string of at most 256 characters.")
            approval_status = item.get("approval_status", "Not recorded")
            if not isinstance(approval_status, str) or approval_status not in {"Approved", "Rejected", "Pending", "Not recorded"}:
                raise ProcessingError(
                    f"Item {number}: approval_status must be Approved, Rejected, Pending, or Not recorded."
                )
            mapping_evidence = item.get("mapping_evidence", "")
            mapping_evidence = "" if mapping_evidence is None else mapping_evidence
            if mapping_evidence != "" and (
                not isinstance(mapping_evidence, str) or len(mapping_evidence) > 1000
                or any(character in mapping_evidence for character in "\r\n")
            ):
                raise ProcessingError(f"Item {number}: mapping_evidence must be a single-line string of at most 1000 characters.")
            source_sha = digest(source)
            hash_match = "MATCH" if expected_sha and source_sha.lower() == expected_sha.lower() else ("MISMATCH" if expected_sha else "NOT_PROVIDED")
            prepared.append({
                "name": name, "source": source, "title": title.strip(), "asset_id": asset_id,
                "attempt": attempt_ref, "expected_sha": expected_sha, "output_id": output_id, "prompt_id": prompt_id,
                "native_generation_id": native_generation_id, "native_output_id": native_output_id,
                "approval_status": approval_status, "mapping_evidence": mapping_evidence,
                "image_id": output_id or (f"A{attempt_ref}-O-{source_sha[:12]}" if attempt_ref else ""),
                "hash_match": hash_match,
                "directory": directory, "master": master, "webp": webp,
                "profile": "lossless-exact-q100-m6" if suffix == ".png" else "picture-q92-m6-sharp-yuv",
                "original_bytes": source.stat().st_size, "source_sha": source_sha, "staged": None,
            })
        if inbox_images != sources:
            missing, unlisted = sorted(sources - inbox_images), sorted(inbox_images - sources)
            details = (["missing: " + ", ".join(missing)] if missing else []) + (["not listed: " + ", ".join(unlisted)] if unlisted else [])
            raise ProcessingError("Every image must appear exactly once in HANDOFF.yml; " + "; ".join(details))
        checks.append("Every uploaded image is listed exactly once; no unlisted image will be processed.")
        if any(item["hash_match"] == "MATCH" for item in prepared):
            checks.append("Uploaded originals matching supplied generation-time SHA-256 values were identified.")
        if any(item["hash_match"] == "MISMATCH" for item in prepared):
            checks.append("WARNING: one or more uploaded originals differ from supplied generation-time SHA-256 values; retained and flagged for mapping review, not automatically rejected.")
        if any(item["hash_match"] == "NOT_PROVIDED" for item in prepared):
            checks.append("Generation-time SHA-256 matching was unavailable for items without expected_sha256.")
        checks.append("Destinations are restricted to approved images/, novel/, or dated drawings/ asset folders; duplicate and existing paths are rejected.")
        text_updates = prepare_attempt_readme_updates(prepared, root)
        if text_updates:
            checks.append("Attempt and daily README targets were prevalidated for automatic output linking.")

        if stage_root.exists() or stage_root.is_symlink():
            raise ProcessingError(f"WebP staging attempt already exists: {stage_root.relative_to(root).as_posix()}")
        stage_root.mkdir(parents=True, exist_ok=False)
        conversion_errors = []
        for item in prepared:
            source = item["source"]
            if source.suffix.lower() == ".png" and is_apng(source):
                msg = f"{source.name}: animated PNG (APNG) cannot be flattened."
                item["status"], item["error"] = "SKIPPED_ANIMATED_PNG", msg
                conversion_errors.append(msg)
                continue
            staged = stage_root / f"{source.name}.webp"
            item["stage_path"] = staged.relative_to(root).as_posix()
            if item["profile"] == "lossless-exact-q100-m6":
                cmd = ["cwebp", "-quiet", "-lossless", "-q", "100", "-m", "6", "-exact", "-metadata", "icc", str(source), "-o", str(staged)]
            else:
                cmd = ["cwebp", "-quiet", "-preset", "picture", "-q", "92", "-m", "6", "-sharp_yuv", "-metadata", "icc", str(source), "-o", str(staged)]
            result = subprocess.run(cmd, capture_output=True, text=True)
            if result.returncode or not valid_webp(staged):
                detail = (result.stderr or result.stdout).strip() or f"cwebp exit code {result.returncode}; invalid WebP output."
                staged.unlink(missing_ok=True)
                item["status"], item["error"] = "FAILED_CONVERSION", detail
                conversion_errors.append(f"{source.name}: {detail}")
                continue
            item["staged"] = staged
            item["webp_bytes"] = staged.stat().st_size
            item["webp_sha"] = digest(staged)
            item["size_change"] = f"{(item['original_bytes'] - item['webp_bytes']) / item['original_bytes'] * 100:.2f}"
            item["status"], item["error"] = "CONVERTED_STAGED", ""
        if conversion_errors:
            raise ProcessingError("Batch conversion failed; no files were relocated. " + " | ".join(conversion_errors))
        checks.append(f"Every WebP passed RIFF/WEBP signature and container-length validation in persistent staging: {stage_root.relative_to(root).as_posix()}/.")

        for item in prepared:
            item["master"].parent.mkdir(parents=True, exist_ok=True)
            os.replace(item["source"], item["master"])
            moved.append((item["master"], item["source"]))
            os.replace(item["staged"], item["webp"])
            staged_moves.append((item["webp"], item["staged"]))
            if digest(item["master"]) != item["source_sha"]:
                raise ProcessingError(f"Original master bytes changed during relocation: {item['master']}")
            if not valid_webp(item["webp"]) or digest(item["webp"]) != item["webp_sha"]:
                raise ProcessingError(f"Final WebP failed verification: {item['webp']}")
            item["master_sha"] = digest(item["master"])
            item["status"] = "RELOCATED_AND_VERIFIED"
        checks.append("Each original master was relocated byte-for-byte; SHA-256 matches its uploaded source.")
        checks.append("Each WebP was moved from persistent staging to its final destination and passed hash and container verification.")

        for text_path, updated_text in text_updates.items():
            previous_bytes = text_path.read_bytes() if text_path.exists() else None
            written_text_updates.append((text_path, previous_bytes))
            text_path.parent.mkdir(parents=True, exist_ok=True)
            text_path.write_text(updated_text, encoding="utf-8")
        manifest_updates = prepare_session_manifest_updates(prepared, root)
        for manifest_path, manifest_content in manifest_updates.items():
            text_updates[manifest_path] = manifest_content

        if text_updates:
            checks.append("Verified WebP-only links and session manifest records were prepared for commit.")

        rows = []
        for item in prepared:
            rows.append({
                "source_filename": item["name"], "source_path": f"images/takeout/{item['name']}",
                "title": item["title"], "asset_id": item["asset_id"], "attempt": item["attempt"],
                "destination_dir": item["directory"].relative_to(root).as_posix(),
                "image_id": item.get("image_id", ""),
                "master_path": item["master"].relative_to(root).as_posix(),
                "webp_path": item["webp"].relative_to(root).as_posix(),
                "manifest_path": (
                    f"drawings/{item['directory'].relative_to(root).parts[1]}/manifest.csv"
                    if item.get("attempt") else ""
                ),
                "staging_webp_path": item.get("stage_path", ""),
                "source_format": item["source"].suffix.lower().lstrip("."),
                "conversion_profile": item["profile"], "original_bytes": item["original_bytes"],
                "webp_bytes": item["webp_bytes"], "size_change_percent": item["size_change"],
                "source_sha256": item["source_sha"], "master_sha256": item["master_sha"],
                "webp_sha256": item["webp_sha"], "generation_sha256": item["expected_sha"],
                "output_id": item["output_id"], "prompt_id": item["prompt_id"],
                "native_generation_id": item["native_generation_id"], "native_output_id": item["native_output_id"],
                "mapping_status": (
                    "Verified" if item["hash_match"] == "MATCH"
                    else "Probable" if item["hash_match"] == "MISMATCH"
                    else "Corroborated" if item.get("attempt")
                    else "Unmapped"
                ),
                "hash_match": item["hash_match"],
                "cwebp_version": encoder_version,
                "status": item["status"], "error": "",
            })
        write_reports(folder, raw, rows, batch, "SUCCESS", checks, [], len(prepared))
        # All staged derivatives have moved to their final destinations. Remove
        # the now-empty attempt directory before clearing the active hand-off.
        stage_root.rmdir()
        try:
            stage_root.parent.rmdir()
        except OSError:
            pass  # Older failed attempts for the same batch may still be present.
        tmp_manifest = inbox / ".HANDOFF.yml.tmp"
        tmp_manifest.write_text(EMPTY_HANDOFF, encoding="utf-8")
        os.replace(tmp_manifest, manifest)
        print(f"Successfully processed {batch}: {len(prepared)} image(s).")
        print(f"Reports: {folder.relative_to(root).as_posix()}/")
        return 0

    except Exception as exc:
        message = str(exc) or exc.__class__.__name__
        errors.append(message)
        rollback_errors = []
        for text_path, original_bytes in reversed(written_text_updates):
            try:
                if original_bytes is None:
                    text_path.unlink(missing_ok=True)
                else:
                    text_path.write_bytes(original_bytes)
            except Exception as rollback_exc:
                rollback_errors.append(f"Could not restore text record {text_path}: {rollback_exc}")
        for master, source in reversed(moved):
            try:
                if master.exists() and not source.exists():
                    source.parent.mkdir(parents=True, exist_ok=True)
                    os.replace(master, source)
            except Exception as rollback_exc:
                rollback_errors.append(f"Could not restore {source.name}: {rollback_exc}")
        for webp, staged in reversed(staged_moves):
            try:
                if webp.exists() and not staged.exists():
                    staged.parent.mkdir(parents=True, exist_ok=True)
                    os.replace(webp, staged)
            except Exception as rollback_exc:
                rollback_errors.append(f"Could not restore staged WebP {staged}: {rollback_exc}")
        errors.extend(rollback_errors)
        checks.append("Batch was not marked successful; sources were restored to takeout and converted WebPs were retained in staging where rollback succeeded.")
        rows = []
        for item in prepared:
            rows.append({
                "source_filename": item["name"], "source_path": f"images/takeout/{item['name']}",
                "title": item["title"], "asset_id": item["asset_id"], "attempt": item["attempt"],
                "destination_dir": item["directory"].relative_to(root).as_posix(),
                "image_id": item.get("image_id", ""),
                "master_path": item["master"].relative_to(root).as_posix(),
                "webp_path": item["webp"].relative_to(root).as_posix(),
                "manifest_path": (
                    f"drawings/{item['directory'].relative_to(root).parts[1]}/manifest.csv"
                    if item.get("attempt") else ""
                ),
                "staging_webp_path": item.get("stage_path", ""),
                "source_format": item["source"].suffix.lower().lstrip("."),
                "conversion_profile": item["profile"], "original_bytes": item["original_bytes"],
                "webp_bytes": item.get("webp_bytes", ""), "size_change_percent": item.get("size_change", ""),
                "source_sha256": item["source_sha"], "master_sha256": "",
                "webp_sha256": item.get("webp_sha", ""), "generation_sha256": item.get("expected_sha", ""),
                "output_id": item.get("output_id", ""), "prompt_id": item.get("prompt_id", ""),
                "native_generation_id": item.get("native_generation_id", ""),
                "native_output_id": item.get("native_output_id", ""),
                "mapping_status": "NOT_ASSESSED",
                "hash_match": item.get("hash_match", "NOT_CHECKED"),
                "cwebp_version": encoder_version,
                "status": item.get("status", "FAILED"), "error": message,
            })
        if not rows:
            rows = failure_rows(items_report, message, encoder_version)
        try:
            write_reports(folder, raw, rows, batch, "FAILED", checks, errors, len(items_report))
        except Exception as report_exc:
            print(f"Could not write diagnostic history: {report_exc}", file=sys.stderr)
        print(f"Takeout batch {batch} failed: {message}", file=sys.stderr)
        return 1

if __name__ == "__main__":
    raise SystemExit(main())
