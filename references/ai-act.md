# 3. AI Act: applicability, classification, and dates

<!-- Generated reference; edit the maintained standalone guide. -->

Source sections: 3.

## 3. AI Act: applicability, classification, and dates

### 3.1 Separate the development tool from the product

- **An application written with AI:** is not thereby an AI system. Storing forms, attendance records, filtering records, or a fixed point calculation are usually ordinary deterministic processing. Assess the actual Article 3(1) definition, not the marketing name.
- **A developer using an AI assistant:** the organisation may be a deployer of that assistant. Duties are assessed for its use; they do not automatically transfer to the delivered application without AI features.
- **AI functionality in the application:** generating feedback, evaluating free-text answers, predicting performance, personalising by results, or monitoring a test require a separate assessment. AI can be an external API or an internal batch process, not only a chatbot in the UI.

[P] Keep an inventory: feature, purpose, model and version, inputs, outputs, recipients, impact on the student, provider, deployer, GDPR basis, classification, and review date. A change of purpose or a substantial modification may change roles under Article 25. [AI Act: official regulation](https://eur-lex.europa.eu/eli/reg/2024/1689/oj), [Commission: navigating the AI Act](https://digital-strategy.ec.europa.eu/en/faqs/navigating-ai-act).

### 3.2 Article 4: AI literacy

[Z/O] Chapter I applies from 2 February 2025. The currently displayed text of Article 4 on the AI Act Service Desk after the July 2026 amendment requires providers and deployers to take measures supporting the development of AI literacy; it does not explicitly require guaranteeing a certain level for every individual. Do not claim the obligation has disappeared, and do not repeat the original wording as current without verification.

[P] Provide appropriate training by role: model errors, data protection, bias, prompt injection, output verification, human oversight, and reporting problems. Record content, date, and attendance; the skill does not require a specific certificate. It also applies to staff using a development AI tool if they fall within the relevant role. [Article 4: current Commission view](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-4).

### 3.3 Article 5: prohibited practices

[Z] For a school application, check in particular the prohibition of AI emotion inference in educational institutions, with a narrow exception for medical or safety reasons. Ordinary attention or cheating monitoring does not automatically meet that exception. Also check harmful manipulation, exploitation of age-related vulnerability, prohibited social scoring, and sensitive biometric categorisation. For each prohibition, respect all its conditions; an ordinary school record or score is not prohibited social scoring by itself.

[P] This profile does not allow emotion recognition, biometric categorisation, or camera AI monitoring of students. The amendment also introduces new prohibitions of certain intimate synthetic material and child sexual abuse material, applicable from 2 December 2026; do not create such features at all. Prohibitions are not replaced by parental or teacher consent. [Article 5](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-5), [Article 113](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-113).

### 3.4 Annex III point 3: education and high-risk AI

[Z] Assess AI intended for admission, access, or assignment to educational institutions, evaluating learning outcomes including steering the learning process, determining the appropriate level of education, and monitoring or detecting prohibited behaviour during tests. AI grade suggestions may fall within this area even if a teacher later approves them. Using AI in a school is not enough to classify it as high-risk. [Annex III](https://ai-act-service-desk.ec.europa.eu/en/ai-act/annex-3).

[Z] The Article 6(3) exception requires no significant risk to health, safety, or fundamental rights, including not materially influencing the outcome of decision-making, and a corresponding condition: a narrow procedural task; improving the result of a previously completed human activity; detecting patterns or deviations without improperly replacing or influencing human assessment; or a preparatory task. It is not an automatic exception of "the teacher stays in the process". An Annex III system that performs profiling of natural persons is always high-risk. The provider must document the exception conclusion before placing the system on the market or into service. [Article 6](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-6).

[O] Registration of exceptions: verify Article 49(2) in the version in force. When checking sources, Articles 6 and 49 on the Service Desk still mentioned registration, while the Commission's amendment notice spoke of simplifying it. The discrepancy did not justify claiming that registration was fully abolished. [Article 49](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-49), [Commission notice on the amendment](https://digital-strategy.ec.europa.eu/en/news/ai-omnibus-enters-force).

[P] Generating a general question without student data and without assessment is usually a different risk from AI grading a specific child. For the latter, involve the DPO and expert legal assessment before production; document the purpose, impact, and actual human oversight.

### 3.5 Duties for actual high-risk use

[Z/O] Depending on role and applicable date, prepare risk management, data governance, technical documentation, logging, human oversight, accuracy, robustness, and cybersecurity; for a provider also a quality management system, the relevant conformity assessment, declaration, marking, and registration. This skill's ordinary checklist does not replace that assessment. [AI Act: Commission overview](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai).

A deployer must use the instructions appropriately, ensure competent oversight, monitor operation, and handle incidents. Automatic logs under its control have a special rule of a reasonable period of at least six months, unless an applicable EU or national rule provides otherwise. Do not confuse them with all ordinary web logs. [Article 26](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-26).

For public authorities and private providers of public services, assess a FRIA under Article 27; it may be relevant for a school. FRIA and GDPR DPIA have a different scope and can be coordinated. Also verify information to affected persons and the applicability of Article 50 to AI interaction or generated content. [Article 27](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-27), [Commission: FAQ](https://digital-strategy.ec.europa.eu/en/faqs/navigating-ai-act).

### 3.6 Timeline and level of legal verification

| Date | Significance for the assessment |
|---|---|
| 1 August 2024 | The original AI Act enters into force. |
| 2 February 2025 | Chapters I and II apply, including Article 4 and the original Article 5 prohibitions. |
| 2 August 2025 | Selected parts apply, including GPAI and governance and supervision; consider transitional provisions for older models. |
| 27 July 2026 | The Commission states that the Digital Omnibus on AI enters into force. |
| 2 August 2026 | General date of applicability with exceptions; do not treat it as the universal date for all high-risk duties. |
| 2 December 2026 | New prohibitions under amended Article 113(a); check specific transparency transitions per system. |
| 2 December 2027 | Amended Article 113 lists Chapter III Sections 1–3, except Article 6(5), for Article 6(2) and Annex III. |
| 2 August 2028 | Corresponding date for Article 6(1) and Annex I. |

Sources: [Article 113 on the Service Desk](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-113), [Commission notice of 27 July 2026](https://digital-strategy.ec.europa.eu/en/news/ai-omnibus-enters-force), [Commission implementation timeline](https://ai-act-service-desk.ec.europa.eu/en/ai-act/eu-ai-act-implementation-timeline). Do not adopt the original dates of 2 August 2026 for Annex III and 2 August 2027 for product systems without checking the amendment. For systems already in use, assess Article 111 individually; do not infer universal grandfathering.

**Limits of verification:** during preparation, the official Commission Service Desk was readable and states consolidation as of 27 July 2026, as was the official report on the amendment. Direct EUR-Lex returned an anti-bot page when loading the original and amended texts. The timeline and amended Article 4 are therefore verified on the official Commission website, not by independently reading the full Official Journal. The Commission refers to [Regulation (EU) 2026/1744](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202601744) and the [consolidation of the AI Act as of 27 July 2026](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02024R1689-20260727). Before any legally significant deployment, confirm these texts, the applicability date of the specific duty, transitions, and the current Czech designation of competent authorities. It is not correct to automatically label ÚOOÚ as the sole AI Act supervisor. GDPR applies independently of any postponement of high-risk rules.

© 2026 Luděk Sušický. [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Revised edition of version 1.1, based on the original October 2026 guide. Preserve author, license and modification notices.
