import streamlit as st
from model import predict_yield

st.set_page_config(page_title="Crop Yield Prediction")

st.title(" Crop Yield Prediction")


crop = st.selectbox("Crop", ["Wheat", "Rice", "Maize"])

temp = st.number_input("Temperature (C)", value=25.0)
rain = st.number_input("Rainfall (mm)", value=120.0)
humidity = st.number_input("Humidity (%)", value=65.0)
sunlight = st.number_input("Sunlight (hours)", value=8.0)
ph = st.number_input("Soil pH", value=6.5)
nitrogen = st.number_input("Soil Nitrogen (%)", value=0.35)
phosphorus = st.number_input("Soil Phosphorus (ppm)", value=18.0)
potassium = st.number_input("Soil Potassium (ppm)", value=140.0)
altitude = st.number_input("Altitude (m)", value=300.0)
wind = st.number_input("Wind Speed (m/s)", value=2.1)


if st.button("Predict Yield"):
    input_data = {
        'Crop': crop,
        'Temperature (C)': temp,
        'Rainfall (mm)': rain,
        'Humidity (%)': humidity,
        'Sunlight (hours)': sunlight,
        'Soil pH': ph,
        'Soil Nitrogen (%)': nitrogen,
        'Soil Phosphorus (ppm)': phosphorus,
        'Soil Potassium (ppm)': potassium,
        'Altitude (m)': altitude,
        'Wind Speed (m/s)': wind
    }

    yield_value, category = predict_yield(input_data)

    st.success(f" Predicted Yield: {yield_value:.2f} tons/ha")
    st.info(f" Yield Category: {category}")