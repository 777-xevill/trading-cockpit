# Invalidation

<!-- A thesis that cannot be wrong is not a thesis. This file defines "wrong". -->

---

## Bias invalidation (before any trade)

**My HTF bias is dead when:** <!-- TODO: ask me -->

**Do I flip bias same-session, or do I stand down for the rest of the day?** <!-- TODO: ask me -->

---

## Setup invalidation (idea forming, not yet entered)

From my strategy document, 2026-08-24. A setup I am waiting on is void when:

1. **No marked liquidity has been hit** by the time the execution window closes.
2. **The reaction never comes.** A liquidity hit alone is not a setup; without opposite-direction
   movement there is nothing to confirm.
3. **BOS never confirms with a body close.** A wick through the level is not a BOS.
4. **The level was already interacted with by a forward candle** and is therefore no longer fresh
   liquidity — see the forward-candle interaction rule in `strategy/01-market-structure.md`.
5. **Time runs out** — the execution window ends.
   <!-- TODO: ask me — the window end time is still undefined. -->

**Time-based void: if BOS has not confirmed within ____ minutes of the sweep, the idea is dead.**
<!-- TODO: ask me — the strategy document never sets this. Without it, a 09:42 sweep could -->
<!-- justify an entry at 11:30 on the same "idea", which is how a setup becomes a story. -->

## Trade invalidation (position is open)

**Structural invalidation — I am out regardless of where price is relative to my stop when:** <!-- TODO: ask me -->

**Time-based invalidation — if the trade has not moved ____ R within ____ minutes, I am out.** <!-- TODO: ask me -->

**Am I allowed to exit before my stop is hit?** <!-- TODO: ask me -->
<!-- Answer carefully. "Yes, on structure" and "yes, when I get scared" look identical in the moment. -->

---

## Re-entry

**Am I allowed to re-enter the same idea after a stop-out?** <!-- TODO: ask me -->

**If yes: how many times, and what must be different about the second entry?** <!-- TODO: ask me -->

**Does a re-entry count against my daily trade cap?** <!-- TODO: ask me -->
