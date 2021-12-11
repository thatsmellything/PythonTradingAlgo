from dataPull.fetchData import pullData
from indicators import *
from dataPull import *
from indicators.getindicators import getindicators, getlastentry


def pulldataandprocess(timeframe, symbol, limit):
    pullData(timeframe, symbol, limit)
    getindicators(symbol)
    getlastentry(symbol)
    #print(getlastentry(symbol))
    values = getlastentry(symbol)
    return values
#test
#pulldataandprocess('1D', 'AAPL', '100')



###GET MACD###
def getmacd(values):
    date, openVal, highVal, lowVal, closeVal, volume, openInterest, macd, signal, histogram, rsi  = values.split(',')
    #print(macd)
    return macd
#getmacd(pulldataandprocess('1D', 'AAPL', '100'))



###GET RSI###
def getrsi(values):
    date, openVal, highVal, lowVal, closeVal, volume, openInterest, macd, signal, histogram, rsi  = values.split(',')
    #print(rsi)
    return rsi

###GET SIGNAL###
def getsignal(values):
    date, openVal, highVal, lowVal, closeVal, volume, openInterest, macd, signal, histogram, rsi  = values.split(',')
    #print(signal)
    return signal