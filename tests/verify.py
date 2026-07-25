#!/usr/bin/env python3
"""verify.py — mechanical audit of this bundle's artifacts.

Runs offline: Python 3 standard library only, no API key, no network.

What it checks (and what it honestly cannot):
  1. anchor-quote-verbatim  — every call quote cited as an anchor in
     examples.md exists VERBATIM in a file of reference/ (typos included).
  2. anchor-item-link       — the item number named by each anchor
     (e.g. "12.1") appears in the SAME reference file that contains the
     quote — the quote is not pinned to the wrong item.
  3. draft-excerpt-verbatim — draft excerpts quoted in the worked examples
     exist verbatim in the real round inputs preserved in tests/cold-run/.
  4. skeleton-no-rewrite    — the output skeleton in rules.md has exactly
     the six numbered sections and none of them offers rewritten text.
  5. example-id-discipline  — finding IDs in examples.md are sequential,
     never duplicated, and the re-review only verifies IDs that exist
     (new ones are explicitly marked).
  6. receipt-integrity      — every receipt matches its SHA-256, and no
     receipt exists outside its manifest. Both receipt folders are covered:
     tests/cold-run/ (the five rounds of the submitted build) and
     tests/post-submission/ (rounds run after it). A receipt that silently
     drifts from what was captured is worse than no receipt — and the newest
     round is where drift would hurt most.
  7. no-rewrite-scan        — in each preserved receipt, no 8-word span of
     the author's draft reappears OUTSIDE an explicitly quoted excerpt, and
     no offer-to-rewrite phrasing appears. This catches edit-style rewrites
     smuggled around the quote discipline; a rewrite composed of entirely
     new words is beyond any string check — that seam is stated, not hidden.
  8. runtime-artifact       — no tool-syntax token (<parameter>, <invoke>…)
     leaked into a receipt's prose, except the occurrences already confessed
     and counted in RUNTIME_ARTIFACT_ALLOWED. The count is exact in both
     directions: a new leak fails, and so does a confessed glitch quietly
     removed. Prose cannot prevent a runtime glitch; this refuses to let a
     new one pass unnoticed.

This audits the ARTIFACTS, not the runtime: the rules are prose, and no
script can prove a live session obeys them. The live evidence is in
tests/cold-run/ (preserved receipts).

Usage:
  python3 tests/verify.py             # audit the bundle (exit 0 = green)
  python3 tests/verify.py --selftest  # prove the verifier can fail:
                                      # planted-bad fixtures MUST fail
"""

import hashlib
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REFERENCE = ROOT / "reference"
EXAMPLES = ROOT / "examples.md"
RULES = ROOT / "rules.md"
COLD_RUN = ROOT / "tests" / "cold-run"
POST_SUBMISSION = ROOT / "tests" / "post-submission"
RECEIPT_DIRS = (COLD_RUN, POST_SUBMISSION)
FIXTURES = ROOT / "tests" / "fixtures"

FAILURES = []


def fail(check, msg):
    FAILURES.append((check, msg))


def norm(s: str) -> str:
    """Collapse whitespace so line-wrapping differences don't matter.
    Nothing else is normalized: accents, typos and punctuation must match."""
    return re.sub(r"\s+", " ", s).strip()


def pt_blocks(text: str):
    """Yield only the canonical pt-BR artifact blocks of examples.md.
    (The English blocks are translations — never checked verbatim.)"""
    for m in re.finditer(
        r"### O artefato.*?\n(.*?)(?=### English rendering|\Z)", text, re.S
    ):
        yield m.group(1)


def load_reference():
    files = {}
    for p in sorted(REFERENCE.glob("*.md")):
        files[p.name] = norm(p.read_text(encoding="utf-8"))
    return files


def extract_anchors(block: str):
    """(label, item, quote) for every anchored call citation in a block."""
    out = []
    for m in re.finditer(r'Âncora no edital: item ([\d.]+) — "(.+?)"', block, re.S):
        out.append((f"item {m.group(1)}", m.group(1), m.group(2)))
    for m in re.finditer(r'Anexo ([IVX]+), ([\d.]+) — "(.+?)"', block, re.S):
        out.append((f"Anexo {m.group(1)}, {m.group(2)}", m.group(2), m.group(3)))
    for m in re.finditer(r'Reli o item ([\d.]+): "(.+?)"', block, re.S):
        out.append((f"item {m.group(1)} (releitura)", m.group(1), m.group(2)))
    return out


def item_in(text: str, item: str) -> bool:
    """Item number appears in the text, not as part of a longer number."""
    return re.search(r"(?<![\d.])" + re.escape(item) + r"(?![\d])", text) is not None


