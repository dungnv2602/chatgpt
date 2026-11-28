#!/usr/bin/env python3
"""Validate bounded structural ownership invariants."""
from __future__ import annotations
import argparse
import re
import sys
from pathlib import Path
CHECKS = {
 "session-start": (".agent/SESSION_START.md", ["# Session Start", "The sole session-start cue is", "[The Worker](skills/the-worker/SKILL.md)"]),
 "conversation-mode": (".agent/skills/the-worker/references/conversation-mode.md", ["# Conversation Mode", "## Presentation settings", "The selected mode controls presentation only."]),
 "initialization-policy": (".agent/INITIALIZATION_POLICY.md", ["# Initialization Policy", "The Worker is the sole operational authority.", ".agent/SESSION_START.md", ".agent/skills/the-worker/SKILL.md", ".agent/skills/the-worker/references/conversation-mode.md"]),
 "worker": (".agent/skills/the-worker/SKILL.md", ["# The Worker", "## Authority and scope", "## Activation"]),
}
def validate(root: Path) -> list[str]:
 errors=[]
 for rule,(rel,markers) in CHECKS.items():
  p=root/rel
  if not p.is_file():
   errors.append(f"{rule}: missing canonical path: {rel}"); continue
  content=p.read_text(encoding="utf-8")
  for marker in markers:
   if marker not in content: errors.append(f"{rule}: {rel}: missing structural marker: {marker}")
 start=root/CHECKS["session-start"][0]
 if start.is_file():
  content=start.read_text(encoding="utf-8")
  links=re.findall(r"\[[^\]]+\]\(([^)]+)\)",content)
  if links != ["skills/the-worker/SKILL.md"]:
   errors.append("session-start: expected exactly one Worker pointer link; found "+repr(links))
  for target in links:
   if not (start.parent/target).is_file(): errors.append(f"session-start: unresolved pointer target: {target}")
 mode=root/CHECKS["conversation-mode"][0]
 if mode.is_file():
  content=mode.read_text(encoding="utf-8")
  if "## Operating rules" in content or "## Execution" in content:
   errors.append("conversation-mode: unexpected operational section marker")
 return errors
def main():
 parser=argparse.ArgumentParser(description=__doc__); parser.add_argument("--root",type=Path,default=Path("."))
 errors=validate(parser.parse_args().root.resolve())
 if errors:
  print("\n".join("ERROR: "+e for e in errors)); return 1
 print("Structural ownership checks passed."); return 0
if __name__=="__main__": sys.exit(main())
