from fastapi import FastAPI
from app.routes.predict import router

app = FastAPI(
    title="House Price Predictor API",
    description="API que predice el precio de una vivienda usando un modelo entrenado.",
    version="1.0.0"
)

app.include_router(router)
