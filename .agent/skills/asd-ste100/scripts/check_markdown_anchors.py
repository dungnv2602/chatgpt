#!/usr/bin/env python3
"""Check local Markdown links and GitHub-style heading anchors."""

from __future__ import annotations

import argparse
import html
import posixpath
import re
import subprocess
import sys
import unicodedata
from pathlib import Path
from urllib.parse import unquote, urlsplit

EXCLUDED_PREFIXES = (
    ".takeout/reports/lint_reports/",
    "workspace/tasks/",
    "workspace/discussion.md",
    "area/drawing/history/",
    "master/",
    "area/novel/templates/",
    ".agent/skills/prompt-master/",
    ".agent/skills/asd-ste100/examples/",
)
BACKTICK = chr(96)
FENCE_RE = re.compile(r"^\s{0,3}(" + re.escape(BACKTICK) + r"{3,}|~{3,})")
HEADING_RE = re.compile(r"^ {0,3}(#{1,6})\s+(.+?)\s*#*\s*$")
SETEXT_RE = re.compile(r"^ {0,3}(=+|-+)\s*$")
INLINE_LINK_RE = re.compile(
    r"!?\[[^\]]*\]\(\s*(<[^>]+>|[^\s)]+)(?:\s+[^)]*)?\)"
)
REFERENCE_RE = re.compile(r"^\s{0,3}\[[^\]]+\]:\s*(<[^>]+>|\S+)")
HTML_LINK_RE = re.compile(r"\b(?:href|src)\s*=\s*([\"'])(.*?)\1", re.I)
HTML_ID_RE = re.compile(r"\b(?:id|name)\s*=\s*([\"'])(.*?)\1", re.I)


