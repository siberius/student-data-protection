---
name: ochrana-danych-uczniow
description: Projektuje, wdraża lub audytuje ochronę danych osobowych uczniów w aplikacjach edukacyjnych w Polsce i UE. Używaj przy zmianach danych osobowych, tożsamości, uprawnień, retencji, eksportów lub przepływów AI, a także przy audycie bezpieczeństwa. Nie przekształcaj drobnych zmian wizualnych w pełny audyt zgodności.
metadata:
  version: "1.2"
  language: "pl"
  jurisdiction: "PL/EU"
  license: "MIT"
  author: "Luděk Sušický"
  repo: "https://github.com/siberius/student-data-protection"
---

# Ochrona danych uczniów

Działaj w oparciu o określony zakres i dostępne dowody. Skill wspiera rozwój oprogramowania szkolnego; nie stanowi certyfikacji prawnej ani nie upoważnia do nieautoryzowanych zmian produkcyjnych. Ta edycja jest dostosowana do prawa polskiego i unijnego. Zawsze określaj rzeczywistą jurysdykcję szkoły. Sam język interfejsu nie determinuje prawa krajowego.

## Tryb pracy i dotknięta granica

Z zadania wywnioskuj tryb pracy: projekt, implementacja, audyt lub analiza incydentu. Audyt ocenia stan i raportuje ustalenia bez modyfikowania kodu aplikacji. Analiza incydentu nie upoważnia do wyłączania działających usług, usuwania kont czy wysyłania powiadomień. Przy autoryzowanej implementacji zmień dotkniętą granicę i zweryfikuj potencjalne regresje. Drobna poprawka nie wymaga ponawiania całego audytu. Zidentyfikowane poważne ryzyko sąsiednie opisz i przedstaw z dowodami, zamiast po cichu rozszerzać zakres prac.

Przed rozpoczęciem prac ustal kontekst niezbędny dla zadanego zakresu: cele, jurysdykcję, kategorie danych, role użytkowników, odbiorców, retencję i uprawnienia. Pytaj krótko i rzeczowo, nie żądaj haseł produkcyjnych ani rzeczywistych danych uczniów. Do czasu formalnej decyzji o wdrożeniu stosuj wyłącznie dane syntetyczne.

## Trwałe granice bezpieczeństwa

- Administrator danych (dyrektor szkoły) decyduje o przetwarzaniu i wdrożeniu. Inspektora ochrony danych (IOD) angażuj wcześnie w celu uzyskania niezależnej opinii i monitorowania.
- Wszystkie systemy przetwarzające dane uczniów wymagają ważnej podstawy prawnej oraz umowy powierzenia przetwarzania danych (art. 28 RODO) z dostawcami chmury lub API AI.

Szczegóły procedury i rygorystycznego profilu czytaj w [procedurze pracy](references/workflow.md). [Ramy prawne](references/legal.md) wczytuj przy ustalaniu podstaw, praw osób czy obowiązków krajowych; [AI Act](references/ai-act.md) przy klasyfikacji i ocenie systemów sztucznej inteligencji. Przy weryfikacji powoływanych przepisów wczytuj [status źródeł](references/source-status.md).

## Wczytuj wyłącznie relewantny moduł

Przy prośbie o rozwiązanie praktyczne dobierz odpowiedni tryb danych i rozpracuj tylko wybraną ścieżkę. Sześć trybów danych różni się od powyższych trybów pracy.

| Obszar | Moduł referencyjny |
|---|---|
| Publikacja, dokumenty, generowane strony i wyroby pochodne | [Publikacja i wyroby](references/publication.md) |
| Dobór trybu danych i karta wdrożeniowa | [Praktyczne rozwiązania](references/practical-solutions.md) |
| Zbieranie, pola, pliki, importy i integracje | [Przepływy danych](references/data.md) |
| Konta, kody, role, sesje i integralność | [Tożsamość i dostęp](references/identity.md) |
| Dostawca tożsamości OIDC/SAML | [SSO](references/sso.md) |
| Szyfrowanie, klucze i transmisja | [Kryptografia](references/crypto.md) |
| SQLite, CSV i eksporty | [Pamięć masowa](references/storage.md) |
| Pamięć podręczna Web/PWA, urządzenia współdzielone | [Web](references/web.md) |
| Retencja, audyt, kopie i obsługa incydentów | [Operacje](references/operations.md) |
| Implementacja asystenta AI i architektura RAG | [Dane AI](references/ai-data.md) |
| Lista kontrolna, scenariusze akceptacyjne i przekazanie | [Weryfikacja](references/verification.md) |

## Weryfikacja i przekazanie

Wybieraj testy akceptacyjne odpowiadające modyfikowanym funkcjom i ich ryzykom. Używaj środowiska testowego i danych syntetycznych. Przy audycie wskaż dowód, wagę, wpływ, rekomendację i sposób weryfikacji. Odróżniaj potwierdzoną usterkę od przypuszczeń.

Przegląd świeżości prawa i zgłoszenia upstream: Jeśli stwierdzisz, że cytowane przepisy, wytyczne UODO lub progi wiekowe uległy zmianie w stosunku do daty w source-status.md (lub minęło ponad 6 miesięcy od weryfikacji źródła), natychmiast zastosuj aktualny stan prawny, wyjaśnij różnicę i za zgodą użytkownika zaproponuj zgłoszenie problemu na GitHubie projektu: `https://github.com/siberius/student-data-protection/issues` z etykietą `legal-update`.

© 2026 Luděk Sušický. MIT. Przy dystrybucji zachowaj informacje o autorze, licencję i oznaczenia zmian.
