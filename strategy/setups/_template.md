# Setup: <NAME>

<!-- Copy this file for every named setup. If a setup is not written down here, it is not a setup, -->
<!-- it is an impulse, and /checktrade will return INCOMPLETE. -->

---

## Name

`<setup_tag>` — the exact string I type into the `setup_tag` column of `data/trades.csv`. Keep it short, lowercase, no spaces.

## Instruments

Which of NQ / ES / XAU/USD / US100 this setup is valid on, and any it is explicitly NOT valid on.

## Session / time window

Valid window in **Dhaka (GMT+6)** and **New York** time. Outside this window the setup does not exist.

## Higher-timeframe context required

What must be true on the HTF before this setup is even considered. Reference definitions in `strategy/01-market-structure.md`.

## Trigger conditions

Numbered, objective, testable. Each one must be answerable **yes** or **no** on a closed candle — never "forming", "looks like", or "almost".

1.
2.
3.

## Entry mechanic

Exactly how I get filled: market on close, limit at level, stop order beyond X. One method. Not "one of these".

## Stop placement rule

A rule that produces a single price, not a range. State what the stop is protecting against structurally.

## Target logic

Where the target comes from — which liquidity pool, which level, which rule. Partial-taking policy if any.

## Minimum R:R

A single number. If the trade cannot make this, it is not this setup.

## Invalidation BEFORE entry

What kills this idea while I am still waiting. See `strategy/invalidation.md`.

## Invalidation AFTER entry

What gets me out other than stop or target being hit.

## Screenshot examples

`screenshots/setups/<setup_tag>/` — at least 3 winners and 3 losers. Losers matter more.
(Note: `screenshots/` is gitignored, kept locally only.)

## Historical performance

<!-- AUTO-FILLED FROM scripts/stats.py — do not type numbers here by hand. -->
<!-- Run /review; the setup_tag breakdown updates this block. -->

| Metric | Value | As of |
|---|---|---|
| Trades | — | — |
| Win rate | — | — |
| Expectancy (R) | — | — |
| Profit factor | — | — |
| Avg process grade | — | — |
