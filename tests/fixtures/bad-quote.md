# fixture: planted-bad anchor (selftest only — this file is SUPPOSED to fail)

This file imitates the examples.md structure with an anchor whose quote does
NOT exist in reference/. If `verify.py --selftest` does not reject it, the
verifier itself is broken.

### O artefato (pt-BR — canonical)

```
[F-99] · altura 1 (dura) · ELIMINATÓRIO · CONFIRMADO
- Trecho do rascunho: "um trecho qualquer de rascunho usado só no selftest"
- Âncora no edital: item 12.1 — "Esta frase foi plantada e não existe em
  nenhum arquivo do reference deste pacote."
- Por que importa: se o verificador aceitar esta âncora, ele não verifica nada.
- O que fazer: nada — este arquivo existe para ser reprovado.
```

### English rendering (translation for judging; the pt-BR block is canonical)

```
(translation omitted — selftest fixture)
```
