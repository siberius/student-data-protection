# Захист персональних даних учнів у шкільних застосунках

[![Skills.sh](https://img.shields.io/badge/skills.sh-Install-blue)](https://skills.sh/siberius/student-data-protection)

Профіль безпеки та скіл асистента для освітніх застосунків (Україна та ЄС).

> Версія: 1.2 · Відповідність: GDPR (ЄС 2016/679), Регламент про AI (AI Act, ЄС 2024/1689), Закон України «Про захист персональних даних» та нормативні акти МОН.

## Встановлення та швидкий старт

Встановіть необхідну версію скіла у свого AI-асистента (Claude Code, Cursor, Codex, Antigravity, OpenCode, Cline тощо) за допомогою CLI зі [skills.sh](https://skills.sh):

```bash
# Встановлення української версії (Україна / ЄС)
npx skills add siberius/student-data-protection --skill zakhyst-danykh-uchniv --full-depth -g -a codex

# Перегляд усіх 7 доступних мовних версій
npx skills add siberius/student-data-protection --full-depth --list
```

Для одноразового тестування скіла без постійного встановлення:

```bash
npx skills use siberius/student-data-protection --skill zakhyst-danykh-uchniv --full-depth --agent codex
```

## Огляд документації

- **Самостійний посібник українською мовою:** [docs/zakhyst-danykh-uchniv.md](docs/zakhyst-danykh-uchniv.md)
- **Реєстр правових та технічних джерел:** [docs/reiestr-dzherel.md](docs/reiestr-dzherel.md)
- **Сценарії оцінювання поведінки скіла:** [docs/otsiniuvannia-navychky.md](docs/otsiniuvannia-navychky.md)
- **Модуль нативного скіла (UA):** [uk/SKILL.md](uk/SKILL.md)

## Основні засади профілю

1. **Відповідальність керівника закладу освіти:** Запуск будь-якого цифрового інструменту з персональними даними учнів вимагає рішення директора закладу після консультації з DPO.
2. **Обов'язковий договір обробки даних (DPA):** Заборонено передавати дані учнів хмарним сервісам або AI-провайдерам без офіційного договору.
3. **Рівні інтеграції AI (L0 / C1 / C2):** Пріоритет локальних моделей (L0) та сувора анонімізація перед хмарою C1.
4. **k-анонімність (k >= 5) та l-різноманітність (l >= 2):** Обов'язкова математична валідація звітів та наборів даних перед обробкою моделями штучного інтелекту.
5. **Актуальність законодавства:** Автоматичний моніторинг змін у нормативній базі з можливістю відкриття запиту на оновлення (GitHub Issue).

### Автор

**Luděk Sušický** - біолог, викладач інформатичних дисциплін у середній школі та університеті

- E-mail: [ludek.susicky@gmail.com](mailto:ludek.susicky@gmail.com)
- X: [@ludeksusicky](https://x.com/ludeksusicky)
- LinkedIn: [Luděk Sušický](https://www.linkedin.com/in/ludek-susicky/)
- GitHub: [@siberius](https://github.com/siberius) - інші освітні проєкти та відкриті застосунки

### Ліцензія

Цей проєкт поширюється на умовах ліцензії MIT. Деталі дивіться у файлі [LICENSE](LICENSE).
