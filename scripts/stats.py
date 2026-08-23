#!/usr/bin/env python3
"""
Trading cockpit statistics.

Reads data/trades.csv and prints a plain-text performance report.
No opinions, no direction, no advice. Arithmetic only.

Usage:
    python scripts/stats.py [path/to/trades.csv]
"""

import sys
from pathlib import Path

try:
    import pandas as pd
except ImportError:
    sys.exit("pandas not installed. Run: pip install -r scripts/requirements.txt")


REPO = Path(__file__).resolve().parent.parent
DEFAULT_CSV = REPO / "data" / "trades.csv"

W = 74
SPARK = "_.-~=+*#"


# ----------------------------------------------------------------------------- helpers

def rule(char="="):
    print(char * W)


def header(text):
    print()
    rule()
    print(text.upper())
    rule()


def sub(text):
    print()
    print(text)
    print("-" * W)


def fmt(value, spec="{:.2f}"):
    if value is None:
        return "n/a"
    try:
        if pd.isna(value):
            return "n/a"
    except (TypeError, ValueError):
        pass
    try:
        return spec.format(value)
    except (TypeError, ValueError):
        return str(value)


def row(label, value, width=38):
    print(f"{label:<{width}} {value}")


def sparkline(values):
    """ASCII sparkline of a numeric series."""
    vals = [v for v in values if pd.notna(v)]
    if len(vals) < 2:
        return "(need at least 2 trades)"
    lo, hi = min(vals), max(vals)
    span = hi - lo
    if span == 0:
        return SPARK[0] * len(vals)
    steps = len(SPARK) - 1
    return "".join(SPARK[min(steps, int((v - lo) / span * steps))] for v in vals)


def max_consecutive(flags):
    """Longest run of True in an iterable of booleans."""
    best = run = 0
    for flag in flags:
        run = run + 1 if flag else 0
        best = max(best, run)
    return best


def expectancy(series):
    """Mean R per trade."""
    s = series.dropna()
    return s.mean() if len(s) else None


def profit_factor(series):
    s = series.dropna()
    gains = s[s > 0].sum()
    losses = -s[s < 0].sum()
    if losses == 0:
        return float("inf") if gains > 0 else None
    return gains / losses


def max_drawdown(series):
    """Max peak-to-trough drawdown of the cumulative curve, in the series' units."""
    s = series.dropna()
    if s.empty:
        return None
    equity_curve = s.cumsum()
    peak = equity_curve.cummax()
    return float((equity_curve - peak).min())


# ----------------------------------------------------------------------------- load

REQUIRED = [
    "date", "time", "instrument", "session", "setup_tag", "direction",
    "entry", "stop", "target", "exit", "size", "risk_usd", "r_planned",
    "r_actual", "pnl_usd", "rules_followed", "rule_broken", "process_grade",
    "emotion_before", "emotion_after", "screenshot", "notes",
]

NUMERIC = ["entry", "stop", "target", "exit", "size", "risk_usd",
           "r_planned", "r_actual", "pnl_usd", "process_grade"]

TEXT = ["instrument", "session", "setup_tag", "direction", "rule_broken"]


def load(path):
    if not path.exists():
        sys.exit(f"No such file: {path}")

    try:
        df = pd.read_csv(path)
    except pd.errors.EmptyDataError:
        return pd.DataFrame(columns=REQUIRED)

    for col in REQUIRED:
        if col not in df.columns:
            df[col] = pd.NA

    for col in NUMERIC:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    df["rules_followed"] = (
        df["rules_followed"].astype("string").str.strip().str.upper().str[:1]
    )
    for col in TEXT:
        df[col] = df[col].astype("string").str.strip()

    df["_dt"] = pd.to_datetime(df["date"], errors="coerce")
    df["dow"] = df["_dt"].dt.day_name()

    # Chronological order matters for streaks, equity curve and drawdown.
    df = df.sort_values(["_dt", "time"], na_position="last").reset_index(drop=True)
    return df


# ----------------------------------------------------------------------------- sections

