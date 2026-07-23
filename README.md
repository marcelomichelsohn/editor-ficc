# The FICC editor

A proposal editor for **FICC 2026** — the *Fundo de Investimentos Culturais de
Campinas*, the municipal culture fund of Campinas, Brazil (call for proposals:
*Chamada Pública nº 003/2026*, in Portuguese an **edital**). Authors bring a
draft proposal; the editor gives it back **criticized, never rewritten**: every
finding quotes the exact excerpt of the draft and the exact item of the call,
re-read in the same turn.

> **Proponente brasileiro?** A instalação está em "Installation" abaixo (10
> minutos, claude.ai). O editor responde em português — a língua da sua
> proposta. Dúvidas sobre o edital: o FAQ não oficial em
> https://faqficc.vercel.app (43+ perguntas com fonte).

## What you get — and what you don't

**You get:** a critique in three heights, every round — (1) hard conformity
(eliminatory items, documents, limits, budget arithmetic), (2) strength of the
writing (is the objective a result or an activity?), and (3) strategy against
the call's scoring grid — each finding anchored in a quoted excerpt and a
quoted item of the call, with persistent IDs (F-01, F-02…) that survive into
re-review. It also declares, at the end of every round, what it could **not**
check.

**You don't get:** rewritten text, in any form — not even "an example of how
it could read". No ghost-writing, no filled-in fields, no shortcuts around the
call's rules (it refuses, and keeps refusing under pressure). The writing stays
yours; so does the final call on every finding.

**Who this is not for:** anyone who wants the proposal written for them; and
proposals outside FICC 2026 — the engine generalizes (see below), but this
build's source of truth is this call only.

## Installation (Claude Project, ~10 minutes)

1. On claude.ai: **Projects → New Project**. Name it, e.g., `Editor FICC 2026`.
2. In **Instructions** (custom instructions), paste exactly:

   You are the FICC editor. Read identity.md — it is who you are. Obey
   rules.md verbatim in every round. Your only source of truth about the call
   is the reference files (edital-2026, anexo-*, anexos-formularios,
   armadilhas, diff-2022-2026, qa-plantao-oficial). Answer in the language of
   the proposal.

3. In **Knowledge**, upload the files in two quick passes (claude.ai uploads
   files, not folders):
   - from the repo's root: `identity.md`, `rules.md`, `examples.md`;
   - then open `reference/` and upload all **11 files** inside it.
   That's 14 files total — nothing else.
4. Open a chat in the Project and paste your draft.

## What is in this folder

| File | Job | Load or verify? |
|---|---|---|
| `identity.md` | Who the editor is; how conflicts resolve | **Load** into the Project |
| `rules.md` | How it critiques — the operating law | **Load** |
| `examples.md` | What good critique looks like (bilingual, 3-block mold) | **Load** |
| `reference/` (11 files) | The call and its 13 annexes, verbatim + digested navigation layers | **Load** |
| `README.md` | This file | — |
| `WRITEUP.md` | How this was built, in three paragraphs | Read |
| `CREDITS.md` | Ideas borrowed from other entries, named openly | Read |
| `tests/verify.py` | Mechanical audit — runs offline, stdlib only, no API key | **Verify** — run it |
| `tests/sample-draft.md` + `gabarito.md` | Sample draft with answer key — including two false positives a correct round must NOT raise | **Verify** |
| `tests/cold-run/` | Preserved verbatim receipts of five real rounds — two dogfood + three consented third-party | **Verify** — never load |

The split matters: what you **load** is the product; what you **verify** is
evidence about the product. The editor never sees its own test material.

## Where this comes from

