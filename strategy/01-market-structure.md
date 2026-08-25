# Market Structure — My Definitions

<!-- Source: my strategy document, given 2026-08-24. -->
<!-- Where a definition below is mine, it is quoted from that document. -->
<!-- Where it is missing, it is marked TODO and stays blank. Nothing here was invented. -->

---

## The four confluences

My execution is based on four major confluences:

1. **Liquidity**
2. **Break of Structure (BOS)**
3. **IFVG**
4. **SMT Divergence**

> "A trade should not be taken simply because one confluence appears. The setup must develop
> according to my execution model and the relevant confluences must align."

**How many of the four must be present to take a trade?** <!-- TODO: ask me -->
<!-- The document says "the relevant confluences must align" but never says which are mandatory. -->
<!-- Section 19 implies BOS is priority and IFVG is optional. SMT is never given a requirement level. -->
<!-- /checktrade cannot check "the relevant ones" — it needs a fixed list. -->

---

## Timeframes I use

| Purpose | Timeframe |
|---|---|
| Higher-timeframe liquidity | **4H** |
| Session liquidity | **Asia / London ranges** |
| Intermediate liquidity | **1H** |
| Short-term liquidity | **5M** |
| **Stage 1 — qualification** | **5M** |
| **Stage 2 — retracement and entry** | **1M** |

The two timeframes have strictly separated jobs, and the boundary is a rule:

> "I do not use the 1-minute timeframe simply to determine whether my marked liquidity has been hit."

> "After the 5M BOS, I shift to the 1M timeframe for the retracement."

**5M decides whether there is a trade. 1M decides when to take it.**
A liquidity hit is never confirmed on the 1M. An entry is never taken on the 5M.

---

## Liquidity framework

Liquidity is the primary component. Before looking for an execution I identify important liquidity
levels. My main references:

1. Session Highs and Lows
2. 4H Highs and Lows
3. 1H Highs and Lows
4. Recent 5-Minute Highs and Lows

### Liquidity hierarchy

**Higher-timeframe liquidity**
- 4H High wick
- 4H Low wick
- 4H body opening
- 4H body closing

**Session liquidity**
- Asia High wick
- Asia Low wick
- London High wick
- London Low wick

**Intermediate liquidity**
- 1H High
- 1H Low

**Short-term liquidity**
- Recent 5M High
- Recent 5M Low

**Does the hierarchy rank the levels by importance, or just group them?** <!-- TODO: ask me -->
<!-- i.e. if price sweeps a 5M high and a 4H high in the same move, does the 4H one govern? -->
<!-- And is a 4H sweep a better trade than a 5M sweep, or are they equal once confirmed? -->

---

## Session high and low marking

### Asia
Begins **18:00 UTC-4**. Range is **18:00 → 03:00**. I mark:
- Asia High
- Asia Low

### London
Begins **03:00 UTC-4**. Range is **03:00 → 08:00**. I mark **only**:
- London High
- London Low

> "I do not add unnecessary additional levels during this period. The London range becomes an
> important liquidity reference for the upcoming New York session."

---

## 4H high and low

I mark 4H High and 4H Low **according to the actual candle extremes**.

> "There is no blue/black candle-selection rule for the 4H timeframe."

The 4H levels are treated as major higher-timeframe liquidity.

I also track **4H body opening** and **4H body closing** as higher-timeframe liquidity (see hierarchy).

**How many 4H candles back do I mark?** <!-- TODO: ask me -->
**Which 4H body open/close — the current candle, the previous one, a specific session's?** <!-- TODO: ask me -->

---

## The blue/black candle rule — 1H, 5M and 1M

My TradingView candle colours:

- **Blue = bullish candle**
- **Black = bearish candle**

The rule applies **only when a blue and a black candle are together**. It does **not** apply to
blue + blue, or black + black. It is specifically for **blue + black** or **black + blue**.

> "The purpose is to identify the more relevant candle extreme rather than marking every candle's
> high and low."

