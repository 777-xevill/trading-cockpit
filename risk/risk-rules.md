# Risk Rules

**This file outranks every file in `strategy/`.** A perfect setup that breaks a rule here is not a trade.
`/checktrade` reads this file first, every time.

<!-- Every value below is a SINGLE NUMBER. Ranges are how rules get broken: -->
<!-- "1-2%" always becomes 2% on the trade I feel best about, which is the one I feel best about because I am tilted. -->

---

## 1. Risk per trade

**Risk depends on the phase of the account. One number per phase, never a range.**

| Phase | Risk per A+ trade | 1R on $50,000 |
|---|---|---|
| Evaluation / challenge | **1.0 %** | **$500** |
| Funded | **0.5 %** | **$250** |

**B-grade setup:** **same as A+** — 1.0 % evaluation, 0.5 % funded. No size reduction.

<!-- CONSEQUENCE, decided 2026-08-24: with identical risk, the A+/B-grade split does NO RISK WORK. -->
<!-- Its only remaining function is statistical: scripts/stats.py breaks expectancy down by setup_tag, -->
<!-- so the grade is how I find out whether B-grade setups actually make money. -->
<!-- That only works if I tag honestly AFTER the fact. Relabelling a B-grade as A+ because it won -->
<!-- destroys the only reason the two categories still exist. -->
<!-- Note also: under §2 a B-grade loss ends the trading day exactly as an A+ loss does. -->

**Percentages are calculated from the STARTING balance — $50,000 — always.**

1R is a fixed dollar amount for the entire challenge. It does not move with the account.

| Phase | Basis | 1R |
|---|---|---|
| Evaluation | $50,000 starting balance | **$500, fixed** |
| Funded | $50,000 starting balance | **$250, fixed** |

No recalculation before a session. No compounding. If the balance is $46,800 on a Thursday, 1R is
still $500. The number on the sizing calculation never changes, which removes one whole category of
arithmetic error at 22:00.

<!-- ACCEPTED TRADE-OFF: in a drawdown, a fixed $500 is a larger share of what is left. -->
<!-- Bounded by §3: the worst week is -3R = -$1,500, so the account cannot drift far enough -->
<!-- for the fixed number to become dangerous before the weekly rule stops me. -->

<!-- ARITHMETIC, for my eyes at 22:00: -->
<!-- Evaluation, 1% = $500/trade. 6 consecutive losses = $3,000 = 6% of the account. -->
<!-- Once risk/prop-firm-rules.md is verified, check that 1% x (max consecutive losses, §4) -->
<!-- still sits inside the firm's OVERALL drawdown with the buffer I chose. If it does not, -->
<!-- either the risk % comes down or the consecutive-loss cap comes down. It cannot be both. -->

## 2. Max daily loss

**$500 OF LOSSES IN A DAY. The limit is dollars, not trades.**

| Phase | Max daily loss | In R |
|---|---|---|
| Evaluation | **$500** | 1.0 R |
| Funded | **$250** | 1.0 R |

The day ends the moment losses reach that figure — whether that is one full stop-out, or two partial
exits that add up to it. It also ends when the 2-trade cap in §5 is used, whichever comes first.

**Worked examples (evaluation, 1R = $500):**

| Trade 1 | Remaining budget | Trade 2 allowed? |
|---|---|---|
| Full stop, −$500 | $0 | **No. Day over.** |
| Early exit, −$180 | $320 | Yes, but stop must risk ≤ $320 |
| Breakeven, $0 | $500 | Yes, full size |
| Winner, +$1,000 | see note below | Yes |

**If trade 2 is taken with a reduced budget, the position is sized to that reduced number** — see
`risk/sizing.md`. A $320 budget does not permit a $500 stop at full size. That is the whole point.

When the limit is hit: the platform gets closed. Not a smaller size. Not a scalp to get back to flat.
The assistant stops all trade analysis for the rest of that day — Prime Directive rule 6 in `CLAUDE.md`.
Arguing with it is itself the signal that the rule is working.

