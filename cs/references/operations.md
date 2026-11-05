# 10. Audit, retence a obnova [P/Z]

<!-- Generovaná reference; upravuj udržovaného samostatného průvodce. -->

Zdrojové oddíly: 10, 11.

## 10. Audit, retence a obnova [P/Z]

### Audit [P]

Eviduj UTC čas, interního aktéra, školu, operaci, objekt, výsledek a korelační ID. Zachycuj přihlášení a jeho selhání, odebrání práv, ověření/přepojení identity, změny evidenčních údajů, čtení vysoce citlivých záznamů, exporty, hromadné mazání, použití mimořádného přístupu, rotace klíčů a obnovy. Nezapisuj tokeny, kódy, klíče, obsah formulářů, zpráv ani jména do běžných provozních logů. Chráněnou historii důležitých změn uchovávej odděleně.

Audit ukládej do append-only cíle, ke kterému běžná aplikace nemá oprávnění mazat. Kontroluj integritu a přístup, synchronizuj čas. Hashový řetězec bez nezávisle chráněného ukotvení neprokazuje nezměnitelnost. Kritická změna evidenčního údaje, oprávnění nebo export musí mít trvalý auditní záznam či transakční outbox před potvrzením úspěchu; selhání auditu nesmí změnu tiše obejít.

### Retenční tabulka

[Z] Uchovávej data jen po dobu nezbytnou pro účel a příslušné povinnosti. GDPR neurčuje univerzální počet dnů pro všechny školní aplikace. [P] Následující hodnoty jsou návrh k potvrzení školou; zákonná povinnost a spisový/skartační režim mají přednost.

| Kategorie | Výchozí návrh |
|---|---|
| Vstupní kód/QR tajemství | Zneplatnit po expiraci nebo uzavření vstupu; nezachovávat použitelné tajemství. |
| Session tajemství | Revokovat ihned při logout/expiraci, neaktivní verifikátory odstranit do 24 hodin; audit bez tajemství lze držet déle. |
| Dočasná účast a device ID pro jednorázovou aktivitu | Odstranit do 24 hodin po jejím konci, pokud není dokumentován jiný nezbytný účel. |
| Rozpracovaná podání | Automatické ukládání jen při potřebě; návrh 7 dnů od poslední úpravy, uživatel zná expiraci. |
| Jednorázový formulář / přihláška | Lhůta podle dokončení účelu a případného přezkumu; před spuštěním nastavit konkrétní spouštěč a dobu. Žádná univerzální retence všech formulářů. |
| Evidence žáků, docházka, hodnocení, kontakty | Konkrétní lhůty podle účelu a příslušného spisového/skartačního režimu; ukončení účtu neznamená automatický výmaz povinné evidence. |
| Zprávy, portfolia a přílohy | Samostatné kategorie; potvrdit potřebu po skončení výuky nebo vztahu se školou. Odvozené kopie nesmějí mít neomezenou retenci. |
| Historie oprav a vazeb na osoby | Vymezit podle účelu ověřitelnosti a přezkumu; nesmí být neomezeným archivem všech smazaných údajů. |
| Dočasný serverový export | Nejvýše 24 hodin; právo ke stažení ověřit vždy znovu. |
| Běžný bezpečnostní audit | 90 dnů; incident může odůvodnit omezené pozastavení výmazu. |
| AI high-risk automatické logy | Samostatný režim podle použitelného čl. 26 odst. 6; nelze slepě použít 90 dnů. |
| Zálohy | Rolling 30 dnů, bez nekonečného uchovávání starých snapshotů. |

Automatický úklid spouštěj denně a sleduj chyby. Výmaz zahrnuje indexy, přílohy, exporty, cache a fronty. U neměnných záloh lze do doběhnutí omezené retence použít izolaci od běžného provozu a povinné opětovné uplatnění výmazů při obnově; dolož tento postup a nezamlčuj existenci záloh. Anonymizaci ověř i proti identifikaci malé třídy nebo vzácné kombinace údajů.

Zálohy jsou šifrované, oddělené a nejméně jedna kopie chráněná před změnou útočníkem. Výchozí provozní cíle: RPO 24 hodin, RTO 8 hodin; pro kritické evidence je škola zpřísní podle dopadu ztráty nebo výpadku. Obnovu proveď nejméně čtvrtletně v izolaci, včetně klíčů, vazeb, auditu, výmazů a zneplatnění historických session. Samotné úspěšné zálohování nedokazuje obnovitelnost.

## 11. Incidenty [Z/P]

[Z] Zpracovatel hlásí porušení správci bez zbytečného odkladu. Správce hlásí ÚOOÚ bez zbytečného odkladu a pokud možno do 72 hodin od chvíle, kdy se o porušení dozvěděl, ledaže je riziko pro práva a svobody nepravděpodobné; opoždění zdůvodní. Při pravděpodobném vysokém riziku informuje dotčené osoby bez zbytečného odkladu s posouzením výjimek čl. 34. Dokumentují se i nehlášená porušení. Šifrování může riziko snížit, ale únik klíče, integrita nebo nedostupnost vyžadují vlastní posouzení. [ÚOOÚ: porušení zabezpečení](https://uoou.gov.cz/profesional/poruseni-zabezpeceni-osobnich-udaju), [čl. 33–34 GDPR v podkladu ÚOOÚ](https://uoou.gov.cz/media/poskytnute-informace/2019/31122019/uoou-0612218-24.pdf).

[P] Připrav kontakt na správce, pověřence a provozní službu. Interní cíl: do 1 hodiny eskalace odpovědné osobě, do 24 hodin prvotní zhodnocení; jde o organizační cíle, ne zákonné lhůty. Runbook:

1. Zaznamenej čas zjištění a rozsah; zachovej důkazy chráněně, nerozesílej celé databáze.
2. Omez škodu: odvolej session/pozvánky, uzavři nebezpečný endpoint, izoluj napadenou službu; zajisti náhradní provoz dotčené agendy.
3. Urči údaje, osoby, příjemce, dostupnost klíčů a možné důsledky; zvaž důvěrnost, integritu i dostupnost.
4. Připrav rozhodnutí o hlášení a jeho podklady. Nečekej na úplnou forenzní zprávu; oznámení lze doplnit postupně.
5. Oprav příčinu, podle potřeby rotuj klíče, obnov a ověř data. Dokumentuj následná opatření a aktualizuj testy.

Samostatně prověř případné povinnosti podle českého zákona o kybernetické bezpečnosti a AI Actu, pokud se na provozovatele/systém vztahují; jejich lhůty nejsou automaticky GDPR 72 hodin. Metodický podklad: [NIST SP 800-61 Rev. 3, finální duben 2025](https://csrc.nist.gov/pubs/sp/800/61/r3/final).

© 2026 Luděk Sušický. [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Revidované vydání verze 1.1 vychází z původního průvodce z října 2026. Zachovej autora, licenci a oznámení úprav.
