import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Profile",
    page_icon="👩",
)

with st.sidebar.container():
    image = Image.open('MUST_Icon.png')
    st.image(image, width= None, use_column_width=True)
    
# Initialize session state
if 'profile_saved' not in st.session_state:
    st.session_state['profile_saved'] = False

# Title
st.header('***My Profile***')

if not st.session_state['profile_saved']:
    # Profile Image
    image = Image.open('ProfilePic.jpeg')
    st.image(image, caption='Profile Picture', width=500, use_column_width=False)

    # Personal Information
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

    consent = st.checkbox("Do you consent for your health and physcial data to be collected anonymously for research purposes")
    
    # Save Profile Button
    if st.button("Save Profile"):
        st.session_state['profile_saved'] = True
        st.session_state['name'] = name
        st.session_state['age'] = age
        st.session_state['sex'] = sex
        st.session_state['height'] = height
        st.session_state['weight'] = weight
        st.session_state['medications'] = medications
        st.session_state['conditions'] = conditions
        st.experimental_rerun()
else:
    # Profile Information Display
    st.subheader(f'Name: {st.session_state["name"]}')
    st.subheader(f'Age: {st.session_state["age"]}')
    st.subheader(f'Sex: {st.session_state["sex"]}')
    st.subheader(f'Height: {st.session_state["height"]} cm')
    st.subheader(f'Weight: {st.session_state["weight"]} kg')
    st.subheader(f'Medications: {st.session_state["medications"]}')
    st.subheader(f'Known Conditions: {st.session_state["conditions"]}')
    st.success("Profile Saved Successfully")

    # Here you can add code to save these details to a database, a file, or any other backend storage.
