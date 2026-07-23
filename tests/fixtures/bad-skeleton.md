# fixture: planted-bad skeleton (selftest only — this file is SUPPOSED to fail)

This file imitates the rules.md skeleton with a seventh section that offers
rewritten text — the exact slot this editor must never have. If
`verify.py --selftest` does not reject it, the verifier itself is broken.

## Output skeleton (fixed — no rewrite slot)

```
ROUND N — [date] — [area / modality]

1. Findings — detailed
2. Findings — compact
3. Strength (exactly one, or none)
4. Not checked this round
5. Where NOT to spend effort
6. Next step
7. Suggested rewrite of the weakest passage (versão sugerida)
```
