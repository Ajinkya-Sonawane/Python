import tweepy

consumerKey = "n5PBzWyLAcf4E2NDHr4uRPHoa"
consumerSecret = "kCBVExRamJz0bga0vSNwu6JP7fnsHDY8zcKvW6fsrar8E8pks7"
accessToken = "2335422042-SPLxm09IZFhtwUBnAZqajQgbhwsj1P7WLuQrvuz"
accessTokenSecret = "kpY77URgsY7RcGnqEkPXC1KcxlIjl5YVLms5MUNq2xBuF"


class TwitterStreamListener(tweepy.streaming.StreamListener):
    ''' Handles data received from the stream. '''
    def on_status(self, status):
        print(status.id)
        print(status.user.name)
        print(status.text)
        return True
 
    def on_error(self, status_code):
        print('Got an error with status code: ' + str(status_code))
        return True # To continue listening
 
    def on_timeout(self):
        print('Timeout...')
        return True # To continue listening
    
if __name__ == '__main__':
    listener = TwitterStreamListener()
    auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
    auth.set_access_token(accessToken, accessTokenSecret)
    stream = tweepy.streaming.Stream(auth, listener)
    stream.filter(track=["#WWIII"])
