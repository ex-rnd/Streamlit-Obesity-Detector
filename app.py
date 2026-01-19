# Load packages 
import pandas as pd
import tensorflow as tf
import keras
import streamlit as st
import numpy as np

# Load the model
model = keras.models.load_model('./model/model.keras')

# Load the dataframe 
df = pd.read_csv('./dataset/obesity_data.csv')

# Create the Pages 

# Container for the Title 
with st.container():
    
    # Columns: Image and Title
    image_col, title_col = st.columns([0.5, 2], vertical_alignment = 'center')
    
    with image_col:
        st.image('./images/logo.png', width = 100)
        
    with title_col:
        st.write('# **:blue[OBESITY🫃🏻 DETECTOR🔍]**')
        
    
    
    
    
    










