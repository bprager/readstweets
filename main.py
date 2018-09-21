#!/usr/bin/env python3
# -*- coding: utf-8 -*

#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Import my credentials
import credentials

#Variables that contains the user credentials to access Twitter API 
access_token = credentials.access_token
access_token_secret = credentials.access_token_secret
consumer_key = credentials.consumer_key
consumer_secret = credentials.consumer_secret

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)

def main():
    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['python', 'javascript', 'ruby'])
    return

if __name__ == '__main__':
    main()