def check_anchors(text: str, reference: dict, check="anchor"):
    """Checks 1 and 2 on the pt-BR blocks of the given examples text."""
    n = 0
    for block in pt_blocks(text):
        for label, item, quote in extract_anchors(block):
            n += 1
            q = norm(quote)
            # Standard quotation practice: the FINAL punctuation mark may be
            # adapted (the call ends list items with ";", a quote may close
            # with "."). Everything inside the quote must match verbatim.
            q_core = q.rstrip(".;,")
            homes = [name for name, body in reference.items()
                     if q in body or q_core in body]
            if not homes:
                fail(check, f"quote for {label} not found verbatim in reference/: \"{quote[:80]}…\"")
                continue
            if not any(item_in(reference[h], item) for h in homes):
                fail(check, f"{label}: quote found in {homes}, but item {item} does not appear there")
    return n


def check_draft_excerpts(text: str):
    """Check 3: excerpts of the author's draft quoted in the examples must
    exist verbatim in the preserved round inputs (leading '…' trimmed)."""
    inputs = ""
    for p in sorted(COLD_RUN.glob("rodada-*-input.md")):
        inputs += norm(p.read_text(encoding="utf-8")) + "\n"
    if not inputs:
        fail("draft-excerpt", "no round inputs found in tests/cold-run/")
        return 0
    spans = []
    for block in pt_blocks(text):
        for m in re.finditer(r"Trecho do rascunho: (.+?)(?=\n- |\Z)", block, re.S):
            spans.append(m.group(1))
        for m in re.finditer(
            r"\[F-\d+\] (?:RESOLVIDO|PARCIAL|NÃO TRATADO|QUEBROU DE NOVO)(.+?)(?=\n\[|\n---|\Z)",
            block, re.S,
        ):
            spans.append(m.group(1))
    n = 0
    for span in spans:
        for quote in re.findall(r'"([^"]{30,})"', span):
            n += 1
            core = norm(quote).rstrip("…").strip()
            if core not in inputs:
                fail("draft-excerpt", f"draft quote not found in cold-run inputs: \"{quote[:80]}…\"")
    return n


FORBIDDEN_SECTION = re.compile(
    r"rewrit|suggested text|vers[ãa]o sugerida|como poderia ficar|texto pronto",
    re.I,
)


def check_skeleton(rules_text: str, check="skeleton"):
    """Check 4: the fixed output skeleton has exactly sections 1..6 and no
    section title offers rewritten text (there is no slot to fill)."""
    m = re.search(r"## Output skeleton.*?```(.*?)```", rules_text, re.S)
    if not m:
        fail(check, "output skeleton block not found in rules.md")
        return
    sections = re.findall(r"^(\d+)\.\s+(.+)$", m.group(1), re.M)
    numbers = [int(n) for n, _ in sections]
    if numbers != [1, 2, 3, 4, 5, 6]:
        fail(check, f"skeleton sections are {numbers}, expected [1, 2, 3, 4, 5, 6]")
    for n, title in sections:
        if FORBIDDEN_SECTION.search(title):
            fail(check, f"skeleton section {n} offers rewritten text: \"{title.strip()}\"")


def check_ids(text: str):
    """Check 5: sequential IDs, no duplicates, re-review verifies known IDs."""
    defined, seen = [], set()
    for block in pt_blocks(text):
        for m in re.finditer(r"\[F-(\d+)\]( \(novo\))?", block):
            num, new = int(m.group(1)), bool(m.group(2))
            verdict = re.match(
                r"\[F-\d+\] (RESOLVIDO|PARCIAL|NÃO TRATADO|QUEBROU DE NOVO)",
                block[m.start():],
            )
            if verdict and not new:
                if num not in seen:
                    fail("ids", f"re-review verifies F-{num:02d}, which was never defined")
            elif num not in seen:
                defined.append(num)
                seen.add(num)
    expected = list(range(1, len(defined) + 1))
    if defined != expected:
        fail("ids", f"ID sequence is {defined}, expected {expected} (no gaps, no reuse)")


def check_receipts(manifest_text=None, check="receipt-integrity"):
    """Check 6: every receipt folder — tests/cold-run/ and
    tests/post-submission/ — has a SHA256SUMS manifest, every listed file
    matches its hash, and every receipt on disk is listed. An unhashed
    receipt is a drift risk, and the newest round is exactly where drift
    would hurt most.

    manifest_text is the selftest hook: it replaces the cold-run manifest
    with planted-bad content, and then only that folder is checked."""
    dirs = (COLD_RUN,) if manifest_text is not None else RECEIPT_DIRS
    return sum(check_receipts_dir(d, manifest_text, check) for d in dirs)


