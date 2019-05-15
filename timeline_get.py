#画像検索して保存
import tweepy
import datetime
import urllib.request as req
import urllib.error as er
from tweet_api_key import tw_api_key

# key = []
# for number in range(4):
# 	key.append(tw_api_key(number))

# auth = tweepy.OAuthHandler(key[0], key[1])
# auth.set_access_token(key[2], key[3])
# api = tweepy.API(auth)

# for tweet in api.home_timeline(count=100)[::-1]:
# 	print('------------------------------------------------------------------')
# 	print(tweet.text)
IMAGES_DIR = './images/'
KEYWORDS = ['缶詰少女','オトメドメイン']

#検索オプション
RETURN_PAR_PAGE = 100
NUMBER_OF_PAGES = 10

class ImageDownloder(object):
	def __init__(self):
		super(ImageDownloder, self).__init__()
		self.set_twitter_api()
		self.media_url_list = []

	def run(self):
		for keyword in KEYWORDS:
			self.max_id = None
			for page in range(NUMBER_OF_PAGES):
				self.download_url_list = []
				self.search(keyword, RETURN_PAR_PAGE)
				for url in self.download_url_list:
					print(url)
					self.download(url)

	def  set_twitter_api(self):
		try:
			key = []
			for number in range(4):
				key.append(tw_api_key(number))

			auth = tweepy.OAuthHandler(key[0], key[1])
			auth.set_access_token(key[2], key[3])
			self.api = tweepy.API(auth)
		except Exception as e:
			print("[+] Error: ",e)
			self.api = None

	def  search(self, term, rpp):
		try:
			if self.max_id:
				search_result = self.api.search(q=term,rpp=rpp,max_id=self.max_id)
			else:
				search_result = self.api.search(q=term,rpp=rpp)

			for result in search_result:
				if 'media' in result.entities:
					for media in result.entities['media']:
						url = media['media_url_https']
						if url not in self.media_url_list:
							self.media_url_list.append(url)
							self.download_url_list.append(url)
			self.max_id = result.id
		except Exception as e:
			print("[-] Error: ", e)

	def download(self, url):
		url_orig = '%s:orig' % url
		filename = url.split('/')[-1]
		savepath = IMAGES_DIR+filename
		try:
			response = req.urlopen(url_orig).read()
			with open(savepath,"wb") as f:
				f.write(response)
		except Exception as e:
			print("[-] Error:",e)

def main():
	try:
		downloder = ImageDownloder()
		downloder.run()
	except KeyboardInterrupt:
		pass

if __name__ == '__main__':
	main()
