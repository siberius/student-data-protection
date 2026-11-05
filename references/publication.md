# 18. Publication, documents and derived outputs [D/O]

<!-- Generated reference; edit the maintained standalone guide. -->

Source sections: 18.

## 18. Publication, documents and derived outputs [D/O]

### 18.1 Trace the actual publication boundary

Load this module for portals, portfolios, public showcases, generated sites, document imports or exports. Compare current code, build commands and deployment configuration with the documentation; an app described as local may now publish to a host. Do not run a build or deploy merely to inspect it: either can copy real records, send data or create a public artifact.

Trace the relevant path from source through transformations to recipients: records, attachments, OCR, working notes, generated HTML/JSON, search indexes, previews, PDFs, screenshots, packages, hosting/CDN caches and previous releases. Include build logs and CI artifacts if they can contain personal data. An artifact is a copy even when no database is deployed. Record audience per output: private working material, authenticated school access or public publication. A teacher's access to a source does not by itself authorise publishing it.

### 18.2 Build an explicit publication projection

Keep working records separate from publishable fields and files. Construct public configuration and exported records from an allowlist for the stated audience and purpose; excluding only a password field can expose a future internal field. Unknown fields remain excluded until assessed. Keep raw sources outside the public directory. Preview the selected projection without uploading real records to an external preview service.

For each published item, retain a minimal internal decision record: source/version, selected fields, audience, responsible decision, applicable processing basis or other justification, and review/removal trigger. Do not treat a UI publish toggle or the creator's approval as proof that all data subjects' rights and legal conditions have been resolved. Do not force a new manual approval for every routine change already covered by a valid decision; recheck material changes in content, audience, purpose or recipients. Do not export the approval register itself with sensitive excerpts.

### 18.3 Review free text, media and imports

Review comments, learner work, OCR, filenames, URLs, image metadata and embedded content as well as structured fields. A document can mention siblings, guardians, classmates or staff; determine whose information is necessary. Redact irreversibly in the distributed copy and check that hidden text, layers, OCR and original attachments do not retain the removed content. Preserve a restricted original only where justified. Review accessibility text and captions for the same exposure.

Keyword detectors, approximate dates and AI classifiers can flag items for review; silence is not proof of safety and a flag is not a diagnosis. Do not import a genealogy rule such as “name and birth year are enough” as a school-wide publication policy. Limit sensitive excerpts in checker output, tickets and logs.

Treat imported CSV, JSON, GEDCOM, documents and archives as untrusted data. Use suitable parsers and validate schema, types, size/count limits, encoding and record references. Where archives exist, constrain expanded size and paths. Avoid executing a supplied Python/JavaScript file as a data import. Trusted project code has a different boundary; do not replace it without evidence. Separate import preview, correction and authorised commitment to official records. These controls complement [OWASP File Upload](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html).

### 18.4 Preserve provenance without creating learner labels

Where an imported or AI-extracted value can affect a person, record its source, relevant version/date, verification state and responsible correction. Distinguish a submitted claim, a checked record, a transcription, an interpretation and an unresolved conflict. A second copied source may share the same origin and is not independent corroboration. An AI suggestion or a plausible match must not silently merge people or become an official grade, diagnosis or durable ability label. Retain necessary correction history with its own access and retention rules.

### 18.5 Check access and external recipients

Protect HTML, images, raw files, JSON and search-index shards consistently, including direct URLs, alternate origins and deployment previews where present. Hiding a link, adding noindex or searching only in the browser does not restrict access. Identify whether hosting, maps, fonts, analytics and support receive requests or data. A remote map tile request can reveal visitor metadata and viewed areas; inspect actual behaviour before claiming a name or record was sent.

A shared answer hashed in a cookie remains a shared bearer credential. Hashing it does not establish an individual identity or enable individual revocation. Match authentication, session expiry and revocation to the data; use the identity module for personal records. See [OWASP Session Management](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html). Do not automatically require accounts for a genuinely public, non-personal activity.

### 18.6 Inspect the release and removal path

Recommend a release check appropriate to risk: compare the actual candidate artifact with the publication projection, inspect added/changed/removed personal fields and files, and identify sensitive findings or unreviewed outputs. A checker should report its coverage and distinguish a warning from a release-stopping condition adopted for this project. A successful build is not this check. For personal publication, unresolved permission or a known unintended disclosure stops that publication; unaffected authorised work can continue.

Plan removal from active HTML, public asset folders, indexes, exports and caches. A copy loop that only adds files can retain withdrawn content. Use a manifest or a clean staging build; prune only confirmed obsolete generated files, never source records or unrelated user files. Check that restore or the next build does not republish withdrawn material. Previous release URLs, host retention and downloaded copies have explicit limits; do not promise remote deletion without evidence. A rollback restores an authorised release, not necessarily one with still-valid privacy decisions.

Before a template/skill update, compare versions and local changes, back up affected files and plan recovery. Preserve records and deployment-specific access controls. Updating a template does not authorise installation, spending or publication. Record observed post-update behaviour separately from planned checks.

### 18.7 Handoff and sanitised feedback

Add to the solution card only the relevant output inventory, publication projection, review status, removal limits and responsible next action. Keep the report actionable and identify uninspected artifacts. Use synthetic distinctive markers when proposing checks of index leakage or deletion; do not place real learner data in test evidence.

Reusable feedback for a skill maintainer contains tool/version, synthetic reproduction, expected versus observed behaviour and a general correction. Remove identifiers, credentials and indirect clues; do not attach production logs, family records, scans or school databases. Show the sanitised content before any separately authorised external submission. Feedback is optional and never sent automatically.

© 2026 Luděk Sušický. [MIT](https://opensource.org/license/mit). Revised edition of version 1.1, based on the original October 2026 guide; preserve attribution, license and change notices. External sources retain their own rights.

## License / Licence

MIT License

Copyright (c) 2026 Luděk Sušický

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

© 2026 Luděk Sušický. [MIT](https://opensource.org/license/mit). Revised edition of version 1.1, based on the original October 2026 guide. Preserve author, license and modification notices.
