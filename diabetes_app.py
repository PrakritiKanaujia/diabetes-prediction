import pickle
import streamlit as st
import time
import numpy as np

import warnings
warnings.filterwarnings("ignore")

#Load model
model_diabetes=pickle.load(open('model_diabetes.sav','rb'))

st.title('App For Diabetes Prediction')

#columns
col1,col2=st.columns(2)
with col1:
    Pregnancies=st.number_input("Enter number of Pregnancies",step=1,min_value=0)
with col2:
     Glucose = st.number_input('Enter the Glucose value',min_value=0.0)
with col1:
     BloodPressure = st.number_input('Enter the Blood Pressure value',min_value=0.0)
with col2 :
     SkinThickness = st.number_input('Enter the Skin Thickness value',min_value=0.0)

with col1 :
     Insulin = st.number_input('Enter the Insulin value',min_value=0.0)

with col2 :
     BMI = st.number_input('Enter the BMI value',min_value=0.0)

with col1 :
     DiabetesPedigreeFunction = st.number_input('Enter the Diabetes Pedigree Function value',min_value=0.0,step=0.001)

with col2 :
     Age = st.number_input('Enter the Age value',step=1,min_value=0)

#Prediction
Diagnosis=""
if st.button("Diabetes Prediction Test"):
    pred=model_diabetes.predict([[Pregnancies,Glucose,BloodPressure,
                                  SkinThickness,Insulin,BMI,
                                  DiabetesPedigreeFunction,Age]])
    if (pred[0]==1):
        Diagnosis= "The Patient has Diabetes"
        with st.spinner('Evaluating...'):
            time.sleep(5)
        st.error(Diagnosis)
    else:
        Diagnosis= "The Patient does not have Diabetes"
        with st.spinner('Evaluating...'):
            time.sleep(5)
        st.success(Diagnosis)

    
    
         
