import sys
import time

import pyspark
import pyspark.streaming

import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import socket
import json
import logging
import csv

#Twitter API credentials
CONSUMER_KEY = 'tOpKHcNzNpu88PSZxAzCI87Ne'
CONSUMER_SECRET = 'EhSEN89oydJi058EkQP3iMjsVlYw6yLYZ2Uq2UAVSWS43wXju9'
ACCESS_TOKEN = '37501551-hUS1bgjvyBq9H1pplnXkQb1rBIqNfNzPsBHFtx8dw'
ACCESS_SECRET = '0MI19XnM6FXT8D8LWM70KbHYZDp5GefyZpYwD6hUUvtSD'


def get_all_tweets(screen_name):
    #Twitter only allows access to a users most recent 3240 tweets with this method
    
    #authorize twitter, initialize tweepy
    auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    api = tweepy.API(auth)
    
    #initialize a list to hold all the tweepy Tweets
    all_tweets = []  
    
    #make initial request for most recent tweets (200 is the maximum allowed count)
    temp = api.user_timeline(screen_name = screen_name,count=10)
    
    #save most recent tweets
    all_tweets.extend(temp)
    
    #save the id of the oldest tweet less one
    oldest = all_tweets[-1].id - 1
    
    #transform the tweepy tweets into a 2D array that will populate the csv 
    outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in all_tweets]


    #write the csv  
    with open('%s_tweets.csv' % screen_name, 'wb') as f:
        writer = csv.writer(f)
        writer.writerow(["id","created_at","text"])
        writer.writerows(outtweets)
    pass


if __name__ == '__main__':
    #pass in the username of the account you want to download
    get_all_tweets("BarackObama")

