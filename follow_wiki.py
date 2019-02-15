#!/usr/bin/python3
import tweepy
from time import sleep
from credentials import *

# Access and authorize our Twitter credentials from credentials.py
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# For loop to iterate over tweets with #ocean, limit to 10
for tweet in tweepy.Cursor(api.search,
                           q='#wikipedia').items(5000):

    try:
        # Favorite the tweet
        tweet.favorite()
        print('Favorited the tweet')

        # Follow the user who tweeted
        if not tweet.user.following:
            tweet.user.follow()
            print('Followed @' + tweet.user.screen_name)

    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
