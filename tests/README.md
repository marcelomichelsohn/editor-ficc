# tests/ — executable proof, in three layers

| Layer | What | How to run / read |
|---|---|---|
| Mechanical | `verify.py` — audits the bundle's artifacts offline (anchor quotes verbatim in `reference/`, anchor↔item link, draft excerpts vs. real inputs, no rewrite slot in the skeleton, finding-ID discipline). Stdlib only, no API key. | `python3 tests/verify.py` · `--selftest` proves it can fail (planted-bad `fixtures/` must be rejected) |
| 60-second test | `sample-draft.md` (synthetic defective draft) + `gabarito.md` (what the editor must flag — and the two traps it must NOT flag). | paste the sample into the editor, compare with the gabarito |
| Real use | `cold-run/` — preserved verbatim receipts of five real rounds: two on the author's own 2023 winning proposal (including the re-review ID by ID), three consented third-party rounds on real FICC 2026 proposals. Method declared before execution. | read `cold-run/README.md` first |

Honesty note: `verify.py` audits **artifacts**; the rules themselves are
prose, and no script proves a live session obeys them. The live evidence is
the preserved cold run — reproducible by anyone with this repo in minutes.
