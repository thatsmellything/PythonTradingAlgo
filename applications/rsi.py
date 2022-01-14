from config import *
import requests, json
from datetime import datetime
import alpaca_trade_api as tradeapi
from config import *
import btalib
import pandas as pd
from time import time, sleep
import sys
import backend



###CHECK RSI LEVELS AND SELL ORDER IF ABOVE THRESHOLD###
def make_limit_sell_order_if_rsi_high(symbol, amount, rsi_value, profit_percentage, buy_price):
    order_good_for = 'gtc'
    ##print countdown timer of 5 min by 30 second intervals
    for i in range(1,6):
        print(i)
        sleep(30)
    print('Checking if RSI is higher than {} on ticker {}'.format(rsi_value, symbol))
    if float(backend.get_rsi(symbol).strip("\n")) > float(rsi_value):
        print("RSI value has been met, selling at last bars close price")
        price_at_close = backend.get_closing_value.strip("\n")
        backend.create_limit_order(symbol, amount, 'sell', 'limit', 'gtc', '{}'.format(price_at_close))
        print("Selling {} of {}, type {} {} {} at {}".format(amount, symbol, 'limit', 'sell', order_good_for, price_at_close))
    else:
        print("RSI value to sell has not been met, taking {}% profit for the day".format(profit_percentage))
        price_at_close = backend.get_closing_value(symbol).strip("\n")
        if float(profit_percentage) < 10:
            profit_percentage = profit_percentage.strip(".")
            price_to_sell = float(buy_price) * (float('1.0'+ profit_percentage))
        else:
            profit_percentage = profit_percentage.strip(".")
            price_to_sell = float(buy_price) * (float('1.'+ profit_percentage))
        
        #print(price)
        backend.create_limit_order(symbol, amount, 'sell', 'limit', 'gtc', '{}'.format(price_to_sell))
        print("Selling {} of {}, type {} {} {} at {}".format(amount, symbol, 'limit', 'sell', order_good_for, price_to_sell))
#makeLimitOrderIfRSIUp('1D', 'CLSK', '1000', '100', '45', 'day')

###CHECK RSI LEVELS AND BUY ORDER IF BELOW THRESHOLD###
def make_limit_buy_order_if_low_rsi(symbol, amount, low_rsi_value, high_rsi_value, profit_percentage):
    order_good_for = 'day'
    
    print('Checking if RSI is lower than {} on ticker {}'.format(low_rsi_value, symbol))
    if float(backend.get_rsi(symbol).strip("\n")) < float(low_rsi_value):
        price = backend.get_closing_value(symbol).strip("\n")
        print(price)
        backend.create_limit_order(symbol, amount, 'buy', 'limit', order_good_for, '{}'.format(price))
        price = (float(price) * 1.0025) #add 0.25% to price to make sure it is bought
        print("Buying {} of {}, type {} {} at {}".format(amount, symbol, 'limit', order_good_for, price))
        #profit_percentage = 1 + float(profit_percentage)
        make_limit_sell_order_if_rsi_high(symbol, amount, high_rsi_value, '{}'.format(profit_percentage), price)

       
    else:

        print("RSI value is not below {}, not buying any stocks\n".format(low_rsi_value))
#make_limit_buy_order_if_low_rsi('SPY', 1, '35')