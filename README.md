# Termopary — Interaktywna Aplikacja Dydaktyczna

Zestaw narzędzi do nauczania kontaktowego pomiaru temperatury termoelementem. Trzy narzędzia w jednym pliku HTML, zero zależności lokalnych.

**Autor:** Mirosław Socha  
**Jednostka:** Katedra Metrologii i Elektroniki, WEAIiIB, AGH Akademia Górniczo-Hutnicza, Kraków  
**Wersja:** v1.7.0

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
- **Klasy tolerancji IEC 60584-1** (1, 2, 3) dla wszystkich typów: odchyłka ±max(a₀, k·|t|) w zakresie klasy, w budżecie jako rozkład prostokątny
- **Przedłużenie do przyrządu**: przewód przedłużający (X), kompensacyjny (C, z odchyłką czułości ε) lub — błędnie — zwykła miedź; temperatura głowicy T_g; błąd jako składnik systematyczny
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

### Zaburzenia (granice praw)
- **Niejednorodność przewodu**: odcinek elektrody A lub B o α + Δα (pozycja, szerokość, Δα). Wkład Δα·[T(koniec) − T(początek)] — działa jak pasożytnicza termopara; widoczny tylko w gradiencie temperatury, zależny od położenia źródła ciepła względem krawędzi odcinka
- **Różne temperatury zacisków**: T(Cu|B) ≠ T(Cu|A) daje dodatkową SEM (α_B − α_Cu)·δ — na schemacie, wykresie potencjału i w pasku wyników z rozbiciem przyczyn

### Prawa fizyczne pokazywane w czasie rzeczywistym
- **Prawo temperatur pośrednich** (Kelvin): SEM = (α_A − α_B)(Tₓ − T₀) niezależnie od kształtu T(x)
- **Prawo metalu pośredniego** (Volta): przewody Cu nie zmieniają odczytu przy jednakowej temperaturze złączy Cu|A i Cu|B

### Baza materiałów
24 materiały: metale czyste, stopy termoparowe, materiały termoelektryczne (Bi₂Te₃, PbTe, GeTe); presety K, J, T, E, N, R, S. Współczynniki α stopów skalibrowane tak, by różnice odtwarzały czułości NIST ITS-90 przy 0 °C. Prace wyjścia stopów i półprzewodników są szacunkami (oznaczone „≈”).

## Zakładka 3 — Peltier i Thomson (`PeltierThomson.html`)

Zamknięty obwód termopary z prądem. Trzy poziomy szczegółowości budowane etapami: **Beginner** (dostępny), Pro (moduł Peltiera — planowany), Expert (pełny model Thomsona — planowany). Pełny opis modelu, przykład kontrolny i źródła: [`docs/PeltierThomson.md`](docs/PeltierThomson.md).

### Poziom Beginner — termopara jako generator
- Typy K, J, T, E, N, S; E(T) i α(T) z tych samych funkcji NIST ITS-90 co w zakładce 1
- Regulacja Tₓ, T₀, rezystancji obciążenia R_L (0,1 Ω – 10 kΩ, skala log), długości i średnicy przewodów; R_tc z rezystywności (Omega, Kanthal)
- **Schemat**: animowane elektrony (przeciwnie do prądu umownego), strzałki ciepła Peltiera — spoina pobiera Π(Tₓ)·I, złącza zimne oddają Π(T₀)·I; odczyt I i U
- **Bilans mocy** (wykres wodospadowy): Π(Tₓ)I − Π(T₀)I + Q_Th = E·I = I²R_tc + I²R_L; ciepło Thomsona z bilansu
- **Dopasowanie obciążenia**: P_L(R_L), I(R_L), maksimum P_max = E²/(4R_tc) przy R_L = R_tc
- **Π_AB(T) = α_AB(T)·T** (relacja Kelvina) z porównaniem ΔΠ i E
- Teoria z cytowaniami źródeł i 7 pytań sprawdzających

---

## Interfejs

| Funkcja | Opis |
|---|---|
| Zakładki | Przełączanie Symulator ↔ Seebeck ↔ Peltier i Thomson; ukryta zakładka wstrzymuje animację |
| ☀️/🌙 Motyw | Globalny przełącznik jasny/ciemny — wszystkie narzędzia jednocześnie |
| 📖 Teoria | Panel z teorią, formułami i bibliografią |
| ❓ Sprawdź się | Pytania sprawdzające (13 w zakładce 1, 12 w zakładce 2, 7 w zakładce 3): losowa kolejność pytań i odpowiedzi, wyjaśnienie po każdej odpowiedzi, wynik końcowy; przycisk **🔬 Sprawdź w symulatorze** ustawia scenariusz pytania, a **❓ Wróć do pytania** przywraca quiz |
| Drag na wykresie | Przeciąganie T_h, T_z na E(T); przeciąganie źródła ciepła/zimna na schemacie |

---

## Struktura plików

```
index.html                  ← punkt wejścia (aplikacje osadzone przez srcdoc)
SymulatorTermopary.html     ← zakładka 1 (wersja źródłowa)
SeebeckVizualizacja.html    ← zakładka 2 (wersja źródłowa)
PeltierThomson.html         ← zakładka 3 (wersja źródłowa)
docs/PeltierThomson.md      ← model, dane i źródła zakładki 3
CHANGELOG.md
```

`index.html` osadza wszystkie aplikacje przez atrybut `srcdoc` — działa bez serwera HTTP. Po zmianie plików źródłowych należy ponownie osadzić je w `index.html` (escape `&` → `&amp;`, `"` → `&quot;`).

---

## Podstawa fizyczna

| Źródło | Zastosowanie |
|---|---|
| NIST Monograph 175 (ITS-90) | Funkcje referencyjne E(T) i ich odwrotności dla wszystkich typów |
| IEC 60584-1:2013 | Definicje typów K/J/T/E/N/S |
| GUM JCGM 100:2008 | Budżet niepewności (u = a/√3, u_c, U) |
| Kelvin / Thomson (1851) | Prawo temperatur pośrednich, relacje Π = α·T i μ_A − μ_B = T·dα/dT |
| Peltier (1834) | Ciepło Peltiera na złączu |
| Omega Z-49, Kanthal | Rezystywności stopów termoparowych |
| Volta | Napięcie kontaktowe, prawo metalu pośredniego |
| Seebeck (1821) | Efekt termoelektryczny |

---

## Licencja

Do użytku dydaktycznego — AGH Kraków.

<sub>AGH KMiE 2026 Socha</sub>
