# Efekt Seebecka — dokumentacja zakładki 2

Plik źródłowy: `SeebeckVizualizacja.html` (osadzony w `index.html` jako zakładka „Efekt Seebecka”).
Odbiorcy: studenci Inżynierii Biomedycznej, Elektrotechniki oraz Automatyki i Robotyki (AGH, WEAIiIB).

Zakładka pokazuje mechanizm powstawania SEM termoelektrycznej: gdzie powstaje napięcie, dlaczego prawo temperatur pośrednich działa (i kiedy przestaje), czym są napięcia kontaktowe i dlaczego woltomierz ich nie widzi. Obwód jest otwarty, czyli prąd nie płynie. Obwód z prądem pokazuje zakładka 3.

## Obwód

Cyfrowy woltomierz → przewody Cu (metal C) → złącza odniesienia Cu|A i Cu|B (T₀) → elektrody A i B → spoina pomiarowa A|B (Tₓ).
Elektroda ma długość znormalizowaną x ∈ [0, 1]: x = 0 to złącze z Cu, x = 1 to spoina. Każda elektroda jest podzielona na N = 30 segmentów.

## Model

### Rozkład temperatury

T(x) = T₀ + (Tₓ − T₀)·x + s·ΔT_ź·b(x), b(x) = exp(−(x − x_ź)²/(2σ²))·(1 − e^(−x/p))·(1 − e^(−(1−x)/p)).

- Temperatury złączy są ustalone (termostatowane). Czynniki z p = 0,025 wygaszają garb przy końcach, żeby T(0) i T(1) się nie zmieniały.
- Źródło ciepła (s = +1, świeczka) lub zimna (s = −1, lód) działa na elektrodę A, B albo obie. Ma położenie x_ź, amplitudę ΔT_ź i szerokość σ = 0,075.
- Różne temperatury zacisków: zimny koniec elektrody B ma T₀ + δ.

### SEM jako suma wkładów segmentów

dV_i = α(x)·[T(x_{i+1}) − T(x_i)], całkowane w 8 podkrokach na segment (ostre krawędzie niejednorodności).

SEM = Σ dV_A − Σ dV_B − α_Cu·δ.

Dla jednorodnych przewodów suma się teleskopuje: SEM = (α_A − α_B)(Tₓ − T₀), niezależnie od kształtu T(x). To prawo temperatur pośrednich.

### Niejednorodność przewodu

Odcinek elektrody A lub B (środek, szerokość, Δα) ma α + Δα. Jego wkład to Δα·[T(koniec) − T(początek)]: działa jak pasożytnicza termopara ze złączami na krawędziach odcinka. Wkład znika w strefie izotermicznej albo gdy obie krawędzie mają tę samą temperaturę.

### Napięcia kontaktowe i poziomy Fermiego

- Napięcie kontaktowe Volty: E(X, Y) = ψ_X − ψ_Y = (W_Y − W_X)/e. Suma w zamkniętej pętli wynosi 0.
- Potencjał elektrochemiczny (poziom Fermiego) jest ciągły na złączach. Woltomierz mierzy jego różnicę, czyli dokładnie SEM.
- Diagram poziomów Fermiego pokazuje stan przed zetknięciem: poziom Fermiego metalu leży na −W. Obsadzenie stanów jest liczone z rozkładu Fermiego–Diraca w skali rzeczywistej (rozmycie ≈ 4kT). Strzałka biegnie od niższego do wyższego poziomu Fermiego i ma długość |E(X, Y)|·e.
- Wykres potencjału ma dwa tryby: elektrochemiczny (mierzony, ciągły) i elektrostatyczny z napięciami kontaktowymi (skoki rzędu 0,1–0,5 V).

### Konwencja znaku i animacja

α = (V_zimny − V_gorący)/(T_gorący − T_zimny). Dla α < 0 nadmiar elektronów gromadzi się przy zimnym końcu, dla α > 0 przy gorącym. Dlatego w termoparze K chromel (α > 0) jest przewodem dodatnim.
Animacja zagęszcza elektrony przy ujemnym końcu przewodu (siła nierównowagi rośnie z |α|), a amplituda drgań cieplnych rośnie z √T. Rzeczywista nierównowaga ładunku jest znikoma; rysunek ją celowo przesadza.

## Baza materiałów (24 pozycje)

α — bezwzględny współczynnik Seebecka w pobliżu temperatury pokojowej, w modelu stały (brak efektu Thomsona). W — praca wyjścia.

### Metale czyste

| Materiał | α [µV/K] | W [eV] | Porównanie z literaturą |
|---|---|---|---|
| Pt | −5,0 | 5,65 | α ≈ −5 [3]; W wg [1] |
| Pd | −10,7 | 5,22 | α ≈ −9,7 (z wartości względem Pt [4]) |
| Au | +1,9 | 5,10 | α ≈ +1,9 [2] |
| Ag | +1,5 | 4,26 | α ≈ +1,5 [2] |
| Cu | +1,8 | 4,65 | α ≈ +1,8 [2] |
| Al | −1,7 | 4,28 | α ≈ −1,7 [2] |
| Ni | −19,5 | 5,15 | α ≈ −20 [2] |
| Fe | +13,4 | 4,50 | α ≈ +14…15 [2, 4] |
| W | +1,1 | 4,55 | inne źródła: ok. +2,5 [2] |
| Cr | +21,8 | 4,50 | — |
| Co | −30,8 | 5,00 | inne źródła: ok. −18 (z wartości względem Pt [4]) |
| Bi | −72 | 4,22 | −72…−77 [2, 4] |
| Sb | +47 | 4,55 | +42…+49 [2, 4] |
| Mo | +5,6 | 4,60 | α ≈ +5 [2] |

