from config import *
import requests, json
from datetime import datetime
import alpaca_trade_api as tradeapi
from config import *
import btalib
import pandas as pd
from time import time, sleep
import sys

#NEED TO ADD MACD AND RSI TO CSV
def get_indicators(symbol):
    df = pd.read_csv("data/{}.txt".format(symbol), parse_dates=True, index_col=0)
    #print(df)
    sma = btalib.sma(df)
    rsi = btalib.rsi(df)
    #macd = btalib.macd(df)
    
    
    df['sma'] = sma.df
    rsi = btalib.rsi(df)
    df['rsi'] = rsi.df
    #df['macd'] = macd.df
    
    #print(df)
    df.to_csv('data/{}.csv'.format(symbol), index=True)

    ##THESE DO NOT WORK FOR NOW##
    #macd = btalib.macd(df)
    #print(macd)
    #rsi = btalib.rsi(df) #period default is 14, rsi = btalib.rsi(df, period = 10)
    #signal = btalib.macd_signal(df)
    #histogram = btalib.macd_histogram(df)
    
    #df['macd'] = macd.df
    #df['signal'] = signal.df
    #df['histogram'] = histogram.df
    #df['rsi'] = rsi.df


    return df
#get_indicators('SPY')