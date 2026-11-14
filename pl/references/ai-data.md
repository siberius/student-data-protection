# 15. Przepływy danych AI, tutor i RAG [P/O]

<!-- Generowana referencja; edytuj utrzymywany samodzielny przewodnik. -->

Sekcje źródłowe: 15.

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

© 2026 Luděk Sušický. [MIT](https://opensource.org/license/mit). Wydanie zrewidowane wersji 1.2, oparte na pierwotnym przewodniku z października 2026 r. Zachowaj informacje o autorze, licencję i oznaczenia zmian.
