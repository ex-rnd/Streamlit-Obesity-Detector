# Load packages 
import pandas as pd
import tensorflow as tf
import keras
import streamlit as st
import numpy as np

# Load the model
model = keras.models.load_model('.\model\model.keras')

# Load the dataframe 
df = pd.read_csv('.\dataset\obesity_data.csv')

# Create the Pages 

# Container for the Title 
with st.container():
    
    # Columns: Image and Title
    image_col, title_col = st.columns([0.5, 2], vertical_alignment = 'center')
    
    with image_col:
        st.image('.\images\logo.png', width = 100)
        
    with title_col:
        st.write('# **:blue[OBESITY🫃🏻 DETECTOR🔍]**')
        
# About the Project 
with st.container():
    with st.expander('**:red[WHAT IS THIS ?]**', expanded=True):
        st.write('**:rainbow[OBESITY DETECTOR]** is a deep learning model that detects the Obesity level of a person with respect to age, gender, height, weight, bmi and physical activity level of the person.')
        
        
# Input Output Container
with st.container():
    
    # Creating Two Columns for input and output 
    input_col, output_col = st.columns([2, 1], vertical_alignment= 'top')
    
    with input_col:
        
     # Heading 
     st.write('### **:violet[ENTER FEATURES OF THE PERSON]**')
     
     # Creating Six Columns for Input Fields
     age_col, gender_col, height_col = st.columns(3)
     weight_col, bmi_col, pal_col = st.columns(3)
     
    with age_col:
        age = st.text_input('**AGE**', placeholder =f"{df['Age'].min()} to {df['Age'].max()}")
        if age:
            age = np.int64(age)
         
    with gender_col:
        gender = st.selectbox('**GENDER**', options=['Male', 'Female'])
        
        
    with height_col:
        min_height = np.round(df['Height'].min(), 2)  
        max_height = np.round(df['Height'].max(), 2)   
        height = st.text_input('**HEIGHT**', placeholder=f"{min_height} to {max_height}")
        
    if height:
        height = np.float64(height)     

    with weight_col:
        min_weight = np.round(df['Weight'].min(), 2)
        max_weight = np.round(df['Weight'].max(), 2)
        weight = st.text_input('**WEIGHT**', placeholder=f"{min_weight} to {max_weight}")

        if weight:
            weight = np.float64(weight)

    with bmi_col:
        # min_bmi = np.round((df['Weight']/df['Height']).min(), 2)
        # max_bmi = np.round((df['Weight']/df['Height']).max(), 2)
        min_bmi = np.round(df['BMI'].min(), 2)
        max_bmi = np.round(df['BMI'].max(), 2)
        bmi = st.text_input('**BMI**', placeholder=f"{min_bmi} to {max_bmi}")

        if bmi:
            bmi = np.float64(bmi)

    with pal_col:
        pal = st.selectbox('**ACTIVITY LEVEL**', options=[1,2,3,4])        
    
    with output_col:
        # heading
        st.write('### **:green[OBESE RESULT]**')
        result = st.empty()

        if age and height and weight and bmi:

            sample = {
                'Age': age,
                'BMI': bmi,
                'Gender': gender,
                'Height': height,
                'Weight': weight,
                'PhysicalActivityLevel': pal
                }

            raw_input = {
                key: keras.ops.convert_to_tensor([value]) for key, value in sample.items()
                }

            prediction = model.predict(raw_input)
            
            output = prediction[0].argmax()
            
            if output == 0:
                with result.container():
                    st.write('# 🙆🏻🤗✅')
                    st.info('**NORMAL WEIGHT ✅**')
            elif output == 1:
                with result.container():
                    st.write('# 🤦🏻😔👎🏻')
                    st.info('**UNDER WEIGHT 👎🏻**')
            elif output == 2:
                with result.container():
                    st.write('# 🙅🏻😲❌')
                    st.info('**OVER WEIGHT ❌**')
            else:
                with result.container():
                    st.write('# 🫄🏻🙄❎')
                    st.info('**OBESED ❎**')    
    
# Container for Socials 
    
with st.container():

    repo_col, linkedIn_col = st.columns([2, 3], vertical_alignment= 'top')

    # Repository Link
    with repo_col:
        st.link_button('**GITHUB REPOSITORY**', icon=':material/code_blocks:', url='https://github.com/madhavpani/Obesity_Detector', help='GITHUB REPOSITORY')

    # LinkedIn link
    with linkedIn_col:
        st.link_button('**CONNECT ON LINKEDIN**', icon=':material/connect_without_contact:', url='https://www.linkedin.com/in/madhavpani', help='LINKEDIN')
    









