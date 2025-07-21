
import os
import sys

current_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(current_dir, ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

import gradio as gr
from src.predict import load_model, prepare_input, predict_time

import gradio as gr
from src.predict import load_model, prepare_input, predict_time

model = load_model("model.pkl")

def predict_interface(sp):
    """
    sp: story points (int від користувача)
    Повертає рядок з прогнозом
    """
    input_df = prepare_input({"story_points": sp})
    hours = predict_time(model, input_df)
    return f"Прогноз: {hours:.2f} годин"

iface = gr.Interface(
    fn=predict_interface,
    inputs=gr.Number(label="Story Points"),
    outputs=gr.Textbox(label="Time to Complete"),
    title="Time-to-Complete Predictor",
    description="Введіть оцінку в story points — отримайте прогноз часу виконання"
)

if __name__ == "__main__":
    iface.launch(server_name="0.0.0.0", server_port=8000, share=False)

