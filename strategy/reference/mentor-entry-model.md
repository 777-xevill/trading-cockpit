# Mentor's entry model — OBSERVED, NOT ADOPTED

> **THIS FILE IS NOT A RULE FILE. NOTHING IN IT BINDS ME.**
>
> It is a transcript of somebody else trading live, thinking out loud, mid-stream,
> while also talking about Netflix and a coin. It is not a strategy document and it
> was never written as one.
>
> `/checktrade` does **not** read this file. `strategy/setups/a-plus.md` is still the
> only definition of my A+ setup. Nothing moves from here into a rule file until I say
> so, question by question — see §7 below.
>
> Everything in quotes is **verbatim**. Everything not in quotes is my reading of it,
> and my reading can be wrong.

**Source:** livestream transcript, supplied 2026-09-01.
**Stream date:** unconfirmed. He refers to being stopped out "on Friday" and to the
market opening, which reads like a Monday. <!-- TODO: ask me — what date was this stream? -->
**Instruments:** NQ (traded) and ES (used for confirmation and targets).
**Outcome: STOPPED OUT.** This is a losing trade being narrated. That matters — see §5.

---

## 1. The trade, in the order it happened

### Pre-market: one-sided level marking

> "I literally didn't mark out a single high cuz I wanted all these lows."

He decided the draw **before** the session and marked only that side.

### The draw on liquidity

> "Are these triple equal lows? It is, right? Oh yeah, those lows have to get cooked.
> These lows have to get blasted. And if these lows get blasted, then this low gets
> blasted. And if this low gets blasted, then ideally these lows get blasted.
> Contingent on a lot of different things right now."

Target classes he names: **relative equal lows**, **triple equal lows**, **untapped
1H lows**. He targets them as a **cascade** — each one taken releases the next.

> "we need to take out these 1 hour lows"

### The wait

> "Going to wait until either we print a down candle or sweep out these highs.
> Simple as that."

### The trigger

> "Okay, we just swept these highs. That makes it a whole lot better. Um, now if we
> can see some sort of a rejection to the downside, I would probably want to get
> into shorts."

> "So we swept out these highs. We rejected off of it. This looks pretty good."

**Sweep → rejection → short.**

### Why NQ and not ES — the SMT call

> "It was mainly based off of ES, but I wanted to enter on NQ because NQ was the one
> that made the bearish SMT."

> "we had market open, boom, we swept out all these highs while ES didn't sweep out
> any of those highs. Um, we get a dump, we push up, fill, I think this was like a
> 5minute gap, something along those lines, and then we get confirmation to move down."

**This is a working definition of bearish SMT**: one index sweeps a high, the other
does not. The index that swept is the one he sells.

### The target was on the OTHER instrument

> "ES had the better targets of these relative equal lows and then these hourly lows.
> Um, but I wanted to take the trade on NASDAQ because I genuinely thought that we
> would be able to come down and probably get a bigger move."

> "because ES ES were more than likely going to want to take these lows. And if ES
> wants to take those lows, then I think NASDAQ has a high probability of taking these."

### He named the risk out loud, before it happened

> "I also need to keep a close eye on ES because if ES ends up taking out this low
> without NASDAQ moving down and taking out any of my lows, then that makes things a
> little bit more difficult."

> "if ES takes out these lows and NASDAQ doesn't, I'm actually going to be furious"

### It is exactly what happened

> "ES is about to take these lows. Let's see if NASDAQ can at least take our first
> lows. ES took those. NASDAQ, we're almost there. Come on, buddy. Come on, buddy.
> Come on, buddy. Bro, ain't no way, bro. **And I am stopped out.**"

> "All I wanted was for NASDAQ to take this low so that I could have taken some profit."

> "S&P took out Asia lows. I know."

---

## 2. What this CONFIRMS in my own model

| My rule | What the transcript shows |
|---|---|
| `a-plus.md` cond. 2 — sweep a marked liquidity level | "we swept out these highs" |
| `a-plus.md` cond. 3 — wait for opposite-direction reaction | "if we can see some sort of a rejection to the downside" |
| `a-plus.md` cond. 10 — the other index is a hard gate | ES was watched continuously, before and during |
| `risk-rules.md` §7 — NQ and ES are one instrument | He is trading one idea across two tickers, explicitly |

---

## 3. What this ADDS that my model does not have

**These are candidate answers to TODOs already open in `a-plus.md`. They are not
written into it. Each needs my yes.**

### 3a. It may answer the SMT-vs-confirmation contradiction

`a-plus.md` carries this open note:

> "my strategy overview lists 'SMT Divergence' as one of the four confluences, but
> step 10 above is not a divergence — it is a CONFIRMATION that the other index is
> doing the SAME thing. Those are opposite ideas."

The transcript uses **both, at different stages**:

| Stage | What the other index is for | Which index |
|---|---|---|
| **Selection** | **Divergence** — one sweeps, the other does not | Trade the one that **swept** |
| **Target** | **Alignment** — both should reach for the same draw | Both must go |

If that is my model too, they are **two rules, not one**, and `a-plus.md` needs a
separate numbered condition for SMT. <!-- TODO: ask me -->

### 3b. Target logic — currently blank in `a-plus.md`

Candidate hierarchy, from what he actually named:
relative equal lows / triple equal lows → untapped 1H lows → session (Asia) lows,
taken as a cascade.
<!-- TODO: ask me — is this my target rule? Which level is the FIRST target for R:R? -->

