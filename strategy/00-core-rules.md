# Core Rules — Non-Negotiable

<!-- These are the rules that do not bend. Everything else in strategy/ is detail. -->
<!-- Nothing here was written by the assistant. Every line is mine. -->

---

## 1. What must be true before I am allowed to look for entries

From my strategy document, 2026-08-24:

1. TradingView timezone confirmed as **UTC-4 New York**.
2. Session vertical lines placed: **03:00**, **09:30**, **18:00**. Never 08:00.
3. **4H** liquidity marked (actual candle extremes, plus body open/close).
4. **1H** liquidity marked using the blue/black wick rule.
5. **Asia High/Low** marked (18:00 -> 03:00).
6. **London High/Low** marked (03:00 -> 08:00).
7. Ready to identify **recent 5M High/Low**.
8. The 09:30 open has passed and **at least 10 minutes of manipulation has been allowed to develop**.
9. `/premarket` has been run and today's journal file exists.

Only then do I begin searching for execution, at **09:40 UTC-4 / 19:40 Dhaka**.

<!-- TODO: ask me — is a stated HTF bias required before the open, or is this model purely -->
<!-- reactive to whichever side of liquidity gets swept? The strategy document reads as reactive, -->
<!-- but it never says so, and /premarket currently asks me for a bias. -->

---

## 2. Instruments

**NASDAQ and S&P 500 only.**

> "I trade only: NASDAQ, S&P 500."

**Not traded:** XAU/USD, US100. Their files are kept but marked out of scope.

<!-- The two indices are analysed TOGETHER for SMT, not as independent markets. -->
<!-- Under risk/risk-rules.md §7 they are one instrument for risk purposes, and §5 permits -->
<!-- one trade per day, so watching both never means trading both. -->

---

## 2b. Sessions I trade — and sessions I never trade

**I trade: the New York open only.**

| Session | UTC-4 | Dhaka | Trade it? |
|---|---|---|---|
| Asia | 18:00 -> 03:00 | 04:00 -> 13:00 | Marked for liquidity. Not traded. |
| London | 03:00 -> 08:00 | 13:00 -> 18:00 | Marked for liquidity. Not traded. |
| **New York** | **09:40-09:45** | **19:40-19:45** | **Yes — the only execution window.** |

<!-- TODO: ask me — confirm I never execute in London or Asia. The strategy document only -->
<!-- describes a New York model; it never says the others are forbidden. Silence is not a rule. -->

## 3. Maximum trades per day

<!-- TODO: ask me -->
<!-- One number. Not "2 or 3". -->

**Hard cap:** **1** trade per day, win or lose. See `risk/risk-rules.md` §5 — that file is authoritative.

**Does a scratch/breakeven trade count against the cap?** No — scratches are free.
The threshold for what counts as a scratch is still undefined. See `risk/risk-rules.md` §5.

---

## 4. What "A+" means to me — in one sentence

<!-- TODO: ask me -->
<!-- The strategy document describes ONE setup. If that setup is A+ by definition, say so and -->
<!-- b-grade gets deleted. If there is a lower grade, it needs its own trigger conditions. -->
<!-- Right now strategy/setups/b-grade.md is an empty template with no content of mine in it. -->

>

---

## 5. What automatically disqualifies a trade

From the strategy document:

1. No marked liquidity has been hit.
2. BOS confirmed by a **wick close** rather than a **body close**.
3. The liquidity level was already interacted with by a forward candle — it is no longer fresh.
4. Time is outside the permitted execution window.
5. Entering at the 09:30 open without allowing 10-15 minutes of manipulation to develop.

<!-- TODO: ask me — what else? News, spread, gap size, my own state. -->
<!-- See strategy/setups/no-trade-conditions.md, which is still empty. -->

---

## 6. Rule-change protocol

Rules are changed in `/review`, never during a live session. If I want to change a rule mid-session, the answer is no.
The changed rule takes effect the **next** trading day, not the current one.
