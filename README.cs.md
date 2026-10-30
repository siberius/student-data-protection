# Ochrana dat žáků ve školních aplikacích

[![Dokumentace](https://github.com/siberius/student-data-protection/actions/workflows/docs.yml/badge.svg)](https://github.com/siberius/student-data-protection/actions/workflows/docs.yml)

**English:** [README.md](README.md) · **Anglická verze průvodce:** [docs/student-data-protection.md](docs/student-data-protection.md)

Praktický průvodce pro učitele, školní IT a každého, kdo staví školní aplikace, které pracují s údaji žáků. Převádí povinnosti GDPR a AI Actu do konkrétních technických pravidel, která se dají implementovat a otestovat.

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
- checklist před produkcí a 30 akceptačních testů

## Jak ho použít

1. Přečtěte si [průvodce](docs/ochrana-dat-zaku.md) dřív, než navrhnete datový model.
2. Sekci 12 použijte jako checklist a sekci 13 jako testovací plán.
3. Vložte průvodce do AI asistenta jako kontext projektu. Je napsaný jako skill a označuje právní povinnosti (`[Z]`), bezpečnostní profil (`[P]`), doporučení (`[D]`) a body k ověření (`[O]`).
4. Skutečné údaje žáků nikdy nevkládejte do AI chatu ani do veřejného repozitáře. Používejte syntetická data.

Průvodce je záměrně konkrétní. Kde říká MUSÍ, popisuje bezpečnostní profil, ne doslovný příkaz GDPR. Odchylku doložte hrozbou, náhradním opatřením, testem a rozhodnutím odpovědné osoby školy.

## Co to není

Není to právní posudek ani certifikát. Splněný checklist nedokazuje soulad s GDPR ani shodu high-risk AI. Před zpracováním reálných dat musí škola a její pověřenec potvrdit právní titul, retenci, smlouvy a případné posouzení. Termíny a výklady AI Actu se mění, před právně významným nasazením ověřte aktuální znění.

## Zdroje a verze

Verze 1.1, zdroje ověřeny 22. 10. 2026, vydání 25. 10. 2026. Průvodce odkazuje na GDPR, AI Act Service Desk, ÚOOÚ, EDPB, OWASP, NIST, ENISA a dokumentaci SQLite.

## Autor

Luděk Sušický, biolog, středoškolský a vysokoškolský učitel informatických předmětů.

## Licence

© 2026 Luděk Sušický. Text je pod licencí [MIT](https://opensource.org/license/mit). Viz [LICENSE](LICENSE).

Opravy a připomínky jsou vítané, hlavně když zastará právní odkaz nebo bezpečnostní doporučení.
