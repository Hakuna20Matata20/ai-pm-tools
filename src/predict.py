# src/predict.py

# → Імпортуємо потрібні бібліотеки
import pandas as pd                # → для роботи з табличними даними
import joblib                      # → щоб завантажити збережену модель

# → Функція для завантаження моделі
def load_model(path="model.pkl"):
    """
    Завантажує ML-модель з файлу.
    path: шлях до файлу з моделлю
    """
    model = joblib.load(path)      # → joblib.load читає серіалізований об’єкт
    return model

# → Функція для підготовки даних до прогнозу
def prepare_input(data: dict):
    """
    Приймає словник з параметрами задачі, повертає DataFrame
    data: {
        "story_points": int
    }
    """
    # → Робимо DataFrame з одного рядка
    df = pd.DataFrame([data])
    # → df матиме колонку "story_points"
    return df

# → Функція для отримання прогнозу
def predict_time(model, input_df: pd.DataFrame):
    """
    Прогнозує actual_time (години) на основі input_df
    model: об’єкт навченої моделі
    input_df: DataFrame з колонкою "story_points"
    """
    prediction = model.predict(input_df)
    # → повертає масив з одним числом
    return float(prediction[0])      # → приводимо до float для простоти

# → Якщо цей файл запустили напряму (не імпорт)
if __name__ == "__main__":
    # → Приклад роботи
    # Створюємо "вхід" у вигляді словника
    sample = {"story_points": 5}
    model = load_model()             # → завантажуємо модель
    pred = predict_time(model, prepare_input(sample))
    print(f"Прогноз часу для {sample['story_points']} SP → {pred:.2f} годин")