def overview(df):
    r = df["r_actual"].dropna()
    pnl = df["pnl_usd"].dropna()

    wins = r[r > 0]
    losses = r[r < 0]
    scratches = r[r == 0]
    decided = len(wins) + len(losses)

    header("overview")
    row("Trades logged", len(df))
    row("Trades with an R result", len(r))
    if len(r) == 0:
        print()
        print("No closed trades with r_actual. Nothing to compute.")
        return

    row("Wins / Losses / Breakeven", f"{len(wins)} / {len(losses)} / {len(scratches)}")
    row("Win rate (excl. breakeven)",
        fmt(len(wins) / decided * 100, "{:.1f}%") if decided else "n/a")
    print()
    row("Average win", f"{fmt(wins.mean())} R" if len(wins) else "n/a")
    row("Average loss", f"{fmt(losses.mean())} R" if len(losses) else "n/a")
    row("EXPECTANCY PER TRADE", f"{fmt(expectancy(r))} R")
    row("Profit factor (R)", fmt(profit_factor(r)))
    print()
    row("Largest win", f"{fmt(r.max())} R")
    row("Largest loss", f"{fmt(r.min())} R")
    row("Max consecutive losses", max_consecutive(r < 0))
    row("Max consecutive wins", max_consecutive(r > 0))
    print()
    row("Total R", fmt(r.sum()))
    if len(pnl):
        row("Total P&L", f"${fmt(pnl.sum(), '{:,.2f}')}")


def equity(df):
    r = df["r_actual"].dropna()
    if r.empty:
        return

    header("equity curve (R)")
    cum = r.cumsum()
    print(sparkline(cum.tolist()))
    print()
    row("Start / End", f"0.00 R  ->  {fmt(cum.iloc[-1])} R")
    row("Peak", f"{fmt(cum.max())} R")
    row("Trough", f"{fmt(cum.min())} R")
    row("MAX DRAWDOWN", f"{fmt(max_drawdown(r))} R")


def breakdown(df, col, title):
    sub(title)
    valid = df[df[col].notna() & (df[col].astype("string").str.len() > 0)]
    if valid.empty:
        print("(no data)")
        return

    print(f"{'':<18}{'n':>5}{'win%':>8}{'exp R':>9}{'total R':>10}{'PF':>8}{'$':>12}")
    for key, grp in valid.groupby(col, dropna=True):
        r = grp["r_actual"].dropna()
        name = str(key)[:17]
        if r.empty:
            print(f"{name:<18}{len(grp):>5}{'-':>8}{'-':>9}{'-':>10}{'-':>8}{'-':>12}")
            continue
        decided = (r > 0).sum() + (r < 0).sum()
        wr = f"{(r > 0).sum() / decided * 100:.0f}%" if decided else "-"
        pf = profit_factor(r)
        pf_s = "inf" if pf == float("inf") else fmt(pf)
        usd = grp["pnl_usd"].dropna().sum()
        print(f"{name:<18}{len(r):>5}{wr:>8}{fmt(expectancy(r)):>9}"
              f"{fmt(r.sum()):>10}{pf_s:>8}{fmt(usd, '{:,.0f}'):>12}")


def breakdowns(df):
    header("breakdowns")
    breakdown(df, "setup_tag", "BY SETUP")
    breakdown(df, "session", "BY SESSION")
    breakdown(df, "instrument", "BY INSTRUMENT")

    sub("BY DAY OF WEEK")
    order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    valid = df[df["dow"].notna()]
    if valid.empty:
        print("(no parseable dates)")
        return
    print(f"{'':<18}{'n':>5}{'win%':>8}{'exp R':>9}{'total R':>10}")
    for day in order:
        grp = valid[valid["dow"] == day]
        if grp.empty:
            continue
        r = grp["r_actual"].dropna()
        if r.empty:
            continue
        decided = (r > 0).sum() + (r < 0).sum()
        wr = f"{(r > 0).sum() / decided * 100:.0f}%" if decided else "-"
        print(f"{day:<18}{len(r):>5}{wr:>8}{fmt(expectancy(r)):>9}{fmt(r.sum()):>10}")


