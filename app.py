import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

st.title("❤️ Heart Disease Prediction App")

st.write("Enter patient data below:")

# Input fields
age = st.number_input("Age", min_value=1, max_value=120, value=40)
sex = st.selectbox("Sex (1=Male, 0=Female)", [1, 0])
cp = st.selectbox("Chest Pain Type (0-3)", [0,1,2,3])
trestbps = st.number_input("Resting Blood Pressure", min_value=80, max_value=200, value=120)
chol = st.number_input("Serum Cholesterol (mg/dl)", min_value=100, max_value=600, value=200)
fbs = st.selectbox("Fasting Blood Sugar > 120 (1=True, 0=False)", [1,0])
restecg = st.selectbox("Resting ECG (0,1,2)", [0,1,2])
thalach = st.number_input("Max Heart Rate", min_value=50, max_value=250, value=150)
exang = st.selectbox("Exercise Induced Angina (1=Yes, 0=No)", [1,0])
oldpeak = st.number_input("ST Depression", min_value=0.0, max_value=10.0, value=1.0)
slope = st.selectbox("Slope (0-2)", [0,1,2])
ca = st.selectbox("Number of vessels (0-3)", [0,1,2,3])
thal = st.selectbox("Thal (1=normal,2=fixed defect,3=reversible defect)", [1,2,3])

# Convert input into dataframe
data = pd.DataFrame({
    'age':[age],
    'sex':[sex],
    'cp':[cp],
    'trestbps':[trestbps],
    'chol':[chol],
    'fbs':[fbs],
    'restecg':[restecg],
    'thalach':[thalach],
    'exang':[exang],
    'oldpeak':[oldpeak],
    'slope':[slope],
    'ca':[ca],
    'thal':[thal]
})

st.write("### Model Input Data:")
st.write(data)

# Prediction
if st.button("🔍 Predict"):
    result = model.predict(data)[0]
    
    if result == 1:
        st.error("⚠️ High possibility of Heart Disease!")
    else:
        st.success("👍 Heart condition looks Normal.")

