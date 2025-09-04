import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Medical Insurance Predictor", page_icon="💸")
st.title("💸 Medical Insurance Cost Predictor")

@st.cache_resource
def load_model():
    return joblib.load("model_pipeline.joblib")

pipe = load_model()

col1, col2 = st.columns(2)

with col1:
    age = st.slider("Age", 18, 64, 30)
    bmi = st.number_input("BMI", 12.0, 60.0, 27.0, step=0.1)
    children = st.slider("Children", 0, 5, 0)

with col2:
    sex = st.selectbox("Sex", ["male", "female"])
    smoker = st.selectbox("Smoker", ["no", "yes"])
    region = st.selectbox("Region", ["northeast", "northwest", "southeast", "southwest"])

if st.button("Predict"):
    X = pd.DataFrame({
        "age": [age],
        "bmi": [bmi],
        "children": [children],
        "sex": [sex],
        "smoker": [smoker],
        "region": [region]
    })
    pred = pipe.predict(X)[0]
    st.success(f"Estimated charges: ${pred:,.2f}")
