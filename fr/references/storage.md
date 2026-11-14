# 8. CSV et SQLite [P]

<!-- Référence générée ; modifier le guide autonome maintenu. -->

Sections sources: 8.

## 8. CSV et SQLite [P]

[P] Fichiers locaux et bases embarquées:
- **Protection anti-injection CSV:** Lors de l'exportation de données d'élèves, tout champ débutant par `=`, `+`, `-`, `@`, tabulation ou retour chariot DOIT être précédé d'une apostrophe (`'`) pour empêcher l'exécution de macros malveillantes dans les tableurs.
- **Mode SQLite:** Utilisation du mode WAL (Write-Ahead Logging) et activation des clés étrangères (`PRAGMA foreign_keys = ON;`). La base SQLite doit impérativement être placée hors de l'arborescence publique du serveur Web.
- **Requêtes paramétrées:** Recours exclusif aux requêtes préparées (Prepared Statements) pour éradiquer tout risque d'injection SQL.

© 2026 Luděk Sušický. [MIT](https://opensource.org/license/mit). Édition révisée de la version 1.2, basée sur le guide initial d'octobre 2026. Conserver les mentions d'auteur, de licence et les avis de modification.
