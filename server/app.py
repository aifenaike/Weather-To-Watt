from fastapi import FastAPI, HTTPException, Form
from fastapi.responses import JSONResponse, RedirectResponse

from typing import Union
import joblib
import numpy as np
import pandas as pd
import uvicorn
from schema import PredictionInput
from utils import *


# Create an instance of the FastAPI class
app = FastAPI()

# Load the trained model
model = joblib.load('./model/catboost_model-v0.1.0.pkl')

#first-contact route endpoint
@app.get("/")
def main():
    return JSONResponse({
            "description": "Welcome to the Weather2Watt API! This API predicts solar power efficiency using metereological data"
        })

#Prediction endpoint
@app.post("/api/predict/", status_code=200)
def predict(data: PredictionInput):
    results ={}
    data = data.model_dump()
    converted_dict = {key: [value] for key, value in data.items()}
    features = pd.DataFrame.from_dict(converted_dict)
    features = engineer_new_features(features)
    features.columns = input_feature_names
    prediction = model.predict(features)

    # if not prediction:
    #     # the exception is raised, not returned - you will get a validation
    #     # error otherwise.
    #     raise HTTPException(
    #         status_code=404, detail="Input Data could not be processed for prediction. Verify that your input conforms to the standards."

    #     )
    
    results = floor_predictions(prediction[0])

    return {"status_code": 200,
        "Diffuse Horizontal Irradiance (DHI)": results[0],
        "Direct Normal Irradiance (DNI)": results[1],
        "Global Horizontal Irradiance (GHI)": results[2],
    }

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)

#uvicorn app:app --reload --port 8000 --host 0.0.0.0