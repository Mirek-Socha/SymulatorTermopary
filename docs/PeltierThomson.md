# Efekty Peltiera i Thomsona — dokumentacja zakładki 3

Plik źródłowy: `PeltierThomson.html` (osadzony w `index.html` jako zakładka „Peltier i Thomson”).
Odbiorcy: studenci Inżynierii Biomedycznej, Elektrotechniki oraz Automatyki i Robotyki (AGH, WEAIiIB).

## Poziomy

| Poziom | Zakres | Status |
|---|---|---|
| **Beginner** | Zamknięty obwód termopary (generator): prąd, ciepło Peltiera na złączach, bilans mocy z efektem Thomsona, dopasowanie obciążenia | v1.7.0 |
| **Pro** | Moduł Peltiera (TEC): półprzewodniki Bi₂Te₃, przewodzenie ciepła, ZT, T_c(I), Q_c(I), COP, grzanie prądem odwróconym | v1.8.0 |
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
Od v1.7.0 te same wartości stosuje zakładka 1 (`TC_PROPS` w `SymulatorTermopary.html`).

## Scenariusze (presety)

Wartości obliczone w aplikacji (T₀ = 20 °C).

| Scenariusz | Ustawienia | Co pokazuje |
|---|---|---|
| ⚖️ Dopasowanie mocy | K, 300 °C, 10 m, Ø 1 mm, R_L = R_tc = 12,7 Ω | P_L = P_max = 2,56 µW; połowa mocy elektrycznej grzeje przewody |
| 🔎 Pomiar woltomierzem | K, 300 °C, R_L = 10 kΩ | I ≈ 1,1 µA, U ≈ E; ciepło Peltiera ≈ 27 nW |
| ⚡ Zwarcie | K, 300 °C, R_L = 0,1 Ω | ciepło Peltiera w spoinie 21 µW, P_L ≈ 79 nW |
| 🩺 Cienka sonda w 37 °C | T, 37 °C, 2 m, Ø 0,25 mm, R_L = 0,1 Ω | nawet przy zwarciu spoina traci < 0,5 µW (pomiary biomedyczne) |
| 🔋 Krótka i gruba | K, 1000 °C, 0,5 m, Ø 3,2 mm, R_L = 0,1 Ω | R_tc ≈ 0,06 Ω, I ≈ 0,25 A, P_L ≈ 6 mW |
| 📈 Typ E | E, 800 °C, dopasowanie | E ≈ 60 mV, P_max ≈ 59 µW |
| 🌀 Typ T | T, 350 °C, dopasowanie | ciepło Thomsona ≈ −51 % E·I (przewody oddają ciepło) |
| 🔄 K w 1300 °C | K, 1300 °C, dopasowanie | ciepło Thomsona zmienia znak: +16 % E·I (maksimum α_K ≈ 42,7 µV/K przy ≈ 530 °C) |
| 🏭 Platyna w 1500 °C | S, 1500 °C, Ø 0,5 mm, dopasowanie | α ≈ 12 µV/K; ciepło Thomsona ≈ −27 % E·I |

Zmiana dowolnej nastawy przełącza scenariusz na „własne ustawienia”.

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

## Model fizyczny — poziom Pro (moduł Peltiera)

### Założenia
1. Model jednowymiarowy, N jednakowych par nóg p–n połączonych elektrycznie szeregowo i cieplnie równolegle [11, 14].
2. Własności α, ρ, κ stałe: Bi₂Te₃ — wartości z 25 °C [9]; para chromel–alumel — α z NIST przy T_h [1], ρ [6], κ przy 100 °C [13].
3. Strona gorąca na idealnym radiatorze (T_h stała). Pominięte: rezystancje kontaktów, opór cieplny ceramiki, straty do otoczenia, efekt Thomsona w nogach.
4. Obiekt na stronie zimnej oddaje moc Q_c (suwak), a T_c wynika z bilansu.

### Równania (na parę: α = α_p − α_n, R = (ρ_p+ρ_n)L/A, K = (κ_p+κ_n)A/L)

