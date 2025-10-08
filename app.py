import streamlit as st
import pandas as pd
import pickle
import numpy as np
st.title("Salary Prediction App ")

dbfile = open('salary.pickle', 'rb')
model = pickle.load(dbfile)

#input form

age = st.number_input("Enter your Age = ", min_value=18, max_value=100)
exp = st.number_input("Enter your Years of Experience = ", min_value=0, max_value=80)
gender = st.radio("Gender", [ "Male", "Female"])
education = st.selectbox("Education =", ["Bachelor's", "Master's", "PhD"])

if st.button("Predict"):
    if gender == "Male":
        gender = True
    else:
        gender = False
    if education == "Bachelor's":
        b=1; m=0; p=0
    elif education == "Master's":
        b=0; m=1; p=0   
    else:
        b=0; m=0; p=1   
        
    df = pd.DataFrame({
           'Age': [age],    
            'Years of Experience': [exp],
            'Male':[gender],
           "Bachelor's": [b],
           "Master's": [m],
           'PhD': [p]
           
           	       })
    st.dataframe(df)
    
    result = round(model.predict(df)[0][0],2)
    print(result)
    st.write(result)
    
    st.write("Success!")
    st.balloons()
    st.snow()
    