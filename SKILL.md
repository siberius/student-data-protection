---
name: student-data-protection
description: Design, implement or audit student-data protection in school applications. Use when a change affects personal data, identity, permissions, retention, exports or AI data flows, or for a requested privacy/security review. Do not turn an unrelated cosmetic edit into a full compliance audit.
metadata:
  version: "1.1"
  language: "en"
  license: "MIT"
  author: "Luděk Sušický"
  repo: "https://github.com/siberius/student-data-protection"
---

# Student data protection

Use the requested scope and available evidence. This skill supports school software work; it does not certify compliance or authorise production changes. The English/Czech editions cover Czech primary and secondary schools (ZŠ/SŠ), excluding preschools and higher education; choose the actual jurisdiction. A language choice alone does not select national law.

## Choose the mode and affected boundary

Infer design, implementation, audit or incident from the request. For an audit, inspect and report without changing the application. Incident analysis does not authorise shutting down services, revoking accounts or sending notifications. For authorised implementation, change the affected boundary and check meaningful regressions. Do not restart a whole-system review for a narrow fix. Flag a serious adjacent risk with evidence and a proposed action rather than silently expanding work.

Reuse known purposes, data flows, school/tenant, roles, hosting and deployment constraints. Ask only when missing information changes the decision. Synthetic data allow development while a real-data processing decision is unresolved. An activity without personal processing need not gain accounts or storage; check operational metadata before describing it as anonymous.

For an existing application, offer a focused entry audit and remediation plan, or a broader pre-deployment review when warranted. If audit or implementation is already requested, follow that scope; do not ask again or silently expand it. Use section 17.6 of the practical guide for evidence, prioritisation and remediation status.

## Keep the durable boundaries

- Minimise data by purpose. A pseudonym, encrypted record, learner reasoning summary or embedding can remain personal data.
- Authenticate appropriately for the data and enforce object/tenant permissions on the server or other trusted boundary. A name, shared code, UUID or model instruction is not authorisation. Separate unverified submissions from approved records.
- Treat user input, attachments, retrieved text and model output as untrusted. Protect secrets and validate outputs before authoritative writes. Do not upload real records, logs or keys to an ordinary AI chat.
- Consider deletion, correction, derived copies, backups and recovery together. Shared devices must not expose the previous user. Report uncertain or failed controls as such.
- Separate legal requirements [Z], selected security-profile choices [P], recommendations [D] and unresolved checks [O]. The detailed strict profile applies when adopted for the system; assess equivalent existing safeguards before proposing an architectural replacement. Do not invent an exemption from law or downgrade necessary protection.
- The controller makes accountable processing/deployment decisions. Consult the DPO in time for independent advice and monitoring; do not describe DPO approval as a universal legal gate or shift controller responsibility to the DPO.

For scope, strict-profile applicability and governance detail, read [workflow](references/workflow.md) when needed. Read [legal framework](references/legal.md) for lawful basis, rights, transfers or local duties, and [AI Act](references/ai-act.md) only when relevant to AI use/classification. Use [source status](references/source-status.md) when checking legal claims. Verify current sources for consequential legal decisions; a successful URL request is not a legal review.

## Load only the relevant module

For a practical solution, recommend one suitable data-handling mode; expand only that recipe. The six data modes differ from the task modes above. Read the practical guide only for this choice. Keep the core short; consider separate skills only when incident response, auditing or implementation develops an independent workflow with distinct inputs and permissions.

| Work | Reference |
|---|---|
| Practical choice of data-handling mode and solution card | [Practical solutions](references/practical-solutions.md) |
| Collection, fields, files, imports or connectors | [Data flows](references/data.md) |
| Accounts, codes, roles, sessions or record integrity | [Identity and access](references/identity.md) |
| OIDC/SAML identity-provider integration | [SSO](references/sso.md) |
| Encryption, keys or transport | [Cryptography](references/crypto.md) |
| SQLite, CSV or exports | [Storage](references/storage.md) |
| Web/PWA cache, shared devices or browser protections | [Web](references/web.md) |
| Retention, audit, restore or an incident | [Operations](references/operations.md) |
| Implemented/requested AI tutoring or RAG | [AI data](references/ai-data.md) |
| Relevant checklist, acceptance scenarios and handoff | [Verification](references/verification.md) |

Do not load every module automatically or add the described technology to use a module. The profile is a reference design; explain material differences and risk rather than assuming a different maintained solution is broken.

## Verify and hand over

For an implementation, select tests for the actual changed feature and its risks. Use authorised environments and synthetic records. For an audit, provide location/evidence, severity, effect, recommendation and needed verification; do not claim proposed tests passed. Distinguish observed failure, hypothesis, not checked and N/A with a reason. Keep legal uncertainty separate from technical failure. Hand over concrete checked properties and remaining decisions; never claim 100% security or GDPR certification.

## Integration and attribution

Suitable for school data workflows, records, portals, forms and AI learning tools where the task affects personal data. No specific stack, provider, API, account system or national curriculum is required. Keep this file, references/ and LICENSE together. Use one relevant language package; a native skill host must support loading its files. The standalone guide remains available separately. This skill does not authorise installation, paid services, publication, production access or processing changes outside the request.

© 2026 Luděk Sušický. MIT. Preserve attribution, license and change notices on redistribution; external sources retain their rights. Revised edition 1.1 adds scoped modes, modular references, AI/SSO controls and revised DPO governance to the original 1.1 guide.
