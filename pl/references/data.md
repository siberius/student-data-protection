# 4. Model danych, zbieranie i minimalizacja [P]

<!-- Generowana referencja; edytuj utrzymywany samodzielny przewodnik. -->

Sekcje źródłowe: 4.

## 4. Model danych, zbieranie i minimalizacja [P]

[P] Model danych aplikacji szkolnej MUSI realizować zasadę minimalizacji danych (art. 5 ust. 1 lit. c RODO):
- **Identyfikatory:** Stosuj sztuczne identyfikatory wewnętrzne (UUIDv4) jako klucze główne. Nigdy nie używaj numeru PESEL ani oficjalnego identyfikatora z SIO jako klucza w adresach URL, nazwach plików lub sesjach.
- **Pola opcjonalne:** Numer telefonu, adres zamieszkania, zdjęcie profilowe nie mogą być polami obowiązkowymi w aplikacjach wspierających naukę przedmiotową.
- **Dane wrażliwe (art. 9 RODO):** Aplikacje przedmiotowe, quizy i platformy ćwiczeniowe NIE MOGĄ przetwarzać danych o zdrowiu, pochodzeniu etnicznym, przekonaniach czy danych biometrycznych. Jeśli wsparcie ucznia wymaga dostosowania (np. dysleksja), przechowuj wyłącznie techniczny znacznik konfiguracyjny (np. `extra_time_ratio: 1.25`) bez ujawniania diagnozy medycznej.
- **Metadane:** Usuwaj metadane EXIF z przesyłanych przez uczniów zdjęć prac przed zapisaniem ich na serwerze.

© 2026 Luděk Sušický. [MIT](https://opensource.org/license/mit). Wydanie zrewidowane wersji 1.2, oparte na pierwotnym przewodniku z października 2026 r. Zachowaj informacje o autorze, licencję i oznaczenia zmian.
