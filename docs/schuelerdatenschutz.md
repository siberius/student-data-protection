# Schülerdatenschutz in schulischen Anwendungen

> Dieses Dokument stellt ein praxisorientiertes Sicherheitsprofil für Schulanwendungen dar. Es ist keine Rechtsberatung und kein Konformitätszertifikat. Vor der Verarbeitung echter Daten trifft der Verantwortliche die Entscheidung über den Einsatz nach angemessener Prüfung und rechtzeitiger Konsultation des Datenschutzbeauftragten (DSB).

**Version:** 1.2 · **Sprache und Rechtsordnung:** Deutsch, Deutschland / EU · **Ursprüngliche Quellenprüfung:** 22. Oktober 2026 · **Ausgabe:** 14. November 2026. Sicherheitsmaßnahmen für KI-Modelle, k-Anonymität (k >= 5), l-Diversität (l >= 2) und skriptgestützte Validierung ergänzt am 14. November 2026.

Verwenden Sie diesen eigenständigen Skill bei Konzeption, Implementierung oder Prüfung von Anwendungen, die personenbezogene Daten von Schülern, deren Erziehungsberechtigten oder Lehrkräften erfassen, speichern, anzeigen, bewerten oder weitergeben. Er umfasst Notenverwaltung, Formulare, Anwesenheit, Hausaufgaben, Portfolios, Kommunikation, Veranstaltungsanmeldungen, Leistungsbewertung und KI-Lernwerkzeuge. Daten können Namen, Kontaktdaten, Klassen, Noten, Dateien, Nachrichten, Testergebnisse, Betriebsprotokolle sowie Sitzungs- und Gerätekennungen sein.

Grundlage ist der Schutz während des gesamten Datenlebenszyklus. Web- und PWA-Prüfungen gelten dort, wo diese Technologie eingesetzt wird; mobile oder Desktop-Clients erfordern plattformspezifische Absicherungen. CSV und SQLite sind unterstützte Entwurfsoptionen, nicht die einzig zulässige Architektur. Fügen Sie keine Tests, Notenvergaben, KI-Modelle oder Code-Logins hinzu, nur weil dieser Skill sie beschreibt.

Unterscheiden Sie zwischen **dauerhaftem Konto mit verifizierter Identität**, **zeitlich begrenzter punktueller Teilnahme** und **öffentlicher Datenerfassung ohne Konto**. Name, Klasse, Endgerät oder Kenntnis eines gemeinsamen Codes beweisen keine Identität. Verwenden Sie eine Authentifizierung, die der Bedeutung der Daten und der Bildungshistorie angemessen ist. Ein Einmalcode oder QR-Code ist ein optionales Modul für begrenzte Aktivitäten, kein universeller Schulzugang.

## 1. Auslegung der Anforderungen und Arbeitsweise des Assistenten

- **[G] Gesetzliche Anforderung:** verbindlich bei Vorliegen der beschriebenen Bedingungen. Zitierte Normen haben Vorrang vor technischen Empfehlungen.
- **[P] Sicherheitsprofil:** spezifische Ausgestaltung dieses Skills. Bestimmungen wie MUSS/DARF NICHT in technischen Abschnitten definieren dieses Profil, nicht die wörtliche DSGVO-Vorgabe. Abweichungen sind mit Bedrohung, Ausgleichsmaßnahme, Test und Entscheidung der verantwortlichen Schulleitung zu dokumentieren.
- **[E] Empfehlung:** zweckmäßige Erweiterung je nach Risiko und Bereitstellungsform.
- **[Ü] Zu überprüfen:** Aspekt, der vom tatsächlichen Betrieb, aktuellem Recht oder unbestätigter Konfiguration abhängt. Nicht ohne Nachweis als erfüllt werten.

