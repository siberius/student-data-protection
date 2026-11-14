# Changelog

## 1.2 (2026-11-14)

- Add non-local AI boundary guards: distinguish local/in-browser models (L0), 1:1 individual pseudonymisation domains (C1), and 1:N cohort analytics/exports (C2).
- Integrate k-anonymity (default k >= 5 distinct learners) and l-diversity (l >= 2) with complementary suppression (PTAC) and row shuffling (AEPD) to prevent singling out, linkability, and inference under EDPB Guidelines 02/2026 on Anonymisation.
- Add local pseudonymisation gateway requirements for 1:1 AI tutoring and feedback under EDPB Guidelines 01/2025 on Pseudonymisation, keeping lookup tables on school servers and redacting free-text PII.
- Add deterministic validation script `scripts/check_k_anonymity.py` without external dependencies to evaluate CSV/JSON exports without chat context bloat.
- Expand source registers with 8 authoritative sources: EDPB Guidelines 02/2026 (Anonymisation), EDPB Guidelines 01/2025 (Pseudonymisation), EDPB Opinion 28/2024 (AI Models), AEPD K-Anonymity Note & Guide, NIST SP 800-188, NIST AI 600-1, US DoE PTAC, and Czech MSMT/NPI AI guidance.
- Add behavioral test BE09 and acceptance tests AT37 (k-anonymity/l-diversity/suppression) and AT38 (local pseudonymisation gateway).
- Add continuous legal freshness checks (> 6 months) and an upstream GitHub feedback loop to report statutory amendments to <https://github.com/siberius/student-data-protection/issues> with user consent.
- Add Section 2.4 comparative legal overview and age threshold matrix covering Germany (BDSG/DSK), France (CNIL/ENT), Poland (UODO), and Ukraine (Mrija/Draft Law 8153).
- Synchronize English, Czech, and Spanish editions across standalone guides and modular native references.
- Add four full language editions with complete standalone guides, legal registers, evaluation suites, native skills, and localized documentation:
  - Polish edition (`pl`): `docs/ochrana-danych-uczniow.md`, `pl/SKILL.md`, `README.pl.md`, adapted to Polish UODO, Prawo oświatowe, and 16-year age threshold.
  - Ukrainian edition (`uk`): `docs/zakhyst-danykh-uchniv.md`, `uk/SKILL.md`, `README.uk.md`, adapted to Ukrainian Law No. 2297-VI, Draft Law 8153, Mrija ecosystem, and displaced pupils in the EU.
  - German edition (`de`): `docs/schuelerdatenschutz.md`, `de/SKILL.md`, `README.de.md`, adapted to BDSG § 16, 16 state school laws, and DSK rulings favoring local L0 execution.
  - French edition (`fr`): `docs/protection-donnees-eleves.md`, `fr/SKILL.md`, `README.fr.md`, adapted to Loi Informatique et Libertés (15-year threshold), CNIL doctrines, and ENT/GAR platforms.

## 1.1 revised edition (2026-11-05)

- Add a necessary-context intake before substantive work, reusing supplied facts and waiting on consequential missing answers.
- Add a conditional publication/document/output guide: explicit field projection, free-text/media review, import boundaries, provenance, artifact/index access, removal, safe updates and sanitised optional feedback.

- Merge upstream Czech ZŠ/SŠ scope clarification; keep the separately requested Spain adaptation.
- Offer a proportionate entry audit for existing applications, with prioritised findings, concrete remediation and explicit verification status.
- Retain release number 1.1 at the author's request; dates distinguish revisions.
- Add six practical data-handling modes, implementation paths, repair guidance and a solution card in a conditional reference. Keep one short core per language and document when a future skill split is justified.
- Separate design, implementation, audit and incident modes, with proportional scope and an explicit analysis-only boundary.
- Clarify controller responsibility and independent DPO advice; scope the strict reference profile without dropping necessary controls.
- Add English, Czech and Spain-localized Spanish native packages with conditional references while preserving the standalone guides.
- Add AI/RAG data lifecycle and SSO guidance plus acceptance scenarios AT31–AT36.
- Add a source-status register and planned skill-behaviour evaluation, separate from application test execution.
- Treat blocked link checks as unverified; keep EUR-Lex exclusions explicit.
- Adopt the upstream MIT license in all editions with the author's confirmation on 2026-11-05; preserve original authorship. Existing 1.1 source verification remains historical; new targeted review is not full legal certification.

## 1.1 original edition (2026-10-25)

- Original bilingual standalone security profile with 30 acceptance scenarios and source-check date 2026-10-22.
