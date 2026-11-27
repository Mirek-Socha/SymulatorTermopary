# Symulator pomiaru — dokumentacja zakładki 1

Plik źródłowy: `SymulatorTermopary.html` (osadzony w `index.html` jako zakładka „Symulator pomiaru”).
Odbiorcy: studenci Inżynierii Biomedycznej, Elektrotechniki oraz Automatyki i Robotyki (AGH, WEAIiIB).

Zakładka modeluje pełny tor pomiaru temperatury termoparą: od temperatury mierzonej, przez SEM termopary, przedłużenie do przyrządu, rezystancję przewodów, przetwornik A/C i kompensację złącza odniesienia, aż do wskazania. Wynik zawiera budżet niepewności według GUM.

## Tryby

| Tryb | Zakres |
|---|---|
| **Podstawowy** | Typ termopary, T_h i T_z (suwaki lub przeciąganie punktów na wykresie E(T)), SEM, wskazanie, błąd, sygnalizacja świetlna, presety. Przyrząd idealny. |
| **Ekspert** | Dodatkowo: schemat blokowy toru, błąd kompensacji δT_cjc, ADC 10–24 bit z zakresem, geometria przewodów i rezystancja wejściowa przyrządu, przedłużenie (X, C, Cu), klasy tolerancji IEC, budżet niepewności, wykres α(T). |

Nieliniowość (przycisk 📐) działa w obu trybach.

## Model toru pomiarowego

```
T_h ─► E(T_h) − E(T_g) ─► [przedłużenie T_g → T_z] ─► dzielnik R_in/(R_in+R_tc) ─► ADC ─► + E(T̂_z) ─► E⁻¹ ─► T_wsk
```

| Etap | Równanie | Uwagi |
|---|---|---|
| Charakterystyka | E(T) — funkcje referencyjne NIST ITS-90 [1]; α(T) = dE/dT — pochodna analityczna | Odwrotność E⁻¹: bisekcja + Newton |
| Bez przedłużenia / przewód X | E_netto = E(T_h) − E(T_z) | Przewód X ma charakterystykę termopary |
| Przewód kompensacyjny C | E_netto = [E(T_h) − E(T_g)] + (1+ε)·[E(T_g) − E(T_z)] | ε — odchyłka czułości przewodu |
| Zwykła miedź | E_netto = E(T_h) − E(T_g) | Złączem odniesienia staje się głowica (T_g) |
| Błąd przedłużenia | δT_kab = E⁻¹(E_netto + E(T_z)) − T_h | Składnik systematyczny |
| Rezystancja przewodów | R_tc = L·(ρ_A + ρ_B)/A; E_mierz = E_netto·R_in/(R_in + R_tc) | Dzielnik napięcia |
| Błąd od R_tc | δT_R = E⁻¹(E_mierz + E_z) − E⁻¹(E_netto + E_z) | Dokładnie, przez funkcję odwrotną; zawsze zaniża |
| ADC | LSB = E_zakr/2ᴺ; E_ADC = round(E/LSB)·LSB; \|E\| > E_zakr → nasycenie | Tylko tryb eksperta |
| CJC | E_koryg = E_ADC + E(T_z + δT_cjc) | Przyrząd mierzy T_z z błędem δT_cjc |
| Wskazanie | T_wsk = E⁻¹(E_koryg), błąd = T_wsk − T_h | |

### Budżet niepewności (GUM [3])

Składniki o nieznanym znaku traktowane są jako rozkłady prostokątne o granicach ±a, czyli u = a/√3.

| Składnik | Granica a | Uwagi |
|---|---|---|
| Kompensacja ZZ | \|δT_cjc\|·α(T_z)/α(T_h) | Błąd przeniesiony na T_h |
| Kwantyzacja ADC | (LSB/2)/α(T_h) | |
| Tolerancja termopary | wg klasy IEC 60584-1 [2] | max(a₀, k·\|t\|) w zakresie klasy |

Niepewność złożona u_c = √(Σu²), rozszerzona U = 2·u_c (k = 2).
Znane błędy systematyczne (rezystancja przewodów, przedłużenie) nie wchodzą do RSS. Pokazuje się je osobno jako poprawki.

### Klasy tolerancji IEC 60584-1

Odchyłka dopuszczalna: ±max(a₀, k·|t|) w zakresie klasy.

