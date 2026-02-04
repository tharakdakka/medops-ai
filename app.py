import streamlit as st
import pandas as pd
import joblib

st.title("🏥 MedOps AI: Inventory Predictor")
st.sidebar.header("Current Conditions")

# Create user input sliders
stock = st.sidebar.slider("Current Stock Level", 0, 1000, 150)
flu_rate = st.sidebar.slider("Local Flu Rate (%)", 0, 100, 5)

# Load your AI model
try:
    model = joblib.load("med_inventory_model.pkl")
    if st.button("Predict Demand"):
        # This matches the 'brain' model we'll upload later
        prediction = model.predict([[stock, 0, flu_rate]]) 
        st.subheader(f"Predicted Demand: {int(prediction[0])} units")
except:
    st.warning("Please upload med_inventory_model.pkl to your GitHub repo.")
