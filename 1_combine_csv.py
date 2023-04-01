import pandas as pd
import numpy as np
from ete3 import Tree
import sys
import re
import subprocess 
from random import sample

f1=pd.read_csv("kernel_phenolics_mean.csv", sep=",", encoding = "ISO-8859-1").dropna(axis=1, how='all')
f2=pd.read_csv("tar spot supplemental.csv", sep=",", encoding = "ISO-8859-1").dropna(axis=1, how='all')

print(f1)
print(f2)
combined_df = pd.merge(f1,f2, how='inner')
print(combined_df)

ref_id=combined_df["LineName"].values
with open("REF_order", "w+") as out:
 for i in ref_id:
  out.write(i.replace("'","")+"\n") 

combined_df.to_csv("combined_traits_tar.csv", header=True, index=False)
