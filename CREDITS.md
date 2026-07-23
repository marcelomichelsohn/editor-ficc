# CREDITS — ideas this build borrowed, and where each one lives

Reading the other entries of competitions #8 and #9 made this build better.
Naming what was borrowed is cheaper than pretending it wasn't. Each line says
where the idea shows up here.

- **Gabriel Azoulay (claimline)** — the self-tested verifier and the line
  that governs it: *"a verifier that passes everything proves nothing."*
  Lives in `tests/verify.py --selftest` and in this repo's README, § For
  judges. The falsify-me framing of that section follows his judge guide.
- **Jude Doocey (Cold Read)** — the negative control inside the answer key:
  an editor is also tested by what it must **not** flag. Lives in
  `tests/gabarito.md` (two forbidden false positives).
- **Mark Albano (Salesforce chat editor)** — the preserved two-round cycle
  (draft → critique → revision → re-review) as the thing worth shipping, not
  narrating. Lives in the design of `tests/cold-run/`.
- **Raph Mercado (Federal Proposal Editor)** — refusal demonstrated under
  *escalating* pressure, not asserted once. Lives in `examples.md`,
  Example 4.
- **Joshua Hubbard (CHALK)** — the README split between what you **load**
  and what you **verify**. Lives in this repo's README, folder table.
- **Craig Howard (SECOND PASS)** — this file. Crediting the community's
  ideas openly is his practice; borrowed like everything above.

The receipts' SHA-256 pinning (`tests/cold-run/SHA256SUMS`) follows a
practice seen in Cold Read and the Salesforce entry.
