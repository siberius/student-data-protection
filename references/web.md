# 9. Web, PWA, and shared devices [P]

<!-- Generated reference; edit the maintained standalone guide. -->

Source sections: 9.

## 9. Web, PWA, and shared devices [P]

- The service worker caches only an explicit allowlist of public static files. Personal APIs, results, HTML with data, and exports use network-only and `Cache-Control: no-store`; a network failure must not return old personal data from a fallback cache.
- The default profile does not store personal data or long-term tokens in localStorage, IndexedDB, or Cache Storage. An offline PWA may show a public shell. An offline solution with personal data needs a separate design: minimal data, a key with controlled access, expiry, deletion, and a lost-device test. A key next to ciphertext provides no effective separation.
- Logout clears UI memory, forms, relevant local storage, caches, and other open tabs. Use `Clear-Site-Data` as a supplement after verifying support and the impact on a shared origin. When returning via history or bfcache, re-verify the page and hide personal content until then.
- Offline logout clears the client and must not claim a successful server revocation until it is confirmed. When connectivity returns, complete the revocation; server expiry limits the residual risk. On a shared device, do not restore a personal session just because the browser window was restored.
- You cannot guarantee removal of screenshots, extensions, OS memory, or an already downloaded file. Do not state "all data disappears after logout"; describe exactly which storage the application controls.
- Prevent XSS with contextual escaping, disabling unverified HTML, and a restrictive CSP with nonce or hash; limit `connect-src`, `frame-ancestors`, `object-src`, and `base-uri`. Do not allow arbitrary CORS origins or credentials with a wildcard. Add `X-Content-Type-Options: nosniff`.
- No advertising trackers or session replay on student screens. Minimise third-party scripts; errors and analytics must redact data. Imports have a size limit, a schema, safe names, and content checks.
- Update the runtime and dependencies, keep a lockfile, check secrets and known vulnerabilities, separate test and production. ASVS level 2 is the default verification target in the relevant scope, not a certification claim. [OWASP ASVS 5.0.0](https://asvs.owasp.org/).

© 2026 Luděk Sušický. [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Revised edition of version 1.1, based on the original October 2026 guide. Preserve author, license and modification notices.