### High rule — compare the UPPER wicks

| Condition | I mark |
|---|---|
| Black candle wick high > Blue candle wick high | **Black candle high** (not the blue one) |
| Blue candle wick high > Black candle wick high | **Blue candle high** (not the black one) |

### Low rule — compare the LOWER wicks

| Condition | I mark |
|---|---|
| Black candle wick low < Blue candle wick low | **Black candle low** |
| Blue candle wick low < Black candle wick low | **Blue candle low** |

This rule applies on **three timeframes**:

| Timeframe | Used for |
|---|---|
| **1H** | Intermediate liquidity marked before the open |
| **5M** | Recent short-term liquidity |
| **1M** | Stage 2 — the recent high/low used in the retracement and entry sequence |

> "On 1M, I focus only on the recent high and low, using the same Blue and Black candle wick rules."

> "Always focus on the most recent valid high/low and apply the same Blue/Black wick rules."

**It does NOT apply on the 4H**, which uses actual candle extremes.

### UNRESOLVED — what "candle high" means here

<!-- TODO: ask me — this changes which price the line goes on, so it matters. -->
<!-- The rule compares WICK highs, then says to mark the "candle high" of the winner. -->
<!--   Reading A: "candle high" = that candle's wick high. Then the rule reduces to -->
<!--              "mark whichever wick is higher", and the blue/black colour adds nothing. -->
<!--   Reading B: "candle high" = that candle's BODY high (open or close, whichever is higher). -->
<!--              Then the colour matters, because body high differs from wick high. -->
<!-- The 4H hierarchy tracks "body opening" and "body closing" separately, which suggests the -->
<!-- body/wick distinction is real in my system. Not guessing which. -->

### Which candles count as "together"?

<!-- TODO: ask me — adjacent candles only, or any blue/black pair in a swing? -->
<!-- Two candles, or a group? The document says "part of the same comparison structure" -->
<!-- without defining that structure. /checktrade cannot test this as written. -->

---

## Forward-candle interaction rule

One of the most important rules in my liquidity marking system.

> "Do not mark liquidity after the market has already interacted with it in a way that makes the
> original level no longer a fresh liquidity reference."

If I identify a level but a later candle has already interacted with or taken it, I do **not** create
a fresh liquidity line from that same already-used level. It is treated as an already-tested area.

**No extra lines through a liquidity hit.** If a candle hits a liquidity area, I do not continue
creating additional lines through that same interaction.

> "One meaningful liquidity area > multiple redundant lines."

**Does "interacted with" mean a wick touch, or a body close through?** <!-- TODO: ask me -->
<!-- This is the same wick/body question as above and it decides whether a level is still live. -->

---

## Recent 5M high and low

Used for short-term liquidity. Marked with the blue/black rule.

> "The 5M high/low marking must not use old or previous market data unnecessarily. I am interested
> in the recent high and low immediately relevant to the current execution."

**How far back is "recent"?** <!-- TODO: ask me -->
<!-- A number of candles, a time window, or since a specific session line? -->
<!-- Without a number, "recent" is decided in the moment, which is where hindsight lives. -->

---

## Break of Structure (BOS)

**BOS must be confirmed by a BODY CANDLE CLOSE, not a wick.** This is stated repeatedly in my
strategy document and is the one confirmation rule I wrote in capitals.

Used on the **5M** as the priority confirmation after a liquidity hit.

- High-side: price takes a marked high, then a **5M bearish BOS with body close** indicates price
  has started breaking structure to the downside.
- Low-side: price takes a marked low, then a **5M bullish BOS with body close** indicates price has
  started breaking structure to the upside.

### 1M BOS — stage 2

The 1M sequence uses BOS twice: once **against** the 5M bias (the retracement), then once **back
with** it (the entry trigger). Both break a recent high/low identified by the blue/black wick rule.

