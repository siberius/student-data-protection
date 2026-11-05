# 17. Průvodce praktickým řešením

<!-- Generovaná reference; upravuj udržovaného samostatného průvodce. -->

Zdrojové oddíly: 17.

## 17. Průvodce praktickým řešením

### 17.1 Vyber režim práce s daty

[D] Tento modul načti při žádosti o praktické řešení nebo volbu rozsahu ochrany. Jde o návrhové postupy pro školní situace, nikoli doložená nasazení z praxe či stupně právního souladu. Doplňují pracovní režimy (návrh, implementace, audit, incident); neopravňují k provedení zásahu. Využij známý kontext. Ptej se jen na chybějící údaje měnící volbu: účel a potřebná pole, nutnost ověřené identity, uchování či úřední využití, sdílená zařízení a příjemce včetně hostingu, analytiky a AI.

Doporuč jeden režim s důvodem a případně jednodušší alternativu. Režimy kombinuj podle funkcí: anonymní cvičení a jmenný přehled učitele mohou mít odlišné hranice. Každá aplikace nepotřebuje nejsložitější režim. Použití reálných dat nadále vyžaduje odpovídající rozhodnutí o zpracování a ochranná opatření.

| Režim a školní příklad | Minimální návrh | Kontroly před reálným použitím |
|---|---|---|
| M1 Jednorázové procvičování: zlomky | Bez jména a účtu, pokud nejsou potřebné; odpovědi v pracovní paměti; vyčištění při ukončení. Lokální/statická aktivita může obejít centrální evidenci. | Obnovení, historie a další uživatel nesmějí odhalit odpovědi; před tvrzením o anonymitě prověř skutečné požadavky, logy, telemetrii a úložiště prohlížeče. |
| M2 Omezený sběr: přihláška na akci | Jen údaje potřebné pro akci; chráněný příjem a přístup; spouštěč výmazu podle účelu. Neověřené podání zůstává nepotvrzené. | Přístup k cizím záznamům, nečekaná zapisovatelná pole, limity podání a výmaz. Společný kód sám neověřuje identitu pro úřední evidenci. |
| M3 Navazující učení: uložený pokrok | Uchovávej minimum pokroku; osobní historii zpřístupni přes ověřenou školní identitu. Pseudonymní přístup posuď podle následků jeho zneužití. | Cizí historie, odhlášení na sdíleném zařízení, změna členství ve třídě a obnova. Pseudonym není automaticky anonymní. |
| M4 Úřední evidence: známky či docházka | Ověřená identita, důvěryhodná autorizace, řízený zápis, řešení souběhu, historie oprav a obnovitelné úložiště; retence podle konkrétní agendy. | Podvržený vlastník či známka, odebraný přístup, souběžné úpravy a obnova. Nepřebírej obecnou lhůtu výmazu cvičných dat. |
| M5 Přehledy učitele a exporty | Přístup podle přidělených tříd a účelu; agregace, když stačí; minimum polí a nové ověření oprávnění při stažení. | Cizí třída, prošlý/odvolaný odkaz, vzorce v CSV, prozrazující názvy souborů a životní cyklus stažených kopií. |
| M6 AI tutor | Nejprve zvaž zkontrolovaná statická vysvětlení. Potřebná AI má schválené příjemce, minimální vstup, klíče na serveru a validovaný výstup. | Oprávnění při vyhledávání, skutečně odesílaná data, injekce, výpadek, retence a výmaz u poskytovatele. Samotný výstup modelu nesmí zapsat úřední známku. |

Pro vynucení objektových oprávnění použij [OWASP Authorization](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html). Tabulka a školní příklady jsou doporučením tohoto průvodce; netvrdí, že OWASP uvedené aplikace posuzoval.

### 17.2 Zvol cestu realizace

- **Lokální/statická aktivita:** hodí se bez potřeby sdílené evidence. Prověř místní ukládání, externí součásti a metadata hostingu; samotný offline provoz nedokládá absenci osobních údajů.
- **Existující školní platforma:** využij vhodnou udržovanou identitu, oprávnění a úložiště. Ověř skutečné nastavení, příjemce, exporty a chování výmazu.
- **Vlastní serverová aplikace:** použij udržované součásti pro autentizaci a relace, vynucuj práva na serveru, validuj vstupy a zajisti ochranu úložiště, obnovu a odpovědnost za provoz. PHP se SQLite je jedna možnost; zachovej rovnocennou podporovanou architekturu.
- **Volitelná AI služba:** přidej vymezený datový tok, limity zdrojů, řízené selhání a lidskou kontrolu tam, kde ji vyžadují následky. Výuková aktivita má mít použitelnou náhradu při výpadku.

Pracnost odhaduj až podle prostředí a závislostí. Neslibuj bezpečnost za pevný počet minut ani nevytvářej nový heslový systém, pokud existuje vhodné školní SSO.

### 17.3 Rozpracuj jen zvolený postup

