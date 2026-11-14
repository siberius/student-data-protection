# 12. Liste de contrôle avant mise en production

<!-- Référence générée ; modifier le guide autonome maintenu. -->

Sections sources: 12, 13, 14.

## 12. Liste de contrôle avant mise en production

Points de contrôle obligatoires:
1. Base légale identifiée et DPO consulté.
2. Contrat de sous-traitance (art. 28 RGPD) signé avec tous les prestataires cloud et IA.
3. Mentions d'information (art. 13-14 RGPD) rédigées dans un langage clair et adapté.
4. Minimisation appliquée: identifiants nationaux exclus des URL, données médicales écartées.
5. Mots de passe protégés par Argon2id; cookies sécurisés par HttpOnly, Secure, SameSite.
6. Habilitations RBAC vérifiées et étanches aux attaques IDOR.
7. TLS 1.3 forcé et chiffrement AES-256 des données au repos.
8. Exports CSV immunisés contre l'injection de formules.
9. Déconnexion assurant le nettoyage complet des caches locaux sur postes partagés.
10. Absence intégrale de traceurs publicitaires et analytiques tiers.

## 13. Scénarios de test d'acceptation (Acceptance tests)

Tableau des 38 scénarios de test d'acceptation obligatoires:

| Identifiant | Domaine | Scénario de test | Résultat attendu |
|---|---|---|---|
| AT01 | Base légale | Traitement de données dans le registre obligatoire des élèves | Référence à l'obligation légale et au Code de l'éducation |
| AT02 | Consentement | Inscription à un cours obligatoire du programme scolaire | Absence de demande de consentement parental comme condition |
| AT03 | Données sensibles | Inscription d'un élève sur un exerciseur de mathématiques | Le formulaire ne contient aucun champ de santé ou de religion |
| AT04 | Clés primaires | Consultation du profil élève dans l'URL du navigateur | Utilisation d'un UUIDv4 aléatoire, absence du numéro INE |
| AT05 | Métadonnées | Téléversement d'une photo de copie manuscrite par un élève | Nettoyage des métadonnées EXIF avant stockage sur le serveur |
| AT06 | Robustesse mot de passe | Tentative de définition du mot de passe « 123456 » | Rejet par le système avec exigence de 12 caractères minimum |
| AT07 | Hachage sécurisé | Inspection de la table des utilisateurs en base | Mots de passe hachés avec Argon2id ou bcrypt robuste |
| AT08 | Attributs de session | Analyse des en-têtes Set-Cookie | Présence des attributs HttpOnly, Secure, SameSite=Lax/Strict |
| AT09 | Inactivité | Absence d'activité d'un élève pendant 35 minutes | Session invalidée, réauthentification exigée |
| AT10 | Contrôle IDOR | L'élève A remplace son ID par celui de l'élève B | Le serveur renvoie une erreur HTTP 403 Forbidden |
| AT11 | Droits applicatifs | Un élève appelle l'API de saisie des notes | Requête rejetée avec code HTTP 403 Forbidden |
| AT12 | Cloisonnement famille | Un parent tente d'afficher les résultats d'un autre enfant | Accès refusé, affichage limité aux seuls enfants rattachés |
| AT13 | Chiffrement en transit | Tentative d'accès via le protocole non sécurisé HTTP | Redirection automatique 301/308 vers HTTPS (TLS 1.3) |
| AT14 | En-tête HSTS | Analyse des en-têtes HTTP de réponse | En-tête Strict-Transport-Security actif |
| AT15 | Injection CSV | Un nom d'élève contient `=1+2';cmd|' ...` | L'export CSV insère une apostrophe en tête de cellule |
| AT16 | Injection SQLite | Saisie de la chaîne `' OR 1=1 --` dans la recherche | Requête préparée exécutée, aucune fuite ni erreur |
| AT17 | Emplacement SQLite | Tentative de téléchargement direct du fichier `.sqlite` | Requête rejetée (403/404), fichier hors de la racine Web |
| AT18 | Postes partagés | Clic sur « Se déconnecter » en salle informatique | Nettoyage complet du localStorage et suppression des jetons |
| AT19 | En-têtes CSP | Injection d'un script tiers non autorisé | Blocage de l'exécution par la directive CSP du navigateur |
| AT20 | Télémétrie | Surveillance du trafic réseau de l'application | Aucune requête vers Google Analytics, Meta ou régies |
| AT21 | Sécurité des logs | Examen des journaux techniques de l'application | Absence de mots de passe en clair et d'informations privées |
| AT22 | Registre d'incidents | Simulation d'une fuite de données de test | Incident consigné, formulaire de notification CNIL préparé |
| AT23 | IA Émotions | Tentative d'installation d'une caméra de suivi de l'humeur | Système bloqué au titre des pratiques interdites (art. 5 AI Act) |
| AT24 | IA Haut risque | Utilisation de l'IA pour l'évaluation finale d'examens | Classification à haut risque, formalisation et contrôle humain |
| AT25 | Contrôle humain IA | L'IA propose une note pour une rédaction libre | L'enseignant conserve la possibilité d'ajuster l'évaluation |
| AT26 | Contrat IA | Intégration d'un service commercial d'IA générative | Contrat art. 28 RGPD signé avant tout traitement |
| AT27 | Entraînement IA | Examen des conditions générales du fournisseur d'IA | Garantie écrite de non-utilisation pour l'entraînement public |
| AT28 | Authentification SSO | Connexion via l'ENT ou la fédération Éducation | Aucun mot de passe élève transmis à l'application tierce |
| AT29 | Départ d'élève | Un élève quitte l'établissement en fin de cursus | Compte désactivé et données archivées selon les règles |
| AT30 | Droit d'accès | Demande d'accès aux données selon l'art. 15 du RGPD | Génération d'un export exhaustif des données de l'élève |
| AT31 | Secrets dans le code | Audit du référentiel de code source du projet | Absence totale de clés d'API ou de mots de passe figés |
| AT32 | Restauration backup | Test de restauration de la sauvegarde de la base | Données restaurées avec succès, sauvegarde chiffrée |
| AT33 | Hachage obsolète | Découverte d'algorithmes MD5 ou SHA-1 dans l'ancien code | Remplacement immédiat par Argon2id |
| AT34 | Hébergement hors EEE | Configuration d'un stockage cloud aux USA sans garanties | Blocage de la configuration pour défaut de base légale |
| AT35 | Transparence de l'IA | L'élève dialogue avec un agent conversationnel d'aide | Notification claire indiquant qu'il s'agit d'une machine |
| AT36 | Périmètre enseignant | Un enseignant d'anglais tente d'éditer les notes d'histoire | Accès en écriture restreint à ses seules attributions |
| AT37 | Passerelle IA L0/C1/C2 | Envoi d'une requête élève contenant nom et classe | La passerelle anonymise les données ou route vers un modèle L0 |
| AT38 | k-anonymat IA | Calcul de statistiques scolaires avec un sous-groupe de 3 | Blocage de l'exportation par le validateur (seuil k >= 5) |

## 14. Modalités de restitution et limites des déclarations

Lors de la remise de rapports ou de préconisations techniques:
- Formulez les constats de manière rigoureuse, factuelle et constructive.
- Distinguez formellement les faits techniques constatés dans le code des recommandations générales.
- Ne garantissez jamais une « conformité RGPD à 100% » ni une « certification absolue », la conformité relevant d'une démarche continue et organisationnelle.

© 2026 Luděk Sušický. [MIT](https://opensource.org/license/mit). Édition révisée de la version 1.2, basée sur le guide initial d'octobre 2026. Conserver les mentions d'auteur, de licence et les avis de modification.
