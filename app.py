# -*- coding:utf8 -*-
import time
import tweepy
import credenciales as cc
# Formato de credenciales.py
"""
CONSUMER_KEY = "<Falta>"
CONSUMER_SECRET = "<Falta>"
ACCESS_KEY = "<Falta>"
ACCESS_SECRET = "<Falta>"
"""

auth = tweepy.OAuthHandler(cc.CONSUMER_KEY, cc.CONSUMER_SECRET)
auth.set_access_token(cc.ACCESS_KEY, cc.ACCESS_SECRET)

api = tweepy.API(auth)

try:
	with open('tweetsLog.txt', 'r+') as tweetsLog:
		tweets = tweetsLog.readlines()

	for tweet in tweets[:]:
		tweet = tweet.strip(r'\n')
		if len(tweet)<=140 and len(tweet)>0:
			print ("Hablando: %s" % tweet)
			api.update_status(status=tweet)
			with open ('tweetsLog.txt', 'w') as tweetsLog:
				tweets.remove(tweet)
				tweetsLog.writelines(tweets)
			time.sleep(60*5) #Espera 5 minutos para mandar otro tweet
		else:
			with open ('tweetsLog.txt', 'w') as tweetsLog:
				tweets.remove(tweet)
				tweetsLog.writelines(tweets)
			print ("Te has pasado, tu mensaje tiene más de 140 caracteres.")
			continue
	print ("Hemos terminado...")


except Exception as e:
	print ("Algo pasa: %s" % e)
