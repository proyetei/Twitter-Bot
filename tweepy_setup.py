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

#How to create a tweet
#client.create_tweet(text="Hellow Twitter")

#How to like a tweet
#client.like(<The tweet ID>) the tweet ID is the bunch of numbers in the twitter post link

#How to retweet a tweet
#client.retweet(<The tweet ID>) the tweet ID is the bunch of numbers in the twitter post link

#How to reply to a tweet
#client.create_tweet(in_reply_to_tweet_id=<The tweet ID>, text = "This is the what reply would be")

#How to scan for tweets in our timeline

for tweet in api.home_timeline():
    print(tweet.text)


