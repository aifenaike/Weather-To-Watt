import numpy as np
import pandas as pd

input_feature_names = ['Dew Point', 'Surface Albedo', 'Pressure', 'Wind Direction',
       'Wind Speed', 'Ozone', 'Cloud Type', 'Solar Zenith Angle',
       'Precipitable Water', 'Relative Humidity', 'DayOfWeek', 'Month',
       'Season', 'Temperature_RollingMean_3day', 'Temp_Humidity_Interaction',
       'Hour_Sin', 'Hour_Cos']


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
    
