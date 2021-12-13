import requests, json
from config import *
import pullandprocess
from time import time, sleep

BASE_URL = "https://paper-api.alpaca.markets"
ACCOUNT_URL = "{}/v2/account".format(BASE_URL)
ORDERS_URL = "{}/v2/orders".format(BASE_URL)
HEADERS = {'APCA-API-KEY-ID': API_KEY_ID, 'APCA-API-SECRET-KEY': SECRET_KEY}





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
    



    

#makemarketorderiflowrsi('1D', 'CLSK', '1000', '100', '45')


def makelimitorderiflowrsi(timeframeofdata, symbol, datalimit, amount, lowerthanrsi, ordergoodfor):
    if float(pullandprocess.returnLatestRsi(timeframeofdata, symbol, datalimit).strip("\n")) < float(lowerthanrsi):
        price = pullandprocess.returnClosingVal(timeframeofdata, symbol, datalimit).strip("\n")
        #print(price)
        create_order_limit(symbol, amount, 'buy', 'limit', 'gtc', '{}'.format(price))
        print("buying {} of {}, type {} {} {} at {}".format(amount, symbol, 'limit', 'buy', ordergoodfor, price))
        sleep(360)
        makeLimitOrderIfRSIUp('1Min', 'CLSK', '1000', '100', '45', 'day')
    else:
        print("not buying any stocks")





def makeLimitOrderIfRSIUp(timeframeofdata, symbol, datalimit, amount, lowerthanrsi, ordergoodfor):
    if float(pullandprocess.returnLatestRsi(timeframeofdata, symbol, datalimit).strip("\n")) > float(lowerthanrsi):
        print("RSI value has been met, selling at yesterdays close price")
        priceAtClose = pullandprocess.returnClosingVal(timeframeofdata, symbol, datalimit).strip("\n")
        create_order_limit(symbol, amount, 'sell', 'limit', 'day', '{}'.format(priceAtClose))
        print("Selling {} of {}, type {} {} {} at {}".format(amount, symbol, 'limit', 'sell', ordergoodfor, priceAtClose))
    else:
        print("RSI value to sell has not been met, taking 6% profit for the day")
        priceAtClose = pullandprocess.returnClosingVal(timeframeofdata, symbol, datalimit).strip("\n")
        priceToSell = float(priceAtClose) * 1.06
        #print(price)
        create_order_limit(symbol, amount, 'sell', 'limit', 'day', '{}'.format(priceToSell))
        print("Selling {} of {}, type {} {} {} at {}".format(amount, symbol, 'limit', 'sell', ordergoodfor, priceToSell))
#makeLimitOrderIfRSIUp('1D', 'CLSK', '1000', '100', '45', 'day')

while True:
    sleep(60 - time() % 60)
	# thing to run
    makelimitorderiflowrsi('1Min', 'CLSK', '1000', '100', '35', 'day')

