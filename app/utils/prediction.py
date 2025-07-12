from app.utils.constants import CAMPO_CORRECCION
import pandas as pd

def predict_price(model, expected_columns, features: dict):
    try:
        for old_key, new_key in CAMPO_CORRECCION.items():
            if old_key in features:
                features[new_key] = features.pop(old_key)

        df = pd.DataFrame([features])
        df = df[expected_columns]
        prediction = model.predict(df)[0]
        return round(prediction, 2)
    except Exception as e:
        raise RuntimeError(f"Error al realizar la predicción: {e}")
