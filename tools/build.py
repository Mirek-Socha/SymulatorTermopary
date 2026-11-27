#!/usr/bin/env python3
"""Budowanie index.html i synchronizacja bloków wspólnych.

Użycie (z katalogu głównego repozytorium):
    python3 tools/build.py            # synchronizacja + osadzenie + kontrola składni
    python3 tools/build.py --check    # tylko sprawdzenie (kod wyjścia 1, gdy coś niezgodne)

Kroki:
 1. Bloki wspólne (między znacznikami >>> / <<<) są nadpisywane ze źródeł:
      QUIZ-CORE, QUIZ-CSS, QUIZ-MARKUP  ← tools/quiz/{core.js,style.css,markup.html}
      NIST (PeltierThomson.html)        ← funkcje NIST z SymulatorTermopary.html
 2. Pliki źródłowe zakładek są osadzane w index.html (iframe f0, f1, f2, atrybut srcdoc;
    escape: & → &amp;, " → &quot;).
 3. Każdy blok <script> jest sprawdzany przez `node --check` (jeśli node jest dostępny).
"""
import re, sys, os, subprocess, tempfile, shutil

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TABS = [('f0', 'SymulatorTermopary.html'), ('f1', 'SeebeckVizualizacja.html'), ('f2', 'PeltierThomson.html')]
QUIZ = {
    'QUIZ-CORE':   ('tools/quiz/core.js',     r'/\* >>> QUIZ-CORE[^\n]*\*/\n', r'\n/\* <<< QUIZ-CORE \*/'),
    'QUIZ-CSS':    ('tools/quiz/style.css',   r'/\* >>> QUIZ-CSS[^\n]*\*/\n',  r'\n/\* <<< QUIZ-CSS \*/'),
    'QUIZ-MARKUP': ('tools/quiz/markup.html', r'<!-- >>> QUIZ-MARKUP[^\n]*-->\n', r'\n<!-- <<< QUIZ-MARKUP -->'),
}

def rd(p): return open(os.path.join(ROOT, p), encoding='utf-8').read()
def wr(p, s): open(os.path.join(ROOT, p), 'w', encoding='utf-8').write(s)

def replace_block(text, begin_re, end_re, new, name, fname):
    m = re.search('(' + begin_re + ')(.*?)(' + end_re + ')', text, re.S)
    if not m:
        raise SystemExit(f'Brak znaczników {name} w {fname}')
    return text[:m.start(2)] + new + text[m.end(2):]

def nist_block():
    """Funkcje NIST z zakładki 1: tablica TC + tcSeg/emf/alpha/tempFromEmf."""
    src = rd('SymulatorTermopary.html')
    a = src.index('// NIST ITS-90 — funkcje referencyjne'); a = src.rindex('// ====', 0, a)
    b = src.index('// WŁAŚCIWOŚCI PRZEWODÓW'); b = src.rindex('// ====', 0, b)
    c = src.index('// Wybór odcinka wielomianu')
    d = src.index('// STAN', c); d = src.rindex('// ====', 0, d)
    return src[a:b].rstrip() + '\n\n' + src[c:d].rstrip() + '\n'

def sync(check_only):
    changed = []
    for _, f in TABS:
        h0 = h = rd(f)
        for name, (srcf, b, e) in QUIZ.items():
            h = replace_block(h, b, e, rd(srcf).strip(), name, f)
        if f == 'PeltierThomson.html':
            h = replace_block(h, r'/\* >>> NIST[^\n]*\*/\n', r'/\* <<< NIST \*/', nist_block(), 'NIST', f)
        if h != h0:
            changed.append(f)
            if not check_only: wr(f, h)
    return changed

def srcdoc(h): return h.replace('&', '&amp;').replace('"', '&quot;')

def embed(check_only):
    idx0 = idx = rd('index.html')
    for fid, f in TABS:
        idx, n = re.subn(r'(<iframe id="%s"[^>]*srcdoc=")[^"]*(")' % fid,
                         lambda m, h=rd(f): m.group(1) + srcdoc(h) + m.group(2), idx)
        if n != 1: raise SystemExit(f'index.html: brak iframe {fid}')
    if idx != idx0 and not check_only: wr('index.html', idx)
    return idx != idx0

def check_js():
    node = shutil.which('node')
    if not node:
        print('  (node niedostępny — pominięto kontrolę składni)'); return True
    ok = True
    for _, f in TABS:
        for i, s in enumerate(re.findall(r'<script(?![^>]*src)[^>]*>(.*?)</script>', rd(f), re.S)):
            with tempfile.NamedTemporaryFile('w', suffix='.js', delete=False, encoding='utf-8') as t:
                t.write(s); tn = t.name
            r = subprocess.run([node, '--check', tn], capture_output=True, text=True); os.unlink(tn)
            if r.returncode:
                ok = False; print(f'  ✗ {f} skrypt {i}:\n{r.stderr}')
    return ok

if __name__ == '__main__':
    chk = '--check' in sys.argv
    ch = sync(chk)
    print(('Niezgodne bloki: ' if chk else 'Zsynchronizowane bloki: ') + (', '.join(ch) if ch else 'brak zmian'))
    emb = embed(chk)
    print('index.html: ' + ('nieaktualny' if chk and emb else 'zaktualizowany' if emb else 'aktualny'))
    js = check_js(); print('Składnia JS: ' + ('OK' if js else 'BŁĘDY'))
    sys.exit(1 if (chk and (ch or emb)) or not js else 0)
