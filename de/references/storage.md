# 8. CSV und SQLite [P]

<!-- Generierte Referenz; bearbeiten Sie den eigenständigen Leitfaden. -->

Quellabschnitte: 8.

## 8. CSV und SQLite [P]

[P] Lokale Datenspeicherung und Exporte:

- **CSV-Injektionsschutz:** Felder, die mit `=`, `+`, `-`, `@`, Tabulator oder Zeilenumbruch beginnen, MÜSSEN beim Export durch ein vorangestelltes Apostroph (`'`) neutralisiert werden, um Makroausführung in Tabellenkalkulationen (Excel, Calc) zu verhindern.
- **SQLite:** Einsatz des WAL-Modus (Write-Ahead Logging) und Aktivierung von Fremdschlüsseln (`PRAGMA foreign_keys = ON;`). Die Datenbankdatei darf nicht im öffentlich erreichbaren Web-Root liegen.
- **Prepared Statements:** Ausschließlich parametrisierte SQL-Abfragen zur Verhinderung von SQL-Injektionen.

© 2026 Luděk Sušický. [MIT](https://opensource.org/license/mit). Überarbeitete Ausgabe der Version 1.2, basierend auf dem ursprünglichen Leitfaden vom Oktober 2026. Urheber-, Lizenz- und Änderungshinweise beibehalten.
