# Student Data Protection in School Apps

[![Skills.sh](https://img.shields.io/badge/skills.sh-Install-blue)](https://skills.sh/siberius/student-data-protection)
[![Dokumentace](https://github.com/siberius/student-data-protection/actions/workflows/docs.yml/badge.svg)](https://github.com/siberius/student-data-protection/actions/workflows/docs.yml)

> 📖 **Článek a rozbor na Vibemaker:** [Chrání vaše aplikace data žáků?](https://vibemaker.cz/clanek/bezpeci-dat-zaku/)

[![Student Data Protection](docs/student-data-protection.gif)](https://vibemaker.cz/clanek/bezpeci-dat-zaku/)

**Čeština:** [README.cs.md](README.cs.md) · **Czech guide:** [docs/ochrana-dat-zaku.md](docs/ochrana-dat-zaku.md)

## Installation and Quick Start

Install one language edition into your coding agent (Claude Code, Cursor, Codex, Antigravity, OpenCode, Cline and others) using the `skills` CLI from [skills.sh](https://skills.sh):

```bash
# Install the international English edition
npx skills add siberius/student-data-protection --skill student-data-protection --full-depth -g -a codex

# Or install the Czech edition
npx skills add siberius/student-data-protection --skill ochrana-dat-zaku --full-depth -g -a codex

# Or list all 7 available language editions
npx skills add siberius/student-data-protection --full-depth --list
```

Without `--agent`, `skills use` prints a prepared prompt. To launch a supported agent with this skill temporarily:

```bash
npx skills use siberius/student-data-protection --skill student-data-protection --full-depth --agent codex
```

A practical guide for teachers, school IT staff, and anyone building school applications that collect, store, or share student data. It connects the applicable legal framework with a concrete, explicitly selected security profile and verifiable implementation controls.

Before substantive work, the skill establishes the necessary context and asks for missing consequential information. Supplied facts and permissions are reused; unanswered decisive questions stop only dependent work. The [workflow intake](references/workflow.md) covers relevant scope, data, audience, recipients, lifecycle and environment.

[Publication and derived outputs](references/publication.md) covers allowed public fields, document/media review, provenance, actual build artifacts, search indexes, access boundaries, removal and safe updates. It loads only for the relevant task. Technical feedback uses sanitised synthetic examples and is never sent automatically.

## Practical solutions and package size

Start with the short native core and load only the relevant reference. [Practical solutions](references/practical-solutions.md) offers six data-handling modes: one-off practice, limited collection, saved progress, official records, teacher reports/exports and AI tutoring. It includes implementation paths, containment versus durable repair and a solution card. Expand only the selected recipe. These are design examples, not evidence of deployed safeguards.

The complete guide remains a standalone reading format; do not load it alongside all references. Keep one skill for now. Split incident response, audit or implementation into separate skills only if they acquire independent inputs, permissions and deliverables; avoid duplicating common safeguards.

**Scope of the English/Czech editions:** the Czech education system, for základní školy (ZŠ, primary and lower-secondary schools) and střední školy (SŠ, upper-secondary schools). **Reference period:** October 2026. The recorded legal-source verification date is 22 October 2026; the scope clarification dated 30 October 2026 is not a new legal review. Before later use, check that the rules remain current and applicable to the particular school.

The English and Czech editions address Czech ZŠ and SŠ, excluding preschools and higher education. The Spanish, Polish, Ukrainian, German, and French editions are adaptations for their respective jurisdictions, not extensions of Czech law.

## Available editions and native skills

| Language / Jurisdiction | Native skill | Standalone guide | Legal register | Readme |
| --- | --- | --- | --- | --- |
| **English (EU / Czech context)** | [SKILL.md](SKILL.md) | [docs/student-data-protection.md](docs/student-data-protection.md) | [docs/source-register.md](docs/source-register.md) | [README.md](README.md) |
| **Čeština (Česko / EU)** | [cs/SKILL.md](cs/SKILL.md) | [docs/ochrana-dat-zaku.md](docs/ochrana-dat-zaku.md) | [docs/registr-zdroju.md](docs/registr-zdroju.md) | [README.cs.md](README.cs.md) |
| **Español (España / UE)** | [es/SKILL.md](es/SKILL.md) | [docs/proteccion-datos-alumnado.md](docs/proteccion-datos-alumnado.md) | [docs/registro-fuentes.md](docs/registro-fuentes.md) | [README.es.md](README.es.md) |
| **Polski (Polska / UE)** | [pl/SKILL.md](pl/SKILL.md) | [docs/ochrana-danych-uczniow.md](docs/ochrana-danych-uczniow.md) | [docs/rejestr-zrodel.md](docs/rejestr-zrodel.md) | [README.pl.md](README.pl.md) |
| **Українська (Україна / ЄС)** | [uk/SKILL.md](uk/SKILL.md) | [docs/zakhyst-danykh-uchniv.md](docs/zakhyst-danykh-uchniv.md) | [docs/reiestr-dzherel.md](docs/reiestr-dzherel.md) | [README.uk.md](README.uk.md) |
| **Deutsch (Deutschland / EU)** | [de/SKILL.md](de/SKILL.md) | [docs/schuelerdatenschutz.md](docs/schuelerdatenschutz.md) | [docs/quellenregister.md](docs/quellenregister.md) | [README.de.md](README.de.md) |
| **Français (France / UE)** | [fr/SKILL.md](fr/SKILL.md) | [docs/protection-donnees-eleves.md](docs/protection-donnees-eleves.md) | [docs/registre-sources.md](docs/registre-sources.md) | [README.fr.md](README.fr.md) |

## What it covers

- data inventory, minimisation, and identity
- verified accounts versus one-time codes and QR
- server-side permissions and record integrity
- encryption (AES-256-GCM, key management, TLS)
- SQLite, CSV, exports, and formula injection
- PWA, shared devices, and logout
- audit, retention, backups, and recovery
- incident response and the 72-hour rule
- AI Act: scope, prohibited practices, high-risk education uses, timeline
- local vs non-local AI boundaries (L0/C1/C2), k-anonymity (k >= 5) and l-diversity (l >= 2) with deterministic script gating
- a pre-production checklist and 38 acceptance scenarios, including conditional AI/RAG, SSO and non-local AI checks

## Native skill and standalone guide

Use [English SKILL.md](SKILL.md), [český skill](cs/SKILL.md), or [Spanish skill for Spain](es/SKILL.md) with a host that supports file-based skills. Keep its LICENSE and references/ together. Load only the relevant modules. The [Spanish guide](docs/proteccion-datos-alumnado.md) adapts national law for Spain; the English guide retains the original EU/Czech context, which must be checked against the actual country. Installation is not automatic and does not prove execution.

Select design, implementation, audit or incident work from the task. An audit reports without app changes. For a narrow correction, inspect the affected data flow and relevant regressions. The strict profile is adopted by context; assess existing equivalent safeguards before replacing architecture.

The complete standalone guides remain available for manual use and instruction-capable chats. Their numbered acceptance scenarios are test plans, not proof of execution. See [skill behaviour scenarios](docs/skill-evaluation.md) separately.

## How to use it

1. Read [the guide](docs/student-data-protection.md) before you design the data model.
2. Use section 12 as a checklist and section 13 as a test plan.
3. Paste the guide into an AI assistant as project context. It is written as a skill and marks legal duties (`[Z]`), the security profile (`[P]`), recommendations (`[D]`), and points to verify (`[O]`).
4. Never put real student data into an ordinary or unapproved AI chat or a public repository. Use synthetic data.

The guide is intentionally specific. Where it says MUST, it describes the security profile, not a literal GDPR command. Document any deviation with the threat, a compensating control, a test, and the decision of the school's responsible person.

## What it is not

This is not legal advice and not a certificate. A completed checklist does not prove GDPR compliance or high-risk AI conformity. Before processing real data, the controller must establish the legal basis, retention, contracts and required assessments, consulting the DPO in time for independent advice. Deployment responsibility remains with the controller. AI Act dates and guidance change; verify the current text before a legally significant deployment.

## Sources and version

Version 1.2, edition of 14 November 2026. Non-local AI safeguards, k-anonymity (k >= 5), l-diversity (l >= 2) and deterministic script gating added on 14 November 2026. The original source-check date is 22 October 2026. See the [source register](docs/source-register.md). The guide links to GDPR, the AI Act Service Desk, ÚOOÚ, EDPB, OWASP, NIST, ENISA, and SQLite documentation.

## Author

**Luděk Sušický**, biologist, secondary-school and university teacher of computing subjects

- E-mail: [ludek.susicky@gmail.com](mailto:ludek.susicky@gmail.com)
- X: [@ludeksusicky](https://x.com/ludeksusicky)
- LinkedIn: [Luděk Sušický](https://www.linkedin.com/in/ludek-susicky/)
- GitHub: [@siberius](https://github.com/siberius): more educational projects and open-source applications

## License

© 2026 Luděk Sušický. The text is licensed under [MIT](https://opensource.org/license/mit). See [LICENSE](LICENSE).

Corrections and issues are welcome, especially when a legal reference or a security recommendation becomes outdated.

[Español: España](README.es.md) · [Source register](docs/source-register.md) · [Skill evaluation](docs/skill-evaluation.md)
