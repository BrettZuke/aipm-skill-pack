#!/usr/bin/env python3
"""
Send a message to Telegram via the Bot API. No pip packages required.

Reads the bot token and chat id from the environment (or a --env file):
    TELEGRAM_BOT_TOKEN   from @BotFather
    TELEGRAM_CHAT_ID     your chat id (from @userinfobot or getUpdates)

Usage:
    python3 send_telegram.py --file brief.txt
    cat brief.txt | python3 send_telegram.py
    python3 send_telegram.py --env ~/.daily-intel.env "Some message text"

Telegram caps messages at 4096 chars, so long briefs are split automatically.
"""
import argparse
import json
import os
import sys
import urllib.parse
import urllib.request

TELEGRAM_LIMIT = 4096


def load_env_file(path):
    """Load simple KEY=VALUE / KEY="VALUE" lines into os.environ (no overwrite)."""
    path = os.path.expanduser(path)
    if not os.path.exists(path):
        sys.exit(f"--env file not found: {path}")
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, val = line.split("=", 1)
            os.environ.setdefault(key.strip(), val.strip().strip('"').strip("'"))


def chunk(text, size=TELEGRAM_LIMIT):
    """Split text into <=size pieces, preferring to break on blank lines."""
    chunks, cur = [], ""
    for para in text.split("\n\n"):
        block = (para + "\n\n")
        if len(cur) + len(block) > size:
            if cur:
                chunks.append(cur.rstrip())
            # a single oversized paragraph: hard-split it
            while len(block) > size:
                chunks.append(block[:size])
                block = block[size:]
            cur = block
        else:
            cur += block
    if cur.strip():
        chunks.append(cur.rstrip())
    return chunks or [text[:size]]


def send(token, chat_id, text):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = urllib.parse.urlencode({
        "chat_id": chat_id,
        "text": text,
        "disable_web_page_preview": "true",
    }).encode()
    req = urllib.request.Request(url, data=data)
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("message", nargs="?", help="message text (or use --file / stdin)")
    ap.add_argument("--file", help="read message from this file")
    ap.add_argument("--env", help="load token/chat id from this KEY=VALUE file")
    args = ap.parse_args()

    if args.env:
        load_env_file(args.env)

    token = os.environ.get("TELEGRAM_BOT_TOKEN")
    chat_id = os.environ.get("TELEGRAM_CHAT_ID")
    if not token or not chat_id:
        sys.exit("Missing TELEGRAM_BOT_TOKEN or TELEGRAM_CHAT_ID (set env vars or use --env).")

    if args.file:
        with open(args.file) as f:
            text = f.read()
    elif args.message:
        text = args.message
    elif not sys.stdin.isatty():
        text = sys.stdin.read()
    else:
        sys.exit("No message provided (pass text, --file, or pipe via stdin).")

    text = text.strip()
    if not text:
        sys.exit("Message is empty.")

    parts = chunk(text)
    for i, part in enumerate(parts, 1):
        try:
            res = send(token, chat_id, part)
        except urllib.error.HTTPError as e:
            sys.exit(f"Telegram API error ({e.code}): {e.read().decode()[:300]}")
        if not res.get("ok"):
            sys.exit(f"Telegram rejected the message: {res}")
        print(f"  sent part {i}/{len(parts)}")
    print("Delivered to Telegram.")


if __name__ == "__main__":
    main()
