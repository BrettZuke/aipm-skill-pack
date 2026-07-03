#!/bin/bash
# Installs every skill in this repo into ~/.claude/skills
set -e

cd "$(dirname "$0")"
DEST="$HOME/.claude/skills"
mkdir -p "$DEST"

count=0
for dir in */; do
  name="${dir%/}"
  [ -f "$name/SKILL.md" ] || continue
  rm -rf "${DEST:?}/$name"
  cp -R "$name" "$DEST/$name"
  echo "installed: $name"
  count=$((count + 1))
done

echo ""
echo "$count skills installed to $DEST"
echo "Restart Claude Code, then try: write me 10 hooks for a video about cold outreach"
