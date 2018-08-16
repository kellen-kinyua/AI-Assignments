import numpy as np
import random
import csv
import pandas as pd

def moving_average(a, n=5) :
    ret = np.cumsum(a, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    return ret[n - 1:] / n


df = pd.read_csv("YahooFinance.csv")
col_open = df['High'].values.tolist()

print("The values")
print(col_open)

print("Moving average")
print(moving_average(col_open))
