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

st.caption("This platform is only meant for patient education and understanding. The advice presented here does not substitute the advice of a professional healthcare provider. Always consult with your medical provider with any questions you may have regarding a medical condition or treatment.")
    
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

    # Streamlit dropdown for drug selection
    option = st.selectbox(
        'What medication are you looking for?',
        ('Imipramine', 'Amitriptyline', 'Doexpin', 'Desipramine', 'Isocarboxazid', 'Fluoxetine', 'Venlafaxine', 'Bupropion')
    )
    st.write('You selected:', option)
    
    # Get and show drug interactions
    interactions = get_drug_interactions(ddi_df, option)
    if len(interactions) == 0:
        st.write(f"No known interactions for {option}.")
    else:
        # New Streamlit dropdown for interacting drugs
        selected_interaction = st.selectbox(
            'Select an interacting drug to learn more:',
            interactions
        )
        
        # Display warning message
        st.divider()
        st.write(f"{option} and {selected_interaction} should not taken together as it can either increase negative side effects or decrease the effectiveness of the antidepressants.")
        st.divider()
# Run the main function to execute the Streamlit app
if __name__ == '__main__':
    main()