| Wielkość | Wzór |
|---|---|
| Wydajność chłodzenia | Q_c = N·(α·I·T_c − ½·I²·R − K·ΔT) |
| Napięcie, moc | U = N·(α·ΔT + I·R), P_el = U·I |
| Ciepło do radiatora | Q_h = Q_c + P_el |
| Temperatura strony zimnej | T_c = (Q_c/N + ½I²R + K·T_h)/(α·I + K) |
| Prąd najniższej T_c | I* = [−KR + √(K²R² + 2α²R(Q_c/N + K·T_h))]/(αR); wtedy T_c = I*·R/α |
| Dobroć | Z = α²/(R·K), ZT |
| Granice | ΔT_max = ½·Z·T_c² (Q_c = 0), I_max = α·T_c,min/R, Q_max = N·α²·T_h²/(2R) (ΔT = 0) |
| Prąd maksymalnego COP przy ΔT | I_opt = α·ΔT/(R·(√(1+Z·T_m) − 1)) |
| COP optymalny | COP_opt = (T_c/ΔT)·(√(1+Z·T_m) − T_h/T_c)/(√(1+Z·T_m) + 1) [14] |

### Dane materiałowe

| Materiał | α [µV/K] | ρ [µΩ·m] | κ [W/(m·K)] | Źródło |
|---|---|---|---|---|
| p: Bi₀,₄₆Sb₁,₅₄Te₃ | +244,78 | 16,92 (σ = 590,86 S/cm) | 0,964 | [9] |
| n: Bi₂Te₂,₇Se₀,₃ | −165,03 | 10,56 (σ = 947,42 S/cm) | 1,172 | [9] |
| Chromel (Thermothal P) | α_K z NIST | 0,706 | 19,2 (100 °C) | [1, 6, 13] |
| Alumel (Thermothal N) | (para) | 0,294 | 29,7 (100 °C) | [1, 6, 13] |

Para Bi₂Te₃: α = 409,8 µV/K, ZT(27 °C) = 0,86. Para chromel–alumel: ZT ≈ 0,010.

### Weryfikacja z kartą katalogową TEC1-12706 [12]

Geometria: 127 par, nogi 1,4 × 1,4 mm. Wysokość nogi 1,15 mm dobrano tak, by R_moduł = 2,05 Ω jak w karcie. T_h = 27 °C.

| Parametr | Model | Karta [12] |
|---|---|---|
| R_moduł | 2,05 Ω | 2,05 Ω |
| ΔT_max | 73,5 K | 74 K |
| Q_max | 59,6 W | 66 W |
| I_max | 5,76 A | 6,3 A |
| U_max | 15,6 V | 16,8 V |

Zgodność w granicach ok. 10 % przy danych materiałowych z niezależnego źródła [9].

### Przykład kontrolny (preset „Najlepsza sprawność przy ΔT = 20 K”)

T_h = 27 °C, T_c = 7 °C, T_m = 290,15 K, Z·T_m = 0,830, √(1+ZT_m) = 1,353.
I_opt = 409,8·10⁻⁶ × 20 / (0,016123 × 0,353) = 1,44 A;
Q_c = 127·(409,8·10⁻⁶·1,44·280,15 − ½·1,44²·0,016123 − 0,003639·20) = 9,63 W;
P_el = 5,75 W, COP = 1,676 (= COP_opt ze wzoru Goldsmida). Wartości zgodne z aplikacją.

### Scenariusze Pro

| Scenariusz | Wynik w aplikacji |
|---|---|
| ❄️ Typowy moduł, 3 A, 20 W | T_c = −1,5 °C (ΔT 28,6 K), U = 7,6 V, P_el = 22,9 W, Q_h = 42,9 W, COP = 0,87 |
| 📉 Maksymalna różnica temperatur | Q_c = 0, I = 5,76 A, T_c = −46,5 °C (ΔT 73,5 K) |
| ⚠️ Za duży prąd (1,5·I_max) | T_c = −15,3 °C zamiast minimum −20,8 °C przy 6,4 A; P_el = 172 W |
| ♻️ Najlepsza sprawność przy ΔT = 20 K | I = 1,44 A, Q_c = 9,6 W, COP = 1,68 |
| 🔥 Odwrócony prąd (−1 A) | izolowany obiekt ogrzewa się do 67,6 °C |
| 🧪 Próbki w 4 °C (T_h = 30 °C, 10 W) | I = 1,74 A, P_el = 8,6 W, COP = 1,17 |
| 🔦 Dioda laserowa (31 par, 25 °C, 1,5 W, T_h = 35 °C) | I = 0,61 A, U = 0,65 V, COP = 3,8 |
| 🔩 Chromel–alumel | I = 20,7 A, ΔT_max = 1,5 K, ZT = 0,010 |

