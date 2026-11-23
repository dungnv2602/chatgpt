#!/usr/bin/env python3
"""Check catalog classes and exact canonical references."""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ALLOWED_ROOTS = {
    "images", "master", "novels", "drawings", "skills", "workspace", "archive"
}
KNOWN_CLASSES = {
    "Embedded contract",
    "Generator-owned",
    "Lightweight pattern",
    "Schema required",
    "Exempt",
}


def split_row(line: str) -> list[str]:
    """Split one simple Markdown table row into cells."""
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def extract_paths(value: str) -> list[str]:
    """Return repository paths written as inline code."""
    paths = []
    for candidate in re.findall(r"`([^`]+)`", value):
        candidate = candidate.strip()
        if "/" in candidate and not candidate.startswith(("http://", "https://")):
            paths.append(candidate)
    return paths


def is_separator(cells: list[str]) -> bool:
    return bool(cells) and all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells)


def read_inventory(content: str) -> tuple[list[dict[str, str]], list[str]]:
    """Read the document-type table from the Initial inventory section."""
    errors: list[str] = []
    lines = content.splitlines()
    section = next(
        (index for index, line in enumerate(lines) if line.strip() == "## Initial inventory"),
        None,
    )
    if section is None:
        return [], ["Catalog has no '## Initial inventory' section."]

    header_index = next(
        (index for index in range(section + 1, len(lines))
         if lines[index].strip().startswith("|")),
        None,
    )
    if header_index is None:
        return [], ["Initial inventory has no Markdown table."]

    header = split_row(lines[header_index])
    expected = [
        "Document type", "Class", "Current canonical format",
        "Inventory finding / next action",
    ]
    if header != expected:
        errors.append("Initial inventory table has unexpected columns.")
        return [], errors

    rows: list[dict[str, str]] = []
    for line_number, line in enumerate(lines[header_index + 1:], start=header_index + 2):
        if not line.strip().startswith("|"):
            break
        cells = split_row(line)
        if is_separator(cells):
            continue
        if len(cells) != 4:
            errors.append(f"Line {line_number}: expected 4 table cells, found {len(cells)}.")
            continue
        rows.append({
            "type": cells[0],
            "class": cells[1],
            "canonical": cells[2],
            "finding": cells[3],
            "line": str(line_number),
            "full_row": line,
        })

    if not rows:
        errors.append("Initial inventory contains no document types.")
    return rows, errors


def validate_catalog(root: Path, catalog_path: Path) -> tuple[list[str], int, int]:
    """Validate catalog rows and their exact repository references."""
    errors: list[str] = []
    try:
        content = catalog_path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        return [f"Cannot read catalog: {exc}"], 0, 0

    rows, parse_errors = read_inventory(content)
    errors.extend(parse_errors)
    seen_types: set[str] = set()
    reference_count = 0

    for row in rows:
        line = row["line"]
        document_type = row["type"]
        class_name = row["class"]
        if not document_type:
            errors.append(f"Line {line}: document type is empty.")
        normalized_type = document_type.casefold()
        if normalized_type in seen_types:
            errors.append(f"Line {line}: duplicate document type '{document_type}'.")
        seen_types.add(normalized_type)

        is_template = class_name == "Template required" or class_name.startswith(
            "Template required "
        )
        if not is_template and class_name not in KNOWN_CLASSES:
            errors.append(f"Line {line}: unknown document class '{class_name}'.")

        canonical_paths = extract_paths(row["canonical"])
        row_paths = extract_paths(row["full_row"])
        if not canonical_paths:
            errors.append(f"Line {line}: canonical format has no exact path reference.")

        for path_text in dict.fromkeys(row_paths):
            reference_count += 1
            path = Path(path_text)
            if (
                path.is_absolute()
                or ".." in path.parts
                or not path.parts
                or path.parts[0] not in ALLOWED_ROOTS
                or path_text.strip() != path_text
            ):
                errors.append(f"Line {line}: unsafe or out-of-scope path '{path_text}'.")
                continue
            target = root / path
            if not target.is_file() and not target.is_dir():
                errors.append(f"Line {line}: referenced path does not exist: {path_text}.")

        if is_template:
            if not any(
                "/templates/" in f"/{path.lower()}"
                or "template" in Path(path).name.lower()
                for path in canonical_paths
            ):
                errors.append(
                    f"Line {line}: Template required class must point to a named template."
                )
        elif class_name == "Embedded contract":
            if len(canonical_paths) < 2:
                errors.append(
                    f"Line {line}: Embedded contract must name its owner and live record."
                )
        elif class_name in {"Schema required", "Generator-owned"}:
            if not any(path.endswith(".py") for path in canonical_paths):
                errors.append(f"Line {line}: {class_name} must reference its Python authority.")
            test_paths = [
                path for path in row_paths
                if Path(path).name.startswith("test_") and path.endswith(".py")
            ]
            if not test_paths:
                errors.append(f"Line {line}: {class_name} must reference a regression test.")

    return errors, len(rows), reference_count


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate the Document Type Catalog.")
    parser.add_argument("--root", default=".", help="Repository root directory.")
    parser.add_argument(
        "--catalog",
        default="skills/document-standards/references/document-type-catalog.md",
        help="Catalog path relative to the repository root.",
    )
    args = parser.parse_args()

    root = Path(args.root).resolve()
    catalog_path = root / args.catalog
    errors, row_count, reference_count = validate_catalog(root, catalog_path)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        print(
            f"Catalog validation failed: {len(errors)} error(s), "
            f"{row_count} document type(s), {reference_count} reference(s).",
            file=sys.stderr,
        )
        return 1

    print(
        f"Catalog validation passed: {row_count} document type(s), "
        f"{reference_count} exact reference(s)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
