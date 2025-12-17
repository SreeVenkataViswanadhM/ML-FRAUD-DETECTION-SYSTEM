import streamlit as st
import numpy as np
import pandas as pd
import joblib

# Load the pre-trained model
@st.cache_resource
def load_model():
    model = joblib.load('model.pkl')
    return model

st.title("🚨 Fraud Detection System")

# Load model
model = load_model()

# Input fields (simplified, assuming key features)
amount = st.number_input("Transaction Amount", value=0.0)
time = st.number_input("Transaction Time", value=0.0)
# Add more inputs as needed, but for demo, using only amount and time

if st.button("Check Fraud"):
    # Assuming the model expects all features, but for demo, create a dummy array
    # In real scenario, collect all features
    input_data = np.array([[time, amount] + [0] * (len(model.feature_names_in_) - 2)])  # Pad with zeros
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("⚠️ Fraudulent Transaction")
    else:
        st.success("✅ Legitimate Transaction")
