# Setup: New York Liquidity Sweep → 5M BOS

<!-- Source: my strategy document, given 2026-08-24, sections 16-24. -->
<!-- TODO: ask me — confirm the name and the setup_tag. I called it this from the description; -->
<!-- I did not invent the mechanics, but the label is mine until you confirm it. -->

> This is the setup I take at full risk. If it does not meet every line below, it is not A+.

---

## Name

`ny-sweep-bos` <!-- TODO: ask me — confirm this exact string for data/trades.csv -->

## Instruments

**NASDAQ and S&P 500 only.**

> "I trade only: NASDAQ, S&P 500."

<!-- TODO: ask me — futures (NQ/ES) or CFDs? The repo has files for both NQ and ES futures. -->
<!-- TODO: ask me — I take ONE trade per day (risk/risk-rules.md §5). If both NQ and ES present -->
<!-- a valid setup in the same window, which do I take? This will happen often, because the two -->
<!-- indices move together and I am watching both for SMT. It needs an answer, not a preference. -->

## Session / time window

| | UTC-4 | Dhaka |
|---|---|---|
| Chart prep complete by | 09:30 | 19:30 |
| Observe, do not execute | 09:30–09:40 | 19:30–19:40 |
| **Begin searching for execution** | **09:40** | **19:40** |
| Stated window ends | 09:45 | 19:45 |
| **Last permitted entry** | <!-- TODO: ask me --> | |

Outside the permitted window the setup does not exist.

## Higher-timeframe context required

Liquidity levels marked before the open, per `strategy/01-market-structure.md`:

- 4H High / Low (actual candle extremes, no blue/black rule) + 4H body open / close
- Asia High / Low (18:00 → 03:00)
- London High / Low (03:00 → 08:00)
- 1H High / Low (blue/black rule)
- Recent 5M High / Low (blue/black rule)

> "My previously marked levels are only potential liquidity targets."

## Trigger conditions

Each must be answerable **yes** or **no** on a **closed candle**. "Forming", "almost", "about to"
are all **no**.

1. **Time is inside the permitted execution window.** <!-- TODO: ask me — window end time undefined -->

2. **One of my pre-marked liquidity levels has been hit**, confirmed on the **5M** timeframe.
   Not the 1M. If no marked level has been hit, I keep waiting and there is no trade.

3. **Price has shown a reaction in the OPPOSITE direction to the sweep.**
   A liquidity hit is not an entry signal.
   > "Liquidity Hit → Wait for Opposite-Direction Confirmation"
   <!-- TODO: ask me — what makes a "reaction" objectively present, before BOS confirms it? -->
   <!-- As written this is a judgement call sitting between two testable conditions. -->

4. **5M BOS in the direction opposite the sweep, confirmed by a BODY CANDLE CLOSE — not a wick.**
   This is the priority confirmation.
   - High swept → **bearish** 5M BOS with body close
   - Low swept → **bullish** 5M BOS with body close

   <!-- TODO: ask me — BOS beyond WHICH level? Undefined. See strategy/01-market-structure.md. -->
   <!-- This is the load-bearing condition of the entire setup and it is not yet testable. -->

5. **5M IFVG** — optional, supporting.
   Must develop after or around the liquidity interaction and support the move away from it.
   <!-- TODO: ask me — IFVG is undefined. And if BOS and IFVG disagree, which wins? -->

6. **SMT divergence between NASDAQ and S&P 500.**
   <!-- TODO: ask me — required or optional? Undefined, and undefined as a concept in my files. -->

### The model in sequence

```
Pre-marked liquidity
        ↓
   Liquidity hit          (confirmed on 5M, not 1M)
        ↓
Opposite 5M structure     (BOS with BODY close — priority)
        ↓
New liquidity identified  (the 5M structure shows the next liquidity area)
        ↓
     Execution
```

## Entry mechanic

<!-- TODO: ask me — NOT DEFINED ANYWHERE IN THE STRATEGY DOCUMENT. -->
<!-- The document ends at "identify the opposite-side liquidity opportunity" and never says how -->
<!-- I get filled. Market order on the BOS close? Limit at the IFVG? Retrace to the BOS level? -->
<!-- One method, not a choice of three. Without this there is no setup, only an observation. -->

## Stop placement rule

<!-- TODO: ask me — NOT DEFINED ANYWHERE IN THE STRATEGY DOCUMENT. -->
<!-- THIS IS THE MOST IMPORTANT GAP IN THE REPO. -->
<!-- risk/risk-rules.md §8 says the stop is a live broker order placed the moment the position -->
<!-- opens, and never moves. risk/sizing.md solves position size FROM the stop distance. -->
<!-- Both are unusable without a rule that produces a single price. -->
<!-- Candidates I have NOT chosen for you: beyond the swept wick; beyond the swing that BOS broke; -->
<!-- beyond the IFVG. Name one. -->

## Target logic

<!-- TODO: ask me — implied but not stated. -->
<!-- The document says the 5M structure identifies "the next liquidity area" and that I then look -->
<!-- for "the opposite-side liquidity opportunity". Which liquidity, specifically? -->
<!-- The nearest opposing marked level? The next one in the hierarchy? A 4H level only? -->

## Minimum R:R

**1:1.5** — from `risk/risk-rules.md` §10. Target must pay at least **1.5R ($750)** measured to the
**first** target. If the nearest logical target does not pay it, the trade does not exist.

Stop distance comes from structure first; size is solved from it. Never shrink a stop to manufacture
the R:R.

## Invalidation BEFORE entry

- No marked liquidity has been hit → no trade, keep waiting.
- Liquidity hit but no opposite-direction 5M BOS with a **body** close → no trade.
- BOS confirmed by a wick only → **no trade.** Wick closes do not count.
- The level was already interacted with by a forward candle → it is not fresh liquidity
  (`strategy/01-market-structure.md`, forward-candle interaction rule).
- Time is outside the permitted window.

<!-- TODO: ask me — if the sweep happens at 09:42 but BOS does not confirm until 10:15, -->
<!-- is the idea still live, or dead? A time limit between sweep and confirmation. -->

## Invalidation AFTER entry

<!-- TODO: ask me — not defined. -->
<!-- Note what risk/risk-rules.md §8 already settles: the stop never moves, there is no breakeven -->
<!-- step, no trailing, no partial exits. So the only question left is whether I am permitted to -->
<!-- exit early on structure, and if so on what objective signal. -->

## Screenshot examples

`screenshots/setups/ny-sweep-bos/` — at least 3 winners and 3 losers. Losers matter more.
(`screenshots/` is gitignored, local only.)

## Historical performance

<!-- AUTO-FILLED FROM scripts/stats.py — do not type numbers here by hand. -->

| Metric | Value | As of |
|---|---|---|
| Trades | — | — |
| Win rate | — | — |
| Expectancy (R) | — | — |
| Profit factor | — | — |
| Avg process grade | — | — |

**Break-even win rate at 1:1.5 is 40%.** This setup has to clear that to be worth taking.
