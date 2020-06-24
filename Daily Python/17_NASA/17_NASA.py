#NASA API Consumption
import requests
from urllib.request import urlretrieve
from pprint import PrettyPrinter
pp = PrettyPrinter()


api_key = "YOUR_NASA_API_KEY"

def fetchAPOD():
  URL_APOD = "https://api.nasa.gov/planetary/apod"
  date = '2020-01-23'
  params = {
      'api_key':api_key,
      'date':date,
      'hd':'True'
  }
  response = requests.get(URL_APOD,params=params).json()
  pp.pprint(response)

fetchAPOD()

def fetchAsteroidNeowsFeed():
  URL_NeoFeed = "https://api.nasa.gov/neo/rest/v1/feed"
  params = {
      'api_key':api_key,
      'start_date':'2020-01-22',
      'end_date':'2020-01-23'
  }
  response = requests.get(URL_NeoFeed,params=params).json()
  pp.pprint(response)

fetchAsteroidNeowsFeed()

def fetchAsteroidNeowsLookup():
  asteroid_id = '3542519'
  URL_NeoLookup = "https://api.nasa.gov/neo/rest/v1/neo/"+ asteroid_id
  params = {
      'api_key':api_key
  }
  response = requests.get(URL_NeoLookup,params=params).json()
  pp.pprint(response)

fetchAsteroidNeowsLookup()

def fetchAsteroidNeowsBrowse():
  URL_NeoBrowse = "https://api.nasa.gov/neo/rest/v1/neo/browse/"
  params = {
      'api_key':api_key
  }
  response = requests.get(URL_NeoBrowse,params=params).json()
  pp.pprint(response)

fetchAsteroidNeowsBrowse()

def fetchEPICData():
  URL_EPIC = "https://api.nasa.gov/EPIC/api/natural/"
  params = {
      'api_key':api_key,
  }
  response = requests.get(URL_EPIC,params=params).json()
  pp.pprint(response)

fetchEPICData()

def fetchEPICImage():
  YEAR = '2015'
  MONTH = '10'
  DAY = '31'
  IMAGE_ID = 'epic_1b_20151031074844'
  URL_EPIC = "https://epic.gsfc.nasa.gov/archive/natural/"
  URL_EPIC = URL_EPIC + YEAR +'/' + MONTH + '/'+DAY
  URL_EPIC = URL_EPIC + '/png'
  URL_EPIC = URL_EPIC + '/' + IMAGE_ID + '.png' 
  print(URL_EPIC)
  urlretrieve(URL_EPIC,IMAGE_ID+'.png')

fetchEPICImage()