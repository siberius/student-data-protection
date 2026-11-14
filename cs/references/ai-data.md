# 15. Datové toky AI, tutor a RAG [P/O]

<!-- Generovaná reference; upravuj udržovaného samostatného průvodce. -->

Zdrojové oddíly: 15.

## 15. Datové toky AI, tutor a RAG [P/O]

Použij jen pro implementovanou nebo výslovně zadanou AI funkci. Kvůli této sekci nepřidávej model, vektorovou databázi ani ukládání rozhovorů. Vývojový asistent a žákovská služba mají různé datové toky a potřebují samostatné položky inventáře.

### 15.1 Minimalizace a hranice toku

Pro každý tok eviduj účel, role správce/zpracovatele, schválené zdroje, kategorie údajů, uživatelský přístup, příjemce, region i vzdálenou podporu, smluvní retenci, způsob výmazu a potřebná předávání. Zahrň prompty, odpovědi, přílohy, rozhovory, předávací záznamy, moderaci a podporu, cache, embeddings, vektorové indexy, logy poskytovatele a výstupy nástrojů či konektorů. Odvozená data mohou být osobní i bez jmen; embeddings nejsou zárukou anonymizace.

Před voláním služby vyber jen pole nezbytná pro daný úkol a oprávněného příjemce. Odstraň nesouvisející identifikátory a tajemství. Nepředpokládej, že učitel smí nahrát celou evidenci třídy. Ověř nastavení a podmínky skutečného účtu a endpointu; vypnutý trénink, školní označení či region EU samy neřeší retenci, přístup podpory ani předávání. Nedostupné podmínky zůstávají neověřené; vývoj může pokračovat se syntetickými daty.

Klíče služby drž na serveru. Cílová místa, nástroje a rozsah dat vynucuj mimo prompt. Vstup žáka, načtené dokumenty i výstup jsou nedůvěryhodné. Dokument ani odpověď nesmí měnit role, volat libovolné URL či odesílat evidenci novému příjemci. U načítání zdrojů omez cíle a prověř podvržení serverových požadavků a odtok dat. Strukturovaný výstup ověř před změnou záznamu a text bezpečně vykresluj.

### 15.2 Oprávnění v celém vyhledávání

Dokumenty, chunky, embeddings a souhrny propoj se zdrojem, školou, příslušnými právy osob/skupin, verzí obsahu a retenční kategorií. Oprávnění vynucuj před vyhledáváním i před vydáním výsledku; podobnost není oprávnění. Sdílený index potřebuje vynucenou izolaci škol. Filtruj hledání, počty, citace, náhledy, exporty i opakované použití rozhovoru, nejen finální odpověď. Odebrání přístupu či výmaz zneplatní související cache a odvozené kopie ve vymezené lhůtě; do potvrzení zneplatnění dotčené výsledky blokuj, pokud by se vydaly podle známého zastaralého oprávnění.

Zachovej původ zdroje a odliš citaci, interpretaci a nepodložené tvrzení. Testuj cizí školu pomocí syntetického rozlišitelného textu i změnu role po indexaci. Smyšlená citace není doklad správnosti. Odděl načtený obsah a ověřuj akce; pokyn ignorovat škodlivé instrukce není dostatečná izolace.

### 15.3 Evidence učení a výmaz

Pro pokračování ukládej jen cíl, potřebné odkazy na úlohy, vyjádřenou odpověď a argumentaci, podmínky pomoci, pozorované revize a další krok nezbytný pro účel. Neodvozuj a nearchivuj diagnózy, osobnost ani soukromé myšlenkové pochody. Souhrn uvažování může být osobní údaj. Platí pro něj stejná oprávnění, informování a účelová retence jako pro aktivitu; na sdíleném zařízení zajisti srozumitelné ukončení a vyčištění.

Výmaz a opravu mapuj do zdrojů, chunků, indexů, souhrnů, exportovaných záznamů, front, záloh a kopií u poskytovatele. Uveď přímý výmaz, nutnou žádost poskytovateli a kopie uchované po odůvodněnou omezenou dobu. Kde výmaz zdroje či práva zneplatní výsledek, pozastav vyhledávání. Zabraň nové indexaci ze zastaralé fronty či zálohy. Neslibuj okamžitý výmaz neměnných záloh ani cizích systémů bez důkazu. Pokud lze, prověř skutečný postup poskytovatele syntetickými daty; nepředpokládej odstranění všech kopií pouhým odesláním žádosti API.

Při výpadku nebo neplatném výstupu zachovej práci a označ hodnocení jako nerozhodnuté. Timeout není plný počet bodů; nevymýšlej hodnocení ani potichu neměň poskytovatele. Významné posouzení vyžaduje odpovídající odpovědný lidský přezkum.

