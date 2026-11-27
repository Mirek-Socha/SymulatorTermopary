# Termopary — Interaktywna Aplikacja Dydaktyczna

Zestaw narzędzi do nauczania kontaktowego pomiaru temperatury termoelementem. Dwa narzędzia w jednym pliku HTML, zero zależności lokalnych.

**Autor:** Mirosław Socha  
**Jednostka:** Katedra Metrologii i Elektroniki, WEAIiIB, AGH Akademia Górniczo-Hutnicza, Kraków  
**Wersja:** v1.5.0

---

## Uruchomienie

```
Pobierz repozytorium → otwórz index.html w przeglądarce
```

Nie wymaga serwera HTTP, instalacji ani połączenia z internetem (poza fontami Google i KaTeX z CDN).

---

## Zakładka 1 — Symulator pomiaru (`SymulatorTermopary.html`)

### Tryb Podstawowy
- 6 typów termopar (K, J, T, E, N, S)
- Charakterystyki E(T) z **funkcji referencyjnych NIST ITS-90** (wielomiany; dla typu K z członem wykładniczym) — dokładność odtworzenia tablic NIST ≤ 0,5 µV
- SEM [mV], T_mierzona [°C], błąd [°C], sygnalizacja świetlna
- Presety scenariuszy (piec, kriogenika, temperatura ciała…)

### Tryb Eksperta
- Schemat blokowy toru z animowanymi strzałkami
- CJC z regulowanym błędem δT_cjc (przeniesionym na wynik przez α(T_z)/α(T_h))
- Model ADC 10–24 bit: kwantyzacja wchodzi do wyniku pomiaru, sygnalizacja nasycenia
- Obliczanie R_tc z geometrii przewodów; selektor przyrządu z historią: galwanometr Siemensa 1875 (50 Ω) → nowoczesny przetwornik (10 MΩ)
- **Budżet niepewności wg GUM**: wartości graniczne ±a → u = a/√3, niepewność złożona u_c (RSS), rozszerzona U (k = 2); rezystancja przewodów jako znany błąd systematyczny (poprawka, poza RSS)
- Teoria z formułami KaTeX i bibliografią

### Wykresy
- **E(T)**: aktywny typ z punktem pracy; pozostałe typy w tle tylko w ich zakresach definicji
- Etykiety typów: przy prawej krawędzi (krzywe kończące się w polu wykresu) oraz **nad górną krawędzią** (`↑E`, `↑J`…) w punktach, gdzie krzywe o większej czułości opuszczają wykres
- **α(T) = dE/dT**: pochodna analityczna — ciągła krzywa czułości (widoczna nieliniowość typu K w zakresie 0–300 °C)
- **Drag** punktów T_h i T_z bezpośrednio na wykresie (mysz + dotyk)

### 📐 Nieliniowość (na żądanie)
- Przycisk nad wykresem E(T) pokazuje delikatną prostą przez punkty pracy (T_z, E_z) i (T_h, E_h) oraz zacieniowaną odchyłkę krzywej od prostej
- Osobny wykres **błędu nieliniowości** δT(T) = T_wsk − T przy liniowym przeliczaniu E → T: zero w punktach kalibracji, ekstremum między nimi (z wartością i temperaturą), ekstrapolacja poza przedziałem przygaszona
- Podsumowanie: czułość średnia S, max ΔE [µV], nieliniowość w % zakresu
- Wspólna oś T z wykresem E(T); sekcja teorii z przykładami (K ≈ 6 °C, S ≈ 60 °C dla 0–1000 °C)

---

## Zakładka 2 — Efekt Seebecka (`SeebeckVizualizacja.html`)

Fizyczna wizualizacja mechanizmu powstawania SEM termoelektrycznej.

### Układ
- Lewa kolumna: **schemat obwodu**, pod nim **poziomy Fermiego** (diagramy wyrównane do złączy)
- Prawa kolumna: T(x), wkłady segmentów dV, potencjał wzdłuż obwodu
- Poniżej 960 px — jedna kolumna

### Schemat obwodu
- Cyfrowy woltomierz → przewody **Cu (metal C)** → złącza zimne Cu|A, Cu|B (T₀) → elektrody A i B → **spoina pomiarowa A|B** (Tₓ); wszystkie przewody tej samej grubości
- Segmenty elektrod zabarwione lokalną temperaturą
- **Gęstość elektronów**: nadmiar e⁻ przy ujemnym końcu przewodu — α < 0 → przy T₀, α > 0 → przy Tₓ (zgodnie z biegunowością termopar: chromel +, alumel −); siła nierównowagi rośnie z |α|, drgania cieplne ∝ √T
- **Napięcia kontaktowe** E(Cu,A), E(Cu,B), E(A,B) z różnicy prac wyjścia: E(X,Y) = (W_Y − W_X)/e; grot strzałki w stronę metalu o wyższym potencjale

