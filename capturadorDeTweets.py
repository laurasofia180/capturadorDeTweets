#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
import tweepy,csv

#Claves de autenticacion
consumer_key = "3yNqHrsVSd4n8msKj6a7BpWIA"
consumer_secret = "1NBIAkp3hG0lbQGGraig2AIuxahDwqOTiLA3P2OTAYqggzMjaP"
access_token = "70793170-DZRt56LsQDd5y01xuZL3JSl8WiceEwk981ufrqdXw"
access_token_secret = "ptES1q1alDlxTPD91pwPXAfNkWcOljmVt5rfDbFOYoEq6"

#Appi de tweetpy para coger datos de tweeter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

print('El siguiente script permite ingresar un termino de busqueda y buscarlo en Twitter, pueden ser hashtags\n')
stdin = (raw_input('Ingrese el termino de busqueda :\n'))
stdin.encode('UTF-8')
try:
    os.remove("mycsvfile.csv")
except OSError:
    pass

try:
	sQuery = tweepy.Cursor(api.search, q=stdin, geocode="6.2690007,-75.7364814,1000km",show_user=True).items(10)
	writedHeader = True
	for tweet in sQuery:

		tweet_data = {}
		tweet_data["texto"] = tweet._json["text"].encode("UTF-8")
		tweet_data["id"] = tweet._json["id"]
		tweet_data["lang"] = tweet._json["lang"].encode("UTF-8")

	with open('mycsvfile.csv', 'a') as f:
	      w = csv.DictWriter(f, tweet_data.keys())
	      if writedHeader:
	        w.writeheader()
	        writedHeader = False
	      w.writerow(tweet_data)
except tweepy.TweepError:
	print('You have an error on your auth, please check your keys')
