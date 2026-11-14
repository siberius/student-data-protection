# 12. Lista kontrolna weryfikacji przed wdrożeniem

<!-- Generowana referencja; edytuj utrzymywany samodzielny przewodnik. -->

Sekcje źródłowe: 12, 13, 14.

## 12. Lista kontrolna weryfikacji przed wdrożeniem

Przed uruchomieniem aplikacji w środowisku szkolnym sprawdź:
1. Podstawa prawna i konsultacja z IOD szkoły udokumentowana.
2. Umowa powierzenia przetwarzania danych (art. 28 RODO) podpisana ze wszystkimi dostawcami chmury i AI.
3. Obowiązek informacyjny (art. 13-14 RODO) przygotowany w zrozumiałym języku.
4. Minimalizacja danych: brak zbędnych pól wrażliwych i usunięty PESEL jako identyfikator aplikacyjny.
5. Hasła haszowane Argon2id/bcrypt; sesje z flagami HttpOnly, Secure, SameSite.
6. Kontrola uprawnień RBAC odporna na IDOR w każdym punkcie końcowym.
7. Szyfrowanie TLS 1.3 i AES-256 dla danych w spoczynku.
8. Eksport CSV zabezpieczony przed iniekcją formuł.
9. Wylogowanie czyści magazyny przeglądarki na urządzeniach współdzielonych.
10. Całkowity brak zewnętrznych trackerów marketingowych i telemetrii.

## 13. Scenariusze akceptacyjne (Acceptance tests)

Poniższa tabela zawiera zestaw 38 scenariuszy testowych weryfikujących spełnienie wymagań prawnych i technicznych:

