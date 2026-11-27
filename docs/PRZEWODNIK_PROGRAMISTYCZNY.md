# Przewodnik programistyczny — Termopary

Opis architektury, konwencji i procedur rozwoju aplikacji. Opis fizyki i danych zawierają pliki `docs/SymulatorTermopary.md`, `docs/SeebeckVizualizacja.md` i `docs/PeltierThomson.md`.

## 1. Architektura

```
index.html  ── nagłówek z zakładkami, przełącznik motywu
 ├─ <iframe id="f0" srcdoc="…SymulatorTermopary.html…">    zakładka 1: Symulator pomiaru
 ├─ <iframe id="f1" srcdoc="…SeebeckVizualizacja.html…">   zakładka 2: Efekt Seebecka
 └─ <iframe id="f2" srcdoc="…PeltierThomson.html…">        zakładka 3: Peltier i Thomson (Beginner / Pro / Expert)
```

- Każda zakładka to **samodzielny plik HTML** (HTML + CSS + JS w jednym pliku, bez bundlera i bez zależności lokalnych). Każdy plik można otworzyć osobno w przeglądarce.
- `index.html` osadza je przez atrybut `srcdoc`, więc aplikacja działa z dysku (`file://`) bez serwera.
- Zewnętrzne zasoby: fonty Google (IBM Plex Sans/Mono, Playfair Display) i KaTeX z CDN (tylko zakładka 1). Bez sieci zmienia się wygląd czcionek i wzory zostają w zapisie TeX; obliczenia działają.
- **Pliki źródłowe zakładek są jedynym miejscem edycji.** Treść `srcdoc` w `index.html` jest generowana przez `tools/build.py`.

### Komunikacja wrapper ↔ zakładki

`index.html` wysyła do każdej ramki komunikaty `postMessage`:

| Komunikat | Kiedy | Reakcja zakładki |
|---|---|---|
| `{type:'setTheme', dark:bool}` | zmiana motywu, załadowanie ramki | przełączenie klasy motywu na `<body>`, przerysowanie |
| `{type:'setActive', active:bool}` | przełączenie zakładki | zakładki 2 i 3 wstrzymują pętlę animacji, gdy są ukryte |

Funkcje wrappera: `sw(i)` przełącza zakładkę, `syncFrames()` rozsyła komunikaty, `toggleTheme()` zmienia motyw. Listy ramek to `[0,1,2]` i `['f0','f1','f2']`; nowa zakładka musi zostać do nich dopisana.

## 2. Struktura plików

```
index.html                    punkt wejścia (generowany srcdoc)
SymulatorTermopary.html       zakładka 1
SeebeckVizualizacja.html      zakładka 2
PeltierThomson.html           zakładka 3
docs/                         dokumentacja modeli i ten przewodnik
tools/build.py                synchronizacja bloków wspólnych + budowa index.html + kontrola składni
tools/test_smoke.py           test w przeglądarce (Playwright)
tools/quiz/                   wspólny moduł quizu: core.js, style.css, markup.html
README.md, CHANGELOG.md
```

## 3. Bloki wspólne

Kod używany w kilku zakładkach ma jedno źródło. W plikach zakładek jest otoczony znacznikami, a `tools/build.py` nadpisuje jego zawartość:

| Blok | Znaczniki | Źródło | Pliki |
|---|---|---|---|
| Moduł quizu (logika) | `/* >>> QUIZ-CORE … */` … `/* <<< QUIZ-CORE */` | `tools/quiz/core.js` | wszystkie trzy |
| Style quizu | `/* >>> QUIZ-CSS … */` … `/* <<< QUIZ-CSS */` | `tools/quiz/style.css` | wszystkie trzy |
| Znaczniki quizu | `<!-- >>> QUIZ-MARKUP … -->` … `<!-- <<< QUIZ-MARKUP -->` | `tools/quiz/markup.html` | wszystkie trzy |
| Funkcje NIST | `/* >>> NIST … */` … `/* <<< NIST */` | `SymulatorTermopary.html` (tablica `TC`, `tcSeg`, `emf`, `alpha`, `tempFromEmf`) | `PeltierThomson.html` |

Nie edytuj treści między znacznikami w plikach zakładek, bo zostanie nadpisana. Zmieniaj źródło i uruchom `python3 tools/build.py`.
Skrypt wycina blok NIST z zakładki 1 według komentarzy `// NIST ITS-90 — funkcje referencyjne`, `// WŁAŚCIWOŚCI PRZEWODÓW`, `// Wybór odcinka wielomianu` i `// STAN`. Te komentarze trzeba zachować.

## 4. Konwencje w zakładkach

### Rysowanie

