# 9. Web, PWA i urządzenia współdzielone [P]

<!-- Generowana referencja; edytuj utrzymywany samodzielny przewodnik. -->

Sekcje źródłowe: 9.

## 9. Web, PWA i urządzenia współdzielone [P]

[P] Bezpieczeństwo aplikacji webowych i Progressive Web Apps na komputerach szkolnych:

- **Urządzenia współdzielone w pracowni:** Szkolne pracownie komputerowe i tablety są urządzeniami współdzielonymi przez wielu uczniów. Aplikacja MUSI oferować widoczne i łatwe w użyciu wylogowanie, które natychmiast czyści pamięć podręczną przeglądarki, `localStorage`, `sessionStorage` oraz bazy `IndexedDB` z danych osobowych i identyfikatorów sesji.
- **Content Security Policy (CSP):** Wdrożenie restrykcyjnej polityki CSP blokującej ładowanie skryptów z nieznanych domen oraz inline scripts bez odpowiednich haszy lub nonce.
- **Brak telemetrii podmiotów trzecich:** Całkowity zakaz instalacji zewnętrznych skryptów analitycznych (Google Analytics, Meta Pixel) śledzących zachowanie uczniów w aplikacjach edukacyjnych.

© 2026 Luděk Sušický. [MIT](https://opensource.org/license/mit). Wydanie zrewidowane wersji 1.2, oparte na pierwotnym przewodniku z października 2026 r. Zachowaj informacje o autorze, licencję i oznaczenia zmian.
