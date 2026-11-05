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

© 2026 Luděk Sušický. [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Revidované vydání verze 1.1 vychází z původního průvodce z října 2026. Zachovej autora, licenci a oznámení úprav.
