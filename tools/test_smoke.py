#!/usr/bin/env python3
"""Test dymny w przeglądarce (Playwright + Chromium).

    python3 tools/test_smoke.py [ścieżka/do/PeltierThomson.html]

Sprawdza: brak błędów JS, przełączanie zakładek i motywu w index.html, wszystkie poziomy
i scenariusze zakładki 3 wraz z kontrolą bilansów, przejście wszystkich pytań quizów.
Wypisuje odcisk liczbowy (do porównań przed/po zmianach). Kod wyjścia 1 przy błędzie.
Wymaga: pip install playwright && playwright install chromium (lub zmienna CHROME=ścieżka).
"""
import asyncio, os, sys, json
from playwright.async_api import async_playwright

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PT = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else os.path.join(ROOT, 'PeltierThomson.html')

PROBE = """(()=>{const out={};
  setLevel('beginner');
  for(const k of Object.keys(PRESETS)){applyPreset(k);const M=model();
    out['B:'+k]=[M.E,M.I,M.Qh,M.Qc,M.Qth,M.Pel,M.Ptc+M.Pl-M.Pel].map(v=>+v.toPrecision(6));}
  setLevel('pro');
  for(const k of Object.keys(PRO_PRESETS)){applyProPreset(k);const M=proModel();
    out['P:'+k]=[P.I,P.QL,M.TcC,M.V,M.Pel,M.Qh,M.Qpel-M.Qj-M.Qk-M.QL].map(v=>+v.toPrecision(6));}
  setLevel('expert');
  for(const k of Object.keys(EXP_PRESETS)){applyExpPreset(k);const M=expModel();
    out['X:'+k]=[X.I,M.QJ,M.QTh,M.QThA,M.symMax,M.antiMax,M.Qb-M.Qf-M.Pel].map(v=>+v.toPrecision(6));}
  setLevel('beginner'); return out;})()"""

async def main():
    errs, fails = [], []
    async with async_playwright() as p:
        kw = {'executable_path': os.environ['CHROME']} if os.environ.get('CHROME') else {}
        if not kw and os.path.exists('/usr/bin/google-chrome'): kw = {'executable_path': '/usr/bin/google-chrome'}
        b = await p.chromium.launch(**kw)
        # 1. zakładka 3 bezpośrednio: odcisk liczbowy i bilanse
        pg = await b.new_page(viewport={'width': 1400, 'height': 900})
        pg.on('pageerror', lambda e: errs.append('PT: ' + str(e)))
        await pg.goto('file://' + PT); await pg.wait_for_timeout(600)
        fp = await pg.evaluate(PROBE)
        for k, v in fp.items():
            res, ref = abs(v[-1]), max(abs(x) for x in v[:-1]) or 1
            if res > 1e-6 * ref + 1e-15: fails.append(f'bilans {k}: reszta {v[-1]}')
            if k.startswith('X:') and abs(v[2] - v[3]) > 1e-3 * max(abs(v[3]), 1e-15): fails.append(f'∫q_Th {k}: {v[2]} vs {v[3]}')
        print(json.dumps(fp, ensure_ascii=False, sort_keys=True))
        # 2. index.html: zakładki, motyw, quizy
        pg = await b.new_page(viewport={'width': 1400, 'height': 900})
        pg.on('pageerror', lambda e: errs.append('index: ' + str(e)))
        await pg.goto('file://' + os.path.join(ROOT, 'index.html')); await pg.wait_for_timeout(1200)
        for t in ['#tab1', '#tab2', '#tab0']:
            await pg.click(t); await pg.wait_for_timeout(300)
        await pg.click('#themeBtn'); await pg.wait_for_timeout(300); await pg.click('#themeBtn')
        for fr in pg.frames[1:]:
            levels = await fr.evaluate("typeof setLevel==='function'?['beginner','pro','expert']:[null]")
            for lv in levels:
                if lv: await fr.evaluate(f"setLevel('{lv}')")
                n = await fr.evaluate("QUIZ_Q.length")
                await fr.evaluate("QUIZ_Q.forEach(q=>{if(q.setup)q.setup();})")
                if lv: await fr.evaluate(f"setLevel('{lv}')")
                await fr.evaluate("Quiz.open()")
                for _ in range(n):
                    await fr.evaluate("document.querySelector('#qzBody .qz-opt').click()")
                    await fr.evaluate("[...document.querySelectorAll('#qzBody button')].find(x=>/^(Dalej|Wynik)/.test(x.textContent.trim())).click()")
                done = await fr.evaluate("/\\d+ \\/ \\d+/.test(document.getElementById('qzBody').innerText)")
                if not done: fails.append(f'quiz nie dobiegł końca ({lv})')
                await fr.evaluate("Quiz.close()")
                print(f'quiz {lv or "-"}: {n} pytań OK')
        await b.close()
    for e in errs: print('BŁĄD JS:', e)
    for f in fails: print('NIEZGODNOŚĆ:', f)
    print('WYNIK:', 'OK' if not errs and not fails else 'BŁĘDY')
    sys.exit(1 if errs or fails else 0)

asyncio.run(main())
