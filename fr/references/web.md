# 9. Web, PWA et équipements partagés [P]

<!-- Référence générée ; modifier le guide autonome maintenu. -->

Sections sources: 9.

## 9. Web, PWA et équipements partagés [P]

[P] Sécurité sur postes partagés:

- **Postes partagés en salle de classe:** L'action de déconnexion DOIT vider intégralement les stockages locaux du navigateur (`localStorage`, `sessionStorage`, `IndexedDB`) pour empêcher la consultation par l'élève suivant.
- **Content Security Policy (CSP):** Politique CSP stricte bloquant les domaines tiers non approuvés et les scripts inline non signés.
- **Absence de traceurs tiers:** Interdiction totale d'intégrer des outils d'analyse marketing ou des pixels publicitaires (Google Analytics, Meta) dans les outils scolaires.

© 2026 Luděk Sušický. [MIT](https://opensource.org/license/mit). Édition révisée de la version 1.2, basée sur le guide initial d'octobre 2026. Conserver les mentions d'auteur, de licence et les avis de modification.
