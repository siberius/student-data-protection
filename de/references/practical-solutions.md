# 17. Leitfaden für praktische Lösungen

<!-- Generierte Referenz; bearbeiten Sie den eigenständigen Leitfaden. -->

Quellabschnitte: 17.

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

```
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

© 2026 Luděk Sušický. [MIT](https://opensource.org/license/mit). Überarbeitete Ausgabe der Version 1.2, basierend auf dem ursprünglichen Leitfaden vom Oktober 2026. Urheber-, Lizenz- und Änderungshinweise beibehalten.
