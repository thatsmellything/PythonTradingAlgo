import alpaca_trade_api as tradeapi
from config import *
# authentication and connection details

base_url = 'https://paper-api.alpaca.markets'

# instantiate REST API
api = tradeapi.REST(api_key, api_secret, base_url, api_version='v2')

# obtain account information
account = api.get_account()
print(account)


