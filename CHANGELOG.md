# Changelog — Termopary (AGH Metrologia)

## [v1.7.0] — 2026-11-27

### Nowa zakładka: Peltier i Thomson — poziom Beginner
- Zamknięty obwód termopary jako generator: prąd I = E/(R_tc + R_L), rezystancja R_tc z geometrii i rezystywności przewodów (Omega Z-49, Kanthal)
- Ciepło Peltiera na złączach z relacji Kelvina Π = α·T (α z NIST ITS-90): spoina pobiera, złącza zimne oddają; animacja elektronów i strzałki ciepła
- Bilans mocy (wykres wodospadowy) z ciepłem Thomsona wyznaczanym z zasady zachowania energii
- Dopasowanie obciążenia: P_L(R_L), I(R_L), P_max przy R_L = R_tc
- Wykres Π_AB(T) z porównaniem ΔΠ i E
- Teoria z cytowaniami (NIST Monograph 175, Peltier 1834, Thomson 1851, Callen, Omega, Kanthal); 7 pytań sprawdzających
- Przełącznik poziomów Beginner / Pro / Expert (Pro i Expert — kolejne etapy)
- Dokumentacja modelu i źródeł: `docs/PeltierThomson.md`
- 9 scenariuszy z opisami (dopasowanie, woltomierz, zwarcie, sonda w 37 °C, gruba termopara, typ E, typ T, K w 1300 °C, S w 1500 °C); zakres Tₓ do górnej granicy typu

### Symulator pomiaru
- Rezystywności przewodów ujednolicone ze źródłami (Omega Z-49, Kanthal): N 1000/365 nΩ·m (było 1060/370), poprawiona kolejność przewodów typu S (Pt-10%Rh dodatni) i wartości 185/98,3 nΩ·m, drobne korekty J, T, E; nowa pozycja w literaturze

## [v1.6.0] — 2026-11-27

### Symulator pomiaru
- Klasy tolerancji termopar wg IEC 60584-1 (K, N, J, T, E, S) — nowy składnik budżetu niepewności (u = a/√3)
- Przedłużenie do przyrządu: przewód przedłużający X, kompensacyjny C (odchyłka czułości ε), zwykła miedź; temperatura głowicy T_g; błąd systematyczny w budżecie
- Scenariusze: przedłużenie miedzią, przewód kompensacyjny, klasa 2 przy 600 °C; wyróżnienie wiersza U w tabeli budżetu
- Teoria: klasy tolerancji, przewody przedłużające i kompensacyjne

### Efekt Seebecka
- Niejednorodność przewodu (odcinek A lub B o zmienionym α): kreskowanie na schemacie, zacienienie na wykresie segmentów, α(x) w gęstości e⁻; obliczenia z podziałem segmentów na podkroki
- Różne temperatury złączy Cu|A i Cu|B: wkład −α_Cu·δ, przebieg Cu(−) na wykresie potencjału, temperatura B na diagramie Fermiego
- Pasek wyników: odchyłka Δ w mV i °C z nazwaniem przyczyny
- Teoria: niejednorodność (pasożytnicza termopara na krawędziach odcinka), temperatura zacisków

### Pytania sprawdzające
- +2 pytania w każdej zakładce (przewód miedziany, klasa tolerancji; niejednorodność, zaciski)

## [v1.5.0] — 2026-11-27

### Dodano
- **Pytania sprawdzające** (❓ Sprawdź się) w obu zakładkach: 11 pytań o tor pomiarowy (prawo temperatur pośrednich, CJC, znak SEM, czułość, nieliniowość, ADC, R_tc, GUM, dobór typu) i 10 o mechanizm efektu Seebecka (znak α, biegunowość, teleskopowanie, napięcia kontaktowe, prawo metalu pośredniego, poziomy Fermiego); losowa kolejność, wyjaśnienia, wynik, scenariusze „🔬 Sprawdź w symulatorze”
- **Nieliniowość charakterystyki** (📐, na żądanie): prosta przez punkty pracy na wykresie E(T), zacieniowana odchyłka, wykres błędu δT(T) z maksimum, nieliniowość w % zakresu; nowa sekcja teorii

## [v1.4.0] — 2026-11-27

### Symulator pomiaru
- Charakterystyki E(T) liczone z funkcji referencyjnych **NIST ITS-90** (wielomiany, typ K z członem wykładniczym) zamiast interpolacji liniowej tablic co 100 °C (błąd do ~0,1 mV); funkcja odwrotna metodą bisekcji + Newtona
- Czułość α(T) jako pochodna analityczna — ciągła krzywa zamiast schodków
- Usunięte literówki tablic: J(900), E(300), E(1000); zakresy: K do 1372 °C, S do 1768 °C, krzywe tła bez „ogonów” poza zakresem
- Kwantyzacja ADC wchodzi do wyniku T_mierz (tryb eksperta) + sygnalizacja nasycenia
- Etykiety typów termopar nad górną krawędzią wykresu E(T) w punktach wyjścia krzywych o większej czułości
- Budżet niepewności wg GUM: u = a/√3, u_c (RSS), U (k=2); błąd CJC przenoszony przez α(T_z)/α(T_h); rezystancja przewodów jako błąd systematyczny (poprawka), liczony dokładnie

