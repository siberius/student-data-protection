# 5. Authentifizierung, Einladungen und Sitzungen [P]

<!-- Generierte Referenz; bearbeiten Sie den eigenständigen Leitfaden. -->

Quellabschnitte: 5, 6.

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

© 2026 Luděk Sušický. [MIT](https://opensource.org/license/mit). Überarbeitete Ausgabe der Version 1.2, basierend auf dem ursprünglichen Leitfaden vom Oktober 2026. Urheber-, Lizenz- und Änderungshinweise beibehalten.
