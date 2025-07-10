from fastapi import APIRouter, HTTPException
from app.schemas.predict_schema import PredictionRequest, PredictionResponse
from app.utils.prediction import predict_price
from app.models.model_loader import load_model

router = APIRouter()
model, expected_columns = load_model()  # 👈 carga también las columnas

@router.post("/predict", response_model=PredictionResponse)
async def predict(data: PredictionRequest):
    try:
        features = data.dict()
        price = predict_price(model, expected_columns, features)
        return { "price": price }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
