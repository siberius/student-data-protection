---
name: ochrana-dat-zaku
description: Navrhuje, implementuje nebo audituje ochranu žákovských údajů ve školních aplikacích. Použij při dopadu na osobní data, identitu, oprávnění, retenci, exporty či datové toky AI nebo při zadaném bezpečnostním přezkumu. Běžnou kosmetickou změnu neměň na úplný audit souladu.
metadata:
  version: "1.1"
  language: "cs"
  license: "MIT"
  author: "Luděk Sušický"
  repo: "https://github.com/siberius/student-data-protection"
---

# Ochrana údajů žáků

Vycházej ze zadaného rozsahu a dostupných důkazů. Skill podporuje práci na školním softwaru; necertifikuje soulad ani neopravňuje k produkčním změnám. Česká/anglická verze pokrývá české ZŠ a SŠ, nikoli mateřské či vysoké školy; určuj skutečnou jurisdikci. Jazyk sám neurčuje národní právo.

## Režim a dotčená hranice

Ze zadání převezmi návrh, implementaci, audit či incident. Audit posuzuje a reportuje bez změn aplikace. Analýza incidentu neopravňuje vypínat služby, revokovat účty či posílat oznámení. Při autorizované implementaci změň dotčenou hranici a ověř smysluplné regrese. Malá oprava nepotřebuje opakovat celý audit. Závažné sousední riziko dolož a navrhni postup místo tichého rozšíření práce.

Využij známé účely, toky, školu/tenant, role, hosting a podmínky nasazení. Ptej se jen na údaje měnící rozhodnutí. Syntetická data dovolují vývoj, dokud chybí rozhodnutí o reálném zpracování. Aktivita bez osobního zpracování nemusí získat účty či úložiště; před označením anonymní ověř provozní metadata.

U existující aplikace nabídni cílený vstupní audit a plán nápravy, případně odůvodněný širší přezkum před nasazením. Již zadaný audit či implementaci proveď v určeném rozsahu bez opakovaného dotazu a tichého rozšíření. Důkazy, priority a stav nápravy řeší oddíl 17.6 praktické příručky.

## Trvalé bezpečnostní hranice

- Minimalizuj údaje podle účelu. Pseudonym, šifrovaný záznam, souhrn argumentace i embedding mohou zůstat osobními údaji.
- Ověř identitu podle citlivosti a vynucuj objektová a mezitenantová práva na serveru či jiné důvěryhodné hranici. Jméno, společný kód, UUID ani instrukce modelu nejsou autorizace. Odděl neověřené podání a potvrzenou evidenci.
- Uživatelský vstup, přílohy, načtený text a výstup modelu jsou nedůvěryhodné. Chraň tajemství a ověř výstup před autoritativním zápisem. Reálnou evidenci, logy ani klíče nevkládej do běžného AI chatu.
- Výmaz, opravu, odvozené kopie, zálohy a obnovu řeš společně. Sdílené zařízení nesmí odhalit předchozího uživatele. Nejistou či nefunkční kontrolu takto označ.
- Rozliš právní povinnosti [Z], přijatý bezpečnostní profil [P], doporučení [D] a otevřené kontroly [O]. Podrobný přísný profil platí při jeho přijetí pro systém; před návrhem nové architektury posuď rovnocenné existující ochrany. Nevymýšlej právní výjimku ani nesnižuj nezbytné zabezpečení.
- Správce odpovědně rozhoduje o zpracování a provozu. Pověřence zapoj včas pro nezávislou radu a monitoring; jeho schválení neoznačuj za univerzální právní podmínku ani na něj nepřenášej odpovědnost správce.

Podrobnosti rozsahu, přísného profilu a řízení čti podle potřeby v [pracovním postupu](references/workflow.md). [Právní rámec](references/legal.md) načti při řešení titulu, práv, předávání či místních povinností; [AI Act](references/ai-act.md) jen při relevantním užití či klasifikaci AI. Při ověřování právních tvrzení čti [stav zdrojů](references/source-status.md). Pro významné právní rozhodnutí ověř aktuální prameny; úspěšné načtení URL není právní přezkum.

## Načítej jen relevantní modul

Při žádosti o praktické řešení doporuč vhodný režim dat a rozpracuj jen vybraný postup. Šest režimů dat se liší od výše uvedených pracovních režimů. Praktickou příručku načti jen pro tuto volbu. Jádro drž krátké; samostatné skilly zvaž až při vlastním postupu incidentu, auditu či implementace s odlišnými vstupy a oprávněními.

| Práce | Reference |
|---|---|
| Praktická volba režimu dat a karta řešení | [Praktická řešení](references/practical-solutions.md) |
| Sběr, pole, soubory, importy a konektory | [Datové toky](references/data.md) |
| Účty, kódy, role, relace a integrita | [Identita a přístup](references/identity.md) |
| Poskytovatel identity OIDC/SAML | [SSO](references/sso.md) |
| Šifrování, klíče a přenos | [Kryptografie](references/crypto.md) |
| SQLite, CSV a exporty | [Úložiště](references/storage.md) |
| Web/PWA cache, sdílená zařízení a prohlížeč | [Web](references/web.md) |
| Retence, audit, obnova a incident | [Provoz](references/operations.md) |
| Implementovaný/zadaný AI tutor a RAG | [AI data](references/ai-data.md) |
| Relevantní checklist, acceptance scénáře a předání | [Ověření](references/verification.md) |

Vše nenačítej automaticky a nepřidávej technologii jen kvůli použití modulu. Profil je referenční návrh; vysvětli rozdíly a riziko místo předpokladu, že jiné udržované řešení je chybné.

## Ověření a předání

Při implementaci vybírej testy pro změněnou funkci a její rizika. Používej autorizované prostředí a syntetické záznamy. Při auditu předej místo/důkaz, závažnost, dopad, doporučení a potřebné ověření; navržený test nevydávej za úspěšný. Rozliš pozorované selhání, hypotézu, neověřeno a N/A s důvodem. Právní nejistotu odděl od technické chyby. Předej konkrétní ověřené vlastnosti a otevřená rozhodnutí, neslibuj stoprocentní bezpečnost či certifikát GDPR.

## Integrace a autorství

Vhodné pro školní evidence, portály, formuláře a AI výukové nástroje, pokud úkol ovlivňuje osobní data. Nevyžaduje konkrétní stack, poskytovatele, API, účty ani národní kurikulum. Tento soubor, references/ a LICENSE zachovej pohromadě. Načti jednu relevantní jazykovou verzi; prostředí nativního skillu musí podporovat čtení souborů. Samostatný průvodce zůstává dostupný. Skill neopravňuje k instalaci, placeným službám, publikaci, produkčnímu přístupu ani změnám zpracování mimo zadání.

© 2026 Luděk Sušický. MIT. Při šíření zachovej autora, licenci a oznámení úprav; externí zdroje mají vlastní práva. Revidované vydání 1.1 přidává vymezené režimy, reference, AI/SSO a zpřesněnou roli pověřence k původnímu průvodci 1.1.