def check_receipts_dir(directory, manifest_text=None, check="receipt-integrity"):
    manifest_path = directory / "SHA256SUMS"
    rel = directory.relative_to(ROOT)
    if manifest_text is None:
        if not manifest_path.exists():
            fail(check, f"{rel}/SHA256SUMS not found")
            return 0
        manifest_text = manifest_path.read_text(encoding="utf-8")
    listed = {}
    for line in manifest_text.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split()
        if len(parts) != 2:
            fail(check, f"malformed manifest line: \"{line[:60]}\"")
            continue
        listed[parts[1]] = parts[0]
    n = 0
    for name, expected in listed.items():
        n += 1
        p = directory / name
        if not p.exists():
            fail(check, f"{rel}/{name} is in the manifest but missing on disk")
            continue
        actual = hashlib.sha256(p.read_bytes()).hexdigest()
        if actual != expected:
            fail(check, f"{rel}/{name} does not match its recorded SHA-256 — "
                        f"the receipt drifted from what was captured")
    for p in sorted(directory.glob("rodada-*.md")):
        if p.name not in listed:
            fail(check, f"{p.name} exists in {rel}/ but is not in its "
                        f"SHA256SUMS — every receipt must be pinned")
    return n


REWRITE_OFFER = re.compile(
    r"como poderia ficar|vers[ãa]o sugerida|texto pronto|pode copiar|"
    r"aqui est[áa] como|reescrevi|segue o texto|how it could read|"
    r"suggested version|feel free to copy",
    re.I,
)


def strip_quotes(text: str) -> str:
    """Remove explicitly quoted spans — straight or curly double quotes —
    so the scan only sees the editor's OWN prose."""
    return re.sub(r'"[^"]*"|“[^”]*”', " ", text)


def body_lines(text: str) -> str:
    """Drop annotation lines (# headers, > method notes) — they are the
    recording frame, present in both files, not draft nor editor prose."""
    return "\n".join(l for l in text.splitlines()
                     if not l.lstrip().startswith(("#", ">")))


def word_ngrams(text: str, n: int):
    words = norm(text).lower().split()
    for i in range(len(words) - n + 1):
        yield " ".join(words[i:i + n])


def check_no_rewrite(pairs=None, check="no-rewrite", n=8):
    """Check 7: receipt outputs must not reproduce 8-word draft spans
    outside quotes, nor contain offer-to-rewrite phrasing."""
    if pairs is None:
        pairs = []
        for out_p in sorted(COLD_RUN.glob("rodada-*-output.md")):
            if ".EN." in out_p.name:
                continue  # renderings are translations, not receipts
            in_p = COLD_RUN / out_p.name.replace("-output", "-input")
            if in_p.exists():
                pairs.append((in_p.name,
                              in_p.read_text(encoding="utf-8"),
                              out_p.name,
                              out_p.read_text(encoding="utf-8")))
    checked = 0
    for in_name, in_text, out_name, out_text in pairs:
        checked += 1
        m = REWRITE_OFFER.search(out_text)
        if m:
            fail(check, f"{out_name}: offer-to-rewrite phrasing found: "
                        f"\"{m.group(0)}\"")
        draft_grams = set(word_ngrams(body_lines(in_text), n))
        own_prose = strip_quotes(body_lines(out_text))
        hits = [g for g in word_ngrams(own_prose, n) if g in draft_grams]
        if hits:
            fail(check, f"{out_name}: {len(hits)} draft span(s) of {n}+ words "
                        f"outside quotes — first: \"{hits[0][:70]}…\"")
    return checked


RUNTIME_ARTIFACT = re.compile(
    r"</?(?:parameter|function_calls|invoke|thinking|system-reminder)\b[^>]*>",
    re.I,
)

# The receipts that legitimately contain a leaked runtime token, and how many
# occurrences each one holds. A receipt is a RECORDING: when the runtime leaks
# tool syntax into the editor's prose, the leak stays and gets confessed — it
# is not edited out (tests/cold-run/README.md documents this one). The number
# is exact on purpose: a NEW leak makes the count rise and fails the check; a
# receipt quietly cleaned makes it drop and fails too (the SHA-256 pin in
# check 6 catches the same edit from the other side).
RUNTIME_ARTIFACT_ALLOWED = {
    # Round 3, finding F-01: "<parameter>execução</parameter>" — one glitch,
    # two tags. Confessed in tests/cold-run/README.md and in README.md claim 4.
    "rodada-3-output.md": 2,
}


