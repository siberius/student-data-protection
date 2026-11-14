# Schülerdatenschutz in schulischen Anwendungen

[![Skills.sh](https://img.shields.io/badge/skills.sh-Install-blue)](https://skills.sh/siberius/student-data-protection)

Sicherheitsprofil und Assistenten-Skill für Schulanwendungen (Deutschland und EU).

> Version: 1.2 · Konformität: DSGVO (EU 2016/679), KI-Verordnung (AI Act, EU 2024/1689), Bundesdatenschutzgesetz (BDSG) und Schulgesetze der Länder.

## Installation und Schnellstart

Installieren Sie den Skill in Ihren Coding-Assistenten (Claude Code, Cursor, Codex, Antigravity, OpenCode, Cline u. a.) über die CLI von [skills.sh](https://skills.sh):

```bash
# Installation der deutschen Ausgabe (Deutschland / EU)
npx skills add siberius/student-data-protection --skill schuelerdatenschutz --full-depth -g -a codex

# Alle 7 verfügbaren Sprachversionen anzeigen
npx skills add siberius/student-data-protection --full-depth --list
```

Temporäre Nutzung ohne dauerhafte Installation:

```bash
npx skills use siberius/student-data-protection --skill schuelerdatenschutz --full-depth --agent codex
```

## Dokumentationsübersicht

- **Eigenständiger Leitfaden auf Deutsch:** [docs/schuelerdatenschutz.md](docs/schuelerdatenschutz.md)
- **Rechts- und Quellenregister:** [docs/quellenregister.md](docs/quellenregister.md)
- **Evaluierungsszenarien des Skills:** [docs/skill-evaluierung.md](docs/skill-evaluierung.md)
- **Natives Skill-Modul (DE):** [de/SKILL.md](de/SKILL.md)

## Kernprinzipien des Profils

1. **Verantwortung der Schulleitung und DSB-Einbindung:** Vor Einführung digitaler Schulanwendungen ist die formale Entscheidung der Schulleitung nach Einbindung des behördlichen DSB erforderlich.
2. **Strikte Auftragsverarbeitung (Art. 28 DSGVO):** Kein Einsatz externer Clouddienste oder KI ohne rechtsgültigen AV-Vertrag.
3. **Architekturstufen für KI (L0 / C1 / C2):** Klarer Vorrang für lokale On-Premise-Modelle (L0) sowie Pseudonymisierung vor Cloud-Nutzung (C1).
4. **k-Anonymität (k >= 5) und l-Diversität (l >= 2):** Mathematische Absicherung statistischer Bildungsdaten vor Weitergabe an Auswertungs- oder Vorhersagesysteme.
5. **Kontinuierliche Rechtsaktualität:** Automatische Prüfung des Quellenalters und strukturierte Upstream-Meldung von Rechtsänderungen via GitHub Issues.

### Autor

**Luděk Sušický** - Biologe, Gymnasial- und Hochschullehrer für Informatikfächer

- E-Mail: [ludek.susicky@gmail.com](mailto:ludek.susicky@gmail.com)
- X: [@ludeksusicky](https://x.com/ludeksusicky)
- LinkedIn: [Luděk Sušický](https://www.linkedin.com/in/ludek-susicky/)
- GitHub: [@siberius](https://github.com/siberius) - weitere Bildungsprojekte und Open-Source-Anwendungen

### Lizenz

Dieses Projekt steht unter der MIT-Lizenz. Details finden sich in der Datei [LICENSE](LICENSE).
