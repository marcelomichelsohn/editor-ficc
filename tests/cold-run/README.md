# tests/cold-run/ — Preserved receipts of real use

This folder holds the **verbatim transcripts** of real editor rounds — two
dogfood rounds on the author's own material, plus three consented
third-party rounds (rounds 3–5, added as they ran, per method item 3
below) — and the exact inputs that produced them. Everything a judge needs
to audit — or reproduce — the cycles is here.

## Method — declared on 22 July 2026, BEFORE the rounds were run

These rules were written down before execution, so the receipts could not be
shaped after the fact:

1. **Runtime:** a Claude Project on claude.ai — the product's declared
   runtime — operated by the author (Marcelo Michelsohn). The Project
   contains **only the files of this repo** (identity.md, rules.md,
   examples.md and the 11 files of `reference/`), with the project
   instructions given in the README's installation section. The `tests/`
   folder is **not** uploaded: the editor never sees expected-findings
   material. The model and date are recorded in each receipt header.
2. **Inputs:** `rodada-1-input.md` and `rodada-2-input.md` are the exact
   messages pasted, byte for byte. The proposal text in each is the
   **integral plain-text export** (Google Docs → File → Download → Plain
   text) of a dated version from the version history of the author's real
   2023 proposal ("Espiral em Mim"): round 1 uses the version of
   **3 Jan 2023, 20:27** (the draft the consultant received that night);
   round 2 uses the version of **10 Jan 2023, 16:06** (the closest
   surviving version to the one submitted). Typos, formatting quirks and
   template leftovers are preserved; nothing was abridged or cleaned.
3. **This is the author's own material (dogfood), declared as such.** No
   third-party proposal appears here. If a consented third-party review
   happens (via the public FAQ site's free-review offer), it will be added
   as its own labeled round — never mixed with these.
4. **The revision between the two rounds is historical.** The author revised
   the proposal in January 2023 in response to a human consultant's critique,
   and that revised version won (result published 31 March 2023 in Campinas's
   official gazette). Round 2 therefore demonstrates the editor's re-review
   behavior — persistent IDs verified one by one — on a **real** before/after
   pair. We do **not** claim the author revised in response to round 1.
5. **Receipts are pasted verbatim and never edited.** Errors of the editor,
   if any, stay in the transcript. We assume asymmetrically that the editor
   made **at least one** mistake across the two rounds; anything found is
   noted in the round record, not cleaned.
6. **Anachronism, declared:** the proposal was originally written for the
   2022 cycle; the editor reviews it against the **2026** reference — as a
   real author reusing old material for the current call would ask. Findings
   about 2022→2026 differences are expected and desirable.
7. **What this proves — and what it doesn't.** It proves one real, preserved
   usage cycle, including the re-review that no other entry demonstrates
   with persistent IDs. It does **not** prove the runtime obeys the rules in
   general — the rules are prose, not code; `tests/verify.py` audits the
   artifacts mechanically, and this folder shows the behavior live, once,
   unedited.

## Files

| File | What it is |
|---|---|
| `rodada-1-input.md` | Exact message pasted in round 1 (2023-01-03 draft, pre-critique) |
| `rodada-1-output.md` | The editor's full critique, verbatim |
| `rodada-2-input.md` | Exact message pasted in round 2 (2023-01-10 as-submitted version) |
| `rodada-2-output.md` | The editor's re-review, ID by ID, verbatim |
| `rodada-3-input.md` | Exact message pasted in round 3 — a **consented third-party proposal** (another FICC 2026 proponent), anonymized before pasting (natural persons → role + initial); each third-party proposal runs in a fresh chat, so the receipt header reads "ROUND 1" (first round of that proposal) |
| `rodada-3-output.md` | The editor's full critique of the third-party proposal, verbatim — including a runtime glitch in F-01 (a `<parameter>` tool-syntax token leaked into a sentence), kept unedited as the method requires |
| `rodada-4-input.md` | Exact message pasted in round 4 — a second **consented third-party proposal** (same proponent-colleague, different project), anonymized before pasting; fresh chat, so its header also reads "ROUND 1" |
| `rodada-4-output.md` | The editor's full critique, verbatim — the first round run with the revised `rules.md` (fixed legend, opening summary, no-promise rule), all three visible in the output |
| `rodada-5-input.md` | Exact message pasted in round 5 — a third **consented third-party proposal** (a different proponent-colleague), anonymized before pasting; fresh chat, header reads "ROUND 1" |
| `rodada-5-output.md` | The editor's full critique, verbatim — **including two editor mistakes kept unedited** (F-02 and F-03 escalated to eliminatory on ambiguous scope / unpasted attachments, against the product's own anti-inflation and intake rules; caught by a human challenge at the gate and confessed in the round record) |
| `rodada-*-output.EN.md` | English renderings (translations) of the rounds 1–2 receipts — **not** the receipts; the pt-BR originals govern. Rounds 3–5 are pt-BR only — for a full reading, paste any of them into any AI and ask for a translation |
| `SHA256SUMS` | SHA-256 of every file above, pinned at capture — `tests/verify.py` recomputes them and fails on any drift |

