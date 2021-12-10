import btalib
import pandas as pd

df = pd.read_csv("data/btalibtest.txt", parse_dates=True, index_col='Date')

macd = btalib.macd(df)

print(macd.df) 