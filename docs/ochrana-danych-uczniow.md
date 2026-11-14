# Ochrona danych osobowych uczniów w aplikacjach szkolnych

> Niniejszy dokument stanowi praktyczny profil bezpieczeństwa dla aplikacji szkolnych. Nie jest poradą prawną ani certyfikatem zgodności. Przed przetwarzaniem rzeczywistych danych administrator podejmuje decyzję o wdrożeniu po przeprowadzeniu odpowiedniej oceny i terminowej konsultacji z inspektorem ochrony danych (IOD / DPO).

**Wersja:** 1.2 · **Język i jurysdykcja:** polski, Polska / UE · **Pierwotna weryfikacja źródeł:** 22 października 2026 · **Wydanie:** 14 listopada 2026. Zabezpieczenia dla modeli AI, k-anonimowość (k >= 5), l-różnorodność (l >= 2) i walidacja skryptowa uzupełnione 14 listopada 2026.

Używaj tego samodzielnego skilla podczas projektowania, implementacji lub audytu aplikacji, które zbierają, przechowują, wyświetlają, oceniają lub udostępniają dane osobowe uczniów, ich opiekunów prawnych lub pracowników szkoły. Obejmuje ewidencje, formularze, obecności, zadania domowe, portfolio, komunikację, zapisy na wydarzenia, ewaluację i narzędzia edukacyjne AI. Danymi mogą być imiona i nazwiska, kontakty, klasy, oceny, pliki, wiadomości, wyniki testów, logi operacyjne oraz identyfikatory sesji i urządzeń.

Podstawą jest ochrona w całym cyklu życia danych. Weryfikacje webowe i PWA stosuj tylko tam, gdzie występuje dana technologia; klient mobilny lub desktopowy wymaga również zabezpieczeń właściwych dla platformy. CSV i SQLite są wspieranymi rozwiązaniami projektowymi, a nie jedyną dopuszczalną architekturą. Nie dodawaj quizów, oceniania, modeli AI ani logowania kodami tylko dlatego, że opisuje je niniejszy skill.

Rozróżniaj **trwałe konto ze zweryfikowaną tożsamością**, **ograniczony udział doraźny** oraz **publiczną zbiórkę bez konta**. Imię, klasa, urządzenie czy znajomość wspólnego kodu nie dowodzą tożsamości. Stosuj uwierzytelnianie odpowiednio silne do wagi ewidencji i historii ucznia. Kod jednorazowy lub QR jest opcjonalnym modułem dla ograniczonych aktywności, a nie uniwersalnym dostępem do danych szkolnych.

## 1. Wykładnia wymagań i procedura asystenta

- **[Z] Wymóg prawny:** obowiązuje przy spełnieniu opisanych warunków. Cytowany przepis ma pierwszeństwo przed zaleceniem technicznym.
- **[P] Profil bezpieczeństwa:** konkretny wybór implementacyjny tego skilla. Określenia MUSI/NIE MOŻE w sekcjach technicznych definiują ten profil, a nie dosłowny nakaz RODO. Odstępstwo udokumentuj zagrożeniem, środkiem kompensacyjnym, testem i decyzją osoby odpowiedzialnej w szkole.
- **[D] Zalecenie:** właściwe rozszerzenie w zależności od ryzyka i specyfiki wdrożenia.
- **[O] Zweryfikować:** kwestia zależna od rzeczywistego użycia, aktualnego prawa lub niepotwierdzonej konfiguracji. Nie uznawaj jej za spełnioną bez dowodu.

1. Z zadania wywnioskuj tryb pracy: projekt, implementacja, audyt lub incydent. Audyt przekazuje ustalenia i rekomendacje bez modyfikowania aplikacji. Analiza incydentu nie upoważnia do wyłączania działających usług, usuwania kont czy wysyłania powiadomień. Działania wykonuj wyłącznie w granicach faktycznego upoważnienia.
2. Wykorzystaj znany kontekst i określ cel przetwarzania, przepływy danych, role i zmianę ryzyka. Pytaj tylko o brakujące informacje wpływające na decyzje. Przy drobnej naprawie oceniaj dotkniętą granicę i regresje; nie rozpoczynaj całego audytu na nowo. Poważny problem sąsiedni udokumentuj i zgłoś; nie rozszerzaj zakresu prac po cichu.
3. Zmapuj dane, odbiorców, tożsamość, uprawnienia, retencję i zagrożenia. Zachowaj bezpieczną architekturę i działające zabezpieczenia. Dopóki brakuje celu, podstawy prawnej lub decyzji wdrożeniowej, stosuj dane syntetyczne.
4. Przy projektowaniu zalecaj proporcjonalne zabezpieczenia. Przy autoryzowanej implementacji realizuj je ze wskazaniem miejsc w kodzie lub konfiguracji. Przy audycie podaj wagę, dowód, wpływ, rekomendację i niezbędną weryfikację. Odróżniaj podejrzenie od zaobserwowanej usterki.
5. Dobierz scenariusze akceptacyjne według funkcji i ryzyka. Rozróżniaj wynik pozytywny, negatywny, niewykonany i niedotyczy z podaniem przyczyny. Plan testów nie stanowi dowodu ich wykonania.
6. Przed rzeczywistym uruchomieniem zweryfikuj podstawę prawną, wymaganą ocenę i aktualne przepisy. Administrator decyduje o wdrożeniu po terminowej konsultacji z IOD i odpowiednim przeglądzie merytorycznym. Bez podstawy prawnej lub oceny nie rekomenduj przetwarzania; kontynuuj autoryzowane prace w środowisku testowym z danymi syntetycznymi.

