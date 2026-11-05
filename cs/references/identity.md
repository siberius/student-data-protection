# 5. Autentizace, volitelné pozvánky a session [P]

<!-- Generovaná reference; upravuj udržovaného samostatného průvodce. -->

Zdrojové oddíly: 5, 6.

## 5. Autentizace, volitelné pozvánky a session [P]

### Volba přístupového režimu

Pro dlouhodobé osobní evidence, komunikaci a historii použij individuální ověřený účet (např. školní SSO nebo passkey). Nabídni bezpečnou obnovu a rušení účtů; nepředpokládej, že každý žák musí mít heslo. Pro rodiče ověř účet i aktuální oprávnění vůči konkrétnímu dítěti. Jednorázový formulář bez účtu smí pouze přijmout vymezené podání; potvrzení podání nesmí odhalit evidované údaje.

Oddíly 5.1 a 5.2 platí **pouze při použití vstupních kódů nebo QR**. Nejsou důvodem zavádět je do aplikace. Oddíl 5.3 platí pro všechny webové session.

### 5.1 Čtyřmístný kód je pouze vstupenka do místnosti

Čtyři číslice mají 10 000 kombinací, přibližně 13,3 bitu entropie. Kód NESMÍ odemykat historii, seznam třídy, známky, učitelské rozhraní ani převzít existující osobní záznam.

1. Kód generuj CSPRNG s rovnoměrným výběrem, včetně počátečních nul. Omez jeho hledání na školu/místnost; zabraň kolizím aktivních kódů v daném rozsahu. Neodvozuj jej z času či ID učitele.
2. Výchozí platnost vstupu je 10 minut, s výslovným prodloužením učitelem; konec přijímání žáků kód zneplatní. Konec vstupu nemusí ukončit již přijaté relace.
3. Před ověřením nezpřístupňuj osobní údaje ani seznam neveřejných aktivit. Odpověď při chybě nerozlišuje, zda kód existuje, vypršel nebo patří jiné škole.
4. Výchozí limity: 5 chybných pokusů za 60 s na předvstupní session, poté 60 s pauza; 100 chybných pokusů za 5 minut na zdrojovou IP; 200 chybných pokusů za 5 minut na školní vstupní prostor spustí dočasné omezení a upozornění učitele. Čítače jsou atomické a sdílené mezi instancemi. Dolaď je pro školní NAT a otestuj dostupnost; nezablokuj bez rozlišení celou školu trvale.
5. Nová browser session nesmí obejít všechny limity. Pro distribuované hádání počítej i s čekárnou a potvrzením učitelem. Limity nejsou náhrada ověření osoby; útočník ve třídě může kód legitimně znát.
6. Kód uchovávej krátce; pro ověření použij HMAC s odděleným serverovým tajemstvím a kontextem místnosti. Prostý hash čtyř číslic odolnost proti offline hádání nezajistí. Neukládej kód do logů.

### 5.2 QR

- QR může nést stejný kód a má pak stejnou bezpečnost. Nevydávej jej za silnější přihlášení.
- Preferovaný QR obsahuje náhodnou pozvánku s nejméně 128 bity entropie, účelem `join`, místností, expirací a možností odvolání. Sdílená třídní pozvánka může být vícekrát použitelná, ale stále nepotvrzuje identitu.
- Individuální pozvánka je jednorázová a výměna za session je atomická. Server ukládá jen hash náhodného tajemství; nesmí vzniknout dvě session při souběžném uplatnění.
- Nevkládej token do běžného query parametru s logováním. Vhodný tok: fragment URL, bez cizích skriptů přečíst, okamžitě odstranit přes `history.replaceState`, předat HTTPS POSTem a vyměnit za cookie. Nastav `Referrer-Policy: no-referrer`. Fragment není absolutní ochrana před historií, rozšířením či screenshotem; zásadní jsou krátká platnost, odvolání a rozsah oprávnění.

### 5.3 Životní cyklus session

