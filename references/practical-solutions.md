# 17. Practical solution guide

<!-- Generated reference; edit the maintained standalone guide. -->

Source sections: 17.

## 17. Practical solution guide

### 17.1 Select a data-handling mode

[D] Read this module when asked for a practical solution or a choice of protection level. These are design patterns for school situations, not field-tested deployments or compliance tiers. They supplement the task modes (design, implementation, audit, incident); they do not authorise execution. Reuse known context. Ask only about missing facts that change the choice: purpose and necessary fields, need for verified identity, persistence or official use, shared devices, and recipients including hosting, analytics and AI.

Recommend one mode with a reason and, when useful, a simpler alternative. Combine modes only for the affected features: an anonymous exercise and an identified teacher report can have different boundaries. Do not force every application into the most complex mode. Real-data use still needs the applicable processing decision and safeguards.

| Mode and school example | Minimum design | Checks before real use |
|---|---|---|
| M1 One-off practice: fractions exercise | No learner name or account when unnecessary; answers in working memory; clear on finish. A local/static activity can avoid a central record. | Reload, history and the next user must not reveal answers; inspect actual requests, logs, telemetry and browser storage before claiming anonymity. |
| M2 Limited collection: event signup | Collect only fields needed for the event; protect receipt and access; set a purpose-based deletion trigger. Treat an unverified submission as pending. | Foreign-record access, unexpected writable fields, submission limits and deletion. A shared code alone cannot establish identity for official records. |
| M3 Resume learning: saved practice progress | Keep minimum progress; use verified school identity for personal history. Assess any pseudonymous access mechanism against its consequences. | Another learner's history, shared-device logout, changed class membership and recovery. A pseudonym is not automatically anonymous. |
| M4 Official records: grades or attendance | Verified identity, trusted authorisation, controlled writes, conflict handling, correction history and recoverable storage; retention follows the actual agenda. | Forged owner or grade, revoked access, concurrent edits and recovery. Do not copy a generic practice-data deletion period. |
| M5 Teacher reports and exports | Scope access to assigned classes and purpose; aggregate when sufficient; minimise fields and recheck permission on download. | Foreign class, expired/revoked link, CSV formula injection, revealing filenames and the lifecycle of downloaded copies. |
| M6 AI tutoring | First consider reviewed static explanations. If AI is needed, define approved recipients, minimise input, keep service keys server-side and validate output. | Retrieval permissions, actual outbound data, injection, outage, provider retention and deletion. Model output alone must not write an official grade. |

For object access enforcement, use [OWASP Authorization](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html). The mode table and school examples are this guide's recommendations; they are not a claim that OWASP evaluated these applications.

### 17.2 Choose an implementation path

- **Local/static activity:** suitable when no shared record is needed. Check local persistence, external assets and host metadata; offline operation alone does not prove absence of personal data.
- **Existing school platform:** reuse maintained identity, permissions and storage where suitable. Verify the actual configuration, recipients, export settings and deletion behaviour.
- **Custom server application:** use maintained components for authentication and sessions, enforce server permissions, validate inputs and provide storage protection, recovery and an operational owner. PHP with SQLite is one possible stack; preserve an equivalent supported architecture.
- **Optional AI service:** add a bounded data flow, resource limits, controlled failure handling and human review where consequences require it. The learning activity must retain a usable fallback.

Estimate effort only after inspecting the environment and dependencies. Do not promise security within a fixed number of minutes or introduce a new password system when suitable school SSO exists.

### 17.3 Apply only the selected recipe

For M1, trace network/storage use, remove unnecessary collection, implement end/reset behaviour and check the next-user experience. For M2, define an allowlist of fields, protected submission/read boundaries and deletion ownership. For M3, establish identity and record ownership, then implement resume/logout and access-revocation handling. For M4, define authorised writes, corrections and conflicts before persistence and recovery. For M5, build a scoped query, minimise the export and authorise its download. Load the corresponding technical module only where needed.

For M6, resolve identity where needed, enforce permissions before selecting source content and sending it to the model, minimise the request, validate the response and display it or submit a separately authorised write for review. Filtering an answer after the call cannot undo disclosure to a provider. Include indexes, caches and summaries in access/deletion design. On outage or uncertain validation, preserve work and return a clear fallback without a silent authoritative write. Consult section 15 and [OWASP RAG Security](https://cheatsheetseries.owasp.org/cheatsheets/RAG_Security_Cheat_Sheet.html) for these controls.

### 17.4 Repair an existing application

Separate immediate containment from the durable correction. Propose the smallest effective containment, such as restricting a public export or stopping unnecessary collection. Removing an exposed client-side key is insufficient: assess revocation and exposure through the authorised incident process. State affected users, verification, residual exposure and the next action. Preserve necessary evidence without copying sensitive logs into a chat.

For the durable correction, fix the evidenced identity, authorisation, storage or operational boundary and retain sound existing components. For migrations affecting records, include integrity checks, backup/recovery and a rollback plan. A proposed containment is not permission to shut down production, revoke credentials or notify others. Escalate suspected disclosure for incident assessment under the applicable local rules.

### 17.5 Deliver a solution card

Keep the initial answer short; expand only the selected mode and relevant controls. Use this adaptable card:

```text
Situation and goal:
Recommended mode and reason:
Necessary fields and data to avoid:
Data flow, recipients and storage:
Identity and permissions:
Retention, deletion and recovery:
Concrete implementation steps:
Checks before use and actual execution status:
Residual risks and unverified assumptions:
Responsible owner and next decision:
```

Label proposed checks separately from performed checks and give N/A reasons. Use synthetic examples, not real learner records. For Spain, use the Spanish legal module; for EU/Czech contexts, use the applicable local framework. A mode or language never selects jurisdiction automatically.

### 17.6 Start with an existing application

When the user brings an existing application, offer a proportionate entry audit with a remediation plan. Reuse any supplied code, architecture and prior findings. If an audit is already requested, proceed within that scope rather than asking for the same approval again. If the user requests a narrow implementation, inspect the affected boundary as part of that work; offer a broader audit separately when evidence warrants it.

Offer two useful depths: a focused review of the changed feature and its data flow, or a broader pre-deployment review of identity, permissions, recipients, retention and recovery. Recommend depth from actual consequences, such as new real-data use, official records, a public export, an AI recipient or a serious observed failure. Missing source or configuration limits what can be concluded; request sanitised code/configuration or a synthetic demonstration, never a production database or secrets. A screenshot alone does not establish server security.

Map current behaviour and evidence first, then deliver prioritised findings with location, affected data/users, observed failure versus hypothesis, proposed correction, effort/dependencies and a verification method. Start with evidenced exposure or integrity risks, then relevant gaps; keep optional improvements separate. Recognise controls that already work. Use the solution card for the selected remediation and preserve existing sound architecture.

An audit request authorises assessment, not application changes. Propose fixes unless implementation is already authorised; apply only that authorised scope. Record whether each item is proposed, implemented but unverified, verified with stated evidence, or unresolved. Run intrusive checks only in an authorised environment; without execution, provide a check plan. Do not mark the application safe for real use solely because the audit produced no finding.

© 2026 Luděk Sušický. [MIT](https://opensource.org/license/mit). Revised edition of version 1.1, based on the original October 2026 guide. Preserve author, license and modification notices.
