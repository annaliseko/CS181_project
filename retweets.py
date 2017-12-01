import sys
import time

import pyspark
import pyspark.streaming

import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import pandas as pd
import socket
import json
import logging
import csv

#Twitter API credentials
CONSUMER_KEY = 'tOpKHcNzNpu88PSZxAzCI87Ne'
CONSUMER_SECRET = 'EhSEN89oydJi058EkQP3iMjsVlYw6yLYZ2Uq2UAVSWS43wXju9'
ACCESS_TOKEN = '37501551-hUS1bgjvyBq9H1pplnXkQb1rBIqNfNzPsBHFtx8dw'
ACCESS_SECRET = '0MI19XnM6FXT8D8LWM70KbHYZDp5GefyZpYwD6hUUvtSD'

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tweepy.API(auth)

# stores all the tweet ids from the csv file into an array, tweet_id
data = pd.read_csv('BarackObama_tweets.csv')
tweet_id = data.id

# stores all the retweet ids and original tweet to a new csv file
with open('retweets.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerow(["user", "user location", "time zone", "geo enabled", "coordinates", "text"])

    # need to potentially calculate coordinates of tweet???
    for x in range(len(tweet_id)):
        retweetTemp = api.retweets(id = tweet_id[x], count = 100)
        retweets = [[retweet.user.id_str, retweet.user.location.encode("utf-8"), retweet.user.time_zone, retweet.user.geo_enabled, retweet.coordinates, retweet.text.encode("utf-8")] for retweet in retweetTemp]
        writer.writerows(retweets)
pass
