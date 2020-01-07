import tweepy
import time

consumerKey = "YOUR_CONSUMER_KEY"
consumerSecret = "YOUR_CONSUMER_SECRET_KEY"
accessToken = "YOUR_ACCESS_TOKEN"
accessTokenSecret = "YOUR_ACCESS_TOKEN_SECRET"

auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)

followers = []
for page in tweepy.Cursor(api.followers, screen_name='@sudershan60', wait_on_rate_limit=True,count=200).pages():
    try:
        followers.extend(page)
    except tweepy.TweepError as e:
        print("Going to sleep:", e)
        time.sleep(60)

for user in followers:
    try:
        print(user.name)
        tweet = api.user_timeline(id = user.id, count = 1)[0]
        api.create_favorite(tweet.id)
        print('----Liking Tweet-----')
        print(tweet.text)
    except:
        pass