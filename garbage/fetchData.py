from config import *
import requests, json
from datetime import datetime
#timeframe = '1D'  #day or 1D, 5Min, 15Min
#limit = '100' #Limit of days or enmtries to grab, max 1000
#symbols = 'SPY,QQQ,AAPL,CLSK'#Symbols seperated by commas

def pullData(timeframe, symbols, limit):
    day_bars_url = BARS_URL + '/{}?symbols={}&limit={}'.format(timeframe, symbols, limit) #, SPY then others seperated by commas, you can add '&limit=1000' for more data
    r = requests.get(day_bars_url, headers=HEADERS)
    #print(r.content)
    #print(json.dumps(r.json(), indent=4)) #make it much more readable
    data = r.json()
    for symbol in data:
        filename = 'data/{}.txt'.format(symbol)
        f = open(filename, 'w+')
        #print(data['symbol'])
        f.write('Date,Open,High,Low,Close,Volume,OpenInterest\n')
        for bar in data[symbol]:
            #t = datetime.fromtimestamp(bar['t'])
            #day = t.strftime('%Y-%m-%d')
            #print(bar['o'])
            line = '{},{},{},{},{},{},{}\n'.format(bar['t'], bar['o'], bar['h'], bar['l'], bar['c'], bar['v'], 0 )
            #line = '{},{},{},{},{},{},{}\n'.format(bar[1], bar[2], bar[3], bar[4], bar[5], bar[6], 0 )
            #line = '{},{},{},{},{},{},{}\n'.format(bar[0], bar[1], bar[2], bar[3], bar[4], bar[5], 0 )
            f.write(line)
    #f.write(data[symbol])

pullData('1D','TSLA','100')
pullData('1D', 'TR', '100')

