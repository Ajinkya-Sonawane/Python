api_key = "YOUR_API_KEY"

from apiclient.discovery import build

youtube = build('youtube','v3',developerKey = api_key)
print(type(youtube))

request = youtube.search().list(q='Countless Storeys',part='snippet',type='video')
print(type(request))

res = request.execute()
from pprint import PrettyPrinter
pp = PrettyPrinter()
pp.pprint(res)

#Print the total number of results
request = youtube.search().list(q='Countless Storeys',part='snippet',type='video',maxResults=50)
res = request.execute()
print('Total items : ',len(res['items']))

#Print the title
request = youtube.search().list(q='Countless Storeys',part='snippet',type='video')
res = request.execute()
for item in res['items']:
    print(item['snippet']['title'])


#Search for channel
request = youtube.search().list(q='Countless Storeys',part='snippet',type='channel')
res = request.execute()
for item in res['items']:
    pp.pprint(item['snippet'])

# Search content by channel
channelId = 'UCoEAf0U-QUWl9TeMZSC8D3w'
request = youtube.search().list(q='Countless Storeys',part='snippet',type='video',channelId=channelId)
res = request.execute()
for item in res['items']:
    pp.pprint(item['snippet'])