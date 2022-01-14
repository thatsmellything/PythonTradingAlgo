from config import *
import requests, json
from datetime import datetime
import alpaca_trade_api as tradeapi
from config import *
import btalib
import pandas as pd
from time import time, sleep
import sys

###GRAB THE LAST ENTRY OF THE CSV FILE###
def get_last_entry(symbol):
    with open("data/" + symbol + ".csv", 'r') as file:
        data = file.readlines() 
    lastRow = data[-1]
    return lastRow
#print(get_last_entry('SPY'))