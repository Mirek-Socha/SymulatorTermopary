# Changelog — Symulator Termopary

## [v1.1.0] — 2026-05-28

### Dodano
- Model fizyczny R_tc obliczany z długości i średnicy przewodów (rezystywności materiałów wg IEC 60584)
- Selector przyrządu pomiarowego R_in z tłem historycznym (galwanometr 1875 → nowoczesny przetwornik)
- Presety historyczne: Galwanometr Siemens 1875, Galwanometr precyzyjny 1900, Miliwooltomierz 1920, DVM 1975
- Teoria eksperta: opis ADC w torze termoparowym, przykłady liczbowe, budżet błędów RSS
- Sekcja autora i bibliografia (7 pozycji: NIST-175, IEC 60584-1, GUM, Childs, Michalski, Seebeck, Tumański)

### Poprawiono
- Dropdown scenariuszy: `position:fixed` z `getBoundingClientRect` — lista nie jest przycinana przez kontener
- Motyw jasny: zmienne CSS przeniesione do `:root`, dodano `color-scheme` — tło formularzy poprawne
- Układ ctrl-row: dwuwierszowy grid (etykieta+wartość / suwak na pełną szerokość) — pola liczbowe zawsze widoczne
- Wykresy: `canvas` z `flex:1` wypełnia całą kartę zamiast stałej wysokości
- `overflow-x:clip` na kolumnie sterowania — brak przycinania elementów poziomych

### Zmieniono
- Parametry R_in i R_L zastąpione przez: długość [m], średnica [mm], selector przyrządu

---

## [v1.0.0] — 2026-05-28

### Dodano
- Pierwszy release: symulator kontaktowego pomiaru temperatury termoparą
- 6 typów termopar (K, J, T, E, N, S) z tablicami NIST ITS-90
- Tryb Podstawowy i Tryb Eksperta
- Schemat blokowy toru pomiarowego (5 bloków z animowanymi strzałkami)
- Kompensacja złącza zimnego (CJC) z regulowanym błędem δT_cjc
- Model przetwornika A/C: rozdzielczość 10–24 bit, zakres 10–100 mV
- Wykresy: charakterystyka E(T) i czułość Seebecka α(T)
- Panel teorii z formułami KaTeX (tryby Podstawowy i Ekspert)
- Sygnalizacja świetlna jakości pomiaru
- Presety scenariuszy
- Obsługa jasnego i ciemnego motywu
