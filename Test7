import streamlit as st
from PIL import Image

# Title
st.header('***My Profile***')

# User Information
st.subheader('Personal Information')
name = st.text_input("Name:", "")
age = st.number_input("Age:", min_value=0, max_value=120, step=1)
sex = st.selectbox("Sex:", ["Male", "Female", "Other"])

# Physical Details
st.subheader('Physical Details')
height = st.number_input("Height (cm):", min_value=0.0, max_value=300.0, step=0.1)
weight = st.number_input("Weight (kg):", min_value=0.0, max_value=300.0, step=0.1)

# Health Information
st.subheader('Health Information')

# Medications
medications = st.text_area("Medications:", "None")

# Known Conditions
conditions = st.text_area("Known Conditions:", "None")

# When user is done, they can press the button to save their profile
if st.button("Save Profile"):
    st.success("Profile Saved Successfully")

# Here you can add code to save these details to a database, a file, or any other backend storage.
