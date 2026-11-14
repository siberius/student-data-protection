# Ochrona danych osobowych uczniów w aplikacjach szkolnych

[![Skills.sh](https://img.shields.io/badge/skills.sh-Install-blue)](https://skills.sh/siberius/student-data-protection)

Profil bezpieczeństwa i skill asystenta dla aplikacji edukacyjnych (Polska i UE).

> Wersja: 1.2 · Zgodność: RODO (UE 2016/679), Akt o sztucznej inteligencji (AI Act, UE 2024/1689), polska Ustawa o ochronie danych osobowych z 2018 r. oraz Prawo oświatowe.

## Instalacja i szybki start

Zainstaluj wybraną edycję w swoim asystencie programowania (Claude Code, Cursor, Codex, Antigravity, OpenCode, Cline i innych) za pomocą narzędzia CLI z [skills.sh](https://skills.sh):

```bash
# Instalacja edycji polskiej (Polska / UE)
npx skills add siberius/student-data-protection --skill ochrana-danych-uczniow --full-depth -g -a codex

# Wyświetlenie wszystkich 7 dostępnych edycji językowych
npx skills add siberius/student-data-protection --full-depth --list
```

Wypróbowanie skilla bez stałej instalacji:

```bash
npx skills use siberius/student-data-protection --skill ochrana-danych-uczniow --full-depth --agent codex
```

## Przegląd edycji i dokumentacja

- **Samodzielny przewodnik w języku polskim:** [docs/ochrana-danych-uczniow.md](docs/ochrana-danych-uczniow.md)
- **Rejestr źródeł prawnych i technicznych:** [docs/rejestr-zrodel.md](docs/rejestr-zrodel.md)
- **Scenariusze ewaluacyjne zachowania skilla:** [docs/ewaluacja-skilla.md](docs/ewaluacja-skilla.md)
- **Natywny moduł skilla (PL):** [pl/SKILL.md](pl/SKILL.md)

## Główne filary profilu

1. **Odpowiedzialność dyrektora jako administratora (ADO):** Wdrożenie oprogramowania przetwarzającego dane uczniów wymaga decyzji dyrektora szkoły po konsultacji z IOD.
2. **Umowa powierzenia przetwarzania danych (art. 28 RODO):** Bezwzględny wymóg formalnej umowy powierzenia ze wszystkimi dostawcami chmury lub API sztucznej inteligencji.
3. **Bramy przetwarzania AI (L0 / C1 / C2):** Prymat modeli w pełni lokalnych (L0) oraz restrykcyjne bramy anonimizacji dla chmury z ZDR (C1).
4. **k-anonimowość (k >= 5) i l-różnorodność (l >= 2):** Obowiązkowa walidacja statystyczna zestawów danych i raportów przed udostępnieniem modelom predykcyjnym lub zewnętrznym.
5. **Ciągła świeżość prawna:** Asystent monitoruje aktualność powoływanych przepisów i za zgodą użytkownika zgłasza propozycje aktualizacji na GitHubie projektu.

### Autor

**Luděk Sušický** - biolog, średnioszkolny i uniwersytecki nauczyciel przedmiotów informatycznych

- E-mail: [ludek.susicky@gmail.com](mailto:ludek.susicky@gmail.com)
- X: [@ludeksusicky](https://x.com/ludeksusicky)
- LinkedIn: [Luděk Sušický](https://www.linkedin.com/in/ludek-susicky/)
- GitHub: [@siberius](https://github.com/siberius) - inne projekty edukacyjne i aplikacje open-source

### Licencja

Ten projekt jest objęty licencją MIT. Szczegóły znajdują się w pliku [LICENSE](LICENSE).