The author has been on both sides of this table. In January 2023 he wrote and
submitted "Espiral em Mim" to this same fund's previous cycle, in the name of
Regiane Bataglini, the proposal's registered proponent — songs of his own
composition, performed by her under Fernando Baeta's musical coordination.
The draft read like an event description. He paid a professional reviewer to look at it — and what
came back was a critique: item by item, anchored in the call's own text,
without a single rewritten sentence. The revised version won (official gazette
of Campinas, 31 March 2023, p. 16:
[DOM 13.058](https://portal-adm.campinas.sp.gov.br/sites/default/files/publicacoes-dom/dom/506314678603467865063131.pdf)).
This editor is that critique turned into a system. The before/after pair of
that proposal is the test material in `tests/cold-run/`.

## For the Weekly Comp #9 judges: check the claims, don't take them

Each claim below names where it would break. If you find the break, that
matters more than anything else in this repo.

1. **"It critiques, never rewrites."** Read any receipt in
   `tests/cold-run/rodada-{1..5}-output.md` (English renderings for rounds
   1–2: `*.EN.md`). Falsified if: any passage hands the author replacement
   text.
2. **"Every finding is anchored."** Run `python3 tests/verify.py` (offline,
   stdlib, ~2 s). Its mechanical scope, stated precisely: it verifies the
   **worked examples'** anchors and draft excerpts verbatim and their ID
   discipline; the **receipts** get their SHA-256 pinned and a scan for
   draft spans reproduced outside quoted excerpts (an edit-style rewrite
   would trip it; a rewrite in entirely new words would not — that seam is
   stated, not hidden). The receipts' own anchors are not re-checked by
   script — they are checkable by hand against `reference/`, and the
   walkthrough maps them round by round. `--selftest` proves the verifier rejects
   deliberately broken material, including a tampered hash and a smuggled
   rewrite — a verifier that passes everything proves nothing. Falsified
   if: a check passes on material you broke yourself.
3. **"Real use, preserved."** `tests/cold-run/` holds five full rounds run
   in the declared runtime — method written down **before** execution,
   inputs byte-for-byte, outputs pasted verbatim, errors kept. Rounds 1–2
   ran on the author's real 2023 proposal; round 2 is the behavior we have
   not seen elsewhere: the editor re-verifies its own 18 findings one by
   one (resolved / partial / not addressed), IDs intact, on a real
   before/after pair — and the scoreboard stays hard (11 not addressed) on
   a text that actually won. Rounds 3–5 are **consented third-party use**:
   three real FICC 2026 proposals from other proponents, anonymized in the
   input, each in a fresh chat (see the walkthrough). Falsified if:
   receipts contradict their inputs, or the walkthrough overstates them
   (`tests/cold-run/README.md` maps all IDs of rounds 1–2 and narrates
   3–5).
4. **"It knows it can be wrong — and shows it."** The receipts preserve
   every editor mistake of this cycle — four, plus one runtime glitch —
   unedited: an ambiguous line limit escalated to eliminatory in round 1
   (the official Q&A says otherwise); a dosage-rule violation found in an
   adversarial teardown; a `<parameter>` syntax token that leaked into a
   sentence of round 3; and — the pair that shows the improvement loop
   end-to-end — two findings of round 5 escalated to eliminatory against
   the product's **own** anti-inflation and intake rules, caught by the
   human operator challenging the round at its gate. Each time the same
   method ran: the mistake stays in the transcript, the confession is
   written down, and the rule that induced it is fixed at the source (the
   round-5 pair produced the two newest rules in `rules.md`, in the
   anti-inflation block). The editor also has an explicit withdrawal rule:
   convinced is different from worn down (`rules.md`).
5. **"Each file does one job."** The table above; cross-check any file
   against its stated job.

## Same engine, any call

Nothing in `identity.md` or `rules.md` is specific to culture funding: the
three heights, the citation gate, re-review with persistent IDs, and the
withdrawal rule are domain-independent. What binds this build to FICC 2026 is
`reference/` — swap it for another call's verbatim text and navigation layer
and you have that call's editor. We ship only the FICC build: depth over
surface, and this is the call the author knows from inside.

## Limits, stated honestly

- The rules are **prose, not code**, at runtime: a Claude Project follows
  markdown instructions. `verify.py` audits artifacts mechanically; the
  receipts show the behavior live — one preserved cycle, not a general proof
  of obedience.
- Rounds 1–2 are **dogfood**: the author's own material, declared as such.
  Rounds 3–5 are **consented third-party use** — three real FICC 2026
  proposals from other proponents, anonymized in the input, consent
  recorded — still a handful of preserved cycles, not a usage statistic.
- The editor **can be wrong** — four documented mistakes this cycle ("For
  judges", item 4), two of them caught only by a human challenging the
  round at its gate. Doubt lowers a claim, never raises it — and where the
  call's text ends, it says so and points to the Secretaria's mediators
  instead of guessing. The human gate is part of the method, not a backup.
- This is an independent tool: **not affiliated** with the Secretaria de
  Cultura de Campinas, and not legal advice.

## Evolution

The repo is tagged `as-submitted` at the competition deadline. Improvements
land on top of that tag, visibly, in the open — the way the three consented
third-party rounds and the two rule fixes they forced already landed before
it.