1. Leiten Sie den Modus ab: Entwurf, Implementierung, Audit oder Sicherheitsvorfall. Ein Audit bewertet und berichtet, ohne die Anwendung zu verändern. Die Vorfallanalyse berechtigt nicht dazu, Dienste abzuschalten, Konten zu löschen oder Benachrichtigungen zu versenden. Handeln Sie nur im Rahmen der tatsächlichen Befugnis.
2. Nutzen Sie bekannten Kontext und ermitteln Sie Zweck, Datenflüsse, Rollen und Risikoänderungen. Fragen Sie nur nach fehlenden, entscheidungsrelevanten Informationen. Bei kleiner Korrektur betroffene Grenze und Regressionen prüfen; nicht das gesamte Audit wiederholen. Gravierendes Nachbarrisiko dokumentieren und melden; den Arbeitsumfang nicht eigenmächtig ausweiten.
3. Erfassen Sie Daten, Empfänger, Identität, Berechtigungen, Speicherfristen und Risiken. Bewahren Sie sichere Architektur und funktionierende Schutzmaßnahmen. Solange Zweck, Rechtsgrundlage oder Bereitstellungsentscheidung fehlen, synthetische Testdaten verwenden.
4. Beim Entwurf verhältnismäßige Sicherheitsmaßnahmen empfehlen. Bei autorisierter Implementierung diese unter Angabe der Code- oder Konfigurationsstellen umsetzen. Beim Audit Schweregrad, Nachweis, Auswirkung, Empfehlung und erforderliche Prüfung angeben. Vermutung von festgestelltem Mangel trennen.
5. Wählen Sie Abnahmetests nach Funktion und Risiko aus. Unterscheiden Sie: Bestanden, Fehlgeschlagen, Nicht ausgeführt und Nicht anwendbar mit Begründung. Ein Testplan ist kein Nachweis erfolgreicher Durchführung.
6. Vor dem Produktivbetrieb Rechtsgrundlage, erforderliche Prüfung und aktuelle Vorschriften kontrollieren. Die Schulleitung entscheidet über den Einsatz nach rechtzeitiger Abstimmung mit dem behördlichen Datenschutzbeauftragten. Ohne Rechtsgrundlage keine Verarbeitung im Echtbetrieb empfehlen; autorisierte Arbeiten in Testumgebung mit Testdaten fortführen.

### 1.4 Fortlaufende Rechtsaktualität und Upstream-Rückmeldung an GitHub [P]

Das Sicherheitsprofil dieses Skills erfordert, dass jede rechtliche Bewertung auf der aktuellen Rechtslage basiert (DSGVO, KI-Verordnung, BDSG, Landesrecht und DSK-Beschlüsse).

1. **Quellenaltersregel (> 6 Monate):** Sind seit der letzten Quellenprüfung mehr als 6 Monate vergangen, muss der Assistent die Gültigkeit der Rechtsgrundlagen überprüfen.
2. **Sofortige Anpassung für den Nutzer:** Bei festgestellten Rechtsänderungen wendet der Assistent sofort die neue Rechtslage an und informiert den Nutzer.
3. **Upstream-Meldung (GitHub Issue):** Der Assistent schlägt mit Zustimmung des Nutzers vor, ein Issue im Repository `https://github.com/siberius/student-data-protection/issues` mit dem Label `legal-update` zu erstellen.

## 2. DSGVO und deutsches Schuldatenschutzrecht

### 2.1 Rechtsgrundlagen an deutschen Schulen

[G] Jede Verarbeitung von Schülerdaten bedarf einer wirksamen Rechtsgrundlage (Art. 6 und Art. 9 DSGVO):

- **Art. 6 Abs. 1 lit. c DSGVO i. V. m. Landesrecht (Rechtliche Verpflichtung):** Führung von Schülerakten, Klassenbüchern, Notenlisten und Zeugnissen nach den Schulgesetzen der 16 Bundesländer (z. B. BayEUG, SchulG NRW, HSchG).
- **Art. 6 Abs. 1 lit. e DSGVO (Wahrnehmung einer Aufgabe im öffentlichen Interesse):** Erfüllung des staatlichen Bildungs- und Erziehungsauftrags.
- **Art. 6 Abs. 1 lit. a DSGVO (Einwilligung):** Nur für freiwillige Angebote (Veröffentlichung von Schülerfotos, freiwillige Arbeitsgemeinschaften, optionale Exkursionen). Die Einwilligung darf keine Voraussetzung für die Teilnahme am regulären Unterricht sein (§ 16 BDSG setzt das Schutzalter auf 16 Jahre fest; darunter ist die Zustimmung der Eltern zwingend).
- **Art. 9 DSGVO (Besondere Datenkategorien):** Gesundheitsdaten (Atteste, Allergien, sonderpädagogischer Förderbedarf) werden nur auf gesetzlicher Basis zur Gewährleistung von Sicherheit und Inklusion verarbeitet.