### 1.4 Ciągła świeżość prawna i zgłaszanie aktualizacji w górę projektu [P]

Profil bezpieczeństwa tego skilla wymaga, aby każda analiza prawna i rekomendacja opierała się na aktualnym stanie prawnym (przepisy RODO, wytyczne EDPB, orzecznictwo TSUE oraz krajowe przepisy oświatowe i stanowiska organów nadzorczych).
1. **Reguła weryfikacji wieku źródeł (> 6 miesięcy):** Jeśli od daty ostatniej weryfikacji źródeł skilla upłynęło ponad 6 miesięcy, asystent musi sprawdzić aktualność powoływanych aktów prawnych i wytycznych.
2. **Natychmiastowe dostosowanie dla użytkownika:** W przypadku stwierdzenia rozbieżności lub nowelizacji prawa asystent natychmiast stosuje w bieżącej odpowiedzi aktualny stan prawny i informuje użytkownika o zmianie.
3. **Zgłoszenie aktualizacji (GitHub Issue):** Asystent pyta użytkownika o zgodę na utworzenie zgłoszenia w repozytorium projektu: `https://github.com/siberius/student-data-protection/issues` z etykietą `legal-update`, podając zidentyfikowaną nowelizację, dotknięte sekcje i proponowaną modyfikację.

## 2. RODO i polskie ramy prawne

### 2.1 Podstawy prawne w polskiej szkole

[Z] Każde przetwarzanie danych osobowych ucznia musi posiadać ważną podstawę prawną (art. 6 i art. 9 RODO). W polskich szkołach podstawowych i ponadpodstawowych podstawowymi przesłankami są:
- **Art. 6 ust. 1 lit. c RODO (obowiązek prawny):** Prowadzenie ewidencji uczniów, księgi uczniów, dziennika lekcyjnego, arkuszy ocen, dokumentacji przebiegu nauczania na podstawie Ustawy z dnia 14 grudnia 2016 r. - Prawo oświatowe oraz rozporządzeń wykonawczych MEN.
- **Art. 6 ust. 1 lit. e RODO (zadanie w interesie publicznym):** Realizacja statutowych celów dydaktycznych, opiekuńczych i wychowawczych.
- **Art. 6 ust. 1 lit. a RODO (zgoda):** Wyłącznie w działaniach fakultatywnych (publikacja wizerunku w mediach społecznościowych, dobrowolne wycieczki, nieobowiązkowe kółka zainteresowań). Zgoda nie może być warunkiem uczestnictwa w edukacji obowiązkowej.
- **Art. 9 ust. 2 lit. g lub b RODO (dane szczególnych kategorii):** Informacje o stanie zdrowia (orzeczenia o potrzebie kształcenia specjalnego, alergie, dieta) przetwarzane na podstawie przepisów oświatowych w celu zapewnienia bezpieczeństwa i wsparcia.

### 2.2 Podmioty i odpowiedzialność w polskim systemie oświaty