**Does the 1M BOS also require a BODY close, like the 5M one?** <!-- TODO: ask me -->
<!-- The body-close rule is stated four times in capitals for the 5M and never once for the 1M. -->
<!-- On a 1M chart, wick-versus-body decides most of these calls. Not assuming it carries over. -->

**Structure broken relative to WHAT, exactly?** <!-- TODO: ask me -->
<!-- The document never says which level the body must close beyond. Candidates: the last 5M swing -->
<!-- low before the sweep, the most recent 5M structural low, an internal low. -->
<!-- This is the single most important undefined item in the strategy: it is the difference between -->
<!-- a testable trigger and a judgement call, and it is the trigger the whole model rests on. -->

---

## IFVG

Listed as confluence 3 and as **optional** 5M confirmation alongside BOS.

> "I am not looking for an IFVG randomly anywhere on the chart. I am specifically interested in an
> IFVG that develops after or around the liquidity interaction and supports the potential move away
> from the liquidity."

**My definition of an IFVG:** <!-- TODO: ask me -->
<!-- Never defined in the strategy document. Presumably an inverted/inversion fair value gap, -->
<!-- but I will not write the standard definition on my behalf. -->

**Minimum size to count, per instrument:** <!-- TODO: ask me -->
**Does it need to be unmitigated / CE tapped / fully inverted?** <!-- TODO: ask me -->
**If BOS and IFVG disagree, which wins?** <!-- TODO: ask me -->

---

## SMT Divergence

NASDAQ and S&P 500 are analysed together, not as independent markets.

> "When one index behaves differently from the other around a liquidity event, that difference can
> become an important confirmation factor. However, SMT should be used within the complete execution
> framework rather than as a standalone entry signal."

**My definition of SMT divergence:** <!-- TODO: ask me -->
<!-- Still undefined as a concept, separately from the other-index gate described below. -->
<!-- e.g. "NQ takes the marked high, ES fails to take its corresponding high, on the same 5M candle" -->
<!-- — but that is my guess at a standard definition, not my rule. Not writing it. -->

### The other-index gate — stage 2, condition 10

At the entry trigger I check the other index:

> "If the other index gives a BOS or IFVG, I take the entry. If there is no BOS or IFVG,
> I do not take the trade."

**This is mandatory.** No BOS and no IFVG on the other index means no trade.

<!-- BUT THIS IS NOT DIVERGENCE, AND THE DIFFERENCE MATTERS: -->
<!-- SMT divergence = the two indices behave DIFFERENTLY at a liquidity event (one takes the -->
<!--   high, the other fails to). -->
<!-- The gate above = the other index does the SAME thing (also gives a BOS or IFVG). -->
<!-- These are opposite conditions. My strategy overview lists "SMT Divergence" as confluence 4, -->
<!-- and my execution rules describe a confirmation gate. -->
<!-- TODO: ask me — are these one rule I have described two ways, or two separate requirements? -->
<!-- If two, SMT divergence needs its own definition and its own place in the trigger list. -->

**On which timeframe must the other index show its BOS or IFVG — 1M or 5M?** <!-- TODO: ask me -->
**Must it be in the same direction as my trade?** <!-- TODO: ask me -->
<!-- Presumably yes, but "presumably" is not a rule and this is a hard gate on every entry. -->

---

## Premium / discount

<!-- TODO: ask me — not mentioned anywhere in the strategy document. -->
<!-- Do I use dealing ranges and premium/discount at all, or is this not part of my model? -->
<!-- "Not part of my model" is a perfectly good answer and I should say so if that is the case. -->

---

## Chart cleanliness rules

My chart should remain clean and meaningful. I avoid:

- Marking every candle high/low
- Marking unnecessary historical 5M levels
- Creating duplicate liquidity lines
- Creating new lines after liquidity has already been hit
- Extending redundant lines through already-tested areas
- Adding unnecessary session markers
- Using the 08:00 vertical line

> "Every marked level should have a clear reason for existing."
