# ES — E-mini S&P 500 Futures

## Contract spec
<!-- TODO: verify with my broker -->

| Field | Value |
|---|---|
| Symbol | ES (E-mini) / MES (Micro) |
| Exchange | CME |
| Tick size | <!-- TODO: verify --> |
| Tick value (ES) | <!-- TODO: verify --> |
| Tick value (MES) | <!-- TODO: verify --> |
| 1 point = | <!-- TODO: verify --> |
| Margin (intraday) | <!-- TODO: verify with my broker --> |

## Hours

| | NY time | Dhaka (GMT+6) |
|---|---|---|
| RTH open | 09:30 | 19:30 |
| RTH close | 16:00 | 02:00 |
| Globex open | 18:00 | 04:00 |

## Behaviour notes
<!-- TODO: ask me -->

- Typical daily range: <!-- TODO: ask me -->
- Typical stop distance for my setups: <!-- TODO: ask me -->
- Minimum FVG size I care about: <!-- TODO: ask me -->

## Rules specific to ES
<!-- TODO: ask me -->

- Max contracts: <!-- TODO: ask me -->
- Sessions permitted: <!-- TODO: ask me -->

## Correlation
ES, NQ and US100 are **one instrument** under `risk/risk-rules.md` §7.
Holding two at once is impossible under §6. After a loss, no same-direction re-entry on any of the three.
