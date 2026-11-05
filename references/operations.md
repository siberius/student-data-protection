# 10. Audit, retention, and recovery [P/Z]

<!-- Generated reference; edit the maintained standalone guide. -->

Source sections: 10, 11.

## 10. Audit, retention, and recovery [P/Z]

### Audit [P]

Record UTC time, internal actor, school, operation, object, result, and correlation ID. Capture login and its failure, permission removal, identity verification or relinking, changes to record data, reads of highly sensitive records, exports, bulk deletion, exceptional access use, key rotation, and restores. Do not write tokens, codes, keys, form content, messages, or names into ordinary operational logs. Keep the protected history of important changes separately.

Store the audit in an append-only target that the ordinary application cannot delete from. Check integrity and access, synchronise time. A hash chain without an independently protected anchor does not prove immutability. A critical change of record data, permission, or export must have a permanent audit record or transactional outbox before confirming success; an audit failure must not silently bypass the change.

### Retention table

[Z] Keep data only for the period necessary for the purpose and applicable duties. GDPR does not set a universal number of days for all school applications. [P] The following values are a proposal to be confirmed by the school; legal duties and the file and retention plan take precedence.

| Category | Default proposal |
|---|---|
| Entry code or QR secret | Invalidate after expiry or closing entry; do not keep a usable secret. |
| Session secret | Revoke immediately on logout or expiry, remove inactive verifiers within 24 hours; audit without secrets can be kept longer. |
| Temporary participation and device ID for a one-time activity | Remove within 24 hours after it ends, unless another necessary purpose is documented. |
| Work in progress submissions | Automatic saving only when needed; proposal 7 days from the last edit, the user knows the expiry. |
| One-time form or registration | Period according to completion of the purpose and any review; set a specific trigger and period before launch. No universal retention for all forms. |
| Student records, attendance, assessment, contacts | Specific periods by purpose and the applicable file and retention plan; account termination does not automatically erase mandatory records. |
| Messages, portfolios, and attachments | Separate categories; confirm the need after the end of teaching or the relationship with the school. Derived copies must not have unlimited retention. |
| History of corrections and links to people | Define by the purpose of verifiability and review; it must not be an unlimited archive of all deleted data. |
| Temporary server export | At most 24 hours; always verify the download right again. |
| Ordinary security audit | 90 days; an incident may justify limited suspension of deletion. |
| AI high-risk automatic logs | A separate regime under applicable Article 26(6); 90 days cannot be applied blindly. |
| Backups | Rolling 30 days, without endless retention of old snapshots. |

Run automatic cleanup daily and monitor errors. Deletion includes indexes, attachments, exports, caches, and queues. For immutable backups, until a limited retention period ends you can use isolation from ordinary operation and mandatory re-application of deletions on restore; document this procedure and do not conceal the existence of backups. Verify anonymization also against identification of a small class or a rare combination of data.

Backups are encrypted, separated, and at least one copy is protected from change by an attacker. Default operational targets: RPO 24 hours, RTO 8 hours; for critical records the school tightens them according to the impact of loss or outage. Restore at least quarterly in isolation, including keys, relations, audit, deletions, and invalidation of historical sessions. Successful backup alone does not prove recoverability.

## 11. Incidents [Z/P]

[Z] A processor reports a breach to the controller without undue delay. The controller reports to ÚOOÚ without undue delay and where possible within 72 hours of becoming aware of it, unless the risk to rights and freedoms is unlikely; justify any delay. Where high risk is likely, inform affected persons without undue delay with an assessment of the Article 34 exceptions. Unreported breaches are also documented. Encryption can reduce risk, but a key leak, integrity, or availability requires its own assessment. [ÚOOÚ: personal data breach](https://uoou.gov.cz/profesional/poruseni-zabezpeceni-osobnich-udaju), [Articles 33–34 GDPR in ÚOOÚ material](https://uoou.gov.cz/media/poskytnute-informace/2019/31122019/uoou-0612218-24.pdf).

[P] Prepare contacts for the controller, DPO, and operational service. Internal target: escalation to the responsible person within 1 hour, initial assessment within 24 hours; these are organisational targets, not legal deadlines. Runbook:

1. Record the time of detection and the scope; preserve evidence securely, do not circulate entire databases.
2. Limit harm: revoke sessions and invitations, close the dangerous endpoint, isolate the affected service; ensure alternative operation of the affected agenda.
3. Determine the data, people, recipients, key availability, and possible consequences; consider confidentiality, integrity, and availability.
4. Prepare the decision on notification and its supporting materials. Do not wait for a complete forensic report; a notification can be supplemented gradually.
5. Fix the cause, rotate keys as needed, restore and verify data. Document follow-up measures and update tests.

Separately assess any duties under the Czech Cybersecurity Act and the AI Act if they apply to the operator or system; their deadlines are not automatically the GDPR 72 hours. Methodological background: [NIST SP 800-61 Rev. 3, final April 2025](https://csrc.nist.gov/pubs/sp/800/61/r3/final).

© 2026 Luděk Sušický. [MIT](https://opensource.org/license/mit). Revised edition of version 1.1, based on the original October 2026 guide. Preserve author, license and modification notices.
