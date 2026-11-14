# 2. GDPR a český právní rámec

<!-- Generovaná reference; upravuj udržovaného samostatného průvodce. -->

Zdrojové oddíly: 2.

## 2. GDPR a český právní rámec

### 2.1 Co je a není osobní údaj

[Z] Jméno spojené s docházkou, kontaktem, zprávou, výsledkem, třídou či známkou je osobní údaj. Náhodné ID, hash jména nebo zašifrovaný záznam zpravidla zůstávají osobními údaji, pokud lze osobu znovu určit. Pseudonymizace není anonymizace. Známky samy o sobě nejsou automaticky zvláštní kategorií podle čl. 9; diagnózy, zdravotní omezení či některé biometrické údaje mohou být. Výchozí profil jejich sběr vypíná; případnou nezbytnou funkci řeš odděleným posouzením a užšími oprávněními. U zvláštních kategorií dolož kromě titulu podle čl. 6 také použitelnou výjimku podle čl. 9 odst. 2. Viz [GDPR](https://eur-lex.europa.eu/eli/reg/2016/679/oj/ces) a [výklad Evropské komise k osobním údajům](https://commission.europa.eu/law/law-topic/data-protection/data-protection-explained_en).

### 2.2 Rozhodnutí školy a dodavatele

| Oblast | Povinnost / rozhodnutí a požadovaný důkaz |
|---|---|
| Účel a titul | [Z] Pro každý účel určete titul dle čl. 6, nezbytná data a dobu uchování. U školních úkolů typicky čl. 6 odst. 1 písm. c) nebo e), s konkrétní oporou a posouzením nezbytnosti. § 28 školského zákona není plošné oprávnění ukládat libovolnou telemetrii. |
| Souhlas | [Z] Nevyžadujte automaticky souhlas rodičů pro povinnou výuku. Kde se skutečně opíráte o souhlas, musí být svobodný, konkrétní a odvolatelný. Česká hranice 15 let pro čl. 8 se týká souhlasu u přímo nabízených služeb informační společnosti, nikoli všech školních zpracování. |
| Odpovědnost | [Z] Škola bývá správcem, poskytovatel hostované aplikace zpracovatelem. Rozhoduje skutečná role; dodavatel pouze předávající software bez přístupu k datům nemusí být zpracovatel. |
| Smlouvy a přístupy | [Z] U zpracovatele smlouva dle čl. 28: pokyny, mlčenlivost, zabezpečení, další zpracovatelé, pomoc s právy a incidenty, vrácení/výmaz a možnost ověření. Evidujte i monitoring, podporu a poskytovatele AI. |
| Evidence a pověřenec | [Z] Veďte odpovídající záznamy dle čl. 30; pravidelné školní zpracování není automaticky osvobozeno hranicí 250 zaměstnanců. Zapojte pověřence dle čl. 37; české školy rozhodující o právech a povinnostech mají specifické postavení orgánu veřejné moci. |
| Posouzení rizik | [Z] Zabezpečení odpovídá riziku dle čl. 32; soukromí navrhujte od začátku dle čl. 25. Posuďte nutnost DPIA dle čl. 35, zvláště u dětí, hodnocení, monitorování a profilování. |

