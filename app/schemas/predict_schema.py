from pydantic import BaseModel

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
    Nbhd_BrDale: int
    Nbhd_BrkSide: int
    Nbhd_ClearCr: int
    Nbhd_CollgCr: int
    Nbhd_Crawfor: int
    Nbhd_Edwards: int
    Nbhd_Gilbert: int
    Nbhd_IDOTRR: int
    Nbhd_MeadowV: int
    Nbhd_Mitchel: int
    Nbhd_NAmes: int
    Nbhd_NoRidge: int
    Nbhd_NPkVill: int
    Nbhd_NridgHt: int
    Nbhd_NWAmes: int
    Nbhd_OldTown: int
    Nbhd_SWISU: int
    Nbhd_Sawyer: int
    Nbhd_SawyerW: int
    Nbhd_Somerst: int
    Nbhd_StoneBr: int
    Nbhd_Timber: int
    Nbhd_Veenker: int


class PredictionResponse(BaseModel):
    price: float