### 2.2 Verantwortlichkeit und Datenschutzbeauftragter

[G] Verantwortlicher für die Datenverarbeitung ist die jeweilige Schule, vertreten durch die Schulleitung.

- **Vertrag zur Auftragsverarbeitung (AVV / ADV, Art. 28 DSGVO):** Jeder externe Clouddienst, Lernplattform-Betreiber oder KI-Dienstleister erfordert vor Beginn der Verarbeitung einen formalen AV-Vertrag.
- **Behördlicher Datenschutzbeauftragter (bDSB):** Öffentliche Schulen sind gesetzlich verpflichtet, einen DSB zu benennen. Der DSB muss vor Einführung neuer IT-Lösungen frühzeitig beratend hinzugezogen werden.
- **Beschlüsse der Datenschutzkonferenz (DSK):** Strikte Anforderungen an Microsoft 365 und Cloud-Dienste: Übermittlung von Telemetriedaten in Drittländer ohne Angemessenheitsbeschluss ist unzulässig. Vorrang für datenschutzfreundliche Alternativen und Open-Source-Systeme (L0 / Moodle).
- **Verbot von Biometrie:** Der Einsatz biometrischer Erkennungsverfahren (Gesichtserkennung, Fingerabdrücke) zur Anwesenheitskontrolle oder Essensausgabe ist an Schulen unzulässig.

### 2.3 Informationspflichten und Betroffenenrechte

[G] Die Schule muss Schüler und Eltern transparent nach Art. 13-14 DSGVO in altersgerechter Sprache informieren.

- Rechte auf Auskunft (Art. 15), Berichtigung (Art. 16) und Einschränkung (Art. 18).
- Das Recht auf Löschung (Art. 17) besteht bei gesetzlich vorgeschriebenen Schulakten während der gesetzlichen Aufbewahrungsfristen nicht.
- Beschwerderecht bei der zuständigen Landesbeauftragten für den Datenschutz (LfDI).

[P] Sicherheitsprofil: Hosting und Datensicherungen MÜSSEN innerhalb der Europäischen Union / des EWR erfolgen. US-Cloud-Speicher ohne Ende-zu-Ende-Verschlüsselung sind für Schülerdaten ausgeschlossen.

### 2.4 Vergleichende Übersicht nationaler Rechtsordnungen und Schutzaltersgrenzen [G/P]

Bei der Entwicklung von Lernanwendungen stets den rechtlichen Rahmen der Schule berücksichtigen:

| Land / Rechtsordnung | Schutzalter nach Art. 8 DSGVO | Aufsichtsbehörde | Schulrechtliche Besonderheiten und Cloud/KI-Vorgaben |
| --- | --- | --- | --- |
| **Deutschland (DE)** | 16 Jahre (§ 16 BDSG) | DSK + 16 Landesbeauftragte (LfDI) | 16 Landesschulgesetze; strenge DSK-Beschlüsse zu M365/Telemetrie; Vorrang für On-Premise/Open-Source (L0); DSFA für KI. |
| **Polen (PL)** | 16 Jahre (Ustawa o ODO 2018) | UODO | Prawo oświatowe; Verantwortung der Schulleitung; Verbot von Schülerbiometrie; ADV nach Art. 28 DSGVO. |
| **Tschechien (CZ)** | 15 Jahre (Gesetz Nr. 110/2019 Sb.) | ÚOOÚ | Schulgesetz Nr. 561/2004 Sb.; Leitlinien von MŠMT und NPI zu KI in Schulen. |
| **Frankreich (FR)** | 15 Jahre (Loi Informatique et Libertés) | CNIL | Code de l'éducation; souveräne ENT-Plattformen; Ministeriumsvorgaben gegen US-Clouds; Verbot von Klassen-Sammelaccounts bei KI. |
| **Spanien (ES)** | 14 Jahre (LOPDGDD Art. 7) | AEPD | Bildungsgesetz LOE; verpflichtender DSB an Schulen; detaillierte AEPD-Vorgaben zu k-Anonymität. |
| **Ukraine (UA)** | 14-18 Jahre (Zivilgesetzbuch) | Ombudsmann für Menschenrechte | Gesetz Nr. 2297-VI und Gesetzentwurf 8153; Mrija-Ökosystem; Schüler in der EU unterliegen voll der DSGVO. |

