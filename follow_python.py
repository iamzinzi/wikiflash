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
                           q='#python').items(200):

    try:
        # Favorite the tweet
        if not tweet.favorited:
            tweet.favorite()
            print('Favorited the tweet')
        else:
            print('Tweet already favorited')

        # Follow the user who tweeted
        if not tweet.user.following:
            tweet.user.follow()
            print('Followed @' + tweet.user.screen_name)

        sleep(3)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
