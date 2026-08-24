# Setup: B-grade <!-- TODO: ask me — name it -->

> **THIS SETUP DOES NOT EXIST YET.**
> My strategy document (2026-08-24) describes exactly one setup — see `a-plus.md`.
> Nothing below is mine; it is the blank template.
> `/checktrade` returns `INCOMPLETE: b-grade is undefined` if I name this setup.
> <!-- TODO: ask me — is there a second, lower-grade setup at all? "No" is a fine answer, -->
> <!-- and if it is the answer this file gets deleted rather than left lying around. -->


> This is a real setup at REDUCED risk. Its whole purpose is to stop me from calling a B-grade trade an A+ so I can size up.
> <!-- TODO: ask me — what risk multiple of A+ do I take on B-grade? A single number, e.g. 0.5x. -->
> <!-- TODO: ask me — am I allowed to take B-grade at all after a loss? -->


<!-- Copy this file for every named setup. If a setup is not written down here, it is not a setup, -->
<!-- it is an impulse, and /checktrade will return INCOMPLETE. -->

---

## Name
<!-- TODO: ask me -->

`<setup_tag>` — the exact string I type into the `setup_tag` column of `data/trades.csv`. Keep it short, lowercase, no spaces.

## Instruments
<!-- TODO: ask me -->

Which of NQ / ES / XAU/USD / US100 this setup is valid on, and any it is explicitly NOT valid on.

## Session / time window
<!-- TODO: ask me -->

Valid window in **Dhaka (GMT+6)** and **New York** time. Outside this window the setup does not exist.

## Higher-timeframe context required
<!-- TODO: ask me -->

What must be true on the HTF before this setup is even considered. Reference definitions in `strategy/01-market-structure.md`.

## Trigger conditions
<!-- TODO: ask me -->

Numbered, objective, testable. Each one must be answerable **yes** or **no** on a closed candle — never "forming", "looks like", or "almost".

1.
2.
3.

## Entry mechanic
<!-- TODO: ask me -->

Exactly how I get filled: market on close, limit at level, stop order beyond X. One method. Not "one of these".

## Stop placement rule
<!-- TODO: ask me -->

A rule that produces a single price, not a range. State what the stop is protecting against structurally.

## Target logic
<!-- TODO: ask me -->

Where the target comes from — which liquidity pool, which level, which rule. Partial-taking policy if any.

## Minimum R:R
<!-- TODO: ask me -->

A single number. If the trade cannot make this, it is not this setup.

## Invalidation BEFORE entry
<!-- TODO: ask me -->

What kills this idea while I am still waiting. See `strategy/invalidation.md`.

## Invalidation AFTER entry
<!-- TODO: ask me -->

What gets me out other than stop or target being hit.

## Screenshot examples
<!-- TODO: ask me -->

`screenshots/setups/<setup_tag>/` — at least 3 winners and 3 losers. Losers matter more.
(Note: `screenshots/` is gitignored, kept locally only.)

## Historical performance
<!-- TODO: ask me -->

<!-- AUTO-FILLED FROM scripts/stats.py — do not type numbers here by hand. -->
<!-- Run /review; the setup_tag breakdown updates this block. -->

| Metric | Value | As of |
|---|---|---|
| Trades | — | — |
| Win rate | — | — |
| Expectancy (R) | — | — |
| Profit factor | — | — |
| Avg process grade | — | — |
