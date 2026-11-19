#!/usr/bin/env python3
"""Process one images/takeout hand-off as a verified, rollback-capable batch."""
from __future__ import annotations
import argparse, csv, hashlib, os, re, shutil, subprocess, sys, tempfile, unicodedata
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath
from typing import Any
import yaml

SUPPORTED = {".png", ".jpg", ".jpeg"}
KNOWN_IMAGE = SUPPORTED | {".apng", ".gif", ".webp", ".bmp", ".tif", ".tiff", ".heic", ".heif", ".avif"}
HANDOFF = "HANDOFF.yml"
EMPTY_HANDOFF = "version: 1\nstatus: empty\nitems: []\n"
FIELDS = [
    "source_filename", "source_path", "title", "asset_id", "destination_dir",
    "master_path", "webp_path", "source_format", "conversion_profile",
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

def attempt_folder(history: Path, batch: str) -> Path:
    if history.is_symlink():
        raise ProcessingError("images/takeout/history must not be a symlink.")
    history.mkdir(parents=True, exist_ok=True)
    batch_root = history / batch
    if batch_root.is_symlink():
        raise ProcessingError(f"Batch history path must not be a symlink: {batch}")
    batch_root.mkdir(parents=True, exist_ok=True)
    n = 1
    while (batch_root / f"attempt-{n:03d}").exists():
        n += 1
    return batch_root / f"attempt-{n:03d}"

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
            "destination_dir": item.get("destination_dir", ""), "master_path": "", "webp_path": "",
            "source_format": Path(str(source)).suffix.lower().lstrip("."),
            "conversion_profile": "", "original_bytes": "", "webp_bytes": "",
            "size_change_percent": "", "source_sha256": "", "master_sha256": "",
            "webp_sha256": "", "cwebp_version": version, "status": "FAILED", "error": error,
        })
    return rows

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

    folder = attempt_folder(inbox / "history", batch)
    raw_items = data.get("items")
    items_report = raw_items if isinstance(raw_items, list) else []
    errors: list[str] = []
    checks: list[str] = []
    prepared: list[dict[str, Any]] = []
    moved: list[tuple[Path, Path]] = []
    created_webps: list[Path] = []
    temp: tempfile.TemporaryDirectory[str] | None = None
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
            if child.name == "history":
                if child.is_symlink() or not child.is_dir():
                    raise ProcessingError("images/takeout/history must be a normal directory.")
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
        checks.append("Inbox is flat and contains only PNG/JPG/JPEG files, HANDOFF.yml and history/.")

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

        temp = tempfile.TemporaryDirectory(prefix="takeout-webp-")
        stage_root = Path(temp.name)
        conversion_errors = []
        for idx, item in enumerate(prepared, start=1):
            source = item["source"]
            if source.suffix.lower() == ".png" and is_apng(source):
                msg = f"{source.name}: animated PNG (APNG) cannot be flattened."
                item["status"], item["error"] = "SKIPPED_ANIMATED_PNG", msg
                conversion_errors.append(msg)
                continue
            staged = stage_root / f"{idx:04d}.webp"
            if item["profile"] == "lossless-exact-q100-m6":
                cmd = ["cwebp", "-quiet", "-lossless", "-q", "100", "-m", "6", "-exact", "-metadata", "icc", str(source), "-o", str(staged)]
            else:
                cmd = ["cwebp", "-quiet", "-preset", "picture", "-q", "92", "-m", "6", "-sharp_yuv", "-metadata", "icc", str(source), "-o", str(staged)]
            result = subprocess.run(cmd, capture_output=True, text=True)
            if result.returncode or not valid_webp(staged):
                detail = (result.stderr or result.stdout).strip() or f"cwebp exit code {result.returncode}; invalid WebP output."
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
        checks.append("Every WebP passed RIFF/WEBP signature and container-length validation in temporary staging.")

        for item in prepared:
            item["master"].parent.mkdir(parents=True, exist_ok=True)
            os.replace(item["source"], item["master"])
            moved.append((item["master"], item["source"]))
            shutil.copyfile(item["staged"], item["webp"])
            created_webps.append(item["webp"])
            if digest(item["master"]) != item["source_sha"]:
                raise ProcessingError(f"Original master bytes changed during relocation: {item['master']}")
            if not valid_webp(item["webp"]) or digest(item["webp"]) != item["webp_sha"]:
                raise ProcessingError(f"Final WebP failed verification: {item['webp']}")
            item["master_sha"] = digest(item["master"])
            item["status"] = "RELOCATED_AND_VERIFIED"
        checks.append("Each original master was relocated byte-for-byte; SHA-256 matches its uploaded source.")
        checks.append("Each final WebP matches the staged output and is valid at its destination.")

        rows = []
        for item in prepared:
            rows.append({
                "source_filename": item["name"], "source_path": f"images/takeout/{item['name']}",
                "title": item["title"], "asset_id": item["asset_id"],
                "destination_dir": item["directory"].relative_to(root).as_posix(),
                "master_path": item["master"].relative_to(root).as_posix(),
                "webp_path": item["webp"].relative_to(root).as_posix(),
                "source_format": item["source"].suffix.lower().lstrip("."),
                "conversion_profile": item["profile"], "original_bytes": item["original_bytes"],
                "webp_bytes": item["webp_bytes"], "size_change_percent": item["size_change"],
                "source_sha256": item["source_sha"], "master_sha256": item["master_sha"],
                "webp_sha256": item["webp_sha"], "cwebp_version": encoder_version,
                "status": item["status"], "error": "",
            })
        write_reports(folder, raw, rows, batch, "SUCCESS", checks, [], len(prepared))
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
        for master, source in reversed(moved):
            try:
                if master.exists() and not source.exists():
                    source.parent.mkdir(parents=True, exist_ok=True)
                    os.replace(master, source)
            except Exception as rollback_exc:
                rollback_errors.append(f"Could not restore {source.name}: {rollback_exc}")
        for webp in reversed(created_webps):
            try:
                webp.unlink(missing_ok=True)
            except Exception as rollback_exc:
                rollback_errors.append(f"Could not remove incomplete WebP {webp}: {rollback_exc}")
        errors.extend(rollback_errors)
        checks.append("Batch was not marked successful; sources were restored to takeout where rollback succeeded.")
        if temp is not None:
            temp.cleanup()
        rows = []
        for item in prepared:
            rows.append({
                "source_filename": item["name"], "source_path": f"images/takeout/{item['name']}",
                "title": item["title"], "asset_id": item["asset_id"],
                "destination_dir": item["directory"].relative_to(root).as_posix(),
                "master_path": item["master"].relative_to(root).as_posix(),
                "webp_path": item["webp"].relative_to(root).as_posix(),
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
    finally:
        if temp is not None:
            temp.cleanup()

if __name__ == "__main__":
    raise SystemExit(main())
