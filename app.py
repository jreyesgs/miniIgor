# -*- coding:utf8 -*-
import tweepy

CONSUMER_KEY = "<Falta>"
CONSUMER_SECRET = "<Falta>"
ACCESS_KEY = "<Falta>"
ACCESS_SECRET = "<Falta>"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth)
"""
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text.encode("utf-8"))
"""
try:
	with open('hablando.txt', 'r+') as tweetsLog:
		tweets = tweetsLog.readlines()

	for tweet in tweets[:]:
		tweet = tweet.strip(r'\n')
		if len(tweet)<=140 and len(tweet)>0:
			print ("Hablando...")
			twitter.update_status(status=tweet)
			with open ('hablando.txt', 'w') as tweetsLog:
				tweets.remove(tweet)
				tweetsLog.writelines(tweets)
			time.sleep(900)
		else:
			with open ('hablando.txt', 'w') as tweetsLog:
				tweets.remove(tweet)
				tweetsLog.writelines(tweets)
			print ("Te has pasado, tu mensaje tiene más de 140 caracteres.")
			continue
	print ("Hemos terminado...")


except Exception as e:
	print (e)
