from datetime import datetime
from pydantic import BaseModel, validator
import json
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

data = {
    "Timestamp": "2019-01-01 01:00:00",
    "Temperature":13,
    "Dew_Point":7.0,
    "Surface_Albedo":0.22,
    "Pressure":1000,
    "Wind_Direction":126,
    "Wind_Speed":1,
    "Ozone":0.256, "Cloud_Type":6,
    "Solar_Zenith_Angle":160,
    "Precipitable_Water":1.4,"Relative_Humidity":67,
}

try:
    model = PredictionInput(**data)
    print(type(model))
    print(json.dumps(data))
except Exception as e:
    print(e.json())