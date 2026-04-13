import streamlit as st
import sys
import os

# Fix import path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.predict import predict_crop

st.set_page_config(page_title="Crop Recommendation", layout="centered")

st.title("🌱 Crop Recommendation System")
st.write("Smart Farming using Machine Learning 🚀")

st.subheader("Enter Soil & Weather Details")

# Inputs
N = st.number_input("Nitrogen (N)", min_value=0.0)
P = st.number_input("Phosphorus (P)", min_value=0.0)
K = st.number_input("Potassium (K)", min_value=0.0)
temp = st.number_input("Temperature (°C)")
humidity = st.number_input("Humidity (%)")
ph = st.number_input("pH Level")
rainfall = st.number_input("Rainfall (mm)")

if st.button("Predict Crop"):
    result = predict_crop(N, P, K, temp, humidity, ph, rainfall)

    st.success(f"🌾 Recommended Crop: {result}")

    # Extra UI
    st.info("✅ Based on soil and weather conditions")
    st.balloons()