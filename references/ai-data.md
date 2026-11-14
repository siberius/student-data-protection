# 15. AI data flows, tutoring and RAG [P/O]

<!-- Generated reference; edit the maintained standalone guide. -->

Source sections: 15.

## 15. AI data flows, tutoring and RAG [P/O]

Apply only to an implemented or explicitly requested AI feature. Do not add a model, a vector database or conversation logging merely to use this section. A development assistant and a student-facing service have different data flows and need separate inventory entries.

### 15.1 Minimise and bound the flow

For each flow record purpose, controller/processor roles, approved sources, data categories, user access, recipients, region and remote support, contractual retention, deletion method and necessary transfers. Include prompts, answers, attachments, conversations, checkpoints, moderation/support traces, caches, embeddings, vector indexes, model-provider logs and tool/connector outputs. Derived data can remain personal even without names; embeddings are not an anonymisation guarantee.

Before calling an AI service, select only the fields necessary for the current task and authorised recipient. Strip irrelevant identifiers and secrets. Do not assume a teacher may upload an entire class record. Verify provider settings and terms for the actual account and endpoint; “training off”, an education label or an EU region alone does not settle retention, support access or transfers. Unavailable terms/configuration remain unverified; development can continue with synthetic data.

Keep service keys server-side. Enforce destination, tool and data-scope permissions outside the prompt. Learner input, retrieved documents and generated output are untrusted. Do not allow a document or an answer to change roles, call arbitrary URLs or send records to a new recipient. Where tools fetch resources, constrain destinations and test request-forgery and data-exfiltration paths. Validate structured output before it can change a record, and encode rendered text safely.

### 15.2 Enforce access throughout retrieval

Associate documents, chunks, embeddings and derived summaries with source ID, school, applicable person/group permissions, content version and retention category. Apply authorisation before retrieval and again before releasing results; a similarity score is not a permission. Shared indexes need enforced tenant isolation. Filter searches, counts, citations, previews, exports and conversation reuse, not just the final visible answer. Permission removal or deletion invalidates related retrieval caches and derived copies within a defined window; if invalidation is not yet confirmed, block affected results rather than serve a known stale permission.

Preserve source provenance and distinguish a quotation, model interpretation and unsupported claim. Test cross-school retrieval with synthetic distinctive text and a role change after indexing. A fabricated citation does not become evidence of correctness. Delimit retrieved content and validate actions; “ignore malicious instructions” is not an adequate isolation control.

### 15.3 Tutoring records and deletion

For resumable learning, store only the goal, necessary task references, expressed response/reasoning, assistance conditions, observed revisions and next step needed for the purpose. Do not infer or archive diagnoses, personality or private thought processes. A summary of a learner's reasoning can be personal data. Give it the same permissions, transparency and purpose-bound retention as the underlying activity; on shared devices, provide a clear finish/clear path.

Map deletion and correction across raw sources, chunks, vector indexes, summaries, exported checkpoints, queues, backups and provider-side copies. Record what can be deleted directly, what requires a provider request and what remains under a justified limited retention period. Suspend retrieval where source deletion or permissions make a result invalid. Prevent re-indexing from a stale queue or backup after deletion. Do not promise immediate removal from immutable backups or third-party systems without evidence. Test the actual provider procedure with synthetic data when available, not by assuming an API request removed all copies.

If the model is unavailable or its output cannot be validated, preserve the learner's work and mark feedback unresolved. Do not turn a timeout into full marks, invent an evaluation or silently switch provider. Consequential evaluation remains subject to appropriate accountable human review.

