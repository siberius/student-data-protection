# 7. Šifrování a správa klíčů [P]

<!-- Generovaná reference; upravuj udržovaného samostatného průvodce. -->

Zdrojové oddíly: 7.

## 7. Šifrování a správa klíčů [P]

GDPR nepředepisuje konkrétně AES-256-GCM ani jednu univerzální šifru. Tento profil ji volí pro aplikační ochranu osobních payloadů, CSV archivů a záloh; TLS chrání přenos. Šifrování nenahrazuje autorizaci a neochrání data před oprávněným, ale kompromitovaným procesem, který drží klíč.

### 7.1 AES-256-GCM

- Použij prověřenou vysokoúrovňovou knihovnu, 256bitový náhodný klíč, 96bitový nonce/IV a 128bitový autentizační tag. Nevytvářej vlastní šifru. Pro stejný klíč NESMÍ dojít k opakování nonce, ani po restartu, obnově či mezi instancemi.
- Pro řádkové payloady lze použít 96bitové CSPRNG nonce s unikátním indexem `(key_id, nonce)`, atomickou rezervací a opakováním generování při kolizi. Po obnově staré databáze nejprve zaveď nový klíč pro nové zápisy. Sleduj agregovaný počet šifrování pod klíčem; profil rotuje nejpozději při 10^6 operací nebo za rok, dříve při incidentu. Tento konzervativní limit není přepis obecného limitu NIST.
- Pro celý CSV archiv nebo záložní objekt vytvoř nový datový klíč pro každý objekt a zašifruj jej spravovaným obalovacím klíčem. Velké soubory řeš knihovnou pro ověřované streamování; nevymýšlej neověřený formát chunků.
- AAD musí kanonicky vázat verzi formátu, školu, typ a ID objektu a verzi záznamu. AAD není tajné; nepatří do něj jméno. Očekávaný kontext získej nezávisle, ne pouze z útočníkem přenesené obálky.
- Obálka obsahuje `format_version`, `algorithm`, `key_id`, `nonce`, `ciphertext`, `tag` a potřebná veřejná metadata. Změnu nonce, AAD, ciphertextu či tagu odmítni bez vrácení jakéhokoli plaintextu. GCM samo nebrání vrácení celé starší platné verze; verzi kontroluj proti důvěryhodnému stavu a auditu.

Podklady: [NIST SP 800-38D](https://csrc.nist.gov/pubs/sp/800/38/d/final), [NIST: oznámení revize](https://csrc.nist.gov/news/2024/nist-to-revise-sp-80038d-gcm-and-gmac-modes). Oznámení revize nepovažuj za hotový nový standard.

### 7.2 Klíče a přenos

Odděl datové klíče od dat a obalovací klíče uchovávej v KMS/HSM nebo vhodném správci tajemství. Aplikace dostane pouze minimální oprávnění; klíče nepatří do repozitáře, klientského JS, image ani záloh spolu s nechráněnými daty. Odděl produkci od testu a účely klíčů. Rotace musí zachovat čitelnost dosud oprávněně uchovaných dat a umožnit revokaci. Monitoruj selhání dešifrování a práci s klíči, nikoli jejich hodnoty. [OWASP Cryptographic Storage](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html).

HTTPS/WSS všude; preferuj TLS 1.3, TLS 1.2 jen pro potřebnou kompatibilitu s ECDHE a AEAD. Vypni SSL a TLS 1.0/1.1, slabé sady a TLS kompresi. AES-128-GCM nebo ChaCha20-Poly1305 v TLS nejsou samy o sobě porušením tohoto profilu. Ověř certifikáty, obnovu a interní síťové spoje. HSTS zaveď po ověření HTTPS, např. `max-age=31536000`; `includeSubDomains` až po kontrole všech subdomén. Osobní data nikdy neodešli nezabezpečeným požadavkem ani před přesměrováním. [OWASP TLS](https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Security_Cheat_Sheet.html).

© 2026 Luděk Sušický. [MIT](https://opensource.org/license/mit). Revidované vydání verze 1.1 vychází z původního průvodce z října 2026. Zachovej autora, licenci a oznámení úprav.
