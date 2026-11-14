# 2. GDPR and the Czech legal framework

<!-- Generated reference; edit the maintained standalone guide. -->

Source sections: 2.

## 2. GDPR and the Czech legal framework

### 2.1 What is and is not personal data

[Z] A name linked to attendance, contact, a message, a result, a class, or a grade is personal data. A random ID, a hash of a name, or an encrypted record generally remains personal data if the person can be re-identified. Pseudonymization is not anonymization. Grades alone are not automatically a special category under Article 9; diagnoses, health limitations, or some biometric data may be. The default profile disables their collection; handle any necessary feature through a separate assessment and narrower permissions. For special categories, document the applicable Article 9(2) exception in addition to the Article 6 basis. See [GDPR](https://eur-lex.europa.eu/eli/reg/2016/679/oj) and the [European Commission's explanation of personal data](https://commission.europa.eu/law/law-topic/data-protection/data-protection-explained_en).

### 2.2 School and supplier decisions

| Area | Duty, decision, and required evidence |
|---|---|
| Purpose and legal basis | [Z] For each purpose, determine the Article 6 basis, the necessary data, and retention. School assignments typically rely on Article 6(1)(c) or (e), with specific support and a necessity assessment. Section 28 of the Czech School Act is not a blanket permission to store arbitrary telemetry. |
| Consent | [Z] Do not automatically require parental consent for compulsory education. Where you actually rely on consent, it must be freely given, specific, and withdrawable. The Czech age threshold of 15 for Article 8 concerns consent for information society services offered directly to a child, not all school processing. |
| Responsibility | [Z] The school is usually the controller; the hosted application provider is the processor. The actual role decides; a supplier that only delivers software without access to data may not be a processor. |
| Contracts and access | [Z] For a processor, an Article 28 contract: instructions, confidentiality, security, sub-processors, help with rights and incidents, return or deletion, and audit rights. Record monitoring, support, and AI providers too. |
| Records and DPO | [Z] Keep appropriate Article 30 records; regular school processing is not automatically exempt by the 250-employee threshold. Involve a DPO under Article 37; Czech schools deciding on rights and obligations have a specific position as a public authority. |
| Risk assessment | [Z] Security must match the risk under Article 32; design privacy by default under Article 25. Assess the need for a DPIA under Article 35, especially for children, evaluation, monitoring, and profiling. |

Sources for the table: [ÚOOÚ: education](https://uoou.gov.cz/profesional/qa-otazky-a-odpovedi/skolstvi), [School Act No. 561/2004, especially Section 28](https://e-sbirka.gov.cz/sb/2004/561), [Act No. 110/2019](https://e-sbirka.gov.cz/sb/2019/110), [ÚOOÚ: basic guide](https://uoou.gov.cz/verejnost/zakladni-prirucka-k-ochrane-udaju), [EDPB: controller and processor](https://www.edpb.europa.eu/sme/learn-the-basics/data-controller-or-data-processor_en), [EDPB: compliance and DPIA](https://www.edpb.europa.eu/sme/be-compliant/be-compliant_en).

[O] Do not infer an automatic DPIA exemption from Section 10 of Act No. 110/2019 or from the fact that it is a school. Consider Article 35(10) GDPR, the specific operations, and current ÚOOÚ lists. With high residual risk, use prior consultation under Article 36. See [ÚOOÚ: DPIA and the relationship of Czech law to GDPR](https://uoou.gov.cz/profesional/qa-otazky-a-odpovedi/posouzeni-vlivu-na-ochranu-osobnich-udaju).

### 2.3 Information, rights, and transfers

[Z] Prepare clear information under Articles 12–14: controller and DPO, purposes and bases, recipients, transfers, retention, rights, complaint, and relevant automated decision-making. Ensure access, rectification, restriction, and other applicable rights; erasure is not absolute. Portability does not automatically apply to every school processing. Verify the requester's identity proportionally, without blanket collection of ID copies. The default response time is one month; a statutory extension requires conditions and timely notification. Assess Article 22 for solely automated decisions with legal or similarly significant effects, even without AI. A formal teacher click is not meaningful human review. [GDPR, Articles 12–22](https://eur-lex.europa.eu/eli/reg/2016/679/oj).

[Z] GDPR generally does not require Czech-only or EU-only hosting. Assess transfers outside the EEA under Chapter V, including remote support and subcontractors. [P] The default profile uses EEA hosting and backups; document any deviation with an applicable mechanism, a transfer assessment where needed, and supplementary measures. ÚOOÚ and EDPB methodologies are interpretative materials, not a separate product certification. [EDPB: roles and international transfers](https://www.edpb.europa.eu/sme/learn-the-basics/data-controller-or-data-processor_en).


### 2.4 Comparative overview of national jurisdictions and age thresholds [Z/P]

When designing a school application or integrating an AI model, always establish the actual jurisdiction of the school and its learners. An interface language alone does not select national law. Article 8 GDPR permits Member States to adjust the digital consent threshold between 13 and 16 years; national education codes and supervisory authority positions on cloud services and AI diverge substantially across jurisdictions:

| Country / Jurisdiction | Article 8 GDPR Age | Supervisory Authority | Education Statute and Cloud/AI Restrictions |
|---|---|---|---|
| **Czech Republic (CZ)** | 15 years (Act No. 110/2019 Coll.) | ÚOOÚ | Education Act No. 561/2004 Coll. (Section 28); pragmatic approach to licensed clouds; Ministry (MŠMT) and NPI AI guidance (AIDIG). |
| **Spain (ES)** | 14 years (LOPDGDD Art. 7) | AEPD + regional authorities | LOE (DA 23); authoritative AEPD k-anonymity guidance and mandatory school DPO appointments (Art. 34.1.b LOPDGDD). |
| **Germany (DE)** | 16 years (BDSG Section 16) | DSK + 16 state DPAs (LfDI, BayLDA, LDI) | 16 state school acts; strict prohibitions or tight curbs on commercial US clouds (M365, Google) and telemetry; mandatory DPIA (DSFA) for school AI. |
| **France (FR)** | 15 years (Loi Informatique et Libertés) | CNIL | Code de l'éducation; sovereign ENT platforms; ministerial circulars barring free US school clouds; CNIL guidance banning deanonymising class prompt accounts. |
| **Poland (PL)** | 16 years (Data Protection Act 2018) | UODO | Prawo oświatowe; headmaster accountability as controller; ban on entering student PII into AI without Art. 28 contracts; strict judicial ban on school biometrics. |
| **Ukraine (UA)** | 14-18 years (partial capacity under CC) | Ukrainian Parliament Commissioner (Ombudsman) | Law No. 2297-VI and pending full GDPR alignment (Draft Law No. 8153); state ecosystem Mrija; learners residing in the EU fall under full GDPR and national refuge legislation. |

#### Implementation Rules for Cross-Border and Jurisdiction-Specific Deployments

1. **German Deployments (Strict Local First):** [Z] When targeting German schools, assume a 16-year digital consent threshold and complete decentralisation across 16 federal states. In light of DSK rulings on Microsoft 365 and Copilot, prioritise local-only processing (L0) on school servers or open-source infrastructure (Moodle, IServ). Any external data flow requires an exhaustive DPIA (DSFA) and verified zero-telemetry terms.
2. **French Deployments (Sovereignty and Deanonymisation Defence):** [Z] In French schools, apply the 15-year consent threshold and ministerial guidelines on ENT platforms. When deploying AI, enforce CNIL recommendations: do not use shared generic class accounts where pupils enter prompts with indirect identifiers, and ensure automated model output never replaces human teacher grading.
3. **Polish Deployments (Controller Accountability and Biometrics Ban):** [Z] In Poland, full controller liability rests with the school headmaster. Teachers must not independently sign up classes for AI tools without a formal Art. 28 GDPR data processing agreement (umowa powierzenia). Enforce the 16-year age threshold and respect the strict judicial prohibition on biometric identification in schools.
4. **Ukrainian Deployments (EU Diaspora and Euro-Integration):** [Z] For Ukrainian displaced learners in EU schools (Czechia, Poland, Germany), European GDPR and host-nation acts apply in full (e.g. Czech Lex Ukraine). For applications targeting schools in Ukraine, design against draft Law No. 8153, integrate safely with Mrija standards, and enforce strict dataset de-identification before any model processing.

© 2026 Luděk Sušický. [MIT](https://opensource.org/license/mit). Revised edition of version 1.2, based on the original October 2026 guide. Preserve author, license and modification notices.
