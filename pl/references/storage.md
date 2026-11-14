# 8. CSV i SQLite [P]

<!-- Generowana referencja; edytuj utrzymywany samodzielny przewodnik. -->

Sekcje źródłowe: 8.

## 8. CSV i SQLite [P]

[P] Zasady bezpiecznej obsługi plików lokalnych i baz wbudowanych:

- **Iniekcja formuł w CSV (CSV Injection / Formula Injection):** Przy eksporcie danych uczniów do plików CSV każde pole tekstowe zaczynające się od znaków `=`, `+`, `-`, `@`, tabulacji lub powrotu karetki MUSI zostać poprzedzone pojedynczym apostrofem (`'`) lub oczyszczone, aby zapobiec wykonaniu złośliwego kodu w arkuszu kalkulacyjnym (Excel, Calc).
- **SQLite w aplikacjach szkolnych:** Stosuj tryb WAL (Write-Ahead Logging). Włącz sprawdzanie kluczy obcych (`PRAGMA foreign_keys = ON;`). Unikaj zapisu bazy SQLite w katalogach dostępnych publicznie przez serwer webowy.
- **Parametryzacja zapytań:** Bezwzględny nakaz stosowania zapytań parametryzowanych (Prepared Statements) w celu eliminacji podatności SQL Injection.

© 2026 Luděk Sušický. [MIT](https://opensource.org/license/mit). Wydanie zrewidowane wersji 1.2, oparte na pierwotnym przewodniku z października 2026 r. Zachowaj informacje o autorze, licencję i oznaczenia zmian.
