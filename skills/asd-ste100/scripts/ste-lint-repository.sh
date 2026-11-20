#!/usr/bin/env bash
set -euo pipefail

if [ "$#" -ne 1 ]; then
  echo "Usage: ste-lint-repository.sh FILE" >&2
  exit 2
fi

file="$1"
baseline=0
disable=""

# These values record the hard findings from the first full-document audit.
# Reduce each value when the file receives a reviewed STE rewrite.
case "$file" in
  skills/INITIALIZATION_POLICY.md) baseline=4 ;;
  skills/agent-skill-authoring/SKILL.md) baseline=6 ;;
  skills/asd-ste100/SKILL.md) baseline=31 ;;
  skills/asd-ste100/references/writing-rules.md) baseline=6 ;;
  skills/conversation-mode/SKILL.md) baseline=3 ;;
  skills/drawing/SKILL.md) baseline=24 ;;
  skills/drawing/references/archive-and-delivery.md) baseline=7 ;;
  skills/drawing/references/generation-recovery-and-provenance.md) baseline=17 ;;
  skills/drawing/references/image-editing-protocol.md) baseline=4 ;;
  skills/drawing/references/prompt-fidelity.md) baseline=15 ;;
  skills/drawing/references/series-continuity-and-iteration.md) baseline=9 ;;
  skills/philosophy-religion-asceticism/SKILL.md) baseline=7 ;;
  skills/philosophy-religion-asceticism/references/schopenhauer-44-week-curriculum.md) baseline=7 ;;
  skills/philosophy-religion-asceticism/references/source-standards.md) baseline=1 ;;
  skills/session-archiving/SKILL.md) baseline=7 ;;
  skills/session-archiving/references/archive-records-and-image-prompts.md) baseline=20 ;;
  skills/session-archiving/references/image-provenance-and-webp.md) baseline=2 ;;
esac

# STE-flavored prose does not enforce synonym rotation.
case "$file" in
  archive/README.md|images/README.md|images/takeout/README.md|skills/asd-ste100/README.md|skills/drawing/README.md|skills/drawing/references/patterns/*.md|skills/drawing/references/style-guide.md|skills/philosophy-religion-asceticism/README.md|skills/philosophy-religion-asceticism/CHANGELOG.md|skills/philosophy-religion-asceticism/references/*.md)
    disable="synonym-rotation"
    ;;
esac

# This reference quotes the semicolon as an example of the prohibited mark.
if [ "$file" = "skills/asd-ste100/references/writing-rules.md" ]; then
  disable="synonym-rotation,semicolon"
fi

args=()
if [ "$baseline" -gt 0 ]; then
  args+=(--baseline "$baseline")
fi
if [ -n "$disable" ]; then
  args+=(--disable "$disable")
fi

python3 skills/asd-ste100/scripts/ste-lint.py "${args[@]}" "$file"
