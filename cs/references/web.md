# 9. Web, PWA a sdílená zařízení [P]

<!-- Generovaná reference; upravuj udržovaného samostatného průvodce. -->

Zdrojové oddíly: 9.

## 9. Web, PWA a sdílená zařízení [P]

- Service worker cachuje pouze explicitní allowlist veřejných statických souborů. Osobní API, výsledky, HTML s daty a exporty používají network-only a `Cache-Control: no-store`; výpadek sítě nesmí vrátit stará osobní data z fallback cache.
- Osobní data ani dlouhodobé tokeny výchozí profil neukládá do localStorage, IndexedDB nebo Cache Storage. Offline PWA může zobrazit veřejný shell. Offline řešení s osobními daty vyžaduje samostatný návrh: minimální data, klíč s řízeným přístupem, expiraci, výmaz a test ztraceného zařízení. Klíč vedle ciphertextu neposkytuje účinné oddělení.
- Logout vyčistí paměť UI, formuláře, příslušná lokální úložiště, cache a další otevřené záložky. `Clear-Site-Data` použij jako doplněk s ověřením podpory a dopadu na společný origin. Při návratu přes historii/bfcache stránku znovu ověř a do té doby osobní obsah skryj.
- Offline logout vyčistí klienta a nesmí tvrdit úspěšnou serverovou revokaci, dokud nebyla potvrzena. Při obnovení spojení se revokace dokončí; zbylé riziko omezuje serverová expirace. Na sdíleném zařízení neobnovuj osobní session jen podle obnovy okna prohlížeče.
- Nelze garantovat odstranění screenshotů, rozšíření, OS paměti ani už staženého souboru. Neformuluj „po odhlášení zmizí všechna data“; popiš přesně aplikací ovládané úložiště.
- Zabraň XSS kontextovým escapováním, zakázáním neověřeného HTML a restriktivní CSP s nonce/hash; omez `connect-src`, `frame-ancestors`, `object-src` a `base-uri`. Nepovoluj libovolné CORS origins ani credentials s wildcardem. Přidej `X-Content-Type-Options: nosniff`.
- Žádné reklamní trackery ani session replay na žákovských obrazovkách. Minimalizuj cizí skripty; chyby a analytika musí mít redakci údajů. Importy mají limit velikosti, schéma, bezpečné názvy a kontrolu obsahu.
- Aktualizuj runtime a závislosti, drž lockfile, kontroluj tajemství a známé zranitelnosti, odděl test a produkci. ASVS úroveň 2 je výchozí ověřovací cíl v relevantním rozsahu, nikoli prohlášení certifikace. [OWASP ASVS 5.0.0](https://asvs.owasp.org/).

© 2026 Luděk Sušický. [MIT](https://opensource.org/license/mit). Revidované vydání verze 1.1 vychází z původního průvodce z října 2026. Zachovej autora, licenci a oznámení úprav.
