# 1. Výklad požadavků a pracovní postup asistenta

<!-- Generovaná reference; upravuj udržovaného samostatného průvodce. -->

Zdrojové oddíly: 1.

## 1. Výklad požadavků a pracovní postup asistenta

- **[Z] Právní požadavek:** platí při splnění popsaných podmínek. Citovaný předpis má přednost před technickým doporučením.
- **[P] Bezpečnostní profil:** konkrétní implementační volba tohoto skillu. Výrazy MUSÍ/NESMÍ v technických sekcích určují tento profil, nikoli doslovný příkaz GDPR. Odchylku dolož hrozbou, náhradním opatřením, testem a rozhodnutím odpovědné osoby školy.
- **[D] Doporučení:** vhodné rozšíření podle rizika a provozu.
- **[O] Ověřit:** otázka závislá na skutečném použití, aktuálním právu nebo dosud nepotvrzené konfiguraci. Nevydávej ji za splněnou.

1. Ze zadání určuj režim: návrh, implementace, audit nebo incident. Audit předává nálezy a doporučení bez změn aplikace. Posouzení incidentu neopravňuje vypínat živé služby, rušit účty či odesílat oznámení. Takové kroky prováděj jen v rozsahu skutečného oprávnění.
2. Využij známý kontext a určuj dotčený účel, datové toky, role a změnu rizika. Ptej se jen na chybějící údaje měnící rozhodnutí. U malé opravy posuzuj dotčenou hranici a regrese, nezačínej celé hodnocení aplikace znovu. Závažný sousední problém dolož a oznam; implementaci potichu nerozšiřuj.
3. Mapuj relevantní data, příjemce, identitu, oprávnění, retenci a hrozby. Zachovej existující bezpečnou architekturu a funkční ochrany. Dokud chybí účel, právní titul či rozhodnutí pro provoz, používej syntetická data.
4. Při návrhu doporuč přiměřené ochrany a kritéria. Při autorizované implementaci je realizuj a dolož místa kódu či konfigurace. Při auditu uveď závažnost, důkaz, dopad, návrh a potřebné ověření. Podezření odliš od pozorovaného selhání.
5. Vyber acceptance scénáře podle dotčených funkcí a rizika. Rozliš prošlo, neprošlo, neprovedeno a netýká se s důvodem; každá oprava nevyžaduje nový návrh celého systému. Testovací plán nevydávej za provedení.
6. Před reálným provozem ověř titul, potřebné posouzení a aktuální předpis. Správce rozhoduje o nasazení s včasnou radou pověřence a odpovídajícím odborným přezkumem. Bez potřebného titulu či posouzení nedoporučuj dotčené zpracování; pokračuj v autorizované práci, které se překážka netýká.

Nevkládej skutečné žákovské údaje, produkční logy, klíče ani databáze do běžného AI chatu nebo veřejného repozitáře. Pro ladění generuj syntetická data. Použití reálných údajů v AI službě vyžaduje samostatné vyhodnocení účelu, nezbytnosti, smlouvy, příjemců, retence a předávání; samotné vypnutí trénování není dostatečné.

### 1.1 Ochrany podle datového toku a rizika

Právní povinnosti platí při splnění jejich podmínek. Základní cíle zahrnují účelové omezení, minimalizaci, důvěryhodné přístupové hranice, integritu, obnovitelnost a odpovědné řešení incidentů a práv podle skutečného zpracování. Aktivita bez osobního zpracování nepotřebuje účty, databázi, KMS ani osobní audit jen proto, že je popisuje průvodce. Před označením anonymní prověř i hosting a provozní metadata.

Podrobné hodnoty [P] níže tvoří přísný referenční profil pro nové systémy s trvalými školními evidencemi nebo projekty, které jej výslovně přijaly. Algoritmy, timeouty a provozní cíle jsou volby profilu. U existujícího systému nejprve posuď skutečné kontroly a rovnocenné ochrany proti relevantním hrozbám; jiná udržovaná technologie není automaticky zranitelnost. Neoslabuj autorizaci ani nevymýšlej právní výjimku. Podstatnou odchylku od přijatého profilu dolož hrozbou, náhradní ochranou, ověřením a rozhodnutím odpovědného správce. Audit může rozhodnutí navrhnout, nesmí předstírat schválení ani vyžadovat nové schválení každé běžné autorizované úpravy.

Architekturu zvol před použitím konkrétního implementačního receptu. Interní šifrování a správa nonce patří komponentě, která šifruje, ne automaticky aplikaci, pokud tuto úlohu řeší ověřená úložná služba. U skutečného řešení vysvětli přístup ke klíčům, zálohy, viditelnost metadat a zbytkové riziko. Změna hostingu, poskytovatele identity, placené služby či příjemců dat potřebuje příslušné oprávnění.

### 1.2 Správce a pověřenec

Správce odpovídá za účely, zákonné zpracování a rozhodnutí o provozu. Pověřenec nezávisle informuje, radí a monitoruje; je včas konzultován včetně DPIA. Tento průvodce mu nepřiděluje obecné provozní schvalování ani odpovědnost správce. Eviduj radu a odpovědné rozhodnutí; neshody řeš odpovídajícím procesem řízení. Viz [EDPB: pověřenec](https://www.edpb.europa.eu/sme/be-compliant/data-protection-officer_en).

© 2026 Luděk Sušický. [MIT](https://opensource.org/license/mit). Revidované vydání verze 1.1 vychází z původního průvodce z října 2026. Zachovej autora, licenci a oznámení úprav.
