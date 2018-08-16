import pandas as pd

df = pd.read_csv("YahooFinance.csv")

saved_column = df['Open']

print (saved_column)
