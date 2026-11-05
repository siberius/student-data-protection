# 4. Data model, collection, and minimisation [P]

<!-- Generated reference; edit the maintained standalone guide. -->

Source sections: 4.

## 4. Data model, collection, and minimisation [P]

### 4.1 Data inventory and identity

- For each field, determine purpose, source, whether it is mandatory or optional, legal basis, recipients, sensitivity, retention, and how it is erased. Refusing an optional field must not block an unrelated basic service.
- Separate `school_id`, the account `user_id`, an internal `student_id`, `record_id`, an optional `submission_id`, and a secret session token. An account and the person the data concerns are not the same: a teacher or parent may legitimately act for a student. A public random ID is not a permission.
- A user-entered name is untrusted data, not authentication. Do not use a name, date of birth, class, or device ID as the sole key to history or to change an existing profile.
- Separate identity mapping from content records where operation allows. For an unverified submission, keep the link to the student unconfirmed; verify and audit the assignment. Do not merge people just because they share a name.
- Allow anonymous or pseudonymous collection if the purpose does not need identity. Do not label a form anonymous if it can be linked to an account, ID, time, or other record.
- Do not collect IMEI, MAC, advertising ID, or fingerprint. If an installation ID is necessary, generate it randomly and limit it by purpose and retention. It is not authentication or anonymization. On a shared device, prefer a session-scoped ID.
- Record the source of the record, verification status, author of the change, version, and retention category; set `expires_at` where the period can be determined. Names, contacts, and content do not belong in URLs, file names, metrics, or error messages.

### 4.2 Forms, attachments, and integrations

- On the server, allow only declared fields and values. Reject unknown fields, protect system fields from mass assignment. Define lengths, types, ranges, encoding, and submission size; do not execute HTML or formulas.
- A public form must not offer people search, a class list with names, or submission history. An unverified submission does not automatically update school records. Limit automated abuse and volume; any bot protection must not introduce unverified tracking of children.
- For free text, warn what must not be entered and offer structured minimal fields. Assess photographs, voice, location, health information, and counselling records separately; do not start collecting them "for future use".
- Accept attachments by a type allowlist, verify the actual format, size limit, and malicious content. Store them outside the webroot under a random name, without execution; reject or safely isolate active content. Previews, OCR, thumbnails, and metadata follow the same permissions and retention as the original.
- Always authorise an attachment download by school, person, purpose, and role. A short-lived signed link is a transferable permission; limit its time and scope. A shared link must not turn a document into a public one.
- A CSV or API import has a mapping preview, duplicate and target-school validation, atomic confirmation, and audit. An external ID is unique within the source system and school. Do not overwrite records based on a name match.
- Integrations have their own service identity with minimal scope, secret rotation, and revocation. Verify webhooks by signature, time window, and replay protection. The default profile sends push and email notifications without sensitive content, only with a link to an authenticated interface.

Background for minimisation and data separation: [ENISA: Data Protection Engineering](https://www.enisa.europa.eu/sites/default/files/publications/ENISA%20Report%20-%20Data%20Protection%20Engineering.pdf). The specific schema and implementation choices above are this skill's proposal.

© 2026 Luděk Sušický. [MIT](https://opensource.org/license/mit). Revised edition of version 1.1, based on the original October 2026 guide. Preserve author, license and modification notices.
