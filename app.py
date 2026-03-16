import streamlit as st
import pandas as pd
import joblib

# Load the engine DNA
@st.cache_resource
def load_model():
    model = joblib.load("models/gradient_boosting_model.joblib")
    scaler = joblib.load("models/scaler.joblib")
    return model, scaler

loaded_gb_model, scaler = load_model()

st.title("Predictive Maintenance")
st.markdown("Monitor the engine failures before they happen.")

# Telemetry Sliders
engine_rpm = st.slider("Engine RPM", 0, 3000, 1000)
lub_oil_pressure = st.slider("Lub Oil Pressure", 0.0, 10.0, 3.0)
fuel_pressure = st.slider("Fuel Pressure", 0.0, 25.0, 6.0)
coolant_pressure = st.slider("Coolant Pressure", 0.0, 10.0, 2.5)
lub_oil_temp = st.slider("Lub Oil Temp", 50.0, 150.0, 75.0)
coolant_temp = st.slider("Coolant Temp", 50.0, 200.0, 80.0)

if st.button("Predict Engine Condition"):
    input_data = pd.DataFrame([[engine_rpm, lub_oil_pressure, fuel_pressure, coolant_pressure, lub_oil_temp, coolant_temp]], 
                              columns=['Engine rpm', 'Lub oil pressure', 'Fuel pressure', 'Coolant pressure', 'lub oil temp', 'Coolant temp'])
    
    scaled_data = scaler.transform(input_data)
    prediction = loaded_gb_model.predict(scaled_data)
    
    if prediction[0] == 1:
        st.error("Engine Failure Predicted - Maintenance Required!")
    else:
        st.success("Engine is Operating Normally")