def tracked_paths() -> list[str]:
    result = subprocess.run(
        ["git", "ls-files"],
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.splitlines()


def tracked_markdown() -> list[str]:
    return [path for path in tracked_paths() if path.lower().endswith(".md")]


def active_markdown(files: list[str]) -> list[str]:
    return [
        path for path in files
        if not path.startswith(EXCLUDED_PREFIXES)
    ]


def select_active_sources(
    active_files: list[str], requested_paths: list[str] | None = None
) -> list[str]:
    if requested_paths is None:
        return list(active_files)
    requested = {path for path in requested_paths if path}
    invalid = sorted(requested - set(active_files))
    if invalid:
        raise ValueError(
            "Source scope contains inactive or untracked Markdown paths: "
            + ", ".join(invalid)
        )
    return [path for path in active_files if path in requested]


def remove_fenced_blocks(text: str) -> str:
    kept = []
    fence_char = None
    fence_size = 0
    for line in text.splitlines():
        match = FENCE_RE.match(line)
        if match:
            marker = match.group(1)
            if fence_char is None:
                fence_char = marker[0]
                fence_size = len(marker)
            elif marker[0] == fence_char and len(marker) >= fence_size:
                fence_char = None
                fence_size = 0
            continue
        if fence_char is None:
            kept.append(line)
    return "\n".join(kept)


def clean_heading(text: str) -> str:
    text = re.sub(r"!\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"<[^>]+>", "", text)
    code_pattern = re.escape(BACKTICK) + r"+([^" + re.escape(BACKTICK) + r"]*)" + re.escape(BACKTICK) + r"+"
    text = re.sub(code_pattern, r"\1", text)
    text = re.sub(r"[*~]", "", text)
    return html.unescape(text).strip()


def github_slug(text: str) -> str:
    value = clean_heading(text).lower()
    output = []
    for char in value:
        category = unicodedata.category(char)
        if char.isspace():
            output.append("-")
        elif char in "-_" or not category.startswith("P"):
            output.append(char)
    return "".join(output).strip("-")


def heading_anchors(text: str) -> set[str]:
    text = remove_fenced_blocks(text)
    anchors = set()
    counts: dict[str, int] = {}
    lines = text.splitlines()
    for index, line in enumerate(lines):
        anchors.update(unquote(value) for _, value in HTML_ID_RE.findall(line))
        match = HEADING_RE.match(line)
        heading = match.group(2) if match else None
        if heading is None and index + 1 < len(lines):
            if line.strip() and SETEXT_RE.match(lines[index + 1]):
                heading = line.strip()
        if heading is None:
            continue
        base = github_slug(heading)
        if not base:
            continue
        count = counts.get(base, 0)
        slug = base if count == 0 else f"{base}-{count}"
        counts[base] = count + 1
        anchors.add(slug)
    return anchors


def link_targets(text: str) -> list[str]:
    text = remove_fenced_blocks(text)
    targets = []
    for match in INLINE_LINK_RE.finditer(text):
        targets.append(match.group(1).strip("<>"))
    for line in text.splitlines():
        match = REFERENCE_RE.match(line)
        if match:
            targets.append(match.group(1).strip("<>"))
    targets.extend(match.group(2) for match in HTML_LINK_RE.finditer(text))
    return targets


TEMPLATE_PLACEHOLDER_RE = re.compile(r"\{[A-Za-z_][A-Za-z0-9_.-]*\}|\$\{\{.*?\}\}")


def resolve_markdown_target(
    source: str, target: str, file_set: set[str], all_paths: set[str]
) -> str | None:
    # This link becomes valid after the template is copied into a task folder.
    if source == "workspace/TASK_TEMPLATE.md" and target == "subtasks/README.md":
        return None
    # Runtime template placeholders are not literal local file paths.
    if TEMPLATE_PLACEHOLDER_RE.search(target):
        return None
    parsed = urlsplit(target)
    if parsed.scheme or parsed.netloc:
        return None
    raw_path = unquote(parsed.path)
    if not raw_path:
        return source
    base = posixpath.dirname(source)
    candidate = posixpath.normpath(
        raw_path.lstrip("/") if raw_path.startswith("/")
        else posixpath.join(base, raw_path)
    )
    if candidate.startswith("../") or candidate == "..":
        return None
    if candidate.lower().endswith(".md"):
        return candidate
    if posixpath.splitext(candidate)[1] or candidate in all_paths:
        return None
    directory_prefix = candidate.rstrip("/") + "/"
    if any(path.startswith(directory_prefix) for path in all_paths):
        return None
    candidates = [
        candidate + ".md",
        posixpath.join(candidate, "README.md"),
        posixpath.join(candidate, "index.md"),
    ]
    return next((path for path in candidates if path in file_set), candidates[0])


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--sources-file",
        type=Path,
        help="Check links only from these changed active Markdown sources.",
    )
    args = parser.parse_args()

    all_paths = set(tracked_paths())
    all_files = sorted(path for path in all_paths if path.lower().endswith(".md"))
    active_files = active_markdown(all_files)
    try:
        requested = None
        if args.sources_file is not None:
            requested = [
                line.strip()
                for line in args.sources_file.read_text(encoding="utf-8").splitlines()
                if line.strip()
            ]
        sources = select_active_sources(active_files, requested)
    except (OSError, ValueError) as exc:
        print("Unable to select active Markdown sources: " + str(exc), file=sys.stderr)
        return 2

    file_set = set(all_files)
    anchors_by_file = {}
    issues = []
    links_checked = 0

    for source in all_files:
        text = Path(source).read_text(encoding="utf-8")
        anchors_by_file[source] = heading_anchors(text)

    for source in sources:
        text = Path(source).read_text(encoding="utf-8")
        for target in link_targets(text):
            parsed = urlsplit(target)
            destination = resolve_markdown_target(source, target, file_set, all_paths)
            if destination is None:
                continue
            links_checked += 1
            if destination not in file_set:
                issues.append((source, target, "missing Markdown file"))
                continue
            fragment = unquote(parsed.fragment)
            if fragment and not re.fullmatch(r"L\d+(?:-L\d+)?", fragment):
                if fragment not in anchors_by_file[destination]:
                    issues.append((source, target, "missing heading anchor"))

    scope = "all active" if requested is None else "changed"
    print(
        f"Scanned {len(sources)} {scope} Markdown sources "
        f"({len(all_files)} available as link targets) and "
        f"{links_checked} local Markdown links."
    )
    print(f"Found {len(issues)} unresolved local Markdown targets or anchors.")
    for source, target, reason in issues:
        print(f"{source}: {reason}: {target}")
    return 1 if issues else 0


if __name__ == "__main__":
    sys.exit(main())
