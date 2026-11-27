# Efekty Peltiera i Thomsona — dokumentacja zakładki 3

Plik źródłowy: `PeltierThomson.html` (osadzony w `index.html` jako zakładka „Peltier i Thomson”).
Odbiorcy: studenci Inżynierii Biomedycznej, Elektrotechniki oraz Automatyki i Robotyki (AGH, WEAIiIB).

## Poziomy

| Poziom | Zakres | Status |
|---|---|---|
| **Beginner** | Zamknięty obwód termopary (generator): prąd, ciepło Peltiera na złączach, bilans mocy z efektem Thomsona, dopasowanie obciążenia | v1.7.0 — do akceptacji |
| Pro | Moduł Peltiera (TEC): półprzewodniki Bi₂Te₃, przewodzenie ciepła, ZT, Q_c(I), COP | planowany |
| Expert | Pełny model: rozkład ciepła Thomsona μ(T) wzdłuż przewodów, przewodzenie, nagrzewanie Joule'a | planowany |

Każdy poziom jest budowany i zatwierdzany osobno.

## Model fizyczny — poziom Beginner

### Założenia
1. Temperatury złączy są **ustalone** (termostaty): spoina pomiarowa w Tₓ, złącza Cu|A i Cu|B w T₀. Pomijamy przewodzenie ciepła wzdłuż przewodów i ich nagrzewanie.
2. SEM i czułość z funkcji referencyjnych NIST ITS-90 [1], tych samych co w zakładce 1 (kod kopiowany programowo).
3. Rezystywności przewodów przy 20 °C, niezależne od temperatury [6–8]. Rezystancję przewodów Cu i miernika pomijamy.

### Równania

| Wielkość | Wzór | Jednostki w kodzie |
|---|---|---|
| SEM | E = E_NIST(Tₓ) − E_NIST(T₀) | mV |
| Rezystancja termopary | R_tc = L·(ρ_A + ρ_B)/A, A = πd²/4 | Ω |
| Prąd | I = E/(R_tc + R_L) | mA |
| Współczynnik Peltiera (I relacja Kelvina [3, 4]) | Π_AB(T) = α_AB(T)·T, T w K | mV |
| Ciepło pobrane w spoinie | Q_h = Π(Tₓ)·I | µW |
| Ciepło oddane w złączach zimnych | Q_c = Π(T₀)·I (suma Cu\|A i Cu\|B) | µW |
| Moc elektryczna | P_el = E·I = I²R_tc + I²R_L | µW |
| Ciepło Thomsona netto (z bilansu) | Q_Th = P_el − (Q_h − Q_c) = I·(E − ΔΠ) | µW |
| Moc maksymalna (R_L = R_tc) | P_max = E²/(4R_tc) | µW |

Skąd się bierze Q_Th: z II relacji Kelvina μ_A − μ_B = T·dα_AB/dT [3, 4] wynika Q_Th = −I·∫(μ_A − μ_B)dT. Na poziomie Beginner Q_Th obliczamy z bilansu energii. Rozkład wzdłuż przewodu pokaże poziom Expert.

Prąd w złączach zimnych: Π_Cu,A(T₀) + Π_B,Cu(T₀) = Π_B,A(T₀) = −Π_AB(T₀). Ciepło obu złączy zimnych nie zależy więc od materiału przewodów doprowadzających. To prawo metalu pośredniego zastosowane do efektu Peltiera.

### Przykład kontrolny (typ K, Tₓ = 300 °C, T₀ = 20 °C, L = 10 m, Ø 1 mm, R_L = 15,8 Ω)

| Wielkość | Wartość |
|---|---|
| E | 11,410 mV |
| α(300 °C), α(20 °C) | 41,45 µV/K, 40,33 µV/K |
| Π(Tₓ) | 41,45 µV/K × 573,15 K = 23,75 mV |
| Π(T₀) | 40,33 µV/K × 293,15 K = 11,82 mV |
| R_tc | 10 m × (706 + 294) nΩ·m / 0,785 mm² = 12,73 Ω |
| I | 399 µA |
| Q_h − Q_c + Q_Th | 9,48 − 4,72 − 0,21 = 4,56 µW |
| I²R_tc + I²R_L | 2,03 + 2,53 = 4,56 µW ✓ |
| P_max | 2,56 µW |

Wartości zgodne z wynikami aplikacji (test Playwright).

### Dane materiałowe

| Typ | Przewód A (+) | ρ_A [nΩ·m] | Przewód B (−) | ρ_B [nΩ·m] | Źródło |
|---|---|---|---|---|---|
| K | Chromel | 706 | Alumel | 294 | [6] |
| J | Żelazo | 100 | Konstantan | 489 | [6] |
| T | Miedź | 15,4 | Konstantan | 489 | [6] |
| E | Chromel | 706 | Konstantan | 489 | [6] |
| N | Nicrosil | 1000 | Nisil | 365 | [7, 8] |
| S | Pt-10%Rh | 185 | Platyna | 98,3 | [6] |

