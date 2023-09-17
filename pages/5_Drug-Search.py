import pandas as pd
import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="DDI",
    page_icon="💊",
)


st.title("Drug-Drug Interaction")

multi = '''A change in a drug’s effect on the body when the drug is taken together with a 
        second drug. A drug-drug interaction can delay, decrease, or enhance the 
        absorption of either drug. This can decrease or increase the action of either 
        or both drugs or cause adverse effects.'''

st.markdown(multi)

with st.sidebar.container():
    image = Image.open('MUST_Icon.png')
    st.image(image, width= None, use_column_width=True)

DrugDf = pd.read_csv("Antidepressant.tsv", sep="\t")

option = st.selectbox(
        'What medication are you looking for?',
        ('Imipramine', 'Amitriptyline', 'Doexpin', 'Desipramine', 'Isocarboxazid', 'Citalopram', 'Venlafaxine', 'Bupropion', 'Buspirone', 'Sertraline', 'Escitalopram', 'Mirtazapine')
    )
st.write('You selected:', option)

for index, row in DrugDf.iterrows():
  if option == row['Drug']:
      st.header(row['Drug'])
      st.subheader("Uses")
      st.write(row['Uses'])
      st.subheader("The Drug's Mechanisms")
      st.write(row['Mechanism'])
      st.subheader("Side Effects")
      st.write(row['Side Effects'])
