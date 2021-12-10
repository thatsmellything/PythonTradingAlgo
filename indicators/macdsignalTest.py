import btalib
import pandas as pd

df = pd.read_csv("data/btalibtest.txt", parse_dates=True, index_col='Date')

macd = btalib.macd(df) #5 day moving average with data supplied from csv file

print(macd.df) 