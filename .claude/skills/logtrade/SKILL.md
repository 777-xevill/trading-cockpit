---
name: logtrade
description: Log a closed trade. Interviews every CSV column, appends the row to data/trades.csv and a summary to today's journal. Asks about emotion and process grade BEFORE P&L.
---

# /logtrade

Log a closed trade. **One question at a time.** No commentary on the outcome — not "unlucky", not "nice one", not "that's a good R". You are a recorder here.

## Order matters

Ask about **emotion and process grade before you ask about P&L**. Once I know the number, my memory of the decision rewrites itself to match it. Do not let me see the outcome framing first. If I volunteer the P&L early, record it but still ask the process and emotion questions before you refer to it, and do not mention it while asking them.

## Interview order

**A. Identification**
1. Date (default today), time of entry (Dhaka GMT+6)
2. Instrument
3. Session
4. `setup_tag` — must match a file in `strategy/setups/`. If it does not, say so and ask me to name the real one or create the file.
5. Direction (long/short) — recorded as data, never discussed

**B. The plan as it was before entry**
6. Entry price
7. Stop price
8. Target price
9. Size
10. Risk in $ (= 1R)
11. `r_planned` — compute from entry/stop/target and show the arithmetic

**C. Process and state — ASK THESE BEFORE P&L**
12. `emotion_before` — one or two words. What was I feeling in the 60 seconds before clicking?
13. `emotion_after` — one or two words.
14. Did you run `/checktrade` before entering? Yes/no.
15. `rules_followed` — Y or N. Y only if every rule held. "Mostly" is N.
16. If N: `rule_broken` — which rule, and what did I tell myself in the moment? Capture the excuse **verbatim**, not tidied up.
17. `process_grade` 1–5, using the scale in `journal/_template.md` §8. Ask me to justify the grade in one line.

**D. The outcome**
18. Exit price
19. `r_actual` — compute, show the arithmetic
20. `pnl_usd`
21. `screenshot` path (optional)
22. `notes` — one line

## Then write

1. Append **one row** to `data/trades.csv` in exact column order:
   `date,time,instrument,session,setup_tag,direction,entry,stop,target,exit,size,risk_usd,r_planned,r_actual,pnl_usd,rules_followed,rule_broken,process_grade,emotion_before,emotion_after,screenshot,notes`
   Quote any field containing a comma. Never reorder columns. Never rewrite existing rows.
2. Append the trade to the table in section 4 of today's journal, and the grade to section 8.
3. If `rules_followed = N`: add a row to `psychology/rules-i-actually-break.md` with the date, the rule, the verbatim excuse, and the cost in R. **Do this even if the trade won** — especially if the trade won.

## Then state, flatly

- Running total for the day: R and $
- Trades used: n of cap
- Risk budget remaining
- If the daily loss limit is now hit: say it, tell me to close the terminal, and stop assisting with trade analysis for the rest of the day.
- If `rules_followed = N` and `r_actual > 0`: one line — "Rule broken, trade won. That is the expensive kind." Nothing more.

No summary of how the trade went. No lessons. That is what `/review` is for.
