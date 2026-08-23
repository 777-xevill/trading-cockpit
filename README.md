# Trading Cockpit

Personal risk-and-process repo for discretionary intraday trading (NQ, ES, XAU/USD, US100 — ICT/SMC).
This is not a signal system. It is a set of rules I wrote for myself, plus a machine that checks whether I followed them.

## Daily loop

| When | Command | What it does |
|---|---|---|
| Before the session | `/premarket` | Sets today's risk budget, bias, levels, news. Creates today's journal file. |
| Before **every** entry | `/checktrade` | Interrogates the trade against my rules. Verdict only: COMPLIES / VIOLATES / INCOMPLETE. |
| After **every** exit | `/logtrade` | Interviews me for every CSV column, appends to `data/trades.csv` and today's journal. |
| After a loss, or when I feel it | `/tilt` | Runs the post-loss protocol. Refuses further analysis if the daily loss limit is hit. |
| Saturday | `/review` | Runs `stats.py`, finds the pattern, writes `reviews/weekly/YYYY-WW.md`, gives me one change. |
| Any time | `/rules` | Dumps my hard rules verbatim. No commentary. |

Rule: no journal file for today means no trade analysis. Run `/premarket` first.

## Stats

```bash
python -m venv .venv
.venv/Scripts/activate      # Windows
pip install -r scripts/requirements.txt
python scripts/stats.py
```

Reads `data/trades.csv`, prints expectancy, profit factor, drawdown, breakdowns, and the rule-compliance analysis — expectancy when I followed my rules vs when I didn't.

## Layout

- `strategy/` — what I trade and when
- `risk/` — how much, and the prop-firm constraints
- `psychology/` — what goes wrong and the protocol for it
- `journal/` — daily entries, one file per trading day
- `reviews/` — weekly and monthly
- `data/trades.csv` — the raw record
- `.claude/skills/` — the slash commands above

`CLAUDE.md` is the contract for how the assistant behaves here. Read it before changing anything.

*Nothing here is financial advice.*
