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
- [x] Max trades per day — **1** (changed from 2 on 2026-08-24) → §5
- [x] Minimum R:R — **1:2** → §10
- [x] Max concurrent positions — **1** → §6
- [x] Strategy document received 2026-08-24 — filed into `strategy/` (see git log)
- [x] 1M entry sequence received 2026-08-26 — stage 2 of `setups/a-plus.md`
- [x] Entry TRIGGER — **second 1M BOS with the 5M bias + other index confirms** → `a-plus.md`
- [x] Other-index gate — **mandatory**: no BOS or IFVG on the other index = no trade → `a-plus.md`
- [x] BOS confirmation — **full body close on EVERY timeframe** (5M and both 1M legs) → `01-market-structure.md`
- [x] **Universal definitions given 2026-08-26** → `01-market-structure.md`
- [x] High / Low — **wick extreme, never the body**
- [x] "Together" — **consecutive adjacent candles of different colour**
- [x] "Recent" — **latest valid structure**, not a candle count
- [x] Liquidity hit — **wick touch**; body close beyond = BOS. Two different events.
- [x] BOS level — **most recent valid structural high/low immediately before the break**
- [x] 4H lookback — **visible levels from active structure**; stays hand-drawn (no mechanical rule)
- [x] Max total open risk — **1.0 R** (follows from one position at 1R) → §6
- [x] B-grade risk — **same as A+**, no reduction → §1
- [x] Risk basis — **starting balance, $50,000, fixed** → §1
- [x] Unrealised P&L vs daily limit — moot under one-position rule; firm's equity measure is a prop-firm TODO → §2
- [x] Partial/early exits — **day ends at $500 of losses cumulative**, not at one trade → §2, §5
- [x] Wins do **not** extend the loss budget — worst day −$500, best day +$2,000 → §2
- [x] Breakeven scratches — **free, do not use a trade slot** (loophole flagged in file) → §5
- [x] The cap is a **ceiling, not a quota** — a no-trade day is a correct day → §5
- [x] Moving stops — **never widen, ever; stop is a live broker order** → §8
- [x] Adding to positions — **never, winners or losers** → §9
- [x] Correlation — **NQ/ES/US100 are one instrument**; sequential re-entry now moot under the 1-trade cap → §7
- [x] Consecutive losses — **no separate streak rule**, §3 weekly limit covers it → §4
- [x] Recovery sizing — **risk never changes**, $500 always; never size up to recover → §11
- [x] Breakeven stop — **none. The stop never moves at all** → §8
- [x] Trailing stop — **none**, for the same reason → §8
- [x] Partial exits — **none. All out at stop or target** (reversed same session) → §9

---

## NEXT UP — RISK (finish this section first)


- [ ] **What exactly counts as a scratch?** *(skipped 2026-08-24, ask me again)* — now the ONLY route to a second entry, so this is the highest-priority open item → §5
- [ ] Does a losing day of less than 1R count toward the 3-day weekly limit? → §3
- [ ] Is XAU/USD a separate bucket from the index group, in my experience? → §7
- [ ] Is 1.5R the minimum for both a-plus and b-grade, or is a-plus higher? → §10

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

## BLOCKING — THE STRATEGY DOCUMENT DID NOT INCLUDE THESE

**These make the difference between a described model and a tradeable one.**
`/checktrade` cannot produce a verdict without them: it cannot size a position or calculate R:R.
Answer these before anything else in this file.

- [ ] **Stop placement rule** — must produce a single price → `strategy/setups/a-plus.md`
      *Beyond the swept wick? Beyond the swing the BOS broke? Beyond the IFVG? Name one.*
- [ ] **Entry FILL method** — the trigger is now defined, the fill price is not → `a-plus.md`
      *Market on the close of the 1M BOS candle? Limit at the 1M IFVG? Limit at the retracement low?*
      *Each gives a different entry price, so a different stop distance, size and R:R.*
- [ ] **How deep may the 1M retracement go before the idea is dead?** → `a-plus.md`
      *Stage 2 waits for price to move against the 5M bias. Nothing says when it has gone too far.*
- [ ] **Target logic** — which liquidity, specifically → `a-plus.md`
      *"Opposite-side liquidity" is stated; which level in the hierarchy is not.*
- [ ] **Last permitted entry time** — is the window 09:40–09:45, or does 09:40 only start it? → `02-session-plan.md`

## THEN — STRATEGY DEFINITIONS

- [ ] Confirm: within a qualifying blue/black pair, does colour select anything, or does it
      reduce to "mark the higher wick"? (See the derivation in `01-market-structure.md`.)
- [ ] Must the recent high and recent low come from the SAME blue/black pair?
- [ ] Is condition 3 ("reaction") still separate from condition 4 (BOS), or redundant now?
- [ ] Do I want BOS markers on the indicator? (Off by default — marks the trigger, not the prep.)

- [ ] **IFVG** — never defined anywhere → `01-market-structure.md`
- [ ] **SMT divergence vs the other-index gate — one rule or two?** → `01-market-structure.md`
      *Confluence 4 is "SMT Divergence" (indices behave differently). Stage 2 condition 10 is a
      confirmation gate (other index does the same thing). These are opposite conditions.*
- [ ] Which timeframe must the other index's BOS/IFVG appear on — 1M or 5M?
- [ ] Must the other index's confirmation be in the same direction as my trade?
- [ ] Is there a time limit on the four-step 1M sequence?
- [ ] How many of the four confluences must align to take a trade?
- [ ] Does the liquidity hierarchy rank importance, or just group levels?
- [ ] Time limit between the sweep and BOS confirmation before the idea is dead
- [ ] NQ and ES both signal in the same window — which one do I take? (One trade per day, §5)
- [ ] Futures (NQ/ES) or CFDs?
- [ ] Is a pre-open HTF bias required, or is the model purely reactive?
- [ ] Premium/discount — part of my model at all? ("No" is a fine answer)
- [ ] Is there a B-grade setup at all, or only this one? → `setups/b-grade.md`
- [ ] What does "A+" mean in one sentence → `00-core-rules.md` §4
- [ ] Am I permitted to exit early on structure, and on what signal? → `a-plus.md`
- [ ] Confirm: never execute in London or Asia
- [ ] Confirm: XAU/USD and US100 are genuinely out of scope
- [ ] Hard flat time — do I ever hold past the session?
- [ ] News rules — releases, blackout window, where I check → `02-session-plan.md`
- [ ] Do I still want a sleep minimum, given the window is 19:40 Dhaka not 01:00?

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
