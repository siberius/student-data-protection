# 7. Szyfrowanie i zarządzanie kluczami [P]

<!-- Generowana referencja; edytuj utrzymywany samodzielny przewodnik. -->

Sekcje źródłowe: 7.

## 7. Szyfrowanie i zarządzanie kluczami [P]

[P] Standardy kryptograficzne:

- **Dane w spoczynku (Data at Rest):** Szyfrowanie baz danych i dysków serwerowych algorytmem AES-256-GCM lub ChaCha20-Poly1305. Wrażliwe kolumny szyfrowane na poziomie aplikacji, jeśli baza jest współdzielona.
- **Dane w transmisji (Data in Transit):** Wymuszony protokół TLS 1.3 (minimalnie TLS 1.2 z bezpiecznymi zestawami szyfrów). Nagłówek HSTS (HTTP Strict Transport Security) z czasem co najmniej 1 rok (`max-age=31536000; includeSubDomains`).
- **Zarządzanie kluczami:** Klucze kryptograficzne NIE MOGĄ znajdować się w repozytorium kodu. Pobieraj klucze ze zmiennych środowiskowych lub bezpiecznego magazynu sekretów (KMS/Vault).

© 2026 Luděk Sušický. [MIT](https://opensource.org/license/mit). Wydanie zrewidowane wersji 1.2, oparte na pierwotnym przewodniku z października 2026 r. Zachowaj informacje o autorze, licencję i oznaczenia zmian.
