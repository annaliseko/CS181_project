import sys
import time

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
    alltweets = []  
    
    #make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name = screen_name,count=20)
    
    #save most recent tweets
    alltweets.extend(new_tweets)
    
    #save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1
    
    #keep grabbing tweets until there are no tweets left to grab
    # while len(alltweets) < 201 :
    #     print "%s" % (alltweets[-1].id)
        
    #     print "getting tweets before %s" % (oldest)
        
    #     #all subsiquent requests use the max_id param to prevent duplicates
    #     new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
    #     if new_tweets==[]:
    #         break
    #     #save most recent tweets
    #     alltweets.extend(new_tweets)
        
    #     #update the id of the oldest tweet less one
    #     oldest = alltweets[-1].id - 1
        
    #     print "...%s tweets downloaded so far" % (len(alltweets))
        
    
    #transform the tweepy tweets into a 2D array that will populate the csv 
    outtweets = [[tweet.id_str, tweet.text.encode("utf-8")] for tweet in alltweets]
    
    #write the csv  
    with open('%s_tweets.csv' % screen_name, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(["id","text"])
        writer.writerows(outtweets)
    
    pass


if __name__ == '__main__':
    #pass in the username of the account you want to download
    get_all_tweets("BarackObama")
    get_all_tweets("BernieSanders")
    get_all_tweets("realDonaldTrump")
    get_all_tweets("SenWarren")
    get_all_tweets("BetsyDeVosED")
    get_all_tweets("HillaryClinton")
    get_all_tweets("JoeBiden")
    get_all_tweets("MittRomney")
    get_all_tweets("PRyan")
    get_all_tweets("mike_pence")

