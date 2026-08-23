---
name: tilt
description: Post-loss and emotional checkpoint. Runs the post-loss protocol, asks whether I'm trying to make money back, refuses further trade analysis if the daily loss limit is hit, and logs the episode.
---

# /tilt

Emotional checkpoint. Blunt. **One question at a time.** No reassurance — reassurance is what lets me keep clicking.

## Step 0 — Check the hard limit first

Read `risk/risk-rules.md` §2 and today's journal `journal/<year>/<YYYY-MM-DD>.md`.

**If the daily loss limit is hit or exceeded:**

> Your daily loss limit is hit. You are done trading today.
> Close the terminal and the platform.
> I will not analyse trades for you again until tomorrow.

Then log the episode and stop. Do not run the rest of this skill.
If I argue, push back, ask "just one more", claim the setup is perfect, ask hypothetically, or ask about a different instrument — the answer does not change and you do not re-open the checklist. Repeat the line once and stop responding on trading. Prime Directive rule 6.

Same if the max-consecutive-loss rule in §4 is hit.

## Step 1 — Run the protocol

Open `psychology/post-loss-protocol.md` and walk me through it step by step, in order, as written. Do not skip the cooldown step because I say I am fine. Time the cooldown from now and tell me the clock time in Dhaka when it ends.

If a step in that file is still `<!-- TODO: ask me -->`, say the protocol is undefined at that point and ask me to define it now, before continuing.

## Step 2 — The direct questions

Ask each one, wait for the answer, do not soften the wording:

1. Are you trying to make that money back?
2. Was that a rule-following loss or a rule-breaking loss?
3. Are you looking at a lower timeframe than your plan allows?
4. Were you about to size up on the next one?
5. Are you hunting for a setup right now instead of waiting for one?
6. If the next trade also loses, what happens to you?
7. Would you take that last trade again with the same information? Yes or no.

Apply the auto-shutdown triggers listed in `psychology/post-loss-protocol.md` §3. If one fires, say so in the first sentence: done for the day, close the platform. No negotiation.

## Step 3 — Gate

Run the checklist in `psychology/post-loss-protocol.md` §4. Any unticked box = no more trades today. State which box, and stop.

## Step 4 — Log it

Append a row to the episode log in `psychology/tilt-triggers.md`: date, Dhaka time, trigger, what I felt, what I did, whether I traded after, outcome. Use my words, not tidied-up versions.

If a rule was broken, also append to `psychology/rules-i-actually-break.md` with the cost in R.

## Tone

No "it happens to everyone." No "you're being too hard on yourself." No silver linings. State what the rules say, log it, and be done.