Prameny k tabulce: [ÚOOÚ: školství](https://uoou.gov.cz/profesional/qa-otazky-a-odpovedi/skolstvi), [školský zákon č. 561/2004 Sb., zejména § 28](https://e-sbirka.gov.cz/sb/2004/561), [zákon č. 110/2019 Sb.](https://e-sbirka.gov.cz/sb/2019/110), [ÚOOÚ: základní příručka](https://uoou.gov.cz/verejnost/zakladni-prirucka-k-ochrane-udaju), [EDPB: správce a zpracovatel](https://www.edpb.europa.eu/sme/learn-the-basics/data-controller-or-data-processor_en), [EDPB: soulad a DPIA](https://www.edpb.europa.eu/sme/be-compliant/be-compliant_en).

[O] Nevyvozuj automatickou výjimku z DPIA jen z § 10 zákona č. 110/2019 Sb. nebo z toho, že jde o školu. Zohledni čl. 35 odst. 10 GDPR, konkrétní operace a aktuální seznamy ÚOOÚ. Při vysokém zbytkovém riziku řeš předchozí konzultaci podle čl. 36. Viz [ÚOOÚ: DPIA a vztah české úpravy ke GDPR](https://uoou.gov.cz/profesional/qa-otazky-a-odpovedi/posouzeni-vlivu-na-ochranu-osobnich-udaju).

### 2.3 Informování, práva a předávání

[Z] Připrav srozumitelnou informaci dle čl. 12–14: správce/pověřenec, účely a tituly, příjemci, předávání, retence, práva, stížnost a relevantní automatizované rozhodování. Zajisti přístup, opravu, omezení a další použitelná práva; výmaz není absolutní. Přenositelnost se nevztahuje automaticky na každé školní zpracování. Identitu žadatele ověř přiměřeně, bez plošného sběru kopií dokladů. Výchozí lhůta vyřízení je jeden měsíc; zákonné prodloužení vyžaduje podmínky a včasné informování. Čl. 22 posuzuj u výhradně automatizovaných rozhodnutí s právním nebo obdobně významným účinkem, i bez AI. Formální kliknutí učitele není smysluplný lidský přezkum. [GDPR, čl. 12–22](https://eur-lex.europa.eu/eli/reg/2016/679/oj/ces).

[Z] GDPR obecně nenařizuje výhradně český ani unijní hosting. Předávání mimo EHP vyhodnoť podle kapitoly V, včetně vzdálené podpory a subdodavatelů. [P] Výchozí profil používá EHP hosting i zálohy; odchylku dolož použitelným mechanismem, případným posouzením předání a doplňkovými opatřeními. ÚOOÚ/EDPB metodiky jsou výkladové podklady, nikoli samostatná certifikace výrobku. [EDPB: role a mezinárodní předávání](https://www.edpb.europa.eu/sme/learn-the-basics/data-controller-or-data-processor_en).


### 2.4 Srovnávací přehled národních jurisdikcí a věkových hranic [Z/P]

Při návrhu školní aplikace nebo integraci AI modelu vždy ověř skutečnou jurisdikci školy a cílové skupiny žáků. Jazyk rozhraní sám o sobě neurčuje použitelné národní právo. GDPR v čl. 8 dává členským státům možnost upravit věkovou hranici pro samostatný digitální souhlas dětí v rozmezí 13 až 16 let; školské zákony a postoje národních dozorových úřadů k externím cloudům a AI se v jednotlivých zemích výrazně liší:

| Stát / jurisdikce | Věk dle čl. 8 GDPR | Dozorový úřad | Školský předpis a specifické omezení cloudu/AI |
|---|---|---|---|
| **Česko (CZ)** | 15 let (zákon č. 110/2019 Sb.) | ÚOOÚ | Školský zákon č. 561/2004 Sb. (§ 28); opatrný a pragmatický přístup k licencovaným cloudům; metodiky MŠMT a NPI ČR (AIDIG). |
| **Španělsko (ES)** | 14 let (LOPDGDD čl. 7) | AEPD + autonomní úřady | LOE (DA 23); detailní metodiky AEPD ke k-anonymitě a povinnost jmenovat DPD ve školách (čl. 34.1.b LOPDGDD). |
| **Německo (DE)** | 16 let (BDSG § 16) | DSK + 16 zemských úřadů (LfDI, BayLDA, LDI) | 16 zemských školských zákonů; striktní zákaz nebo omezení komerčních US cloudů (M365, Google) a telemetrie; povinná DSFA (DPIA) pro školní AI. |
| **Francie (FR)** | 15 let (Loi Informatique et Libertés) | CNIL | Code de l'éducation; státní platformy ENT; ministerský zákaz bezplatných verzí US cloudů; metodika CNIL zakazující sdílené účty odhalující identitu v promptech. |
| **Polsko (PL)** | 16 let (Ustawa o ODO 2018) | UODO | Prawo oświatowe; odpovědnost ředitele školy jako správce; zákaz vkládání údajů do AI bez smlouvy dle čl. 28 GDPR; judikatorní zákaz biometrie ve školách. |
| **Ukrajina (UA)** | 14-18 let (částečná způsobilost dle OZ) | Ombudsman Ukrajiny (Уповноважений) | Zákon č. 2297-VI a chystaná plná harmonizace s GDPR (návrh č. 8153); státní ekosystém Mrija (Мрія); u žáků v EU platí plné GDPR a Lex Ukrajina. |

#### Pravidla pro přeshraniční a specifické nasazení

1. **Německý kontext (Striktní lokální režim):** [Z] Pokud aplikace míří do německých škol, předpokládej věk souhlasu 16 let a plnou decentralizaci podle 16 zemských zákonů. Z důvodu usnesení DSK k Microsoft 365 a Copilotu preferuj čistě lokální zpracování (L0) na školním serveru nebo open-source stacku (Moodle, IServ). Jakýkoli odchod dat mimo školu vyžaduje detailní posouzení DSFA a vyloučení telemetrie.
2. **Francouzský kontext (Suverenita a ochrana před de-anonymizací):** [Z] Ve francouzských školách respektuj věkovou hranici 15 let a ministerská doporučení k platformám ENT. Při integraci AI dbej na metodiku CNIL: nepoužívej společné účty třídy, do nichž žáci vkládají prompty obsahující nepřímé identifikátory, a zajisti, aby hodnocení žáka nebylo svěřeno výstupu modelu bez učitele.
3. **Polský kontext (Odpovědnost správce a zákaz biometrie):** [Z] V Polsku nese plnou odpovědnost škola zastoupená ředitelem (ADO). Učitel nesmí samostatně registrovat žáky do nástrojů AI bez formální smlouvy o pověření zpracování (umowa powierzenia dle čl. 28 GDPR). Respektuj věkovou hranici 16 let a zákaz jakékoli biometrické identifikace dětí (včetně docházky a jídelen).
4. **Ukrajinský kontext (Integrace v EU a eurointegrační standardy):** [Z] Pro ukrajinské žáky integrované v českých, polských či jiných evropských školách platí v plném rozsahu unijní GDPR a místní právní předpisy (v ČR zákon Lex Ukrajina). Pro aplikace vyvíjené přímo pro ukrajinské vzdělávací prostředí zohledni chystaný evropský zákon č. 8153, platformu Mrija a povinné znečitelnění (zneosoblenňa) žákovských dat před předáním modelům AI.

© 2026 Luděk Sušický. [MIT](https://opensource.org/license/mit). Revidované vydání verze 1.2 vychází z původního průvodce z října 2026. Zachovej autora, licenci a oznámení úprav.
