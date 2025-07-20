import pandas as pd
import random

# 🧠 Створюємо список можливих полів
titles = [
    "API для оплати", "Рефакторинг модулю звітів",
    "Імпорт даних", "UI для дашборда", "Тестування OAuth",
    "Налаштування CI/CD", "Виправити баг з логуванням",
    "Оптимізувати кешування", "Інтеграція з Slack"
]
assignees = ["Olena","Andrii","Kateryna","Dmytro","Sergiy"]
rows = []

# 🧠 Генеруємо 20 рядків
for i in range(1, 21):
    title = random.choice(titles)
    desc = f"{title} — детальний опис задачі #{i}"
    sp = random.choice([1,2,3,5,8,13])
    at = sp * random.uniform(1.5, 3.0)  # actual_time в годинах
    assignee = random.choice(assignees)
    rows.append({
        "task_id": i,
        "title": title,
        "description": desc,
        "story_points": sp,
        "assignee": assignee,
        "actual_time": round(at,1)
    })

# 🧠 Перетворюємо в DataFrame і зберігаємо в CSV
df = pd.DataFrame(rows)
df.to_csv("data/sample_tasks.csv", index=False)
print("data/sample_tasks.csv згенеровано!")
