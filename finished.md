# Záznam dokončených změn (finished.md)

## 2026-11-14 | v1.2.0 / 29958e9

- Výsledek: Vydání verze 1.2.0 skillu student-data-protection v 7 jazykových mutacích (EN, CS, ES, PL, UK, DE, FR), včetně specializovaných registrů právních norem, skriptu k-anonymity (scripts/check_k_anonymity.py) a samostatných distribučních balíčků.
- Katalogy a distribuce:
  - skills.sh: Plná registrace všech 7 variant (student-data-protection, ochrana-dat-zaku, schuelerdatenschutz, proteccion-datos-alumnado, protection-donnees-eleves, ochrana-danych-uczniow, zakhyst-danykh-uchniv), všechny ověřeny s kódem HTTP 200.
  - GitHub metadata: Nastaveny klíčové topics (agent-skills, skills, ai-skills, claude-skills, edtech, data-protection, gdpr, ai-act, security, privacy) pro automatické indexování katalogů (Skills Directory, SkillsMP).
  - VoltAgent: Prověřena pravidla; podle správy portfolia (SKILLS-ROUTING.md) vyžaduje VoltAgent doloženou komunitní adopci, proto se nové skilly nenavrhují předčasně.
- Ověření: Python testy referencí (build_skill_refs.py --check) prošly s 0 chybami, textový linter (tools/check_text.py) prošel bez závad.

