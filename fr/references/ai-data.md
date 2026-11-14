# 15. Flux de données d'IA, tuteurs et architectures RAG [P/V]

<!-- Référence générée ; modifier le guide autonome maintenu. -->

Sections sources: 15.

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

© 2026 Luděk Sušický. [MIT](https://opensource.org/license/mit). Édition révisée de la version 1.2, basée sur le guide initial d'octobre 2026. Conserver les mentions d'auteur, de licence et les avis de modification.
