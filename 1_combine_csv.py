import pandas as pd
import numpy as np
from ete3 import Tree
import sys
import re
import subprocess 
from random import sample

"""
f1=pd.read_csv("widiv2021pheno_4colorclasses_cleaned02272023.csv", sep=",", encoding = "ISO-8859-1").dropna(axis=1, how='all')

# Select the columns to keep after running randomForest to test for variable importance
#f1 = f1[["GRIN","MaizeObsTarSpot"]]
f1 = f1[["common_name","MaizeObsTarSpot"]]

#NaNs are annoying to deal with in tab-deliminated trait files -- they mess up the columns
f1.dropna(axis=0,inplace = True)
combined_df = f1
#ref_id=combined_df["GRIN"].values
ref_id=combined_df["common_name"].values
with open("REF_order", "w+") as out:
 for i in ref_id:
  out.write(i.replace("'","")+"\n") 

combined_df.to_csv("combined_traits_tar.csv", header=True, index=False)
"""

f1=pd.read_csv("kernel_phenolics_mean.csv", sep=",", encoding = "ISO-8859-1").dropna(axis=1, how='all')
f2=pd.read_csv("tar_spot_supplemental_mod.csv", sep=",", encoding = "ISO-8859-1").dropna(axis=1, how='all')

# Select the columns to keep after running randomForest to test for variable importance
f1 = f1[["Accession","LineName",'VanillicAcid','Dihydrokaempferol', "SyringicAcid"]]
f2 = f2[["Accession","INAUDPC", "WISFinal"]]

#NaNs are annoying to deal with in tab-deliminated trait files -- they mess up the columns
f1.dropna(axis=0,inplace = True)
f2.dropna(axis=0,inplace = True)

combined_df = pd.merge(f1,f2, how='inner')
print(combined_df)

ref_id=combined_df["LineName"].values
with open("REF_order", "w+") as out:
 for i in ref_id:
  out.write(i.replace("'","")+"\n") 

combined_df.to_csv("combined_traits_tar.csv", header=True, index=False)


"""
# for adding in a third file that is no longer used
f3=pd.read_csv("SupplementalDataFileS2_GenotypesAndTraitValues.csv", sep=",", encoding = "ISO-8859-1").dropna(axis=1, how='all')
print(f3["GrainPercentMoisture_J"])
f3=f3[["Accession","GrainPercentMoisture_J"]]
combined_df = pd.merge(f1,f2, how='inner')
print("F1F2")
print(combined_df)
combined_df = pd.merge(combined_df,f3, how='inner')
print("F1F2F3")
print(combined_df)
"""

"""
# getting only one value, the WISFinal
#NaNs are annoying to deal with in tab-deliminated trait files -- they mess up the columns
f1=pd.read_csv("kernel_phenolics_mean.csv", sep=",", encoding = "ISO-8859-1").dropna(axis=1, how='all')
f2=pd.read_csv("tar_spot_supplemental_mod.csv", sep=",", encoding = "ISO-8859-1").dropna(axis=1, how='all')
f2=f2[["Accession","WISFinal"]]
f1=f1[["Accession","LineName"]]
f2.dropna(axis=0,inplace = True)

combined_df = pd.merge(f1,f2, how='inner')
print(combined_df)
ref_id=combined_df["LineName"].values
with open("REF_order", "w+") as out:
 for i in ref_id:
  out.write(i.replace("'","")+"\n")

combined_df.to_csv("combined_traits_tar.csv", header=True, index=False)

"""
