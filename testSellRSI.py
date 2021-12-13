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
    if float(pullandprocess.returnLatestRsi(timeframe, symbol, datalimit).strip("\n")) > float(lowerthanrsi):
        create_order_market(symbol, amount, 'sell', 'market', 'gtc')
        print("Selling {} of {}, type {} {} {}".format(amount, symbol, 'market', 'sell', 'gtc'))
    else:
        print("not selling buying any stocks")
    

#makemarketorderiflowrsi('1D', 'CLSK', '1000', '100', '45')


def makeLimitOrderIfRSIUp(timeframe, symbol, datalimit, amount, lowerthanrsi):
    if float(pullandprocess.returnLatestRsi(timeframe, symbol, datalimit).strip("\n")) > float(lowerthanrsi):
        print("RSI value has been met, selling at yesterdays close price")
        priceAtClose = pullandprocess.returnClosingVal(timeframe, symbol, datalimit).strip("\n")
        create_order_limit(symbol, amount, 'sell', 'limit', 'day', '{}'.format(priceAtClose))
        print("Selling {} of {}, type {} {} {} at {}".format(amount, symbol, 'limit', 'sell', 'day', priceAtClose))
    else:
        print("RSI value to sell has not been met, taking 6% profit for the day")
        priceAtClose = pullandprocess.returnClosingVal(timeframe, symbol, datalimit).strip("\n")
        priceToSell = float(priceAtClose) * 1.06
        #print(price)
        create_order_limit(symbol, amount, 'sell', 'limit', 'day', '{}'.format(priceToSell))
        print("Selling {} of {}, type {} {} {} at {}".format(amount, symbol, 'limit', 'sell', 'day', priceToSell))
makeLimitOrderIfRSIUp('1D', 'CLSK', '1000', '100', '45')
