---
name: daily-intel
description: A daily content-intelligence briefing for your niche, delivered to Telegram. Use this whenever the user wants to know what to post about today, what is trending in their space, what competitors or top creators are doing, or whether a platform changed something, or says things like "what should I post today," "what's trending in my niche," "give me my daily brief," "set up my daily intel," or "catch me up on my space." It reads a config file describing the user's niche, competitors, keywords, and where to look, searches the web for the last 24 to 48 hours, writes a short prioritized briefing with ready-to-use post ideas, and sends it to the user's Telegram so it is waiting for them every morning. Trigger it for any "what's happening / what do I post" request, and offer to set up the config and Telegram bot the first time.
---

# Daily Content Intel

A creator who knows what is working *today* never stares at a blank page. This skill is a morning analyst: it scans the user's niche, then hands back a short, ranked briefing of trends, competitor moves, platform changes, and content angles, with a few ready-to-use post ideas pulled from it. It delivers straight to **Telegram**, so the brief is sitting on their phone (and laptop) when they wake up.

It runs on a small config file so it is tailored, not generic. Set the config and the Telegram bot up once, then it can run every morning on a schedule.

## Step 1 — Load or create the config

Look for `my-niche.md` in the current project or the skill folder. If it exists, read it and use it. If it does not, create it with the user using `assets/my-niche-template.md` by asking:

- **Niche, in one line** (e.g. "personal branding for B2B founders").
- **Ideal audience** — who they are and what they care about.
- **Competitors / creators to track** — 3 to 8 handles, names, or channels. These are watched directly for new moves.
- **Keywords to search** — the exact topics they always want flagged (e.g. "founder-led marketing," "AI for content," "algorithm change").
- **Where to look** — which platforms and sources (Instagram, LinkedIn, YouTube, X, TikTok, Substack, specific blogs or newsletters).

Save their answers to `my-niche.md` and confirm it before the first run.

## Step 2 — Set up the Telegram bot (one time)

If `TELEGRAM_BOT_TOKEN` and `TELEGRAM_CHAT_ID` are already in the environment or a `.env` file, skip this. Otherwise walk the user through it once:

1. In Telegram, message **@BotFather**, send `/newbot`, and follow the prompts. It gives you a **bot token** (looks like `123456:ABC-DEF...`).
2. Send your new bot any message (say "hi") so it is allowed to message you back.
3. Get your **chat id**: message **@userinfobot**, or open `https://api.telegram.org/bot<YOUR_TOKEN>/getUpdates` in a browser and copy the `chat":{"id": ...}` number.
4. Save both as environment variables, never hard-coded in files:

   ```bash
   echo 'TELEGRAM_BOT_TOKEN="123456:ABC-your-token"' >> ~/.daily-intel.env
   echo 'TELEGRAM_CHAT_ID="111222333"' >> ~/.daily-intel.env
   ```

The send script reads these from the environment (or from a `.env` you point it at).

## Step 3 — Research the last 24 to 48 hours

Use web search. Run several focused searches in parallel, driven by the config's **keywords**, **competitors**, and **where to look**. Cover:

- **Niche news and trends** for the user's keywords.
- **Tracked competitors/creators** — recent notable posts, launches, or takes.
- **Platform updates** — algorithm, feature, or policy changes on their platforms.
- **What's spreading** — high-engagement posts, threads, or videos in the last day or two.
- **One wildcard** — an adjacent angle that could spark a fresh idea.

Always keep the real source URLs. Throw out anything older than 48 hours or off-topic. If a category is empty, skip it. Do not manufacture filler; an honest short brief beats a padded one.

## Step 4 — Write the briefing

Keep only what would actually change what the user makes or posts today. Use this structure, kept short and skimmable (aim for one phone screen):

```
📡 Daily Content Intel — [Day, Date]

🔥 Trending
1. [Punchy line]. Why it matters: [one line]. (link)
2. ...

👀 Competitor moves
- [Account] [did X]. Angle for you: [one line]. (link)

⚙️ Platform changes
- [Platform]: [what changed + the practical implication]. (link)

✍️ 3 post ideas for today
1. [Specific hook/angle tied to something above]
2. ...
3. ...
```

The "3 post ideas" section is the payoff — each idea specific enough to film or write immediately and tied to something real from the brief. (Emojis are fine here because Telegram is a private channel, not a public post.)

## Step 5 — Send it to Telegram

Pass the finished brief to the bundled sender, which posts it to the user's chat via the Telegram Bot API (no pip packages needed):

```bash
python3 scripts/send_telegram.py --env ~/.daily-intel.env --file brief.txt
# or pipe it:
cat brief.txt | python3 scripts/send_telegram.py --env ~/.daily-intel.env
```

It chunks long briefs to fit Telegram's message limit and reports success. Confirm delivery to the user on the first run.

## Step 6 — Run it every morning (optional but the whole point)

To make the brief arrive automatically, schedule a job that runs Claude Code with this skill and pipes the output to the sender.

**macOS / Linux (cron), 7am daily:**

```bash
crontab -e
# add this line (adjust the path to the skill):
0 7 * * * cd ~/.claude/skills/daily-intel && claude -p "Run daily-intel: research my niche and send the brief to Telegram" >> ~/daily-intel.log 2>&1
```

Use `scripts/run_daily.sh` as a ready-made wrapper if they prefer. Keep the Telegram token in the `.env`, never in the crontab. If they are on Windows, point them to Task Scheduler with the same command. Don't assume their tooling is installed — confirm `claude` and `python3` are on the PATH first.
