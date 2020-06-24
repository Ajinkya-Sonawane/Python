import requests
import tweepy
import time
import json

def setup_Bot():
    consumerKey = "YOUR_API_KEY"
    consumerSecret = "YOUR_API_KEY_SECRET"
    accessToken = "YOUR_ACCESS_TOKEN"
    accessTokenSecret = "YOUR_ACCESS_TOKEN_SECRET"
    auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
    auth.set_access_token(accessToken, accessTokenSecret)
    api = tweepy.API(auth)
    return api

def get_Quote():
    params = {
        'method':'getQuote',
        'lang':'en',
        'format':'json'
    }
    res = requests.get('http://api.forismatic.com/api/1.0/',params)
    jsonText =json.loads(res.text)
    return jsonText["quoteText"],jsonText["quoteAuthor"]


api = setup_Bot()
while True:
    try:
        quote,author = get_Quote()
        status = quote+" -"+author+"\n"+"#python \
        #dailypython #twitterbot #pythonquotes #programming"
        print('\nUpdating : ',status)
        api.update_status(status=status)
        print("\nGoing to Sleep for 1 min")
        time.sleep(60)
    except Exception as ex:
        print(ex)
        break
    