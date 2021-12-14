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


def makelimitorderiflowrsi(timeframeofdata, symbol, datalimit, amount, lowerthanrsi, ordergoodfor, profitpercentage):
    print("attempting to buy {} {} stock, and gain at least {} percent".format(amount, symbol, profitpercentage))
    if float(pullandprocess.returnLatestRsi(timeframeofdata, symbol, datalimit).strip("\n")) < float(lowerthanrsi):
        price = pullandprocess.returnClosingVal(timeframeofdata, symbol, datalimit).strip("\n")
        #print(price)
        create_order_limit(symbol, amount, 'buy', 'limit', 'day', '{}'.format(price))
        print("buying {} of {}, type {} {} {} at {}".format(amount, symbol, 'limit', 'buy', 'gtc', price))
        #sleep(360)
        profitpercentage = profitpercentage
        makeLimitOrderIfRSIUp(timeframeofdata, symbol, datalimit, amount, '45', ordergoodfor, profitpercentage)
    else:
        print("not buying any stocks")





def makeLimitOrderIfRSIUp(timeframeofdata, symbol, datalimit, amount, lowerthanrsi, ordergoodfor, profitpercentage):
    print("waiting 6 more minutes until resuming")
    sleep(30)
    print("waiting 5.5 more minutes until resuming")
    sleep(30)
    print("waiting 5 more minutes until resuming")
    sleep(30)
    print("waiting 4.5 more minutes until resuming")
    sleep(30)
    print("waiting 4 more minutes until resuming")
    sleep(30)
    print("waiting 3.5 more minutes until resuming")
    sleep(30)
    print("waiting 3 more minutes until resuming")
    sleep(30)
    print("waiting 2.5 more minutes until resuming")
    sleep(30)
    print("waiting 2 more minutes until resuming")
    sleep(30)
    print("waiting 1.5 more minutes until resuming")
    sleep(30)
    print("waiting 1 more minutes until resuming")
    sleep(30)
    print("waiting .5 more minutes until resuming")
    sleep(30)
    print("resuming")
    if float(pullandprocess.returnLatestRsi(timeframeofdata, symbol, datalimit).strip("\n")) > float(lowerthanrsi):
        print("RSI value has been met, selling at yesterdays close price")
        priceAtClose = pullandprocess.returnClosingVal(timeframeofdata, symbol, datalimit).strip("\n")
        create_order_limit(symbol, amount, 'sell', 'limit', 'day', '{}'.format(priceAtClose))
        print("Selling {} of {}, type {} {} {} at {}".format(amount, symbol, 'limit', 'sell', ordergoodfor, priceAtClose))
    else:
        print("RSI value to sell has not been met, taking 1.6% profit for the day")
        priceAtClose = pullandprocess.returnClosingVal(timeframeofdata, symbol, datalimit).strip("\n")
        priceToSell = float(priceAtClose) * float(profitpercentage)
        #print(price)
        create_order_limit(symbol, amount, 'sell', 'limit', 'day', '{}'.format(priceToSell))
        print("Selling {} of {}, type {} {} {} at {}".format(amount, symbol, 'limit', 'sell', ordergoodfor, priceToSell))
#makeLimitOrderIfRSIUp('1D', 'CLSK', '1000', '100', '45', 'day')

while True:
    
	# thing to run
    makelimitorderiflowrsi('1Min', 'SPY', '300', '1', '35', 'day', '1.03')
    sleep(30)

