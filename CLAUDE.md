# Инструкции для Claude

## Рабочий процесс с git

Платформа Claude Code on the Web принудительно создаёт feature-ветку
`claude/<name>-<id>` для каждой сессии и требует развития только в ней.

**После завершения каждой задачи делай fast-forward в `master` и пушь:**

```bash
git checkout master
git merge --ff-only <feature-branch>
git push origin master
git checkout <feature-branch>   # вернуться в feature-ветку, как требует платформа
```

Это нужно делать в самом конце задачи, после того как все коммиты в feature-ветку
запушены. Если fast-forward невозможен (master ушёл вперёд) — сообщи и спроси
пользователя, как поступить.

## Запуск проекта

Это консольный тренажёр устного счёта по методу Трахтенберга на Python 3.
Запуск: `python3 berg.py`.

Артефакты времени выполнения (`log.csv`, `records.json`) игнорируются git'ом
через `.gitignore` и не должны коммититься.