[Z] Administratorem danych osobowych (ADO) w szkole publicznej jest placówka reprezentowana przez dyrektora szkoły. Nauczyciel lub administrator IT działa z upoważnienia dyrektora.
- **Umowa powierzenia przetwarzania danych (art. 28 RODO):** Każde zewnętrzne narzędzie edukacyjne, platforma chmurowa, dostawca dziennika elektronicznego lub zewnętrzny model AI przetwarzający dane uczniów wymaga formalnej umowy powierzenia podpisanej przez dyrektora szkoły przed rozpoczęciem przetwarzania.
- **Inspektor Ochrony Danych (IOD):** Szkoła ma bezwzględny prawny obowiązek wyznaczenia IOD (art. 10 Ustawy o ochronie danych osobowych z dnia 10 maja 2018 r.). IOD musi być konsultowany przed wdrożeniem każdego nowego oprogramowania przetwarzającego dane uczniów.
- **Nadzór:** Organem nadzorczym w Polsce jest Prezes Urzędu Ochrony Danych Osobowych (UODO). Odwołania do orzecznictwa: Naczelny Sąd Administracyjny (NSA) w wyroku dotyczącym biometrii w szkołach (I OSK 3945/19) potwierdził bezwzględny zakaz pobierania danych biometrycznych uczniów (np. linii papilarnych) w celu weryfikacji uprawnień do obiadów.

### 2.3 Obowiązek informacyjny, prawa osób i transfer danych

[Z] Szkoła musi spełnić obowiązek informacyjny zgodnie z art. 13-14 RODO w formie przystępnej zarówno dla rodziców, jak i samych uczniów (motyw 58 RODO).
Prawa uczniów i rodziców obejmują:
- Prawo dostępu (art. 15 RODO) i sprostowania (art. 16 RODO).
- Prawo do usunięcia danych ("bycia zapomnianym", art. 17 RODO) nie przysługuje w odniesieniu do danych przetwarzanych na podstawie obowiązku prawnego (np. dokumentacja przebiegu nauczania musi być przechowywana zgodnie z instrukcją kancelaryjną i przepisami archiwalnymi).
- Prawo do sprzeciwu (art. 21 RODO) oraz prawo wniesienia skargi do Prezesa UODO.

[P] Profil bezpieczeństwa: Wszystkie bazy danych i kopie zapasowe aplikacji szkolnej MUSZĄ znajdować się na terenie Europejskiego Obszaru Gospodarczego (EOG). Przekazywanie danych poza EOG jest zakazane, chyba że istnieje decyzja Komisji Europejskiej o adekwatności lub podpisano standardowe klauzule umowne (SCC) wraz z udokumentowaną oceną TIA i szyfrowaniem end-to-end.

### 2.4 Porównawczy przegląd jurysdykcji krajowych i progów wiekowych [Z/P]

Przy projektowaniu aplikacji edukacyjnej lub integracji modeli AI zawsze weryfikuj właściwą jurysdykcję szkoły i grupy uczniów. Sam język interfejsu nie determinuje prawa krajowego. RODO w art. 8 umożliwia państwom członkowskim określenie wieku zgody cyfrowej w przedziale od 13 do 16 lat; przepisy oświatowe i stanowiska organów nadzorczych różnią się w poszczególnych krajach:

| Państwo / jurysdykcja | Wiek z art. 8 RODO | Organ nadzorczy | Przepisy oświatowe i ograniczenia chmury / AI |
|---|---|---|---|
| **Polska (PL)** | 16 lat (Ustawa o ODO 2018) | UODO | Prawo oświatowe; odpowiedzialność dyrektora jako ADO; wymóg umowy powierzenia z art. 28 RODO dla AI; zakaz biometrii uczniów (NSA). |
| **Czechy (CZ)** | 15 lat (ustawa nr 110/2019 Sb.) | ÚOOÚ | Ustawa o szkolnictwie nr 561/2004 Sb. (§ 28); pragmatyczne podejście do chmur edukacyjnych; wytyczne MŠMT i NPI (AIDIG). |
| **Hiszpania (ES)** | 14 lat (LOPDGDD art. 7) | AEPD + organy regionalne | LOE (DA 23); szczegółowe wytyczne AEPD dotyczące k-anonimowości i obowiązek DPO w szkołach (art. 34.1.b LOPDGDD). |
| **Niemcy (DE)** | 16 lat (BDSG § 16) | DSK + 16 organów krajów związkowych | 16 krajowych ustaw szkolnych; ścisłe ograniczenia i zakazy chmur komercyjnych USA (M365) i telemetrii; obowiązkowa DSFA (DPIA) dla AI. |
| **Francja (FR)** | 15 lat (Loi Informatique et Libertés) | CNIL | Code de l'éducation; państwowe platformy ENT; wytyczne ministerstwa przeciw darmowym chmurom USA; zakaz kont klasowych deanonimizujących w promptach. |
| **Ukraina (UA)** | 14-18 lat (częściowa zdolność wg KC) | Rzecznik Praw Obywatelskich (Ombudsman) | Ustawa nr 2297-VI i projekt ustawy nr 8153 harmonizowany z RODO; ekosystem Mrija; uczniowie w UE podlegają pełnemu RODO. |

