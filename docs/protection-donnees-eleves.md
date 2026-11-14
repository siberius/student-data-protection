# Protection des données des élèves dans les applications scolaires

> Ce document constitue un profil de sécurité pratique pour les applications scolaires. Il ne constitue pas un conseil juridique ni une certification de conformité. Avant tout traitement de données réelles, le responsable de traitement prend la décision de déploiement après évaluation appropriée et consultation préalable du délégué à la protection des données (DPO).

**Version:** 1.2 · **Langue et juridiction:** français, France / UE · **Vérification initiale des sources:** 22 octobre 2026 · **Édition:** 14 novembre 2026. Mesures de sécurité pour les modèles d'IA, k-anonymat (k >= 5), l-diversité (l >= 2) et validation par script complétées le 14 novembre 2026.

Utilisez ce skill autonome lors de la conception, de la mise en œuvre ou de l'audit d'applications qui collectent, stockent, affichent, évaluent ou partagent des données à caractère personnel d'élèves, de leurs représentants légaux ou d'enseignants. Il couvre les registres scolaires, formulaires, suivis de présence, devoirs, portfolios, communications, inscriptions aux activités, évaluations et outils pédagogiques d'IA. Les données peuvent inclure noms, coordonnées, classes, notes, fichiers, messages, résultats d'épreuves, journaux techniques ainsi qu'identifiants de session et d'appareils.

La base repose sur la protection tout au long du cycle de vie des données. Les contrôles Web et PWA s'appliquent là où la technologie est présente ; les clients mobiles ou de bureau requièrent des garanties adaptées à la plateforme. CSV et SQLite constituent des choix de conception pris en charge, non une architecture obligatoire unique. N'ajoutez pas d'évaluations, de modèles d'IA ou d'authentification par code uniquement parce que ce skill les décrit.

Distinguez **compte durable avec identité vérifiée**, **participation ponctuelle limitée** et **collecte publique sans compte**. Le nom, la classe, l'appareil ou la connaissance d'un code partagé ne prouvent pas l'identité. Utilisez une authentification proportionnée aux enjeux du dossier et à l'historique scolaire de l'élève. Un code à usage unique ou QR code est un module facultatif pour des activités ponctuelles, non un accès universel aux données scolaires.

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

## 2. RGPD et cadre juridique français

### 2.1 Bases légales en milieu scolaire français

