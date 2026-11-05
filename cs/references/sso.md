# 16. Školní federované přihlášení a SSO [P]

<!-- Generovaná reference; upravuj udržovaného samostatného průvodce. -->

Zdrojové oddíly: 16.

## 16. Školní federované přihlášení a SSO [P]

Použij jen při zapojení poskytovatele identity. Funkční přihlášení nenahrazuj pouze kvůli zavedení SSO. Použij udržovanou protokolovou knihovnu a aktuální integrační pokyny poskytovatele; autorizace OAuth sama nepotvrzuje identitu uživatele.

U OIDC ověř vydavatele, podpis s důvěryhodným zjištěním klíčů, příjemce a případnou povinnou autorizovanou stranu, expiraci, nonce a vazbu na přihlašovací transakci. Použij tok autorizačního kódu s PKCE, kde jej profil klienta podporuje a vyžaduje; přesně omez redirect URI, svaž callback s původním prohlížečem a zabraň login CSRF a opakovanému použití kódu. Access token nepovažuj za ID token. U SAML ověř potřebné podpisy, vydavatele, audience, destination, recipient, vazbu na požadavek, časové podmínky a opakované použití assertion pomocí udržované implementace. Nevytvářej vlastní parser XML podpisu. Kontroly vybírej podle skutečného protokolu a toku, ne pro oba protokoly automaticky.

Identitu propoj ověřeným stabilním identifikátorem v rozsahu důvěryhodného vydavatele, například issuer a subject; následně přiřaď oprávněné členství správné škole a aplikační roli. E-mail, jméno, doména či nedůvěryhodný údaj školy samy nesmí slučovat účty nebo udělit zaměstnanecký přístup. Vymez registraci, spojení účtů, změnu e-mailu či subject, shodu jmen a odebrání členství. Privilegovaná role vychází z důvěryhodných oprávnění nebo oprávněného administrativního kroku. Úspěšné přihlášení u poskytovatele samo neotevírá všechny školní evidence.

Místní relace musí být odvolatelné; logout poskytovatele a aplikace mají různý rozsah. Členství a privilegia vyhodnocuj podle doloženého přenosu změn a pro známé odebrání zajisti okamžitou aplikační revokaci. Zaměstnanecký přístup nenechávej potichu platný do vzdálené expirace tokenu poskytovatele. Při výpadku či neplatných metadatech odmítni chráněný přístup a nabídni odpovídající provozní náhradu; neobcházej MFA a nevěř neověřeným assertion.

Pro skutečný tok ověř cizí issuer/audience, chybný či chybějící povinný podpis, expiraci a replay, nesouhlas state/nonce, mapování jiné školy, shodný e-mail, odebrané členství a výpadek poskytovatele. Eviduj verze protokolu/knihovny a skutečné výsledky. Společná tabulka přidává scénáře SSO; samotný test běžné relace nestačí.

Technické vodítko: [OWASP OAuth2](https://cheatsheetseries.owasp.org/cheatsheets/OAuth2_Cheat_Sheet.html), [OWASP SAML Security](https://cheatsheetseries.owasp.org/cheatsheets/SAML_Security_Cheat_Sheet.html).

Dílčí doplnění (role pověřence, RAG a SSO) posouzena 5. 11. 2026. Původní datum ověření zdrojů výše je historické; vydání netvrdí nový úplný právní audit. Ověřená a neověřená tvrzení rozlišuje registr zdrojů.

© 2026 Luděk Sušický. [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Revidované vydání verze 1.1 vychází z původního průvodce z října 2026. Zachovej autora, licenci a oznámení úprav.
