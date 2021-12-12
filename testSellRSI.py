import requests, json
from config import *
import pullandprocess

BASE_URL = "https://paper-api.alpaca.markets"
ACCOUNT_URL = "{}/v2/account".format(BASE_URL)
ORDERS_URL = "{}/v2/orders".format(BASE_URL)
HEADERS = {'APCA-API-KEY-ID': API_KEY_ID, 'APCA-API-SECRET-KEY': SECRET_KEY}




def create_order(symbol, qty, side, type, time_in_force):
    data = {
        "symbol": symbol,
        "qty": qty,
        "side": side,
        "type": type,
        "time_in_force": time_in_force
    }

def makeorderiflowrsi(timeframe, symbol, datalimit, amount, lowerthanrsi):
    if float(pullandprocess.returnLatestRsi(timeframe, symbol, datalimit).strip("\n")) < float(lowerthanrsi):
        create_order(symbol, amount, 'sell', 'market', 'gtc')
        print("buying {} of {}, type {} {} {}".format(amount, symbol, 'market', 'sell', 'gtc'))
    else:
        print("not buying any stocks")

makeorderiflowrsi('1D', 'CLSK', '100', '100', '50')