[J] Tout traitement de données scolaires doit reposer sur une base légale valide (art. 6 et art. 9 du RGPD):
- **Art. 6 par. 1 point c du RGPD (Obligation légale):** Tenue du registre des élèves, livret scolaire unique (LSU), appel quotidien et gestion des examens sur la base du Code de l'éducation.
- **Art. 6 par. 1 point e du RGPD (Mission d'intérêt public):** Accomplissement de la mission éducative, pédagogique et d'encadrement des élèves.
- **Art. 6 par. 1 point a du RGPD (Consentement):** Strictement réservé aux activités facultatives (publication de photos sur les réseaux sociaux, clubs péri-éducatifs, sorties facultatives). Le consentement ne peut conditionner la scolarité obligatoire (l'article 45 de la Loi Informatique et Libertés fixe l'âge de la majorité numérique à 15 ans pour les services en ligne).
- **Art. 9 du RGPD (Données sensibles):** Informations médicales (projets d'accueil individualisé - PAI, aménagements pour handicap) traitées sur la base de textes législatifs protecteurs pour assurer la sécurité et l'inclusion.

### 2.2 Responsabilité et délégué à la protection des données (DPO)

[J] Le responsable de traitement est l'établissement scolaire (représenté par le chef d'établissement pour le second degré ou l'autorité académique pour le premier degré).
- **Contrat de sous-traitance (art. 28 du RGPD):** Tout outil logiciel externe, espace numérique ou solution d'IA requiert un contrat formel de sous-traitance fixant les obligations de sécurité et de confidentialité.
- **Délégué à la Protection des Données (DPO):** La désignation d'un DPO est obligatoire pour les établissements publics d'enseignement. Le DPO doit être consulté avant l'adoption de tout nouvel outil numérique.
- **Interdiction de la biométrie:** La CNIL s'oppose formellement au déploiement de dispositifs de reconnaissance biométrique (reconnaissance faciale ou digitale) pour l'accès aux établissements ou aux cantines.

### 2.3 Devoir d'information et droits des personnes

[J] L'établissement doit fournir une information claire aux élèves et à leurs parents (art. 13-14 du RGPD) dans un langage accessible aux mineurs.
- Droits d'accès (art. 15), de rectification (art. 16) et de limitation (art. 18).
- Le droit à l'effacement (« droit à l'oubli », art. 17) ne s'applique pas aux registres scolaires officiels soumis aux règles de conservation des archives publiques.
- Droit de réclamation auprès de la CNIL.

[P] Profil de sécurité: L'hébergement et les sauvegardes DOIVENT être situés au sein de l'Espace économique européen (EEE). Les clouds publics non sécurisés sans chiffrement de bout en bout sont exclus.

### 2.4 Synthèse comparative des juridictions et seuils d'âge [J/P]

Lors de la conception d'une application éducative, vérifiez toujours le cadre national applicable:

| Pays / Juridiction | Âge de consentement (art. 8 RGPD) | Autorité de contrôle | Spécificités scolaires et doctrines Cloud / IA |
|---|---|---|---|
| **France (FR)** | 15 ans (Loi Informatique et Libertés) | CNIL | Code de l'éducation; doctrine ENT et cadre GAR; consignes ministérielles interdisant les clouds gratuits US; interdiction des comptes partagés en classe pour l'IA. |
| **Allemagne (DE)** | 16 ans (§ 16 BDSG) | DSK + 16 autorités régionales | 16 lois scolaires des Länder; décisions DSK contre M365 et la télémétrie; priorité au modèle local (L0); AIPD obligatoire pour l'IA. |
| **Pologne (PL)** | 16 ans (Loi ODO 2018) | UODO | Prawo oświatowe; responsabilité du chef d'établissement; interdiction de la biométrie; contrat art. 28 RGPD obligatoire pour l'IA. |
| **Tchéquie (CZ)** | 15 ans (Loi n° 110/2019 Sb.) | ÚOOÚ | Loi scolaire n° 561/2004 Sb.; recommandations ministérielles MŠMT et NPI pour l'IA. |
| **Espagne (ES)** | 14 ans (LOPDGDD art. 7) | AEPD | Législation LOE; DPO obligatoire dans les écoles; guides détaillés de l'AEPD sur le k-anonymat. |
| **Ukraine (UA)** | 14-18 ans (Code civil) | Médiateur des droits humains | Loi n° 2297-VI et projet de loi 8153; écosystème Mrija; les élèves déplacés dans l'UE relèvent du RGPD européen. |

#### Règles applicables aux projets en France

1. **Intégration dans l'écosystème souverain (ENT et GAR):** [J/P] Les applications destinées aux établissements français doivent privilégier l'interconnexion avec les Espaces Numériques de Travail (ENT) et respecter le cadre du Gestionnaire d'Accès aux Ressources (GAR).
2. **Interdiction des comptes génériques de classe pour l'IA:** [P] Conformément aux recommandations de la CNIL, il est interdit d'utiliser un compte partagé d'établissement où les requêtes libres des élèves contiennent des données identifiantes ou indirectes.

## 3. Règlement sur l'intelligence artificielle (AI Act)

### 3.1 Applicabilité aux outils éducatifs

[J] Le Règlement (UE) 2024/1689 (AI Act) s'applique aux systèmes d'IA développés, déployés ou utilisés dans l'UE, y compris en milieu éducatif.
Les algorithmes déterministes classiques, calculs de moyennes par formule fixe et requêtes SQL statiques ne constituent pas des systèmes d'IA au sens du règlement.

### 3.2 Pratiques interdites en milieu scolaire (Article 5)

[J] Sont strictement interdits dans les établissements scolaires:
1. **Reconnaissance des émotions:** Utilisation de l'IA pour déduire l'état émotionnel des élèves à partir de la caméra ou de la voix (art. 5 par. 1 point f).
2. **Notation sociale (Social Scoring):** Classement ou évaluation des élèves menant à un traitement préjudiciable hors du contexte initial (art. 5 par. 1 point c).
3. **Catégorisation biométrique:** Déduction de caractéristiques sensibles (origines, opinions, croyances) à partir de données biométriques.
4. **Manipulation subliminale:** Techniques altérant le comportement d'un élève et susceptibles de lui causer un préjudice.

### 3.3 Systèmes d'IA à haut risque dans l'éducation (Article 6 et Annexe III)

[J] Sont classés à haut risque (High-Risk AI) les systèmes d'IA destinés à:
- Déterminer l'admission ou l'orientation des élèves vers des filières scolaires.
- Évaluer les acquis d'apprentissage et corriger automatiquement des épreuves influant sur l'orientation ou les notes.
- Surveiller le comportement et détecter les fraudes lors d'examens (proctoring).

### 3.4 Obligations des fournisseurs et des établissements

- **Fournisseur:** Système de gestion des risques (art. 9), qualité des données d'entraînement (art. 10), documentation technique (art. 11), journalisation automatique (art. 12), transparence (art. 13), contrôle humain (Human-in-the-loop, art. 14).
- **Établissement utilisateur:** Utilisation conforme à la notice, maintien du contrôle effectif par les enseignants, conservation des journaux pendant au moins 6 mois (art. 26 par. 6), information préalable des personnes concernées.

### 3.5 Calendrier d'application

- Février 2025: Interdiction des pratiques prohibées (détection des émotions, notation sociale).
- Août 2025: Règles applicables aux modèles d'IA à usage général (GPAI).
- Août 2026: Entrée en vigueur complète pour les systèmes à haut risque dans l'enseignement.

## 4. Modèle de données, collecte et minimisation [P]

[P] Le modèle de données de l'application DOIT respecter le principe de minimisation:
- **Identifiants:** Utiliser des UUIDv4 synthétiques comme clés primaires. Ne jamais exposer le numéro d'identification national (INE en France) ni le nom de l'élève dans les URL ou le stockage local.
- **Champs facultatifs:** Les numéros de téléphone personnel, adresses postales et photographies ne doivent pas être obligatoires dans les applications disciplinaires.
- **Données sensibles:** Les applications pédagogiques NE DOIVENT PAS collecter de diagnostics médicaux. Pour les aménagements d'épreuves (tiers-temps), seul un paramètre technique (`extra_time_multiplier: 1.33`) doit être conservé.
- **Métadonnées:** Purger systématiquement les métadonnées EXIF des photos de devoirs téléversées par les élèves avant stockage.

## 5. Authentification, invitations et sessions [P]

[P] Profil d'authentification:
- **Mots de passe:** Longueur minimale de 12 caractères. Contrôle contre les dictionnaires de mots de passe compromis. Hachage obligatoire via Argon2id ou bcrypt avec coût élevé.
- **Codes PIN et QR codes:** Réservés exclusivement aux élèves des classes primaires pour des séances encadrées en classe avec expiration automatique.
- **Gestion des sessions:** Identifiants de session cryptographiquement sûrs (au moins 128 bits d'entropie). Cookies munis des attributs `HttpOnly`, `Secure` et `SameSite=Lax/Strict`.
- **Délai d'inactivité:** Déconnexion automatique après 30 minutes sans action pour les élèves et 15 minutes pour les enseignants et administrateurs.

## 6. Rôles, habilitations et intégrité [P]

[P] Contrôle d'accès:
- **Modèle RBAC:** Rôles distincts: Élève, Enseignant, Parent/Responsable, Chef d'établissement/Administrateur.
- **Cloisonnement des données:** Contrôle systématique des autorisations à chaque requête. Un élève ne consulte que ses propres notes; un parent ne voit que ses enfants; un enseignant accède uniquement à ses classes d'enseignement.
- **Protection anti-IDOR:** Toute modification d'identifiant d'objet dans la requête doit être bloquée côté serveur avec un code HTTP 403 Forbidden.
- **Traçabilité:** Toute modification de note ou d'appréciation officielle génère une piste d'audit avec horodatage UTC et identifiant de l'auteur.

## 7. Chiffrement et gestion des clés [P]

[P] Standards cryptographiques:
- **Données au repos (At Rest):** Chiffrement des bases de données et sauvegardes avec AES-256-GCM ou ChaCha20-Poly1305.
- **Données en transit (In Transit):** Utilisation stricte de TLS 1.3 (minimum TLS 1.2 avec suites cryptographiques robustes). Activation de l'en-tête HSTS pour au moins 1 an (`max-age=31536000; includeSubDomains`).
- **Gestion des secrets:** Interdiction d'enregistrer des clés ou mots de passe dans le code source. Utilisation de variables d'environnement ou d'un gestionnaire de secrets dédié.

## 8. CSV et SQLite [P]

[P] Fichiers locaux et bases embarquées:
- **Protection anti-injection CSV:** Lors de l'exportation de données d'élèves, tout champ débutant par `=`, `+`, `-`, `@`, tabulation ou retour chariot DOIT être précédé d'une apostrophe (`'`) pour empêcher l'exécution de macros malveillantes dans les tableurs.
- **Mode SQLite:** Utilisation du mode WAL (Write-Ahead Logging) et activation des clés étrangères (`PRAGMA foreign_keys = ON;`). La base SQLite doit impérativement être placée hors de l'arborescence publique du serveur Web.
- **Requêtes paramétrées:** Recours exclusif aux requêtes préparées (Prepared Statements) pour éradiquer tout risque d'injection SQL.

## 9. Web, PWA et équipements partagés [P]

[P] Sécurité sur postes partagés:
- **Postes partagés en salle de classe:** L'action de déconnexion DOIT vider intégralement les stockages locaux du navigateur (`localStorage`, `sessionStorage`, `IndexedDB`) pour empêcher la consultation par l'élève suivant.
- **Content Security Policy (CSP):** Politique CSP stricte bloquant les domaines tiers non approuvés et les scripts inline non signés.
- **Absence de traceurs tiers:** Interdiction totale d'intégrer des outils d'analyse marketing ou des pixels publicitaires (Google Analytics, Meta) dans les outils scolaires.

## 10. Audit, durées de conservation et reprise [P/J]

[P/J] Traçabilité et cycle de vie:
- **Journaux d'audit:** Enregistrement des connexions, échecs d'authentification, modifications de droits et saisies de notes.
- **Minimisation des logs:** Pas de mots de passe en clair ni de données d'élèves sensibles dans les fichiers journaux.
- **Purge et archivage:** Suppression des données d'exercices à l'issue de l'année scolaire; versement des éléments administratifs aux archives selon la réglementation nationale.
- **Sauvegardes:** Sauvegardes chiffrées régulières avec exercice de restauration semestriel.

## 11. Gestion des incidents de sécurité [J/P]

[J] Notification et registre des violations (art. 33-34 du RGPD):
- **Notification à la CNIL:** L'établissement notifie toute violation de données personnelles à la CNIL dans les 72 heures suivant sa découverte, sauf si elle ne présente pas de risque pour les droits des personnes.
- **Information des familles:** Si le risque pour les droits des élèves est élevé, les familles doivent être informées directement et sans délai.
- **Registre interne:** Inscription obligatoire de tout incident dans le registre interne des violations de l'établissement.

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

## 15. Flux de données d'IA, tuteurs et architectures RAG [P/V]

### 15.1 Modèles de langage en contexte scolaire

[P/V] Recours aux grands modèles de langage (LLM) comme assistants pédagogiques:
- **Rétention nulle (Zero-Data Retention - ZDR):** Les engagements contractuels du fournisseur doivent stipuler que les requêtes des élèves ne sont pas conservées au-delà de la réponse et ne servent pas à l'entraînement de modèles.
- **Sensibilisation aux prompts:** Les élèves doivent être formés à ne jamais saisir d'informations nominatives, d'adresses ou d'éléments de vie privée dans l'interface de requête.

### 15.2 Génération augmentée par récupération (RAG)

[P] Dans les architectures RAG éducatives:
- Vectorisez uniquement des contenus pédagogiques libres et des manuels scolaires autorisés.
- Ne versez jamais de dossiers scolaires, rapports d'orientation ou données d'élèves dans les index vectoriels.

### 15.3 Primauté de l'évaluation pédagogique

[P] Les suggestions de l'IA restent purement indicatives. Aucune décision d'orientation ou de sanction ne peut être prise de manière entièrement automatisée (art. 22 du RGPD).

### 15.4 Passerelles architecturales et k-anonymat pour l'IA [P]

[P] Architecture de protection des données pour l'IA scolaire:

#### 1. Niveaux de traitement (L0 / C1 / C2)
- **Niveau L0 (Entièrement local):** Modèle exécuté sur l'infrastructure propre de l'établissement ou sur le poste (ex. Ollama, llama.cpp sur le réseau scolaire). Aucune donnée ne sort de l'école.
- **Niveau C1 (Cloud avec contrat RGPD et ZDR):** Fournisseur hébergé dans l'EEE disposant d'un contrat de sous-traitance (art. 28 RGPD) et d'un engagement ZDR. Les identifiants directs des élèves DOIVENT être retirés ou pseudonymisés avant transmission.
- **Niveau C2 (Modèles publics sans contrat scolaire):** Uniquement pour des requêtes entièrement anonymisées et décontextualisées, sans aucun lien avec l'élève ou l'établissement.

#### 2. Seuils de k-anonymat (k >= 5) et l-diversité (l >= 2)
Pour toute diffusion de données agrégées ou alimentation d'algorithmes prédictifs:
- **Seuil de k-anonymat:** Chaque groupe partageant des quasi-identifiants identiques (âge, classe, filière) DOIT comporter au minimum $k = 5$ élèves distincts. Les groupes inférieurs font l'objet d'une suppression ou d'une généralisation.
- **Seuil de l-diversité:** Les attributs sensibles au sein de chaque groupe doivent présenter au moins $l = 2$ valeurs différentes pour parer aux attaques par homogénéité.
- **Validation automatisée:** Exécutez systématiquement un script de validation (`scripts/check_k_anonymity.py`) avant toute extraction.

## 16. Authentification fédérée et ENT [P]

[P] Raccordement aux systèmes d'identité:
- Privilégiez les protocoles standardisés OpenID Connect (OIDC) ou SAML 2.0 via l'ENT ou le GAR.
- Ne demandez que les attributs strictement nécessaires (identifiant pseudonymisé `sub` et profil d'appartenance).
- Conservez les jetons de manière sécurisée côté serveur sans les exposer dans le stockage du navigateur.

## 17. Guide des solutions pratiques

### 17.1 Modes de déploiement (M1 - M6)

L'assistant prend en charge les architectures suivantes:
- **M1 (Application autonome locale / Hors ligne):** Fonctionne sur l'ordinateur de l'enseignant sans internet (SQLite, CSV).
- **M2 (Serveur dédié de l'établissement):** Application Web hébergée au sein du réseau local de l'école.
- **M3 (Plateforme éducative avec contrat DPA):** Solution cloud officielle couverte par un contrat conforme à l'article 28 du RGPD.
- **M4 (Audit de conformité et de code):** Évaluation d'une application existante.
- **M5 (Tuteur d'IA local L0):** Déploiement d'un modèle local en classe informatique sans fuite de données.
- **M6 (IA hybride avec k-anonymat):** Traitement cloud C1 avec anonymisation préalable et validation mathématique k >= 5.

### 17.2 Schéma d'architecture de référence

```
[ Navigateur ou PWA de l'élève ]
             │
             │ HTTPS (TLS 1.3 + HSTS)
             ▼
[ Reverse Proxy (Nginx / Caddy) ] ── (Protection, CSP stricte, en-têtes durcis)
             │
             │ Réseau scolaire isolé
             ▼
[ Serveur d'application (Backend) ]
     ├── Module RBAC et gestion sécurisée des sessions
     ├── Module de sanitisation et protection CSV
     └── Passerelle IA (L0 / C1 / C2 avec validation k >= 5)
             │
             │ Connexion chiffrée
             ▼
[ Base de données (PostgreSQL / SQLite WAL) ] (Chiffrement au repos AES-256)
```

### 17.5 Fiche descriptive de module applicatif

Chaque module fait l'objet d'une fiche normalisée:
1. **Nom du module et finalité éducative:** Description synthétique.
2. **Catégories de données traitées:** Données ordinaires et techniques.
3. **Fondement juridique:** Article du RGPD et référence au Code de l'éducation.
4. **Niveau architectural:** Sélection M1 - M6 et passerelle IA (L0 / C1 / C2).
5. **Mesures de protection:** Paramètres de chiffrement, purge de session et seuils de k-anonymat.

## 18. Publication, documents et produits dérivés [R/V]

### 18.1 Règles relatives aux photographies et créations d'élèves

[R/V] Diffusion sur le site de l'établissement et supports d'information:
- **Consentement écrit préalable:** Accord explicite des responsables légaux avant toute publication d'image d'un élève mineur.
- **Principe de dissociation:** Le formulaire de droit à l'image ne doit pas être inclus dans le dossier général d'inscription administrative.
- **Anonymat des publications:** Ne pas associer le nom complet et la classe d'un élève à sa photographie sur des plateformes publiques.

### 18.2 Actualisation des règles et remontée amont

[P] Toute proposition d'actualisation de ce skill ou de nouvelles recommandations d'autorités de contrôle peut être soumise sur le dépôt GitHub:
`https://github.com/siberius/student-data-protection/issues` avec le label `legal-update`.

© 2026 Luděk Sušický. [MIT](https://opensource.org/license/mit). La version révisée 1.2 repose sur le guide initial d'octobre 2026; conserver les mentions d'auteur, de licence et les avis de modification. Les sources externes conservent leurs droits.

## Licence (License)

MIT License

Copyright (c) 2026 Luděk Sušický

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
