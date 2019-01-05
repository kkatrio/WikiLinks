import json
import twitter
from scrap_wikipedia import Wiki_scrapper
from post_update import print_tweet, get_last_link


filename = 'cred.json'
with open(filename) as f:
    data = json.load(f)

api = twitter.Api(consumer_key=data['consumer key'],
                  consumer_secret=data['consumer secret'],
                  access_token_key=data['access token key'],
                  access_token_secret=data['access token secret'])

scrapper = Wiki_scrapper()
last_page = get_last_link(scrapper, api)

try:
    content = scrapper.wiki_content(last_page)
    # print new
    print_tweet(content)
except AssertionError:
    print("Can't scrap wiki page")