| Typ | Klasa 1 | Klasa 2 | Klasa 3 |
|---|---|---|---|
| K, N | −40…1000 °C: 1,5 °C / 0,004 | −40…1200 °C: 2,5 °C / 0,0075 | −200…40 °C: 2,5 °C / 0,015 |
| J | −40…750 °C: 1,5 °C / 0,004 | −40…750 °C: 2,5 °C / 0,0075 | — |
| T | −40…350 °C: 0,5 °C / 0,004 | −40…350 °C: 1,0 °C / 0,0075 | −200…40 °C: 1,0 °C / 0,015 |
| E | −40…800 °C: 1,5 °C / 0,004 | −40…900 °C: 2,5 °C / 0,0075 | −200…40 °C: 2,5 °C / 0,015 |
| S | 0…1100 °C: 1 °C; 1100…1600 °C: 1 + 0,003·(t − 1100) °C | 0…1600 °C: 1,5 °C / 0,0025 | — |

### Nieliniowość

Przy liniowym przeliczaniu przez dwa punkty kalibracji (T_z, E_z) i (T_h, E_h):

S = (E_h − E_z)/(T_h − T_z), T_wsk(T) = T_z + (E(T) − E_z)/S, δT(T) = T_wsk(T) − T.

Błąd jest zerowy w punktach kalibracji i ma ekstremum między nimi. Kontrola (typ K, 0–1000 °C): ekstremum δT = 6,27 °C przy 770 °C, odchyłka ΔE = 0,259 mV, nieliniowość 0,63 % zakresu.

## Dane

### Typy termopar (zakresy w aplikacji)

| Typ | Przewody (+ / −) | Zakres [°C] |
|---|---|---|
| K | Ni-Cr / Ni-Al | −200…1372 |
| J | Fe / Cu-Ni | −210…1200 |
| T | Cu / Cu-Ni | −250…400 |
| E | Ni-Cr / Cu-Ni | −200…1000 |
| N | Ni-Cr-Si / Ni-Si | −200…1300 |
| S | Pt-10%Rh / Pt | −50…1768 |

Funkcje NIST są zdefiniowane w szerszych zakresach (np. K i T od −270 °C). Aplikacja ogranicza zakres do obszaru praktycznego.

### Rezystywności przewodów (20 °C) [6–8]

| Typ | ρ_A [nΩ·m] | ρ_B [nΩ·m] |
|---|---|---|
| K | 706 | 294 |
| J | 100 | 489 |
| T | 15,4 | 489 |
| E | 706 | 489 |
| N | 1000 | 365 |
| S | 185 | 98,3 |

Przeliczenie: 1 Ω·cmil/ft = 1,6624 nΩ·m (Omega). Wartości są wspólne z zakładką 3.

### Przyrządy (rezystancja wejściowa)

Galwanometr Siemensa (~1875) 50 Ω · galwanometr precyzyjny (~1900) 100 Ω · miliwoltomierz d'Arsonvala (~1920) 500 Ω · woltomierz tranzystorowy (~1960) 100 kΩ · woltomierz cyfrowy (~1975) 1 MΩ · nowoczesny przetwornik 10 MΩ.

Średnice przewodów: 0,25 / 0,5 / 0,8 / 1,0 / 1,5 / 2,0 mm.

## Przykłady kontrolne (wyniki aplikacji, tryb eksperta)

| Preset | Ustawienia | Wynik |
|---|---|---|
| 🔥 Piec laboratoryjny | K, 300/20 °C, ADC 16 bit 50 mV, 10 m Ø 1 mm, 10 MΩ | E_h = 12,2086 mV, E_z = 0,7981 mV, E_netto = 11,4105 mV; R_tc = 12,73 Ω; LSB 0,76 µV → ±0,009 °C; U = ±0,011 °C |
| ⚠️ Błąd kompensacji ZZ | K, 200/20 °C, δT_cjc = +3 °C | błąd +3,03 °C (= 3·α(20)/α(200)); u_c = 1,748 °C, U = ±3,50 °C |
| 💡 ADC 10 bit | K, 300/20 °C | LSB 48,8 µV → ±0,589 °C; wskazanie 300,4 °C |
| 🏛️ Galwanometr Siemensa | K, 300/20 °C, R_in = 50 Ω, R_tc = 12,73 Ω | E_mierz = 9,0942 mV, błąd −56,4 °C |
| 🔌 Przedłużenie miedzią | K, 300/20 °C, głowica 80 °C | błąd −60,2 °C (złącze odniesienia w głowicy) |
| 🔗 Przewód kompensacyjny +3 % | K, 300/20 °C, głowica 120 °C | błąd +2,98 °C |
| 📏 Klasa 2 | K, 600 °C | a = max(2,5; 0,0075·600) = 4,5 °C → u = 2,60 °C, U = ±5,20 °C |
| 🌡️ Piec hutniczy | S, 1000/25 °C, Ø 2 mm | R_tc = 0,90 Ω; α = 11,54 µV/°C → kwantyzacja ±0,033 °C |
| 🫀 Temperatura ciała | K, 37/20 °C, 2 m | E_netto = 0,6905 mV; α = 40,91 µV/°C |

