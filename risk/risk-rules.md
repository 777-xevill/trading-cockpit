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

**Does a breakeven scratch count against the 2? NO. Scratches are free.**

A trade closed at breakeven does not use a trade slot. I may enter again.
The $500 loss budget in §2 is untouched by a scratch, because a scratch costs nothing.

<!-- KNOWN LOOPHOLE, written down deliberately so I cannot pretend it surprised me: -->
<!-- This is the most stretchable rule in the file. The failure mode is that "scratch" grows: -->
<!-- −$40 gets called a scratch to buy a third entry, then −$90, and the 2-trade cap stops existing. -->
<!-- If /review ever shows days with more than 2 entries, this rule is the reason and it gets cut. -->

**What exactly counts as a scratch? UNDEFINED — skipped on 2026-08-24. Ask me again.**

Until it is defined, `/checktrade` cannot count trades reliably: it does not know whether the
previous trade used a slot. It reports `INCOMPLETE: scratch threshold undefined` when the day's
first trade closed at a small loss and a second is proposed. It does not pick a number for me.
<!-- Commission and spread mean a trade exited at the entry price is never exactly $0.00. -->
<!-- On NQ a round turn is a few dollars, so "flat" is realistically a small negative. -->
<!-- Without a boundary this rule either never triggers, or triggers whenever I want it to. -->
<!-- Not inventing the number. Options I have to choose between: exact $0.00 only; -->
<!-- costs-only (fees and spread, no adverse move); or a fixed dollar band I name. -->

**Two is a CAP, not a quota.** Nothing obliges me to take a second trade. Stopping after one
winner is always permitted and never needs a reason. The rule sets a ceiling on activity, not a floor.


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

**NQ, ES and US100 are ONE INSTRUMENT for the purposes of these rules.**

They are three tickers on the same underlying risk: US equity indices. Treating them as separate
ideas is the fastest way to take the same trade twice while believing I diversified.

### Simultaneous — resolved by structure

§6 permits one open position at a time, so holding two correlated positions is impossible.
Nothing further to decide here.

### Sequential — this is the live rule

**After a losing trade, trade 2 may not be the same direction on any instrument in the index group.**

That is a re-entry into a trade that already failed, wearing a different ticker. If the only setup
available is a same-direction index trade, **the day is done.**

| Trade 1 | Trade 2 proposed | Permitted? |
|---|---|---|
| Long NQ — lost | Long US100 | **No.** Same trade re-entered. |
| Long NQ — lost | Long ES | **No.** Same trade re-entered. |
| Long NQ — lost | Long NQ | **No.** Plainly the same trade. |
| Long NQ — lost | Short NQ / ES / US100 | Different trade. Permitted. |
| Long NQ — lost | XAU/USD | Different instrument. Permitted. |
| Long NQ — **won** | Long US100 | <!-- TODO: ask me — does this rule apply after a WIN too? --> |

`/checktrade` blocks the barred rows and quotes this table.

**XAU/USD vs the index group:** <!-- TODO: ask me — separate bucket, or correlated in my experience? -->

## 8. Moving stops

**A stop NEVER moves away from entry. Not once, not for any reason, not on any instrument.**

**The stop is a live order with the broker, placed the moment the position is opened.**
Not a mental stop. Not an alert. Not "I'll watch it." A working order sitting in the book.

I cannot widen what I do not have to look at. A mental stop is not a stop — it is an intention,
and intentions do not survive contact with a position that is losing.

<!-- WHY THIS RULE OUTRANKS ALMOST EVERYTHING ELSE HERE: -->
<!-- Widening a stop turns $500 of risk into $700, then $900. The moment that happens, every -->
<!-- number in this file is fiction: the daily limit, the weekly limit, the position sizing, -->
<!-- the expectancy in scripts/stats.py. All of it assumes 1R means what it says. -->
<!-- There are NO exceptions written here, deliberately, so that none can be argued for at 01:00. -->

Moving the stop **toward** profit is a different action and is governed below.

**When may a stop move to breakeven?** <!-- TODO: ask me -->
<!-- Needs a single objective trigger, e.g. "at +1R". Not "when it looks safe". -->
<!-- Note the cost: a breakeven stop converts losers into scratches AND winners into scratches. -->
<!-- It is not free, and at a 1:2 minimum R:R it can quietly destroy the edge. -->

**Trailing rule, if any:** <!-- TODO: ask me -->

## 9. Adding to positions

**NO ADDING. Not to winners, not to losers, not ever.**

One entry. One size. One stop. What I open with is what I close with.

- **Adding to a loser** is averaging down. It converts a defined $500 risk into an undefined one and
  makes the stop meaningless. On a challenge account with a firm drawdown behind it, this is the
  single fastest route to failure.
- **Adding to a winner** is not safer, only slower. It moves the average entry against me and lets a
  reversal turn a won trade into a lost one.

This rule also keeps `risk/sizing.md` honest: 1R is $500 from the moment the position opens to the
moment it closes, so `r_actual` in `data/trades.csv` means the same thing on every row. Scaling in
would make every statistic in `scripts/stats.py` incomparable.

**Partial exits (scaling OUT) are a different action** and are governed by the target logic in the
setup file, not here. <!-- TODO: ask me — do I take partials at all, or is it all-out at one target? -->

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
