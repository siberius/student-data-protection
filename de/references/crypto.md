# 7. Verschlüsselung und Schlüsselverwaltung [P]

<!-- Generierte Referenz; bearbeiten Sie den eigenständigen Leitfaden. -->

Quellabschnitte: 7.

## 7. Verschlüsselung und Schlüsselverwaltung [P]

[P] Kryptografische Standards:

- **Ruhende Daten (At Rest):** Verschlüsselung von Datenbanken und Backups mit AES-256-GCM oder ChaCha20-Poly1305.
- **Übertragene Daten (In Transit):** Erzwingung von TLS 1.3 (mindestens TLS 1.2 mit Forward Secrecy). Aktiviertes HSTS für mindestens 1 Jahr (`max-age=31536000; includeSubDomains`).
- **Schlüsselmanagement:** Keine kryptografischen Schlüssel im Quellcode oder Repository. Verwendung sicherer Secret-Stores oder Umgebungsvariablen.

© 2026 Luděk Sušický. [MIT](https://opensource.org/license/mit). Überarbeitete Ausgabe der Version 1.2, basierend auf dem ursprünglichen Leitfaden vom Oktober 2026. Urheber-, Lizenz- und Änderungshinweise beibehalten.
