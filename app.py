# -*- coding:utf8 -*-
import time
import codecs
import tweepy

# Sustituir <Falta> por las credenciales de tu app de twitter
CONSUMER_KEY = "<Falta>"
CONSUMER_SECRET = "<Falta>"
ACCESS_KEY = "<Falta>"
ACCESS_SECRET = "<Falta>"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth)
try:
	with codecs.open('tweetsLog.txt', 'r+', 'utf-8') as tweetsLog:
		tweets = tweetsLog.readlines()

	for tweet in tweets:
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
