import pandas as pd
import numpy as np

large = pd.read_csv("../../dataset/Sorted/removed_duplicates/final.csv", chinksize=100000)

with open("../../dataset/sorted/removed_duplicates/indexes.csv") as f:
    for df in large:
        unique_rows = df.drop_duplicates(subset=['i', 'j'])
        
        for i,j in unique_rows.iterrows():
            f.write(i+"\n")