- `rszC(canvas)` ustawia rozmiar bufora wg `devicePixelRatio` i zwraca `[ctx, W, H]` w pikselach CSS albo `[null, 0, 0]`, gdy płótno jest za małe (np. ukryte). Funkcja rysująca zwraca wtedy `false`, a pętla ponawia próbę w następnej klatce.
- Pętla `requestAnimationFrame(frame)` w zakładkach 2 i 3: flaga `needDraw` wymusza pełne przerysowanie (wykresy, pasek wyników, teoria). Bez flagi animowany jest tylko schemat.
- `ResizeObserver` na wszystkich płótnach ustawia `needDraw = true`.
- Kolory pochodzą ze zmiennych CSS (`tv('--amber')`, `tv('--text')`…), ustawionych osobno dla motywu ciemnego i jasnego.
- Każdy wykres przycina zawartość do pola (`ctx.save(); ctx.clip(); … ctx.restore()`). Etykiety rysuje się po `restore()`, żeby nie znikały.

### Formatowanie

- Separatorem dziesiętnym jest przecinek. W zakładce 3 służą do tego funkcje `dec`, `nf`, `fmtP` (µW), `fmtI` (mA), `fmtW` (W), `fmtA` (A), `fmtR`, `fmtC`, `fmtK`, `fmtWm`.
- Teksty interfejsu i komentarze są po polsku; nazwy zmiennych w notacji fizycznej (`Tx`, `T0`, `Rtc`, `Qh`, `QL`…).

### Stan i interfejs

- Zakładka 2: obiekt `S`. Zakładka 3: `S` (Beginner i poziom bieżący), `P` (Pro), `X` (Expert). Suwaki zmieniają stan przez `setState`/`setPro`/`setExp`, a to ustawia `needDraw` i czyści wybrany scenariusz.
- Scenariusze (presety) to obiekty `PRESETS`, `PRO_PRESETS`, `EXP_PRESETS` z polem `note` (HTML wyświetlany pod paskiem sterowania).
- Zakładka 1 nie ma pętli animacji: każda zmiana wywołuje `scheduleUpdate()` → `update()`.

## 5. Zakładka 3 — budowa

Plik ma cztery bloki `<script>`, wykonywane po kolei. Stałe i funkcje z wcześniejszych bloków są widoczne w późniejszych.

| Blok | Zawartość |
|---|---|
| 1. Wspólny + Beginner | NIST (generowany), dane przewodów `LEGS`, stan `S`, przełączanie poziomów `setLevel`, `model()`, pomocnicze funkcje rysowania i formatowania, wspólne narzędzia (`drawWF`, `axesBox`, `gridX`, `gridY`, `attachDrag`, `attachTips`), rysowanie poziomu Beginner, pasek wyników, teoria, pętla `frame` |
| 2. Pro | `MATS`, `P`, `pm()` (stałe modułu), `proModel()`, interfejs, `drawModule`, `drawProBal`, `drawTcI`, `drawQI`, `drawCOP`, `updateRbarPro`, `updateExplPro`, `drawPro` |
| 3. Expert | `KAPPA`, `X`, `muAB`, `xConst`, `solveT` (różnice skończone + Thomas + Picard), `expModel()` z pamięcią podręczną, `drawCable`, `drawXT`, `drawXD`, `drawXQ`, `drawMu`, `updateRbarExp`, `updateExplExp`, `drawExp` |
| 4. Quiz | `quizSet`, zestawy `QUIZ_BEG`, `QUIZ_PRO`, `QUIZ_EXP`, zmienna `QUIZ_Q` (zestaw bieżący), moduł `Quiz` (blok wspólny) |

Przełączanie poziomów: `setLevel(l)` ukrywa i pokazuje kontenery `#begUI`, `#proUI`, `#expUI`, zmienia tytuł, podmienia `QUIZ_Q` i restartuje quiz. Funkcje `updateRbar()` i `updateExpl()` wybierają wersję dla poziomu, a `frame()` wywołuje `drawPro`/`drawExp` albo rysowanie poziomu Beginner.

### Interakcja

- `attachDrag(canvas, klasaKursora, apply(map, x, y), onUp?)`: funkcja rysująca zapisuje w `canvas._map` granice pola (`pL`, `pR`, `pT`, `pB`) i przeliczniki `x2v`/`y2v`. Przeciąganie i kliknięcie wołają `apply`.
- `attachTips(canvas)`: wykres wodospadowy zapisuje w `canvas._hit` kolumny słupków z treścią dymka (`tip`, HTML). Pod kursorem pokazuje się `#tip`, a słupek jest podświetlany (`hovBar`).
- `drawWF(canvas, bars, równanie, formatter)`: słupek `{k, sub, v, c, tip}` dodaje `v` do sumy bieżącej, słupek `{k, sub, total, c, tip}` pokazuje sumę od zera.

## 6. Jak dodać…

### Scenariusz (preset)
Dopisz wpis do `PRESETS`/`PRO_PRESETS`/`EXP_PRESETS` (parametry + `note`) oraz `<option>` w odpowiedniej liście `<select>`. Liczby z opisu sprawdź w aplikacji (np. przez `tools/test_smoke.py`, który wypisuje wyniki wszystkich scenariuszy).

