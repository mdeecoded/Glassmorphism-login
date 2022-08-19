import requests,time
import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

from datetime import datetime

def datetotimestamp(date):
    time_tuple = date.timetuple()
    timestamp = round(time.mktime(time_tuple))
    return timestamp

def timestamptodate(timestamp):
   return datetime.fromtimestamp(timestamp)


start = datetotimestamp(datetime(2022,1,1))
end = datetotimestamp(datetime.today())
url = 'https://priceapi.moneycontrol.com/globaltechCharts/crypto/history?symbol=btcusdt&resolution=15&from='+str(start)+'&to='+str(end)+''


resp = requests.get(url).json()
data = pd.DataFrame(resp)
date = []
for dt in data['t']:
    date.append({'Date':timestamptodate(dt)})

dt = pd.DataFrame(date)

intraday15 = pd.concat([dt , data['o'],data['h']], axis=1)\
    .rename(columns={'o':'Open','h':'HighPrice'})


print(intraday15)