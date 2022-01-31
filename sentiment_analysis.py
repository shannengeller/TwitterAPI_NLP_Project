from ast import keyword
import webbrowser
import tweepy
from textblob import TextBlob
import preprocessor as p
from typing import List
from secret_keys import api_key, api_secret_key
import json 
from requests_oauthlib import OAuth1Session

# new variables to hold keys and things
callback_url = 'oob'
consumer_key = api_key
consumer_secrets = api_secret_key

# logging into my twitter and recieving access and a pin number to make sure its me :)
auth = tweepy.OAuthHandler(consumer_key,consumer_secrets,callback_url)
redirect_url = auth.get_authorization_url()
webbrowser.open(redirect_url)
user_input_code = input("What is the code?")
auth.get_access_token(user_input_code)
api = tweepy.API(auth)

my_timeline = api.user_timeline()
thirty_days = api.search_30_day()
searchQuery = 'Amazon OR AMAZON OR amazon -filter:links'

#searching for a specific type of tweet containing a keyword using Amazon
search_tweets = api.search(q= searchQuery, rpp = 100, lang = 'en', result_type = 'recent')
for tweet in search_tweets:
    print(tweet.full_text)

# reading through all my tweets and cleaning them, and appending to a list
# writing these to a new text document
clean_tweets = []
for tweet in my_timeline:
    clean_tweets.append(tweet.full_text)
    print()


def comp_sci_tweets(clean_tweets):
    return 

