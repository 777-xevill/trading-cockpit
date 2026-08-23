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

**B-grade setup:** ____ % <!-- TODO: ask me — a multiple of the A+ number for the current phase, e.g. 0.5x -->

Which account balance do I calculate % from — starting balance, current balance, or high-water mark? <!-- TODO: ask me -->

<!-- ARITHMETIC, for my eyes at 22:00: -->
<!-- Evaluation, 1% = $500/trade. 6 consecutive losses = $3,000 = 6% of the account. -->
<!-- Once risk/prop-firm-rules.md is verified, check that 1% x (max consecutive losses, §4) -->
<!-- still sits inside the firm's OVERALL drawdown with the buffer I chose. If it does not, -->
<!-- either the risk % comes down or the consecutive-loss cap comes down. It cannot be both. -->

## 2. Max daily loss

**ONE FULL STOP-OUT. That is the whole rule.**

| Phase | Max daily loss | In R | In $ |
|---|---|---|---|
| Evaluation | 1 losing trade | **1.0 R** | **$500** |
| Funded | 1 losing trade | **1.0 R** | **$250** |

When the first stop is hit, the trading day is over. Not a smaller size. Not a scalp to get back to flat.
Not "the setup after this one is the real one." The platform gets closed.

The assistant stops all trade analysis for the rest of that day — see Prime Directive rule 6 in `CLAUDE.md`.
It will not negotiate, and arguing with it is itself the signal that the rule is working.

<!-- WHAT THIS RULE IMPLIES — read it so I am not surprised at 22:00: -->
<!--  * Two losses in one day is IMPOSSIBLE under this rule. The consecutive-loss rule in §4 -->
<!--    is therefore a MULTI-DAY rule: losses on consecutive days, not consecutive trades. -->
<!--  * Most losing days end after a single trade. That is the design, not a malfunction. -->
<!--  * A day can still contain several trades if none of them lose. §5 caps that. -->

Does an open winning position count toward this at unrealised value? <!-- TODO: ask me -->
Does a breakeven scratch or a partial loss (exited early, less than 1R) end the day? <!-- TODO: ask me -->

## 3. Max weekly loss

**In R:** ____ R <!-- TODO: ask me -->
**In $:** $____ <!-- TODO: ask me -->

When hit: <!-- TODO: ask me — stop until Monday? Reduce size? Mandatory review before returning? -->

## 4. Max consecutive losses before shutdown

**Number:** ____ <!-- TODO: ask me -->
**Shutdown means:** <!-- TODO: ask me — rest of day, or rest of week? -->
**Does a breakeven scratch reset the streak?** <!-- TODO: ask me -->

## 5. Max trades per day

**Number:** ____ <!-- TODO: ask me -->
Must match `strategy/00-core-rules.md` section 3. If the two ever disagree, this file wins and the other gets fixed.

## 6. Max concurrent positions

**Number:** ____ <!-- TODO: ask me -->
**Max total open risk at any moment:** ____ R <!-- TODO: ask me -->

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

**Number:** ____ : 1 <!-- TODO: ask me -->
Measured to the **first** target, not the dream target.
If the nearest logical target does not pay this, the trade does not exist.

## 11. Recovery / size-up rules

**After a losing day, next day's risk per trade is:** <!-- TODO: ask me -->
**After hitting a milestone, am I allowed to increase size?** <!-- TODO: ask me -->
**Revenge-size rule:** never increase size to make back a loss. <!-- TODO: ask me — confirm as an absolute -->

---

## Enforcement

- These numbers are changed only in `/review`, between sessions, in writing.
- A rule changed mid-session does not exist. The old number stands until tomorrow.
- Every breach gets logged in `psychology/rules-i-actually-break.md` with its cost in R. No exceptions, especially not the ones that made money.
