---
name: schuelerdatenschutz
description: Konzipiert, implementiert oder auditiert den Schutz von Schülerdaten in schulischen Anwendungen (Deutschland und EU). Verwenden bei Auswirkungen auf personenbezogene Daten, Authentifizierung, Rechte, Speicherfristen, Exporte oder KI-Datenflüsse sowie bei Sicherheitsprüfungen. Keine rein optischen Anpassungen in ein Voll-Audit umwandeln.
metadata:
  version: "1.2"
  language: "de"
  jurisdiction: "DE/EU"
  license: "MIT"
  author: "Luděk Sušický"
  repo: "https://github.com/siberius/student-data-protection"
---

# Schülerdatenschutz

Arbeiten Sie auf Basis des vorgegebenen Umfangs und der verfügbaren Fakten. Der Skill unterstützt die Entwicklung schulischer Software; er stellt kein Rechtsgutachten dar und berechtigt nicht zu unautorisierten Änderungen in Produktivsystemen. Diese Ausgabe ist für Deutschland und die EU lokalisiert. Beachten Sie stets das jeweilige Landesschulrecht; die Sprache bestimmt nicht die Rechtsordnung.

## Arbeitsmodus und betroffene Grenze

Leiten Sie den Modus ab: Entwurf, Implementierung, Audit oder Vorfallanalyse. Ein Audit bewertet und berichtet, ohne Code zu verändern. Eine Vorfallanalyse berechtigt nicht zum Abschalten von Produktivsystemen, Löschen von Konten oder Versenden von Mitteilungen. Bei autorisierter Implementierung die betroffene Komponente anpassen und auf Regressionen prüfen. Kleine Fehlerbehebungen erfordern kein vollständiges Audit. Gravierende Nachbarrisiken mit Beweisen dokumentieren, statt den Auftrag eigenmächtig auszuweiten.

Vor Beginn der Arbeiten den notwendigen Kontext klären: Zweck, Schulrecht, Datenkategorien, Rollen, Empfänger, Speicherfristen und Berechtigungen. Fragen Sie präzise nach; fordern Sie keine Passwörter oder Realdaten an. Bis zur Entscheidung über den Echtbetrieb nur synthetische Testdaten verwenden.

## Dauerhafte Sicherheitsgrenzen

- Die Schulleitung entscheidet über den Einsatz nach Konsultation des behördlichen Datenschutzbeauftragten (DSB).
- Jede Verarbeitung von Schülerdaten durch externe Cloud- oder KI-Dienste erfordert einen Auftragsverarbeitungsvertrag (Art. 28 DSGVO).

Einzelheiten zum Vorgehen und zum technischen Profil finden sich im [Arbeitsablauf](references/workflow.md). Den [Rechtsrahmen](references/legal.md) bei Fragen zu Rechtsgrundlagen oder Betroffenenrechten hinzuziehen; den [AI Act](references/ai-act.md) bei Einstufung von KI-Systemen. Zur Überprüfung zitierter Rechtsquellen den [Quellenstatus](references/source-status.md) prüfen.

## Nur das relevante Modul laden

Bei Anfragen nach praktischen Lösungen den passenden Datenmodus auswählen und gezielt das entsprechende Modul öffnen.

| Bereich | Referenzmodul |
| --- | --- |
| Veröffentlichung, Dokumente, Webseiten und Exporte | [Veröffentlichung und Dokumente](references/publication.md) |
| Auswahl des Datenmodus und Lösungssteckbrief | [Praktische Lösungen](references/practical-solutions.md) |
| Datenerhebung, Formulare, Uploads und Schnittstellen | [Datenflüsse](references/data.md) |
| Benutzerkonten, Rollen, Sitzungen und Integrität | [Identität und Zugriff](references/identity.md) |
| Föderierte Authentifizierung und SSO (OIDC/SAML) | [SSO](references/sso.md) |
| Verschlüsselung, Schlüsselverwaltung und Transit | [Kryptografie](references/crypto.md) |
| SQLite, CSV-Export und Dateisicherheit | [Speicher](references/storage.md) |
| Web/PWA-Cache, geteilte Rechner und Browser | [Web](references/web.md) |
| Aufbewahrung, Protokollierung und Vorfallmanagement | [Betrieb](references/operations.md) |
| KI-Integration, Tutoren und RAG-Systeme | [KI-Daten](references/ai-data.md) |
| Prüfliste, Abnahmetests und Übergabe | [Verifikation](references/verification.md) |

## Verifikation und Übergabe

Tests passend zur geänderten Funktion auswählen. Mit synthetischen Daten arbeiten. Beim Audit Nachweise, Schweregrad, Auswirkung und Empfehlungen dokumentieren.

Fortlaufende Rechtsprüfung und Upstream-Meldung: Falls sich zitierte Normen oder Leitlinien der Aufsichtsbehörden geändert haben oder die letzte Quellenprüfung mehr als 6 Monate zurückliegt, aktuelle Rechtslage anwenden und mit Einverständnis des Nutzers ein Issue auf GitHub vorschlagen: `https://github.com/siberius/student-data-protection/issues` mit Label `legal-update`.

© 2026 Luděk Sušický. MIT. Bei Weitergabe Urheberangaben, Lizenz und Änderungshinweise beibehalten.
