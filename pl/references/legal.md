# 2. RODO i polskie ramy prawne

<!-- Generowana referencja; edytuj utrzymywany samodzielny przewodnik. -->

Sekcje źródłowe: 2.

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

© 2026 Luděk Sušický. [MIT](https://opensource.org/license/mit). Wydanie zrewidowane wersji 1.2, oparte na pierwotnym przewodniku z października 2026 r. Zachowaj informacje o autorze, licencję i oznaczenia zmian.
