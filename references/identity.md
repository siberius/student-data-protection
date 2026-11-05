# 5. Authentication, optional invitations, and sessions [P]

<!-- Generated reference; edit the maintained standalone guide. -->

Source sections: 5, 6.

## 5. Authentication, optional invitations, and sessions [P]

### Choosing an access mode

For long-term personal records, communication, and history, use an individual verified account (for example school SSO or a passkey). Offer secure recovery and account deletion; do not assume every student must have a password. For parents, verify the account and the current permission for the specific child. A one-time form without an account may only accept a defined submission; the confirmation must not reveal stored data.

Sections 5.1 and 5.2 apply **only when entry codes or QR are used**. They are not a reason to introduce them. Section 5.3 applies to all web sessions.

### 5.1 A four-digit code is only a ticket into the room

Four digits have 10,000 combinations, about 13.3 bits of entropy. The code MUST NOT unlock history, a class list, grades, a teacher interface, or take over an existing personal record.

1. Generate the code with a CSPRNG using uniform selection, including leading zeros. Limit its search to a school or room; prevent collisions of active codes in that scope. Do not derive it from time or a teacher ID.
2. The default entry validity is 10 minutes, with explicit extension by the teacher; ending admission invalidates the code. Ending entry does not have to terminate sessions already accepted.
3. Do not expose personal data or a list of non-public activities before verification. An error response must not distinguish whether the code exists, expired, or belongs to another school.
4. Default limits: 5 failed attempts per 60 seconds per pre-entry session, then a 60-second pause; 100 failed attempts per 5 minutes per source IP; 200 failed attempts per 5 minutes per school entry space triggers temporary throttling and a teacher alert. Counters are atomic and shared across instances. Tune them for school NAT and test availability; do not permanently block an entire school without distinction.
5. A new browser session must not bypass all limits. For distributed guessing, also account for a waiting room and teacher confirmation. Limits are not a replacement for verifying a person; an attacker in the classroom may legitimately know the code.
6. Store the code briefly; for verification use an HMAC with a separate server secret and room context. A plain hash of four digits does not provide resistance to offline guessing. Do not log the code.

### 5.2 QR

- A QR may carry the same code and then has the same security. Do not present it as stronger login.
- The preferred QR contains a random invitation with at least 128 bits of entropy, the purpose `join`, the room, expiry, and a revocation option. A shared class invitation may be reusable but still does not confirm identity.
- An individual invitation is single-use and the exchange for a session is atomic. The server stores only a hash of the random secret; two sessions must not arise from concurrent redemption.
- Do not put the token in an ordinary query parameter that gets logged. A suitable flow: URL fragment, read by first-party code only, immediately remove via `history.replaceState`, submit over HTTPS POST, and exchange for a cookie. Set `Referrer-Policy: no-referrer`. A fragment is not absolute protection against history, extensions, or screenshots; short validity, revocation, and permission scope are essential.

### 5.3 Session lifecycle

- The server issues 32 random bytes from a CSPRNG; it stores a hash of the token, scope, verified identity or limited anonymous session, expiry, and revocation status. The token carries no name or grade.
- Cookie: `__Host-school_session`, `Secure`, `HttpOnly`, `SameSite=Lax` or `Strict` according to the verified flow, `Path=/`, no `Domain`. Do not store a bearer token in localStorage, a URL, or ordinary logs.
- A new entry or login and a permission change create a new token and revoke the original. The server does not accept a token chosen by the client.
- Default inactivity for a student is 30 minutes, absolute maximum 4 hours or the end of a one-time activity. For a teacher, 15 minutes of inactivity and 8 hours absolute; document available adjustments for longer work and accessibility. Automatic polling does not extend inactivity.
- Logout is a server revocation, cookie expiry, and local cleanup. On a password change, role removal, or incident, an administrator can revoke all related sessions.
- After logout, there is no return to personal records by name or device ID. Allow recovery only through new verification and securely transferred permission.
- Write requests are protected by a CSRF token and origin check; GET does not change state. `SameSite` is a supplementary control. WebSocket verifies Origin, session, and permissions for each room and ends access after revocation.

Background: [OWASP Session Management](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html), [OWASP ASVS 5.0.0](https://asvs.owasp.org/). The time and count limits are choices of this profile, not legal values.

## 6. Roles, permissions, and record integrity [P]

| Role | Permitted scope |
|---|---|
| Unauthenticated | Public content and any limited submission; no reading of personal records. |
| One-time participant | Only the currently permitted activity or submission; no history or other people's records. |
| Verified student | Their own data and student-facing functions; history only within the purpose and permission. They do not change officially confirmed data by merely editing a profile. |
| Verified legal guardian | Only data of the specific child for whom they currently have verified permission; never automatically the whole class. |
| Teacher or school staff | Only assigned people, classes, processes, and data categories needed for the work. |
| Specialised staff | More sensitive agenda only with explicit authorisation; the teacher role alone does not open counselling or health data. |
| School administrator | Management of school membership and permissions; not automatically access to all content. |
| Operational support | Technical diagnostics without student content; exceptional access limited in time, justified, and audited. |
| Integration or service account | Only the specific operations and data needed for the approved integration. |
| DPO or auditor | Defined records and audit; not an automatic right to change school records. |

Check permissions on the server for every operation and object, including lists, result counts, search, attachments, exports, WebSocket, and background jobs. Derive `school_id`, role, and ownership from the verified context. If the client determines the person on whose behalf it acts, verify the corresponding relationship. Deny by default. A UUID or a hidden button is not authorisation.

A change of school or class, an employee leaving, account deletion, or a change of representation must update access, including active sessions, shared links, and integrations. Do not derive parental permission only from a matching surname or knowledge of a child's birth date. Review memberships and privileged roles regularly.

Staff with access to student data and administrators have an individual account via SSO or secure login; the profile requires MFA, preferably a passkey. Account recovery must not bypass MFA. Store your own passwords one-way with a maintained Argon2id implementation, never AES; set parameters according to current recommendations and hosting performance.

All inputs are validated by the server. Ownership, approval, attendance, grades, and other authoritative data have permitted transitions and designated roles. Important writes are transactional; an idempotency key tied to the user and operation prevents duplicate creation. Concurrent changes to the same version raise a controlled conflict, not a silent overwrite. A correction of important data records the author, reason, and previous version in a protected history with its own retention.

**If the application evaluates:** the server calculates or confirms the score; a client result is not authoritative; the answer key is not published early. **If it accepts applications or attendance:** the user's submission is distinct from the approved record; the user must not set the approval status themselves.

© 2026 Luděk Sušický. [MIT](https://opensource.org/license/mit). Revised edition of version 1.1, based on the original October 2026 guide. Preserve author, license and modification notices.
