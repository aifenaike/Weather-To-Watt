# Weather-To-Watt

Solar power generation is highly dependent on various meteorological factors. Understanding and predicting the efficiency of solar energy production under clear sky conditions (a state where solar irradiance is not hindered by clouds) is crucial for optimizing solar panel performance and energy grid management. 

This project aims to address this need by developing a robust predictive model that can accurately estimate solar energy production using a range of weather parameters. Accurate predictions are vital for energy planning, reducing wastage, and improving the reliability of solar power as a sustainable energy source.


### Objective
The primary objective of this project is to develop and validate a multi-label regression model capable of predicting key solar irradiance components: Diffuse Horizontal Irradiance (DHI), Direct Normal Irradiance (DNI), and Global Horizontal Irradiance (GHI). The model utilizes a comprehensive set of input parameters, including temperature, dew point, surface albedo, atmospheric pressure, wind conditions, solar zenith angle, and more, to provide precise and location-specific predictions.

### Model
In this project, I employed the CatBoost algorithm, a high-performance gradient boosting framework, due to its effectiveness in handling diverse and complex datasets. The model was trained on historical weather data and solar irradiance measurements, focusing on these inputs:
  - **Timestamp**: Date and time of measurement
  - **Temperature**: Degrees Celsius (°C)
  - **Dew Point**: Degrees Celsius (°C)
  - **Surface Albedo:** Decimal fraction between 0 and 1
  - **Pressure:** Hectopascals (hPa)
  - **Wind Direction:** Degrees (°)
  - **Wind Speed:** Meters per second (m/s)
  - **Ozone:** Dobson Units (DU)
  - **Cloud Type:** Classification scheme (0-9) indicating cloud cover type
  - **Solar Zenith Angle:** Degrees (°)
  - **Precipitable Water:** Millimeters (mm)
  - **Relative Humidity:** Percentage (%)
    
The choice of a multi-label regression approach allows for simultaneous predictions of DHI, DNI, and GHI, offering a comprehensive view of solar irradiance under clear sky conditions.
