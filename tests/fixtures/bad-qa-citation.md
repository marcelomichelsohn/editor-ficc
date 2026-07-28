# Planted-bad fixture — a true timestamp bound to the wrong entry

This file is deliberately broken. Check 9 (`qa-citation-address`) MUST fail on
it; `python3 tests/verify.py --selftest` proves that it does. It reproduces the
defect found in the round-7 receipt, in miniature: the claim is correct, the
timestamp is real and exists in `reference/qa-plantao-oficial.md` — and it sits
under a different question than the one the citation names. A verifier that
passes this proves nothing.

**[F-01] · Altura 1: Conformidade com o edital · Gravidade: SUGESTÃO · Confiança: CONFIRMADO**

- Trecho do rascunho: campo 4.1, mês 6 — *"Confecção de relatório final e
  prestação de contas do projeto."*
- Interpretação oficial: na inscrição vai só até o Anexo VII (planilha
  orçamentária) (Q&A do plantão, "Como entrego o material finalizado e quando
  presto contas?", 22/07/26, 09:07:06).
- Por que importa: o carimbo é verdadeiro e a afirmação é verdadeira — mas a
  entrada nomeada é outra. O par pergunta + carimbo é o que denuncia isso.
