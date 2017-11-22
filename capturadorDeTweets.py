#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys,re,json
import tweepy,csv,os

#Claves de autenticacion
consumer_key = "3yNqHrsVSd4n8msKj6a7BpWIA"
consumer_secret = "1NBIAkp3hG0lbQGGraig2AIuxahDwqOTiLA3P2OTAYqggzMjaP"
access_token = "70793170-DZRt56LsQDd5y01xuZL3JSl8WiceEwk981ufrqdXw"
access_token_secret = "ptES1q1alDlxTPD91pwPXAfNkWcOljmVt5rfDbFOYoEq6"

#Appi de tweetpy para coger datos de tweeter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#Obtiene lo que se quiere buscar
print('El siguiente script permite ingresar un termino de busqueda y buscarlo en Twitter, pueden ser hashtags\n')
stdin = (raw_input('Ingrese el termino de busqueda :\n'))
stdin.encode('UTF-8')
#Esto quita el archivo si ya existe
#try:
    #os.remove("mycsvfile.csv")
#except OSError:
    #pass

try:
    #Crea el set de tweets dependiendo de lo que se busco
    sQuery = tweepy.Cursor(api.search, q=stdin, geocode="6.2690007,-75.7364814,100km",show_user=True).items(10)
    writedHeader = True
    for tweet in sQuery:
        stdin=stdin.replace(" ", "-")
        #Creo el tweet como un diccionario
        tweet_data = {}
        tweet_data["texto"] = tweet._json["text"].encode("UTF-8")
        tweet_data["id"] = tweet._json["id"]
        tweet_data["lang"] = tweet._json["lang"].encode("UTF-8")
        print json.dumps(tweet._json)
		#Abro el csv y le hago append de ese tweet, solo escribo el header la primera vez mediante la variable de control
        with open(stdin+'_dataset.csv', 'a') as f:
			#El header seran las keys de ese tweet (que son las mismas para todos los tweets)
            w = csv.DictWriter(f, tweet_data.keys())
            if writedHeader:
                w.writeheader()
                writedHeader = False
            w.writerow(tweet_data)
except tweepy.TweepError:
    print('You have an error on your auth, please check your keys')
#Metodo clasificar
