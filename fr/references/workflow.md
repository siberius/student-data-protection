# 1. Interprétation des exigences et méthode de travail de l'assistant

<!-- Référence générée ; modifier le guide autonome maintenu. -->

Sections sources: 1.

## 1. Interprétation des exigences et méthode de travail de l'assistant

- **[J] Exigence juridique:** contraignante lorsque les conditions décrites sont réunies. Le texte de loi prévaut sur toute recommandation technique.
- **[P] Profil de sécurité:** choix d'implémentation spécifique de ce skill. Les termes DOIT/NE PEUT PAS dans les sections techniques définissent ce profil et non l'obligation littérale du RGPD. Toute dérogation doit être documentée avec risque, mesure compensatoire, test et décision du chef d'établissement.
- **[R] Recommandation:** extension opportune selon le niveau de risque et les spécificités du déploiement.
- **[V] À vérifier:** aspect dépendant de l'usage effectif, du droit en vigueur ou d'une configuration non confirmée. Ne pas considérer comme satisfait sans preuve.

1. Déterminez le mode d'intervention: conception, implémentation, audit ou incident. Un audit analyse et rend compte sans modifier le code de l'application. L'analyse d'incident ne donne pas l'autorisation d'éteindre des services, supprimer des comptes ou diffuser des alertes. Agissez strictement dans le cadre de l'autorisation reçue.
2. Exploitez le contexte connu et déterminez finalité, flux de données, rôles et évolution du risque. Ne demandez que les informations manquantes ayant un impact direct sur les décisions. Lors d'un correctif mineur, testez le périmètre touché et les régressions; ne relancez pas un audit complet. Documentez et signalez tout risque voisin significatif; n'étendez pas le périmètre en silence.
3. Cartographiez données, destinataires, identité, habilitations, durées de conservation et menaces. Maintenez une architecture éprouvée et des protections effectives. En l'absence de finalité, de base légale ou de décision de déploiement, utilisez des données synthétiques.
4. Lors de la conception, préconisez des mesures proportionnées. Lors d'une implémentation autorisée, appliquez-les en précisant les emplacements dans le code ou la configuration. Lors d'un audit, détaillez gravité, preuve, impact, recommandation et vérification requise. Distinguez l'anomalie constatée de la simple hypothèse.
5. Sélectionnez les scénarios de test d'acceptation selon la fonction et le niveau de risque. Qualifiez le résultat: réussi, échoué, non exécuté ou non applicable avec justification. Un plan de test ne prouve pas son exécution.
6. Avant toute mise en production, vérifiez la base légale, l'évaluation requise et la réglementation actuelle. Le chef d'établissement décide du déploiement après consultation en temps utile du DPO. Sans base légale ou sans analyse d'impact, ne recommandez pas le traitement; poursuivez le travail autorisé en environnement de test avec données synthétiques.

### 1.4 Fraîcheur juridique continue et remontée vers GitHub [P]

Le profil de sécurité de ce skill impose que toute analyse juridique s'appuie sur le droit positif à jour (RGPD, Règlement sur l'IA, Loi Informatique et Libertés, doctrines de la CNIL et consignes ministérielles).

1. **Règle d'ancienneté des sources (> 6 mois):** Si plus de 6 mois se sont écoulés depuis la dernière revue des sources, l'assistant doit vérifier la validité des textes cités.
2. **Prise en compte immédiate pour l'utilisateur:** En cas d'évolution législative ou doctrinale, l'assistant applique immédiatement la règle actuelle dans sa réponse et en informe l'utilisateur.
3. **Remontée amont (GitHub Issue):** Avec l'accord de l'utilisateur, l'assistant propose d'ouvrir une issue sur le dépôt: `https://github.com/siberius/student-data-protection/issues` avec l'étiquette `legal-update`.

© 2026 Luděk Sušický. [MIT](https://opensource.org/license/mit). Édition révisée de la version 1.2, basée sur le guide initial d'octobre 2026. Conserver les mentions d'auteur, de licence et les avis de modification.
