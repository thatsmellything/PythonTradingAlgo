from config import *
import requests, json
from datetime import datetime
import alpaca_trade_api as tradeapi
from config import *
import btalib
import pandas as pd
from time import time, sleep
import sys

###RETURN LATEST INDICATORS###

###GET RSI###
def get_rsi(symbol):
    date, open_value, high_value, low_value, closing_value, volume, sma, rsi  = get_last_entry(symbol).split(',')
    print("RSI value of {} is {}".format(symbol, rsi.strip("\n")))
    return rsi
#get_rsi('SPY')
###GET Closing Value###
def get_closing_value(symbol):
    date, open_value, high_value, low_value, closing_value, volume, sma, rsi  = get_last_entry(symbol).split(',')
    #print(closing_value)
    return closing_value
#get_closing_value('SPY')
###GET SMA###
def get_sma(symbol):
    date, open_value, high_value, low_value, closing_value, volume, sma, rsi  = get_last_entry(symbol).split(',')
    #print(sma)
    return sma
#get_sma('SPY')
###GET Volume###
def get_volume(symbol):
    date, open_value, high_value, low_value, closing_value, volume, sma, rsi  = get_last_entry(symbol).split(',')
    #print(volume)
    return volume
#get_volume('SPY')
###GET Open Value###
def get_open_value(symbol):
    date, open_value, high_value, low_value, closing_value, volume, sma, rsi  = get_last_entry(symbol).split(',')
    #print(open_value)
    return open_value
#get_open_value('SPY')
###GET High Value###
def get_high_value(symbol):
    date, open_value, high_value, low_value, closing_value, volume, sma, rsi  = get_last_entry(symbol).split(',')
    #print(high_value)
    return high_value
#get_high_value('SPY')
###GET Low Value###
def get_low_value(symbol):
    date, open_value, high_value, low_value, closing_value, volume, sma, rsi  = get_last_entry(symbol).split(',')
    #print(low_value)
    return low_value
#get_low_value('SPY')
###GET Date###
def get_date(symbol):
    date, open_value, high_value, low_value, closing_value, volume, sma, rsi  = get_last_entry(symbol).split(',')
    #print(date)
    return date
#get_date('SPY')