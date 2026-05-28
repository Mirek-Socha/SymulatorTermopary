# Changelog — Termopary (AGH Metrologia)

## [v1.2.0] — 2026-05-28

### Dodano
- **`SeebeckVizualizacja.html`** — nowa aplikacja: fizyka efektu Seebecka
  - Schemat obwodu: spoina lewa (T₁/T₂), woltomierz prawy — topologia wg normy
  - Gęstość elektronów proporcjonalna do n(T) i znaku α — bez mylącego ruchu pętlowego
  - Zewnętrzne źródło ciepła/zimna (🔥/❄️) na elektrodzie A, B lub obu
  - N segmentów (10–60) z wyliczaniem dV = α·ΔT na segment
  - Wykres T(x), wykres słupkowy wkładów dV, skumulowany potencjał V(x)
  - Prawo temperatur pośrednich — SEM niezmieniona mimo niemonotonnego T(x)
  - Przeciągnij źródło po schemacie myszą lub dotykiem
- **`index.html`** — wrapper z zakładkami (srcdoc, działa lokalnie bez serwera HTTP)
- Globalny przełącznik motywu jasny/ciemny — postMessage do obu iframe'ów jednocześnie
- Teoria Seebecka jako sliding overlay (przycisk 📖 Teoria w nagłówku)
- Drag T_h i T_z bezpośrednio na wykresie E(T) (kursor grab/grabbing, obsługa touch)
- Tło charakterystyk pozostałych typów TC na wykresie E(T) z etykietami przy prawej krawędzi
- Górne etykiety `↑K`, `↑E`… — dynamiczne oznaczenie typów o wyższej czułości α w punkcie T_h

### Poprawiono
- Naprawa scrollbara w navie wrappera (`overflow:hidden` + responsywne ukrywanie .sub/.lbl)
- `blendColor()` — parser koloru obsługuje zarówno `#rrggbb` jak i `rgb(r,g,b)` (fix NaN w addColorStop)
- Wszystkie canvasy SeebeckVizualizacja używają `tv()` z CSS vars — motyw jasny działa poprawnie
- `postMessage` listener w Symulatorze — bezpośrednie ustawianie klas CSS bez podwójnego odwracania isDark

---

## [v1.1.0] — 2026-05-28

### Dodano
- Model fizyczny R_tc obliczany z długości i średnicy przewodów (rezystywności materiałów wg IEC 60584)
- Selector przyrządu pomiarowego R_in z tłem historycznym (galwanometr 1875 → nowoczesny przetwornik)
- Presety historyczne: Galwanometr Siemens 1875 (50 Ω), Galwanometr precyzyjny 1900 (100 Ω), Miliwooltomierz 1920 (500 Ω), DVM 1975 (1 MΩ)
- Teoria eksperta: opis ADC w torze termoparowym, przykłady liczbowe 10/16/24 bit, budżet błędów RSS z omówieniem rozkładów
- Sekcja autora i bibliografia (7 pozycji: NIST-175, IEC 60584-1, GUM, Childs, Michalski, Seebeck, Tumański)

### Poprawiono
- Dropdown scenariuszy: `position:fixed` z `getBoundingClientRect` — lista nie jest przycinana przez kontener
- Motyw jasny: CSS vars przeniesione do `:root`, dodano `color-scheme` — tło formularzy poprawne
- Układ ctrl-row: dwuwierszowy grid (etykieta+wartość / suwak na pełną szerokość) — pola liczbowe zawsze widoczne
- Wykresy: `canvas flex:1` wypełnia całą kartę zamiast stałej wysokości clamp()
- `overflow-x:clip` na kolumnie sterowania

### Zmieniono
- Parametry R_in i R_L zastąpione przez: długość [m], średnica [mm], selector przyrządu (lista nazwana)

---

## [v1.0.0] — 2026-05-28

### Dodano
- Pierwszy release: symulator kontaktowego pomiaru temperatury termoparą
- 6 typów termopar (K, J, T, E, N, S) z tablicami NIST ITS-90, interpolacja liniowa
- Tryb Podstawowy (student) i Tryb Eksperta (inżynier)
- Schemat blokowy toru pomiarowego (5 bloków z animowanymi strzałkami SVG)
- Kompensacja złącza zimnego (CJC) z regulowanym błędem δT_cjc
- Model przetwornika A/C: rozdzielczość 10–24 bit, zakres 10–100 mV
- Wykresy: charakterystyka E(T) i czułość Seebecka α(T) = dE/dT
- Panel teorii z formułami renderowanymi przez KaTeX
- Sygnalizacja świetlna jakości pomiaru (RSS < 1°C / < 5°C / > 5°C)
- Presety scenariuszy (5 podstawowych)
- Obsługa jasnego i ciemnego motywu