### 3c. A 5M gap fill before the confirmation

> "we get a dump, we push up, fill, I think this was like a 5minute gap ... and then
> we get confirmation to move down"

Retrace into a 5M gap **before** the entry confirmation. My model's stage 2 is a 1M
BOS sequence, not a gap fill. These may be the same thing described differently, or
they may be different models. <!-- TODO: ask me -->

### 3d. IFVG as a re-entry condition

> "re-entry. If we inverse this gap, then that would technically be valid."

`a-plus.md` lists IFVG as "optional, supporting" and still has it undefined.

---

## 4. WHERE THIS CONFLICTS WITH RULES I HAVE ALREADY LOCKED

**Read this section before copying anything above.**

### 4a. His model includes a re-entry after a stop-out. Mine does not.

> "This is pretty much exactly what happened on Friday. We got stopped out of the
> first trade, took a second one, and then dubbed."

`risk/risk-rules.md` §5: **"ONE. One trade per day. Win, lose or scratch — when it
closes, the day is over."**

That is not a small difference. **His winning day on Friday is a day my rules would
have ended after the first loss.** If I adopt his entry model whole, I adopt a second
trade with it, and §5 stops existing.

<!-- TODO: ask me — do I want a re-entry rule? If yes it is a CHANGE TO §5, made in -->
<!-- /review, in writing, between sessions. Never mid-session. If no, then his model -->
<!-- and mine differ on the single most important number in my risk file, and I need -->
<!-- to know that going in. -->

### 4b. "Move stop to break even"

Said in his chat, not by him, and not acted on. `risk-rules.md` §8: **the stop does
not move at all**, in either direction. Nothing here changes that.

### 4c. He has no fixed execution window

He starts at the open and stops because of a phone call:

> "I have a call in like 10 minutes"

My `02-session-plan.md` has a window starting at 09:40 and a **last permitted entry
that is still undefined.** His practice does not supply one — he simply trades until
he stops. <!-- TODO: ask me — this does NOT answer my window-end question. -->

### 4d. Discretion in size and target he does not state

He judges "better targets", "bigger move", "half decent" live. My §1 and §10 are
fixed numbers. Nothing here is convertible into either.

---

## 5. THE MOST IMPORTANT THING IN THIS TRANSCRIPT IS WHAT IS MISSING

His chat asks, five times:

> "Where's your stop loss? Where's your stop loss? Where's your stop loss, bro?
> Where's your stop loss? Where's your stop loss, bro? Hey, bro. Where'd you place
> that stop loss? You want to know about that stop loss?"

**He never answers. Not once, in the whole stream.**

`strategy/setups/a-plus.md` § "Stop placement rule" is the biggest gap in this repo —
it is the reason `/checktrade` returns INCOMPLETE, the reason sizing is improvised,
and the direct cause of the §1 oversize on 2026-08-28.

**That gap is not going to be filled from this source.** It is absent there too.

---

## 6. THE LESSON THIS TRADE ACTUALLY TEACHES

He shorted **NQ** because NQ made the SMT. The **targets he wanted were cleaner on
ES**. He said so before entering, and he named the exact failure out loud:

> "if ES ends up taking out this low without NASDAQ moving down ... that makes things
> a little bit more difficult"

ES reached the lows. NQ did not. He was stopped for a full loss on the instrument
that had the weaker draw, holding the correct directional read.

**The read was right. The instrument selection was wrong.** Being right about
direction and wrong about which ticker expresses it still pays −1R.

This lands directly on an open question in my own `a-plus.md`:

> "I take ONE trade per day (§5). If both NQ and ES present a valid setup in the same
> window, which do I take? This will happen often ... It needs an answer, not a
> preference."

The transcript shows the cost of getting that answer wrong. It does not give me the
answer. <!-- TODO: ask me -->

---

## 7. QUESTIONS THIS RAISES — to be answered one at a time

Mirrored into `OPEN-QUESTIONS.md`.

1. Is SMT divergence a **separate numbered condition** in my A+ setup, distinct from
   the cond. 10 other-index confirmation? If yes, define it.
2. When NQ and ES both qualify, **which do I trade** — the one that made the SMT, or
   the one whose target liquidity is cleaner? He chose the former and it cost him.
3. **What is my target hierarchy?** Are relative/triple equal lows and untapped 1H
   lows my draws, or just his?
4. Does a **re-entry after a stop-out** enter my model? That is a §5 change and can
   only happen in `/review`.
5. Is the **5M gap fill** part of my entry sequence, or is my 1M BOS sequence a
   different model that I should not blend with it?
6. **Was my 2026-08-31 SPX500 short taken from this stream or from my own chart?**
   `no-trade-conditions.md` has an unanswered prompt: *"Trade idea came from someone
   else's chart or a Discord/Twitter post?"* I shorted the S&P on 08-31. He shorted
   NQ, targeting lows, on what looks like the same day. If those are connected, that
   prompt stops being hypothetical and needs to become a real box on the list.

---

## 8. ONE LINE HE SAID THAT IS ALREADY MY RULE

> "But I don't want to force anything."

> "Not every single day is a winning day."

`risk-rules.md` §5: "One is a **CAP, not a quota.** ... A day with no setup is a day
with no trade, and that is a correct day, not a wasted one."
