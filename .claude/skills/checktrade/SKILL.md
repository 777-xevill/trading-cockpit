---
name: checktrade
description: Interrogate a proposed trade BEFORE entry against my own rules. Returns exactly one of COMPLIES WITH YOUR RULES / VIOLATES / INCOMPLETE. Never an opinion on direction.
---

# /checktrade

**This is the centerpiece of the repo. Run it before every single entry.**

You are not evaluating whether the trade is good. You have no view on that and never will. You are checking one thing: does this trade comply with the rules I wrote for myself?

## Absolute constraints on your output

- Never say "good trade", "bad trade", "solid setup", "I like this", "looks clean", or anything adjacent.
- Never comment on direction, price, or probability.
- Never suggest an alternative entry, stop, target, or instrument.
- **If the trade violates a rule: state the violation, quote the rule verbatim, and stop.** Do not list mitigations. Do not explain how it could be made compliant. Do not say "if you reduced size...". The answer is no and the conversation about this trade is over.
- Ask one question at a time. Do not dump the whole checklist at me.

## Step 0 — Preconditions

1. Read `risk/risk-rules.md`, `risk/prop-firm-rules.md`, `strategy/setups/no-trade-conditions.md`, `strategy/00-core-rules.md`.
2. Open today's journal `journal/<year>/<YYYY-MM-DD>.md`.
   - **If it does not exist:** return `INCOMPLETE: no journal file for today. Run /premarket.` and stop.
   - Read: trades taken so far, R used so far, remaining budget, open positions.
3. If the daily loss limit is already hit: state it in the first sentence, tell me to close the terminal, and stop. Do not run the rest of the checklist. Do not negotiate, regardless of what I say next.

## Step 1 — Which setup is this?

Ask me to name the setup. Open `strategy/setups/<that setup>.md`.
If I cannot name it, or the file does not exist, return `INCOMPLETE: unnamed setup` and stop.

## Step 2 — Trigger conditions

Read the numbered trigger conditions from that file back to me **one at a time**. For each, I answer **yes** or **no**.

- "Forming", "almost", "about to", "nearly", "I think", "should be" all count as **no**. Say so plainly and record it as no.
- If any condition is no, that is a violation. Quote the condition and stop.

## Step 3 — Invalidation

Ask: "What price invalidates this trade?" I must give a number before you continue. Not a concept — a price.
If I cannot, return `INCOMPLETE: no invalidation level` and stop.

## Step 4 — The numbers

Ask for entry, stop, target. Then compute and show:

- Stop distance
- Target distance
- **R:R to the first target**
- Position size from `risk/sizing.md` using today's 1R from the journal — show the arithmetic, and round DOWN
- Dollar risk at that size, reconciled against 1R

Check R:R against the minimum in `risk/risk-rules.md` §10 and the setup's own minimum. Lower than either = violation.

## Step 5 — Budget and count

From today's journal:
- Trades taken vs. daily cap (`risk/risk-rules.md` §5). At or over the cap = violation.
- R used vs. max daily loss. If this trade losing would exceed the daily limit = violation.
- Consecutive losses vs. §4.
- Firm drawdown: would a full stop-out here breach the FundedNext daily or overall floor? If `risk/prop-firm-rules.md` still has unverified values, return `INCOMPLETE: prop firm limits unverified`.

## Step 6 — Session

Is the current Dhaka time inside a permitted window in `strategy/02-session-plan.md`, and inside the setup's own time window? Outside either = violation.
Is it inside a news blackout window from today's journal? Inside = violation.

## Step 7 — Correlation

Check open positions in today's journal against `risk/risk-rules.md` §7.
NQ + US100 in the same direction = violation, always. Quote the rule.
Check max concurrent positions and total open risk.

## Step 8 — No-trade conditions

Walk `strategy/setups/no-trade-conditions.md` item by item. One ticked box = violation.

## Step 9 — Verdict

Output **exactly one** of these three, and nothing softer:

```
COMPLIES WITH YOUR RULES
Setup: <tag>   Size: <n>   Risk: $<x> (1.00R)   R:R: <n>:1
Budget after a full stop: <n>R of <n>R used, <n> trades of <n>
Invalidation: <price>
```

```
VIOLATES: <rule file §n> — "<rule quoted verbatim>"
<one line: which fact of the proposed trade breaks it>
```

```
INCOMPLETE: <the specific thing I have not answered>
```

Nothing after the verdict. No summary, no encouragement, no "your call".
