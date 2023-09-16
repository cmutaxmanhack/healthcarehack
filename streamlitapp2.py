import streamlit as st
import numpy
import pandas as pd

DataDf = pd.read_csv("response_to_antidepressant.tsv", sep="\t")
TestDf = pd.read_csv("TestData.tsv", sep="\t")

alleleArray = []

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

print(trait_Df)

for index, column in trait_Df.iterrows():
    if column["p Value Annotation"] == "(Citalopram+Buspirone, Dizziness)":
        print("Citalopram and Buspirone effective in treating major depressive disorder.\n"
              "Side Effects: At risk for anti-depressant-induced dizziness.")
