import tweepy

consumerKey = "YOUR_CONSUMER_KEY"
consumerSecret = "YOUR_CONSUMER_SECRET_KEY"
accessToken = "YOUR_ACCESS_TOKEN"
accessTokenSecret = "YOUR_ACCESS_TOKEN_SECRET"

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
    stream.filter(track=["#Python"])
