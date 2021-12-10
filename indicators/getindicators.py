import btalib
import pandas as pd

#df = pd.read_csv("../data/btalibtest.txt", parse_dates=True, index_col='Date')

#macd = btalib.macd(df)

#print(macd.df) 

#df = pd.read_csv("../dataPull/stockdata/AAPL.txt", parse_dates=True, index_col='Date')



def getindicators(symbol):
#symbol = 'btalibtest'

    df = pd.read_csv("../data/{}.txt".format(symbol), parse_dates=True, index_col='Date')

    macd = btalib.macd(df)

    rsi = btalib.rsi(df) #period default is 14, rsi = btalib.rsi(df, period = 10)

    
    df['macd'] = macd.df['macd']
    df['signal'] = macd.df['signal']
    df['histogram'] = macd.df['histogram']
    df['rsi'] = rsi.df['rsi']
    print(df)
getindicators('btalibtest')

def getlastentry(filename):
    with open(filename, 'r') as file:
        data = file.readlines()
    lastRow = data[-3]
    print(lastRow)
getlastentry('datatest.txt')