### Interakcja
- Przeciąganie (mysz, dotyk): T_c(I) i COP(I) — prąd; Q_c(I) — prąd (oś x) i obciążenie cieplne (oś y); w poziomie Beginner wykres P_L(R_L) — rezystancja obciążenia.
- Dymki na słupkach obu bilansów: nazwa składnika, równanie, podstawienie wartości i krótki komentarz.
- COP jest wyświetlany tylko przy ΔT > 0. Gdy obiekt jest cieplejszy od radiatora, ciepło płynie samoistnie i COP traci sens.

### Pytania sprawdzające Pro (7)
Optymalny prąd; warunki ΔT_max; dlaczego półprzewodniki (ZT, Wiedemann–Franz); grzanie prądem odwróconym; bilans radiatora Q_h = Q_c + P_el; COP a ΔT; wpływ liczby par N.

## Źródła

1. G. W. Burns, M. G. Scroger, G. F. Strouse, M. C. Croarkin, W. F. Guthrie, *Temperature-electromotive force reference functions and tables for the letter-designated thermocouple types based on the ITS-90*, NIST Monograph 175, NIST, Gaithersburg 1993. https://doi.org/10.6028/NIST.MONO.175 — funkcje E(T), α(T) = dE/dT.
2. J. C. A. Peltier, „Nouvelles expériences sur la caloricité des courants électriques”, *Annales de Chimie et de Physique* 56 (1834) 371–386 — odkrycie efektu.
3. W. Thomson, „On a mechanical theory of thermo-electric currents”, *Proceedings of the Royal Society of Edinburgh* 3 (1851, wyd. 1857) 91–98. https://doi.org/10.1017/S0370164600027310 — relacje Kelvina, efekt Thomsona.
4. M. Wagner, *Simulation of Thermoelectric Devices*, rozprawa doktorska, TU Wien, rozdz. „Thermoelectric effects”. https://iue.tuwien.ac.at/phd/mwagner/node17.html — relacje Kelvina: π_ab/T = α_ab, T·dα_ab/dT = χ_a − χ_b.
5. H. B. Callen, *Thermodynamics and an Introduction to Thermostatistics*, wyd. 2, Wiley, New York 1985 — termodynamika procesów nieodwracalnych, bilans energii w obwodzie termoelektrycznym.
6. Omega Engineering, *Thermocouple Technical Reference*, s. Z-49 (rezystywność stopów termoparowych). https://it.omega.com/temperature/Z/pdf/z049-050.pdf
7. Kanthal, karta materiałowa *Nicrosil* (drut termoparowy) — 1,00 Ω·mm²/m przy 20 °C.
8. Kanthal, karta materiałowa *Nisil* (drut termoparowy) — 0,365 Ω·mm²/m przy 20 °C.
9. N. Kumari, J. Chung, S. Oh, J. Jang, J. Park, J. H. Son, S. Park, B. Ryu, „Reference compositions for bismuth telluride thermoelectric materials for low-temperature power generation”, arXiv:2507.06101 (2025). https://arxiv.org/abs/2507.06101 — α, σ, κ, zT materiałów Bi₂Te₃ (p i n) w 25 °C.
10. H. J. Goldsmid, „Bismuth Telluride and Its Alloys as Materials for Thermoelectric Generation”, *Materials* 7 (2014) 2577–2592. https://doi.org/10.3390/ma7042577
11. Ferrotec, *Thermoelectric Technical Reference*, rozdz. 11 „Mathematical Modeling of Thermoelectric Cooling Modules”. https://thermal.ferrotec.com/?p=107 — równania Q_c, U, Q_h, COP, Q_max, ΔT_max.
12. Thermonamic, karta katalogowa modułu TEC1-12706. https://akizukidenshi.com/goodsaffix/TETC1-12706.pdf — dane do weryfikacji modelu.
13. Kanthal, karty materiałowe *Thermothal P* i *Thermothal N* (κ = 19,2 i 29,7 W/(m·K) przy 100 °C).
14. H. J. Goldsmid, *Introduction to Thermoelectricity*, wyd. 2, Springer, Berlin 2016. https://doi.org/10.1007/978-3-662-49256-7 — ΔT_max, COP_opt, prawo Wiedemanna–Franza w kontekście ZT.

Literatura uzupełniająca: D. D. Pollock, *Thermoelectricity: Theory, Thermometry, Tool*, ASTM STP 852, 1985.

<sub>AGH KMiE 2026 Socha</sub>
