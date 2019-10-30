import os
import sys
import pandas as pd

df = pd.read_csv(os.path.join(os.path.dirname(os.path.dirname(__file__)), '..', 'dataset/small.csv'), chunksize=300000)

for i in df:
    print(i)