**Does a winning trade increase the day's remaining loss budget? NO.**

The loss budget is $500 per day and it never grows. Profit does not become risk.

| Trade 1 | Trade 2 may risk | Day ends at |
|---|---|---|
| +$1,000 | $500 | +$500 net if trade 2 stops out |
| +$300 | $500 | −$200 net if trade 2 stops out |
| $0 | $500 | −$500 net if trade 2 stops out |
| −$180 | $320 | −$500 net if trade 2 stops out |
| −$500 | nothing, day over | −$500 |

**The worst possible day is −$500. The best is +$2,000.** Both are now hard numbers, not intentions.

<!-- The rejected version, 2026-08-24: letting the day run to −$500 NET, so a +$1,000 morning -->
<!-- would permit trade 2 to lose $1,500. That is the "house money" rule and it is how a green -->
<!-- day becomes a red one. Rejected deliberately. Do not reintroduce it mid-session. -->

**Does an open position count toward this at unrealised value?**
Resolved by structure, not by preference: §6 allows one position at a time and the stop sits inside
the remaining budget, so unrealised loss cannot exceed it.
<!-- This still matters for the FIRM's limit if FundedNext measures daily drawdown on EQUITY -->
<!-- rather than closing balance. That is a TODO in risk/prop-firm-rules.md, not a decision for me. -->

## 3. Max weekly loss

**THREE LOSING DAYS. The week is then over.**

| Phase | Max weekly loss | In R | In $ |
|---|---|---|---|
| Evaluation | 3 losing days | **3.0 R** | **$1,500** |
| Funded | 3 losing days | **3.0 R** | **$750** |

Because §2 allows only one loss per day, three losses = three separate days. They do not have to be consecutive.

When hit: **no trading until Monday.** Not reduced size. Not "just watching with a small one on."
Before returning on Monday I must run `/review` and write down what the three losses had in common.

<!-- Worst possible week under §2 + §3 is -3R = -3% of the account in evaluation. -->
<!-- Cross-check this against the firm's OVERALL drawdown once prop-firm-rules.md is verified. -->

<!-- TODO: ask me — does a losing day where I exited early for less than 1R count as a losing day? -->

## 4. Max consecutive losses before shutdown

**Number:** ____ <!-- TODO: ask me -->
**Shutdown means:** <!-- TODO: ask me — rest of day, or rest of week? -->
**Does a breakeven scratch reset the streak?** <!-- TODO: ask me -->

## 5. Max trades per day

**TWO. Hard cap, win or lose.**

| Phase | Max trades per day |
|---|---|
| Evaluation | **2** |
| Funded | **2** <!-- TODO: ask me — confirm this stays 2 once funded --> |

The day ends at **two trades or $500 of losses, whichever comes first** (§2).

| Trade 1 result | Day continues? |
|---|---|
| Full stop, −$500 | **No.** Loss budget exhausted. |
| Partial loss, −$180 | Yes — trade 2 permitted, sized to the remaining $320 |
| Breakeven | Yes — trade 2 permitted at full size |
| Winner | Yes — trade 2 permitted |

After trade 2 closes, the day is over regardless of outcome.

Must match `strategy/00-core-rules.md` §3. If the two ever disagree, this file wins and the other gets fixed.

<!-- TODO: ask me — does a breakeven scratch count against the 2? -->
<!-- TODO: ask me — if trade 1 wins, am I allowed to stop for the day instead of taking trade 2? -->

## 6. Max concurrent positions

**ONE. Never two open at the same time.**

| Field | Value |
|---|---|
| Max concurrent positions | **1** |
| Max total open risk at any moment | **1.0 R** ($500 evaluation / $250 funded) |

Trade 2 may only be opened after trade 1 is **closed**. Not "nearly closed", not "at breakeven with
a runner on". Closed. Flat. Then, and only then, does a second trade exist as a possibility.

