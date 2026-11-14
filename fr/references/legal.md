# 2. RGPD et cadre juridique français

<!-- Référence générée ; modifier le guide autonome maintenu. -->

Sections sources: 2.

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

© 2026 Luděk Sušický. [MIT](https://opensource.org/license/mit). Édition révisée de la version 1.2, basée sur le guide initial d'octobre 2026. Conserver les mentions d'auteur, de licence et les avis de modification.
