from pydantic import BaseModel
from typing import Dict


class PredictionRequest(BaseModel):
    GrLivArea: float
    GarageCars: int
    TotalBsmtSF: float
    YearBuilt: int
    OverallQual: int
    GrLivArea_Qual: float
    Is_Modern: int
    Is_Luxury: int
    AvgPriceByNbhd: float
    SocioEconomicLevel: int
    # Variables one-hot
    Nbhd_Blueste: int
    Nbhd_Brdale: int
    Nbhd_Brkside: int
    Nbhd_Clearcr: int
    Nbhd_Collgcr: int
    Nbhd_Crawfor: int
    Nbhd_Edwards: int
    Nbhd_Gilbert: int
    Nbhd_Idotrr: int
    Nbhd_Meadowv: int
    Nbhd_Mitchel: int
    Nbhd_Names: int
    Nbhd_Noridge: int
    Nbhd_Npkvill: int
    Nbhd_Nridght: int
    Nbhd_Nwames: int
    Nbhd_Oldtown: int
    Nbhd_Sawyer: int
    Nbhd_Sawyerw: int
    Nbhd_Somerst: int
    Nbhd_Stonebr: int
    Nbhd_Swisu: int
    Nbhd_Timber: int
    Nbhd_Veenker: int


class PredictionResponse(BaseModel):
    price: float
