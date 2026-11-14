# 12. Checkliste vor Produktivbetrieb

<!-- Generierte Referenz; bearbeiten Sie den eigenständigen Leitfaden. -->

Quellabschnitte: 12, 13, 14.

## 12. Checkliste vor Produktivbetrieb

Vor dem Echtbetrieb überprüfen:
1. Rechtsgrundlage dokumentiert und Abstimmung mit dem behördlichen DSB erfolgt.
2. AV-Vertrag (Art. 28 DSGVO) mit allen IT- und Cloud-Dienstleistern abgeschlossen.
3. Datenschutzhinweise nach Art. 13-14 DSGVO in verständlicher Sprache bereitgestellt.
4. Datenminimierung umgesetzt: keine Klarnamen in URLs, sensible Daten entfernt.
5. Passwörter mit Argon2id gehasht; Cookies mit HttpOnly, Secure, SameSite gesichert.
6. RBAC-Rollenkontrolle serverseitig gegen IDOR abgesichert.
7. TLS 1.3 und AES-256 für ruhende Daten aktiviert.
8. CSV-Exporte gegen Formel-Injektionen gehärtet.
9. Abmeldung löscht alle Browser-Speicher auf geteilten Schulrechnern.
10. Vollständig frei von Drittanbieter-Trackern und Werbeanalyse.

## 13. Abnahmetests (Acceptance tests)

Tabelle der 38 verbindlichen Prüfszenarien:

| Kennung | Bereich | Testszenario | Erwartetes Ergebnis |
|---|---|---|---|
| AT01 | Rechtsgrundlage | Verarbeitung von Schülerdaten im amtlichen Verzeichnis | Nachweis von Art. 6 Abs. 1 lit. c DSGVO i. V. m. Schulgesetz |
| AT02 | Einwilligung | Teilnahme am verpflichtenden Informatikunterricht | Keine Einwilligungserklärung als Zugangsvoraussetzung |
| AT03 | Sensible Daten | Registrierung in einer Mathematik-Lern-App | Keine Felder zu Religion, Herkunft oder Gesundheit |
| AT04 | Primärschlüssel | Aufruf des Schülerprofils in der Browser-URL | Zufällige UUIDv4 sichtbar, keine Schülernummer |
| AT05 | Metadaten | Schüler lädt Foto einer gelösten Aufgabe hoch | EXIF-Daten werden vor Speicherung serverseitig gelöscht |
| AT06 | Passwortstärke | Benutzer vergibt das Passwort „123456“ | Ablehnung durch System, Mindestanforderung 12 Zeichen |
| AT07 | Passwort-Hash | Inspektion der Benutzertabelle in der Datenbank | Passwörter sicher mit Argon2id oder bcrypt gehasht |
| AT08 | Cookie-Flags | Prüfung der Set-Cookie-Header | Flags HttpOnly, Secure, SameSite=Lax/Strict vorhanden |
| AT09 | Inaktivität | Schüler ist 35 Minuten ohne Aktion am Gerät | Sitzung automatisch beendet, Neuanmeldung erforderlich |
| AT10 | IDOR-Schutz | Schüler A ändert ID im Request auf Schüler B | Server antwortet mit 403 Forbidden |
| AT11 | Rollenrechte | Schüler sendet API-Request zur Notenänderung | Aktion wird mit 403 Forbidden abgewiesen |
| AT12 | Elterntrennung | Elternteil versucht fremdes Zeugnis abzurufen | Zugriff gesperrt, nur eigene Kinder sichtbar |
| AT13 | Transportverschlüsselung | Unverschlüsselter Aufruf per HTTP | Automatische 301-Weiterleitung auf HTTPS (TLS 1.3) |
| AT14 | HSTS-Header | Überprüfung der HTTP-Sicherheitsheader | Header Strict-Transport-Security aktiv |
| AT15 | CSV-Injektion | Name enthält `=1+2';cmd|' ...` | Exportiertes CSV stellt Apostroph vor die Zelle |
| AT16 | SQLite-Injektion | Eingabe von `' OR 1=1 --` in Suchmaske | Abfrage parametrisiert, kein Datenabfluss |
| AT17 | SQLite-Ablage | Direkter Aufruf der `.sqlite`-Datei im Browser | Zugriff verweigert (403/404), Datei außerhalb Web-Root |
| AT18 | Geteilte Rechner | Klick auf „Abmelden“ im Computerraum | LocalStorage und Tokens rückstandslos gelöscht |
| AT19 | CSP-Header | Versuch, externes Skript aus fremder Domäne zu laden | CSP blockiert Ausführung im Browser |
| AT20 | Telemetrie | Netzwerkanalyse der Schul-App | Keine Anfragen an Google Analytics, Meta oder Werbenetze |
| AT21 | Log-Sicherheit | Prüfung der Server-Protokolldateien | Keine Klartext-Passwörter oder Schülerdaten in Logs |
| AT22 | Vorfallregister | Simulation eines Datenlecks in Testumgebung | Vorfall erfasst, Meldemuster für LfDI vorbereitet |
| AT23 | KI-Emotion | Versuch, mimikbasierte Stimmungsanalyse zu nutzen | Blockierung als verbotene Praxis (Art. 5 KI-Verordnung) |
| AT24 | KI-Hochrisiko | KI zur automatischen Notenvergabe bei Prüfungen | Als Hochrisiko eingestuft, strenge Auflagen und Aufsicht |
| AT25 | KI-Aufsicht | KI schlägt Note für Freitextaufgabe vor | Lehrkraft kann Note jederzeit manuell anpassen |
| AT26 | KI-AVV | Einbindung einer kommerziellen LLM-API | AV-Vertrag nach Art. 28 DSGVO vor Einsatz geschlossen |
| AT27 | KI-Training | AGB-Prüfung des externen KI-Dienstes | Vertragliche Zusicherung: keine Nutzung für Modelltraining |
| AT28 | SSO-Federation | Anmeldung über schulisches Shibboleth / OIDC | Keine Passwortübertragung an die externe Webanwendung |
| AT29 | Schulaustritt | Schüler verlässt die Schule nach Abschluss | Konto deaktiviert, Daten archiviert bzw. gelöscht |
| AT30 | Auskunftsrecht | Antrag auf Datenauskunft nach Art. 15 DSGVO | Export aller gespeicherten Schülerdaten generierbar |
| AT31 | Quellcode-Audit | Untersuchung des Quellcode-Repositorys | Keine Passwörter oder API-Schlüssel im Quelltext |
| AT32 | Backup-Prüfung | Test der Datenwiederherstellung aus Sicherung | Backup verschlüsselt, Wiederherstellung erfolgreich |
| AT33 | Veraltetes Hashing | Fund von MD5 oder SHA-1 in Legacy-Code | Sofortige Aktualisierung auf Argon2id gefordert |
| AT34 | Drittlandtransfer | Sicherungsserver in US-Cloud ohne Garantien | Konfiguration blockiert wegen fehlender Rechtsgrundlage |
| AT35 | KI-Transparenz | Schüler chattet mit schulischem Lernbot | Klare Kennzeichnung, dass es sich um eine KI handelt |
| AT36 | Lehrkraftgrenze | Fachlehrer für Sport will Physiknoten ändern | Zugriff gemäß zugewiesener Fächerberechtigung gesperrt |
| AT37 | KI-Gate L0/C1/C2 | Schüler sendet Prompt mit Name und Klasse | Gate filtert PII heraus oder nutzt lokales L0-Modell |
| AT38 | k-Anonymität KI | Bildung von Lernfortschrittsdaten mit k=3 | Validierungsskript blockiert Export (Forderung k >= 5) |

## 14. Form der Übergabe und Grenzen von Zusagen

Bei der Übergabe von Auditberichten oder Dokumentation:
- Feststellungen sachlich, präzise und konstruktiv formulieren.
- Beobachtete Code-Tatsachen klar von allgemeinen Empfehlungen trennen.
- Niemals Formulierungen wie „100% DSGVO-konform“ oder „garantiert rechtssicher“ verwenden; Datenschutz ist ein fortlaufender organisatorischer Prozess.

© 2026 Luděk Sušický. [MIT](https://opensource.org/license/mit). Überarbeitete Ausgabe der Version 1.2, basierend auf dem ursprünglichen Leitfaden vom Oktober 2026. Urheber-, Lizenz- und Änderungshinweise beibehalten.
