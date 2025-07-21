# src/train_model.py

# → Імпортуємо потрібні бібліотеки
import pandas as pd                          # → для роботи з табличними даними (DataFrame)
from sklearn.model_selection import train_test_split  # → для поділу даних на train/test
from sklearn.linear_model import LinearRegression      # → модель лінійної регресії
from sklearn.metrics import mean_absolute_error, r2_score  # → метрики для оцінки якості
import joblib                                 # → для серіалізації (збереження) моделі

# → Крок 1: Завантажуємо дані
df = pd.read_csv("data/sample_tasks.csv")    # → читаємо CSV із папки data/
# → df зараз — pandas DataFrame із колонками: task_id, title, description, story_points, assignee, actual_time

# → Крок 2: Попередня обробка
df = df.dropna(subset=["story_points", "actual_time"])
# → видаляємо рядки, де відсутні story_points або actual_time

# → Крок 3: Формуємо матрицю ознак X та вектор цілі y
# → В якості ознак візьмемо лише числові story_points (можна додавати нові фічі пізніше)
X = df[["story_points"]]                    # → DataFrame з однією колонкою
y = df["actual_time"]                       # → Series з тим, що потрібно прогнозувати

# → Крок 4: Розбиваємо дані на тренувальний та тестовий сет
X_train, X_test, y_train, y_test = train_test_split(
    X,               # → усі дані для X
    y,               # → усі дані для y
    test_size=0.2,   # → 20% даних піде в X_test та y_test
    random_state=42  # → фіксуємо сид для відтворюваності поділу
)

# → Крок 5: Створюємо та тренуємо модель
model = LinearRegression()   # → ініціалізуємо лінійну регресію
model.fit(X_train, y_train)  # → навчаємо модель на тренувальних даних

# → Крок 6: Оцінюємо модель
y_pred = model.predict(X_test)  # → робимо прогнози на тестовому сеті
mae = mean_absolute_error(y_test, y_pred)  # → середня абсолютна помилка
r2 = r2_score(y_test, y_pred)             # → коефіцієнт детермінації

print(f"MAE: {mae:.2f} годин")   # → виводимо MAE з округленням до 2 знаків
print(f"R^2: {r2:.2f}")          # → виводимо R^2 з округленням

# → Крок 7: Зберігаємо модель у файл
joblib.dump(model, "model.pkl")  # → серіалізуємо об’єкт model у файл model.pkl
print("Модель збережена як model.pkl")
