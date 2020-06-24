import requests
from pprint import PrettyPrinter
pp = PrettyPrinter()

AppID = "0d298da8"
AppKey = "ecae8ec7c3e3368cf706242e747e466b"

params = {
    "app_id":AppID,
    "app_key":AppKey,
    "format":"json",
    "source":"PNQ",
    "destination":"BOM",
    "dateofdeparture":"20200215",
    "dateofarrival":"",
    "":"",
    "seatingclass":"E",
    "adults":"1",
    "children":"0",
    "counter":"100",  
}

URL = "http://developer.goibibo.com/api/search/"

response = requests.get(URL,params=params).json()
pp.pprint(response)





