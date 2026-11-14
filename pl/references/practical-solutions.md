# 17. Przewodnik po rozwiązaniach praktycznych

<!-- Generowana referencja; edytuj utrzymywany samodzielny przewodnik. -->

Sekcje źródłowe: 17.

## 17. Przewodnik po rozwiązaniach praktycznych

### 17.1 Tryby operacyjne (M1 - M6)

Podczas pracy z aplikacją szkolną asystent rozpoznaje i wspiera następujące tryby wdrożeniowe:

- **Tryb M1 (Aplikacja w pełni lokalna / Offline):** Działa na komputerze nauczyciela lub w sieci lokalnej bez połączenia z chmurą. Baza danych SQLite, pliki CSV.
- **Tryb M2 (Chmura szkolna / Własny serwer EOG):** Aplikacja webowa hostowana na szkolnym serwerze VPS w europejskim centrum danych.
- **Tryb M3 (Komercyjna platforma edukacyjna z umową DPA):** Integracja z oficjalnymi platformami szkolnymi na podstawie art. 28 RODO.
- **Tryb M4 (Audyt bezpieczeństwa i kodu):** Ocena istniejącego rozwiązania pod kątem podatności i zgodności z profilem bezpieczeństwa.
- **Tryb M5 (Lokalny asystent AI - L0):** Uruchomienie lokalnego modelu edukacyjnego w szkolnej pracowni bez transferu danych na zewnątrz.
- **Tryb M6 (Hybrydowy system AI z k-anonimowością):** Przetwarzanie w chmurze C1 ze wstępną anonimizacją i walidacją k >= 5.

### 17.2 Architektura referencyjna aplikacji szkolnej

Rekomendowana architektura:

```text
[ Przeglądarka / PWA ucznia ]
             │
             │ HTTPS (TLS 1.3 + HSTS)
             ▼
[ Odwrócone proxy (Nginx / Caddy) ] ── (Blokada ataków, obsługa CSP, nagłówki bezpieczeństwa)
             │
             │ Izolowana sieć wewnętrzna
             ▼
[ Serwer aplikacji (Backend) ]
     ├── Moduł RBAC i walidacji sesji
     ├── Moduł sanitizacji i ochrony CSV
     └── Brama modeli AI (L0 / C1 / C2 z anonimizacją k >= 5)
             │
             │ Szyfrowane połączenie
             ▼
[ Baza danych (PostgreSQL / SQLite WAL) ] (Szyfrowanie w spoczynku AES-256)
```

### 17.5 Szablon karty wdrożeniowej rozwiązania

Dla każdego modułu edukacyjnego przygotuj kartę wdrożeniową według poniższego schematu:

1. **Nazwa modułu i cel dydaktyczny:** Krótki opis funkcjonalności.
2. **Kategorie przetwarzanych danych:** Wyszczególnienie danych zwykłych i technicznych.
3. **Podstawa prawna:** Wskazanie odpowiedniego artykułu RODO i Prawa oświatowego.
4. **Architektura przetwarzania:** Wybór poziomu (M1 - M6, L0 / C1 / C2).
5. **Środki techniczne:** Zastosowane szyfrowanie, zabezpieczenia sesji, retencja i testy k-anonimowości.

© 2026 Luděk Sušický. [MIT](https://opensource.org/license/mit). Wydanie zrewidowane wersji 1.2, oparte na pierwotnym przewodniku z października 2026 r. Zachowaj informacje o autorze, licencję i oznaczenia zmian.
