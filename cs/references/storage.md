# 8. CSV a SQLite [P]

<!-- Generovaná reference; upravuj udržovaného samostatného průvodce. -->

Zdrojové oddíly: 8.

## 8. CSV a SQLite [P]

### 8.1 SQLite jako transakční úložiště

- SQLite je přípustná volba; běžná SQLite sama nešifruje. Aplikace přistupuje serverově, nikoli přes veřejný download databáze. Pro více instancí a vysoký souběh zvol databázi odpovídající architektuře; nesdílej soubor nekontrolovaně přes síťový disk.
- Výchozí profil: AES-256-GCM aplikačně šifrované osobní payloady + šifrovaný disk/svazek. Použitá databázová šifrovací rozšíření mají vlastní algoritmy; netvrď, že SQLCipher automaticky znamená AES-GCM. Nezašifrované indexy, vazby a počty mohou být stále osobní metadata.
- Adresář a DB přístupné jen servisnímu účtu, na Unixu orientačně adresář `0700`, soubory `0600`, ekvivalentní ACL jinde. Žádný public webroot, statická cesta, veřejný bucket, synchronizovaná osobní složka či repozitář.
- Parametrizované dotazy; dynamické názvy polí jen z allowlistu. Cizí klíče zapni na každém spojení, důležité vazby omez také školou. Transakčně chraň odevzdání, jednorázové pozvánky a audit změn. Ošetři zamčenou DB, plný disk a neúplný zápis.
- Zahrň `-wal`, `-shm`, journal, dočasné soubory, dumpy a crash/swap do ochrany a retence. Zálohuj konzistentním [SQLite Online Backup API](https://sqlite.org/backup.html) nebo ověřeným snapshotem, ne slepou kopií živého hlavního souboru bez WAL.
- Výmaz řeš na úrovni dat i kopií. `secure_delete`, checkpoint nebo `VACUUM` mohou pomoci, ale nezaručí fyzické smazání SSD, snapshotů a starých záloh. U FTS a dalších rozšíření ověř zbytkové kopie. [SQLite PRAGMA secure_delete](https://sqlite.org/pragma.html#pragma_secure_delete).

### 8.2 CSV jako export nebo omezené úložiště

Použij transakční databázi odpovídající provozu jako autoritativní úložiště a CSV jako řízený export; SQLite je vhodná pro vymezené menší nasazení. Pokud projekt potřebuje CSV jako hlavní úložiště, implementuj jednoho zapisujícího, uzamčení, validaci schématu, revize a atomickou náhradu souboru po úspěšném zápisu a synchronizaci. Při pádu zůstane poslední úplná verze. CSV samo neposkytuje transakce, role ani šifrování.

CSV na serveru archivuj v ověřeném AES-GCM kontejneru, nikoli pouze přejmenováním přípony. Plaintext sestavuj v paměti; dočasný soubor pouze na chráněném šifrovaném prostoru s automatickým úklidem. Obyčejný ZIP s heslem není náhrada tohoto profilu.

Export povol pouze roli s výslovným oprávněním, v rozsahu příslušné školy, osob a kategorií dat. Zahrň jen potřebné sloupce, nikdy session tokeny či device ID bez doloženého účelu. Vytvoření i stažení audituj. Download endpoint znovu ověří session a práva, vrací `Cache-Control: no-store` a `Content-Disposition: attachment`; případný odkaz je krátkodobý a omezený, nikoli veřejný trvalý URL.

Použij CSV knihovnu s řádným citováním oddělovačů, uvozovek a nových řádků. Ochrana proti formula injection je oddělený krok: pro lidský tabulkový export ošetři text začínající `=`, `+`, `-`, `@`, řídicími znaky i obcházejícími variantami. Číselné sloupce parsuj jako čísla, nikoli libovolné řetězce. Apostrof a uvozování nejsou univerzální záruka po uložení a znovuotevření v Excelu. Definuj podporovaný importní postup a otestuj Excel/LibreOffice; pokud nezajistí bezpečnost, nabídni pro lidské čtení formát s explicitně textovými buňkami a rizikový export odmítni. Neměň kvůli exportu původní údaje. [OWASP CSV Injection](https://owasp.org/www-community/attacks/CSV_Injection).

Stažený otevřený CSV je nešifrovaná kopie na zařízení příjemce. Informuj o zabezpečeném uložení a lhůtě smazání; logout jej nesmaže. Je-li potřeba šifrovaný přenos souboru mimo aplikaci, použij spravovaný bezpečný kanál nebo vhodný kontejner a oddělené předání tajemství.

© 2026 Luděk Sušický. [MIT](https://opensource.org/license/mit). Revidované vydání verze 1.1 vychází z původního průvodce z října 2026. Zachovej autora, licenci a oznámení úprav.
