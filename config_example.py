#Make a config.py file that has all of this information in it otherwise it will not work
API_KEY = "INSERT YOUR API KEY HERE"
API_KEY_ID = API_KEY
SECRET_KEY = "INSERT YOUR SECRET KEY HERE"
APCA_API_KEY_ID = API_KEY
APCA_SECRET_KEY = SECRET_KEY
api_key = API_KEY_ID
api_secret = SECRET_KEY
HEADERS = {
    'APCA-API-KEY-ID': API_KEY,
    'APCA-API-SECRET-KEY': SECRET_KEY
}
BARS_URL = 'https://data.alpaca.markets/v1/bars'