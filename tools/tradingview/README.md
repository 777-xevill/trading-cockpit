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

## What it draws now

Since the Universal Definitions of 2026-08-26, most of the marking routine is mechanical:

| | |
|---|---|
| Vertical lines | 03:00 London, 09:30 New York, 18:00 Asia |
| 08:00 | Deliberately absent - invisible observation boundary |
| Asia range | High/low 18:00 -> 03:00, carried forward |
| London range | High/low 03:00 -> 08:00, carried forward |
| **Blue/Black structure** | Adjacent different-colour pairs only. High = higher upper wick, low = lower lower wick. |
| **Forward-candle interaction** | A level that gets **wicked** turns grey and dashed, labelled "hit". It stops extending. |
| Execution window | 09:40-09:45 shaded |

Add it on whichever timeframe you are reading - 1H, 5M or 1M. The blue/black rule is identical on
all three, so one indicator covers them.

## What it deliberately does NOT draw

| Not drawn | Why |
|---|---|
| 4H high / low | My rule is "visible highs and lows from the current active market structure". That is a judgement made by eye, with no mechanical definition. Stays hand-drawn - and that is a valid answer, not a gap. |
| BOS markers | Fully defined and easy to add. Left out because marking my levels is preparation, while marking my BOS is marking my trigger. A chart that lights up when the setup fires reads as a signal regardless of the label. My call to make in review. |
| Entries | Never. |

## The boundary

This folder marks **levels I defined**. It does not mark entries, and it will not.
An indicator that says "enter here" is a signal generator, and that is not what this repo is.
See the Prime Directive in `CLAUDE.md`.
