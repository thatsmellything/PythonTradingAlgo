import requests, json
from config import *
import pullandprocess

BASE_URL = "https://paper-api.alpaca.markets"
ACCOUNT_URL = "{}/v2/account".format(BASE_URL)
ORDERS_URL = "{}/v2/orders".format(BASE_URL)
HEADERS = {'APCA-API-KEY-ID': API_KEY_ID, 'APCA-API-SECRET-KEY': SECRET_KEY}




def create_order_market(symbol, qty, side, type, time_in_force):
    data = {
        "symbol": symbol,
        "qty": qty,
        "side": side,
        "type": type,
        "time_in_force": time_in_force
    }
    r = requests.post(ORDERS_URL, json=data, headers=HEADERS)

    return json.loads(r.content)

def create_order_limit(symbol, qty, side, type, time_in_force,limit_price):
    data = {
        "symbol":symbol,
        "qty":qty,
        "side":side,
        "type":type,
        "time_in_force":time_in_force,
        "limit_price":limit_price
    }
    r = requests.post(ORDERS_URL, json=data, headers=HEADERS)

    return json.loads(r.content)
    


def makemarketorderiflowrsi(timeframe, symbol, datalimit, amount, lowerthanrsi):
    if float(pullandprocess.returnLatestRsi(timeframe, symbol, datalimit).strip("\n")) < float(lowerthanrsi):
        create_order_market(symbol, amount, 'buy', 'market', 'gtc')
        print("buying {} of {}, type {} {} {}".format(amount, symbol, 'market', 'buy', 'gtc'))
    else:
        print("not buying any stocks")
    

#makemarketorderiflowrsi('1D', 'CLSK', '100', '100', '35')


def makelimitorderiflowrsi(timeframe, symbol, datalimit, amount, lowerthanrsi):
    if float(pullandprocess.returnLatestRsi(timeframe, symbol, datalimit).strip("\n")) < float(lowerthanrsi):
        price = pullandprocess.returnClosingVal(timeframe, symbol, datalimit).strip("\n")
        #print(price)
        create_order_limit(symbol, amount, 'buy', 'limit', 'opg', '{}'.format(price))
        print("buying {} of {}, type {} {} {} at {}".format(amount, symbol, 'limit', 'buy', 'opg', price))
    else:
        print("not buying any stocks")
makelimitorderiflowrsi('1D', 'CLSK', '100', '100', '35')