import btalib
import pandas as pd

df = pd.read_csv("data/btalibtest.txt", parse_dates=True, index_col='Date')

sma = btalib.sma(df, period=200) #5 day moving average with data supplied from csv file

print(sma.df) 