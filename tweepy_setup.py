from logging import exception
import tweepy
import json
import time

f = open("twitterKeys.json")
data = json.load(f)

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
#client.like(<The Tweet ID>)

#How to retweet a tweet
#client.retweet(<The tweet ID>) the tweet ID is the bunch of numbers in the twitter post link

#How to reply to a tweet
#client.create_tweet(in_reply_to_tweet_id=<The tweet ID>, text = "This is the what reply would be")

#How to scan for tweets in our timeline
'''
for tweet in api.home_timeline():
    print(tweet.text)
'''

#How to get a certain users id
#person = client.get_user(username="Mohsinxn1").data.id

#get a users tweets
'''
for tweet in client.get_users_tweets(person).data:
    print(tweet.text)
'''

#How to scan all tweets and print a tweet with a keyword
'''
searchTerms = ["Python"]

class MyStream(tweepy.StreamingClient):
    def on_connect(self):
        print("Connected")

    def on_tweet(self, tweet):
        if tweet.referenced_tweets == None:
            print(tweet.text)

            time.sleep(0.2)

stream = MyStream(bearer_token)

for term in searchTerms:
    stream.add_rules(tweepy.StreamRule(term))

stream.filter(tweet_fields=["referenced_tweets"])
'''


#THE CODE BELOW REPLIES TO TWEETS I HAVE BEEN TAGGED IN
message = "I have been tagged"
#our ID
client_id = client.get_me().data.id
start_id = 1
initialisation_resp = client.get_users_mentions(client_id)
if initialisation_resp.data != None:
    start_id = initialisation_resp.data[0].id

#this loop will look for tweets that mention me
while True:
    #search for tweets that mention me
    response = client.get_users_mentions(client_id, since_id=start_id)
    #check if response is not empty
    if response.data != None:
        for tweet in response.data:
            try:
                print(tweet.text)
                client.create_tweet(in_reply_to_tweet_id=tweet.id, text=message)
                start_id = tweet.id
            except Exception as error:
                print(error)
                pass
    time.sleep(2)