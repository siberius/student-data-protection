# 1. Wykładnia wymagań i procedura asystenta

<!-- Generowana referencja; edytuj utrzymywany samodzielny przewodnik. -->

Sekcje źródłowe: 1.

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

© 2026 Luděk Sušický. [MIT](https://opensource.org/license/mit). Wydanie zrewidowane wersji 1.2, oparte na pierwotnym przewodniku z października 2026 r. Zachowaj informacje o autorze, licencję i oznaczenia zmian.
