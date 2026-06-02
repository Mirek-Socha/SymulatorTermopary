# Termopary — Interaktywna Aplikacja Dydaktyczna

Zestaw narzędzi do nauczania kontaktowego pomiaru temperatury termoelementem. Dwa narzędzia w jednym pliku HTML, zero zależności lokalnych.

**Autor:** Mirosław Socha  
**Jednostka:** Katedra Metrologii i Elektroniki, WEAIiIB, AGH Akademia Górniczo-Hutnicza, Kraków  
**Wersja:** v1.3.0

---

## Uruchomienie

```
Pobierz repozytorium → otwórz index.html w przeglądarce
```

Nie wymaga serwera HTTP, instalacji ani połączenia z internetem (poza fontami Google).

---

## Zakładka 1 — Symulator pomiaru (`SymulatorTermopary.html`)

### Tryb Podstawowy
- 6 typów termopar (K, J, T, E, N, S) z tablicami NIST ITS-90
- SEM [mV], T_mierzona [°C], błąd [°C], sygnalizacja świetlna
- Presety scenariuszy (piec, kriogenika, temperatura ciała…)

### Tryb Eksperta
- Schemat blokowy 5-blokowy z animowanymi strzałkami
- CJC z regulowanym błędem δT_cjc
- Model ADC 10–24 bit, obliczanie R_tc z geometrii przewodów
- Selector przyrządu z historią: galwanometr Siemensa 1875 (50 Ω) → nowoczesny przetwornik (10 MΩ)
- Budżet błędów RSS + teoria z formułami KaTeX i bibliografią

### Wykres E(T)
- Aktywny typ — pełna krzywa z punktem pracy
- Tło: pozostałe typy jako półprzezroczyste krzywe z etykietami
- Górne etykiety `↑K`, `↑E`… gdy dany typ ma wyższą czułość α w T_h
- **Drag** punktów T_h i T_z bezpośrednio na wykresie (kursor grab/grabbing + touch)

---

## Zakładka 2 — Efekt Seebecka (`SeebeckVizualizacja.html`)

Fizyczna wizualizacja źródła napięcia termoelektrycznego.

### Schemat obwodu
- Topologia: woltomierz po lewej (T₀), spoina gorąca po prawej (Tₓ) — spójna z wykresami
- Segmentowy gradient temperatury wzdłuż obu elektrod
- **Gęstość elektronów** z modelem fizycznym:
  - α > 0 (Chromel): zagęszczenie przy T₀ — zimnym końcu (woltomierz, lewa)
  - α < 0 (Alumel): zagęszczenie przy Tₓ — gorącym końcu (spoina, prawa)
  - **Zmiana znaku α widoczna bez żadnych ustawień** — student widzi różnicę natychmiast
  - Gradient radialny (białe jądro → kolor metalu → przezroczysty); pulsacja przy źródle

### Zewnętrzne źródło (świeczka / lód)
- 7 trybów: brak / 🔥❄️ na elektrodzie A / B / obu
- Gaussowski pik/dołek temperatury z regulowaną pozycją i amplitudą
- Kliknij lub **przeciągnij źródło** po schemacie (mouse + touch)

### Wykresy
- **T(x)**: rozkład temperatury wzdłuż elektrod z segmentami
- **dV = α·ΔT na segment**: słupki symetryczne (+ w górę, − w dół) — widoczne kasowanie +/− przy niemonotonnym T(x); clip uniemożliwia wychodzenie poza obszar
- **V(x)**: skumulowany potencjał wzdłuż obwodu, konwergencja przy spoinie

### Prawo temperatur pośrednich (Kelvin, 1854)
SEM ze źródłem = SEM bez źródła — suma teleskopuje się do α·(Tₓ−T₀) niezależnie od kształtu T(x). Pasek wyników potwierdza to w czasie rzeczywistym.

---

## Interfejs

| Funkcja | Opis |
|---|---|
| Zakładki | Przełączanie Symulator ↔ Seebeck |
| ☀️/🌙 Motyw | Globalny przełącznik jasny/ciemny — oba narzędzia jednocześnie |
| 📖 Teoria | Sliding overlay z formułami (KaTeX) i bibliografią |
| Drag na wykresie | Przeciąganie T_h, T_z na E(T); przeciąganie źródła ciepła/zimna |

---

## Struktura plików

```
index.html                  ← punkt wejścia
SymulatorTermopary.html     ← zakładka 1
SeebeckVizualizacja.html    ← zakładka 2
CHANGELOG.md
```

`index.html` osadza obie aplikacje przez `srcdoc` — działa bez serwera HTTP.

---

## Podstawa fizyczna

| Źródło | Zastosowanie |
|---|---|
| NIST Monograph 175 (ITS-90) | Tablice E(T) dla wszystkich typów |
| IEC 60584-1:2013 | Definicje typów K/J/T/E/N/S |
| GUM JCGM 100:2008 | Budżet niepewności RSS |
| Kelvin (1854) | Prawo temperatur pośrednich |
| Seebeck (1821) | Efekt termoelektryczny |

---

## Licencja

Do użytku dydaktycznego — AGH Kraków.
