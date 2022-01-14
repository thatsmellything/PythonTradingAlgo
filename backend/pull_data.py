from config import *
import requests, json
from datetime import datetime
import alpaca_trade_api as tradeapi
from config import *
import btalib
import pandas as pd
from time import time, sleep
import sys

###PULL BARS DATA TO .txt FILE###
def pull_data(timeframe, symbols, limit):
    day_bars_url = BARS_URL + '/{}?symbols={}&limit={}'.format(timeframe, symbols, limit) #, SPY then others seperated by commas, you can add '&limit=1000' for more data
    r = requests.get(day_bars_url, headers=HEADERS)
    #print(r.content)
    #print(json.dumps(r.json(), indent=4)) #make it much more readable
    data = r.json()
    for symbol in data:
        filename = 'data/{}.txt'.format(symbol)
        f = open(filename, 'w+')
        #print(data['symbol'])
        f.write('Date,Open,High,Low,Close,Volume\n')
        for bar in data[symbol]:
            t = datetime.fromtimestamp(bar['t'])
            day = t.strftime('%Y-%m-%d')
            open_price = bar['o']
            high_price = bar['h']
            low_price = bar['l']
            close_price = bar['c']
            volume = bar['v']
            f.write('{},{},{},{},{},{}\n'.format(day, open_price, high_price, low_price, close_price, volume))

pull_data('1D','SPY','100')
pull_data('1Min', 'TR', '1000')