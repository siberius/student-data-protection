# 8. CSV and SQLite [P]

<!-- Generated reference; edit the maintained standalone guide. -->

Source sections: 8.

## 8. CSV and SQLite [P]

### 8.1 SQLite as a transactional store

- SQLite is an acceptable choice; ordinary SQLite does not encrypt by itself. The application accesses it on the server, not through a public database download. For multiple instances and high concurrency, choose a database that matches the architecture; do not share the file uncontrolled over a network drive.
- Default profile: application-level AES-256-GCM encrypted personal payloads plus an encrypted disk or volume. Database encryption extensions have their own algorithms; do not claim that SQLCipher automatically means AES-GCM. Unencrypted indexes, relations, and counts can still be personal metadata.
- The directory and database are accessible only to the service account, on Unix roughly directory `0700`, files `0600`, an equivalent ACL elsewhere. No public webroot, static path, public bucket, synced personal folder, or repository.
- Parameterised queries; dynamic field names only from an allowlist. Enable foreign keys on every connection, and also constrain important relations by school. Protect submission, one-time invitations, and the change audit transactionally. Handle a locked database, a full disk, and an incomplete write.
- Include `-wal`, `-shm`, journal, temporary files, dumps, and crash or swap files in protection and retention. Back up with the consistent [SQLite Online Backup API](https://sqlite.org/backup.html) or a verified snapshot, not a blind copy of the live main file without the WAL.
- Handle deletion at the data and copy level. `secure_delete`, checkpoint, or `VACUUM` can help, but they do not guarantee physical erasure on SSDs, snapshots, and old backups. For FTS and other extensions, verify residual copies. [SQLite PRAGMA secure_delete](https://sqlite.org/pragma.html#pragma_secure_delete).

### 8.2 CSV as export or limited storage

Use a transactional database that matches operation as the authoritative store, and CSV as a controlled export; SQLite suits defined smaller deployments. If a project needs CSV as the primary store, implement a single writer, locking, schema validation, revisions, and atomic file replacement after a successful write and sync. On a crash, the last complete version remains. CSV alone provides no transactions, roles, or encryption.

Archive CSV on the server in an authenticated AES-GCM container, not just by renaming the extension. Build plaintext in memory; a temporary file only on protected encrypted space with automatic cleanup. An ordinary password-protected ZIP is not a replacement for this profile.

Allow export only to a role with explicit permission, within the relevant school, people, and data categories. Include only necessary columns, never session tokens or device IDs without a documented purpose. Audit both creation and download. The download endpoint re-verifies the session and permissions, returns `Cache-Control: no-store` and `Content-Disposition: attachment`; any link is short-lived and scoped, not a public permanent URL.

Use a CSV library with proper quoting of delimiters, quotes, and newlines. Protection against formula injection is a separate step: for a human spreadsheet export, handle text starting with `=`, `+`, `-`, `@`, control characters, and bypass variants. Parse numeric columns as numbers, not arbitrary strings. An apostrophe and quoting are not a universal guarantee after saving and reopening in Excel. Define the supported import procedure and test Excel and LibreOffice; if they cannot ensure safety, offer a format with explicitly text cells for human reading and refuse the risky export. Do not change the original data because of the export. [OWASP CSV Injection](https://owasp.org/www-community/attacks/CSV_Injection).

A downloaded, opened CSV is an unencrypted copy on the recipient's device. Inform about secure storage and the deletion period; logout does not delete it. If an encrypted file transfer outside the application is needed, use a managed secure channel or a suitable container with separate secret delivery.

© 2026 Luděk Sušický. [MIT](https://opensource.org/license/mit). Revised edition of version 1.1, based on the original October 2026 guide. Preserve author, license and modification notices.