### Poziomy Fermiego
- Oś: energia względem poziomu próżni, poziom Fermiego metalu na −W (stan przed zetknięciem)
- Złącza zimne: kolejność **A | Cu | B**; złącze pomiarowe: **A | B**
- Obsadzenie stanów wg rozkładu Fermiego–Diraca w skali rzeczywistej (rozmycie ≈ 4kT, wyraźnie szersze przy Tₓ)
- Strzałki od niższego do wyższego poziomu Fermiego — długość = |E(X,Y)|·e

### Zewnętrzne źródło (świeczka / lód)
- 7 trybów: brak / 🔥❄️ na elektrodzie A / B / obu
- Gaussowski pik/dołek temperatury z regulowaną pozycją i amplitudą; temperatury złączy pozostają ustalone
- Kliknij lub **przeciągnij źródło** po schemacie (pointer events: mysz + dotyk)

### Wykresy
- **T(x)**: rozkład temperatury wzdłuż elektrod
- **dV = α·ΔT na segment**: słupki ± — widoczne kasowanie wkładów przy niemonotonnym T(x)
- **Potencjał wzdłuż obwodu** w dwóch trybach:
  - *elektrochemiczny (mierzony)* — ciągły na złączach; między zaciskami Cu dokładnie SEM
  - *elektrostatyczny + kontaktowe* — skoki na złączach (rzędu 0,1–0,5 V), których suma w zamkniętej pętli = 0

### Prawa fizyczne pokazywane w czasie rzeczywistym
- **Prawo temperatur pośrednich** (Kelvin): SEM = (α_A − α_B)(Tₓ − T₀) niezależnie od kształtu T(x)
- **Prawo metalu pośredniego** (Volta): przewody Cu nie zmieniają odczytu przy jednakowej temperaturze złączy Cu|A i Cu|B

### Baza materiałów
24 materiały: metale czyste, stopy termoparowe, materiały termoelektryczne (Bi₂Te₃, PbTe, GeTe); presety K, J, T, E, N, R, S. Współczynniki α stopów skalibrowane tak, by różnice odtwarzały czułości NIST ITS-90 przy 0 °C. Prace wyjścia stopów i półprzewodników są szacunkami (oznaczone „≈”).

---

## Interfejs

| Funkcja | Opis |
|---|---|
| Zakładki | Przełączanie Symulator ↔ Seebeck; ukryta zakładka wstrzymuje animację |
| ☀️/🌙 Motyw | Globalny przełącznik jasny/ciemny — oba narzędzia jednocześnie |
| 📖 Teoria | Panel z teorią, formułami i bibliografią |
| ❓ Sprawdź się | Pytania sprawdzające (11 w zakładce 1, 10 w zakładce 2): losowa kolejność pytań i odpowiedzi, wyjaśnienie po każdej odpowiedzi, wynik końcowy; przycisk **🔬 Sprawdź w symulatorze** ustawia scenariusz pytania, a **❓ Wróć do pytania** przywraca quiz |
| Drag na wykresie | Przeciąganie T_h, T_z na E(T); przeciąganie źródła ciepła/zimna na schemacie |

---

## Struktura plików

```
index.html                  ← punkt wejścia (obie aplikacje osadzone przez srcdoc)
SymulatorTermopary.html     ← zakładka 1 (wersja źródłowa)
SeebeckVizualizacja.html    ← zakładka 2 (wersja źródłowa)
CHANGELOG.md
```

`index.html` osadza obie aplikacje przez atrybut `srcdoc` — działa bez serwera HTTP. Po zmianie plików źródłowych należy ponownie osadzić je w `index.html` (escape `&` → `&amp;`, `"` → `&quot;`).

---

## Podstawa fizyczna

| Źródło | Zastosowanie |
|---|---|
| NIST Monograph 175 (ITS-90) | Funkcje referencyjne E(T) i ich odwrotności dla wszystkich typów |
| IEC 60584-1:2013 | Definicje typów K/J/T/E/N/S |
| GUM JCGM 100:2008 | Budżet niepewności (u = a/√3, u_c, U) |
| Kelvin (1854) | Prawo temperatur pośrednich, relacja Π = α·T |
| Volta | Napięcie kontaktowe, prawo metalu pośredniego |
| Seebeck (1821) | Efekt termoelektryczny |

---

## Licencja

Do użytku dydaktycznego — AGH Kraków.

<sub>AGH KMiE 2026 Socha</sub>
