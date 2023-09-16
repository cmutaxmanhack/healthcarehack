import pandas as pd
import streamlit as st


DataDf = pd.read_csv("response_to_antidepressant.tsv", sep="\t")

option = st.selectbox(
        'What medication are you looking for?',
        ('Imipramine', 'Amitriptyline', 'Doexpin', 'Desipramine', 'Isocarboxazid', 'Fluoxetine', 'Venlafaxine', 'Bupropion'))
    
    st.write('You selected:', option)

# Function to get drug interactions
def get_drug_interactions(df, drug_name):
    interactions = df[df.iloc[:, 0] == drug_name].iloc[:, 1].tolist()
    return interactions

# Main Streamlit application
def main():
    # Your existing code for antidepressants
    DataDf = pd.read_csv("response_to_antidepressant.tsv", sep="\t")
    # Reading drug interactions data
    ddi_df = pd.read_csv("ddi.csv")

    # Streamlit dropdown for drug interactions
    
    
    #st.subheader("Check Drug Interactions")
    #unique_drugs = ddi_df.iloc[:, 0].unique()
    #selected_drug = st.selectbox("Select a drug to check its interactions:", unique_drugs)
    
    # Show drug interactions
    interactions = get_drug_interactions(ddi_df, selected_drug)
    if len(interactions) == 0:
        st.write(f"No known interactions for {selected_drug}.")
    else:
        st.write(f"The following drugs interact with {selected_drug}:")
        for interaction in interactions:
            st.write(f"- {interaction}")

