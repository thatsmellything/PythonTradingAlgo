import btalib
import pandas as pd

df = pd.read_csv("../data/btalibtest.txt", parse_dates=True, index_col='Date')

macd = btalib.macd(df)

#print(macd.df) 

df = pd.read_csv("../dataPull/stockdata/AAPL.txt", parse_dates=True, index_col='Date')

macd = btalib.macd(df)

rsi = btalib.rsi(df) #period default is 14

#print(rsi.df) 
df = pd.read_csv("../dataPull/stockdata/AAPL.txt", parse_dates=True, index_col='Date')

rsi = btalib.rsi(df)

#print(macd.df) 
df['macd'] = macd.df['macd']
df['signal'] = macd.df['signal']
df['histogram'] = macd.df['histogram']
df['rsi'] = rsi.df['rsi']
print(df)