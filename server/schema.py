from pydantic import BaseModel, validator
from pydantic import BaseModel
from datetime import datetime    


# Input Data Validation
class PredictionInput(BaseModel):
    """Pydantic model for prediction input"""
    Timestamp: datetime
    Temperature: float
    Dew_Point: float
    Surface_Albedo: float
    Pressure: float
    Wind_Direction: int
    Wind_Speed: float
    Ozone: float
    Cloud_Type: int
    Solar_Zenith_Angle: float
    Precipitable_Water: float
    Relative_Humidity: float

    @validator("Timestamp", pre=True)
    def non_iso_date(cls, value: str) -> datetime:
        try:
            return datetime.strptime(value, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            raise ValueError(f"Date {value} is not a valid yyyy-mm-dd H:M:S format")