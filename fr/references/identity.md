# 5. Authentification, invitations et sessions [P]

<!-- Référence générée ; modifier le guide autonome maintenu. -->

Sections sources: 5, 6.

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

© 2026 Luděk Sušický. [MIT](https://opensource.org/license/mit). Édition révisée de la version 1.2, basée sur le guide initial d'octobre 2026. Conserver les mentions d'auteur, de licence et les avis de modification.
