#!/usr/bin/env python3
"""Process one images/takeout hand-off as a verified, rollback-capable batch."""
from __future__ import annotations
import argparse, csv, hashlib, os, re, shutil, subprocess, sys, unicodedata
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath
from typing import Any
import yaml

SUPPORTED = {".png", ".jpg", ".jpeg"}
KNOWN_IMAGE = SUPPORTED | {".apng", ".gif", ".webp", ".bmp", ".tif", ".tiff", ".heic", ".heif", ".avif"}
HANDOFF = "HANDOFF.yml"
EMPTY_HANDOFF = "version: 1\nstatus: empty\nitems: []\n"
FIELDS = [
    "source_filename", "source_path", "title", "asset_id", "attempt", "destination_dir",
    "master_path", "webp_path", "staging_webp_path", "source_format", "conversion_profile",
    "original_bytes", "webp_bytes", "size_change_percent", "source_sha256",
    "master_sha256", "webp_sha256", "cwebp_version", "status", "error",
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
    if parts[0] not in {"images", "novel"}:
        raise ProcessingError("Destinations must be inside images/ or novel/.")
    if parts[0] == "images" and len(parts) > 1 and parts[1] in {"takeout", "webp", "scripts"}:
        raise ProcessingError(f"Reserved image destination: {value!r}")
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
            "destination_dir": item.get("destination_dir", ""), "master_path": "", "webp_path": "",
            "source_format": Path(str(source)).suffix.lower().lstrip("."),
            "conversion_profile": "", "original_bytes": "", "webp_bytes": "",
            "size_change_percent": "", "source_sha256": "", "master_sha256": "",
            "webp_sha256": "", "cwebp_version": version, "status": "FAILED", "error": error,
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
            existing = re.findall(r"\[[^\]]+\]\((images/[^)]+)\)", section)
            additions = [link for link in links if link not in existing]
            if additions:
                section += "\n" + "\n".join(
                    f"- [{Path(link).name}]({link})" for link in additions
                )
                attempt_content = (
                    attempt_content[:section_match.start()]
                    + section
                    + "\n\n"
                    + attempt_content[section_match.end():].lstrip("\n")
                )
        else:
            link_lines = "\n".join(f"- [{Path(link).name}]({link})" for link in links)
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
        existing_links = re.findall(r"\[[^\]]+\]\((images/[^)]+)\)", cells[5])
        merged_links = list(dict.fromkeys(existing_links + links))
        cells[5] = ", ".join(
            f"[{Path(link).name}]({link})" for link in merged_links
        )
        lines[row_index] = "| " + " | ".join(cells) + " |"
        updates[readme_path] = "\n".join(lines) + ("\n" if readme_content.endswith("\n") else "")

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
        data = {}
    if data.get("status") != "ready":
        print(f"Hand-off status is {data.get('status')!r}; no-op. Uploaded files remain untouched.")
        return 0
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
    written_text_updates: list[tuple[Path, bytes]] = []
    stage_root = inbox / "webp" / batch / folder.name
    encoder_version = ""

    try:
        if data.get("version") != 1:
            raise ProcessingError("HANDOFF.yml version must be 1.")
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
            asset_id = item.get("asset_id") or ""
            if asset_id:
                if not isinstance(asset_id, str) or not re.fullmatch(r"[A-Z][A-Z0-9-]{0,31}", asset_id):
                    raise ProcessingError(f"Invalid asset_id {asset_id!r}; use uppercase letters, numbers and hyphens, e.g. ILL-001.")
                if asset_id in ids:
                    raise ProcessingError(f"Duplicate asset_id: {asset_id}")
                ids.add(asset_id)
            directory = destination_dir(item.get("destination_dir"), root)
            attempt_value = item.get("attempt")
            attempt_ref = ""
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
            master, webp = directory / f"{stem}{original_suffix}", directory / f"{stem}.webp"
            for target in (master, webp):
                rel = target.relative_to(root).as_posix()
                if rel in targets:
                    raise ProcessingError(f"Multiple items resolve to the same destination: {rel}")
                targets.add(rel)
                reject_symlink_components(target.parent, root)
                if target.exists() or target.is_symlink():
                    raise ProcessingError(f"Destination already exists; refusing to overwrite: {rel}")
            prepared.append({
                "name": name, "source": source, "title": title.strip(), "asset_id": asset_id,
                "attempt": attempt_ref,
                "directory": directory, "master": master, "webp": webp,
                "profile": "lossless-exact-q100-m6" if suffix == ".png" else "picture-q92-m6-sharp-yuv",
                "original_bytes": source.stat().st_size, "source_sha": digest(source), "staged": None,
            })
        if inbox_images != sources:
            missing, unlisted = sorted(sources - inbox_images), sorted(inbox_images - sources)
            details = (["missing: " + ", ".join(missing)] if missing else []) + (["not listed: " + ", ".join(unlisted)] if unlisted else [])
            raise ProcessingError("Every image must appear exactly once in HANDOFF.yml; " + "; ".join(details))
        checks.append("Every uploaded image is listed exactly once; no unlisted image will be processed.")
        checks.append("Destinations are restricted to images/ or novel/; duplicate and existing paths are rejected.")
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
            previous_bytes = text_path.read_bytes()
            text_path.write_text(updated_text, encoding="utf-8")
            written_text_updates.append((text_path, previous_bytes))
        if written_text_updates:
            checks.append("Verified output links were added to the matching attempt records and daily README rows.")

        rows = []
        for item in prepared:
            rows.append({
                "source_filename": item["name"], "source_path": f"images/takeout/{item['name']}",
                "title": item["title"], "asset_id": item["asset_id"], "attempt": item["attempt"],
                "destination_dir": item["directory"].relative_to(root).as_posix(),
                "master_path": item["master"].relative_to(root).as_posix(),
                "webp_path": item["webp"].relative_to(root).as_posix(),
                "staging_webp_path": item.get("stage_path", ""),
                "source_format": item["source"].suffix.lower().lstrip("."),
                "conversion_profile": item["profile"], "original_bytes": item["original_bytes"],
                "webp_bytes": item["webp_bytes"], "size_change_percent": item["size_change"],
                "source_sha256": item["source_sha"], "master_sha256": item["master_sha"],
                "webp_sha256": item["webp_sha"], "cwebp_version": encoder_version,
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
                text_path.write_bytes(original_bytes)
            except Exception as rollback_exc:
                rollback_errors.append(f"Could not restore Markdown record {text_path}: {rollback_exc}")
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
                "master_path": item["master"].relative_to(root).as_posix(),
                "webp_path": item["webp"].relative_to(root).as_posix(),
                "staging_webp_path": item.get("stage_path", ""),
                "source_format": item["source"].suffix.lower().lstrip("."),
                "conversion_profile": item["profile"], "original_bytes": item["original_bytes"],
                "webp_bytes": item.get("webp_bytes", ""), "size_change_percent": item.get("size_change", ""),
                "source_sha256": item["source_sha"], "master_sha256": "",
                "webp_sha256": item.get("webp_sha", ""), "cwebp_version": encoder_version,
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