#### Reguły implementacji transgranicznej i krajowej

1. **Wdrożenia w Polsce (Odpowiedzialność dyrektora i zakaz biometrii):** [Z] W polskich szkołach pełna odpowiedzialność prawna spoczywa na dyrektorze placówki (ADO). Nauczyciele nie mogą samodzielnie wdrażać narzędzi AI ani rejestrować uczniów bez formalnej umowy powierzenia przetwarzania danych (art. 28 RODO). Obowiązuje granica 16 lat oraz bezwzględny judykacyjny zakaz identyfikacji biometrycznej uczniów (np. w stołówkach czy bibliotekach).
2. **Wdrożenia w Niemczech (Ścisły prymat rozwiązań lokalnych):** [Z] W Niemczech obowiązuje granica 16 lat i decentralizacja w 16 landach. W świetle uchwał DSK dotyczących Microsoft 365 priorytetem jest przetwarzanie wyłącznie lokalne (L0) na serwerach szkolnych lub oprogramowaniu open-source (Moodle, IServ).
3. **Wdrożenia we Francji (Suwerenność i zakaz wspólnych kont promptowych):** [Z] Obowiązuje granica 15 lat i ministerialne wytyczne dotyczące środowisk ENT. Przy integracji AI stosuj wytyczne CNIL: zakazane są konta ogólne, w których zapytania uczniów zawierają dane pośrednie, a ocena ucznia nie może zależeć wyłącznie od modelu.
4. **Wdrożenia ukraińskie (Integracja w UE i standardy eurointegracyjne):** [Z] Dla uczniów ukraińskich w szkołach polskich, czeskich i innych w UE obowiązuje w pełni europejskie RODO i lokalne specustawy. Dla aplikacji tworzonych dla Ukrainy projektuj rozwiązania zgodne z projektem ustawy nr 8153 i ekosystemem Mrija ze ścisłą anonimizacją danych przed użyciem AI.

## 3. Akt o sztucznej inteligencji (AI Act): stosowalność, klasyfikacja i terminy

### 3.1 Zastosowanie do narzędzi edukacyjnych

[Z] Rozporządzenie Parlamentu Europejskiego i Rady (UE) 2024/1689 (AI Act) stosuje się do systemów AI wdrażanych lub używanych w Unii Europejskiej, w tym w instytucjach edukacyjnych. Systemem AI jest system oparty na maszynie, który działa z różnym poziomem autonomii i może po wdrożeniu wykazywać zdolność adaptacji, a który na podstawie otrzymanych danych wejściowych wnioskuje, w jaki sposób generować wyniki (np. predykcje, treść, zalecenia lub decyzje).

Tradycyjne algorytmy deterministyczne, regułowe kalkulatory punktów, statyczne formularze i bazy danych bez wnioskowania nie są systemami AI i nie podlegają obowiązkom AI Actu. Zwykłe zapytanie SQL nie staje się sztuczną inteligencją tylko z powodu złożoności filtrów.

### 3.2 Praktyki zakazane w edukacji (Art. 5)

[Z] AI Act bezwzględnie zakazuje w szkołach i placówkach oświatowych:
1. **Rozpoznawania emocji:** Używania systemów AI do wnioskowania o stanie emocjonalnym uczniów w klasie na podstawie obrazu z kamer lub analizy głosu (art. 5 ust. 1 lit. f). Zakaz ten nie dopuszcza wyjątków w szkolnictwie podstawowym i średnim.
2. **Punktacji społecznej (Social Scoring):** Klasyfikacji lub oceny uczniów prowadzącej do niekorzystnego traktowania w kontekstach niezwiązanych z pierwotnym celem (art. 5 ust. 1 lit. c).
3. **Biometrycznej kategoryzacji:** Systemów wnioskujących o cechach wrażliwych (pochodzenie, poglądy, przekonania religijne) na podstawie danych biometrycznych.
4. **Manipulacji podprogowej:** Technik wpływających na zachowanie ucznia w sposób zniekształcający jego zdolność do podjęcia świadomej decyzji, powodujących szkodę.

### 3.3 Systemy wysokiego ryzyka w edukacji (Art. 6 i Załącznik III, pkt 3)

[Z] Systemy AI w edukacji kwalifikują się jako systemy wysokiego ryzyka (High-Risk AI Systems), jeśli są przeznaczone do:
- **Określania dostępu lub przydziału:** Kwalifikacji uczniów do szkół, profili, kierunków kształcenia lub poziomów zaawansowania.
- **Oceny wyników i uczenia się:** Ewaluacji efektów uczenia się, automatycznego sprawdzania i oceniania prac rzutującego na końcową klasyfikację.
- **Oceny poziomu wykształcenia:** Monitorowania zachowania i wykrywania niedozwolonych zachowań podczas egzaminów (proctoring).

