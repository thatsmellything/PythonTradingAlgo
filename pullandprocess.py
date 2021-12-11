from dataPull.fetchData import pullData
from indicators import *
from dataPull import *
from indicators.formatdata import getindicators, getlastentry


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


###THESE PULL THE DATA AND PROCESS IT ALL AT ONCE###
def returnLatestMacd(timeframe, symbol, limit):
    macd = getmacd(pulldataandprocess(timeframe, symbol, limit))
    print(macd)
    return macd

def returnLatestRsi(timeframe, symbol, limit):
    rsi = getrsi(pulldataandprocess(timeframe, symbol, limit))
    print(rsi)
    return rsi

def returnLatestSignal(timeframe, symbol, limit):
    signal = getsignal(pulldataandprocess(timeframe, symbol, limit))
    print(signal)
    return signal
