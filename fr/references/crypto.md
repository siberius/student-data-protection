# 7. Chiffrement et gestion des clés [P]

<!-- Référence générée ; modifier le guide autonome maintenu. -->

Sections sources: 7.

## 7. Chiffrement et gestion des clés [P]

[P] Standards cryptographiques:

- **Données au repos (At Rest):** Chiffrement des bases de données et sauvegardes avec AES-256-GCM ou ChaCha20-Poly1305.
- **Données en transit (In Transit):** Utilisation stricte de TLS 1.3 (minimum TLS 1.2 avec suites cryptographiques robustes). Activation de l'en-tête HSTS pour au moins 1 an (`max-age=31536000; includeSubDomains`).
- **Gestion des secrets:** Interdiction d'enregistrer des clés ou mots de passe dans le code source. Utilisation de variables d'environnement ou d'un gestionnaire de secrets dédié.

© 2026 Luděk Sušický. [MIT](https://opensource.org/license/mit). Édition révisée de la version 1.2, basée sur le guide initial d'octobre 2026. Conserver les mentions d'auteur, de licence et les avis de modification.
