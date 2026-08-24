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

**ONE TRADE PER DAY (§5), so the day's loss is whatever that single trade did. Ceiling: $500.**

| Phase | Max daily loss | In R |
|---|---|---|
| Evaluation | **$500** | 1.0 R |
| Funded | **$250** | 1.0 R |

The trade closes, and the trading day is over — win, lose or scratch. There is no second decision
to make and no budget to carry forward.

**The full range of a day, evaluation (1R = $500):**

| The one trade | Day ends at |
|---|---|
| Target hit, +1.5R | **+$750** |
| Early exit in profit | between $0 and +$750 |
| Scratch | $0 |
| Early exit at a loss | between $0 and −$500 |
| Full stop | **−$500** |

**Worst possible day −$500. Best possible day +$750.** Both are hard numbers, not intentions.

Wins do not create a budget to lose later, because there is no later. Profit never becomes risk.

When the trade closes: the platform gets closed. Not a scalp to get back to flat, not "one more
because the first was a scratch". The assistant stops all trade analysis for the rest of that day —
Prime Directive rule 6 in `CLAUDE.md`. Arguing with it is itself the signal that the rule is working.

<!-- SIMPLIFIED 2026-08-24 when the trade cap went from 2 to 1. -->
<!-- Everything the old §2 needed — cumulative loss tracking, carried-forward budgets, sizing -->
<!-- trade 2 to the remainder, whether wins extend the budget — is now dead. One trade cannot -->
<!-- exceed its own stop, so the daily limit enforces itself. -->

**Does an open position count toward this at unrealised value?**
Resolved by structure: one position, one trade, stop at 1R. Unrealised loss cannot exceed $500.
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

**No separate streak rule. §3 covers it.**

Three losing days ends the week regardless of whether they were consecutive. A streak of three in a
row and three scattered across a week produce the same outcome: stop, run `/review`, return Monday.

<!-- Considered and rejected on 2026-08-24: a harsher streak trigger (demo, or half size until a -->
<!-- winning week). Rejected because §3 already caps the damage at -$1,500 and a second overlapping -->
<!-- shutdown rule is one more thing to track at 01:00. One rule that fires is better than two that -->
<!-- get argued about. -->

**If `/review` ever shows the three losses had a common cause** — same setup, same hour, same
instrument, same state of mind — that is a strategy problem, not a streak problem, and it gets fixed
in the setup file, not with a bigger shutdown.

## 5. Max trades per day

**ONE. One trade per day. Win, lose or scratch — when it closes, the day is over.**

| Phase | Max trades per day |
|---|---|
| Evaluation | **1** |
| Funded | **1** <!-- TODO: ask me — confirm this stays 1 once funded --> |

**One is a CAP, not a quota.** Nothing obliges me to trade at all. A day with no setup is a day with
no trade, and that is a correct day, not a wasted one. The rule sets a ceiling on activity, never a floor.

Must match `strategy/00-core-rules.md` §3. If the two ever disagree, this file wins and the other gets fixed.

<!-- CHANGED 2026-08-24 from 2 to 1, during the interview, before any live trading. -->
<!-- WHAT THIS FIXES: with one trade a day there is no revenge trade, no "make it back", no -->
<!-- second-guessing after a loss, and no correlated re-entry. The whole class of after-the-loss -->
<!-- mistakes is removed structurally rather than by willpower at 01:00. -->

### THE SCRATCH LOOPHOLE — now the only way to get a second entry

A scratch does not use the day's trade (see below), so **a scratch is the single remaining path to
trading twice in one day.** With the cap at 1 rather than 2, that loophole matters far more than it
did, and the boundary of "scratch" is still undefined.

**Does a breakeven scratch count against the 1? NO. Scratches are free.**

<!-- STANDING RISK, written down so I cannot claim it surprised me: -->
<!-- "Scratch" is undefined (see below), so in principle an unlimited number of small-loss exits -->
<!-- could be called scratches and the one-trade cap would not exist at all. -->
<!-- If /review ever shows a day with more than one real entry, this is the mechanism. -->

**What exactly counts as a scratch? UNDEFINED — skipped on 2026-08-24. Ask me again.**
<!-- A trade exited at the entry price is never exactly $0.00 after commission and spread. -->
<!-- Without a boundary this rule either never fires, or fires whenever I want it to. -->
<!-- Not inventing the number. The options are: exact $0.00 or better; costs-only; or a dollar band I name. -->

Until it is defined, `/checktrade` returns `INCOMPLETE: scratch threshold undefined` when the day's
trade closed at a small loss and another is proposed. It does not pick a number for me.

## 6. Max concurrent positions

**ONE. Never two open at the same time.**

| Field | Value |
|---|---|
| Max concurrent positions | **1** |
| Max total open risk at any moment | **1.0 R** ($500 evaluation / $250 funded) |

Since §5 caps the day at one trade, this rule is largely structural now: one trade a day cannot
be two positions at once. It stays written down because it is what makes the cap enforceable at the
platform level — if there is never more than one ticket open, there is nothing to reconcile.

**It becomes load-bearing again the moment §5 changes.** If the daily cap ever goes above 1, this
is the rule that stops two positions from turning $500 of risk into $1,000.

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

### Sequential — resolved by structure since 2026-08-24

