# 18. Publikování, dokumenty a odvozené výstupy [D/O]

<!-- Generovaná reference; upravuj udržovaného samostatného průvodce. -->

Zdrojové oddíly: 18.

## 18. Publikování, dokumenty a odvozené výstupy [D/O]

### 18.1 Zmapuj skutečnou hranici publikování

Modul načti pro portály, portfolia, veřejné ukázky, generované weby, importy dokumentů či exporty. Porovnej aktuální kód, příkazy sestavení a konfiguraci nasazení s dokumentací; aplikace popsaná jako lokální už může publikovat na hosting. Kvůli průzkumu automaticky nespouštěj sestavení ani nasazení: mohou kopírovat reálné záznamy, odesílat data či vytvořit veřejný výstup.

Sleduj relevantní cestu od zdroje přes úpravy k příjemcům: záznamy, přílohy, OCR, pracovní poznámky, generované HTML/JSON, vyhledávací indexy, náhledy, PDF, screenshoty, balíčky, cache hostingu/CDN a starší vydání. Zahrň logy sestavení a výstupy CI, pokud mohou obsahovat osobní údaje. Výstup je kopií dat, i když se nenasazuje databáze. U každého určuj publikum: soukromý pracovní podklad, přístup ověřených školních uživatelů, nebo veřejné zveřejnění. Přístup učitele ke zdroji sám neopravňuje jeho zveřejnění.

### 18.2 Sestav výslovně povolený publikační výstup

Pracovní záznamy odděl od zveřejnitelných polí a souborů. Veřejnou konfiguraci a export sestav z povoleného seznamu pro určené publikum a účel; samotné vyloučení hesla může odhalit budoucí interní pole. Neznámá pole ponech vyloučená do posouzení. Surové zdroje drž mimo veřejný adresář. Vybraný výstup ukaž v náhledu bez nahrávání skutečných záznamů do cizí náhledové služby.

Pro zveřejňovanou položku uchovej minimální interní záznam rozhodnutí: zdroj/verzi, vybraná pole, publikum, odpovědné rozhodnutí, použitelný titul či jiné odůvodnění a podnět k přezkumu/stažení. Přepínač publikování ani souhlas tvůrce nedokládají vyřešení práv všech dotčených osob a právních podmínek. Nevyžaduj nové ruční schválení každé běžné změny již pokryté platným rozhodnutím; znovu posuzuj podstatnou změnu obsahu, publika, účelu či příjemců. Samotný registr rozhodnutí s citlivými úryvky neexportuj.

### 18.3 Prověř volný text, média a importy

Vedle strukturovaných polí posuzuj komentáře, práce žáků, OCR, názvy souborů, URL, metadata obrázků a vložený obsah. Dokument může uvádět sourozence, rodiče, spolužáky či zaměstnance; určuj, čí údaje jsou potřebné. V distribuované kopii proveď nevratné začernění/odstranění a prověř skrytý text, vrstvy, OCR i původní přílohy. Omezeně přístupný originál ponech jen s odůvodněním. Stejně posuzuj přístupné alternativní texty a popisky.

Detektory slov, přibližná data a klasifikátory AI mohou upozornit k přezkumu; absence hlášení nedokládá bezpečnost a nález není diagnóza. Genealogické pravidlo typu „stačí jméno a rok narození“ nepřenášej jako obecnou školní publikační politiku. Omez citlivé úryvky ve výstupech kontrol, úkolech a logách.

CSV, JSON, GEDCOM, dokumenty a archivy považuj za nedůvěryhodná data. Použij vhodný parser a validuj schéma, typy, limity velikosti/počtu, kódování a odkazy mezi záznamy. U archivů omez rozbalenou velikost a cesty. Dodaný soubor Python/JavaScript nespouštěj jako datový import. Důvěryhodný projektový kód má jinou hranici; bez důkazů jej nenahrazuj. Odděl náhled importu, opravy a autorizované převzetí do úřední evidence. Tato opatření doplňuje [OWASP File Upload](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html).

### 18.4 Zachovej původ údajů bez nálepkování žáka

Kde importovaný či AI vytěžený údaj může ovlivnit člověka, eviduj zdroj, relevantní verzi/datum, stav ověření a odpovědnost za opravu. Rozliš podané tvrzení, ověřený záznam, přepis, interpretaci a nevyřešený rozpor. Druhý převzatý zdroj může mít stejný původ a není nezávislým potvrzením. Návrh AI ani pravděpodobná shoda nesmějí potichu sloučit osoby či vytvořit úřední známku, diagnózu nebo trvalou nálepku schopností. Potřebná historie oprav má vlastní oprávnění a retenci.

