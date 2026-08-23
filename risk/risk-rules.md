# Risk Rules

**This file outranks every file in `strategy/`.** A perfect setup that breaks a rule here is not a trade.
`/checktrade` reads this file first, every time.

<!-- Every value below is a SINGLE NUMBER. Ranges are how rules get broken: -->
<!-- "1-2%" always becomes 2% on the trade I feel best about, which is the one I feel best about because I am tilted. -->

---

## 1. Risk per trade

**A+ setup:** ____ % of account <!-- TODO: ask me -->
**B-grade setup:** ____ % of account <!-- TODO: ask me -->
**In dollars on the $50K challenge:** $____ <!-- derived, filled once the % is set -->

Which account balance do I calculate % from — starting balance, current balance, or high-water mark? <!-- TODO: ask me -->

## 2. Max daily loss

**In R:** ____ R <!-- TODO: ask me -->
**In $:** $____ <!-- TODO: ask me -->
**Whichever comes first.**

When this is hit: I close the platform. Not "one more small one." Not "a scalp to get back to flat."
The assistant stops all trade analysis for the day — see Prime Directive rule 6 in `CLAUDE.md`.

Does an open winning position count toward this at unrealised value? <!-- TODO: ask me -->

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
