# Ochrana dat žáků ve školních aplikacích

[![Skills.sh](https://img.shields.io/badge/skills.sh-Install-blue)](https://skills.sh/siberius/student-data-protection)
[![Dokumentace](https://github.com/siberius/student-data-protection/actions/workflows/docs.yml/badge.svg)](https://github.com/siberius/student-data-protection/actions/workflows/docs.yml)

> 📖 **Článek a rozbor na Vibemaker:** [Chrání vaše aplikace data žáků?](https://vibemaker.cz/clanek/bezpeci-dat-zaku/)

[![Bezpečí dat žáků](docs/student-data-protection.gif)](https://vibemaker.cz/clanek/bezpeci-dat-zaku/)

**English:** [README.md](README.md) · **Anglická verze průvodce:** [docs/student-data-protection.md](docs/student-data-protection.md)

## Instalace a rychlé spuštění

Nainstaluj vybranou jazykovou variantu do svého AI asistenta (Claude Code, Cursor, Codex, Antigravity, OpenCode, Cline aj.) přes CLI standard [skills.sh](https://skills.sh):

```bash
# Instalace české varianty (pro české ZŠ a SŠ)
npx skills add siberius/student-data-protection --skill ochrana-dat-zaku --full-depth -g -a codex

# Nebo instalace mezinárodní anglické verze
npx skills add siberius/student-data-protection --skill student-data-protection --full-depth -g -a codex

# Výpis všech 7 dostupných jazykových variant
npx skills add siberius/student-data-protection --full-depth --list
```

Bez `--agent` příkaz `skills use` vypíše připravený prompt. Pro dočasné spuštění podporovaného asistenta se skillem:

```bash
npx skills use siberius/student-data-protection --skill ochrana-dat-zaku --full-depth --agent codex
```

Praktický průvodce pro učitele, školní IT a každého, kdo staví školní aplikace, které pracují s údaji žáků. Propojuje použitelný právní rámec s výslovně zvoleným bezpečnostním profilem a ověřitelnými implementačními kontrolami.

Před vlastní prací skill zjistí potřebný kontext a doptá se na chybějící rozhodující informace. Využívá již sdělená fakta a oprávnění; nezodpovězená rozhodující otázka zastaví jen závislou práci. [Vstupní postup](cs/references/workflow.md) pokrývá relevantní rozsah, data, publikum, příjemce, životní cyklus a prostředí.

[Publikování a odvozené výstupy](cs/references/publication.md) řeší povolená veřejná pole, přezkum dokumentů/médií, původ údajů, skutečné sestavené výstupy, indexy, přístup, odstranění a bezpečné aktualizace. Načítá se jen pro příslušný úkol. Technická zpětná vazba používá očištěné syntetické příklady a nikdy se neodesílá automaticky.

## Praktická řešení a velikost balíčku

Začni krátkým nativním jádrem a načti jen potřebnou referenci. [Praktická řešení](cs/references/practical-solutions.md) nabízejí šest režimů dat: jednorázové procvičování, omezený sběr, uložený pokrok, úřední evidenci, přehledy/exporty a AI tutora. Obsahují cesty realizace, omezení rizika oproti trvalé opravě a kartu řešení. Rozpracuj jen zvolený postup. Jde o návrhové příklady, nikoli důkaz nasazených ochran.

Kompletní průvodce zůstává samostatnou čtenářskou verzí; nenačítej jej současně se všemi referencemi. Zatím zachovej jeden skill. Incidenty, audit či implementaci vyčleň až při samostatných vstupech, oprávněních a výstupech; společné ochrany neduplikuj.

**Rozsah české/anglické verze:** české prostředí základních a středních škol (ZŠ a SŠ). **Časové vymezení:** říjen 2026. Uvedené datum ověření právních zdrojů je 22. 10. 2026; upřesnění rozsahu ze dne 30. 10. 2026 nepředstavuje nové právní ověření. Před pozdějším použitím zkontrolujte aktuálnost předpisů a jejich použitelnost v konkrétní škole.

Česká a anglická verze jsou určeny českým ZŠ a SŠ, nikoli mateřským či vysokým školám. Španělská, polská, ukrajinská, německá a francouzská verze jsou samostatnými adaptacemi pro příslušné právní řády, nikoli pouhým přenesením českého práva.

## Dostupné jazykové verze a nativní skilly

| Jazyk / Jurisdikce | Nativní skill | Samostatný průvodce | Registr zdrojů | Readme |
| --- | --- | --- | --- | --- |
| **Čeština (Česko / EU)** | [cs/SKILL.md](cs/SKILL.md) | [docs/ochrana-dat-zaku.md](docs/ochrana-dat-zaku.md) | [docs/registr-zdroju.md](docs/registr-zdroju.md) | [README.cs.md](README.cs.md) |
| **English (EU / Czech context)** | [SKILL.md](SKILL.md) | [docs/student-data-protection.md](docs/student-data-protection.md) | [docs/source-register.md](docs/source-register.md) | [README.md](README.md) |
| **Español (España / UE)** | [es/SKILL.md](es/SKILL.md) | [docs/proteccion-datos-alumnado.md](docs/proteccion-datos-alumnado.md) | [docs/registro-fuentes.md](docs/registro-fuentes.md) | [README.es.md](README.es.md) |
| **Polski (Polska / UE)** | [pl/SKILL.md](pl/SKILL.md) | [docs/ochrana-danych-uczniow.md](docs/ochrana-danych-uczniow.md) | [docs/rejestr-zrodel.md](docs/rejestr-zrodel.md) | [README.pl.md](README.pl.md) |
| **Українська (Україна / ЄС)** | [uk/SKILL.md](uk/SKILL.md) | [docs/zakhyst-danykh-uchniv.md](docs/zakhyst-danykh-uchniv.md) | [docs/reiestr-dzherel.md](docs/reiestr-dzherel.md) | [README.uk.md](README.uk.md) |
| **Deutsch (Deutschland / EU)** | [de/SKILL.md](de/SKILL.md) | [docs/schuelerdatenschutz.md](docs/schuelerdatenschutz.md) | [docs/quellenregister.md](docs/quellenregister.md) | [README.de.md](README.de.md) |
| **Français (France / UE)** | [fr/SKILL.md](fr/SKILL.md) | [docs/protection-donnees-eleves.md](docs/protection-donnees-eleves.md) | [docs/registre-sources.md](docs/registre-sources.md) | [README.fr.md](README.fr.md) |

## Co v průvodci najdete

- datový inventář, minimalizaci a identitu
- ověřené účty versus jednorázové kódy a QR
- oprávnění na serveru a integritu záznamů
- šifrování (AES-256-GCM, správa klíčů, TLS)
- SQLite, CSV, exporty a ochranu proti vzorcům
- PWA, sdílená zařízení a odhlášení
- audit, retenci, zálohy a obnovu
- reakci na incidenty a lhůtu 72 hodin
- AI Act: rozsah, zakázané praktiky, high-risk použití ve vzdělávání, časovou osu
- rozlišení lokální a nelokální AI (L0/C1/C2), k-anonymita (k >= 5) a l-diverzita (l >= 2) s deterministickou kontrolou skriptem
- checklist před produkcí a 38 přijímacích scénářů včetně podmíněných kontrol AI/RAG, SSO a nelokální AI

## Nativní skill a samostatný průvodce

Použij [český SKILL.md](cs/SKILL.md), [anglický skill](SKILL.md) nebo [španělský skill pro Španělsko](es/SKILL.md) v prostředí se souborovými skilly. Zachovej LICENSE a references/ pohromadě. Načítej jen potřebné moduly. [Španělský průvodce](docs/proteccion-datos-alumnado.md) upravuje národní právo pro Španělsko; anglický průvodce zachovává původní kontext EU/ČR, který je třeba vztáhnout ke skutečné zemi. Instalace není automatická ani neprokazuje provedení.

Ze zadání vyber návrh, implementaci, audit nebo incident. Audit reportuje bez změn aplikace. U malé opravy posuď dotčený tok a relevantní regrese. Přísný profil se přijímá podle kontextu; před výměnou architektury posuď existující rovnocenné ochrany.

Úplné samostatné návody zůstávají pro ruční použití a chaty s instrukcemi. Jejich očíslované scénáře jsou plánem testů, nikoli důkazem provedení. [Scénáře chování skillu](docs/overeni-chovani-skillu.md) jsou oddělené.

## Jak ho použít

1. Přečtěte si [průvodce](docs/ochrana-dat-zaku.md) dřív, než navrhnete datový model.
2. Sekci 12 použijte jako checklist a sekci 13 jako testovací plán.
3. Vložte průvodce do AI asistenta jako kontext projektu. Je napsaný jako skill a označuje právní povinnosti (`[Z]`), bezpečnostní profil (`[P]`), doporučení (`[D]`) a body k ověření (`[O]`).
4. Skutečné údaje žáků nikdy nevkládejte do běžného či neschváleného AI chatu ani do veřejného repozitáře. Používejte syntetická data.

Průvodce je záměrně konkrétní. Kde říká MUSÍ, popisuje bezpečnostní profil, ne doslovný příkaz GDPR. Odchylku doložte hrozbou, náhradním opatřením, testem a rozhodnutím odpovědné osoby školy.

## Co to není

Není to právní posudek ani certifikát. Splněný checklist nedokazuje soulad s GDPR ani shodu high-risk AI. Před reálným zpracováním správce zajistí titul, retenci, smlouvy a potřebná posouzení a včas konzultuje pověřence pro nezávislou radu. Odpovědnost za provoz zůstává správci. Termíny a výklady AI Actu se mění, před právně významným nasazením ověřte aktuální znění.

## Zdroje a verze

Verze 1.2, vydání 14. 11. 2026. Ochrana pro nelokální AI, k-anonymita (k >= 5), l-diverzita (l >= 2) a deterministická kontrola skriptem doplněny 14. 11. 2026. Původní datum ověření zdrojů je 22. 10. 2026. Viz [registr zdrojů](docs/registr-zdroju.md). Průvodce odkazuje na GDPR, AI Act Service Desk, ÚOOÚ, EDPB, OWASP, NIST, ENISA a dokumentaci SQLite.

## Autor

**Luděk Sušický**, biolog, středoškolský a vysokoškolský učitel informatických předmětů

- E-mail: [ludek.susicky@gmail.com](mailto:ludek.susicky@gmail.com)
- X: [@ludeksusicky](https://x.com/ludeksusicky)
- LinkedIn: [Luděk Sušický](https://www.linkedin.com/in/ludek-susicky/)
- GitHub: [@siberius](https://github.com/siberius): další vzdělávací projekty a otevřené aplikace

## Licence

© 2026 Luděk Sušický. Text je pod licencí [MIT](https://opensource.org/license/mit). Viz [LICENSE](LICENSE).

Opravy a připomínky jsou vítané, hlavně když zastará právní odkaz nebo bezpečnostní doporučení.

[Español: Španělsko](README.es.md) · [Registr zdrojů](docs/registr-zdroju.md) · [Ověření skillu](docs/overeni-chovani-skillu.md)
