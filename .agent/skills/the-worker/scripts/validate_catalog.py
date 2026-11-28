#!/usr/bin/env python3
"""Validate the Markdown path-coverage contract in the Worker document catalog."""
from __future__ import annotations
import argparse
import re
import sys
from pathlib import Path

CATALOG = ".agent/skills/the-worker/references/document-type-catalog.md"
SECTION = "## Markdown inventory coverage"
VALID_CLASSES = {"Template required", "Schema required", "Embedded contract", "Generator-owned", "Lightweight pattern", "Exempt"}
VALID_STATUS = {"Active", "Reserved", "Optional"}

def parse_rules(text: str) -> list[dict[str,str]]:
    section = text.split(SECTION,1)
    if len(section)!=2: return []
    rows=[]
    in_table=False
    for line in section[1].splitlines():
        if line.strip().startswith("|"): in_table=True
        elif in_table and line.strip(): break
        if not line.strip().startswith("|"): continue
        cells=[x.strip() for x in line.strip().strip("|").split("|")]
        if len(cells)!=5 or cells[0]=="Path pattern" or all(re.fullmatch(r":?-+:?",x or "-") for x in cells): continue
        rows.append(dict(zip(("pattern","class","status","authority","rationale"),cells)))
    return rows

def matches(root: Path, pattern: str) -> list[str]:
    return sorted(p.as_posix() for p in root.glob(pattern) if p.is_file() and p.suffix.lower()==".md")

def validate(root: Path) -> list[str]:
    errors=[]
    catalog=root/CATALOG
    if not catalog.is_file(): return [f"missing catalog: {CATALOG}"]
    rules=parse_rules(catalog.read_text(encoding="utf-8"))
    if not rules: return ["catalog: Markdown inventory coverage table is missing or empty"]
    seen=set()
    rule_matches={}
    for row in rules:
        p=row["pattern"]
        if p in seen: errors.append(f"duplicate path rule: {p}")
        seen.add(p)
        if row["class"] not in VALID_CLASSES: errors.append(f"{p}: invalid class {row['class']}")
        if row["status"] not in VALID_STATUS: errors.append(f"{p}: invalid coverage status {row['status']}")
        if row["status"]=="Optional" and row["class"]!="Generator-owned": errors.append(f"{p}: Optional is only valid for Generator-owned")
        found=[x for x in matches(root,p) if not x.startswith("master/") and not x.startswith("workspace/archive/")]
        rule_matches[p]=set(found)
        if row["status"]=="Active" and not found: errors.append(f"{p}: Active rule matches no in-scope Markdown file")
        if row["status"]=="Reserved" and found: errors.append(f"{p}: Reserved rule already matches: {found[:5]}")
    # Each in-scope Markdown file must be covered by at least one Active or Optional rule.
    inventory=[]
    for path in root.rglob("*.md"):
        rel=path.relative_to(root).as_posix()
        if rel.startswith("master/") or rel.startswith("workspace/archive/") or ".git/" in rel: continue
        inventory.append(rel)
    for rel in inventory:
        covered=any(row["status"] in {"Active","Optional"} and rel in rule_matches.get(row["pattern"],set()) for row in rules)
        if not covered: errors.append(f"uncovered Markdown path: {rel}")
    return errors

def main() -> int:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root",type=Path,default=Path("."))
    errors=validate(parser.parse_args().root.resolve())
    if errors: print("\n".join("ERROR: "+e for e in errors)); return 1
    print("Document catalog coverage checks passed."); return 0
if __name__=="__main__": sys.exit(main())