Przeliczenie wartości Omega (Ω·cmil/ft przy 0 °C): 1 Ω·cmil/ft = 1,6624 nΩ·m. Wartości Kanthal (Ω·mm²/m przy 20 °C): 1 Ω·mm²/m = 1000 nΩ·m.
Zakładka 1 używa dla typu N wartości 1060/370 nΩ·m. Różnica (~5 %) nie wpływa na wnioski; ujednolicenie jest możliwe w kolejnej wersji.

## Wizualizacje

- **Schemat obwodu**: elektrody A i B, przewody Cu, rezystor R_L, odczyt I i U. Elektrony płyną przeciwnie do prądu umownego, a ich prędkość rośnie logarytmicznie z |I|. Strzałki ciepła mają grubość logarytmiczną w mocy: do spoiny wchodzi Π(Tₓ)·I, ze złączy zimnych wychodzi Π(T₀)·I.
- **Bilans mocy** (wykres wodospadowy): +Q_h, −Q_c, ±Q_Th → E·I, rozdzielone na I²R_tc i I²R_L.
- **Dopasowanie obciążenia**: P_L(R_L) i I(R_L) na osi logarytmicznej 0,1 Ω–10 kΩ, z zaznaczonym R_L = R_tc i punktem pracy.
- **Π_AB(T)**: krzywa z punktami Π(T₀) i Π(Tₓ) oraz porównanie ΔΠ z E (różnica = efekt Thomsona na jednostkę prądu).

## Wartość dydaktyczna według kierunku

- **Inżynieria Biomedyczna**: dlaczego pomiar temperatury termoparą musi być bezprądowy. Prąd chłodzi spoinę, co ma znaczenie przy pomiarach w tkance. Przejście do modułów Peltiera (chłodzenie próbek, PCR — poziom Pro).
- **Elektrotechnika**: termopara jako źródło z rezystancją wewnętrzną, twierdzenie o dopasowaniu, bilans energii.
- **Automatyka i Robotyka**: wpływ rezystancji wejściowej przyrządu na wynik (U vs E), dobór obciążenia czujnika.

## Pytania sprawdzające (7)

1. Kierunek ciepła Peltiera w generatorze.
2. Wartość Π = α·T (kelwiny, nie °C; różnica od napięcia kontaktowego).
3. Dopasowanie obciążenia R_L = R_tc.
4. Odwracalność ciepła Peltiera a ciepło Joule'a.
5. Bilans energii i efekt Thomsona.
6. Dlaczego woltomierz musi mieć dużą rezystancję wejściową.
7. Wpływ średnicy przewodów na P_max.

## Źródła

1. G. W. Burns, M. G. Scroger, G. F. Strouse, M. C. Croarkin, W. F. Guthrie, *Temperature-electromotive force reference functions and tables for the letter-designated thermocouple types based on the ITS-90*, NIST Monograph 175, NIST, Gaithersburg 1993. https://doi.org/10.6028/NIST.MONO.175 — funkcje E(T), α(T) = dE/dT.
2. J. C. A. Peltier, „Nouvelles expériences sur la caloricité des courants électriques”, *Annales de Chimie et de Physique* 56 (1834) 371–386 — odkrycie efektu.
3. W. Thomson, „On a mechanical theory of thermo-electric currents”, *Proceedings of the Royal Society of Edinburgh* 3 (1851, wyd. 1857) 91–98. https://doi.org/10.1017/S0370164600027310 — relacje Kelvina, efekt Thomsona.
4. M. Wagner, *Simulation of Thermoelectric Devices*, rozprawa doktorska, TU Wien, rozdz. „Thermoelectric effects”. https://iue.tuwien.ac.at/phd/mwagner/node17.html — relacje Kelvina: π_ab/T = α_ab, T·dα_ab/dT = χ_a − χ_b.
5. H. B. Callen, *Thermodynamics and an Introduction to Thermostatistics*, wyd. 2, Wiley, New York 1985 — termodynamika procesów nieodwracalnych, bilans energii w obwodzie termoelektrycznym.
6. Omega Engineering, *Thermocouple Technical Reference*, s. Z-49 (rezystywność stopów termoparowych). https://it.omega.com/temperature/Z/pdf/z049-050.pdf
7. Kanthal, karta materiałowa *Nicrosil* (drut termoparowy) — 1,00 Ω·mm²/m przy 20 °C.
8. Kanthal, karta materiałowa *Nisil* (drut termoparowy) — 0,365 Ω·mm²/m przy 20 °C.

Literatura uzupełniająca: D. D. Pollock, *Thermoelectricity: Theory, Thermometry, Tool*, ASTM STP 852, 1985.

<sub>AGH KMiE 2026 Socha</sub>
