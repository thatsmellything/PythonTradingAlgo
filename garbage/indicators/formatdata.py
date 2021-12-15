import btalib
import pandas as pd





def getindicators(symbol):


    df = pd.read_csv("./data/{}.txt".format(symbol), parse_dates=True, index_col='Date')
    print(df)
    macd = btalib.macd(df)
    print(macd)
    rsi = btalib.rsi(df) #period default is 14, rsi = btalib.rsi(df, period = 10)
    signal = btalib.macd_signal(df)
    histogram = btalib.macd_histogram(df)
    
    df['macd'] = macd.df['macd']
    df['signal'] = signal.df['signal']
    df['histogram'] = histogram.df['histogram']
    df['rsi'] = rsi.df['rsi']

    print(macd)
    df.to_csv('./data/processed/{}'.format(symbol) + '.csv', index=True)
    return df
print(getindicators('TSLA'))

def getlastentry(filename):
    with open("./data/processed/" + filename + ".csv", 'r') as file:
        data = file.readlines()
    
    lastRow = data[-1]
    
    return lastRow
#print(getlastentry('btalibtest'))

