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

## UNIVERSAL DEFINITIONS

**Given 2026-08-26. These override every looser wording elsewhere in this repo.**
Wherever this strategy says High, Low, Recent High, Recent Low, Candle High, Candle Low,
1M/5M/1H High or Low, the following always apply:

| Term | Definition |
|---|---|
| **High / Low** | The **wick extreme**. Never the body. |
| **Candle High** | Highest point of the upper wick |
| **Candle Low** | Lowest point of the lower wick |
| **Blue / Black "together"** | **Consecutive, adjacent** candles of **different** colour |
| **Recent** | The **most recent valid structure**, not a fixed candle count |
| **Liquidity hit** | **Wick touch** - a body close is NOT required |
| **BOS** | **Body close beyond** the structural level |

**Liquidity hit and BOS are two different events on purpose.** A wick reaching a level *takes*
that liquidity. A body closing beyond a level *breaks* structure. One is the sweep, the other is
the confirmation. Do not collapse them.

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

### 4H lookback - active structure, not a candle count

Resolved 2026-08-26.

> "I mark the relevant visible 4H highs and lows from the current active market structure.
> I do not use an arbitrary fixed number of candles such as the last 5, 10, or 20 candles."

**A 4H level stays valid until price interacts with it** per the forward-candle rule - i.e. until a
wick reaches it. Once hit, it is no longer fresh and I do not draw a duplicate line from it.

<!-- NOTE FOR THE INDICATOR: "visible, from current active structure" is a judgement a human -->
<!-- makes by looking at the chart. It has no mechanical definition, so 4H levels stay HAND-DRAWN. -->
<!-- That is a legitimate outcome, not a gap - but it means 4H marking cannot be automated. -->
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

### "Candle high" means the WICK extreme

Resolved 2026-08-26.

> "Whenever I say candle high or candle low, I always mean the wick extreme, not the candle body."

So in the tables above, "Black candle high" means that candle's **upper wick tip**.

### "Together" means CONSECUTIVE candles of different colour

Resolved 2026-08-26.

> "The Blue/Black rule applies when a Blue candle and a Black candle are adjacent/consecutive
> candles in the same timeframe."

Adjacent only. Not any pair in a swing, not a group.

| Pair | Rule applies? |
|---|---|
| Blue then Black | **Yes** |
| Black then Blue | **Yes** |
| Blue then Blue | No |
| Black then Black | No |

### What these two definitions imply - CHECK THIS

<!-- Not an invention. It is what my own two definitions produce when combined, and it matters -->
<!-- because it is what the Pine indicator has to implement. -->
<!-- If candle high = wick extreme, and I mark whichever of the two candles has the higher wick, -->
<!-- then within a qualifying pair the COLOUR selects nothing. Both cases reduce to: -->
<!--     mark the higher of the two upper wicks, and the lower of the two lower wicks. -->
<!-- The colour still does real work, but at the previous step: it acts as a FILTER deciding -->
<!-- WHICH PAIRS create a level at all. Blue+Blue and Black+Black pairs create nothing. -->
<!-- TODO: ask me - confirm that reading. If the colour is meant to select the candle even when -->
<!-- its wick is lower, then one of the two definitions above needs rewording. -->

**Working statement, pending that confirmation:**

1. Take each pair of adjacent candles.
2. If they are the same colour, no level is created.
3. If they are different colours, mark the **higher upper wick** as the high and the
   **lower lower wick** as the low.

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

### "Interacted with" means a WICK TOUCH

Resolved 2026-08-26.

> "A liquidity level is considered interacted with when a future candle's wick reaches or passes
> through the marked liquidity level. A body close is not required for the level to be considered hit."

| Event | Meaning |
|---|---|
| **Wick touch** | Liquidity **interacted with / hit**. Level is no longer fresh. |
| **Body close beyond** | Liquidity **fully broken** - structure confirmation, i.e. BOS |

**These are two different concepts and must not be merged.**

Once a forward candle has wicked into a marked level, that level is no longer a fresh untouched
liquidity reference, and I do not create a duplicate line from the same already-hit area.

---

## Recent 5M high and low

Used for short-term liquidity. Marked with the blue/black rule.

> "The 5M high/low marking must not use old or previous market data unnecessarily. I am interested
> in the recent high and low immediately relevant to the current execution."

### "Recent" means the latest valid structure - not a candle count

Resolved 2026-08-26.

> "When I say Recent High or Recent Low, I always mean the most recent valid high or low created
> by the latest relevant Blue/Black candle structure. I do not use an arbitrary number of previous
> candles."

> "Always focus on the latest valid structure immediately before the current price action."

For 5M and 1M execution, old highs and lows are **ignored** unless they are still separately marked
as a higher-timeframe liquidity level.

**In practice this is codeable:** scan backwards for the most recent adjacent different-colour pair;
that pair supplies the recent high and the recent low.

<!-- TODO: ask me - must the recent high and the recent low come from the SAME pair, or is each -->
<!-- taken from the most recent pair that produced one? Usually the same pair gives both, but -->
<!-- after a BOS the structure is re-identified and they can diverge. -->

---

## Break of Structure (BOS)

**BOS must be confirmed by a FULL BODY CANDLE CLOSE, not a wick — on EVERY timeframe.**

This is the one confirmation rule I wrote in capitals, and as of 2026-08-26 it is universal:
the 5M BOS and both 1M BOS legs are all body-close only. There is no timeframe in this model
where a wick through a level counts as a break of structure.

Used on the **5M** as the priority confirmation after a liquidity hit.

- High-side: price takes a marked high, then a **5M bearish BOS with body close** indicates price
  has started breaking structure to the downside.
- Low-side: price takes a marked low, then a **5M bullish BOS with body close** indicates price has
  started breaking structure to the upside.

### 1M BOS — stage 2

The 1M sequence uses BOS twice: once **against** the 5M bias (the retracement), then once **back
with** it (the entry trigger). Both break a recent high/low identified by the blue/black wick rule.

**Both 1M BOS legs require a FULL BODY CLOSE.** Confirmed 2026-08-26. Same standard as the 5M.

### BOS is measured against the MOST RECENT VALID STRUCTURE

Resolved 2026-08-26. This was the load-bearing gap; it is now closed.

> "The BOS level is always the most recent valid structural high or low being monitored immediately
> before the break."

> "The BOS level should always come from the latest relevant structure, not an old unrelated high or low."

| Direction | Condition |
|---|---|
| **Bullish BOS** | A candle's **closing price** is **above** the most recent valid structural high |
| **Bearish BOS** | A candle's **closing price** is **below** the most recent valid structural low |

The structural high/low is the one produced by the latest qualifying blue/black pair, per the
"Recent" definition above.

**Wick through level = no BOS. Body close beyond level = BOS.** On every timeframe.

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
