import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Set page configuration
st.set_page_config(page_title="CLTV Predictor", layout="centered")

# Load model components
model = joblib.load("model_artifacts/model.pkl") 
scaler = joblib.load("model_artifacts/scaler.pkl")
feature_columns = joblib.load("model_artifacts/feature_columns.pkl")

# Extract supported countries from feature columns
country_dummies = [col.replace('Country_', '') for col in feature_columns if col.startswith('Country_')]

# UI
st.title("🛍️ Customer Lifetime Value (CLTV) Predictor")
st.subheader("Enter Customer Details")

recency = st.number_input("🕒 Recency (days since last purchase)", min_value=0.0, step=1.0)
frequency = st.number_input("🔁 Frequency (number of purchases)", min_value=0.0, step=1.0)
country = st.selectbox("🌍 Country", options=country_dummies)

# Create input dictionary
input_data = {
    'Recency': recency,
    'Frequency': frequency,
    f'Country_{country}': 1
}

# Convert to full feature DataFrame
features_df = pd.DataFrame([input_data])

# Ensure all columns are present and in correct order
for col in feature_columns:
    if col not in features_df.columns:
        features_df[col] = 0  #

features_df = features_df[feature_columns]

# Scale features
scaled_input = scaler.transform(features_df)


# Prediction
if st.button("🚀 Predict CLTV"):
    prediction = model.predict(scaled_input)[0]
    usd_to_inr = 83.10  
    inr_prediction = prediction * usd_to_inr
    st.success(f"💰 Predicted Monetary Value: **${inr_prediction:.2f} -> (~₹{inr_prediction:,.2f})**")

    st.markdown("---")
    st.markdown("📊 *Model trained on historical RFM data. Prediction is an estimate of customer's value.*")
