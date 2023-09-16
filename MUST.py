import numpy
import pandas as pd
import streamlit as st
from PIL import Image


st.set_page_config(
    page_title="MUST: Machine Utilized Screening Tool",
    page_icon="🧬",
)

image = Image.open("MUST_Icon.png")
st.image(image, caption=None, width= 200, use_column_width=None, clamp=False, channels="RGB", output_format="auto")


DataDf = pd.read_csv("response_to_antidepressant.tsv", sep="\t")

st.caption("This platform is only meant for patient education and understanding. The advice presented here does not substitute the advice of a professional healthcare provider. Always consult with your medical provider with any questions you may have regarding a medical condition or treatment.") 

option = st.selectbox(
        'What condition medication are you looking for?',
        ('Major Depressive Disorder', 'Unipolar Disorder', 'Bipolar Disorder', 'Generalized Anxiety Disorder', 'Schizophrenia'))
    
st.write('You selected:', option)

#TestDf = pd.read_csv("patient3.tsv", sep="\t")

test_file = st.file_uploader("Upload your genome", type=["tsv"])

alleleArray = []


if test_file:
    TestDf = pd.read_csv(test_file, sep="\t")

    for index, row in TestDf.iterrows():
        alleleArray.append(row.tolist())
    
    trait_dict = {
        "Risk Allele": [],
        "p Value": [],
        "p Value Annotation": [],
        "Trait Name": [],        
        "efo Traits": [],
        "bg Traits": []
        }
    
    for index, row in DataDf.iterrows():
        for allele_list in alleleArray:
            for allele in allele_list:
                if allele in row['riskAllele']:
                    trait_dict["Risk Allele"].append(row['riskAllele'])
                    trait_dict["p Value"].append(row['pValue'])
                    trait_dict["p Value Annotation"].append(row['pValueAnnotation'])
                    trait_dict["Trait Name"].append(row['traitName'])
                    trait_dict["efo Traits"].append(row['efoTraits'])
                    trait_dict["bg Traits"].append(row['bgTraits'])
    
    trait_Df = pd.DataFrame(trait_dict)
    trait_Df = trait_Df.set_index("Risk Allele")
    trait_Df = trait_Df.sort_values(by=["p Value"], ascending= False)
    
    #print("You are looking for medication that works for Major Depressive Disorder.\n")
    st.subheader("Here are potential treatment options based on the genetic information you provided: ")
    for index, row in trait_Df.iterrows():
        if row["efo Traits"] == "antidepressant-induced side effect,response to citalopram,response to buspirone,response to antidepressant":
            st.write("Citalopram, Buspirone, Sertraline, Bupropion\n")
            st.write("ALERT! ⚠️ You are at risk for General Side Effects: including but not limited to nausea, weight gain, and sleeping trouble.")
            print()
    
        if row["efo Traits"] == "antidepressant-induced visual impairment,response to bupropion,response to citalopram,response to antidepressant":
            st.write("Citalopram and Bupropion\n")
            st.write("ALERT! ⚠️ You are at risk for these side effects: Antidepressant-Induced Visual and Hearing Impairment")
            print()
    
        if row["efo Traits"] == "response to citalopram,antidepressant-induced dizziness,response to buspirone,response to antidepressant":
            st.write("Citalopram, Buspirone, Venlafaxine")
            st.write("ALERT! ⚠️ You are at risk for these side effects: Antidepressant-Induced Dizziness")
            print()
    
        if row["efo Traits"] == "antidepressant-induced sexual dysfunction,response to bupropion,response to antidepressant":
            st.write("Bupropion")
            st.write("ALERT! ⚠️ You are at risk for these side effects: Antidepressant-Induced Sexual Dysfunction")
            print()
        
        if row["efo Traits"] == "unipolar depression,response to escitalopram,response to citalopram,mood disorder":
            st.write("Unfortunately, based on the genetic information you provided Citalopram and Escitalopram have not proven effective for treating your condition.")
            print()
    
        if row["efo Traits"] == "unipolar depression,response to bupropion,mood disorder":
            st.write("Unfortunately, based on the genetic information you provided Bupropion has not proven effective for treating your condition. ")
            print()
    
        if row["efo Traits"] == "response to antidepressant":
            st.write("Unfortunately, patients with similar genetic information have exibhited antidepressant treatment resistance.")
            st.write("Please consult your doctor for alternative treatment options.")
            print()
    
        if row["efo Traits"] == "unipolar depression,response to selective serotonin reuptake inhibitor,mood disorder":
            st.write("Unfortunately, based on the genetic information you provided Selective Serotonin Reuptake inhibitors (SSRIs) have not proven effective for treating your condition. SSRIs include but are not limited to medication such as Serteraline, Citalopram, Escitalopram, Fluoxetine, etc.")
        else:
            st.write(" ")
