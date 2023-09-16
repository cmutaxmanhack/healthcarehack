import streamlit as st
import PLK as image

st.header('***My Profile***')
image = Image.open('profilepicmichelle.jfif')
    st.image(image, width= None, use_column_width=True)
