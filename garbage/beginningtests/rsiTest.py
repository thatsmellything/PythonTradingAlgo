import btalib
import pandas as pd

df = pd.read_csv("../data/btalibtest.txt", parse_dates=True, index_col='Date')

rsi = btalib.rsi(df) #period default is 14

print(rsi.df) 
df = pd.read_csv("../dataPull/stockdata/CLSK.txt", parse_dates=True, index_col='Date')

rsi = btalib.rsi(df) #period default is 14

print(rsi.df) 