### Efekt Seebecka
- Nowy układ: schemat + poziomy Fermiego (pod schematem, wyrównane do złączy) | wykresy; jedna kolumna < 960 px
- Schemat: cyfrowy woltomierz, przewody Cu/A/B jednakowej grubości, spoina pomiarowa jako styk A|B
- **Poprawiony znak gęstości e⁻**: α<0 → nadmiar przy zimnym końcu, α>0 → przy gorącym (zgodnie z biegunowością termopar)
- Napięcia kontaktowe z różnicy **prac wyjścia** W (nie energii Fermiego od dna pasma); strzałki grotem do metalu o wyższym potencjale
- Diagram Fermiego: oś względem próżni, kolejność A | Cu | B, rozmycie Fermiego–Diraca w skali rzeczywistej
- Wykres potencjału: tryb elektrochemiczny (mierzony) i elektrostatyczny (skoki kontaktowe, suma w pętli = 0)
- Temperatury złączy ustalone przy źródle zewnętrznym (wcześniej ogon gaussowski zmieniał T złączy)
- Baza materiałów: α stopów skalibrowane do czułości NIST przy 0 °C, dodane prace wyjścia, preset R, poprawiony S (Pt-10%Rh)
- Animacja wstrzymywana w nieaktywnej zakładce

## [v1.3.0] — 2026-06-02

### Dodano
- **Elektrony z inverse-CDF** — rozkład gęstości e⁻ oparty na lokalnej T(x) z uwzględnieniem źródła ciepła/zimna; gradient radialny (białe jądro → kolor metalu → przezroczysty); pulsacja przy aktywnym źródle
- **Prawdziwy model fizyczny** — α>0: zagęszczenie przy T₀ (zimny); α<0: zagęszczenie przy Tₓ (gorący); zmiana znaku α widoczna gołym okiem

### Poprawiono
- Schemat obwodu: woltomierz po lewej (T₀), spoina gorąca po prawej (Tₓ) — spójne z wykresami T(x) i V(x)
- Gęstość elektronów: usunięto błędne `1-x` w CDF; kierunek zagęszczenia poprawiony
- Wykresy drawTemp/drawSegs/drawVolt: dodano `ctx.clip()` — krzywe i słupki nie wychodzą poza obszar
- drawSegs: linia zerowa przeniesiona na środek każdej połówki; słupki ±symetryczne; clip per panel
- Canvas: jawne wysokości `clamp(vh)` zamiast łańcucha flex — działa w srcdoc iframe
- Naprawiony krytyczny błąd składni JS (`parseColor` osierocony blok) blokujący cały skrypt
- Naprawiony `ptAtS` — clamp `s∈[0,1]` i guard `idx<pts.length-1`; koniec błędu `undefined.x`
- Header Symulatora: `flex-wrap:nowrap`, etykiety `.btn-lbl` chowane przy ≤600px
- Zakładki index.html: `flex:1;min-width:0` na `.tab` — koniec nakładania na nav-right
- Czcionki powiększone w całej aplikacji Seebeck (canvas `fs` skalowan od szerokości)

---

## [v1.2.0] — 2026-05-28

### Dodano
- **`SeebeckVizualizacja.html`** — interaktywna wizualizacja efektu Seebecka
  - Schemat obwodu: topologia wg normy, gęstość e⁻, kliknij/przeciągnij źródło
  - Zewnętrzne źródło ciepła/zimna (🔥/❄️) na elektrodzie A, B lub obu
  - N segmentów (10–60) z wyliczaniem dV = α·ΔT na segment
  - Wykresy: T(x), słupki dV, skumulowany V(x)
  - Prawo temperatur pośrednich — SEM niezmieniona mimo niemonotonnego T(x)
- **`index.html`** — wrapper z zakładkami (srcdoc, działa lokalnie bez serwera HTTP)
- Globalny przełącznik motywu jasny/ciemny (postMessage do obu iframe'ów)
- Teoria Seebecka jako sliding overlay (📖 Teoria)
- Drag T_h i T_z na wykresie E(T)
- Tło charakterystyk pozostałych typów TC + górne etykiety α>αsel

### Poprawiono
- Dropdown scenariuszy: `position:fixed` — lista nie przycinana przez kontener
- Motyw jasny: CSS vars do `:root`, `color-scheme` — tło formularzy poprawne
- Układ ctrl-row: dwuwierszowy grid — pola liczbowe zawsze widoczne
- `overflow-x:clip` na kolumnie sterowania

---

## [v1.1.0] — 2026-05-28

### Dodano
- Model R_tc z geometrii przewodów (długość, średnica, rezystywności IEC 60584)
- Selector przyrządu z historycznym kontekstem (galwanometr 1875 → przetwornik 10 MΩ)
- Teoria eksperta: ADC, budżet błędów RSS, historia przyrządów
- Autor i bibliografia (7 pozycji)

---

## [v1.0.0] — 2026-05-28

### Dodano
- Symulator toru pomiarowego termopary (6 typów, NIST ITS-90)
- Tryb Podstawowy i Eksperta, schemat blokowy, CJC, ADC, sygnalizacja świetlna