Wyjątek proceduralny (art. 6 ust. 3) dla systemów wąskich (wąskie zadanie proceduralne, poprawa wcześniejszej działalności człowieka lub proste wykrywanie anomalii) wymaga formalnej dokumentacji i rejestracji, chyba że system dokonuje profilowania osób fizycznych. Profilowanie ucznia zawsze wyklucza wyjątek i utrzymuje klasyfikację wysokiego ryzyka.

### 3.4 Obowiązki dostawców i podmiotów wdrażających

[Z] Dla systemów AI wysokiego ryzyka:
- **Dostawca (producent / deweloper):** System zarządzania ryzykiem (art. 9), zarządzanie jakością danych szkoleniowych (art. 10), dokumentacja techniczna (art. 11), automatyczne rejestrowanie logów (art. 12), przejrzystość i instrukcja obsługi (art. 13), nadzór ludzki w architekturze (art. 14), dokładność, solidność i cyberbezpieczeństwo (art. 15), rejestracja w unijnej bazie danych (art. 71).
- **Podmiot wdrażający (szkoła / dyrektor):** Używanie zgodnie z instrukcją dostawcy (art. 26 ust. 1), zapewnienie kompetentnego nadzoru ludzkiego przez nauczycieli (art. 26 ust. 2), monitorowanie działania i zgłaszanie incydentów dostawcy, przechowywanie automatycznie generowanych logów przez co najmniej 6 miesięcy (art. 26 ust. 6), przeprowadzenie oceny skutków dla praw podstawowych (FRIA, art. 27), poinformowanie przedstawicieli pracowników i uczniów przed uruchomieniem.

### 3.5 Terminy i harmonogram wdrażania AI Act

- **2 sierpnia 2024 r.:** Wejście w życie AI Act.
- **2 lutego 2025 r.:** Zakaz praktyk niedozwolonych (art. 5: rozpoznawanie emocji, scoring społeczny).
- **2 sierpnia 2025 r.:** Obowiązki dla modeli ogólnego przeznaczenia (GPAI) oraz wyznaczenie organów nadzorczych.
- **2 sierpnia 2026 r.:** Pełne stosowanie przepisów dla systemów wysokiego ryzyka z Załącznika III (w tym w edukacji i szkoleniu zawodowym).
- **2 sierpnia 2027 r.:** Stosowanie do systemów stanowiących komponenty bezpieczeństwa w ramach innych unijnych przepisów harmonizacyjnych.

## 4. Model danych, zbieranie i minimalizacja [P]

[P] Model danych aplikacji szkolnej MUSI realizować zasadę minimalizacji danych (art. 5 ust. 1 lit. c RODO):
- **Identyfikatory:** Stosuj sztuczne identyfikatory wewnętrzne (UUIDv4) jako klucze główne. Nigdy nie używaj numeru PESEL ani oficjalnego identyfikatora z SIO jako klucza w adresach URL, nazwach plików lub sesjach.
- **Pola opcjonalne:** Numer telefonu, adres zamieszkania, zdjęcie profilowe nie mogą być polami obowiązkowymi w aplikacjach wspierających naukę przedmiotową.
- **Dane wrażliwe (art. 9 RODO):** Aplikacje przedmiotowe, quizy i platformy ćwiczeniowe NIE MOGĄ przetwarzać danych o zdrowiu, pochodzeniu etnicznym, przekonaniach czy danych biometrycznych. Jeśli wsparcie ucznia wymaga dostosowania (np. dysleksja), przechowuj wyłącznie techniczny znacznik konfiguracyjny (np. `extra_time_ratio: 1.25`) bez ujawniania diagnozy medycznej.
- **Metadane:** Usuwaj metadane EXIF z przesyłanych przez uczniów zdjęć prac przed zapisaniem ich na serwerze.

## 5. Uwierzytelnianie, opcjonalne zaproszenia i sesja [P]

