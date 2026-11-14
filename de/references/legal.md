# 2. DSGVO und deutsches Schuldatenschutzrecht

<!-- Generierte Referenz; bearbeiten Sie den eigenständigen Leitfaden. -->

Quellabschnitte: 2.

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

© 2026 Luděk Sušický. [MIT](https://opensource.org/license/mit). Überarbeitete Ausgabe der Version 1.2, basierend auf dem ursprünglichen Leitfaden vom Oktober 2026. Urheber-, Lizenz- und Änderungshinweise beibehalten.
