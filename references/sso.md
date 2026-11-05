# 16. Federated school login and SSO [P]

<!-- Generated reference; edit the maintained standalone guide. -->

Source sections: 16.

## 16. Federated school login and SSO [P]

Apply only where an identity provider is used. Do not replace a working login just to introduce SSO. Use a maintained protocol library and the provider's current integration instructions; OAuth authorisation alone is not proof of user identity.

For OIDC, validate issuer, signature with trusted key discovery, intended audience and any required authorised party, expiry, nonce and correlation to the login transaction. Use an authorisation-code flow with PKCE where supported and required by the client profile; constrain redirect URIs exactly, bind the callback to the initiating browser and prevent login CSRF and code replay. Do not treat an access token as an ID token. For SAML, validate the required signatures, issuer, audience, destination, recipient, request correlation, time conditions and assertion replay using a maintained implementation. Do not invent an XML signature parser. Choose the checks for the actual protocol and flow, not both protocols by default.

Link identities by a verified stable identifier scoped to the trusted issuer (for example issuer plus subject), then map authorised membership to the correct school and application role. Email address, display name, domain or an untrusted school claim alone must not merge accounts or grant staff access. Define enrolment, account linking, renamed addresses, subject changes, duplicate names and removal of membership. Privileged role assignment requires trusted entitlement data or an authorised administrative step. A successful identity-provider login does not itself grant access to every school record.

Keep local sessions revocable; provider logout and application logout have different scopes. Re-evaluate membership and privileges according to documented change propagation, and provide immediate application-side revocation for a known removal. Do not silently retain staff access until a distant provider token expiry. On provider outage or invalid metadata, fail closed for protected access and offer an appropriate operational fallback; do not bypass MFA or trust unverified assertions.

For an implemented flow, test wrong issuer/audience, bad or missing required signature, expired/replayed assertion or code, mismatched callback state/nonce, foreign-school mapping, duplicate email, removed membership and provider failure. Record protocol/library versions and actual results. The shared acceptance table adds the relevant SSO scenarios; passing a generic session test is insufficient.

Technical guidance: [OWASP OAuth2](https://cheatsheetseries.owasp.org/cheatsheets/OAuth2_Cheat_Sheet.html), [OWASP SAML Security](https://cheatsheetseries.owasp.org/cheatsheets/SAML_Security_Cheat_Sheet.html).

Targeted additions (DPO role, RAG and SSO guidance) reviewed 5 November 2026. The original source-check date above is historical; this edition does not claim a new full legal audit. Consult the source register for checked and unverified claims.

© 2026 Luděk Sušický. [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Revised edition of version 1.1, based on the original October 2026 guide. Preserve author, license and modification notices.
