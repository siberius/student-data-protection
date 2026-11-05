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

© 2026 Luděk Sušický. [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Revised edition of version 1.1, based on the original October 2026 guide. Preserve author, license and modification notices.
