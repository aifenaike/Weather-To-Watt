import numpy as np
import pandas as pd

input_feature_names = ['Dew Point', 'Surface Albedo', 'Pressure', 'Wind Direction',
       'Wind Speed', 'Ozone', 'Cloud Type', 'Solar Zenith Angle',
       'Precipitable Water', 'Relative Humidity', 'DayOfWeek', 'Month',
       'Season', 'Temperature_RollingMean_3day', 'Temp_Humidity_Interaction',
       'Hour_Sin', 'Hour_Cos']

contact={
        "name": "Ifenaike Alexander",
        "url": "https://github.com/aifenaike"
    }

description = """

Weather2Watt API helps you forecast solar power efficiency ☀️💡.

## Data Inputs

* **Timestamp**: Date and time of measurement.

* **Temperature**: Degrees Celsius (°C).

* **Dew Point**: Degrees Celsius (°C).

* **Surface Albedo**: Decimal fraction between 0 and 1.

* **Pressure**: Hectopascals (hPa).

* **Wind Direction**: Degrees (°).

* **Wind Speed**: Meters per second (m/s).

* **Ozone**: Dobson Units (DU).

* **Cloud Type**: Classification scheme (0-9) indicating cloud cover type.

* **Solar Zenith Angle**: Degrees (°).

* **Precipitable Water**: Millimeters (mm).

* **Relative Humidity**: Percentage (%).

## Users

You will be able to:

* **Pass weather-related data into the API to obtain a forecast**

## Example

{
    "Timestamp": "2019-01-01 01:00:00"**,
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

**Note**: _Correct the Timestamp to be able to properly use the API_
"""

def engineer_new_features(data):
    """
    Create new and modify existing features from user defined inputs
    """
    columns_to_remove = ['Temperature',"Hour"]

    # Time-Based Features
    data['Hour'] = data['Timestamp'].dt.hour
    data['DayOfWeek'] = data['Timestamp'].dt.dayofweek
    data['Month'] = data['Timestamp'].dt.month
    data['Season'] = data['Month'].apply(lambda x: (x%12 + 3)//3)

    data['Temperature_RollingMean_3day']  = data["Temperature"]

    # Interaction Terms
    data['Temp_Humidity_Interaction'] = data['Temperature'] * data['Relative_Humidity']

    # Trigonometric Features for Cyclical Nature (hour of the day)
    data['Hour_Sin'] = np.sin(data['Hour']*(2.*np.pi/24))
    data['Hour_Cos'] = np.cos(data['Hour']*(2.*np.pi/24))

    data.set_index('Timestamp', inplace=True)
    data.sort_index(inplace=True)

    data_ = data.drop(columns_to_remove,axis=1)

    return data_


def floor_predictions(predictions):
    return [max(0, pred) for pred in predictions]
    
