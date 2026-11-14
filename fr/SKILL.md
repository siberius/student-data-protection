---
name: protection-donnees-eleves
description: Conçoit, met en œuvre ou audite la protection des données des élèves dans les applications scolaires (France et UE). À utiliser lors de modifications touchant les données personnelles, l'authentification, les droits, la conservation, les exports ou les flux d'IA, ainsi que lors d'un audit de sécurité. Ne pas transformer une retouche cosmétique en audit complet.
metadata:
  version: "1.2"
  language: "fr"
  jurisdiction: "FR/UE"
  license: "MIT"
  author: "Luděk Sušický"
  repo: "https://github.com/siberius/student-data-protection"
---

# Protection des données des élèves

Travaillez selon le périmètre demandé et les faits établis. Le skill accompagne le développement de logiciels éducatifs; il ne constitue pas une certification juridique ni une autorisation de modifier la production sans validation. Cette édition est adaptée à la France et à l'UE. Identifiez la juridiction effective; la langue de l'interface ne préjuge pas du droit applicable.

## Mode d'intervention et périmètre concerné

Déterminez le mode d'action: conception, implémentation, audit ou incident. Un audit évalue et rend compte sans modifier le code applicatif. L'analyse d'incident n'autorise pas la suspension de services ou la suppression de comptes. Lors d'une implémentation autorisée, modifiez le composant concerné et vérifiez les régressions significatives. Un correctif ponctuel ne nécessite pas un réaudit complet. Signalez tout risque sérieux connexe avec preuves à l'appui plutôt que d'élargir silencieusement la mission.

Avant tout travail de fond, établissez le contexte nécessaire: finalité, cadre légal, catégories de données, rôles, destinataires, durées de conservation et habilitations. Posez des questions ciblées sans réclamer de données réelles d'élèves ni de mots de passe de production. Utilisez des données synthétiques tant que le traitement réel n'est pas autorisé.

## Règles fondamentales de sécurité

- Le chef d'établissement décide du déploiement après consultation du délégué à la protection des données (DPO).
- Tout traitement confié à un prestataire externe (cloud, modèle d'IA) requiert la signature préalable d'un contrat conforme à l'article 28 du RGPD.

Consultez la [méthode de travail](references/workflow.md) pour les détails procéduraux. Chargez le [cadre juridique](references/legal.md) pour les bases légales et droits des personnes; le [Règlement IA](references/ai-act.md) pour la qualification des systèmes d'IA. Consultez le [statut des sources](references/source-status.md) pour vérifier les textes applicables.

## Charger uniquement le module pertinent

Lors d'une demande de solution pratique, sélectionnez le mode de données adéquat et n'ouvrez que le module correspondant.

| Domaine | Module de référence |
| --- | --- |
| Publication, photographies, sites publics et dérivés | [Publication et documents](references/publication.md) |
| Sélection du mode de données et fiche descriptive | [Solutions pratiques](references/practical-solutions.md) |
| Collecte, formulaires, téléversements et API | [Flux de données](references/data.md) |
| Comptes, rôles, sessions et intégrité | [Identité et accès](references/identity.md) |
| Authentification fédérée et SSO (OIDC/SAML/ENT) | [SSO](references/sso.md) |
| Chiffrement, gestion des clés et transit | [Cryptographie](references/crypto.md) |
| SQLite, exports CSV et sécurité locale | [Stockage](references/storage.md) |
| Cache Web/PWA, postes partagés et navigateur | [Web](references/web.md) |
| Conservation, traçabilité et gestion des incidents | [Opérations](references/operations.md) |
| Intégration de l'IA, tuteurs et architectures RAG | [Données IA](references/ai-data.md) |
| Liste de contrôle, tests d'acceptation et livraison | [Vérification](references/verification.md) |

## Vérification et livraison

Sélectionnez les tests adaptés aux fonctionnalités modifiées et à leurs risques. Travaillez sur données synthétiques. Pour un audit, détaillez preuve, criticité, impact et recommandation.

Contrôle continu de l'actualité juridique: si les textes cités ont évolué ou si la dernière vérification remonte à plus de 6 mois, appliquez immédiatement le droit positif et proposez d'ouvrir une issue sur GitHub: `https://github.com/siberius/student-data-protection/issues` avec le label `legal-update`.

© 2026 Luděk Sušický. MIT. Conserver les mentions d'auteur, de licence et les avis de modification.