#### Regeln für deutsche Implementierungen

1. **Föderaler Rahmen und DSK-Konformität:** [G] Beachten Sie das Schulrecht des jeweiligen Bundeslandes. Lösungen müssen den DSK-Vorgaben genügen (keine abfließende Diagnosetelemetrie an Dritte).
2. **Priorität für lokale KI (L0-Gate):** [P] Wo immer möglich, sind lokale Open-Source-Modelle (Ollama, llama.cpp im Schulnetz) zu bevorzugen, um Datentransfers vollständig zu vermeiden.

## 3. KI-Verordnung (AI Act): Geltung, Einstufung und Fristen

### 3.1 Anwendbarkeit auf Schulinstrumente

[G] Die Verordnung (EU) 2024/1689 (KI-Verordnung) gilt für KI-Systeme, die in der EU in Verkehr gebracht oder verwendet werden.
Klassische regelbasierte Algorithmen, deterministische Punkteberechnungen und Datenbankabfragen sind keine KI-Systeme im Sinne der Verordnung.

### 3.2 Verbotene KI-Praktiken im Bildungsbereich (Art. 5)

[G] Strikt verboten sind an Schulen:

1. **Emotionserkennung:** Systeme, die emotionale Zustände von Schülern anhand von Mimik oder Stimme im Unterricht ableiten (Art. 5 Abs. 1 lit. f).
2. **Social Scoring:** Bewertung oder Klassifizierung des Schülerverhaltens, die zu Benachteiligungen führt (Art. 5 Abs. 1 lit. c).
3. **Biometrische Kategorisierung:** Ableitung sensibler Merkmale aus biometrischen Daten.
4. **Unterbewusste Beeinflussung:** Techniken, die das Verhalten von Schülern manipulieren und ihnen Schaden zufügen können.

### 3.3 Hochrisiko-KI-Systeme in der Bildung (Art. 6 und Anhang III)

[G] Als Hochrisiko-KI (High-Risk AI) gelten Systeme für:

- Zulassung und Zuweisung zu Bildungsgängen oder Schulen.
- Bewertung von Lernergebnissen und automatisierte Prüfungsbewertung mit Einfluss auf Noten.
- Verhaltensüberwachung und Aufdeckung von Täuschungsversuchen bei Prüfungen (Proctoring).

### 3.4 Pflichten für Anbieter und Betreiber (Schulen)

- **Anbieter:** Risikomanagementsystem (Art. 9), Datenqualitätsmanagement (Art. 10), technische Dokumentation (Art. 11), automatische Protokollierung (Art. 12), Transparenz und Anleitung (Art. 13), menschliche Aufsicht (Human-in-the-Loop, Art. 14).
- **Schule (Betreiber):** Verwendung nach Anleitung, Gewährleistung menschlicher Kontrolle durch Lehrkräfte, Aufbewahrung von Systemprotokollen für mindestens 6 Monate (Art. 26 Abs. 6), Information der Betroffenen.

### 3.5 Zeitplan

- **Februar 2025:** Verbot verbotener Praktiken (Emotionserkennung, Social Scoring).
- **August 2025:** Regeln für KI-Modelle mit allgemeinem Verwendungszweck (GPAI).
- **August 2026:** Volle Anwendung für Hochrisiko-KI in Bildung und Berufsbildung.

## 4. Datenmodell, Erhebung und Datenminimierung [P]

[P] Das Datenmodell MUSS dem Grundsatz der Datenminimierung entsprechen (Art. 5 Abs. 1 lit. c DSGVO):

- **Identifikatoren:** Generierte UUIDv4-Schlüssel als Primärschlüssel verwenden. Niemals Schüleraktennummern oder Klarnamen in URLs, Dateinamen oder Client-Speichern nutzen.
- **Optionale Felder:** Telefonnummern, Wohnanschriften oder Fotos dürfen in fachbezogenen Lern-Apps keine Pflichtfelder sein.
- **Besondere Kategorien:** Keine Speicherung von Krankheitsdiagnosen. Für Nachteilsausgleiche (z. B. Zeitzugabe) genügt ein technischer Parameter (`extra_time_factor: 1.25`) ohne Angabe des medizinischen Befunds.
- **Metadaten:** EXIF-Metadaten aus von Schülern hochgeladenen Aufgabenbildern vor dem Speichern auf dem Server vollständig entfernen.

