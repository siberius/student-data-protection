# Protection des données des élèves dans les applications scolaires

[![Skills.sh](https://img.shields.io/badge/skills.sh-Install-blue)](https://skills.sh/siberius/student-data-protection)

Profil de sécurité et skill d'assistance pour les applications scolaires (France et UE).

> Version: 1.2 · Conformité: RGPD (UE 2016/679), Règlement sur l'IA (AI Act, UE 2024/1689), Loi Informatique et Libertés et Code de l'éducation.

## Installation et démarrage rapide

Installez le skill dans votre assistant de code (Claude Code, Cursor, Codex, Antigravity, OpenCode, Cline et autres) via la CLI de [skills.sh](https://skills.sh):

```bash
# Installation de l'édition française (France / UE)
npx skills add siberius/student-data-protection --skill protection-donnees-eleves --full-depth -g -a codex

# Afficher toutes les 7 éditions disponibles
npx skills add siberius/student-data-protection --full-depth --list
```

Test ponctuel sans installation permanente:

```bash
npx skills use siberius/student-data-protection --skill protection-donnees-eleves --full-depth --agent codex
```

## Vue d'ensemble de la documentation

- **Guide autonome en français:** [docs/protection-donnees-eleves.md](docs/protection-donnees-eleves.md)
- **Registre des sources juridiques et techniques:** [docs/registre-sources.md](docs/registre-sources.md)
- **Scénarios d'évaluation du comportement du skill:** [docs/evaluation-competence.md](docs/evaluation-competence.md)
- **Module de skill natif (FR):** [fr/SKILL.md](fr/SKILL.md)

## Principes fondamentaux du profil

1. **Responsabilité du chef d'établissement et rôle du DPO:** Tout déploiement d'outil numérique traitant des données d'élèves relève de la décision du chef d'établissement après avis de son DPO.
2. **Encadrement strict des sous-traitants (art. 28 RGPD):** Interdiction de transmettre des données scolaires à des tiers sans contrat formel de traitement de données.
3. **Paliers architecturaux pour l'IA (L0 / C1 / C2):** Priorité aux modèles locaux souverains (L0) et dépersonnalisation rigoureuse avant tout recours au cloud (C1).
4. **k-anonymat (k >= 5) et l-diversité (l >= 2):** Contrôle statistique systématique de tout jeu de données pédagogiques avant transmission à des modèles d'évaluation ou d'analyse.
5. **Veille juridique continue:** Surveillance de la fraîcheur des sources et procédure de remontée amont via les issues GitHub du projet.

### Auteur

**Luděk Sušický** - biologiste, enseignant d'informatique dans le secondaire et le supérieur

- E-mail: [ludek.susicky@gmail.com](mailto:ludek.susicky@gmail.com)
- X: [@ludeksusicky](https://x.com/ludeksusicky)
- LinkedIn: [Luděk Sušický](https://www.linkedin.com/in/ludek-susicky/)
- GitHub: [@siberius](https://github.com/siberius) - autres projets éducatifs et logiciels libres

### Licence

Ce projet est sous licence MIT. Consultez le fichier [LICENSE](LICENSE) pour plus de détails.
