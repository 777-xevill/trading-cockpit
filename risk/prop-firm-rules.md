# FundedNext — Stellar Lite $50K

> **EVERY VALUE IN THIS FILE IS UNVERIFIED.**
> Nothing below was filled in from memory. Prop firm rules change without notice, and a wrong number
> in this file costs the account, not an argument. Open the FundedNext site and the account dashboard,
> copy the current numbers in, and put the date you checked next to each one.

**Account:** FundedNext Stellar Lite, $50,000
**Phase:** <!-- TODO: verify on FundedNext site -->
**Rules last verified on:** <!-- TODO: verify on FundedNext site — put the date here -->
**Source URL:** <!-- TODO: verify on FundedNext site -->

---

## Core numbers

| Constraint | Value | Verified |
|---|---|---|
| Profit target (Phase 1) | `TODO: verify on FundedNext site` | ☐ |
| Profit target (Phase 2, if any) | `TODO: verify on FundedNext site` | ☐ |
| Max daily drawdown (%) | `TODO: verify on FundedNext site` | ☐ |
| Max daily drawdown ($) | `TODO: verify on FundedNext site` | ☐ |
| Max overall drawdown (%) | `TODO: verify on FundedNext site` | ☐ |
| Max overall drawdown ($) | `TODO: verify on FundedNext site` | ☐ |
| Drawdown type — static or trailing | `TODO: verify on FundedNext site` | ☐ |
| If trailing: trails equity or balance? Stops trailing at initial balance? | `TODO: verify on FundedNext site` | ☐ |
| Daily drawdown measured from balance or equity? | `TODO: verify on FundedNext site` | ☐ |
| Daily reset time (and what that is in Dhaka GMT+6) | `TODO: verify on FundedNext site` | ☐ |
| Minimum trading days | `TODO: verify on FundedNext site` | ☐ |
| Maximum trading period / time limit | `TODO: verify on FundedNext site` | ☐ |
| Consistency rule (max % of profit from one day) | `TODO: verify on FundedNext site` | ☐ |
| News trading restriction | `TODO: verify on FundedNext site` | ☐ |
| Weekend holding allowed? | `TODO: verify on FundedNext site` | ☐ |
| Overnight holding allowed? | `TODO: verify on FundedNext site` | ☐ |
| Max lot size / position limit | `TODO: verify on FundedNext site` | ☐ |
| EA / copy trading / HFT restrictions | `TODO: verify on FundedNext site` | ☐ |
| Payout split and schedule | `TODO: verify on FundedNext site` | ☐ |
| Instruments allowed (are NQ/ES futures even offered, or only CFD equivalents?) | `TODO: verify on FundedNext site` | ☐ |

---

## What this means for my daily budget

**My personal daily loss limit must be strictly SMALLER than the firm's daily drawdown.**
If they are equal, one bad fill or one spread spike breaches the account.

- Firm daily drawdown: `TODO: verify`
- My daily loss limit (`risk/risk-rules.md` §2): `TODO: ask me`
- Buffer between them: `TODO`

<!-- TODO: ask me — what buffer do I want, as a single number or %? -->

## Distance to breach — updated manually

| Field | Value | As of |
|---|---|---|
| Current balance | | |
| Current equity | | |
| Today's drawdown floor ($) | | |
| Overall drawdown floor ($) | | |
| $ remaining before daily breach | | |
| $ remaining before overall breach | | |

`/premarket` fills this in each morning. `/checktrade` reads it before approving anything.

---

## Traps that end challenges

<!-- Keep this list as I learn them. Do not populate from assumption. -->

- Trailing drawdown that follows equity intraday, not closing balance. <!-- TODO: verify which applies -->
- Consistency rule failing an otherwise passing account because one day was too good. <!-- TODO: verify -->
- Positions open through a news restriction window. <!-- TODO: verify -->
- Weekend gap on a Friday hold. <!-- TODO: verify -->