## 5. Authentifizierung, Einladungen und Sitzungen [P]

[P] Sicherheitsanforderungen:

- **Passwörter:** Mindestens 12 Zeichen, Abgleich gegen Wörterbücher kompromittierter Passwörter. Passwort-Hashing zwingend mit Argon2id oder bcrypt (hoher Work-Factor).
- **PIN- und QR-Codes:** Nur für jüngere Schüler für zeitlich begrenzte Unterrichtseinheiten im Klassenraum zulässig.
- **Sitzungen:** Kryptografisch sichere Sitzungs-IDs (mindestens 128 Bit Entropie). Cookies mit `HttpOnly`, `Secure` und `SameSite=Lax/Strict`.
- **Inaktivitäts-Timeout:** Automatischer Logout nach maximal 30 Minuten bei Schülern und 15 Minuten bei Lehrkräften/Verwaltung.

## 6. Rollen, Berechtigungen und Integrität [P]

[P] Zugriffskontrolle:

- **RBAC-Modell:** Definierte Rollen: Schüler, Lehrkraft, Eltern/Erziehungsberechtigte, Schulleitung/Administrator.
- **Mandantentrennung:** Berechtigungsprüfung bei jeder Datenbankabfrage. Schüler sehen nur eigene Noten; Eltern nur eigene Kinder; Lehrkräfte nur die eigenen Klassen.
- **Schutz vor IDOR:** Manipulation von Objekt-IDs im Request muss serverseitig mit 403 Forbidden blockiert werden.
- **Audit-Trail:** Änderungen von Noten und Zeugnisvermerken werden revisionssicher mit Zeitstempel (UTC) und Benutzerkennung protokolliert.

## 7. Verschlüsselung und Schlüsselverwaltung [P]

[P] Kryptografische Standards:

- **Ruhende Daten (At Rest):** Verschlüsselung von Datenbanken und Backups mit AES-256-GCM oder ChaCha20-Poly1305.
- **Übertragene Daten (In Transit):** Erzwingung von TLS 1.3 (mindestens TLS 1.2 mit Forward Secrecy). Aktiviertes HSTS für mindestens 1 Jahr (`max-age=31536000; includeSubDomains`).
- **Schlüsselmanagement:** Keine kryptografischen Schlüssel im Quellcode oder Repository. Verwendung sicherer Secret-Stores oder Umgebungsvariablen.

## 8. CSV und SQLite [P]

[P] Lokale Datenspeicherung und Exporte:

- **CSV-Injektionsschutz:** Felder, die mit `=`, `+`, `-`, `@`, Tabulator oder Zeilenumbruch beginnen, MÜSSEN beim Export durch ein vorangestelltes Apostroph (`'`) neutralisiert werden, um Makroausführung in Tabellenkalkulationen (Excel, Calc) zu verhindern.
- **SQLite:** Einsatz des WAL-Modus (Write-Ahead Logging) und Aktivierung von Fremdschlüsseln (`PRAGMA foreign_keys = ON;`). Die Datenbankdatei darf nicht im öffentlich erreichbaren Web-Root liegen.
- **Prepared Statements:** Ausschließlich parametrisierte SQL-Abfragen zur Verhinderung von SQL-Injektionen.

## 9. Web, PWA und geteilte Geräte [P]

[P] Sicherheit an Schulgeräten:

- **Geteilte Rechner im Computerraum:** Bei Klick auf „Abmelden“ MÜSSEN `localStorage`, `sessionStorage` und `IndexedDB` vollständig von personenbezogenen Daten und Tokens bereinigt werden.
- **Content Security Policy (CSP):** Strikte CSP-Header verhindern das Nachladen von Skripten Dritter und unautorisierten Inline-Code.
- **Keine Werbetracker:** Vollständiges Verbot von Google Analytics, Meta Pixel oder Marketing-Trackern in schulischen Anwendungen.

## 10. Audit, Aufbewahrung und Wiederherstellung [P/G]

[P/G] Protokollierung und Datenlebenszyklus:

