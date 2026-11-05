# Přispívání / Contributing

**Česky:** opravy a doplnění jsou vítané. Otevřete issue nebo pull request.
U právních změn uveďte zdroj a datum ověření. Nevkládejte skutečné údaje žáků,
klíče ani konfiguraci školy.

**English:** corrections and additions are welcome. Open an issue or a pull
request. For legal changes, include the source and the date you verified it.
Never include real student data, keys, or school configuration.

## Kontrola před odesláním / Before you submit

```bash
python3 tools/check_text.py
```

Kontrola hlásí dlouhé pomlčky, spojovací pomlčky, šablonové fráze a chybějící
relativní odkazy. Text pište jako pro člověka: konkrétní fakta, krátké věty,
žádné marketingové fráze. The checker flags em dashes, spaced dashes, template
phrases, and broken relative links.

## Nativní balíčky / Native bundles

Úplné návody v docs/ jsou udržované zdroje. Nativní jádra jsou SKILL.md, cs/SKILL.md a es/SKILL.md; references/ se odvozují z příslušného průvodce. V místním autorském checkoutu obnoví reference `python3 testing/build_skill_refs.py` a zkontroluje je `--check`. Vývojové nástroje v testing/ se nepublikují; hotové balíčky je nepotřebují. Veřejná kontrola výše zachytí chybějící nebo zastaralé bezpečnostní oddíly a licenční kopie. Při změně jádra zkontroluj i ostatní jazyky a zachovej omezení auditu na posouzení.

Complete docs/ guides are the maintained sources. Native cores use conditional references derived from them. Update all affected language editions, preserve attribution and distinguish source review, proposed scenarios, actual skill behaviour and application test execution. The public checker detects source/reference drift; it does not certify security or legal compliance. See the source registers for verification limits.
