import btalib
import pandas as pd





def getindicators(symbol):


    df = pd.read_csv("../data/{}.txt".format(symbol), parse_dates=True, index_col='Date')

    macd = btalib.macd(df)

    rsi = btalib.rsi(df) #period default is 14, rsi = btalib.rsi(df, period = 10)

    
    df['macd'] = macd.df['macd']
    df['signal'] = macd.df['signal']
    df['histogram'] = macd.df['histogram']
    df['rsi'] = rsi.df['rsi']
    df.to_csv('../data/processed/{}'.format(symbol) + '.csv', index=True)
    return df
print(getindicators('btalibtest'))

def getlastentry(filename):
    with open("../data/processed/" + filename + ".csv", 'r') as file:
        data = file.readlines()
    
    lastRow = data[-1]
    
    return lastRow
#print(getlastentry('btalibtest'))

