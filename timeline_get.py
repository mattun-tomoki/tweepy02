#画像検索して保存
import tweepy
import datetime
import urllib.request as req
import urllib.error as er
from tweet_api_key import tw_api_key

key = []
for number in range(4):
	key.append(tw_api_key(number))

auth = tweepy.OAuthHandler(key[0], key[1])
auth.set_access_token(key[2], key[3])
api = tweepy.API(auth)

for tweet in api.home_timeline(count=10)[::-1]:
	print('------------------------------------------------------------------')
	print(tweet.text)
