# NQ — E-mini Nasdaq 100 Futures

## Contract spec
<!-- TODO: verify with my broker -->

| Field | Value |
|---|---|
| Symbol | NQ (E-mini) / MNQ (Micro) |
| Exchange | CME |
| Tick size | <!-- TODO: verify --> |
| Tick value (NQ) | <!-- TODO: verify --> |
| Tick value (MNQ) | <!-- TODO: verify --> |
| 1 point = | <!-- TODO: verify --> |
| Margin (intraday) | <!-- TODO: verify with my broker --> |

## Hours
<!-- TODO: ask me — which hours I actually watch, in Dhaka time -->

| | NY time | Dhaka (GMT+6) |
|---|---|---|
| RTH open | 09:30 | 19:30 |
| RTH close | 16:00 | 02:00 |
| Globex open | 18:00 | 04:00 |

## Behaviour notes
<!-- TODO: ask me — what NQ does that ES doesn't, in MY experience. Not textbook. -->

- Typical daily range: <!-- TODO: ask me -->
- Typical stop distance for my setups: <!-- TODO: ask me -->
- Minimum FVG size I care about: <!-- TODO: ask me -->

## Rules specific to NQ
<!-- TODO: ask me -->

- Max contracts: <!-- TODO: ask me -->
- Sessions permitted: <!-- TODO: ask me -->

## Correlation
NQ, ES and US100 are **one instrument** under `risk/risk-rules.md` §7.
One position at a time (§6), and after a loss no same-direction re-entry on any of the three.
