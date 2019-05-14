import tweepy
from tweet_api_key import tw_api_key

key = []
for number in range(4):
	key.append(tw_api_key(number))

auth = tweepy.OAuthHandler(key[0], key[1])
auth.set_access_token(key[2], key[3])
#screen_name = 'domain of twitter'
screen_name = '******'

api = tweepy.API(auth)
user_info = api.get_user(screen_name=screen_name)

name = user_info.name
screen_name = user_info.screen_name
description = user_info.description
image_url = user_info.profile_image_url_https
follow_count = user_info.friends_count
follower_count = user_info.followers_count

print('<名前> {}\n <アカウント名> {}\n <自己紹介> {}\n <画像URL> {}\n <フォロー数> :{}\n <フォロワー数> :{}\n'
	.format(name, screen_name,description,image_url,follow_count,follower_count))