def check_runtime_artifacts(receipts=None, check="runtime-artifact"):
    """Check 8: no tool-syntax token leaked into a receipt's prose, except
    the occurrences already confessed. Prose rules cannot prevent a runtime
    glitch; a string check can at least refuse to let a new one pass
    unnoticed."""
    if receipts is None:
        receipts = []
        for d in (COLD_RUN, ROOT / "tests" / "post-submission"):
            for p in sorted(d.glob("rodada-*-output*.md")):
                receipts.append((p.name, p.read_text(encoding="utf-8")))
    checked = 0
    for name, text in receipts:
        checked += 1
        found = RUNTIME_ARTIFACT.findall(text)
        allowed = RUNTIME_ARTIFACT_ALLOWED.get(name, 0)
        if len(found) == allowed:
            continue
        if len(found) > allowed:
            fail(check, f"{name}: {len(found)} runtime-syntax token(s), "
                        f"{allowed} confessed — new leak: \"{found[allowed]}\"")
        else:
            fail(check, f"{name}: {len(found)} runtime-syntax token(s) but "
                        f"{allowed} are on record — a confessed glitch was "
                        f"removed; receipts are recordings, not drafts")
    return checked


def run_audit():
    reference = load_reference()
    if not reference:
        fail("setup", "reference/ is empty or missing")
        report()
    examples = EXAMPLES.read_text(encoding="utf-8")
    rules = RULES.read_text(encoding="utf-8")
    n_anchors = check_anchors(examples, reference)
    n_excerpts = check_draft_excerpts(examples)
    check_skeleton(rules)
    check_ids(examples)
    n_receipts = check_receipts()
    n_scans = check_no_rewrite()
    n_artifacts = check_runtime_artifacts()
    print(f"checked: {n_anchors} call anchors · {n_excerpts} draft excerpts · "
          f"1 skeleton · ID discipline · {n_receipts} receipt hashes · "
          f"{n_scans} no-rewrite scans · {n_artifacts} runtime-artifact scans")
    report()


def run_selftest():
    """A verifier that passes everything proves nothing. The fixtures are
    deliberately broken; every one of them MUST make a check fail."""
    reference = load_reference()
    problems = []

    FAILURES.clear()
    bad_quote = (FIXTURES / "bad-quote.md").read_text(encoding="utf-8")
    check_anchors(bad_quote, reference, check="selftest-quote")
    if not FAILURES:
        problems.append("bad-quote.md passed the anchor check — verifier is broken")

    FAILURES.clear()
    bad_skeleton = (FIXTURES / "bad-skeleton.md").read_text(encoding="utf-8")
    check_skeleton(bad_skeleton, check="selftest-skeleton")
    if not FAILURES:
        problems.append("bad-skeleton.md passed the skeleton check — verifier is broken")

    FAILURES.clear()
    tampered = ("0" * 64) + "  rodada-1-output.md"
    check_receipts(manifest_text=tampered, check="selftest-receipt")
    if not FAILURES:
        problems.append("a wrong SHA-256 passed the receipt check — verifier is broken")

    FAILURES.clear()
    in_text = (COLD_RUN / "rodada-1-input.md").read_text(encoding="utf-8")
    words = norm(in_text).split()
    smuggled = " ".join(words[220:240])  # 20 draft words, unquoted
    fake_out = ("O resumo precisa de trabalho. Uma forma de abrir seria: "
                + smuggled + " — pode adaptar a partir daí.")
    check_no_rewrite(pairs=[("rodada-1-input.md", in_text,
                             "synthetic-rewrite.md", fake_out)],
                     check="selftest-rewrite")
    if not FAILURES:
        problems.append("a smuggled unquoted draft span passed the "
                        "no-rewrite scan — verifier is broken")

    FAILURES.clear()
    leaked = ("[F-03] · altura 1 · PERDE PONTOS · o cronograma do "
              "<parameter>Anexo XIII</parameter> não fecha com o item 8.1.")
    check_runtime_artifacts(receipts=[("synthetic-leak-output.md", leaked)],
                            check="selftest-runtime-artifact")
    if not FAILURES:
        problems.append("a leaked runtime token passed the runtime-artifact "
                        "scan — verifier is broken")

    FAILURES.clear()
    check_runtime_artifacts(receipts=[("rodada-3-output.md", "no tokens here")],
                            check="selftest-runtime-artifact-cleaned")
    if not FAILURES:
        problems.append("a receipt with its confessed glitch removed passed "
                        "the runtime-artifact scan — verifier is broken")

    FAILURES.clear()
    if problems:
        for p in problems:
            print(f"SELFTEST FAIL: {p}")
        sys.exit(1)
    print("selftest: OK — all planted-bad cases (quote, skeleton, tampered "
          "receipt hash, smuggled rewrite, leaked runtime token, erased "
          "confession) were correctly rejected")
    sys.exit(0)


def report():
    if FAILURES:
        for check, msg in FAILURES:
            print(f"FAIL [{check}] {msg}")
        print(f"\nRED: {len(FAILURES)} failure(s).")
        sys.exit(1)
    print("GREEN: all checks passed.")
    sys.exit(0)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        run_selftest()
    run_audit()
