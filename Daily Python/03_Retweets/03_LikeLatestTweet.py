import tweepy
import time

consumerKey = "n5PBzWyLAcf4E2NDHr4uRPHoa"
consumerSecret = "kCBVExRamJz0bga0vSNwu6JP7fnsHDY8zcKvW6fsrar8E8pks7"
accessToken = "2335422042-SPLxm09IZFhtwUBnAZqajQgbhwsj1P7WLuQrvuz"
accessTokenSecret = "kpY77URgsY7RcGnqEkPXC1KcxlIjl5YVLms5MUNq2xBuF"

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