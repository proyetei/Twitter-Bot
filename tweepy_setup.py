import tweepy
import json

f = open("twitterKeys.json")
data = json.load(f)

print(data["keys"]["API_Key"])

api_key = data["keys"]["API_Key"]
api_secret = data["keys"]["API_Key_Secret"]
bearer_token = data["keys"]["Bearer_Token"]
access_token = data["keys"]["Access_Token"]
access_token_secret = data["keys"]["Access_Token_Secret"]

#setup the client
client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)

#may not use this, useful if we need older tweepy version
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

client.create_tweet(text="Hellow Twitter")