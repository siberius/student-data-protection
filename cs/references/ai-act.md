# 3. AI Act: použitelnost, klasifikace a termíny

<!-- Generovaná reference; upravuj udržovaného samostatného průvodce. -->

Zdrojové oddíly: 3.

## 3. AI Act: použitelnost, klasifikace a termíny

### 3.1 Odděl vývojový nástroj od produktu

- **Aplikace napsaná s pomocí AI:** sama tím není AI systémem. Ukládání formulářů, evidence docházky, filtrování záznamů nebo pevný výpočet bodů obvykle představují běžné deterministické zpracování. Posuzuj skutečnou definici čl. 3 odst. 1, nikoli marketingový název.
- **Vývojář používající AI asistenta:** organizace může být zavádějícím subjektem tohoto asistenta. Povinnosti se hodnotí pro jeho použití; automaticky se nepřenášejí na dodanou aplikaci bez AI funkcí.
- **AI funkcionalita v aplikaci:** generování zpětné vazby, vyhodnocování volných odpovědí, predikce výkonu, personalizace podle výsledků nebo dohled nad testem vyžadují samostatné posouzení. AI může být externí API i interní dávkový proces, nejen chatbot v UI.

[P] Veď inventář: funkce, účel, model/verze, vstupy, výstupy, příjemci, vliv na žáka, poskytovatel, zavádějící subjekt, GDPR titul, klasifikace a datum přezkumu. Změna účelu nebo podstatná úprava může změnit role podle čl. 25. [AI Act: oficiální předpis](https://eur-lex.europa.eu/eli/reg/2024/1689/oj/ces), [Komise: orientace v AI Actu](https://digital-strategy.ec.europa.eu/en/faqs/navigating-ai-act).

### 3.2 Článek 4: AI gramotnost

[Z/O] Kapitola I se používá od 2. 2. 2025. Aktuálně zobrazené znění čl. 4 na AI Act Service Desk po novele z července 2026 ukládá poskytovatelům a zavádějícím subjektům přijímat opatření podporující rozvoj AI gramotnosti; výslovně nevyžaduje garantovat určitou úroveň každého jednotlivce. Nelze tvrdit, že povinnost zcela zmizela, ani bez ověření opakovat původní formulaci jako aktuální.

[P] Zajisti přiměřené školení podle rolí: omyly modelu, ochrana dat, předsudky, prompt injection, ověřování výstupů, lidský dohled a hlášení problémů. Eviduj obsah, datum a účast; skill nevyžaduje konkrétní certifikát. Platí i pro personál používající vývojový AI nástroj, pokud spadá do dotčené role. [Čl. 4: aktuální zobrazení Komise](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-4).

### 3.3 Článek 5: zakázané praktiky

[Z] Pro školní aplikaci prověř zejména zákaz AI odvozování emocí ve vzdělávacích institucích s úzkou výjimkou pro zdravotní nebo bezpečnostní důvody. Běžný dohled nad pozorností či podváděním tuto výjimku automaticky nesplňuje. Prověř také škodlivou manipulaci, zneužití zranitelnosti z důvodu věku, zakázané sociální skórování a citlivou biometrickou kategorizaci. U každého zákazu respektuj všechny jeho podmínky; obyčejný školní evidenční údaj nebo bodový výsledek není sám o sobě zakázané sociální skóre.

[P] Tento profil nepovoluje rozpoznávání emocí, biometrickou kategorizaci ani kamerové AI sledování žáků. Novela uvádí také nové zákazy některých intimních syntetických materiálů a materiálů sexuálního zneužívání dětí s použitelností od 2. 12. 2026; zde takové funkce vůbec nevytvářej. Zákazy nenahrazuje souhlas rodiče ani učitele. [Čl. 5](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-5), [čl. 113](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-113).

### 3.4 Příloha III bod 3: vzdělávání a vysoce rizikové AI

[Z] Posuzuj AI určenou pro přijímání/přístup či přiřazování do vzdělávacích institucí, vyhodnocování výsledků učení včetně řízení vzdělávacího procesu, určování vhodné úrovně vzdělání a sledování/detekci zakázaného chování během testů. AI návrh známky může spadat do této oblasti, i když jej učitel následně schválí. Samotné použití AI ve škole nestačí ke klasifikaci high-risk. [Příloha III](https://ai-act-service-desk.ec.europa.eu/en/ai-act/annex-3).

[Z] Výjimka čl. 6 odst. 3 vyžaduje absenci významného rizika pro zdraví, bezpečnost nebo základní práva, včetně neovlivnění podstatně výsledku rozhodování, a odpovídající podmínku: úzký procesní úkol; zlepšení výsledku již dokončené lidské činnosti; detekci vzorců/odchylek bez nepřípustného nahrazení nebo ovlivnění lidského posouzení; nebo přípravný úkol. Není to automatická výjimka „učitel zůstává v procesu“. Systém z přílohy III provádějící profilování fyzických osob je vždy high-risk. Závěr o výjimce poskytovatel zdokumentuje před uvedením na trh/do provozu. [Čl. 6](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-6).

[O] Registrace výjimek: ověř čl. 49 odst. 2 v účinném znění. Při kontrole zdrojů čl. 6 a 49 na Service Desk stále uváděly registraci, zatímco oznámení Komise o novele hovořilo o jejím zjednodušení. Tento rozpor neopravňoval tvrdit úplné zrušení registrace. [Čl. 49](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-49), [oznámení Komise o novele](https://digital-strategy.ec.europa.eu/en/news/ai-omnibus-enters-force).

[P] Generování obecné otázky bez údajů žáka a bez hodnocení je zpravidla jiné riziko než AI známkování konkrétního dítěte. U druhého případu zapoj pověřence a odborné právní posouzení před produkcí; zdokumentuj účel, dopad a skutečný lidský dohled.

### 3.5 Povinnosti při skutečném high-risk použití

[Z/O] Podle role a data použitelnosti připrav řízení rizik, správu dat, technickou dokumentaci, logování, dohled člověka, přesnost, odolnost a kybernetickou bezpečnost; u poskytovatele také systém řízení kvality, příslušné posouzení shody, prohlášení, označení a registraci. Běžný checklist tohoto skillu toto posouzení nenahrazuje. [AI Act: přehled Komise](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai).

Zavádějící subjekt musí odpovídajícím způsobem používat návod, zajistit kompetentní dohled, sledovat provoz a řešit incidenty. Automatické logy pod jeho kontrolou mají zvláštní pravidlo přiměřené doby nejméně šesti měsíců, nestanoví-li použitelný unijní či národní předpis jinak. Nezaměňuj je se všemi běžnými webovými logy. [Čl. 26](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-26).

U veřejnoprávních subjektů a soukromých poskytovatelů veřejných služeb posuď FRIA podle čl. 27; u školy může být relevantní. FRIA a GDPR DPIA mají rozdílný rozsah, lze je koordinovat. Ověř též informování dotčených osob a použitelnost čl. 50 u AI interakce či generovaného obsahu. [Čl. 27](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-27), [Komise: FAQ](https://digital-strategy.ec.europa.eu/en/faqs/navigating-ai-act).

### 3.6 Časová osa a míra právního ověření

| Datum | Význam pro posouzení |
|---|---|
| 1. 8. 2024 | Vstup původního AI Actu v platnost. |
| 2. 2. 2025 | Použitelnost kapitol I a II, tedy mj. čl. 4 a původních zákazů čl. 5. |
| 2. 8. 2025 | Použitelnost vybraných částí včetně GPAI a správy/dozoru; zohledni přechodná ustanovení pro starší modely. |
| 27. 7. 2026 | Komise uvádí vstup Digital Omnibus on AI v platnost. |
| 2. 8. 2026 | Obecné datum použitelnosti s výjimkami; nepovažuj je již za univerzální termín všech high-risk povinností. |
| 2. 12. 2026 | Nové zákazy podle změněného čl. 113 písm. a); zvláštní přechody transparentnosti ověř podle konkrétního systému. |
| 2. 12. 2027 | Změněný čl. 113 uvádí kapitolu III oddíly 1–3, s výjimkou čl. 6 odst. 5, pro čl. 6 odst. 2 / přílohu III. |
| 2. 8. 2028 | Odpovídající termín pro čl. 6 odst. 1 / přílohu I. |

Zdroje: [čl. 113 na Service Desk](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-113), [oznámení Komise z 27. 7. 2026](https://digital-strategy.ec.europa.eu/en/news/ai-omnibus-enters-force), [implementační harmonogram Komise](https://ai-act-service-desk.ec.europa.eu/en/ai-act/eu-ai-act-implementation-timeline). Původní termíny 2. 8. 2026 pro přílohu III a 2. 8. 2027 pro produktové systémy nepřebírej bez kontroly novely. Pro již zavedené systémy posuď čl. 111 individuálně; nevyvozuj univerzální „grandfathering“.

**Omezení ověření:** při přípravě byl čitelný oficiální Service Desk Komise, který uvádí konsolidaci k 27. 7. 2026, a oficiální zpráva o novele. Přímý EUR-Lex při načítání původních i novelizovaných textů vracel anti-bot stránku. Harmonogram a novelizovaný čl. 4 jsou proto ověřeny na oficiálním webu Komise, nikoli nezávislým přečtením úplného Úředního věstníku. Komise odkazuje na [nařízení (EU) 2026/1744](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202601744) a [konsolidaci AI Actu k 27. 7. 2026](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02024R1689-20260727). Před právně významným nasazením potvrď tato znění, datum použitelnosti konkrétní povinnosti, přechody a aktuální české určení příslušných orgánů. Není správné automaticky označit ÚOOÚ za jediného dozorce AI Actu. GDPR platí nezávisle na odkladu high-risk pravidel.

© 2026 Luděk Sušický. [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Revidované vydání verze 1.1 vychází z původního průvodce z října 2026. Zachovej autora, licenci a oznámení úprav.
