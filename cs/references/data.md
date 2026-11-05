# 4. Datový model, sběr a minimalizace [P]

<!-- Generovaná reference; upravuj udržovaného samostatného průvodce. -->

Zdrojové oddíly: 4.

## 4. Datový model, sběr a minimalizace [P]

### 4.1 Datový inventář a identita

- Pro každé pole určuj účel, zdroj, povinnost/volitelnost, právní titul, příjemce, citlivost, retenci a způsob výmazu. Odmítnutí volitelného pole nesmí zablokovat nesouvisející základní službu.
- Odděl `school_id`, `user_id` účtu, interní `student_id`, `record_id`, případné `submission_id` a tajný session token. Účet a osoba, které se údaj týká, nejsou totéž: učitel nebo rodič může oprávněně jednat za žáka. Veřejné náhodné ID není oprávnění.
- Jméno zadané uživatelem je nedůvěryhodný údaj, ne autentizace. Nepoužívej jméno, datum narození, třídu ani device ID jako samotný klíč k historii či ke změně existujícího profilu.
- Odděl identifikační mapování od obsahových záznamů, kde to provoz umožňuje. U neověřeného podání ponech vazbu na žáka nepotvrzenou; přiřazení ověř a audituj. Neslučuj osoby jen podle stejného jména.
- Umožni anonymní nebo pseudonymní sběr, pokud účel nepotřebuje identitu. Za anonymní neoznačuj formulář, pokud jej lze spojit s účtem, ID, časem či jinou evidencí.
- Nezjišťuj IMEI, MAC, reklamní ID ani fingerprint. Je-li instalační ID nutné, generuj je náhodně a omez účelem a retencí. Není autentizací ani anonymizací. Na sdíleném zařízení preferuj ID dané relace.
- Eviduj zdroj záznamu, stav ověření, autora změny, verzi a retenční kategorii; `expires_at` nastav tam, kde je doba určitelná. Jména, kontakty ani obsah nepatří do URL, názvů souborů, metrik nebo chybových hlášení.

### 4.2 Formuláře, přílohy a integrace

- Na serveru povol jen deklarovaná pole a hodnoty. Neznámá pole odmítni, chraň systémová pole před hromadným přiřazením. Stanov délky, typy, rozsahy, kódování a velikost podání; HTML ani vzorce nespouštěj.
- Veřejný formulář nesmí nabízet vyhledávání osob, seznam tříd se jmény nebo historii podání. Neověřené podání neaktualizuje automaticky školní evidenci. Omez automatizované zneužití a objem; případná ochrana proti botům nesmí zavést neprověřené sledování dětí.
- U volného textu upozorni, co se nemá zadávat, a nabídni strukturovaná minimální pole. Zvlášť posuď fotografie, hlas, polohu, zdravotní informace a poradenské záznamy; nezaváděj jejich sběr jen „pro budoucí využití“.
- Přílohy přijímej podle allowlistu typů, ověř skutečný formát, limit velikosti a škodlivý obsah. Ukládej mimo webroot pod náhodným názvem, bez možnosti spuštění; aktivní obsah odmítni nebo bezpečně izoluj. Náhledy, OCR, náhledové obrázky a metadata mají stejná oprávnění a retenční pravidla jako originál.
- Stažení přílohy vždy autorizuj podle školy, osoby, účelu a role. Krátkodobý podepsaný odkaz je přenositelné oprávnění; omez jeho dobu a rozsah. Sdílený odkaz nesmí změnit dokument na veřejný.
- Import CSV/API má náhled mapování, validaci duplicit a cílové školy, atomické potvrzení a audit. Externí ID je unikátní v rámci zdrojového systému a školy. Nepřepisuj evidenci na základě shody jména.
- Integrace mají vlastní servisní identitu s minimálním rozsahem, rotací tajemství a možností odvolání. Webhooky ověř podpisem, časovým oknem a ochranou proti opakování. Push/e-mail upozornění výchozí profil posílá bez citlivého obsahu, pouze s odkazem do ověřeného rozhraní.

Podklad pro návrh minimalizace a oddělování dat: [ENISA: Data Protection Engineering](https://www.enisa.europa.eu/sites/default/files/publications/ENISA%20Report%20-%20Data%20Protection%20Engineering.pdf). Konkrétní schéma a implementační volby výše jsou návrh tohoto skillu.

© 2026 Luděk Sušický. [MIT](https://opensource.org/license/mit). Revidované vydání verze 1.1 vychází z původního průvodce z října 2026. Zachovej autora, licenci a oznámení úprav.
