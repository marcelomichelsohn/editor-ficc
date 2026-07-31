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
  — **the first receipt produced under `rules.md` v4.** Both files are pinned
  by SHA-256 in `tests/post-submission/SHA256SUMS` and checked by
  `tests/verify.py`, exactly like the five receipts of the submitted build:
  the guarantee covers every round, not only the ones that shipped first.

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

## 2026-07-23 — two chains: the editor refuses to guess, and the answer comes back in under a minute

The editor's first rule is that it may assert a violation only after re-reading
the cited item in the same turn. Where the call itself is ambiguous, it does not
resolve the ambiguity — it names it and sends the proponent to the Secretaria's
mediators, who own the answer. Two rounds produced exactly that instruction, and
both proponents went and asked. Both exchanges were re-read line by line in the
raw export of the official help desk group (a WhatsApp group with 237 members)
before being written here; no participant is named.

**Chain 1 — the deadline that does not exist (round 5).** Finding F-08 of the
round-5 devolutiva is a one-line compact: the proposal's month-by-month schedule
had no anchor to the contract's term, item 8.1 of the call names a finalization
date of "31 June 2027" — a date that does not exist — and Anexo X, clause 7.1
says 31 December 2026. The finding did not pick a side; it told the author to
confirm the real deadline with the mediators before assuming any slack. The
proponent took it to the group **as their own question, in their own words** —
they did not paste the editor's output — at **15:49:24**. The help desk answered at
**15:49:57**: "30 de junho de 2027". Thirty-three seconds, in public, in front
of 237 people. The impossible date had been circulating in that group since
14 July, and had been repeated in an official answer.

**Chain 2 — what counts as an unreleased album (rounds 3 and 4).** The receipts
of rounds 3 and 4 told that proponent to ask the mediators whether re-recordings
and new arrangements of already-known songs fit "Projetos de Gravação de Álbum
Inédito" (Anexo I, 11.2.2) — an ambiguity the editor explicitly refused to
settle. They asked in the group at **16:13:04** and were answered at
**16:13:31**: "Olá, pode sim!" Twenty-seven seconds. On 26 July they confirmed
that they had already assumed that answer, and that it was useful for the
system to make them check it with the people who decide.

What this says about the design: the value is not in the answer. It is in the
routing. A tool that refuses to guess sends traffic to the source of truth — and
one of these two questions corrected the call's deadline for an entire room, not
only for the person who asked.

## 2026-07-27 — round 7: a third proponent, the first receipt under v6, and one defect confessed

A third real proponent — a Multilinguagens project (a costume exhibition plus a
printed publication) — sent her Anexo VI on 27 July. Consent was asked for and
given **before anything was processed**, in two explicit parts: to run the
analysis, and to publish the material without her name. First round under
`rules.md` **v6**, with `reference/` at the current curation of the official
Q&A. The receipt carried 20 findings: 1 ELIMINATÓRIO, 13 PERDE PONTOS,
6 SUGESTÃO.

Two things are worth recording.

**The double-anchor check ran as a script, not as a reading.** Every quotation
in the receipt was matched — normalized — against the proposal text and against
each file in `reference/`; every cited item number was located in its source and
read, which meant resolving the numbering collisions by hand (12.1, 7.3, 7.4,
13.1, 16.4.1 and 8.1 all exist in more than one file, with different texts); and
all 44 help-desk timestamps cited in the receipt were searched in
`reference/qa-plantao-oficial.md`. Result: 20 of 20 findings carry both anchors,
all 44 timestamps exist, the opening summary's counts match the findings ID by
ID, and no sentence of the author's text was rewritten anywhere.

**The check found one defect — and it is the exact failure this product preaches
against.** In the closing section on where *not* to spend effort, the receipt
cited a real help-desk timestamp, one that exists in the file, bound to the
**wrong entry**. The claim ("at submission you file only up to Anexo VII") is
correct and is in the official Q&A — but under a different question. A true
identifier attached to the wrong statement. Rule #1 of `rules.md` requires
re-reading the cited item verbatim in the same turn; it was written for the text
of the call, and help-desk timestamps were being treated as topic labels rather
than as addresses to open.

