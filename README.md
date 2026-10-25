# Student Data Protection in School Apps

[![Dokumentace](https://github.com/siberius/student-data-protection/actions/workflows/docs.yml/badge.svg)](https://github.com/siberius/student-data-protection/actions/workflows/docs.yml)

**Čeština:** [README.cs.md](README.cs.md) · **Czech guide:** [docs/ochrana-dat-zaku.md](docs/ochrana-dat-zaku.md)

A practical guide for teachers, school IT staff, and anyone building school applications that collect, store, or share student data. It turns GDPR and AI Act duties into concrete technical rules that can be implemented and tested.

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
- a pre-production checklist and 30 acceptance tests

## How to use it

1. Read [the guide](docs/student-data-protection.md) before you design the data model.
2. Use section 12 as a checklist and section 13 as a test plan.
3. Paste the guide into an AI assistant as project context. It is written as a skill and marks legal duties (`[Z]`), the security profile (`[P]`), recommendations (`[D]`), and points to verify (`[O]`).
4. Never put real student data into an AI chat or a public repository. Use synthetic data.

The guide is intentionally specific. Where it says MUST, it describes the security profile, not a literal GDPR command. Document any deviation with the threat, a compensating control, a test, and the decision of the school's responsible person.

## What it is not

This is not legal advice and not a certificate. A completed checklist does not prove GDPR compliance or high-risk AI conformity. Before processing real data, the school and its data protection officer must confirm the legal basis, retention, contracts, and any required assessment. AI Act dates and guidance change; verify the current text before a legally significant deployment.

## Sources and version

Version 1.1, sources verified on 22 October 2026, edition of 25 October 2026. The guide links to GDPR, the AI Act Service Desk, ÚOOÚ, EDPB, OWASP, NIST, ENISA, and SQLite documentation.

## Author

Luděk Sušický, biologist and secondary and university teacher of computer science.

## License

© 2026 Luděk Sušický. The text is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). See [LICENSE](LICENSE).

Corrections and issues are welcome, especially when a legal reference or a security recommendation becomes outdated.
