# 7. Encryption and key management [P]

<!-- Generated reference; edit the maintained standalone guide. -->

Source sections: 7.

## 7. Encryption and key management [P]

GDPR does not prescribe AES-256-GCM or any single universal cipher. This profile chooses it for application-level protection of personal payloads, CSV archives, and backups; TLS protects transport. Encryption does not replace authorisation and does not protect data from an authorised but compromised process that holds the key.

### 7.1 AES-256-GCM

- Use a proven high-level library, a 256-bit random key, a 96-bit nonce or IV, and a 128-bit authentication tag. Do not build your own cipher. The same key MUST NOT reuse a nonce, not even after a restart, recovery, or across instances.
- For row payloads, you can use a 96-bit CSPRNG nonce with a unique `(key_id, nonce)` index, atomic reservation, and regeneration on collision. After restoring an old database, first introduce a new key for new writes. Track the aggregate number of encryptions under a key; the profile rotates at the latest after 10^6 operations or one year, sooner on an incident. This conservative limit does not rewrite the general NIST limit.
- For a whole CSV archive or backup object, create a new data key for each object and encrypt it with a managed wrapping key. Handle large files with a library for authenticated streaming; do not invent an unverified chunk format.
- AAD must canonically bind the format version, school, type and ID of the object, and record version. AAD is not secret; a name does not belong in it. Obtain the expected context independently, not only from an envelope supplied by an attacker.
- The envelope contains `format_version`, `algorithm`, `key_id`, `nonce`, `ciphertext`, `tag`, and necessary public metadata. Reject a change to the nonce, AAD, ciphertext, or tag without returning any plaintext. GCM alone does not prevent replay of an entire older valid version; check the version against trusted state and audit.

Background: [NIST SP 800-38D](https://csrc.nist.gov/pubs/sp/800/38/d/final), [NIST: revision announcement](https://csrc.nist.gov/news/2024/nist-to-revise-sp-80038d-gcm-and-gmac-modes). Do not treat the revision announcement as a finished new standard.

### 7.2 Keys and transport

Separate data keys from data, and keep wrapping keys in a KMS or HSM or a suitable secrets manager. The application receives only minimal permissions; keys do not belong in a repository, client-side JS, an image, or backups together with unprotected data. Separate production from test and separate key purposes. Rotation must preserve readability of data still legitimately retained and allow revocation. Monitor decryption failures and key operations, not key values. [OWASP Cryptographic Storage](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html).

HTTPS and WSS everywhere; prefer TLS 1.3, TLS 1.2 only where necessary for compatibility with ECDHE and AEAD. Disable SSL and TLS 1.0 and 1.1, weak suites, and TLS compression. AES-128-GCM or ChaCha20-Poly1305 in TLS do not by themselves violate this profile. Verify certificates, renewal, and internal network links. Deploy HSTS after verifying HTTPS, for example `max-age=31536000`; `includeSubDomains` only after checking all subdomains. Never send personal data over an insecure request or before a redirect. [OWASP TLS](https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Security_Cheat_Sheet.html).

© 2026 Luděk Sušický. [MIT](https://opensource.org/license/mit). Revised edition of version 1.1, based on the original October 2026 guide. Preserve author, license and modification notices.
