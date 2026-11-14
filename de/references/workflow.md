# 1. Auslegung der Anforderungen und Arbeitsweise des Assistenten

<!-- Generierte Referenz; bearbeiten Sie den eigenständigen Leitfaden. -->

Quellabschnitte: 1.

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

© 2026 Luděk Sušický. [MIT](https://opensource.org/license/mit). Überarbeitete Ausgabe der Version 1.2, basierend auf dem ursprünglichen Leitfaden vom Oktober 2026. Urheber-, Lizenz- und Änderungshinweise beibehalten.
