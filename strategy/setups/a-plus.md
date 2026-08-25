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

**Stage 1 qualifies the idea. It is not an entry.** Once conditions 1–4 are met I move to the 1M.

---

### STAGE 2 — 1M entry sequence

> "After the 5M BOS, I shift to the 1M timeframe for the retracement."

On the 1M I focus **only on the recent high and low**, using the same **blue/black candle wick rules**
from `strategy/01-market-structure.md`.

> "Always focus on the most recent valid high/low and apply the same Blue/Black wick rules."

Written for a **long** (a marked low was swept, 5M BOS was bullish). Reverse everything for a short.

6. **A recent LOW forms on the 1M**, identified by the blue/black wick rule, including its relevant wick.

7. **That recent low is broken to the downside by a 1M BOS, confirmed by a FULL BODY CLOSE.**
   Not a wick through the level. This is the retracement leg — it moves *against* the 5M bias, on purpose.

8. **The most recent high/low is identified again** on the 1M, same blue/black wick rules.

9. **A 1M BOS back to the UPSIDE, confirmed by a FULL BODY CLOSE** — back in the direction of
   the 5M bias. Wick closes do not count here either.

10. **The other index confirms.** I check NASDAQ against S&P 500.
    > "If the other index gives a BOS or IFVG, I take the entry. If there is no BOS or IFVG,
    > I do not take the trade."

    **This is a hard gate.** No confirmation on the other index = no trade, regardless of how clean
    the first nine conditions were.

### The full model in sequence

```
              STAGE 1  —  5M qualification
   Pre-marked liquidity
           |
      Liquidity hit           (confirmed on 5M, never 1M)
           |
   Opposite-direction reaction
           |
      5M BOS                  (BODY close, not wick)
           |
              STAGE 2  —  1M entry
   Shift to 1M
           |
   Recent low forms           (blue/black wick rule)
           |
   1M BOS downside            (BODY close - the retracement, against the 5M bias)
           |
   Recent high/low again      (blue/black wick rule)
           |
   1M BOS upside              (BODY close - back with the 5M bias)
           |
   Other index: BOS or IFVG?  --- NO ---> NO TRADE
           |
          YES
           |
       EXECUTION
```

<!-- NOTE ON CONFLUENCE 4: my strategy overview lists "SMT Divergence" as one of the four -->
<!-- confluences, but step 10 above is not a divergence — it is a CONFIRMATION that the other -->
<!-- index is doing the SAME thing. Those are opposite ideas. -->
<!-- TODO: ask me — are these one rule or two? If SMT divergence is a separate requirement, -->
<!-- it needs its own numbered condition and its own definition. Not merging them on my own. -->

## Entry mechanic

**The TRIGGER is defined** (stage 2, conditions 6–10): the second 1M BOS back in the direction of
the 5M bias, with the other index confirming by BOS or IFVG.

**The FILL is not.** <!-- TODO: ask me -->
<!-- The trigger tells me WHEN. It does not tell me at WHAT PRICE I get in. Candidates: -->
<!--   (a) Market order on the close of the 1M BOS candle -->
<!--   (b) Limit order at the 1M IFVG / imbalance left by that BOS -->
<!--   (c) Limit order at the retracement low that the BOS broke away from -->
<!-- These produce different entry prices, therefore different stop distances, therefore -->
<!-- different position sizes and different R:R on the same trade. One method, not three. -->

**Both 1M BOS legs require a full body close** (confirmed 2026-08-26), same standard as the 5M.
One confirmation rule across every timeframe — there is nothing to remember per-chart.

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
- **Any BOS confirmed by a wick only → no trade.** Applies to the 5M BOS and to both 1M BOS legs.
  A wick through a level is not a break of structure on any timeframe in this model.
- The level was already interacted with by a forward candle → it is not fresh liquidity
  (`strategy/01-market-structure.md`, forward-candle interaction rule).
- Time is outside the permitted window.
- **The other index gives neither a BOS nor an IFVG** at stage 2 condition 10.
- The 1M retracement sequence never completes — no 1M counter-BOS, or no 1M BOS back in the
  direction of the 5M bias.

<!-- TODO: ask me — if the sweep happens at 09:42 but BOS does not confirm until 10:15, -->
<!-- is the idea still live, or dead? A time limit between sweep and confirmation. -->

<!-- TODO: ask me — HOW DEEP MAY THE 1M RETRACEMENT GO before the idea is dead? -->
<!-- Stage 2 deliberately waits for price to move AGAINST the 5M bias. Nothing in my strategy -->
<!-- says when that retracement has gone too far. On a long, if the 1M downside BOS runs all the -->
<!-- way back through the swept low, the sweep itself has failed — but as written I would still -->
<!-- be waiting for a 1M BOS back up and calling it a valid entry. -->
<!-- This needs a hard price level, not a feel. -->

<!-- TODO: ask me — is there a time limit on the 1M sequence? It has four steps (recent low, -->
<!-- counter-BOS, recent high/low, BOS back). At 1M that could resolve in 6 minutes or 90. -->

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