## What ran, and what it showed — a guide for non-Portuguese readers

*(Written after the rounds. The method above was declared before them; the
receipts are in Portuguese because the editor answers in the proposal's
language — that is the product working, not an oversight. Full English
renderings: `rodada-1-output.EN.md` / `rodada-2-output.EN.md`.)*

**Round 1** (22 Jul 2026, Claude Fable 5, low reasoning effort): first full
critique of the pre-critique 2023 draft. 18 findings, F-01..F-18, each
anchored in a verbatim quote from the 2026 call, checkable against
`reference/` in this repo; most also quote the draft verbatim, checkable
against `rodada-1-input.md`. Findings of **absence** (F-08, F-09 — documents
not presented; F-13 — a field left unanswered) have no draft line to quote,
by nature; F-02's "excerpt" is the document as a whole.
Severity triage put the one clock-dependent eliminatory item (venue consent
letters, which depend on third parties) as the single "do this today" step.

**Round 2** (same chat, second message): the re-review — the behavior no
other entry demonstrates. The editor verified its own 18 findings one by one
against the as-submitted version that actually won FICC 2022. Scoreboard:
**1 RESOLVED · 6 PARTIAL · 11 NOT ADDRESSED**, plus 2 new findings.

| ID | Finding (one line) | Round-2 verdict |
|---|---|---|
| F-01 | Still on the 2022 form; the 2026 form is different | NOT ADDRESSED |
| F-02 | Over the 150-line limit | NOT ADDRESSED* |
| F-03 | Venues without consent letters | PARTIAL (list closed; letters missing) |
| F-04 | Counterpart section no longer exists in 2026 | NOT ADDRESSED |
| F-05 | 2022 "social counterpart" ≠ 2026 accessibility criterion | PARTIAL |
| F-06 | No team roster / inducer declarations (up to 5 points) | NOT ADDRESSED |
| F-07 | Schedule and dates are 2023's | NOT ADDRESSED |
| F-08 | Budget sheet not presented | NOT ADDRESSED |
| F-09 | Résumés + schedule attachments missing | NOT ADDRESSED |
| F-10 | "Categoria" field does not exist in 2026 | NOT ADDRESSED |
| F-11 | Previously awarded project → activity report required | NOT ADDRESSED |
| F-12 | "Option 1 / Option 2" menus instead of one plan | **RESOLVED** |
| F-13 | New age-range field unanswered | NOT ADDRESSED |
| F-14 | Accountability design is 2022's | NOT ADDRESSED |
| F-15 | Modality's complementary info (repertoire/links) | PARTIAL |
| F-16 | Third-party covers → author authorization | PARTIAL / TO CONFIRM |
| F-17 | Typos and template leftovers | PARTIAL |
| F-18 | Objectives not measurable | PARTIAL |
| F-19 | *(new)* "5% of tickets" in shows declared free | — |
| F-20 | *(new)* 2022/23 history narrated as news | — |

Three moments worth a judge's attention:

1. **Cross-version memory:** the editor caught that a band member is spelled
   "Wanessa" in the round-1 draft and "Vanessa" in the round-2 version — a
   real discrepancy that matters on the team roster — and asked the author
   which is correct instead of picking one.
2. **Honest framing:** round 2 opens by stating that the second version is
   the historical document that won the 2022 cycle, not an adaptation to
   2026 — and the scoreboard stays hard (11 NOT ADDRESSED) instead of
   inflating "resolved" counts on a winning text.
