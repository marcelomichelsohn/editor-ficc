# Competition Writeup

**What I built:** A proposal editor for FICC 2026 — the municipal culture fund
of Campinas, Brazil, a call I know from inside. In 2023 I wrote and submitted a
proposal to this fund's previous cycle, in the name of its registered
proponent, Regiane Bataglini; I paid a professional reviewer to critique it,
and the revised version won. This editor is that critique turned into a
system: it reads a draft and returns findings in three heights — hard
conformity, strength of the writing, strategy against the scoring grid — each
anchored in a quoted excerpt of the draft and a quoted item of the call,
re-read in the same turn, each with a persistent ID that survives into
re-review. It never hands the author rewritten text. Around the product sits
its evidence: an offline verifier (`tests/verify.py`) and five preserved real
rounds — two on my own 2023 proposal, three consented rounds on real FICC 2026
proposals by other proponents.

**One design decision:** Receipts are immutable. The editor got things wrong
four times this cycle; each time the mistake stayed in the transcript, the
confession was written next to it, and the rule that induced it was fixed at
the source — the round-5 pair produced the two newest rules in `rules.md`.
Re-running until the transcript looked clean would have given me prettier
receipts and no evidence.

**One thing I'd add:** The bundle has two kinds of files, and the split
matters here. `identity.md` and `rules.md` define how the editor criticizes —
the three heights, the anchoring rule, re-review with persistent IDs. They
would work, unchanged, for any public call: nothing in them mentions culture
funding. What binds this build to FICC 2026 is a single folder, `reference/`:
the call's own text, copied word for word, plus the navigation files the
editor uses to move around in it — the traps catalog, the diff against the
previous cycle, the official Q&A. Building that folder was AI work
already — I pointed Claude at the published PDFs and it extracted everything —
but it happened in my own workspace, as a bespoke session, not inside the
product. That is what I would add: a packaged step where any user hands the
editor a new call's published PDF and it builds that call's `reference/`
itself. With that piece in place, the same engine serves any call. Without
it, I chose to ship one call, the FICC 2026, built deep — the one I know from inside.
