import requests
from pprint import PrettyPrinter
pp = PrettyPrinter()

apiKey = 'YOUR_OMDb_API_Key' 

#Fetch Movie Data
data_URL = 'http://www.omdbapi.com/?apikey='+apiKey
year = ''
movieTitle = 'Fast & Furious'
params = {
    's':movieTitle,
    'type':'movie',
    'y':year    
}

response = requests.get(data_URL,params=params).json()
pp.pprint(response)



#Fetch Series Data
data_URL = 'http://www.omdbapi.com/?apikey='+apiKey
year = ''
series = 'Friends'
params = {
    't':series,
    'plot':'full',
    'type':'series',
    'y':year    
}

response = requests.get(data_URL,params=params).json()
pp.pprint(response)


#Fetch Movie with Full Plot  Data
data_URL = 'http://www.omdbapi.com/?apikey='+apiKey
year = ''
movie = 'Fast & Furious' 
params = {
    't':movie,
    'type':'movie',
    'y':year,
    'plot':'full'
}

response = requests.get(data_URL,params=params).json()
pp.pprint(response)