- Server vydá 32 náhodných bajtů z CSPRNG; ukládá hash tokenu, scope, ověřenou identitu nebo omezenou anonymní relaci, expiraci a stav odvolání. Token nenese jméno ani známku.
- Cookie: `__Host-school_session`, `Secure`, `HttpOnly`, `SameSite=Lax` nebo `Strict` podle ověřeného toku, `Path=/`, bez `Domain`. Neukládej bearer token do localStorage, URL ani běžných logů.
- Nový vstup/přihlášení a změna oprávnění vytvoří nový token a odvolá původní. Server nepřebírá token zvolený klientem.
- Výchozí neaktivita žáka 30 minut, absolutně nejvýše 4 hodiny nebo konec jednorázové aktivity. U učitele 15 minut neaktivity a 8 hodin absolutně; dostupné úpravy pro delší práci a přístupnost zdokumentuj. Automatický polling neprodlužuje neaktivitu.
- Logout je serverová revokace, vypršení cookie a lokální úklid. Při změně hesla, odebrání role nebo incidentu umí správce odvolat všechny související session.
- Po odhlášení není návrat k osobním záznamům podle jména/device ID. Obnovu povol jen novým ověřením a bezpečně předaným oprávněním.
- Zápisové požadavky chrání CSRF token a kontrola původu; GET nemění stav. `SameSite` je doplňková ochrana. WebSocket ověřuje Origin, session i práva ke každé místnosti a ukončí přístup po revokaci.

Podklady: [OWASP Session Management](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html), [OWASP ASVS 5.0.0](https://asvs.owasp.org/). Časové a početní limity jsou volby tohoto profilu, nikoli zákonné hodnoty.

## 6. Role, oprávnění a integrita záznamů [P]

| Role | Povolený rozsah |
|---|---|
| Nepřihlášený | Veřejný obsah a případné omezené podání; žádné čtení osobních evidencí. |
| Jednorázový účastník | Pouze právě povolená aktivita/podání; bez historie a cizích záznamů. |
| Ověřený žák | Vlastní údaje a funkce určené žákovi; historii jen v rozsahu účelu a oprávnění. Nemění úředně potvrzené údaje pouhou editací profilu. |
| Ověřený zákonný zástupce | Jen údaje konkrétního dítěte, k nimž má aktuálně ověřené oprávnění; nikdy automaticky celá třída. |
| Učitel / pracovník školy | Jen přidělené osoby, třídy, procesy a kategorie údajů nutné pro práci. |
| Specializovaný pracovník | Citlivější agenda pouze s výslovným pověřením; samotná role učitele nezpřístupní poradenské nebo zdravotní údaje. |
| Správce školy | Správa členství a oprávnění školy; automaticky ne přístup ke všemu obsahu. |
| Provozní podpora | Technická diagnostika bez obsahu žáků; mimořádný přístup časově omezený, zdůvodněný a auditovaný. |
| Integrace / servisní účet | Jen konkrétní operace a data potřebná pro schválenou integraci. |
| Pověřenec/auditor | Vymezené evidence a audit; ne automatické právo měnit školní záznamy. |

Kontroluj oprávnění na serveru u každé operace a objektu, včetně seznamů, počtů výsledků, vyhledávání, příloh, exportů, WebSocketu a úloh na pozadí. `school_id`, role a vlastnictví odvozuj z ověřeného kontextu. Pokud klient určuje osobu, za kterou jedná, ověř příslušnou vazbu. Zákaz je výchozí. UUID ani skryté tlačítko nejsou autorizace.

Změna školy/třídy, odchod zaměstnance, zrušení účtu nebo změna zastupování musí aktualizovat přístupy včetně aktivních relací, sdílených odkazů a integrací. Neodvozuj rodičovské oprávnění jen ze shody příjmení nebo znalosti narození dítěte. Pravidelně kontroluj členství a privilegované role.

Zaměstnanci s přístupem k údajům žáků a správci mají individuální účet přes SSO nebo bezpečné přihlášení; profil požaduje MFA, přednostně passkey. Obnova účtu nesmí MFA obejít. Vlastní hesla ukládej jednosměrně pomocí udržované implementace Argon2id, nikdy AES; parametry stanov podle aktuálních doporučení a výkonu hostingu.

Všechny vstupy validuje server. Vlastnictví, schválení, docházka, známky a jiné autoritativní údaje mají povolené přechody a určené role. Důležité zápisy jsou transakční; idempotency klíč vázaný na uživatele a operaci brání duplicitnímu vytvoření. Souběžné změny stejné verze vyvolají řízený konflikt, nikoli tiché přepsání. Oprava důležitého údaje eviduje autora, důvod a předchozí verzi v chráněné historii s vlastní retencí.

**Pokud aplikace hodnotí:** skóre počítá nebo potvrzuje server, klientský výsledek není autoritativní; klíč odpovědí se nezveřejní předčasně. **Pokud přijímá žádosti nebo docházku:** podání uživatele se odlišuje od schváleného záznamu; uživatel si nesmí sám nastavit stav schválení.

© 2026 Luděk Sušický. [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Revidované vydání verze 1.1 vychází z původního průvodce z října 2026. Zachovej autora, licenci a oznámení úprav.
