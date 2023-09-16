import streamlit as st
from PIL import Image

st.header('***My Profile***')

st.markdown ("Name")
st.markdown ("Age")
image = Image.open('profilepicmichelle.png')
st.image(image, width= None, use_column_width=True)
