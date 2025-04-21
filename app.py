import numpy as np
import streamlit as st
import pickle

model = pickle.load(open('SalaryPredictor.mdl','rb'))
st.title("Salary Predictor")
yExperience = np.array([[float(st.text_input("Enter Years of Experience: ","1"))]])

sal = model.predict(yExperience)

st.write(f'Hello, *World!* :sunglasses: . Predicted Salary for {yExperience} years of experience is $ {sal}')