- **Protokolldaten:** Aufzeichnung von Anmeldungen, Fehlversuchen, Rechteänderungen und Notenbearbeitungen.
- **Minimierte Logs:** Keine Klartext-Passwörter oder sensiblen Schülerdaten in Protokolldateien.
- **Löschfristen:** Temporäre Unterrichtsdaten nach Schuljahresende löschen; amtliche Nachweise gemäß den Archivvorschriften des jeweiligen Bundeslandes sichern.
- **Backups:** Regelmäßige verschlüsselte Backups mit halbjährlicher Wiederherstellungsprüfung.

## 11. Sicherheitsvorfälle (Incidents) [G/P]

[G] Vorgehen bei Datenschutzverletzungen (Art. 33-34 DSGVO):

- **Meldung an Aufsichtsbehörde:** Meldung an die zuständige Landesbeauftragte für den Datenschutz (LfDI) innerhalb von 72 Stunden nach Bekanntwerden, sofern ein Risiko für die Rechte der Schüler besteht.
- **Benachrichtigung der Betroffenen:** Bei hohem Risiko unverzügliche Information der Eltern und Schüler.
- **Vorfallregister:** Dokumentation aller Sicherheitsvorfälle im internen Verzeichnis der Schule.

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
| --- | --- | --- | --- |
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
| AT15 | CSV-Injektion | Name enthält `=1+2';cmd&#124;' ...` | Exportiertes CSV stellt Apostroph vor die Zelle |
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

## 15. KI-Datenflüsse, Lernassistenten und RAG [P/Ü]

### 15.1 Sprachmodelle im Unterricht

[P/Ü] Einsatz von KI-Sprachmodellen (LLM) als Tutoren:

- **Zero-Data Retention (ZDR):** Verträge mit Anbietern müssen garantieren, dass Prompts nicht dauerhaft gespeichert und nicht für das Training künftiger Modelle verwendet werden.
- **Prompt-Hygiene:** Schüler werden unterwiesen, keine Klarnamen, Adressen oder persönlichen Erlebnisse in Prompt-Felder einzugeben.

### 15.2 Retrieval-Augmented Generation (RAG)

[P] Bei schulischen RAG-Architekturen:

- Nur lehrplanrelevante Unterrichtsmaterialien und Aufgaben vektorisieren.
- Keine Zeugnisse, Förderpläne oder Schülerprofile in Vektordatenbanken ablegen.

### 15.3 Pädagogische Verantwortung

[P] KI-Ergebnisse sind reine Hilfsmittel. Keine Versetzungsentscheidung oder Benotung darf rein automatisiert getroffen werden (Art. 22 DSGVO).

### 15.4 Architektonische Schutz-Gates und k-Anonymität für KI-Systeme [P]

[P] Dreistufiges Sicherheitsmodell für KI-Lernanwendungen:

#### 1. Verarbeitungsstufen (L0 / C1 / C2)

- **Stufe L0 (Vollständig lokal):** Modell läuft ausschließlich im Schulnetz oder auf dem Endgerät (z. B. Ollama, llama.cpp). Keine Daten verlassen die Schule. Höchste Datenschutzstufe.
- **Stufe C1 (Cloud mit AVV und ZDR):** Europäischer Anbieter mit AVV (Art. 28 DSGVO) und vertraglichem Zero-Data-Retention. Direkte Schülerdaten (Namen, IDs) MÜSSEN vor Absenden des Prompts pseudonymisiert oder entfernt werden.
- **Stufe C2 (Öffentliche kommerzielle KI ohne Schulvertrag):** Nur vollständig anonymisierte, verallgemeinerte Anfragen ohne jeglichen Schüler- oder Schulbezug zulässig.

#### 2. Vorgaben zu k-Anonymität (k >= 5) und l-Diversität (l >= 2)

Bei der Aggregation von Schülerdaten für Analysen oder Vorhersagemodelle:

- **k-Anonymitätsschwelle:** Jede Gruppe mit identischen Quasi-Identifikatoren (z. B. Alter, Klasse, Geschlecht) MUSS mindestens $k = 5$ verschiedene Schüler umfassen. Kleinere Gruppen sind zu unterdrücken oder zu vergröbern.
- **l-Diversitätsschwelle:** Sensible Attribute innerhalb einer Gruppe müssen mindestens $l = 2$ verschiedene Ausprägungen aufweisen, um Homogenitätsangriffe zu verhindern.
- **Validierungsskript:** Einsatz des deterministischen Prüfskripts (`scripts/check_k_anonymity.py`) vor jedem Datenexport.