Technické vodítko: [OWASP RAG Security](https://cheatsheetseries.owasp.org/cheatsheets/RAG_Security_Cheat_Sheet.html). Jde o implementační ochrany; nenahrazují právní klasifikaci ani posouzení poskytovatele.

### 15.4 Architektonické podmínky pro lokální vs. nelokální modely AI a k-anonymita [P/Z]

Pokud záměr tvůrce (návrh projektu nebo nová funkce) směřuje k zapojení AI modelu, nejprve rozliš, zda model běží **lokálně v perimetru správce (L0)**, nebo jde o **nelokální (cloudový/externí) model (C1/C2)**. U nelokálního modelu tvůrce vždy proaktivně upozorni, že před odesláním dat mimo školu je nutné v aplikaci vytvořit transformační mezivrstvu:

| Architektonický režim AI | Charakteristika toku | Povinné podmínky přípravy dat v aplikaci [P] |
|---|---|---|
| **L0: Lokální / In-Browser AI** (lokální model na školním serveru či v prohlížeči bez telemetrie) | Data neopouštějí zařízení nebo server školy; žádný externí příjemce. | Nevyžaduje externí k-anonymitu ani smlouvu dle čl. 28 GDPR. Zajisti lokální oprávnění (sekce 6) a vyčištění paměti/cache na sdíleném zařízení po odhlášení (sekce 9). |
| **C1: Nelokální AI - Individuální interakce (1:1)** (zpětná vazba k úloze jednoho žáka) | Dotaz se týká jednotlivce; matematickou k-anonymitu nelze na jediný izolovaný záznam aplikovat. | Vytvoř **lokální pseudonymizační bránu** (EDPB 01/2025): 1. Odstraň přímé identifikátory (, , , ). 2. Mapovací tabulku () drž výhradně v lokální DB školy mimo dosah AI poskytovatele. 3. Volný text žáka očisti od PII (redakce jmen, kontaktů a názvu školy). 4. Použij bezestavové volání s ověřenou retencí u poskytovatele. |
| **C2: Nelokální AI - Skupinová / třídní analytika a exporty (1:N)** (rozbor výsledků třídy, hledání trendů, RAG nad více žáky) | Do modelu odchází soubor záznamů více žáků. V malé třídě prostá pseudonymizace () selhává. | Vytvoř **agregační nebo k-anonymizační pipeline** (EDPB 02/2026, AEPD): 1. Preferuj odeslání pouze **agregovaných souhrnů** (průměry, četnosti chyb bez řádkových záznamů jednotlivců). 2. Pokud účel vyžaduje řádková mikrodata, vynuť **k-anonymitu ( různých osob)** a **l-diverzitu ( různých hodnot citlivého atributu)** v každé třídě ekvivalence. |

#### Pravidla pro vytvoření k-anonymizační pipeline u nelokální AI a exportů (Režim C2 a M5)

1. **Klasifikace polí před transformací:** Přímé identifikátory (, , , , , , , ) bezvýjimečně odstraň (nepoužívej prostý hash, který zůstává osobním údajem a umožňuje propojení záznamů). Na kvazi-identifikátory (, , , , , ) aplikuj **generalizaci** (např.  -> ;  -> ;  -> ). U citlivých a cílových atributů (, , , ) kontroluj diverzitu hodnot ve skupině.
2. **Proti vyčlenění (No Record Isolation -> k-anonymita):** Seskup záznamy podle všech přítomných kvazi-identifikátorů. Každá skupina (třída ekvivalence) MUSÍ obsahovat záznamy alespoň **5 různých fyzických osob ( počítáno přes )**. Pokud má žák v tabulce více řádků (časová řada pokusů), 5 řádků téhož žáka NENÍ . Skupiny s  dále generalizuj nebo trvale odstraň (**suprese záznamu / record suppression**).
3. **Proti propojení (No Linkage):** Před exportem náhodně promíchej pořadí řádků (**shuffling**), aby pořadí neodpovídalo abecednímu seznamu v třídním výkazu. U přehledových tabulek se součty aplikuj **komplementární supresi** (PTAC), aby potlačenou buňku s  nebylo možné dopočítat odečtením od řádkového či sloupcového součtu.
4. **Proti odvození (No Inference -> l-diverzita):** Pokud všichni žáci ve stejné třídě ekvivalence sdílejí tutéž citlivou hodnotu (, např. všichni mají známku 5 nebo stejné SVP), dochází k prozrazení citlivého údaje útokem homogenitou. Vynuť alespoň ** různé hodnoty** cílového atributu v každé skupině, jinak skupinu sluč s širší kategorií nebo potlač.
5. **Právní hranice (Perspektiva zpracovatele dle EDPB 02/2026 a Stanoviska 28/2024):** [Z] Pokud poskytovatel nelokální AI zpracovává data jménem školy (zpracovatel dle čl. 28 GDPR) a škola drží původní identifikované záznamy, posuzuje se povaha dat z perspektivy správce. Ani technická k-anonymita na straně školy nesnímá povinnost mít uzavřenou zpracovatelskou smlouvu a prověřit soulad s věkovými limity (např. v ČR 15 let pro samostatný digitální souhlas; podmínky OpenAI a Google od 13 let se souhlasem zástupce). K-anonymita slouží jako zásadní technické opatření minimalizace dopadu (čl. 25 a 32 GDPR).

© 2026 Luděk Sušický. [MIT](https://opensource.org/license/mit). Revidované vydání verze 1.2 vychází z původního průvodce z října 2026. Zachovej autora, licenci a oznámení úprav.