With one trade per day (§5), there is no second trade to police. A losing long on NQ cannot be
re-entered as a long on US100 or ES, because the day is over the moment the NQ trade closes.

<!-- The rule this replaced: "after a losing trade, trade 2 may not be the same direction on any -->
<!-- index-group instrument." Correct, and now unreachable. Kept in git history. -->
<!-- IT COMES BACK THE MOMENT THE CAP GOES ABOVE 1, so if §5 ever changes, restore it. -->

**The group is still defined, and still matters** — for the weekly picture, for `/review`, and for
`scripts/stats.py` breakdowns by instrument. Three losing days in a row all long the index group is
one idea failing three times, not three independent losses.

| Instrument | Group |
|---|---|
| NQ | Index |
| ES | Index |
| US100 | Index |
| XAU/USD | <!-- TODO: ask me — separate bucket, or correlated in my experience? --> |


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

**A stop NEVER moves to breakeven either. The stop does not move at all.**

Set at entry from structure, and left alone until it is hit or the target is hit. There is no
breakeven step, no partial protection, no management. Stop or target. Nothing in between.

<!-- CHANGED 2026-08-24: a +1.5R breakeven trigger was written, then removed the same session -->
<!-- when the target itself dropped to 1.5R (§10) — the trigger and the target became the same -->
<!-- price, so the rule could never fire. Removing it entirely is the honest resolution. -->
<!-- CONSEQUENCE: the stop is now completely static. Nothing about a live position is discretionary. -->
<!-- There is exactly one decision per trade, and it happens before entry. -->

**Trailing rule: none.** A trailing stop is stop movement, and the stop does not move.

**Summary of §8 in one line:** the stop is placed once, from structure, before entry, as a live
broker order — and is never touched again in either direction.

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

### Scaling out — NOT USED. All out at one exit.

**One entry, one exit. The trade closes at the stop or at the target, in full.**

`r_actual` is therefore always a single clean number, which keeps every row in `data/trades.csv`
comparable and `scripts/stats.py` expectancy honest.

<!-- Reversed on 2026-08-24, same session it was written. Briefly recorded as "half at target, -->
<!-- half runs", then withdrawn in favour of a single exit. Kept in the git history deliberately: -->
<!-- if I propose scaling out again, this is the second time, and /review should ask why. -->

## 10. Minimum R:R

**1:1.5 — risk 1 to make 1.5. Minimum target is 1.5R.**

Measured to the **first** target, not the dream target.
If the nearest logical target does not pay 1.5R, the trade does not exist. Hard filter, not a preference.

| Phase | 1R risked | Minimum target |
|---|---|---|
| Evaluation | $500 | **$750** |
| Funded | $250 | **$375** |

**Stop distance is set by structure first, then size is solved from it** — never the reverse.
Never shrink a stop to manufacture a 1.5R target. That is how a 1.5R trade becomes a 0.3R trade
with five times the size.

<!-- CHANGED 2026-08-24, same session it was set at 1:2. Lowered to 1:1.5. -->
<!-- THE COST OF THAT CHANGE, in numbers: -->
<!--   Break-even win rate at 1:2   = 33.3%  (need ~3.3 winners in 10) -->
<!--   Break-even win rate at 1:1.5 = 40.0%  (need 4 winners in 10) -->
<!-- A closer target should produce a higher hit rate, which is the trade being made here. -->
<!-- /review must check that it actually did: if the win rate in scripts/stats.py sits below 40%, -->
<!-- this rule is losing money and goes back to 1:2. That check happens in review, never mid-session. -->

<!-- WHAT THIS MEANS FOR THE CHALLENGE MATH: -->
<!--   Best possible day  = 1 winner  = +1.5R = +$750 (§5 caps the day at one trade) -->
<!--   Worst possible day = -1.0R = -$500 (§2) -->
<!--   Worst possible week = -3.0R = -$1,500 (§3) -->
<!-- TODO: verify the profit target on FundedNext, then divide by 1.5R to get the minimum -->
<!-- number of NET winning trades needed to pass. That number is the real plan. -->

<!-- TODO: ask me — is 1.5R the minimum for BOTH a-plus and b-grade, or is a-plus higher? -->

## 11. Recovery / size-up rules

**Risk never changes. $500 per trade in evaluation, $250 funded. Every day, every trade.**

- After a losing day: **still $500.** Yesterday is not an input to today's sizing.
- After a winning day: **still $500.** A good run is not permission to size up.
- After a losing week: **still $500** on return. `/review` may change the strategy; it does not change the number.
- To make back a loss: **never.** Size is not a recovery tool. Increasing risk after a loss is the
  single behaviour that turns a bad week into a failed account, and it always feels justified at the time.

The only thing that changes the risk number is the phase of the account (§1), and that change goes
one way: **down**, from 1% in evaluation to 0.5% funded.

<!-- One number, forever, is the entire point. A risk size that moves is a risk size I will argue -->
<!-- with, and I will win that argument at 01:00 on a losing night. -->

---

## Enforcement

- These numbers are changed only in `/review`, between sessions, in writing.
- A rule changed mid-session does not exist. The old number stands until tomorrow.
- Every breach gets logged in `psychology/rules-i-actually-break.md` with its cost in R. No exceptions, especially not the ones that made money.
