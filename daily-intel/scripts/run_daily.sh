#!/usr/bin/env bash
# Generate today's brief with Claude Code and send it to Telegram.
# Schedule this with cron/launchd (e.g. 7am daily). Adjust paths as needed.
#
#   0 7 * * *  /bin/bash ~/.claude/skills/daily-intel/scripts/run_daily.sh
#
set -euo pipefail

SKILL_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ENV_FILE="${DAILY_INTEL_ENV:-$HOME/.daily-intel.env}"
BRIEF="$(mktemp)"
trap 'rm -f "$BRIEF"' EXIT

cd "$SKILL_DIR"

# Ask Claude Code to run this skill and write the brief to stdout.
claude -p "Run the daily-intel skill: read my-niche.md, research the last 24-48h, and output ONLY the finished briefing text (no preamble)." > "$BRIEF"

# Ship it to Telegram.
python3 "$SKILL_DIR/scripts/send_telegram.py" --env "$ENV_FILE" --file "$BRIEF"
