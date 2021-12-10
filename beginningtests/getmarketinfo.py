import alpaca_trade_api as tradeapi
from config import *
# authentication and connection details


base_url = 'https://paper-api.alpaca.markets'


api = tradeapi.REST(api_key, api_secret, base_url, api_version='v2')

# Get daily price data for AAPL over the last 5 trading days.
barset = api.get_barset('AAPL', 'day', limit=5)
aapl_bars = barset['AAPL']

# See how much AAPL moved in that timeframe.
week_open = aapl_bars[0].o
week_close = aapl_bars[-1].c
percent_change = (week_close - week_open) / week_open * 100
print('AAPL moved {}% over the last 5 days'.format(percent_change))