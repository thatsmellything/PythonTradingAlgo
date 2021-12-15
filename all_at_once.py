from config import *
import requests, json
from datetime import datetime
import alpaca_trade_api as tradeapi
from config import *

###FIRST PRINT ACCOUNT INFO TO MAKE SURE WE HAVE A CONNECTION###
def print_account_information():
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
        print('Market is open.')
        return True
    else:
        print('Market is closed.')
        return False
check_trading_hours()



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

###FORMAT DATA .txt INTO .csv###
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
format_data('SPY')
#NEED TO ADD MACD AND RSI TO CSV