[P] Profil uwierzytelniania w środowisku szkolnym:
- **Hasła:** Wymagaj haseł o długości minimum 12 znaków. Weryfikuj hasła z listami popularnych wycieków (HaveIBeenPwned API lub lokalny słownik). Hasła MUSZĄ być haszowane przy użyciu algorytmu Argon2id (rekomendacja) lub bcrypt z odpowiednim kosztem pracy (work factor >= 12).
- **Logowanie kodem PIN / kodem QR:** Dopuszczalne wyłącznie dla młodszych uczniów w ramach kont tymczasowych lub ograniczonych sesji w klasie. Kod PIN musi wygasać i być powiązany z fizycznym stanowiskiem lub ograniczonym czasem lekcji.
- **Zarządzanie sesją:** Identyfikator sesji musi być kryptograficznie losowy (co najmniej 128 bitów entropii). Ciasteczka sesyjne MUSZĄ posiadać flagi `HttpOnly`, `Secure` oraz `SameSite=Lax` (lub `Strict`).
- **Wygasanie sesji:** Automatyczne wylogowanie po okresie bezczynności (maksymalnie 30 minut dla uczniów, 15 minut dla personelu administracyjnego i nauczycieli).

## 6. Role, uprawnienia i integralność wpisów [P]

[P] Kontrola dostępu w aplikacji szkolnej:
- **RBAC (Role-Based Access Control):** Zdefiniuj wyraźne role: Uczeń, Nauczyciel, Rodzic/Opiekun, Dyrektor/Administrator.
- **Izolacja danych (Multi-Tenancy):** Każde zapytanie do bazy danych MUSI weryfikować uprawnienie w kontekście zalogowanego użytkownika (np. uczeń widzi wyłącznie własne oceny i zadania; rodzic widzi wyłącznie dane swoich dzieci; nauczyciel widzi uczniów klas, w których uczy).
- **Zabezpieczenie przed IDOR:** Bezpośrednie odwołania do obiektów (Insecure Direct Object Reference) muszą być blokowane na poziomie serwera, a nie ukrywane w interfejsie.
- **Niezmienność wpisów:** Zmiany ocen, frekwencji i oficjalnych uwag wymagają ścieżki audytu z identyfikatorem wprowadzającego i znacznikiem czasu UTC.

## 7. Szyfrowanie i zarządzanie kluczami [P]

[P] Standardy kryptograficzne:
- **Dane w spoczynku (Data at Rest):** Szyfrowanie baz danych i dysków serwerowych algorytmem AES-256-GCM lub ChaCha20-Poly1305. Wrażliwe kolumny szyfrowane na poziomie aplikacji, jeśli baza jest współdzielona.
- **Dane w transmisji (Data in Transit):** Wymuszony protokół TLS 1.3 (minimalnie TLS 1.2 z bezpiecznymi zestawami szyfrów). Nagłówek HSTS (HTTP Strict Transport Security) z czasem co najmniej 1 rok (`max-age=31536000; includeSubDomains`).
- **Zarządzanie kluczami:** Klucze kryptograficzne NIE MOGĄ znajdować się w repozytorium kodu. Pobieraj klucze ze zmiennych środowiskowych lub bezpiecznego magazynu sekretów (KMS/Vault).

## 8. CSV i SQLite [P]

[P] Zasady bezpiecznej obsługi plików lokalnych i baz wbudowanych:
- **Iniekcja formuł w CSV (CSV Injection / Formula Injection):** Przy eksporcie danych uczniów do plików CSV każde pole tekstowe zaczynające się od znaków `=`, `+`, `-`, `@`, tabulacji lub powrotu karetki MUSI zostać poprzedzone pojedynczym apostrofem (`'`) lub oczyszczone, aby zapobiec wykonaniu złośliwego kodu w arkuszu kalkulacyjnym (Excel, Calc).
- **SQLite w aplikacjach szkolnych:** Stosuj tryb WAL (Write-Ahead Logging). Włącz sprawdzanie kluczy obcych (`PRAGMA foreign_keys = ON;`). Unikaj zapisu bazy SQLite w katalogach dostępnych publicznie przez serwer webowy.
- **Parametryzacja zapytań:** Bezwzględny nakaz stosowania zapytań parametryzowanych (Prepared Statements) w celu eliminacji podatności SQL Injection.

## 9. Web, PWA i urządzenia współdzielone [P]

[P] Bezpieczeństwo aplikacji webowych i Progressive Web Apps na komputerach szkolnych:
- **Urządzenia współdzielone w pracowni:** Szkolne pracownie komputerowe i tablety są urządzeniami współdzielonymi przez wielu uczniów. Aplikacja MUSI oferować widoczne i łatwe w użyciu wylogowanie, które natychmiast czyści pamięć podręczną przeglądarki, `localStorage`, `sessionStorage` oraz bazy `IndexedDB` z danych osobowych i identyfikatorów sesji.
- **Content Security Policy (CSP):** Wdrożenie restrykcyjnej polityki CSP blokującej ładowanie skryptów z nieznanych domen oraz inline scripts bez odpowiednich haszy lub nonce.
- **Brak telemetrii podmiotów trzecich:** Całkowity zakaz instalacji zewnętrznych skryptów analitycznych (Google Analytics, Meta Pixel) śledzących zachowanie uczniów w aplikacjach edukacyjnych.