Prace wyjścia metali czystych odpowiadają zestawieniu Michaelsona [1] (polikryształy).
Wartości α w literaturze różnią się zależnie od czystości próbki i temperatury odniesienia. Tabele podają je często względem platyny: wartość bezwzględną daje dodanie α_Pt ≈ −5 µV/K [3]. Rozbieżności dla W i Co warto sprawdzić przy kolejnej aktualizacji bazy.

### Stopy termoparowe i materiały termoelektryczne (szacunki, „≈”)

| Materiał | α [µV/K] | W [eV] |
|---|---|---|
| Chromel (Ni-Cr) | +21,7 | 5,09 ≈ |
| Alumel (Ni-Al) | −17,7 | 5,12 ≈ |
| Konstantan (Cu-Ni) | −37,0 | 4,88 ≈ |
| Nicrosil | +13,0 | 5,06 ≈ |
| Nisil | −13,2 | 5,14 ≈ |
| Pt-13%Rh | +0,3 | 5,56 ≈ |
| Pt-10%Rh | +0,4 | 5,58 ≈ |
| Bi₂Te₃ (n) | −200 | 5,10 ≈ |
| PbTe (n) | −180 | 4,60 ≈ |
| GeTe (p) | +120 | 5,20 ≈ |

α stopów dobrano tak, by różnice odtwarzały czułości NIST ITS-90 [5] przy 0 °C. Kontrola: K 21,7 + 17,7 = 39,4 (NIST 39,45); J 13,4 + 37,0 = 50,4 (50,38); T 1,8 + 37,0 = 38,8 (38,75); E 21,7 + 37,0 = 58,7 (58,67); N 13,0 + 13,2 = 26,2 (26,13); R 0,3 + 5,0 = 5,3 (5,29); S 0,4 + 5,0 = 5,4 (5,40) µV/K.
Prace wyjścia stopów i półprzewodników są szacunkami. Zależą od składu i stanu powierzchni, a w aplikacji oznaczone są „≈”.

Presety par: K, J, T, E, N, R, S. Elektrody A i B można też wybrać niezależnie, co daje dowolną parę z 24 materiałów.

## Wykresy

- **T(x)**: rozkład temperatury wzdłuż elektrod.
- **dV na segment**: słupki ±. Przy niemonotonnym T(x) widać kasowanie się wkładów.
- **Potencjał wzdłuż obwodu**: tryb elektrochemiczny lub elektrostatyczny z napięciami kontaktowymi.
- **Poziomy Fermiego**: pod schematem, wyrównane do złączy; kolejność A | Cu | B przy T₀ oraz A | B przy Tₓ.

## Pytania sprawdzające (12)

Niejednorodność przewodu; temperatura zacisków; znak współczynnika Seebecka; biegunowość termopary; prawo temperatur pośrednich; teleskopowanie; napięcie kontaktowe (2); pomiar a napięcia kontaktowe; prawo metalu pośredniego; termopara T; poziomy Fermiego.

## Ograniczenia modelu

- α stałe w temperaturze, więc SEM jest liniowa w (Tₓ − T₀). Pełną nieliniowość pokazuje zakładka 1, a efekt Thomsona zakładka 3 (poziom Expert).
- Rozkład T(x) jest zadany (prosta plus garb Gaussa), a nie wyliczony z równania przewodzenia.
- Napięcia kontaktowe pokazane są jako równowagowe różnice prac wyjścia, bez wpływu stanu powierzchni.
- Teoria w aplikacji (sekcja 6) wyjaśnia, dlaczego współczesny opis lokalizuje SEM w objętości przewodów, a nie w złączach.

## Źródła

1. H. B. Michaelson, „The work function of the elements and its periodicity”, *J. Appl. Phys.* 48 (1977) 4729–4733. https://doi.org/10.1063/1.323539
2. Seebeck coefficient — tabela wartości względem Pt (temperatura pokojowa), Wikipedia, za: „The Seebeck Coefficient”, *Electronics Cooling*. https://en.wikipedia.org/wiki/Seebeck_coefficient
3. J. P. Moore, R. S. Graves, „Absolute Seebeck coefficient of platinum from 80 to 340 K and the thermal and electrical conductivities of lead from 80 to 400 K”, *J. Appl. Phys.* 44 (1973) 1174.
4. Tabela współczynników Seebecka względem Pt, za: F. Cardarelli, *Materials Handbook: A Concise Desktop Reference*, Springer. https://commons.princeton.edu/josephhenry/wp-content/uploads/sites/71/2019/08/Table-of-Seebeck-Coefficients-JH.pdf
5. G. W. Burns i in., NIST Monograph 175, 1993. https://doi.org/10.6028/NIST.MONO.175
6. H. B. Callen, *Thermodynamics and an Introduction to Thermostatistics*, wyd. 2, Wiley 1985 — opis objętościowy SEM i relacje Kelvina.

<sub>AGH KMiE 2026 Socha</sub>
