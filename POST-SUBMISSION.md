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

## 2026-07-23 — round 6: a second real proponent, first round under v4

Later the same day, a second colleague from the FICC plantão brought a real
proposal — a book-publication project, Literature area — with consent to run
the round and to publish it anonymized. Same protocol as round 5: the input
was anonymized **before** it entered the runtime (author → "P."; artistic
name → "[nome artístico removido]"; the work's title and the fictional
character's name kept), so the receipt was born clean.

- Input: [`tests/post-submission/rodada-6-input.md`](tests/post-submission/rodada-6-input.md)
- Receipt: [`tests/post-submission/rodada-6-output.md`](tests/post-submission/rodada-6-output.md)
  — **the first receipt produced under `rules.md` v4.**

What v4 changed, visibly, against the failure modes of round 5:

- **No absence-in-chat findings.** The budget sheet, team roster and
  résumés that were not pasted into the chat went to "Not checked this
  round" — the receipt itself says "Documento não visto é não verificado,
  não ausente" ("a document not seen is unverified, not absent").
- **The single ELIMINATÓRIO names a real mechanism.** It anchors to an
  eligibility condition of the modality (Anexo I, 10.2.1.2 — the proponent
  must be the author of the work), is explicitly conditional on a fact only
  the author can confirm, and carries the `DECISÃO SUA` marker instead of
  asserting the fact.
- **An ambiguous deadline stayed ambiguous.** The call contradicts itself
  on the execution deadline (item 8.1 names "31 June 2027", a date that
  does not exist; Anexo X says 31 December 2026); the receipt flagged the
  contradiction and sent it to the Secretaria's mediators, A CONFERIR,
  without picking a side. *(The mediators have since answered: the final
  execution date is 30 June 2027 — "31 June" is a typo and the Anexo X date
  was corrected. The receipt stays untouched; the resolution lives in
  `reference/armadilhas.md` and in the official Q&A, with its date and time.
  This is the loop working: the editor refused to guess, the question went to
  the people who own the answer, and the answer came back into the source.)*

One known caveat, preserved unedited: finding F-04 bites the marker
"[nome artístico removido]" — an artifact of this repo's own
anonymize-before-run protocol, not the author's text. The editor read what
it received; the finding is correct for its input. Details in the receipt's
header note.

## Ruleset labeling

All five receipts in `tests/cold-run/` were produced under the **previous
ruleset** — `rules.md` as of the `as-submitted` tag. They stay untouched
(their SHA-256 pins would flag any edit). Round 6 ran under v4, as its record
says.

`rules.md` has moved twice since: **v5** (24 July) fixed the two deviations
round 6 exposed — the date of an interpretation is copied from its source
block instead of compressed into a range, and the opening summary matches the
sections ID by ID and is written last. **v6** (24 July) added one sentence to
the anti-rubber-stamp guard: if every section closed with an instant verdict,
the editor confirmed instead of challenged. The same day, `reference/` was
updated — the official Q&A grew from 43 to 63 pairs, and the execution
deadline stopped being an open ambiguity (see the round-6 note above). Rounds
from here on run under v6 and say so in their records.
