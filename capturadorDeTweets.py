#!/usr/bin/python
# -*- coding: utf-8 -*-
import tweepy

#Claves de autenticacion 
consumer_key = "3yNqHrsVSd4n8msKj6a7BpWIA"
consumer_secret = "1NBIAkp3hG0lbQGGraig2AIuxahDwqOTiLA3P2OTAYqggzMjaP"
access_token = "70793170-DZRt56LsQDd5y01xuZL3JSl8WiceEwk981ufrqdXw"
access_token_secret = "ptES1q1alDlxTPD91pwPXAfNkWcOljmVt5rfDbFOYoEq6"

#Este es el api de tweeter para acceder a tweets tomado de cristo 
print('El siguiente script permite ingresar un termino de busqueda y buscarlo en Twitter, pueden ser hashtags\n')
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

try:
	sQuery = tweepy.Cursor(api.search, q=stdin).items(100)
	f = open('data_out.txt', 'w')
	
	for tweet in sQuery:
		f.write(tweet.text.encode('UTF-8')+'\n\n')
		print str(tweet.created_at)+'\n'+tweet.text.encode('UTF-8')+'\n'+str(tweet.lang)+'\n\n'
	f.close()
except tweepy.TweepError:
	print('You have an error on your auth, please check your keys')



