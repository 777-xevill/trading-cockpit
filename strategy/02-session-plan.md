# Session Plan

<!-- Source: my strategy document, given 2026-08-24. -->

**My charts are always set to UTC-4 — New York time.** All strategy times below are stated in
UTC-4 first, because that is what I actually look at, with Dhaka alongside so I know when to sit down.

---

## My clock

**UTC-4 to Dhaka (GMT+6) is +10 hours.**

| Marker | UTC-4 (my chart) | Dhaka (GMT+6) | Vertical line? |
|---|---|---|---|
| Asia session start | **18:00** | 04:00 | **Yes** |
| London session start | **03:00** | 13:00 | **Yes** |
| London pre-NY observation point | **08:00** | 18:00 | **No — invisible boundary** |
| New York / US market open | **09:30** | **19:30** | **Yes** |
| **My execution window** | **09:40–09:45** | **19:40–19:45** | — |

### The 08:00 rule

> "I do not use a visible vertical line at 08:00. The 08:00 point is effectively treated as an
> invisible observation boundary."

From **03:00 → 08:00** I focus specifically on the London session high and London session low.

### Daylight saving — READ THIS TWICE A YEAR

UTC-4 is New York in **summer** (EDT). In **winter** New York is UTC-5 (EST), and TradingView's
"New York" timezone follows the change automatically while the label "UTC-4" does not.

**When New York is on EST, every Dhaka time above shifts one hour later:** the 09:30 open becomes
**20:30 Dhaka** and the execution window becomes **20:40–20:45 Dhaka**.

<!-- TODO: ask me — do I want the winter times written out as a second table, or is one -->
<!-- reminder enough? Getting this wrong means sitting down an hour late and missing the window. -->

---

## Fatigue

The whole execution window is **19:40–19:45 Dhaka** (20:40–20:45 in winter). This is early evening.

**The late-night fatigue risk this repo was built around does not apply to this strategy.**
I am not trading the London killzone at 1am. I am trading the New York open at dinner time.

<!-- TODO: ask me — given that, do I still want a sleep minimum and a latest-hour rule? -->
<!-- They may be unnecessary now, or they may still matter for the chart prep the night before. -->
<!-- A rule that does not bind is a rule I stop reading, so if it is unnecessary it should go. -->

---

## Hard session rules

### New York open rule

I do **not** execute at the 09:30 open.

> "The 09:30 open frequently produces manipulation, liquidity grabs, and false movements."

**09:30 = Observation / Market Open.** I wait approximately **10–15 minutes**.

> "The purpose of waiting is to allow the initial New York manipulation to develop before looking
> for my actual execution model."

**Earliest I may execute:** **09:40 UTC-4** / 19:40 Dhaka.

**Latest I may enter:** <!-- TODO: ask me -->
<!-- The document says 09:40-09:45 is where I BEGIN actively searching. It never says when I stop. -->
<!-- Two readings, and they are very different rules: -->
<!--   (a) The window IS 09:40-09:45. Nothing after 09:45. Five minutes, then done. -->
<!--   (b) Searching STARTS at 09:40 and continues until some later time I have not named. -->
<!-- Under reading (b) there is no closing time at all, which means there is no rule. -->
<!-- /checktrade cannot check the session window until this is answered. -->

**Hard flat time — everything closed by:** <!-- TODO: ask me -->
<!-- Do I hold into the afternoon? Through the close? Never overnight? -->
<!-- Note: overnight and weekend holding may also be restricted by FundedNext. Unverified. -->

---

## Pre-session routine

From my strategy document, Step 1 — before the New York open:

1. Confirm TradingView timezone is **UTC-4 New York**
2. Mark the session vertical lines: **03:00**, **09:30**, **18:00** (never 08:00)
3. Mark relevant **4H** liquidity
4. Mark relevant **1H** liquidity — blue/black rule
5. Mark **Asia High / Low** (18:00 → 03:00)
6. Mark **London High / Low** (03:00 → 08:00)
7. Prepare to identify **recent 5M High / Low**

Then run `/premarket` to set the risk budget and write today's journal.

**What time do I sit down to do this?** <!-- TODO: ask me -->
<!-- The 4H and 1H marking has to happen before 09:30 UTC-4 / 19:30 Dhaka. How long does it take me? -->

---

## Sessions I trade

**New York open only.** London and Asia are marked for liquidity but are not execution sessions.

<!-- TODO: ask me — confirm. The strategy document describes only a New York execution model, -->
<!-- but never explicitly says I never execute in London or Asia. Silence is not a rule. -->

---

## News

<!-- TODO: ask me — not mentioned anywhere in the strategy document. -->
<!-- The execution window is 09:40-09:45 UTC-4. US data releases land at 08:30 and 10:00 UTC-4, -->
<!-- either side of it. This needs an answer before live trading: -->
<!--   * Which releases stop me trading that day? -->
<!--   * No-trade window: how many minutes before and after? -->
<!--   * Where do I check the calendar? -->
<!-- FundedNext may also restrict news trading. Unverified — see risk/prop-firm-rules.md. -->
