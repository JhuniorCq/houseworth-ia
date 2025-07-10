import pandas as pd
import numpy as np

def predict_price(model, expected_columns, features: dict):
    try:
        df = pd.DataFrame([features])
        # Reordenar las columnas del DataFrame
        df = df[expected_columns]
        prediction = model.predict(df)[0]
        return round(prediction, 2)
    except Exception as e:
        raise RuntimeError(f"Error al realizar la predicción: {e}")