## 10. Audyt, retencja i przywracanie [P/Z]

[P/Z] Polityka logowania i retencji:
- **Logi audytowe:** Rejestruj zdarzenia uwierzytelniania, odmowy dostępu, modyfikacje danych edukacyjnych i eksporty plików.
- **Minimalizacja w logach:** Logi systemowe i serwerowe NIE MOGĄ zawierać haseł w otwartym tekście, treści wiadomości ani pełnych danych osobowych uczniów. Zapisuj identyfikator użytkownika, znacznik czasu UTC, kod operacji i status wyniku.
- **Retencja danych:** Okres przechowywania danych w aplikacji nie może przekraczać czasu niezbędnego do realizacji celów dydaktycznych lub wymogów przepisów oświatowych. Po zakończeniu cyklu kształcenia dane są archiwizowane lub trwale usuwane.
- **Kopie zapasowe (Backup):** Regularne kopie zapasowe, testowane pod kątem przywracania co najmniej raz w semestrze, szyfrowane i przechowywane w bezpiecznej lokalizacji w EOG.

## 11. Incydenty [Z/P]

[Z] Procedura reagowania na naruszenia ochrony danych (art. 33-34 RODO):
- **Zgłoszenie do organu nadzorczego:** Szkoła (dyrektor) jako administrator danych ma obowiązek zgłosić naruszenie ochrony danych osobowych Prezesowi UODO bez zbędnej zwłoki, w miarę możliwości nie później niż w terminie 72 godzin po stwierdzeniu naruszenia, chyba że jest mało prawdopodobne, by skutkowało ono ryzykiem naruszenia praw lub wolności osób fizycznych.
- **Powiadomienie osób:** W przypadku wysokiego ryzyka naruszenia praw lub wolności uczniów i ich rodziców szkoła musi niezwłocznie zawiadomić osoby, których dane dotyczą.
- **Rejestr incydentów:** Każde naruszenie, jego okoliczności, skutki oraz podjęte działania naprawcze muszą zostać wpisane do wewnętrznego szkolnego rejestru naruszeń.

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

## 15. Przepływy danych AI, tutor i RAG [P/O]

### 15.1 Modele językowe w edukacji

[P/O] Zastosowanie modeli językowych (LLM) jako tutorów lub asystentów nauki wymaga szczególnej ostrożności:
- **Zero-Data Retention (ZDR):** Jeśli szkoła korzysta z zewnętrznego API modelu AI, umowa MUSI gwarantować, że dane z promptów uczniów nie są zapisywane na dyskach dostawcy dłużej niż jest to konieczne do wygenerowania odpowiedzi (maksymalnie buforowanie pamięciowe bez logowania) i NIE MOGĄ być wykorzystywane do trenowania przyszłych modeli.
- **Prywatność promptów:** Uczniowie MUSZĄ zostać poinstruowani, aby nie wpisywali do okna promptu danych osobowych, adresów, informacji rodzinnych ani zwierzeń.

### 15.2 Retrieval-Augmented Generation (RAG)

[P] W architekturze RAG przeszukującej materiały szkolne:
- Wektoryzuj wyłącznie materiały edukacyjne (podręczniki, konspekty, zadania).
- Bazy wektorowe NIE MOGĄ zawierać dokumentacji pedagogicznej, orzeczeń psychologicznych ani danych osobowych uczniów.
- Izolacja uprawnień: Model nie może mieć dostępu do bazy dokumentów z innych klas lub poziomów uprawnień.

### 15.3 Halucynacje i odpowiedzialność pedagogiczna

[P] Wyniki generowane przez systemy AI mają charakter pomocniczy. Żadna oficjalna ocena, klasyfikacja semestralna ani decyzja o promocji nie może być podejmowana wyłącznie w sposób zautomatyzowany (art. 22 RODO). Nauczyciel zachowuje pełną merytoryczną i prawną kontrolę nad ocenianiem.

### 15.4 Bramy architektoniczne i k-anonimowość dla modeli AI [P]

[P] W architekturze systemów edukacyjnych integrujących komponenty AI obowiązują trzy poziomy ochrony danych:

