# 5. Uwierzytelnianie, opcjonalne zaproszenia i sesja [P]

<!-- Generowana referencja; edytuj utrzymywany samodzielny przewodnik. -->

Sekcje źródłowe: 5, 6.

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

© 2026 Luděk Sušický. [MIT](https://opensource.org/license/mit). Wydanie zrewidowane wersji 1.2, oparte na pierwotnym przewodniku z października 2026 r. Zachowaj informacje o autorze, licencję i oznaczenia zmian.
