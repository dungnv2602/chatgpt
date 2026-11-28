#!/usr/bin/env python3
"""Check catalog classes, path coverage, canonical owners, and placement."""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ALLOWED_ROOTS = {".agent", ".github", ".takeout", "area", "archive", "images", "workspace", "master"}
NON_MARKDOWN_ARTIFACT_TYPES = {
    "Agent metadata",
    "Binary reference asset",
    "JSON data",
    "JSON schema",
    "License text",
    "Python script",
    "Shell script",
    "Static HTML asset",
    "Vendored XML schema",
    "Worker policy and schema",
    "GitHub Actions workflow",
}
NON_MARKDOWN_SUFFIXES = {
    "Agent metadata": {".yaml", ".yml"},
    "Binary reference asset": {".pdf"},
    "JSON data": {".json"},
    "JSON schema": {".json"},
    "License text": {""},
    "Python script": {".py"},
    "Shell script": {".sh"},
    "Static HTML asset": {".html"},
    "Vendored XML schema": {".xsd"},
    "Worker policy and schema": {".json"},
    "GitHub Actions workflow": {".yml", ".yaml"},
}
NON_MARKDOWN_PLACEMENT_RULES = {
    "skill-assets",
    "skill-scripts",
    "skill-agents",
    "skill-root",
    "skill-eval-viewer",
    "skill-vendored-schemas",
    "github-workflows",
    "workspace-task-validation",
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


def read_coverage(content: str) -> tuple[list[dict[str, str]], list[str]]:
    """Read the path-pattern coverage table for in-scope Markdown documents."""
    errors: list[str] = []
    lines = content.splitlines()
    section = next(
        (index for index, line in enumerate(lines)
         if line.strip() == "## Markdown inventory coverage"),
        None,
    )
    if section is None:
        return [], ["Catalog has no '## Markdown inventory coverage' section."]

    header_index = next(
        (index for index in range(section + 1, len(lines))
         if lines[index].strip().startswith("|")),
        None,
    )
    if header_index is None:
        return [], ["Markdown inventory coverage has no table."]

    expected = ["Path pattern", "Class", "Coverage status", "Canonical authority", "Coverage rationale"]
    if split_row(lines[header_index]) != expected:
        return [], ["Markdown inventory coverage table has unexpected columns."]

    rows: list[dict[str, str]] = []
    for line_number, line in enumerate(lines[header_index + 1:], start=header_index + 2):
        if not line.strip().startswith("|"):
            break
        cells = split_row(line)
        if is_separator(cells):
            continue
        if len(cells) != 5:
            errors.append(
                f"Line {line_number}: expected 5 Markdown coverage cells, found {len(cells)}."
            )
            continue
        patterns = re.findall(r"`([^`]+)`", cells[0])
        if len(patterns) != 1:
            errors.append(
                f"Line {line_number}: path pattern must contain exactly one inline-code glob."
            )
            continue
        rows.append({
            "pattern": patterns[0],
            "class": cells[1],
            "status": cells[2],
            "canonical": cells[3],
            "rationale": cells[4],
            "line": str(line_number),
        })

    if not rows:
        errors.append("Markdown inventory coverage contains no path rules.")
    return rows, errors


def find_markdown_documents(root: Path) -> list[str]:
    """List repository Markdown files, excluding root master/, workspace/archive/, and .git/."""
    documents: list[str] = []
    for candidate in root.iterdir():
        if candidate.name in {"master", ".git"}:
            continue
        if candidate.is_dir():
            documents.extend(
                path.relative_to(root).as_posix()
                for path in candidate.rglob("*.md")
                if path.is_file() and path.relative_to(root).parts[:2] != ("workspace", "archive")
            )
        elif candidate.is_file() and candidate.suffix.casefold() == ".md":
            documents.append(candidate.relative_to(root).as_posix())
    return sorted(set(documents))


def compile_path_pattern(pattern: str) -> re.Pattern[str]:
    """Compile a repository-relative glob where * stays within one path segment."""
    pieces: list[str] = []
    index = 0
    while index < len(pattern):
        if pattern[index:index + 2] == "**":
            pieces.append(".*")
            index += 2
        elif pattern[index] == "*":
            pieces.append("[^/]*")
            index += 1
        elif pattern[index] == "?":
            pieces.append("[^/]")
            index += 1
        else:
            pieces.append(re.escape(pattern[index]))
            index += 1
    return re.compile("^" + "".join(pieces) + "$")


def validate_markdown_coverage(root: Path, content: str) -> list[str]:
    """Require every in-scope Markdown path to match a catalogued family rule."""
    errors: list[str] = []
    rows, parse_errors = read_coverage(content)
    errors.extend(parse_errors)
    if parse_errors or not rows:
        return errors

    documents = find_markdown_documents(root)
    seen_patterns: set[str] = set()
    compiled: list[tuple[re.Pattern[str], str]] = []

    for row in rows:
        line = row["line"]
        pattern = row["pattern"]
        class_name = row["class"]
        coverage_status = row["status"]
        if coverage_status not in {"Active", "Reserved", "Optional"}:
            errors.append(
                f"Line {line}: unknown Markdown coverage status '{coverage_status}'. "
                "Use Active, Reserved, or Optional."
            )
        if pattern in seen_patterns:
            errors.append(f"Line {line}: duplicate Markdown coverage pattern '{pattern}'.")
        seen_patterns.add(pattern)

        parts = pattern.split("/")
        if (
            pattern.startswith("/")
            or any(part in {"", ".", ".."} for part in parts)
            or parts[0] not in ALLOWED_ROOTS
            or parts[0] == "master"
            or parts[:2] == ["workspace", "archive"]
        ):
            errors.append(f"Line {line}: unsafe or excluded Markdown coverage pattern '{pattern}'.")
            continue

        is_template = class_name == "Template required" or class_name.startswith(
            "Template required "
        )
        if not is_template and class_name not in KNOWN_CLASSES:
            errors.append(f"Line {line}: unknown Markdown coverage class '{class_name}'.")
        if coverage_status == "Optional" and class_name != "Generator-owned":
            errors.append(
                f"Line {line}: Optional Markdown coverage is limited to Generator-owned outputs."
            )

        canonical_paths = extract_paths(row["canonical"])
        if not canonical_paths:
            errors.append(f"Line {line}: Markdown coverage rule has no canonical authority path.")

        for path_text in dict.fromkeys(canonical_paths):
            path = Path(path_text)
            raw_parts = path_text.split("/")
            if (
                path.is_absolute()
                or any(part in {"", ".", ".."} for part in raw_parts)
                or not path.parts
                or path.parts[0] not in ALLOWED_ROOTS
                or path.parts[0] == "master"
                or path.parts[:2] == ("workspace", "archive")
                or path_text.strip() != path_text
            ):
                errors.append(f"Line {line}: unsafe or excluded authority path '{path_text}'.")
                continue
            if not (root / path).is_file():
                errors.append(f"Line {line}: Markdown coverage authority does not exist: {path_text}.")

        if is_template:
            template_paths = [
                path for path in canonical_paths if is_template_asset(path)
            ]
            if not template_paths:
                errors.append(
                    f"Line {line}: Template required coverage must point to a named template."
                )
            for template_path in template_paths:
                location_error = template_location_error(template_path)
                if location_error:
                    errors.append(
                        f"Line {line}: invalid coverage template location for "
                        f"'{template_path}': {location_error}."
                    )
        elif class_name == "Embedded contract" and len(canonical_paths) < 2:
            errors.append(
                f"Line {line}: Embedded contract coverage must name its owner and live record."
            )
        elif class_name in {"Schema required", "Generator-owned"}:
            if not any(path.endswith(".py") for path in canonical_paths):
                errors.append(
                    f"Line {line}: {class_name} coverage must reference its Python authority."
                )
            if not any(
                Path(path).name.startswith("test_") and path.endswith(".py")
                for path in canonical_paths
            ):
                errors.append(
                    f"Line {line}: {class_name} coverage must reference a regression test."
                )

        path_regex = compile_path_pattern(pattern)
        matches = [path for path in documents if path_regex.fullmatch(path)]
        if coverage_status == "Active" and not matches:
            errors.append(
                f"Line {line}: Markdown coverage pattern matches no in-scope document: '{pattern}'."
            )
        elif coverage_status == "Reserved" and matches:
            errors.append(
                f"Line {line}: Reserved Markdown coverage pattern already matches "
                f"{len(matches)} in-scope document(s): '{pattern}'. Change it to Active."
            )
        # Optional generator-owned outputs may be empty; any present files remain covered.
        compiled.append((path_regex, class_name))

    uncovered = [
        path for path in documents
        if not any(path_regex.fullmatch(path) for path_regex, _ in compiled)
    ]
    if uncovered:
        preview = ", ".join(uncovered[:20])
        remainder = len(uncovered) - 20
        suffix = f" (and {remainder} more)" if remainder > 0 else ""
        errors.append(
            f"{len(uncovered)} Markdown file(s) are not covered by the catalog: "
            f"{preview}{suffix}."
        )
    return errors


def read_non_markdown_coverage(content: str) -> tuple[list[dict[str, str]], list[str]]:
    """Read the explicit path and placement rules for governed non-Markdown files."""
    errors: list[str] = []
    lines = content.splitlines()
    section = next(
        (index for index, line in enumerate(lines)
         if line.strip() == "## Governed non-Markdown artifact coverage"),
        None,
    )
    if section is None:
        return [], ["Catalog has no '## Governed non-Markdown artifact coverage' section."]

    section_end = next(
        (index for index in range(section + 1, len(lines))
         if lines[index].startswith("## ")),
        len(lines),
    )
    header_index = next(
        (index for index in range(section + 1, section_end)
         if lines[index].strip().startswith("|")),
        None,
    )
    if header_index is None:
        return [], ["Governed non-Markdown coverage has no table."]

    expected = [
        "Path pattern", "Artifact type", "Coverage status",
        "Canonical owner", "Placement rule", "Coverage rationale",
    ]
    if split_row(lines[header_index]) != expected:
        return [], ["Governed non-Markdown coverage table has unexpected columns."]

    rows: list[dict[str, str]] = []
    for line_number, line in enumerate(lines[header_index + 1:section_end], start=header_index + 2):
        if not line.strip().startswith("|"):
            continue
        cells = split_row(line)
        if is_separator(cells) or cells == expected:
            continue
        if len(cells) != 6:
            errors.append(
                f"Line {line_number}: expected 6 non-Markdown coverage cells, found {len(cells)}."
            )
            continue
        patterns = re.findall(r"`([^`]+)`", cells[0])
        if len(patterns) != 1:
            errors.append(
                f"Line {line_number}: path pattern must contain exactly one inline-code glob."
            )
            continue
        rows.append({
            "pattern": patterns[0],
            "type": cells[1],
            "status": cells[2],
            "owner": cells[3],
            "placement": cells[4],
            "rationale": cells[5],
            "line": str(line_number),
        })

    if not rows:
        errors.append("Governed non-Markdown coverage contains no path rules.")
    return rows, errors


def find_non_markdown_documents(root: Path) -> list[str]:
    """List governed non-Markdown files in skill, GitHub, and workspace trees."""
    documents: list[str] = []
    for relative_root in (".agent/skills", ".github", "workspace"):
        scan_root = root / relative_root
        if not scan_root.is_dir():
            continue
        documents.extend(
            path.relative_to(root).as_posix()
            for path in scan_root.rglob("*")
            if (
                path.is_file()
                and path.suffix.casefold() != ".md"
                and path.relative_to(root).parts[:2] != ("workspace", "archive")
            )
        )
    return sorted(set(documents))


def non_markdown_placement_error(path_text: str, placement: str) -> str | None:
    """Check whether an artifact uses its registered canonical directory."""
    parts = Path(path_text).parts
    skill_path = len(parts) >= 4 and parts[:2] == (".agent", "skills")
    if placement == "skill-assets":
        valid = skill_path and len(parts) >= 5 and parts[3] == "assets"
    elif placement == "skill-scripts":
        valid = skill_path and len(parts) >= 5 and parts[3] == "scripts"
    elif placement == "skill-agents":
        valid = skill_path and len(parts) >= 5 and parts[3] == "agents"
    elif placement == "skill-root":
        valid = skill_path and len(parts) == 4
    elif placement == "skill-eval-viewer":
        valid = parts[:4] == (".agent", "skills", "skill-creator", "eval-viewer") and len(parts) >= 5
    elif placement == "skill-vendored-schemas":
        valid = (
            parts[:6] == (
                ".agent", "skills", "xlsx", "scripts", "office", "schemas"
            )
            and len(parts) >= 7
        )
    elif placement == "github-workflows":
        valid = parts[:2] == (".github", "workflows") and len(parts) >= 3
    elif placement == "workspace-task-validation":
        valid = parts[:2] == ("workspace", "task-validation") and len(parts) >= 3
    else:
        valid = False
    return None if valid else f"artifact is not in its registered '{placement}' location"


def non_markdown_type_error(path_text: str, artifact_type: str) -> str | None:
    """Check whether a file suffix matches its registered artifact type."""
    path = Path(path_text)
    allowed_suffixes = NON_MARKDOWN_SUFFIXES.get(artifact_type)
    if allowed_suffixes is None:
        return f"unknown artifact type '{artifact_type}'"
    if artifact_type == "License text":
        valid = path.name.casefold().startswith("license")
    else:
        valid = path.suffix.casefold() in allowed_suffixes
    return None if valid else f"file type does not match '{artifact_type}'"


def validate_non_markdown_coverage(root: Path, content: str) -> list[str]:
    """Require every governed non-Markdown file to match one owner and placement rule."""
    errors: list[str] = []
    rows, parse_errors = read_non_markdown_coverage(content)
    errors.extend(parse_errors)
    if parse_errors or not rows:
        return errors

    documents = find_non_markdown_documents(root)
    seen_patterns: set[str] = set()
    matched_paths: dict[str, str] = {}

    for row in rows:
        line = row["line"]
        pattern = row["pattern"]
        artifact_type = row["type"]
        status = row["status"]
        placement = row["placement"]
        if status not in {"Active", "Reserved"}:
            errors.append(
                f"Line {line}: unknown non-Markdown coverage status '{status}'. "
                "Use Active or Reserved."
            )
        if pattern in seen_patterns:
            errors.append(f"Line {line}: duplicate non-Markdown coverage pattern '{pattern}'.")
        seen_patterns.add(pattern)

        parts = pattern.split("/")
        if (
            pattern.startswith("/")
            or any(part in {"", ".", ".."} for part in parts)
            or not (
                (parts[:2] == [".agent", "skills"] and len(parts) >= 3)
                or (parts[0] == ".github" and len(parts) >= 2)
                or (parts[0] == "workspace" and parts[:2] != ["workspace", "archive"])
            )
        ):
            errors.append(
                f"Line {line}: unsafe or out-of-scope non-Markdown pattern '{pattern}'."
            )
            continue
        if artifact_type not in NON_MARKDOWN_ARTIFACT_TYPES:
            errors.append(
                f"Line {line}: unknown non-Markdown artifact type '{artifact_type}'."
            )
        if placement not in NON_MARKDOWN_PLACEMENT_RULES:
            errors.append(
                f"Line {line}: unknown non-Markdown placement rule '{placement}'."
            )

        owner_text = row["owner"]
        external_owner = owner_text.startswith("external:")
        owner_pattern: str | None = None
        owner_regex: re.Pattern[str] | None = None
        if external_owner:
            if placement != "github-workflows" or artifact_type != "GitHub Actions workflow":
                errors.append(
                    f"Line {line}: external ownership is only valid for GitHub workflow definitions."
                )
        else:
            owner_paths = extract_paths(owner_text)
            if len(owner_paths) != 1:
                errors.append(
                    f"Line {line}: canonical owner must contain exactly one skill SKILL.md path."
                )
            else:
                owner_pattern = owner_paths[0]
                owner_parts = owner_pattern.split("/")
                if (
                    owner_pattern.startswith("/")
                    or any(part in {"", ".", ".."} for part in owner_parts)
                    or owner_parts[:2] != [".agent", "skills"]
                    or owner_parts[-1] != "SKILL.md"
                ):
                    errors.append(
                        f"Line {line}: canonical owner must be a safe owning-skill SKILL.md path."
                    )
                else:
                    owner_regex = compile_path_pattern(owner_pattern)

        path_regex = compile_path_pattern(pattern)
        matches = [document for document in documents if path_regex.fullmatch(document)]
        if status == "Active" and not matches:
            errors.append(
                f"Line {line}: Active non-Markdown pattern matches no file: '{pattern}'."
            )
        elif status == "Reserved" and matches:
            errors.append(
                f"Line {line}: Reserved non-Markdown pattern already matches "
                f"{len(matches)} file(s): '{pattern}'. Change it to Active."
            )

        for document in matches:
            previous = matched_paths.get(document)
            if previous is not None:
                errors.append(
                    f"Line {line}: duplicate canonical ownership for '{document}' "
                    f"from '{previous}' and '{pattern}'."
                )
            else:
                matched_paths[document] = pattern

            location_error = non_markdown_placement_error(document, placement)
            if location_error:
                errors.append(
                    f"Line {line}: invalid placement for '{document}': {location_error}."
                )
            type_error = non_markdown_type_error(document, artifact_type)
            if type_error:
                errors.append(
                    f"Line {line}: invalid artifact type for '{document}': {type_error}."
                )

            document_parts = Path(document).parts
            if document_parts[:2] == (".agent", "skills"):
                expected_owner = (
                    f".agent/skills/{document_parts[2]}/SKILL.md"
                    if len(document_parts) >= 4 else ""
                )
                if owner_regex is None or not owner_regex.fullmatch(expected_owner):
                    errors.append(
                        f"Line {line}: canonical owner does not match the owning skill "
                        f"for '{document}'."
                    )
                elif not (root / expected_owner).is_file():
                    errors.append(
                        f"Line {line}: canonical owner does not exist: '{expected_owner}'."
                    )
                if external_owner:
                    errors.append(
                        f"Line {line}: skill-owned artifact cannot use an external owner."
                    )
            elif document_parts[:2] == (".github", "workflows"):
                if not external_owner or placement != "github-workflows":
                    errors.append(
                        f"Line {line}: GitHub workflow definitions must use the external workflow owner."
                    )
            else:
                errors.append(
                    f"Line {line}: governed non-Markdown artifact is outside supported roots: '{document}'."
                )


    uncovered = [document for document in documents if document not in matched_paths]
    if uncovered:
        preview = ", ".join(uncovered[:20])
        remainder = len(uncovered) - 20
        suffix = f" (and {remainder} more)" if remainder > 0 else ""
        errors.append(
            f"{len(uncovered)} non-Markdown file(s) are not covered by the catalog: "
            f"{preview}{suffix}."
        )
    return errors


def is_template_asset(path_text: str) -> bool:
    """Return whether a path identifies a reusable template asset."""
    path = Path(path_text)
    return (
        "template" in path.name.casefold()
        or any(part.casefold() in {"template", "templates"} for part in path.parts)
    )


def template_location_error(path_text: str) -> str | None:
    """Require reusable templates to live in an owning skill's assets directory."""
    parts = Path(path_text).parts
    if len(parts) >= 4 and parts[:2] == (".agent", "skills") and parts[3] == "assets":
        return None
    return "template must be stored in its owning skill's assets/ directory"


def _is_task_record(parts: tuple[str, ...]) -> bool:
    """Return whether a path is an active task/index record, not a reusable template."""
    if parts[:2] != ("workspace", "tasks"):
        return False
    if len(parts) == 3 and parts[2] == "task.md":
        return True
    return (
        len(parts) == 4
        and parts[2] == "subtasks"
        and (
            parts[3] == "README.md"
            or re.fullmatch(r"\d{2}-.*\.md", parts[3], flags=re.IGNORECASE) is not None
        )
    )


def find_external_templates(root: Path) -> list[str]:
    """Find reusable template files or template directories outside skill folders."""
    errors: list[str] = []
    for candidate in root.rglob("*"):
        relative = candidate.relative_to(root)
        parts = relative.parts
        if (
            parts[:1] in {(".git",), ("master",)}
            or parts[:2] in {("workspace", "archive"), (".agent", "skills")}
            or _is_task_record(parts)
        ):
            continue

        if candidate.is_dir():
            if is_template_asset(relative.as_posix()):
                errors.append(
                    f"Misplaced template outside skills (directory): {relative.as_posix()}. "
                    "Move it to the owning skill's assets/ directory."
                )
            continue

        if not candidate.is_file() or not is_template_asset(relative.as_posix()):
            continue
        # Report the misplaced template directory once, not every file inside it.
        if any(part.casefold() in {"template", "templates"} for part in parts[:-1]):
            continue
        errors.append(
            f"Misplaced template outside skills: {relative.as_posix()}. "
            "Move it to the owning skill's assets/ directory."
        )
    return errors


def find_misplaced_skill_templates(root: Path) -> list[str]:
    """Find reusable templates or template directories outside skill assets/."""
    skill_root = root / ".agent" / "skills"
    if not skill_root.is_dir():
        return []
    errors: list[str] = []
    for candidate in skill_root.rglob("*"):
        relative = candidate.relative_to(root)
        parts = relative.parts
        if not is_template_asset(relative.as_posix()):
            continue
        if len(parts) >= 4 and parts[:2] == (".agent", "skills") and parts[3] == "assets":
            continue
        if candidate.is_file() and any(
            part.casefold() in {"template", "templates"} for part in parts[4:-1]
        ):
            continue
        errors.append(
            f"Misplaced skill template outside assets/: {relative.as_posix()}. "
            "Move copy-ready assets to the owning skill's assets/ directory."
        )
    return errors


def validate_catalog(root: Path, catalog_path: Path) -> tuple[list[str], int, int]:
    """Validate catalog rows and their exact repository references."""
    errors: list[str] = []
    try:
        content = catalog_path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        return [f"Cannot read catalog: {exc}"], 0, 0

    rows, parse_errors = read_inventory(content)
    errors.extend(parse_errors)
    errors.extend(find_misplaced_skill_templates(root))
    errors.extend(find_external_templates(root))
    errors.extend(validate_markdown_coverage(root, content))
    errors.extend(validate_non_markdown_coverage(root, content))
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
            raw_parts = path_text.split("/")
            if (
                path.is_absolute()
                or any(part in {"", ".", ".."} for part in raw_parts)
                or not path.parts
                or path.parts[0] not in ALLOWED_ROOTS
                or path_text.strip() != path_text
            ):
                errors.append(f"Line {line}: unsafe or out-of-scope path '{path_text}'.")
                continue
            target = root / path
            if not target.is_file():
                errors.append(f"Line {line}: referenced file does not exist: {path_text}.")

        if is_template:
            template_paths = [
                path for path in canonical_paths if is_template_asset(path)
            ]
            if not template_paths:
                errors.append(
                    f"Line {line}: Template required class must point to a named template."
                )
            for template_path in template_paths:
                location_error = template_location_error(template_path)
                if location_error:
                    errors.append(
                        f"Line {line}: invalid template location for "
                        f"'{template_path}': {location_error}."
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
        default=".agent/skills/the-worker/references/document-type-catalog.md",
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
