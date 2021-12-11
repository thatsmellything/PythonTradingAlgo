from dataPull.fetchData import pullData
from indicators import *
from dataPull import *
from indicators.getindicators import getindicators, getlastentry


def pulldataandprocess(timeframe, symbol, limit):
    pullData(timeframe, symbol, limit)
    getindicators(symbol)
    getlastentry(symbol)
    print(getlastentry(symbol))

#pulldataandprocess('1D', 'NET', '1000')