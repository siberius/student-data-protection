# 16. Authentification fédérée et ENT [P]

<!-- Référence générée ; modifier le guide autonome maintenu. -->

Sections sources: 16.

## 16. Authentification fédérée et ENT [P]

[P] Raccordement aux systèmes d'identité:

- Privilégiez les protocoles standardisés OpenID Connect (OIDC) ou SAML 2.0 via l'ENT ou le GAR.
- Ne demandez que les attributs strictement nécessaires (identifiant pseudonymisé `sub` et profil d'appartenance).
- Conservez les jetons de manière sécurisée côté serveur sans les exposer dans le stockage du navigateur.

© 2026 Luděk Sušický. [MIT](https://opensource.org/license/mit). Édition révisée de la version 1.2, basée sur le guide initial d'octobre 2026. Conserver les mentions d'auteur, de licence et les avis de modification.
