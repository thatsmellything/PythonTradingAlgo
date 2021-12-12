import alpaca_trade_api as tradeapi
from config import *



base_url = 'https://paper-api.alpaca.markets'


api = tradeapi.REST(api_key, api_secret, base_url, api_version='v2')

# Get our account information.
account = api.get_account()
#print(account)

# Check if our account is restricted from trading.
if account.trading_blocked:
    print('Account is currently restricted from trading.')

# Check how much money we can use to open new positions.
print('${} is available as buying power.'.format(account.buying_power))