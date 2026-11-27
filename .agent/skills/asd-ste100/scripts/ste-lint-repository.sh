#!/usr/bin/env bash
set -euo pipefail

json_output=0
if [[ "${1:-}" == "--json" ]]; then
  json_output=1
  shift
fi
if [ "$#" -ne 1 ]; then
  echo "Usage: ste-lint-repository.sh [--json] FILE" >&2
  exit 2
fi

file="$1"
baseline=0
disable=""

# These values record the hard findings from the first full-document audit.
# Reduce each value when the file receives a reviewed STE rewrite.
case "$file" in
  .agent/INITIALIZATION_POLICY.md) baseline=4 ;;
  .agent/skills/agent-skill-authoring/SKILL.md) baseline=6 ;;
  .agent/skills/asd-ste100/SKILL.md) baseline=31 ;;
  .agent/skills/asd-ste100/references/writing-rules.md) baseline=6 ;;
  .agent/skills/drawing/SKILL.md) baseline=24 ;;
  .agent/skills/drawing/references/archive-and-delivery.md) baseline=7 ;;
  .agent/skills/drawing/references/generation-recovery-and-provenance.md) baseline=17 ;;
  .agent/skills/drawing/references/image-editing-protocol.md) baseline=4 ;;
  .agent/skills/drawing/references/prompt-fidelity.md) baseline=15 ;;
  .agent/skills/drawing/references/series-continuity-and-iteration.md) baseline=9 ;;
  .agent/skills/philosophy-religion-asceticism/SKILL.md) baseline=7 ;;
  .agent/skills/philosophy-religion-asceticism/references/schopenhauer-44-week-curriculum.md) baseline=7 ;;
  .agent/skills/philosophy-religion-asceticism/references/source-standards.md) baseline=1 ;;
esac

# STE-flavored prose does not enforce synonym rotation.
case "$file" in
  .takeout/images/README.md|.agent/skills/asd-ste100/README.md|.agent/skills/drawing/README.md|.agent/skills/drawing/references/patterns/*.md|.agent/skills/drawing/references/style-guide.md|.agent/skills/philosophy-religion-asceticism/README.md|.agent/skills/philosophy-religion-asceticism/CHANGELOG.md|.agent/skills/philosophy-religion-asceticism/references/*.md)
    disable="synonym-rotation"
    ;;
esac

# This reference quotes the semicolon as an example of the prohibited mark.
if [ "$file" = ".agent/skills/asd-ste100/references/writing-rules.md" ]; then
  disable="synonym-rotation,semicolon"
fi

args=()
if [ "$baseline" -gt 0 ]; then
  args+=(--baseline "$baseline")
fi
if [ -n "$disable" ]; then
  args+=(--disable "$disable")
fi
if [ "$json_output" -eq 1 ]; then
  args+=(--json)
fi

python3 .agent/skills/asd-ste100/scripts/ste-lint.py "${args[@]}" "$file"
