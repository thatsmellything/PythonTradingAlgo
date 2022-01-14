from config import *
import requests, json
from datetime import datetime
import alpaca_trade_api as tradeapi
from config import *
import btalib
import pandas as pd
from time import time, sleep
import sys

###FORMAT DATA .txt INTO .csv (turns out not needed)###
def format_data(symbol):
    filename = 'data/{}.txt'.format(symbol)
    f = open(filename, 'r')
    lines = f.readlines()
    f.close()
    filename = 'data/{}.csv'.format(symbol)
    f = open(filename, 'w+')
    #f.write('Date,Open,High,Low,Close,Volume\n')
    for line in lines:
        f.write(line.replace(',', ' '))
    f.close()
#format_data('SPY')