3. **Downgrade instead of assertion:** on F-16 the editor could not verify
   the authorship of 3 songs, so it downgraded the finding to "TO CONFIRM"
   and asked the author — the product's signature rule (no flag without a
   quote) operating live.

*\* F-02 is also one of the editor's four mistakes in this cycle, kept
in the receipts as the method requires: it read the form's "150 lines" note
as a per-document cap and escalated it to eliminatory; the official Q&A
(`reference/qa-plantao-oficial.md`) says the limit is per topic. The rule
that induced the error was fixed at the source after the rounds — the
receipts stay untouched.*

*The second known mistake: in round 1 the editor placed two `ELIMINATÓRIO`
findings (F-08, F-09) in the compact one-line section, which `rules.md`
forbids ("a finding that eliminates never gets one line"). Found in an
adversarial teardown after the rounds; noted here, never cleaned.*

*A phrasing note: the author's round-2 preamble calls the pasted text "the
version I actually submitted"; the method's phrasing above — the **closest
surviving version** to the one submitted — is the precise one (the exact
submitted file was not preserved; the 10 Jan 16:06 version history entry is
the nearest snapshot).*

## Rounds 3–5 — consented third-party use (22 Jul 2026)

Three real FICC 2026 proposals from other proponents, reviewed with
recorded consent. They came from direct outreach on deadline week: the
author messaged twelve people from the Secretaria's official Q&A group —
none of whom he knows personally — offering a free review. Five answered:
one said the project was not ready yet, two said they would still send
theirs, and two sent proposals (one sent two, the other one) — the three
proposals that became rounds 3, 4 and 5. Anonymization happened **in the
input**, before pasting (natural persons → role + initial; personal
identifiers removed), so the receipts were born clean. Each proposal ran
in a **fresh chat** — the runtime has no memory across chats — which is
why each header reads "ROUND 1": it is round 1 of that proposal. All three
ran on Claude Fable 5, medium reasoning effort (rounds 1–2 ran on low).
These three receipts are pt-BR only — the originals govern in any case;
for a full reading, open `rodada-3-output.md`, `rodada-4-output.md` or
`rodada-5-output.md` and ask any AI for a translation.

**Round 3** ("Travessia", voice-and-repertoire album): 12 findings. The
receipt preserves a **runtime glitch, unedited**: in F-01, a `<parameter>`
tool-syntax token leaked mid-sentence. Prose rules cannot prevent a
generation glitch — the answer is detection, and a syntax-artifact check
went to the improvement backlog. The round also exposed a UX gap (labels
like F-01 and "heights" mean nothing to a first-time proponent) that
produced three rule changes at the source after it: the fixed legend, the
opening summary, and the ban on promising future work inside a critique.

**Round 4** ("Todo Batuque do Meu Samba", instrumental samba album): first
round on the revised rules — legend, opening summary and neutral "not
checked" framing all visible in the output, and the runtime scan came back
clean. Detail worth a judge's minute: the proponent's form carried the
**wrong modality name** (the number of the album modality with the name of
the circulation one); the editor framed the whole round under the correct
modality and made the mismatch its top finding, instead of inheriting the
error.

**Round 5** ("Horizonte de Eventos", alternative rock album): the round
where the **human gate caught the editor breaking its own rules** — and
the reason this section is worth reading. Two findings (F-02, consent
letters for the recording studios; F-03, the modality's complementary-info
attachment) were escalated to eliminatory-and-confirmed on (a) a scope
ambiguity the finding itself admits in writing, and (b) attachments that
simply were not pasted into the chat — against the product's own
anti-inflation and intake rules. The operator challenged both at the gate;
re-reading the sources sided with the challenge (the official Q&A even
records that a missing consent letter can be presented after approval, and
that for another area the locais item can be declared not applicable).
Mistakes 3 and 4 of the cycle, same method as always: **the receipt stays
untouched, the confession is written down, and the cause was fixed at the
source** — the two newest rules in `rules.md`'s anti-inflation block ("the
chat is not the inscription"; "ELIMINATÓRIO names the mechanism") exist
because this round forced them. That is the improvement loop this product
claims, operating live: receipt → human gate → confessed error → source
fix, in the open.
