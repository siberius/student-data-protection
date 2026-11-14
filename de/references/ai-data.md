# 15. KI-Datenflüsse, Lernassistenten und RAG [P/Ü]

<!-- Generierte Referenz; bearbeiten Sie den eigenständigen Leitfaden. -->

Quellabschnitte: 15.

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

© 2026 Luděk Sušický. [MIT](https://opensource.org/license/mit). Überarbeitete Ausgabe der Version 1.2, basierend auf dem ursprünglichen Leitfaden vom Oktober 2026. Urheber-, Lizenz- und Änderungshinweise beibehalten.
