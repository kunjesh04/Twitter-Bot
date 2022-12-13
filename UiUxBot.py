import tweepy
from Keys.keys import keys

my_keys = keys()

API_KEY = my_keys.API_KEY
API_KEY_SECRET = my_keys.API_KEY_SECRET

BEARER_TOKEN = my_keys.BEARER_TOKEN

ACCESS_TOKEN = my_keys.ACCESS_TOKEN
ACCESS_TOKEN_SECRET = my_keys.ACCESS_TOKEN_SECRET

CLIENT_ID = my_keys.CLIENT_ID
CLIENT_SECRET = my_keys.CLIENT_SECRET

client = tweepy.Client(BEARER_TOKEN, API_KEY, API_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)


auth = tweepy.OAuthHandler(API_KEY, API_KEY_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth, wait_on_rate_limit=True)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")



class MyStream(tweepy.StreamingClient):
    def on_tweet(self, tweet):
        print(tweet.text)
        try:
            client.like(tweet.id)
            print("Tweet Linked")
            client.retweet(tweet.id)
            print("Tweet Retweeted")
        except Exception as error:
            print(error)


stream = MyStream(bearer_token=BEARER_TOKEN)

rule = tweepy.StreamRule("(#100DaysOfUiUx OR #UiUxDesign) (-is:retweet -is:reply)")

stream.add_rules(rule)

stream.filter()
