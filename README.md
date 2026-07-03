# AIPM Skill Pack

15 Claude Code skills for content, copy, lead generation, local SEO, and premium client sites. Nothing here overlaps the starter pack you installed from ai-partner-method-claude-starter, this is all new. Install once, then just ask Claude for the thing you want. Claude picks the right skill automatically.

## Install (1 minute)

Open Terminal and run:

```
git clone https://github.com/BrettZuke/aipm-skill-pack.git
cd aipm-skill-pack
bash install.sh
```

Then restart Claude Code. That is it.

Manual alternative: download this repo as a zip (green Code button, Download ZIP), unzip it, and copy every skill folder into `~/.claude/skills/` (Mac: Finder, press Cmd+Shift+G, type `~/.claude/skills`). Create the folder if it does not exist.

## First steps

1. When you sign a client, say "set up a client profile for [business name]". Five questions, answered once per client. Every content skill then writes in that client's voice instead of re-asking setup questions.
2. Test it: ask Claude "write me 10 hooks for a video about cold outreach". If it mentions using viral-hook-creator, you are live.

## What is inside and how to trigger each one

| Skill | Say something like |
|---|---|
| client-brand | "Set up a client profile for [business]" (once per client; saves their niche, offer, and voice so every other skill writes as them) |
| viral-hook-creator | "Write hooks for a video about X" |
| idea-hacker | "Turn this idea into a week of content" |
| creative-copywriting-master | "Write the carousel copy for X" |
| ugc-content-creator | "Write a UGC-style ad script for X" |
| viral-reel-generator | "Script a 30 second reel about X" |
| avoid-ai-writing | "Strip the AI patterns out of this draft" |
| carousel-builder | "Make a carousel about X" (needs Google Chrome installed) |
| lead-magnet-builder | "Turn this video into a lead magnet PDF" |
| sales-call-analyzer | "Pull content ideas from this call transcript" |
| daily-intel | "Set up my daily content brief" (optional: 5 min Telegram bot setup, the skill walks you through it) |
| editorial-luxury-site | "Build a fancy Editorial Luxury site for my client" (premium one-page showpiece for high-ticket clients; includes a finished example site you can open in your browser, plus a photo generator that needs your own OpenAI key, about 50 cents per site) |
| premium-funnel-page | "Build a premium opt-in page" or "build the funnel pages" (editorial dark luxury funnel pages: opt-in, confirmation, booking) |
| apple-scroll-hero | "Give this site an Apple-style scroll video hero" (video scrubs frame by frame as the visitor scrolls) |
| seo-maps | "Run a maps audit for [business] in [city]" (Google Maps presence for local clients: competitor radius mapping, NAP checks, Google Business checklist, LocalBusiness schema; free tier needs no API keys, pairs with the seo-local skill from the starter pack) |

## Notes

- Everything runs locally inside your Claude Code. No accounts, no subscriptions, no data leaves your machine except normal Claude usage.
- carousel-builder renders real 1080x1350 PNG slides using your installed Chrome. First run, tell it your client's brand colors and handle and it remembers.
- daily-intel can run on a schedule every morning. Ask Claude to "set up the daily-intel cron" after the Telegram step.
- Stack them: idea-hacker to plan the week, viral-hook-creator for openers, carousel-builder to design, avoid-ai-writing as the final pass.
- Claude Code needs a paid Claude plan (Pro or above) when you sign in.
- Re-running install.sh is safe. It updates every skill to the latest version in this repo.
