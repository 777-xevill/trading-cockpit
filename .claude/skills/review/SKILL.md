---
name: review
description: Weekly review. Runs stats.py, finds which setup carries expectancy, what broken rules cost, and when I break them. Writes reviews/weekly/YYYY-WW.md and ends with exactly one change.
---

# /review

Weekly review. Run it on Saturday, between sessions, never during one.

## Step 1 — Data

Run `python scripts/stats.py` and capture the full output. If pandas is missing, tell me the install command and stop.
Also read: every `journal/` file from the period, `psychology/rules-i-actually-break.md`, `psychology/tilt-triggers.md`, and the previous week's review in `reviews/weekly/`.

## Step 2 — Analyse

Answer these five questions with numbers, not impressions. Where the sample is too small to conclude anything, say "insufficient sample" — do not manufacture a pattern out of four trades.

1. **Which setup is actually carrying my expectancy?** Rank by total R contributed and by expectancy per trade. Name the one doing the work.
2. **Which setup do I *think* is good but isn't?** Compare how often I take a setup against what it returns. Frequency high + expectancy at or below zero = the answer. Say it in one sentence.
3. **What did broken rules cost me this period?** In R and in $. Include the opportunity cost line from stats.py. List rule-breaking trades that **won** separately — those are the ones building the habit.
4. **When do I break rules?** Cross-reference `psychology/rules-i-actually-break.md` and the journals against: time of day (Dhaka), after a loss, after a win, day of week, trade number of the day, hours of sleep. Name the strongest correlation you can actually support.
5. **Process vs. outcome.** Where did I get paid for a bad decision? Where did I do it right and lose? Which of those two is more common tells me whether the problem is the plan or the execution.

## Step 3 — Compare to last week

Did last week's one change actually happen? Yes or no, with evidence from the journals. If no, say so first, before anything else in the report.

## Step 4 — Write the file

Write `reviews/weekly/<YYYY>-<WW>.md` (ISO week number) containing:

- Period covered, trades, total R, total $
- The raw `stats.py` output
- Answers to the five questions
- Last week's change: done / not done
- Update the "Historical performance" block in each `strategy/setups/*.md` from the setup breakdown
- Update the "Repeat offenders" table in `psychology/rules-i-actually-break.md`

## Step 5 — One change

End with **exactly one** change for next week. One. Not a list, not "and also", not a primary plus two secondary.

It must be:
- a change to behaviour or to a written rule, not to my "mindset"
- specific enough that next Saturday it is provably done or not done
- the highest-leverage one, chosen by the numbers above

Format:

```
NEXT WEEK'S ONE CHANGE:
<the change>
How I will know it happened: <the test>
```

Nothing after that line. No encouragement.
