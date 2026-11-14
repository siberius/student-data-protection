# 17. Guide des solutions pratiques

<!-- Référence générée ; modifier le guide autonome maintenu. -->

Sections sources: 17.

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

```text
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

© 2026 Luděk Sušický. [MIT](https://opensource.org/license/mit). Édition révisée de la version 1.2, basée sur le guide initial d'octobre 2026. Conserver les mentions d'auteur, de licence et les avis de modification.