This is what makes §2 enforceable rather than merely intended: with one position at a time, the
day's loss is the sum of at most two closed trades, and trade 2 is sized to whatever budget trade 1
left behind. **Size trade 2 to the remaining budget and the $500 ceiling cannot be breached.**
The two ways to breach it are both deliberate: sizing trade 2 at full risk when the budget is
already partly spent, or re-entering after the budget is gone.

<!-- The alternative I rejected on 2026-08-24: two positions at 0.5R each. -->
<!-- Rejected because half-size sizing under pressure at 22:00 is where arithmetic errors live, -->
<!-- and because it halves the payout on the one good setup to fund a second, worse one. -->

## 7. Correlation rule

**NQ and US100 are effectively the same instrument.** A long NQ plus a long US100 is one trade at double size, dressed up as two ideas. It is the single fastest way to breach a daily drawdown while believing I am diversified.

- Never hold NQ and US100 at the same time in the same direction. <!-- TODO: ask me — confirm, and decide the opposite-direction case -->
- ES and NQ: <!-- TODO: ask me — allowed together? at what combined risk? -->
- XAU/USD vs indices: <!-- TODO: ask me -->
- If two correlated positions are open, total risk counts as: <!-- TODO: ask me — sum, or worst case? -->

`/checktrade` blocks a correlated second entry.

## 8. Moving stops

**Am I allowed to move a stop further away from entry?** <!-- TODO: ask me -->
<!-- The correct answer is almost always "never". Say it explicitly so I cannot pretend it was ambiguous at 22:40. -->

**When may I move a stop to breakeven?** <!-- TODO: ask me — a specific trigger, e.g. "at +1R", not "when it looks safe". -->

**Trailing rule, if any:** <!-- TODO: ask me -->

## 9. Adding to positions

**Am I allowed to add to a winner?** <!-- TODO: ask me -->
**Am I allowed to add to a loser?** <!-- TODO: ask me -->
**If adding is allowed: max total risk after the add, and where the combined stop goes.** <!-- TODO: ask me -->

## 10. Minimum R:R

**1:2 — risk 1 to make 2. Minimum target is 2.0R.**

Measured to the **first** target, not the dream target.
If the nearest logical target does not pay 2.0R, the trade does not exist. This is a hard filter, not a preference.

| Phase | 1R | Minimum target |
|---|---|---|
| Evaluation | $500 | **$1,000** |
| Funded | $250 | **$500** |

**Stop distance is set by structure first, then size is solved from it** — never the reverse.
Never shrink a stop to manufacture a 2R target. That is how a 2R trade becomes a 0.4R trade with four times the size.

<!-- WHAT THIS MEANS FOR THE CHALLENGE MATH: -->
<!--   Best possible day  = 2 winners = +4R = +4% -->
<!--   Worst possible day = 1 loser   = -1R = -1% -->
<!--   Worst possible week = -3R = -3% (§3) -->
<!--   Break-even win rate at 2R with no costs = 33.3%. Above that, the edge is positive. -->
<!-- TODO: verify the profit target on FundedNext, then divide by 2R to get the minimum -->
<!-- number of NET winning trades needed to pass. That number is the real plan, not "2 trades". -->

<!-- TODO: ask me — is 2.0R the minimum for BOTH a-plus and b-grade, or is a-plus higher? -->

## 11. Recovery / size-up rules

**After a losing day, next day's risk per trade is:** <!-- TODO: ask me -->
**After hitting a milestone, am I allowed to increase size?** <!-- TODO: ask me -->
**Revenge-size rule:** never increase size to make back a loss. <!-- TODO: ask me — confirm as an absolute -->

---

## Enforcement

- These numbers are changed only in `/review`, between sessions, in writing.
- A rule changed mid-session does not exist. The old number stands until tomorrow.
- Every breach gets logged in `psychology/rules-i-actually-break.md` with its cost in R. No exceptions, especially not the ones that made money.
