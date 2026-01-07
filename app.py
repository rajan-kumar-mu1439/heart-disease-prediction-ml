import streamlit as st
import numpy as np
import joblib 

model = joblib.load("logistic_model.pkl")

st.title("Heart Disease Prediction Model")

st.divider()
st.write("Enter the details of the Patient:")

Age = st.number_input("Age (30 - 90):",min_value=30)
Sex =st.number_input("Gender (Male = 1, Female=0)",min_value=0,max_value=1)
Cp = st.number_input("Chest Pain Type (Normal = 0, medium = 1, high=2, Uncontrol=3)", min_value=0, max_value=3)
oldpeak = st.number_input("ST Depression(0 - 6)", min_value=0, max_value=6)
thal = st.number_input("Thalassemia (0 - 3): ",min_value=0, max_value=3)

st.divider()
x = [[Age, Sex, Cp, oldpeak, thal]]
predict_button = st.button("Click_Predict")
if predict_button:
    st.balloons()
    x_arr = np.array(x)
    prediction = model.predict(x_arr)[0]
    if prediction==1:
       st.error("High risk of heart disease.")
    else:
       st.success("Low risk of heart disease.") 