### Pytanie do quizu
Dopisz obiekt do zestawu (`QUIZ_Q` w zakładkach 1–2, `QUIZ_BEG`/`QUIZ_PRO`/`QUIZ_EXP` w zakładce 3):
```js
{topic:'…', q:'treść (HTML)', opts:['poprawna','zła','zła','zła'], a:0, exp:'wyjaśnienie', setup:()=>quizSet({...})}
```
Poprawna odpowiedź ma indeks `a`. Moduł losuje kolejność pytań i odpowiedzi. `setup` jest opcjonalne i obsługuje przycisk „🔬 Sprawdź w symulatorze”.

### Poziom lub zakładkę
- Nowy poziom w zakładce 3: kontener `<div id="…UI" hidden>`, przycisk w `#lvlBtns`, wpis w `LEVEL_TXT`, gałęzie w `setLevel`, `updateRbar`, `updateExpl`, `frame`, nowy blok `<script>` przed quizem, zestaw pytań.
- Nowa zakładka: plik HTML obsługujący `setTheme` i `setActive`, przycisk `#tabN` i `<iframe id="fN" srcdoc="">` w `index.html`, rozszerzenie list `[0,1,2]` i `['f0','f1','f2']` w skrypcie wrappera oraz pozycja w `TABS` w `tools/build.py`.

### Dane materiałowe
Każda wartość liczbowa musi mieć źródło w dokumentacji modelu (`docs/*.md`) i w panelu teorii zakładki. Wartości szacunkowe oznacza się „≈”.

## 7. Narzędzia

```bash
python3 tools/build.py            # synchronizacja bloków, osadzenie w index.html, node --check
python3 tools/build.py --check    # tylko kontrola (kod 1, gdy coś nieaktualne) — np. przed commitem
python3 tools/test_smoke.py       # test w przeglądarce
```

`test_smoke.py` wymaga Playwrighta z Chromium (`pip install playwright && playwright install chromium`; własną przeglądarkę wskazuje zmienna `CHROME`). Test robi trzy rzeczy:
- wypisuje odcisk liczbowy wszystkich scenariuszy zakładki 3 (JSON w pierwszej linii); porównanie odcisków przed i po zmianie wykrywa niezamierzone zmiany obliczeń,
- sprawdza domknięcie bilansów (Beginner, Pro, termostaty w Expert) oraz zgodność ∫q_Th dx z I·(ΔΠ − E),
- przełącza zakładki i motyw, przechodzi wszystkie pytania wszystkich quizów i zgłasza każdy błąd JavaScript.

## 8. Procedura zmian i wydań

1. Zmiany w plikach źródłowych zakładek (oraz `tools/quiz/*`).
2. `python3 tools/build.py`, potem `python3 tools/test_smoke.py`.
3. Commit na gałąź testową, wysłanie `index.html` do sprawdzenia w przeglądarce.
4. **Po akceptacji autora:** scalenie do `main` (fast-forward), wpis w `CHANGELOG.md`, aktualizacja `README.md` i `docs/`.
5. Tag wersji `vX.Y.Z` (GitHub → Releases) na ostatnim commicie wydania.
6. Każdy plik i dokument ma dyskretną stopkę „AGH KMiE 2026 Socha”.

Wersjonowanie: wersja główna całości w README i CHANGELOG. Znaczniki w zakładkach: `vtag` w nagłówku zakładek 1 i 3 oraz plakietki w zakładkach `index.html`. Plakietkę zmienia się tylko przy zmianie danej zakładki.

## 9. Historia architektury

| Wersja | Zmiana |
|---|---|
| v1.0–v1.3 | Dwie zakładki (symulator, Seebeck) w jednym `index.html` przez `srcdoc`; wspólny przełącznik motywu |
| v1.4.0 | Audyt układu i fizyki; `rszC` z ponowieniem rysowania, `ResizeObserver`, komunikat `setActive` |
| v1.5.0 | Wspólny moduł quizu (wstrzykiwany do obu zakładek); nieliniowość na żądanie |
| v1.6.0 | Klasy IEC, przewody przedłużające, niejednorodność, temperatury zacisków |
| v1.7.0 | Zakładka 3 (Beginner); funkcje NIST kopiowane z zakładki 1; ujednolicone rezystywności |
| v1.8.0 | Poziom Pro; przeciąganie punktu pracy, dymki na wykresach wodospadowych |
| v1.9.0 | Poziom Expert (równanie przewodzenia z Thomsonem) |
| v1.9.1 | Refaktoryzacja: wspólne narzędzia wykresów w zakładce 3, bloki wspólne ze znacznikami, `tools/build.py`, `tools/test_smoke.py`; usunięcie martwego kodu i danych; dokumentacja wszystkich zakładek |

<sub>AGH KMiE 2026 Socha</sub>
