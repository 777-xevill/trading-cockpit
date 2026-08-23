# Position Sizing

**Arithmetic only. This file contains no opinions about whether to take the trade.**

---

## The formula

```
risk_$        = account_size × risk_%
stop_distance = |entry − stop|                 (in points/pips, per instrument convention)
value_per_point_per_unit = from the table below
size          = risk_$ / (stop_distance × value_per_point_per_unit)
```

Then **round DOWN** to the nearest tradeable increment. Never round up.
If rounding down gives 0, the trade is too big for the account. Do not "just take the minimum" — that is sizing by wishful thinking, not by rule.

**Sanity check, always:** `size × stop_distance × value_per_point = risk_$`. If it does not reconcile, do not click.

---

## Instrument table

<!-- Every row is TODO: verify with my broker. A wrong tick value here is a 10x sizing error. -->

| Instrument | Unit | Tick / point size | Value per point per unit | Min increment | Verified |
|---|---|---|---|---|---|
| NQ (E-mini) | contract | `TODO: verify with broker` | `TODO: verify with broker` | 1 | ☐ |
| MNQ (Micro) | contract | `TODO: verify with broker` | `TODO: verify with broker` | 1 | ☐ |
| ES (E-mini) | contract | `TODO: verify with broker` | `TODO: verify with broker` | 1 | ☐ |
| MES (Micro) | contract | `TODO: verify with broker` | `TODO: verify with broker` | 1 | ☐ |
| XAU/USD | lot | `TODO: verify with broker` | `TODO: verify with broker` | `TODO: verify` | ☐ |
| US100 | lot | `TODO: verify with broker` | `TODO: verify with broker` | `TODO: verify` | ☐ |

<!-- XAU/USD warning: brokers disagree on whether a "pip" is 0.10 or 0.01, and on contract size (100oz is common). -->
<!-- Confirm by placing a 1-unit trade and reading the actual $ move per point, or by asking support in writing. -->

---

## Worked examples

<!-- Fill these in once the table above is verified. Then re-derive them by hand once a month. -->
<!-- If I cannot do this arithmetic in my head at 22:00 under pressure, I am not allowed to trade that instrument. -->

**NQ example** — account $50,000, risk `TODO`%, stop `TODO` points:
```
TODO
```

**XAU/USD example** — account $50,000, risk `TODO`%, stop `TODO`:
```
TODO
```

---

## Costs

Spread, commission and slippage come out of the R, not out of nowhere.

| Instrument | Commission per unit round-turn | Typical spread | Slippage assumption |
|---|---|---|---|
| NQ | `TODO: verify with broker` | | |
| ES | `TODO: verify with broker` | | |
| XAU/USD | `TODO: verify with broker` | | |
| US100 | `TODO: verify with broker` | | |

**Do I subtract costs before calculating R?** <!-- TODO: ask me -->

---

## Hard caps

**Max contracts/lots per instrument regardless of what the formula says:** <!-- TODO: ask me -->
**Max total open risk across all positions:** <!-- TODO: ask me — must match `risk/risk-rules.md` §6 -->