U M1 zmapuj síť a úložiště, odstraň zbytečný sběr, doplň ukončení/reset a prověř dalšího uživatele. U M2 stanov povolená pole, chráněné hranice podání/čtení a odpovědnost za výmaz. U M3 vyřeš identitu a vlastnictví záznamu, následně návrat k práci, odhlášení a odebrání přístupu. U M4 definuj oprávněný zápis, opravy a konflikty před ukládáním a obnovou. U M5 vytvoř omezený dotaz, minimalizuj export a autorizuj stažení. Odpovídající technický modul načítej jen podle potřeby.

U M6 vyřeš potřebnou identitu, vynuť oprávnění před výběrem zdrojů a odesláním modelu, minimalizuj požadavek, ověř odpověď a zobraz ji, případně předej samostatně autorizovaný zápis ke kontrole. Filtrace odpovědi po volání nevrátí již předaná data poskytovateli. Přístup a výmaz zahrnují indexy, cache i souhrny. Při výpadku či nejisté validaci zachovej práci a nabídni srozumitelnou náhradu bez tichého autoritativního zápisu. Podrobnosti řeší oddíl 15 a [OWASP RAG Security](https://cheatsheetseries.owasp.org/cheatsheets/RAG_Security_Cheat_Sheet.html).

### 17.4 Oprav existující aplikaci

Odděl okamžité omezení rizika od trvalé opravy. Navrhni nejmenší účinný zásah, například omezení veřejného exportu či zastavení zbytečného sběru. Odstranění zveřejněného klíče z klienta nestačí: revokaci a rozsah vystavení řeš autorizovaným incidentním postupem. Uveď dotčené uživatele, ověření, zbytkové vystavení a další krok. Potřebné důkazy zachovej bez kopírování citlivých logů do chatu.

Trvalou opravou řeš doloženou hranici identity, oprávnění, úložiště nebo provozu a ponech funkční součásti. Migrace záznamů potřebuje kontrolu integrity, zálohu/obnovu a plán návratu. Návrh opatření neopravňuje vypnout produkci, revokovat přístupy ani rozesílat oznámení. Podezření na zpřístupnění dat předej k posouzení incidentu podle použitelných místních pravidel.

### 17.5 Předej kartu řešení

Úvodní odpověď drž stručnou; rozpracuj jen vybraný režim a relevantní ochrany. Přizpůsob tuto kartu:

```text
Situace a cíl:
Doporučený režim a důvod:
Potřebné údaje a údaje, které nesbírat:
Tok dat, příjemci a místo ukládání:
Identita a oprávnění:
Uchovávání, výmaz a obnova:
Konkrétní kroky realizace:
Kontroly před použitím a skutečný stav provedení:
Zbytková rizika a neověřené předpoklady:
Odpovědná osoba a další rozhodnutí:
```

Odliš plánované a provedené kontroly, u N/A doplň důvod. Používej syntetické příklady bez reálných záznamů žáků. Pro Španělsko použij španělský právní modul; pro EU/ČR použitelný místní rámec. Režim ani jazyk automaticky neurčují jurisdikci.

### 17.6 Začni u existující aplikace

Když uživatel přinese existující aplikaci, nabídni přiměřený vstupní audit a plán nápravy. Využij dodaný kód, architekturu a předchozí nálezy. Pokud už audit zadal, pokračuj v tomto rozsahu bez opakovaného schvalování stejného kroku. Při zadání drobné implementace prověř dotčenou hranici v rámci práce; širší audit nabídni samostatně, pokud jej odůvodňují zjištění.

Nabídni dvě použitelné hloubky: cílenou kontrolu měněné funkce a jejího datového toku, nebo širší přezkum před nasazením zaměřený na identitu, oprávnění, příjemce, retenci a obnovu. Hloubku doporuč podle skutečných následků, například při novém použití reálných dat, úřední evidenci, veřejném exportu, novém AI příjemci či závažném pozorovaném selhání. Chybějící kód nebo nastavení omezuje závěry; vyžádej očištěný kód/konfiguraci či syntetickou ukázku, nikdy produkční databázi nebo tajemství. Samotný screenshot nedokládá zabezpečení serveru.

Nejprve zmapuj současné chování a důkazy, potom předej seřazené nálezy s místem, dotčenými údaji/uživateli, rozlišením pozorovaného selhání a hypotézy, návrhem opravy, pracností/závislostmi a způsobem ověření. Začni doloženým zpřístupněním či ohrožením integrity, potom relevantními nedostatky; volitelná zlepšení označ zvlášť. Uveď i funkční ochrany. Vybranou nápravu rozpracuj kartou řešení a zachovej vhodnou architekturu.

Zadání auditu opravňuje k posouzení, nikoli ke změnám aplikace. Opravy navrhni, pokud implementace již není autorizována; prováděj jen schválený rozsah. U každého bodu rozliš návrh, provedeno bez ověření, ověřeno s konkrétními důkazy a nevyřešeno. Zásahové kontroly prováděj jen v autorizovaném prostředí; bez provedení předej plán. Absence nálezu sama nedokládá bezpečnost aplikace pro reálná data.

© 2026 Luděk Sušický. [MIT](https://opensource.org/license/mit). Revidované vydání verze 1.1 vychází z původního průvodce z října 2026. Zachovej autora, licenci a oznámení úprav.
