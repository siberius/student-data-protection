# 16. Szkolne logowanie federacyjne i SSO [P]

<!-- Generowana referencja; edytuj utrzymywany samodzielny przewodnik. -->

Sekcje źródłowe: 16.

## 16. Szkolne logowanie federacyjne i SSO [P]

[P] Integracja ze szkolnymi systemami tożsamości:
- **Protokoły standardowe:** Stosuj OpenID Connect (OIDC) lub SAML 2.0.
- **Minimalizacja atrybutów:** W żądaniach uwierzytelniających pobieraj wyłącznie niezbędne atrybuty (np. wewnętrzny identyfikator `sub` oraz rola w szkole `eduPersonAffiliation`). Nie pobieraj pełnych profili użytkowników ani list kontaktów.
- **Ochrona tokenów:** Tokeny dostępu i tokeny odświeżające (Refresh Tokens) muszą być przechowywane w bezpieczny sposób (np. szyfrowana baza lub pamięć serwera), a nie w otwartym magazynie przeglądarki.

© 2026 Luděk Sušický. [MIT](https://opensource.org/license/mit). Wydanie zrewidowane wersji 1.2, oparte na pierwotnym przewodniku z października 2026 r. Zachowaj informacje o autorze, licencję i oznaczenia zmian.