def compliance(df):
    header("rule compliance")

    followed = df[df["rules_followed"] == "Y"]
    broken = df[df["rules_followed"] == "N"]
    unmarked = len(df) - len(followed) - len(broken)

    if len(followed) == 0 and len(broken) == 0:
        print("No trades marked Y/N in rules_followed. This analysis is the point of the repo.")
        print("Fill the column.")
        return

    r_ok = followed["r_actual"].dropna()
    r_no = broken["r_actual"].dropna()

    print(f"{'':<18}{'n':>5}{'win%':>8}{'exp R':>9}{'total R':>10}{'$':>12}")
    for label, grp, r in (("Rules followed", followed, r_ok), ("Rules broken", broken, r_no)):
        if r.empty:
            print(f"{label:<18}{len(grp):>5}{'-':>8}{'-':>9}{'-':>10}{'-':>12}")
            continue
        decided = (r > 0).sum() + (r < 0).sum()
        wr = f"{(r > 0).sum() / decided * 100:.0f}%" if decided else "-"
        usd = grp["pnl_usd"].dropna().sum()
        print(f"{label:<18}{len(r):>5}{wr:>8}{fmt(expectancy(r)):>9}"
              f"{fmt(r.sum()):>10}{fmt(usd, '{:,.0f}'):>12}")

    if unmarked:
        print(f"{'Unmarked':<18}{unmarked:>5}   <- fill these in")

    print()
    e_ok, e_no = expectancy(r_ok), expectancy(r_no)
    if e_ok is not None and e_no is not None:
        row("Expectancy gap (followed - broken)", f"{fmt(e_ok - e_no)} R per trade")

    if not r_no.empty:
        cost_r = r_no.sum()
        cost_usd = broken["pnl_usd"].dropna().sum()
        row("Total R on rule-broken trades", fmt(cost_r))
        row("TOTAL $ ON RULE-BROKEN TRADES", f"${fmt(cost_usd, '{:,.2f}')}")
        if e_ok is not None:
            counterfactual = e_ok * len(r_no)
            row("Same trades at compliant expectancy", f"{fmt(counterfactual)} R")
            row("OPPORTUNITY COST OF BREAKING RULES", f"{fmt(counterfactual - cost_r)} R")
        won = r_no[r_no > 0]
        if len(won):
            print()
            print(f"WARNING: {len(won)} rule-breaking trades made money ({fmt(won.sum())} R).")
            print("Those are the expensive ones. They are what teaches the habit.")

    sub("MOST-BROKEN RULES")
    named = broken["rule_broken"].dropna()
    named = named[named.astype("string").str.len() > 0]
    if named.empty:
        print("(rule_broken column empty)")
    else:
        for name, n in named.value_counts().items():
            grp = broken[broken["rule_broken"] == name]
            cost = fmt(grp["r_actual"].dropna().sum())
            print(f"{str(name)[:45]:<47}{n:>4}x{cost:>10} R")


def process(df):
    header("process grade vs outcome")

    graded = df[df["process_grade"].notna() & df["r_actual"].notna()]
    if graded.empty:
        print("No trades with both a process grade and an R result.")
        print("The process grade is how you tell skill from luck. Fill it.")
        return

    row("Average process grade", fmt(graded["process_grade"].mean()))
    print()
    print(f"{'grade':<8}{'n':>5}{'win%':>8}{'exp R':>9}{'total R':>10}")
    for grade in sorted(graded["process_grade"].unique()):
        grp = graded[graded["process_grade"] == grade]
        r = grp["r_actual"]
        decided = (r > 0).sum() + (r < 0).sum()
        wr = f"{(r > 0).sum() / decided * 100:.0f}%" if decided else "-"
        print(f"{fmt(grade, '{:.0f}'):<8}{len(r):>5}{wr:>8}"
              f"{fmt(expectancy(r)):>9}{fmt(r.sum()):>10}")

    print()
    wins = graded[graded["r_actual"] > 0]
    lucky = wins[wins["process_grade"] <= 2]
    unlucky = graded[(graded["r_actual"] < 0) & (graded["process_grade"] >= 4)]

    row("Winners with a process grade <= 2", f"{len(lucky)}  (luck, not skill)")
    if len(lucky):
        row("  R won on those", fmt(lucky["r_actual"].sum()))
    row("Losers with a process grade >= 4", f"{len(unlucky)}  (correct trades, bad outcome)")
    if len(unlucky):
        row("  R lost on those", fmt(unlucky["r_actual"].sum()))

    corr = graded["process_grade"].corr(graded["r_actual"])
    if pd.notna(corr):
        print()
        row("Correlation: process grade vs R", fmt(corr))
        if len(graded) < 30:
            print("(sample too small to mean much yet)")


# ----------------------------------------------------------------------------- main

def main():
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_CSV
    df = load(path)

    rule()
    print("TRADING COCKPIT - STATISTICS")
    print(f"Source: {path}")
    rule()

    if df.empty:
        print()
        print("No trades logged yet.")
        print("Log a trade with /logtrade, or append rows to data/trades.csv.")
        print()
        rule()
        return

    overview(df)
    equity(df)
    breakdowns(df)
    compliance(df)
    process(df)

    print()
    rule()
    print("End of report. Numbers only - every decision is yours.")
    rule()


if __name__ == "__main__":
    main()