### 18.5 Prověř přístup a externí příjemce

Chraň shodně HTML, obrázky, surové soubory, JSON a části vyhledávacího indexu včetně přímých URL, alternativních adres hostingu a náhledových nasazení, pokud existují. Skrytý odkaz, noindex ani vyhledávání v prohlížeči neomezují přístup. Urči, zda hosting, mapy, fonty, analytika a podpora dostávají požadavky nebo údaje. Požadavek na cizí mapové dlaždice může odhalit metadata návštěvníka a zobrazovaná území; před tvrzením o odeslání jména či záznamu prověř skutečné chování.

Otisk společné odpovědi uložený v cookie zůstává sdíleným přístupovým údajem. Hash sám neověřuje jednotlivce ani neumožňuje individuálně odebrat přístup. Autentizaci, délku relace a revokaci přizpůsob údajům; pro osobní evidenci použij modul identity. Viz [OWASP Session Management](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html). Skutečně veřejná aktivita bez osobních údajů automaticky nepotřebuje účty.

### 18.6 Prověř vydání a cestu odstranění

Doporuč kontrolu vydání přiměřenou riziku: porovnej skutečný kandidátní výstup s povoleným obsahem, prověř přidaná/změněná/odstraněná osobní pole a soubory a označ citlivé nálezy či neposouzené výstupy. Kontrola uvádí pokrytí a rozlišuje upozornění od podmínky bránící publikaci přijaté pro daný projekt. Úspěšné sestavení tuto kontrolu nenahrazuje. Nevyřešené oprávnění nebo známé nechtěné zpřístupnění brání dotčené osobní publikaci; ostatní autorizovaná práce může pokračovat.

Naplánuj odstranění z aktivního HTML, veřejných složek, indexů, exportů a cache. Kopírovací smyčka, která jen přidává soubory, může zachovat stažený obsah. Použij manifest či čisté pracovní sestavení; odstraňuj jen potvrzeně nepotřebné generované soubory, nikdy zdrojové záznamy a cizí uživatelské soubory. Prověř, že obnova či další sestavení obsah znovu nezveřejní. Starší URL, retence hostingu a stažené kopie mají výslovné limity; bez důkazů neslibuj vzdálený výmaz. Návrat obnovuje autorizované vydání, jehož publikační rozhodnutí ještě musejí platit.

Před aktualizací šablony/skillu porovnej verze a místní změny, zálohuj dotčené soubory a připrav obnovu. Zachovej záznamy i přístupové ochrany daného nasazení. Aktualizace šablony neopravňuje k instalaci, platbám či publikaci. Pozorované chování po aktualizaci odliš od plánovaných kontrol.

### 18.7 Předání a očištěná zpětná vazba

Do karty řešení doplň jen potřebný přehled výstupů, povolený publikační obsah, stav přezkumu, limity odstranění a odpovědný další krok. Report má vést k proveditelné nápravě a pojmenovat neprozkoumané výstupy. Pro návrh kontroly úniku do indexu nebo výmazu používej syntetické rozlišitelné značky, nikoli skutečné údaje žáků v důkazech testu.

Zpětná vazba pro správce skillu obsahuje nástroj/verzi, syntetickou reprodukci, očekávané a pozorované chování a obecnou opravu. Odstraň identifikátory, tajemství i nepřímá vodítka; nepřikládej produkční logy, rodinné záznamy, skeny ani školní databáze. Očištěný obsah ukaž před případným samostatně autorizovaným odesláním. Zpětná vazba je volitelná a neposílá se automaticky.

© 2026 Luděk Sušický. [MIT](https://opensource.org/license/mit). Revidované vydání verze 1.1 vychází z původního průvodce z října 2026; zachovej autora, licenci a oznámení úprav. Externí zdroje mají vlastní práva.

## License / Licence

MIT License

Copyright (c) 2026 Luděk Sušický

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

© 2026 Luděk Sušický. [MIT](https://opensource.org/license/mit). Revidované vydání verze 1.1 vychází z původního průvodce z října 2026. Zachovej autora, licenci a oznámení úprav.
