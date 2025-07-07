import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
#matplotlib inline
import matplotlib
matplotlib.rcParams['figure.figsize'] = [20, 10]

df1 = pd.read_csv('Bengaluru_House_Data.csv')
print(df1.head())  # Show first 5 rows
print(df1.shape)   # Show dimensions

print(df1.groupby('area_type')['area_type'].agg('count'))

