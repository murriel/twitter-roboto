''' 
Framework for a Twitter Bot 
2020-11
References: 
https://realpython.com/twitter-bot-python-tweepy/
https://www.geeksforgeeks.org/how-to-make-a-twitter-bot-in-python/ 
''' 

import tweepy 
from time import sleep 
from credentials import *
from config import QUERY, FOLLOW, LIKE, SLEEP_TIME, STATS

auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
auth.set_access_token(access_token, access_token_secret) 
api = tweepy.API(auth) 

# Create a tweet
api.update_status(status = STATS)

print("Twitter bot which retweets, like tweets and follow users") 
print("Bot Settings") 
print("Like Tweets :", LIKE) 
print("Follow users :", FOLLOW) 

for tweet in tweepy.Cursor(api.search, q = QUERY).items(): 
	try: 
		sleep(SLEEP_TIME)
		print('\nTweet by: @' + tweet.user.screen_name) 

		tweet.retweet() 
		print('Retweeted the tweet') 

		# Favorite the tweet 
		if LIKE: 
			tweet.favorite() 
			print('Favorited the tweet') 

		# Follow the user who tweeted 
		# check that bot is not already following the user 
		if FOLLOW: 
			if not tweet.user.following: 
				tweet.user.follow() 
				print('Followed the user') 

		sleep(SLEEP_TIME) 

	except tweepy.TweepError as e: 
		print(e.reason) 

	except StopIteration: 
		break