**The fix went to the source before any new proposal was run** — the same order
as every other rule fix here — and it went one step past the rule. `rules.md`
**v7** closes Rule 1 with a subsection, *Citing the Q&A — the entry is the
address*: locate the entry whose `Fonte` line carries the timestamp before
citing it; never run the lookup backwards from a topic to a plausible date; and
**carry that entry's question in the citation**. The anti-easy self-audit gained
a matching question, answered before delivery: a timestamp that came from memory
or from a neighbouring entry is removed, not repaired.

That last requirement is the part worth reading twice, and it is not about
style. A bare timestamp is **true wherever it is pasted** — which is exactly why
no script could catch this defect, and why a human had to. Once the citation
carries the question, the pair becomes checkable in one step, and
`tests/verify.py` gained **check 9**: the question named must exist as an entry
heading in `reference/qa-plantao-oficial.md`, and that entry's `Fonte` line must
list the cited timestamp. A timestamp cited with no question fails too. The
planted-bad fixture reproduces this very defect in miniature, and `--selftest`
proves the check rejects it. **An error the editor made became a check the
editor cannot make again silently.**

Its limit, stated rather than implied: **no receipt published here obeys the new
format yet.** The five rounds of the submitted build and round 6 predate it;
round 7's files are withheld for the reason below. Today check 9 verifies the
example inside the rule itself and waits. Its live proof arrives with the first
round run under v7 — not with this commit.

**Had this happened before?** Every published receipt was swept for the same
defect. None of them cites the Q&A by timestamp at all: they cite it by date,
and several compress a range of days (`13–21/07/26`) — the deviation **v5**
already fixed and confessed. A date names a day, not an entry; many answers can
share one. So those citations carry no address to be wrong about, and this class
of defect could not have arisen there in the form it took in round 7 — the
timestamp only became citable when v5 made the time mandatory, which made round
7 the first receipt that could commit this error, and it committed it once in
thirteen citations. **That does not clear them.** Whether a date-only citation
supports the claim attached to it is not checkable by script at that
granularity, and the entry-by-entry reading was not done. Every audit run prints
how many such citations exist, so the gap stays counted instead of forgotten.

**Why this round's input and receipt are not published here.** Every previous
round published both, pinned by SHA-256. This one publishes neither, and the
reason is a rule rather than an omission: the proposal declares the proponent's
own health condition as part of her accessibility argument, and the receipt
quotes it. Dropping her name would not anonymize the document — the project
title, three named works with their directors and three named venues identify it
uniquely, and the city publishes the result of the call in the Diário Oficial
(item 12.16), which pairs project and proponent by name. Editing the receipt to
remove the finding was refused for a different reason: a receipt is a recording,
and the SHA-256 pins exist precisely so that nobody, including us, can retouch
one. So the round is narrated and its files are withheld. **The record stops
where a person's sensitive data begins.** Her consent covered publication
without her name; it did not cover this, and asking her for more four days
before the deadline would serve this repo, not her.

## Ruleset labeling

All five receipts in `tests/cold-run/` were produced under the **previous
ruleset** — `rules.md` as of the `as-submitted` tag. They stay untouched
(their SHA-256 pins would flag any edit). Round 6 ran under v4, as its record
says.

`rules.md` has moved since, and every move was forced by a round: **v5**
(24 July) fixed the two deviations
round 6 exposed — the date of an interpretation is copied from its source
block instead of compressed into a range, and the opening summary matches the
sections ID by ID and is written last. **v6** (24 July) added one sentence to
the anti-rubber-stamp guard: if every section closed with an instant verdict,
the editor confirmed instead of challenged. The same day, `reference/` was
updated — the official Q&A was extended (43 pairs at submission; it has kept
growing since, every time the help desk answered), and the
execution deadline stopped being an open ambiguity (see the round-6 note
above). The file is its own count: `reference/qa-plantao-oficial.md` carries
the provenance in its header, and any number quoted elsewhere would drift the
next time the help desk answers.

**v7** (27 July) is the fix round 7 forced, described above: the Q&A is cited by
address, the citation carries its entry's question, and check 9 verifies the
pair. Round 7 ran under v6 and says so in its record; rounds from here on run
under v7.
