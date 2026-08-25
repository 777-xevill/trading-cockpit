# TradingView tools

## Why there is no MCP server here

TradingView has no official MCP server, and no public API that lets an external program draw on a
chart at tradingview.com. Third-party "TradingView MCP" projects pull quotes and screener data
through unofficial endpoints; none of them can place a line on my chart, because there is nothing
to place it through.

Pine Script runs **inside** TradingView and can. That is what this folder is for.

## cockpit-levels.pine

Marks the session levels from `strategy/02-session-plan.md` automatically.

**Install:** TradingView → Pine Editor → paste the file → Save → Add to chart.
Add it to both NASDAQ and S&P 500, since I watch the pair.

**What it draws**

| | |
|---|---|
| Vertical lines | 03:00 London, 09:30 New York, 18:00 Asia |
| 08:00 | Deliberately absent — invisible observation boundary |
| Asia range | High and low, 18:00 → 03:00, carried forward |
| London range | High and low, 03:00 → 08:00, carried forward |
| Execution window | 09:40–09:45 shaded |

Only one Asia range and one London range exist on the chart at a time. Previous sessions are
deleted, per "One meaningful liquidity area > multiple redundant lines."

**Timezone:** uses `America/New_York`, so it follows US daylight saving on its own. My notes say
UTC-4, which is only correct in summer — the indicator does not have that bug.

## What it does NOT draw, and why

Each of these needs a definition I have not written yet. Code cannot be vague, so these stay out
rather than being guessed at.

| Not drawn | The missing definition |
|---|---|
| Blue/black wick levels (1H, 5M, 1M) | Is "candle high" the wick high or the body high? What counts as "together"? |
| Recent 5M / 1M high and low | "Recent" has no number — bars or minutes? |
| Forward-candle interaction | Is "interacted with" a wick touch or a body close through? |
| 4H high / low | How many candles back? |
| BOS markers | Body close beyond **which** level? |

All five are open items in `OPEN-QUESTIONS.md`.

## The boundary

This folder marks **levels I defined**. It does not mark entries, and it will not.
An indicator that says "enter here" is a signal generator, and that is not what this repo is.
See the Prime Directive in `CLAUDE.md`.
