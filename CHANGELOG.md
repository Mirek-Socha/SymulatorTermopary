# Changelog — Termopary (AGH Metrologia)

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