#### 1. Klasyfikacja poziomów przetwarzania (L0 / C1 / C2)
- **Poziom L0 (Model w pełni lokalny):** Model działa wyłącznie na infrastrukturze szkolnej lub urządzeniu końcowym (np. llama.cpp, Ollama w sieci lokalnej szkoły). Żadne zapytania nie opuszczają sieci szkolnej. Dozwolony dla zapytań z danymi kontekstowymi po autoryzacji.
- **Poziom C1 (Chmura z umową powierzenia DPA i ZDR):** Zewnętrzny dostawca przetwarzający zapytania na terenie EOG z podpisaną umową powierzenia przetwarzania danych (art. 28 RODO) oraz gwarancją braku trenowania modeli na danych użytkowników (Zero Data Retention). Przed wysłaniem zapytania bezpośrednie identyfikatory uczniów (imię, nazwisko, PESEL, login) MUSZĄ zostać usunięte lub zastąpione sztucznymi tokenami jednorazowymi.
- **Poziom C2 (Zewnętrzne komercyjne modele publiczne):** Brak dedykowanej umowy powierzenia ze szkołą. Wszelkie zapytania wysyłane do takich serwisów MUSZĄ być w 100% zanonimizowane i pozbawione jakichkolwiek cech pozwalających na identyfikację ucznia lub szkoły.

#### 2. Wymóg k-anonimowości (k >= 5) i l-różnorodności (l >= 2)
Przy generowaniu zagregowanych statystyk edukacyjnych, raportów postępów lub zasilaniu modeli predykcyjnych:
- **Próg k-anonimowości:** Każda grupa uczniów o identycznych quasi-identyfikatorach (np. wiek, klasa, płeć, profil) MUSI liczyć co najmniej $k = 5$ unikalnych uczniów. Grupy o liczebności poniżej 5 podlegają supresji (usunięciu) lub uogólnieniu (generalizacji).
- **Próg l-różnorodności:** W ramach każdej grupy o identycznych quasi-identyfikatorach atrybuty wrażliwe (np. oceny, status wsparcia psychologicznego) muszą posiadać co najmniej $l = 2$ różne wartości, uniemożliwiając atak oparty na jednorodności (homogeneity attack).
- **Walidacja skryptowa:** Zastosuj deterministyczny skrypt weryfikujący (np. `scripts/check_k_anonymity.py`) przed wyeksportowaniem lub przesłaniem zbioru danych.

## 16. Szkolne logowanie federacyjne i SSO [P]

[P] Integracja ze szkolnymi systemami tożsamości:
- **Protokoły standardowe:** Stosuj OpenID Connect (OIDC) lub SAML 2.0.
- **Minimalizacja atrybutów:** W żądaniach uwierzytelniających pobieraj wyłącznie niezbędne atrybuty (np. wewnętrzny identyfikator `sub` oraz rola w szkole `eduPersonAffiliation`). Nie pobieraj pełnych profili użytkowników ani list kontaktów.
- **Ochrona tokenów:** Tokeny dostępu i tokeny odświeżające (Refresh Tokens) muszą być przechowywane w bezpieczny sposób (np. szyfrowana baza lub pamięć serwera), a nie w otwartym magazynie przeglądarki.

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
```
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

## 18. Publikacja, dokumenty i produkty pochodne [D/O]

### 18.1 Zasady publikacji wizerunku i prac uczniów

[D/O] Publikacja zdjęć uczniów na stronie internetowej szkoły lub profilach społecznościowych:
- **Zgoda opiekunów:** Wymagana dobrowolna, pisemna zgoda rodziców (art. 6 ust. 1 lit. a RODO oraz prawo autorskie i prawo prasowe).
- **Zasada rozdzielności:** Zgoda na publikację wizerunku nie może być łączona z innymi zgodami ani traktowana jako obowiązek rekrutacyjny.
- **Brak łączenia z danymi:** Unikaj podpisywania zdjęć pełnym imieniem i nazwiskiem ucznia wraz z klasą w mediach publicznych.

### 18.2 Zgłaszanie aktualizacji prawnych i weryfikacja źródeł

[P] Wszelkie propozycje aktualizacji niniejszego skilla, rejestru źródeł lub procedur bezpieczeństwa należy zgłaszać w repozytorium GitHub projektu:
`https://github.com/siberius/student-data-protection/issues` z etykietą `legal-update`.

© 2026 Luděk Sušický. [MIT](https://opensource.org/license/mit). Zmodyfikowana wersja 1.2 opiera się na pierwotnym przewodniku z października 2026 r.; zachowaj informacje o autorze, licencję i oznaczenia zmian. Źródła zewnętrzne zachowują własne prawa.

## Licencja (License)

MIT License

Copyright (c) 2026 Luděk Sušický

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