Technical guidance: [OWASP RAG Security](https://cheatsheetseries.owasp.org/cheatsheets/RAG_Security_Cheat_Sheet.html). These are implementation controls, not a replacement for the separate legal classification and provider assessment.

### 15.4 Architectural safeguards for local vs. non-local AI models and k-anonymity [P/Z]

When a creator's proposal or new feature introduces an AI model, first determine whether the model runs **locally within the controller perimeter (L0)** or is a **non-local (cloud/external) model (C1/C2)**. For non-local models, proactively alert the creator that a transformation layer must be established within the application before transferring data outside the school boundary:

| AI Architectural Mode | Flow Characteristics | Required Application Data-Preparation Controls [P] |
|---|---|---|
| **L0: Local / In-Browser AI** (e.g., local model on school server or client browser without telemetry) | Data never leave the school device or local server; no external recipient. | Does not require external k-anonymity or an Article 28 GDPR contract. Enforce local authorization (section 6) and clean shared device cache/memory on logout (section 9). |
| **C1: Non-Local AI - Individual Interaction (1:1)** (e.g., automated feedback on an individual assignment) | Query pertains to a single learner; mathematical k-anonymity cannot be applied to an isolated prompt. | Establish a **local pseudonymisation domain** (EDPB 01/2025): 1. Strip direct identifiers (`name`, `email`, `student_id`, `class`). 2. Keep the mapping table (`lookup table`) strictly on the school's local server outside vendor reach. 3. Sanitize learner free text (redact names, contacts, school title). 4. Use stateless API calls with verified provider zero-retention terms. |
| **C2: Non-Local AI - Cohort / Class Analytics & Exports (1:N)** (e.g., class error trends, dropout prediction, RAG over cohorts) | Multiple learner records sent to the model. In small classes, simple pseudonymisation (`Student_01`) fails. | Establish an **aggregation or k-anonymity pipeline** (EDPB 02/2026, AEPD): 1. Prefer sending **aggregated summaries** (class averages, error counts without microdata). 2. If granular records are required, enforce **k-anonymity (`k >= 5` distinct persons)** and **l-diversity (`l >= 2` distinct sensitive values)** per equivalence class. |

#### Rules for k-Anonymity Pipelines in Non-Local AI and Cohort Exports (Modes C2 and M5)

1. **Attribute Classification Before Transformation:** Direct identifiers (`name`, `birth_number`, `email`, `phone`, `student_id`, `device_id`, `voice`, `photo`) must be completely dropped (do not rely on simple hashing, which remains personal data and enables linkability). For quasi-identifiers (`class`, `date_of_birth / age`, `gender`, `SEN/IEP`, `municipality / postal_code`, `submission_timestamp`), apply **generalization** (e.g., `class 8B` -> `lower secondary`; `age 13` -> `12-15`; `timestamp` -> `week/month`). For sensitive/target attributes (`grade`, `error_type`, `qualitative_feedback`, `counseling_record`), verify diversity across each group.
2. **Against Singling Out (No Record Isolation -> k-Anonymity):** Group records by all active quasi-identifiers. Every equivalence class MUST contain at least **5 distinct individual learners (`k >= 5` calculated via `COUNT(DISTINCT student_id)`)**. If a learner has multiple rows (time series of submissions), 5 rows from one learner do NOT satisfy `k = 5`. Groups with `k < 5` must be further generalized or dropped (**record suppression**).
3. **Against Linkability (No Linkage):** Randomly shuffle row order (**permutation**) before export to avoid re-identification via class register order. In summary tables with row/column totals, apply **complementary suppression** (PTAC) so suppressed cells with `k < 5` cannot be recalculated by subtraction.
4. **Against Inference (No Inference -> l-Diversity):** If all learners in an equivalence class share the same sensitive attribute value (`l = 1`, e.g., all received failing marks or share an identical learning disability), sensitive facts are disclosed via homogeneity attack. Enforce at least **`l >= 2` distinct values** per group, or merge the class into a wider category.
5. **Legal Boundary (Processor Perspective under EDPB 02/2026 and Opinion 28/2024):** [Z] When a cloud AI vendor processes data on behalf of a school (Article 28 processor) and the school retains the original identifiable records, personal data status is assessed from the controller's perspective. Technical k-anonymity does not eliminate the need for a data processing agreement (DPA) or age-gate compliance (e.g., Czech digital consent age 15; vendor terms 13+ with parental consent). K-anonymity operates as an indispensable technical safeguard to minimize risk (Articles 25 and 32 GDPR).

© 2026 Luděk Sušický. [MIT](https://opensource.org/license/mit). Revised edition of version 1.2, based on the original October 2026 guide. Preserve author, license and modification notices.
