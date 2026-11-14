# 4. Datenmodell, Erhebung und Datenminimierung [P]

<!-- Generierte Referenz; bearbeiten Sie den eigenständigen Leitfaden. -->

Quellabschnitte: 4.

## 4. Datenmodell, Erhebung und Datenminimierung [P]

[P] Das Datenmodell MUSS dem Grundsatz der Datenminimierung entsprechen (Art. 5 Abs. 1 lit. c DSGVO):

- **Identifikatoren:** Generierte UUIDv4-Schlüssel als Primärschlüssel verwenden. Niemals Schüleraktennummern oder Klarnamen in URLs, Dateinamen oder Client-Speichern nutzen.
- **Optionale Felder:** Telefonnummern, Wohnanschriften oder Fotos dürfen in fachbezogenen Lern-Apps keine Pflichtfelder sein.
- **Besondere Kategorien:** Keine Speicherung von Krankheitsdiagnosen. Für Nachteilsausgleiche (z. B. Zeitzugabe) genügt ein technischer Parameter (`extra_time_factor: 1.25`) ohne Angabe des medizinischen Befunds.
- **Metadaten:** EXIF-Metadaten aus von Schülern hochgeladenen Aufgabenbildern vor dem Speichern auf dem Server vollständig entfernen.

© 2026 Luděk Sušický. [MIT](https://opensource.org/license/mit). Überarbeitete Ausgabe der Version 1.2, basierend auf dem ursprünglichen Leitfaden vom Oktober 2026. Urheber-, Lizenz- und Änderungshinweise beibehalten.
