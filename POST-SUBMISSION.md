# Post-submission rounds — real third-party feedback

Everything in this file happened **after** the `as-submitted` tag. Nothing
under the tag was edited (see README § Evolution): new evidence lands as a
new layer, labeled, never as a retouch of the old one.

## 2026-07-23 — the round-5 proponent replies

One day after receiving the round-5 critique (a PDF devolutiva of 12
findings, F-01 to F-12), the proponent of round 5 sent back a written reply
and four voice notes (~13 minutes). The voice notes were transcribed locally
(whisper, no cloud), with consent, anonymized to the same standard as the
round inputs, and preserved verbatim in
[`tests/post-submission/feedback-rodada-5.md`](tests/post-submission/feedback-rodada-5.md)
— Portuguese original followed by an English translation, same file.

What he did with the critique, unprompted:

- **Used it as a working checklist.** He went finding by finding, F-01 to
  F-12, and classified each one in his own words. His scoreboard: **resolved**
  F-02, F-04, F-05, F-07, F-10, F-12 · **in progress** F-01, F-06, F-08,
  F-11 · **open** F-03 (rights over AI-generated guide tracks — "the big
  problem") and F-09 (the 5-year record-keeping duty — "an unknown").
- **Asked for a second round on his own.** He will send a revised Anexo VI
  and asked whether he could submit it for re-review — the re-review with
  persistent IDs that `rules.md` § re-review defines. That round will be
  recorded here when it runs.
- **Proposed an improvement.** A per-item progress map: every scoreable item
  of the call as a cell that clears when the proposal satisfies it, so the
  author sees exactly where the gaps are.

## What this changed in the product

The two findings he stalled on — F-03 and F-09 — are precisely the two whose
remedy was **his decision**, not a text fix; and nothing in the finding line
said so. He also could not decode the summary's color legend ("I didn't
understand the difference between the colors, which weight is which") — and
that was already the redesigned legend. A failure found by a real reader,
where self-critique had declared the problem solved.

Both fixes landed at the source, in `rules.md` (v4, committed on top of the
tag — the diff is public):

1. **`DECISÃO SUA` ("your call") marker** — appended to a finding line when
   the remedy is a choice only the author can make. The critique names the
   decision and what each option involves; it never makes it for the author.
2. **Self-describing finding line** — every label written out with its name
   (`Altura 1: Conformidade com o edital · Gravidade: … · Confiança: …`), so
   no line needs the legend to be decoded; plus the legend itself rewritten
   in plain language.

His progress-map idea is **queued, credited to him**, with two safeguards
already fixed: only an item actually re-read in the round may clear a cell,
and the map never predicts the official reviewer's score — that judgment
belongs to someone else.

## Ruleset labeling

All five receipts in `tests/cold-run/` were produced under the **previous
ruleset** — `rules.md` as of the `as-submitted` tag. They stay untouched
(their SHA-256 pins would flag any edit). Rounds run from here on use v4 and
will say so in their records.
