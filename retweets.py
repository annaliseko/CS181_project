import sys
import time

import pyspark
import pyspark.streaming

# # common setup
# def printItems(items):
#     for item in items:
#         print item.encode('utf-8')
        
# def main():
#     sc = pyspark.SparkContext(master="local[%i]" % 2)
#     sc.setLogLevel("ERROR")
#     ssc = pyspark.streaming.StreamingContext(sc, 10)

#     socket_stream = ssc.socketTextStream("127.0.0.1", 5555)
    
#     lines = socket_stream.window(10)
#     #lines.pprint()
    
#     #hashtags = lines.flatMap(lambda line: line.split(" "))\
#     #                .filter(lambda word: word.lower().startswith('#'))\
#     # hashtags.pprint()                   

#     counts = lines.flatMap(lambda line: line.split(" ")) \
#                   .filter(lambda word: word.lower().startswith("#"))\
#                   .map(lambda word: (word, 1)) \
#                   .reduceByKey(lambda a, b: a+b)\
#                   .transform(lambda rdd: rdd.sortBy(lambda a: a[1],ascending=False))
#     counts.pprint()

#     ssc.start()
#     ssc.awaitTermination()

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

# stores all the tweet ids from the csv file into an array, tweet_id
data = pd.read_csv('BarackObama_tweets.csv')
tweet_id = data.id

