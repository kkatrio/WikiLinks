#!/usr/bin/env python

import json
import twitter
from scrap_wikipedia import Wiki_scrapper
from post_update import print_tweet, get_link


filename = 'cred.json'
with open(filename) as f:
    data = json.load(f)

api = twitter.Api(consumer_key=data['consumer key'],
                  consumer_secret=data['consumer secret'],
                  access_token_key=data['access token key'],
                  access_token_secret=data['access token secret'])

scrapper = Wiki_scrapper()
last_page = get_link(api, 0)

try:
    content = scrapper.wiki_content(last_page)
    if content is None:
        previous_page = get_link(api, 1) # previous
        print("previous page: ", previous_page)
        scrapper.reset()
        content = scrapper.wiki_content(previous_page)
        print_tweet(content)
    # print new
    print_tweet(content)
except AssertionError:
    print("Can't scrap wiki page")
