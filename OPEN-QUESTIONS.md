# Open Questions

**This is the interview queue. It is not finished.**

Rules for working through this file:

- **Ask the next unanswered question at the top of every session**, before anything else, unless I say "not now" or I am mid-session and about to trade.
- **One question at a time.** Wait for the answer.
- If my answer is vague or a range, push back once and make me give a single number.
- If my answer contradicts a rule already written, stop and point at the contradiction before writing anything.
- Write the answer into the correct file immediately. Do not batch.
- Tick the box here, and commit.

---

## ANSWERED SO FAR

- [x] Risk per trade — **1% evaluation / 0.5% funded** → `risk/risk-rules.md` §1
- [x] Max daily loss — **1 loss / 1R** → §2
- [x] Max weekly loss — **3 losing days / 3R** → §3
- [x] Max trades per day — **2** → §5
- [x] Minimum R:R — **1:2** → §10
- [x] Max concurrent positions — **1** → §6
- [x] Max total open risk — **1.0 R** (follows from one position at 1R) → §6
- [x] B-grade risk — **same as A+**, no reduction → §1
- [x] Risk basis — **starting balance, $50,000, fixed** → §1
- [x] Unrealised P&L vs daily limit — moot under one-position rule; firm's equity measure is a prop-firm TODO → §2
- [x] Partial/early exits — **day ends at $500 of losses cumulative**, not at one trade → §2, §5
- [x] Wins do **not** extend the loss budget — worst day −$500, best day +$2,000 → §2
- [x] Breakeven scratches — **free, do not use a trade slot** (loophole flagged in file) → §5
- [x] 2 trades is a **cap, not a quota** — stopping after one winner is always allowed → §5
- [x] Moving stops — **never widen, ever; stop is a live broker order** → §8
- [x] Adding to positions — **never, winners or losers** → §9
- [x] Correlation — **NQ/ES/US100 are one instrument**; no same-direction re-entry after a loss → §7
- [x] Consecutive losses — **no separate streak rule**, §3 weekly limit covers it → §4

---

## NEXT UP — RISK (finish this section first)

- [ ] **What exactly counts as a scratch?** *(skipped 2026-08-24, ask me again)* — blocks reliable trade counting → §5
- [ ] Does a losing day of less than 1R count toward the 3-day weekly limit? → §3
- [ ] Does the correlation re-entry bar apply after a WIN as well as a loss? → §7
- [ ] Is XAU/USD a separate bucket from the index group, in my experience? → §7
- [ ] When exactly may a stop move to breakeven? A single objective trigger → §8
- [ ] Trailing stop rule, if any → §8
- [ ] Do I take partial exits (scale out), or all-out at one target? → §9 / setup files
- [ ] After a losing day, does the next day's risk change? → §11
- [ ] Is 2.0R the minimum for both a-plus and b-grade, or is a-plus higher? → §10

## THEN — PROP FIRM (30 unverified values)

**None of these get filled from memory. Open the FundedNext site and the account dashboard.**
The single most important one is the minimum-trading-days rule, because it determines whether a
fast pass is even legal. → `risk/prop-firm-rules.md`

- [ ] Profit target (%)
- [ ] Max daily drawdown — % and $, and whether it is measured on balance or equity
- [ ] Max overall drawdown — % and $
- [ ] Drawdown type — static or trailing; if trailing, does it stop at initial balance?
- [ ] Daily reset time, converted to Dhaka GMT+6
- [ ] **Minimum trading days**
- [ ] Consistency rule
- [ ] News restriction
- [ ] Weekend / overnight holding
- [ ] Which instruments are actually offered — are NQ/ES futures available, or only CFDs?
- [ ] Buffer I want between the firm's daily drawdown and my own 1R limit
- [ ] Then: **profit target ÷ 2R = the real number of net winners needed to pass.** Write that number down.

## THEN — SIZING (verify with broker, not from memory)

- [ ] NQ / MNQ tick value → `risk/sizing.md`
- [ ] ES / MES tick value
- [ ] XAU/USD contract size and value per point — **brokers disagree; a wrong value here is a 10x sizing error**
- [ ] US100 contract size and value per point
- [ ] Commission and typical spread per instrument
- [ ] Do I subtract costs before calculating R?
- [ ] Hard cap on contracts/lots per instrument

## THEN — CORE RULES

- [ ] What must be true before I am allowed to look for entries → `strategy/00-core-rules.md` §1
- [ ] Which sessions I trade and never trade, in Dhaka time → §2, `strategy/02-session-plan.md`
- [ ] Earliest entry / last entry / hard flat time, Dhaka time → session plan
- [ ] Fatigue rule — minimum sleep, latest hour I may open a position → session plan
- [ ] News blackout window in minutes, before and after → session plan
- [ ] What "A+" means, in one sentence → §4
- [ ] What automatically disqualifies a trade → §5

## THEN — MARKET STRUCTURE (my definitions, not textbook ICT)

- [ ] Timeframes: HTF bias / intermediate / entry → `strategy/01-market-structure.md`
- [ ] Liquidity sweep — my definition, and how I confirm it on a closed candle
- [ ] MSS — body close or wick? which timeframe?
- [ ] Order block — my definition, wick or body, when it is dead
- [ ] FVG — minimum size per instrument, mitigation requirement
- [ ] Premium/discount — which dealing range, and is a wrong-half entry refused?
- [ ] The levels I mark every single day

## THEN — SETUPS

- [ ] Name of the A+ setup, and its numbered trigger conditions → `strategy/setups/a-plus.md`
- [ ] Entry mechanic, stop rule, target logic for A+
- [ ] Name and triggers for the B-grade setup → `strategy/setups/b-grade.md`
- [ ] Am I allowed to take B-grade at all after a loss?
- [ ] **The no-trade conditions list — currently empty** → `strategy/setups/no-trade-conditions.md`
- [ ] Bias invalidation, setup invalidation, trade invalidation → `strategy/invalidation.md`
- [ ] Re-entry rules after a stop-out

## THEN — PSYCHOLOGY

- [ ] Cooldown length after a loss, in minutes → `psychology/post-loss-protocol.md`
- [ ] Which honesty-question answers are auto-shutdown vs. warning
- [ ] Conditions required before the next trade is allowed
- [ ] Cooldown after a win; do I stop at a daily profit target?
- [ ] What actually tilts me — specific, not "losing" → `psychology/tilt-triggers.md`
- [ ] What changes in my behaviour after midnight Dhaka time

---

## STANDING RULE

An unanswered question above is **not** a gap for the assistant to fill with a sensible default.
Where a rule is blank, `/checktrade` returns `INCOMPLETE` and names the missing rule.
A blank rule is honest. An invented rule gets me stopped out on someone else's logic.
