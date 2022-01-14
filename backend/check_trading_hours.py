from config import *
import requests, json
from datetime import datetime
import alpaca_trade_api as tradeapi
from config import *
import btalib
import pandas as pd
from time import time, sleep
import sys

###CHECK TRADING HOURS###
def check_trading_hours():
    base_url = 'https://paper-api.alpaca.markets'
    api = tradeapi.REST(api_key, api_secret, base_url, api_version='v2')
    clock = api.get_clock()
    if clock.is_open:
        #print('Market is open.')
        return True
    else:
        #print('Market is closed.')
        return False
check_trading_hours()