Pozostałe presety: kriogenika (T, −100 °C), najwyższa czułość (E, 400 °C), pomiar idealny (K, 24 bit), niska czułość (S, 1200 °C), galwanometr 1900 (100 Ω), miliwoltomierz 1920 (500 Ω), woltomierz cyfrowy 1975 (1 MΩ).

## Wykresy

- **E(T)**: aktywny typ z punktami pracy T_z i T_h (do przeciągania). Pozostałe typy są w tle, każdy tylko w swoim zakresie definicji. Etykiety stoją przy prawej krawędzi, a nad górną krawędzią (↑E, ↑J…) tam, gdzie krzywa opuszcza wykres.
- **α(T)**: ciągła krzywa czułości (tryb eksperta).
- **δT(T)** (na żądanie): błąd nieliniowości z zaznaczonym ekstremum; ekstrapolacja przygaszona.

## Pytania sprawdzające (13)

Przewody przedłużające; klasy tolerancji; prawo temperatur pośrednich; kompensacja złącza zimnego; znak SEM; czułość; nieliniowość (2); przetwornik A/C; rezystancja przewodów; niepewność (GUM); błąd systematyczny; dobór termopary.
Przycisk „🔬 Sprawdź w symulatorze” ustawia scenariusz pytania.

## Ograniczenia modelu

- Charakterystyki idealne NIST. Tolerancję egzemplarza termopary uwzględnia się tylko jako składnik niepewności.
- Rezystywności stałe (20 °C), bez zależności od temperatury wzdłuż przewodu.
- Przewód przedłużający X idealny; przewód kompensacyjny opisany jedną stałą odchyłką czułości ε.
- ADC idealny (bez szumu, offsetu i błędu wzmocnienia); rezystancja przewodów Cu do przyrządu pominięta.

## Źródła

1. G. W. Burns, M. G. Scroger, G. F. Strouse, M. C. Croarkin, W. F. Guthrie, *Temperature-electromotive force reference functions and tables for the letter-designated thermocouple types based on the ITS-90*, NIST Monograph 175, Gaithersburg 1993. https://doi.org/10.6028/NIST.MONO.175
2. IEC 60584-1:2013, *Thermocouples — Part 1: EMF specifications and tolerances*, IEC, Genewa 2013.
3. JCGM 100:2008 (GUM), *Evaluation of measurement data — Guide to the expression of uncertainty in measurement*, JCGM 2008.
4. P. R. N. Childs, *Practical Temperature Measurement*, Butterworth-Heinemann, Oxford 2001 — rozdz. 5–7: termopary, kompensacja, rezystancja przewodów.
5. L. Michalski, K. Eckersdorf, J. Kucharski, J. McGhee, *Temperature Measurement*, wyd. 2, Wiley, Chichester 2001.
6. Omega Engineering, *Thermocouple Technical Reference*, s. Z-49. https://it.omega.com/temperature/Z/pdf/z049-050.pdf
7. Kanthal, karta materiałowa *Nicrosil* — 1,00 Ω·mm²/m (20 °C).
8. Kanthal, karta materiałowa *Nisil* — 0,365 Ω·mm²/m (20 °C).
9. T. J. Seebeck, „Magnetische Polarisation der Metalle und Erze durch Temperatur-Differenz”, *Abh. Preuß. Akad. Wiss.*, Berlin 1822–1823, 265–373.
10. S. Tumański, *Technika pomiarowa*, WNT, Warszawa 2016.

<sub>AGH KMiE 2026 Socha</sub>