## 16. Schulisches Single Sign-On (SSO) [P]

[P] Föderierte Authentifizierung:

- Verwendung von Standards wie OpenID Connect (OIDC) oder SAML 2.0 (z. B. Shibboleth).
- Minimale Attributübermittlung (nur pseudonyme User-ID und Schulzugehörigkeit). Keine Übergabe kompletter Profile.
- Schutz von Tokens im Backend; keine Speicherung im ungeschützten Browser-Speicher.

## 17. Leitfaden für praktische Lösungen

### 17.1 Bereitstellungsmodi (M1 - M6)

Folgende Modi werden unterstützt:

- **M1 (Vollständig lokal / Offline):** Läuft lokal beim Lehrer ohne Internet (SQLite, CSV).
- **M2 (Schuleigener Server):** Web-Applikation auf schuleigenem Server oder Rechenzentrum.
- **M3 (Bildungs-Cloud mit AVV):** Offiziell beschaffte Plattform mit ADV-Vertrag.
- **M4 (Sicherheits- und Code-Audit):** Prüfung einer bestehenden Anwendung.
- **M5 (Lokaler KI-Tutor L0):** Lokale KI-Infrastruktur im Computerraum ohne Cloud-Abhängigkeit.
- **M6 (Hybride KI mit k-Anonymität):** Cloud-Anbindung C1 mit vorgeschalteter Filterung und k >= 5.

### 17.2 Referenzarchitektur

```text
[ Schüler-Browser / PWA ]
             │
             │ HTTPS (TLS 1.3 + HSTS)
             ▼
[ Reverse Proxy (Nginx / Caddy) ] ── (Angriffsschutz, CSP, Härtungs-Header)
             │
             │ Isoliertes Schulnetz
             ▼
[ Anwendungs-Server (Backend) ]
     ├── RBAC-Rechteprüfung und Sitzungsverwaltung
     ├── CSV-Härtung und Formelneutralisierung
     └── KI-Schutzgate (L0 / C1 / C2 mit k >= 5)
             │
             │ Verschlüsselte Verbindung
             ▼
[ Datenbank (PostgreSQL / SQLite WAL) ] (Verschlüsselung At Rest AES-256)
```

### 17.5 Vorlage für Modul-Steckbrief

Für jedes Anwendungsmodul ist ein Steckbrief zu erstellen:

1. **Modulname und didaktischer Zweck:** Kurzbeschreibung.
2. **Datenkategorien:** Erfasste Felder.
3. **Rechtsgrundlage:** Artikel der DSGVO und landesrechtliche Norm.
4. **Architekturstufe:** M1 - M6 sowie KI-Kategorie (L0 / C1 / C2).
5. **Schutzmaßnahmen:** Verschlüsselung, Sitzungsbereinigung und k-Anonymitätsprüfung.

## 18. Veröffentlichung, Dokumente und Folgeprodukte [E/Ü]

### 18.1 Veröffentlichung von Schülerfotos und Schülerarbeiten

[E/Ü] Auftritt der Schule in Web und Medien:

- **Schriftliche Einwilligung:** Freiwillige schriftliche Zustimmung der Erziehungsberechtigten vorab (Art. 6 Abs. 1 lit. a DSGVO, KUG).
- **Kopplungsverbot:** Die Foto-Einwilligung darf nicht mit der Schulanmeldung verknüpft werden.
- **Keine Klarnamen-Zuordnung:** Fotos im Web nicht mit vollständigem Vor- und Nachnamen und Klasse beschriften.

### 18.2 Rechtsaktualisierung und Upstream-Meldung

[P] Vorschläge zur Aktualisierung dieses Skills oder neuer behördlicher Leitlinien können im GitHub-Repository eingereicht werden:
`https://github.com/siberius/student-data-protection/issues` mit dem Label `legal-update`.

© 2026 Luděk Sušický. [MIT](https://opensource.org/license/mit). Überarbeitete Version 1.2 basiert auf dem ursprünglichen Leitfaden vom Oktober 2026; Urheberangaben, Lizenz und Änderungshinweise beibehalten. Externe Quellen behalten ihre Rechte.

## Lizenz (License)

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
