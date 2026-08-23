---
name: rules
description: Dump my hard rules verbatim from risk/ and strategy/00-core-rules.md. No commentary, no interpretation.
---

# /rules

Print my rules. Verbatim.

Read and output, in this order:

1. `risk/risk-rules.md`
2. `risk/prop-firm-rules.md`
3. `strategy/00-core-rules.md`
4. `strategy/setups/no-trade-conditions.md`

## How to output

- Reproduce the content as written. Do not paraphrase, summarise, reorder, or shorten.
- Separate each file with a `---` and its filename as a heading.
- Where a value is still `<!-- TODO: ask me -->` or `TODO: verify`, print it exactly as it stands so I can see the hole.

## What not to do

- No commentary before, between, or after.
- No interpretation of what a rule means.
- No note on which rules I have been breaking.
- No suggestion that a rule should change.
- No "let me know if you want to discuss any of these."

If I argue with a rule after seeing it: "Rules change in `/review`, not now."

Output the files. Stop.
