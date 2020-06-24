#Import requests module
import requests

#Import Pretty Printer module
from pprint import PrettyPrinter
pp = PrettyPrinter()

#Store the API Token
api_token = 'zlI4jkX6AA2REJ6HcgI6V58UIioxDwahyUKokvqtB9xDhJoyBtd9V06QhLNf'

#Fetch Stock Data
url = 'https://api.worldtradingdata.com/api/v1/stock'
params = {
    'symbol':'GOOGL',
    'api_token':api_token,
}
response = requests.request('GET',url,params=params)
pp.pprint(response.json())

#Fetch Mutual Fund Data
url = 'https://api.worldtradingdata.com/api/v1/mutualfund'
params = {
  'symbol': 'AAAAX,AAAGX',
  'api_token': api_token
}
response = requests.request('GET', url, params=params)
pp.pprint(response.json())

#Fetch Intraday Stock Data 
url = 'https://intraday.worldtradingdata.com/api/v1/intraday'
params = {
  'symbol': 'GOOGL',
  'api_token': api_token,
  'interval': '1',
  'range': '1'
}
response = requests.request('GET', url, params=params)
pp.pprint(response.json())

#Fetch Real-Time Forex Data
url = 'https://api.worldtradingdata.com/api/v1/forex'
params = {
  'base': 'INR',
  'api_token': api_token
}
response = requests.request('GET', url, params=params)
print(response.json())

#Fetch Historical Market Data
url = 'https://api.worldtradingdata.com/api/v1/history'
params = {
  'symbol': 'GOOGL',
  'api_token': api_token,
  'date_from':'2020-01-08',
  'date_to':'2020-01-14'
}
response = requests.request('GET', url, params=params)
pp.pprint(response.json())