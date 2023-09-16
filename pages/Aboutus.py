import streamlit as st

st.set_page_config(
    page_title="About Us",
    page_icon="🌸",
)

with st.sidebar.container():
    image = Image.open('MUST_Icon.jpg')
    st.image(image, width= None, use_column_width=True)

st.header('_***Our Mission***:_ :cherry_blossom:', divider='rainbow')

st.markdown ("Our mission is to empower individuals and healthcare professionals with personalized healthcare solutions by providing an easy-to-use and free-access platform for antidepressant medication screening. We are dedicated to revolutionizing the way people approach their health and wellness journey. The goal of our website is to offer a user-friendly and accessible tool that harnesses the power of data and technology to help users discover the medications that work best for their unique needs. Through cutting-edge research, data analysis, and a commitment to user privacy, we aim to guide individuals and healthcare professionals toward more effective and tailored treatment options, ultimately improving their quality of life and well-being. We envision a future where healthcare is not a one-size-fits-all approach, but a personalized and informed choice, and our mission is to make this vision a reality.")
