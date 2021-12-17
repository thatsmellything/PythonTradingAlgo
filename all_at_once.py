from config import *
import requests, json
from datetime import datetime
import alpaca_trade_api as tradeapi
from config import *
import btalib
import pandas as pd
from time import time, sleep
import sys


###FIRST PRINT ACCOUNT INFO TO MAKE SURE WE HAVE A CONNECTION###
def print_account_information():
    print('\n')
    print('Account Information:')
    base_url = 'https://paper-api.alpaca.markets'
    api = tradeapi.REST(api_key, api_secret, base_url, api_version='v2')
    # Get our account information.
    account = api.get_account()
    print(account)
    # Check if our account is restricted from trading.
    if account.trading_blocked:
        print('Account is currently restricted from trading.')
    # Check how much money we can use to open new positions.
    print('${} is available as buying power.'.format(account.buying_power))
print_account_information()


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
#check_trading_hours()



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

#pull_data('1D','SPY','100')
#pull_data('1Min', 'TR', '1000')

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

#NEED TO ADD MACD AND RSI TO CSV
def get_indicators(symbol):
    df = pd.read_csv("data/{}.txt".format(symbol), parse_dates=True, index_col=0)
    #print(df)
    sma = btalib.sma(df)
    rsi = btalib.rsi(df)
    #macd = btalib.macd(df)
    
    
    df['sma'] = sma.df
    rsi = btalib.rsi(df)
    df['rsi'] = rsi.df
    #df['macd'] = macd.df
    
    #print(df)
    df.to_csv('data/{}.csv'.format(symbol), index=True)

    ##THESE DO NOT WORK FOR NOW##
    #macd = btalib.macd(df)
    #print(macd)
    #rsi = btalib.rsi(df) #period default is 14, rsi = btalib.rsi(df, period = 10)
    #signal = btalib.macd_signal(df)
    #histogram = btalib.macd_histogram(df)
    
    #df['macd'] = macd.df
    #df['signal'] = signal.df
    #df['histogram'] = histogram.df
    #df['rsi'] = rsi.df


    return df
#get_indicators('SPY')

###GRAB THE LAST ENTRY OF THE CSV FILE###
def get_last_entry(symbol):
    with open("data/" + symbol + ".csv", 'r') as file:
        data = file.readlines() 
    lastRow = data[-1]
    return lastRow
#print(get_last_entry('SPY'))

###RETURN LATEST INDICATORS###

###GET RSI###
def get_rsi(symbol):
    date, open_value, high_value, low_value, closing_value, volume, sma, rsi  = get_last_entry(symbol).split(',')
    print("RSI value of {} is {}".format(symbol, rsi.strip("\n")))
    return rsi
#get_rsi('SPY')
###GET Closing Value###
def get_closing_value(symbol):
    date, open_value, high_value, low_value, closing_value, volume, sma, rsi  = get_last_entry(symbol).split(',')
    #print(closing_value)
    return closing_value
#get_closing_value('SPY')
###GET SMA###
def get_sma(symbol):
    date, open_value, high_value, low_value, closing_value, volume, sma, rsi  = get_last_entry(symbol).split(',')
    #print(sma)
    return sma
#get_sma('SPY')
###GET Volume###
def get_volume(symbol):
    date, open_value, high_value, low_value, closing_value, volume, sma, rsi  = get_last_entry(symbol).split(',')
    #print(volume)
    return volume
#get_volume('SPY')
###GET Open Value###
def get_open_value(symbol):
    date, open_value, high_value, low_value, closing_value, volume, sma, rsi  = get_last_entry(symbol).split(',')
    #print(open_value)
    return open_value
#get_open_value('SPY')
###GET High Value###
def get_high_value(symbol):
    date, open_value, high_value, low_value, closing_value, volume, sma, rsi  = get_last_entry(symbol).split(',')
    #print(high_value)
    return high_value
#get_high_value('SPY')
###GET Low Value###
def get_low_value(symbol):
    date, open_value, high_value, low_value, closing_value, volume, sma, rsi  = get_last_entry(symbol).split(',')
    #print(low_value)
    return low_value
#get_low_value('SPY')
###GET Date###
def get_date(symbol):
    date, open_value, high_value, low_value, closing_value, volume, sma, rsi  = get_last_entry(symbol).split(',')
    #print(date)
    return date