| Identyfikator | Obszar | Scenariusz testowy | Oczekiwany wynik |
|---|---|---|---|
| AT01 | Podstawa prawna | Przetwarzanie danych ucznia w ewidencji obowiązkowej | Wskazany art. 6 ust. 1 lit. c RODO i Prawo oświatowe |
| AT02 | Zgoda | Udział w obowiązkowej lekcji informatyki | Brak żądania zgody rodzica jako warunku wstępnego |
| AT03 | Dane wrażliwe | Rejestracja ucznia w aplikacji do matematyki | Formularz nie zawiera pól dotyczących zdrowia ani wyznania |
| AT04 | Klucze główne | Wyświetlanie profilu ucznia w adresie URL | Adres zawiera sztuczny UUID, brak numeru PESEL |
| AT05 | Metadane | Wgrywanie zdjęcia odręcznego zadania domowego | Plik zapisany na serwerze nie zawiera metadanych EXIF |
| AT06 | Hasła | Rejestracja hasła "123456" lub słownikowego | System odrzuca słabe hasło i wymusza złożoność |
| AT07 | Haszowanie | Inspekcja bazy danych użytkowników | Hasła haszowane algorytmem Argon2id lub bcrypt |
| AT08 | Sesja | Analiza nagłówków Set-Cookie | Obecne flagi HttpOnly, Secure, SameSite=Lax/Strict |
| AT09 | Bezczynność | Brak aktywności ucznia przez 35 minut | Sesja wygaszona, wymagane ponowne logowanie |
| AT10 | IDOR | Uczeń A zmienia parametr ID w żądaniu na ID ucznia B | Serwer zwraca kod błędu 403 Forbidden |
| AT11 | Uprawnienia ról | Uczeń próbuje wywołać API edycji ocen | Serwer odrzuca żądanie z kodem 403 Forbidden |
| AT12 | Izolacja rodzica | Rodzic próbuje pobrać raport innego dziecka | Dostęp zablokowany, widoczne wyłącznie własne dzieci |
| AT13 | Szyfrowanie tranzytu | Próba połączenia przez nieszyfrowany protokół HTTP | Automatyczne przekierowanie 301/308 na HTTPS (TLS 1.3) |
| AT14 | HSTS | Weryfikacja nagłówków odpowiedzi HTTP | Obecny nagłówek Strict-Transport-Security |
| AT15 | Iniekcja CSV | Uczeń wpisuje w nazwisku `=1+2';cmd|' ...` | Eksportowany plik CSV poprzedza komórkę apostrofem |
| AT16 | SQLite Injection | Wprowadzenie `' OR 1=1 --` w wyszukiwarce | Zapytanie parametryzowane, brak błędu i wycieku danych |
| AT17 | SQLite lokalizacja | Próba pobrania pliku `.sqlite` przez przeglądarkę | Serwer zwraca kod 404 lub 403, plik poza publicznym rootem |
| AT18 | Współdzielone PC | Kliknięcie "Wyloguj" w pracowni szkolnej | Dane z localStorage i sesja całkowicie wyczyszczone |
| AT19 | CSP | Próba wstrzyknięcia skryptu z zewnętrznej domeny | Polityka CSP blokuje wykonanie nieautoryzowanego skryptu |
| AT20 | Telemetria | Analiza ruchu sieciowego podczas nauki | Brak zapytań do Google Analytics, Meta lub brokerów |
| AT21 | Logi bez PII | Analiza pliku dziennika zdarzeń serwera | Brak haseł w tekście jawnym i wrażliwych danych uczniów |
| AT22 | Rejestr incydentów | Symulacja wycieku danych testowych | Zdarzenie odnotowane, przygotowany szablon zgłoszenia UODO |
| AT23 | AI Emotion | Próba wdrożenia analizy mimiki twarzy kamerą AI | System odrzucony jako praktyka zakazana (art. 5 AI Act) |
| AT24 | AI High-Risk | Wdrożenie AI do końcowej oceny egzaminu | Kwalifikacja jako High-Risk, wymagana dokumentacja i nadzór |
| AT25 | AI Nadzór ludzki | System AI proponuje ocenę niedostateczną | Nauczyciel ma możliwość weryfikacji i zmiany oceny |
| AT26 | AI Umowa DPA | Integracja zewnętrznego komercyjnego API LLM | Podpisana umowa powierzenia przetwarzania przed wdrożeniem |
| AT27 | AI Trening | Weryfikacja regulaminu dostawcy zewnętrznego AI | Zapewnienie, że dane uczniów nie trenują modeli publicznych |
| AT28 | SSO Federacja | Logowanie przez szkolny węzeł SAML / OIDC | Brak przekazywania haseł do aplikacji zewnętrznej |
| AT29 | Retencja kont | Uczeń opuszcza szkołę (zakończenie edukacji) | Konto dezaktywowane, dane przeznaczone do archiwizacji |
| AT30 | Prawa osób | Żądanie dostępu do danych z art. 15 RODO | Wygenerowanie kompletnego eksportu danych ucznia |
| AT31 | Klucze API | Analiza repozytorium kodu źródłowego aplikacji | Brak zahardkodowanych kluczy i haseł w kodzie |
| AT32 | Backup szyfrowany | Weryfikacja integralności kopii zapasowej | Plik kopii zaszyfrowany, odzyskiwanie zweryfikowane pomyślnie |
| AT33 | Słabe haszowanie | Zastosowanie algorytmu MD5 lub SHA1 do haseł | Natychmiastowe odrzucenie i zastąpienie przez Argon2id |
| AT34 | Kopia poza EOG | Konfiguracja serwera zapasowego w chmurze USA | Blokada konfiguracji przy braku odpowiednich zabezpieczeń |
| AT35 | Informacja o AI | Uczeń korzysta z bota wspomagającego naukę | Uczeń poinformowany, że wchodzi w interakcję ze sztuczną inteligencją |
| AT36 | Dostęp nauczyciela | Nauczyciel biologii próbuje przeglądać oceny z historii | Dostęp ograniczony zgodnie z polityką uprawnień szkoły |
| AT37 | AI Brama L0/C1/C2 | Uczeń wysyła prompt z nazwiskiem i numerem klasy | Brama L0/C1 blokuje wysyłkę lub anonimizuje zapytanie |
| AT38 | k-anonimowość AI | Generowanie statystyk postępów z k=3 | Skrypt walidacyjny odrzuca zbiór, wymagając progu k >= 5 |

## 14. Forma przekazania i granice twierdzeń

Podczas przekazywania wyników audytu lub dokumentacji technicznej:
- Prezentuj ustalenia w sposób rzeczowy, precyzyjny i konstruktywny.
- Wyraźnie rozróżniaj fakty zaobserwowane w kodzie od założeń i rekomendacji.
- Nigdy nie używaj zwrotów gwarantujących "100% zgodność z prawem" ani "certyfikację RODO", gdyż zgodność jest procesem ciągłym zależnym od wdrożenia i organizacji.

© 2026 Luděk Sušický. [MIT](https://opensource.org/license/mit). Wydanie zrewidowane wersji 1.2, oparte na pierwotnym przewodniku z października 2026 r. Zachowaj informacje o autorze, licencję i oznaczenia zmian.
