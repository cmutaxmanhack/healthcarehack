import streamlit as st
import pandas as pd
from io import StringIO

st.sidebar.header('Choose your weightings')

st.sidebar.write("""#### Choose your SG bias""")
def user_input_features():
    sgott = st.sidebar.slider('SG Off the Tee', 0, 100, 70, 5)
    sga2g = st.sidebar.slider('SG Approach to Green', 0, 100, 90, 5)
    sgatg = st.sidebar.slider('SG Around the Green', 0, 100, 50, 5)
    sgputt = st.sidebar.slider('SG Putting', 0, 100, 25, 5)
    sgmasters = st.sidebar.slider('SG Masters History', 0, 100, 80, 5)
    sgtotal = st.sidebar.slider('SG Total', 0, 100, 25, 5)
    sgpar5 = st.sidebar.slider('SG Par 5s', 0, 100, 75, 5)
    sgpar4 = st.sidebar.slider('SG Par 4s', 0, 100, 25, 5)
    sgpar3 = st.sidebar.slider('SG Par 3s', 0, 100, 20, 5)

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    st.write(bytes_data)

    # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    st.write(stringio)

    # To read file as string:
    string_data = stringio.read()
    st.write(string_data)

    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)
