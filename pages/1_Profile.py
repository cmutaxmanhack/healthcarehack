import streamlit as st
from PIL import Image

st.header('***My Profile***')
image = Image.open('profilepicmichelle.jfif')
st.image(image, width= None, use_column_width=True)
