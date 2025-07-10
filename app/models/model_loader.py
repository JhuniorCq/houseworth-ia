import joblib
import os

MODEL_PATH = os.path.join(os.path.dirname(__file__), '../../modelo_final.pkl')

def load_model():
    try:
        data = joblib.load(MODEL_PATH)
        model = data["model"]
        columns = data["columns"]
        return model, columns
    except Exception as e:
        raise RuntimeError(f"No se pudo cargar el modelo: {e}")
