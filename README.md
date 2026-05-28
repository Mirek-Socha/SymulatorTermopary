# Termopary — Interaktywna Aplikacja Dydaktyczna

Zestaw narzędzi do wirtualnego nauczania kontaktowego pomiaru temperatury termoelementem. Dwie zakładki w jednym pliku HTML, zero zależności lokalnych — działa po otwarciu `index.html` w przeglądarce.

**Autor:** Mirosław Socha  
**Jednostka:** Katedra Metrologii i Elektroniki, WEAIiIB, AGH Akademia Górniczo-Hutnicza, Kraków  
**Wersja:** v1.2.0

---

## Uruchomienie

```
Pobierz repozytorium → otwórz index.html w przeglądarce
```

Nie wymaga serwera HTTP, instalacji ani połączenia z internetem (poza fontami Google).

---

## Zakładka 1 — Symulator pomiaru (`SymulatorTermopary.html`)

Symulacja toru pomiarowego termopary zgodnie z NIST ITS-90.

### Tryb Podstawowy
- Wybór 6 typów termopar: **K, J, T, E, N, S**
- Suwaki T_gorące i T_zimne z zakresami wg normy IEC 60584-1
- Odczyt SEM [mV], T_mierzona [°C], błąd [°C]
- Sygnalizacja świetlna jakości pomiaru (zielona / żółta / czerwona)
- Presety scenariuszy (piec lab., kriogenika, temperatura ciała…)

### Tryb Eksperta
- Schemat blokowy toru pomiarowego z 5 blokami i animowanymi strzałkami
- Kompensacja złącza zimnego (CJC): regulowany błąd δT_cjc
- Model przetwornika A/C: rozdzielczość 10–24 bit, zakres 10–100 mV
- Obliczanie R_tc z geometrii przewodów (długość, średnica, rezystywność materiałów)
- Selector przyrządu pomiarowego z tłem historycznym:  
  galwanometr Siemens 1875 (50 Ω) → nowoczesny przetwornik (10 MΩ)
- Budżet błędów metodą RSS (δT_cjc, δT_ADC, δT_Rtc)
- Panel teorii z formułami KaTeX i bibliografią (7 pozycji)

### Wykres E(T)
- Charakterystyka termoelektryczna aktywnego typu — pełna krzywa
- **Tło porównawcze**: pozostałe typy jako półprzezroczyste krzywe z etykietami
- **Górne etykiety** `↑K`, `↑E`…: pojawia się gdy dany typ ma wyższą czułość α niż wybrany w aktualnym T_h
- **Przeciąganie** punktów T_h i T_z bezpośrednio na wykresie (kursor `grab`)
- Wykres czułości Seebecka α(T) = dE/dT [µV/°C] (tryb Eksperta)

---

## Zakładka 2 — Efekt Seebecka (`SeebeckVizualizacja.html`)

Fizyczna wizualizacja źródła napięcia termoelektrycznego.

### Schemat obwodu
- Topologia: spoina gorąca po lewej (T₁/T₂), woltomierz po prawej
- Segmentowy gradient temperatury wzdłuż obu elektrod
- **Gęstość elektronów** proporcjonalna do lokalnej koncentracji (α > 0: zagęszczenie przy zimnemu końcu, α < 0: odwrotnie) — brak animacji cyrkulacji prądu (obwód rozwarty)

### Źródło zewnętrzne (świeczka/lód)
- 7 trybów: brak / 🔥❄️ na elektrodzie A / B / obu
- Gaussowski pik lub dołek temperatury w dowolnym miejscu
- Kliknij lub przeciągnij źródło bezpośrednio po schemacie

### Wykresy
- **T(x)**: rozkład temperatury wzdłuż obu elektrod z N segmentami
- **dV = α·ΔT na segment**: wykres słupkowy — widoczne kasowanie +/− przy niemonotonnym T(x)
- **V(x)**: skumulowany potencjał wzdłuż obwodu

### Prawo temperatur pośrednich
Pasek wyników potwierdza w czasie rzeczywistym: SEM bez źródła = SEM ze źródłem → teleskopowanie sumy segmentów.

Panel teorii (przycisk **📖 Teoria**) zawiera wyprowadzenie wzorów, opis dyfuzji elektronów, wyjaśnienie efektu świeczki.

---

## Interfejs

| Funkcja | Opis |
|---|---|
| Zakładki | Przełączanie między Symulatorem a Seebeckiem |
| ☀️ / 🌙 Motyw | Globalny przełącznik jasny/ciemny — działa w obu zakładkach jednocześnie |
| 📖 Teoria | Sliding overlay z formułami i bibliografią |
| Drag na wykresie | Przeciąganie punktów T_h, T_z na charakterystyce E(T) |

---

## Struktura plików

```
index.html                  ← punkt wejścia (otwórz ten)
SymulatorTermopary.html     ← zakładka 1: symulator toru pomiarowego
SeebeckVizualizacja.html    ← zakładka 2: fizyka efektu Seebecka
CHANGELOG.md                ← historia wersji
```

`index.html` osadza obie aplikacje przez atrybut `srcdoc` — działa lokalnie bez serwera HTTP.

---

## Podstawa fizyczna

- Tablice termoelektryczne: **NIST ITS-90** (NIST Monograph 175)
- Norma typów: **IEC 60584-1:2013**
- Budżet niepewności: **GUM (JCGM 100:2008)**
- Model rezystancji: rezystywności materiałów wg IEC 60584 i danych literaturowych

---

## Licencja

Do użytku dydaktycznego — AGH Kraków.