#get_date('SPY')




###CREATE A LIMIT ORDER###
def create_limit_order(symbol, qty, side, type, time_in_force, limit_price):
    BASE_URL = "https://paper-api.alpaca.markets"
    ACCOUNT_URL = "{}/v2/account".format(BASE_URL)
    ORDERS_URL = "{}/v2/orders".format(BASE_URL)
    HEADERS = {'APCA-API-KEY-ID': API_KEY_ID, 'APCA-API-SECRET-KEY': SECRET_KEY}
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

###CHECK RSI LEVELS AND SELL ORDER IF ABOVE THRESHOLD###
def make_limit_sell_order_if_rsi_high(symbol, amount, rsi_value, profit_percentage, buy_price):
    order_good_for = 'gtc'
    ##print countdown timer of 5 min by 30 second intervals
    for i in range(1,6):
        print(i)
        sleep(30)
    print('Checking if RSI is higher than {} on ticker {}'.format(rsi_value, symbol))
    if float(get_rsi(symbol).strip("\n")) > float(rsi_value):
        print("RSI value has been met, selling at yesterdays close price")
        price_at_close = get_closing_value.strip("\n")
        create_limit_order(symbol, amount, 'sell', 'limit', 'gtc', '{}'.format(price_at_close))
        print("Selling {} of {}, type {} {} {} at {}".format(amount, symbol, 'limit', 'sell', order_good_for, price_at_close))
    else:
        print("RSI value to sell has not been met, taking {}% profit for the day".format(profit_percentage))
        price_at_close = get_closing_value(symbol).strip("\n")
        price_to_sell = float(buy_price) * (float('1.0'+ profit_percentage))
        #print(price)
        create_limit_order(symbol, amount, 'sell', 'limit', 'gtc', '{}'.format(price_to_sell))
        print("Selling {} of {}, type {} {} {} at {}".format(amount, symbol, 'limit', 'sell', order_good_for, price_to_sell))
#makeLimitOrderIfRSIUp('1D', 'CLSK', '1000', '100', '45', 'day')

###CHECK RSI LEVELS AND BUY ORDER IF BELOW THRESHOLD###
def make_limit_buy_order_if_low_rsi(symbol, amount, low_rsi_value, high_rsi_value, profit_percentage):
    order_good_for = 'day'
    
    print('Checking if RSI is lower than {} on ticker {}'.format(low_rsi_value, symbol))
    if float(get_rsi(symbol).strip("\n")) < float(low_rsi_value):
        price = get_closing_value(symbol).strip("\n")
        print(price)
        create_limit_order(symbol, amount, 'buy', 'limit', order_good_for, '{}'.format(price))
        price = (float(price) * 1.005) #add 0.5% to price to make sure it is bought
        print("Buying {} of {}, type {} {} at {}".format(amount, symbol, 'limit', order_good_for, price))
        #profit_percentage = 1 + float(profit_percentage)
        make_limit_sell_order_if_rsi_high(symbol, amount, high_rsi_value, '{}'.format(profit_percentage), price)

       
    else:

        print("RSI value is not below {}, not buying any stocks\n".format(low_rsi_value))
#make_limit_buy_order_if_low_rsi('SPY', 1, '35')



###FUNCTION TO LOOP###
def loop_me(data_timeframe, symbol, data_size, order_amount, low_rsi_value, high_rsi_value, profit_percentage):
    pull_data(data_timeframe, symbol, data_size)
    get_indicators(symbol)
    make_limit_buy_order_if_low_rsi(symbol, order_amount, low_rsi_value, high_rsi_value, profit_percentage)


###MAIN###
def run():
    while check_trading_hours() == True:
        loop_me(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7])
        sleep(30)
    else:
        print("Not trading hours")
        sleep(300)
        run()

### GET INPUT ARGS FROM USER###
print("Order of arguments is: data timeframe, symbol, data size, order amount, low rsi value, high rsi value, profit percentage (6 would be a 6 percent gain)")
list_of_arguments = sys.argv
if len(list_of_arguments) == 8:
    run()
else:
    print("Not enough arguments or too many, please try again")
    print("Order of arguments is: data timeframe, symbol, data size, order amount, low rsi value, high rsi value, profit percentage (6 would be a 6 percent gain)")

