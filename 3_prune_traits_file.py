import pandas as pd
import numpy as np
from ete3 import Tree
import sys
import re
import subprocess 
from random import sample
"""
with open("id_to_rm_from_traits_file", "r") as infile:
 rm_id=infile.read().split("\n")

combined_df=pd.read_csv("combined_traits_tar.csv", sep=",", encoding = "ISO-8859-1")
print(combined_df)
for i in rm_id:
 print(i)
 #myindex = combined_df[combined_df["GRIN"] == i].index
 myindex = combined_df[combined_df["common_name"] == i].index
 combined_df.drop(myindex,inplace = True)

print(combined_df)
ref_id=combined_df["common_name"].values
with open("REF_order_final", "w+") as out:
 for i in ref_id:
  out.write(i.replace("'","")+"\n")

combined_df.to_csv("combined_traits_tar_pruned.csv", sep="\t", header=True, index=False)

#combined_df.drop(['GRIN'],axis=1,inplace = True)
combined_df.drop(["common_name"],axis=1,inplace = True)
#combined_df.dropna(axis='columns',inplace = True)
print(combined_df)
combined_df.to_csv("combined_traits_tar_pruned_id.csv", sep="\t", header=True, index=False)

"""
with open("id_to_rm_from_traits_file", "r") as infile:
 rm_id=infile.read().split("\n")

combined_df=pd.read_csv("combined_traits_tar.csv", sep=",", encoding = "ISO-8859-1")
print(combined_df)
for i in rm_id:
 print(i)
 myindex = combined_df[combined_df["LineName"] == i].index
 combined_df.drop(myindex,inplace = True)

print(combined_df)
ref_id=combined_df["LineName"].values
with open("REF_order_final", "w+") as out:
 for i in ref_id:
  out.write(i.replace("'","")+"\n")

combined_df.to_csv("combined_traits_tar_pruned.csv", sep="\t", header=True, index=False)

combined_df.drop(['Accession','LineName'],axis=1,inplace = True)
#combined_df.dropna(axis='columns',inplace = True)
print(combined_df)
combined_df.to_csv("combined_traits_tar_pruned_id.csv", sep="\t", header=True, index=False)

