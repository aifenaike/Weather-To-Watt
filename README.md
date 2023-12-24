# Weather-To-Watt (Solar Efficiency Prediction Microservice)

## Project Overview
Solar power generation is highly dependent on various meteorological factors. Understanding and predicting the efficiency of solar energy production under clear sky conditions (a state where solar irradiance is not hindered by clouds) is crucial for optimizing solar panel performance and energy grid management. 

This project focuses on creating a microservice adept at predicting solar energy efficiency. It harnesses cutting-edge machine learning techniques, along with extensive weather data, to forecast the performance under clear sky conditions accurately.  The accuracy of these predictions is key to streamlining energy planning, minimizing resource wastage, and bolstering the dependability of solar power as a renewable energy option. The architecture of this system, encompassing FastAPI for the API implementation and Celery for asynchronous task management, ensures both high efficiency and responsiveness, aligning with the demands of modern, sustainable energy solutions.

### Objective

The primary objective of this project is to develop and validate a multi-label regression model capable of predicting key solar irradiance components: Diffuse Horizontal Irradiance (DHI), Direct Normal Irradiance (DNI), and Global Horizontal Irradiance (GHI). The model utilizes a comprehensive set of input parameters, including temperature, dew point, surface albedo, atmospheric pressure, wind conditions, solar zenith angle, and more, to provide precise and location-specific predictions via a microservice.

### Model Development

I adopted a **multi-label regression** strategy to enable simultaneous predictions of Diffuse Horizontal Irradiance (DHI), Direct Normal Irradiance (DNI), and Global Horizontal Irradiance (GHI). This approach allows for a detailed analysis of solar irradiance in clear sky conditions. **Central to this microservice is the predictive model, for which I chose the CatBoost algorithm. Renowned for its high performance as a gradient boosting framework, CatBoost excels in managing datasets that are both diverse and complex.**

To ensure the model's accuracy and reliability, it was trained on a historical dataset encompassing both weather data and solar irradiance measurements. This training process emphasized the following key inputs:
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


## Features

- **Accurate Predictions**: Multi-label regression model using CatBoost to predict Diffuse Horizontal Irradiance (DHI), Direct Normal Irradiance (DNI), and Global Horizontal Irradiance (GHI).
- **Asynchronous Processing**: Leveraging Celery for handling heavy computational tasks without blocking the main API server.
- **Scalable Architecture**: Both FastAPI and Celery are containerized using Docker, allowing for easy scaling.
- **Comprehensive Inputs**: Utilizes various parameters like temperature, dew point, wind conditions, solar zenith angle, etc., for precise predictions.


## System Architecture

1. **FastAPI Server**: Handles incoming HTTP requests, validates them, and dispatches prediction tasks.
2. **Celery Worker**: Processes the predictive tasks asynchronously.
3. **Message Broker (RabbitMQ/Redis)**: Manages the task queue between FastAPI and Celery.
4. **Machine Learning Model**: Encapsulated in a Docker container, accessible by Celery workers.
5. **Database (Optional)**: Stores prediction results and request data.
